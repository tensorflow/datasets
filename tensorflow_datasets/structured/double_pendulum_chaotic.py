# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Double Pendulum dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import glob
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DOUBLE_PENDULUM_URL = "https://s3.us-south.cloud-object-storage.appdomain.cloud/dax-assets-dev/dax-double-pendulum-chaotic/2.0.1/double-pendulum-chaotic.tar.gz"
_REL_CSV_PATH = "original/dpc_dataset_csv/"

_CITATION = """\
@InProceedings{asseman2018learning,
title={Learning beyond simulated physics},
author={Asseman, Alexis and Kornuta, Tomasz and Ozcan, Ahmet},
year={2018}
maintitle={Neural Information Processing Systems},
booktitle={Modeling and Decision-making in the Spatiotemporal Domain Workshop},
url={https://openreview.net/forum?id=HylajWsRF7},
}
"""

_DESCRIPTION = """\
A double pendulum is a pendulum with another pendulum attached to its end.
Despite being a simple physical system, it exhibits a rich dynamic behavior with
a strong sensitivity to initial conditions and noises in the environment (motion
of the air in the room, sound vibrations, vibration of the table due to coupling
with the pendulum etc.). Those influences at any given time will affect future
trajectory in a way that is increasingly significant with time, making it a
chaotic system.

Videos of the double pendulum were taken using a high-speed Phantom Miro EX2
camera. The camera’s fast global shutter enabled us to take non-distorted
frames, with a short exposure time to avoid any motion blur. To make the
extraction of the arm positions easier, a matte black background was used, and
the three datums were marked with red, green and blue fiducial markers. The
markers were printed so that their diameter matches exactly that of the pendulum
datums, which made their alignment easier. A powerful LED floodlight with a
custom DC power supply (to avoid flicker) was used to illuminate the pendulum,
to compensate for the short frame exposure time. The camera was placed at 2
meters from the pendulum, with the axis of the objective aligned with the first
pendulum datum. The pendulum was launched by hand, and the camera was motion
triggered. Our dataset was generated on the basis of 21 individual runs of the
pendulum. Each of the recorded sequences lasted around 40s and consisted of
around 17500 frames.

We implemented the program to extract the positions of the markers obtained from
the video. The video frames were first upscaled 5 times to easily take advantage
of subpixel positional resolution. We used scikit-image to draw the fiducial
markers templates. These templates were used with the OpenCV cross-correlation
algorithm to find the best matches on a per frame basis. The found matching
markers were finally distinguished on the basis of their color.

The proposed challenge is to predict the next 200 consecutive time-steps on the
basis of the past 4 consecutive time-steps. For that purpose we have
preprocessed the original 21 sequences in a way described below.

We extracted 5% of the data as “validation and test sets”, in such a way
that those sequences were homogeneously spread over the data and the runtime of
the pendulum runs. In order to avoid strong correlations between the training
and the validation/test sets, we discarded 200 time-steps before and after each
of the extracted sequence. That resulted in 123 non-overlapping sequences: 39
training sequences of varying length (from 637 to 16850 time-steps) and 84
validation/test sequences of 204 time-steps each. In the latter case the first 4
steps represent the inputs (i), and the next 200 steps correspond to the targets
(t). Finally, we randomized the order of all files.

We supplement the original images with two additional representations: marker
positions and arm angles. Marker positions are three pairs (x,y) representing
image coordinates of all three markers (each value is multiplied by 5). Arm
angles are sines and cosines of two angles α and β, where α is the angle
between the horizontal image line pointing right and the the first arm, whereas
β is the angle between the first and second arm.

It is worth noting that one might combine and use different representations for
inputs and targets/predictions, what regulates the difficulty of the challenge.
In particular, using raw images as both inputs and targets seems to be the most
complex task, whereas utilization of arm angles as inputs and targets reduces
the task into classic multiple-input multiple-output time-series prediction.
"""


class DoublePendulumChaotic(tfds.core.GeneratorBasedBuilder):
  """Double Pendulum Chaotic dataset."""
  VERSION = tfds.core.Version("1.0.0",
                              experiments={tfds.core.Experiment.S3: False})

  SUPPORTED_VERSIONS = [
      tfds.core.Version(
          "2.0.0", "New split API (https://tensorflow.org/datasets/splits)"),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "input_sequence":
                tfds.features.Tensor(shape=(None, 6), dtype=tf.float64),
            "output_sequence":
                tfds.features.Tensor(shape=(None, 6), dtype=tf.float64),
        }),
        supervised_keys=("input_sequence", "output_sequence"),
        urls=["https://developer.ibm.com/exchanges/data/all/double-pendulum-chaotic/"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    dp_files = dl_manager.download_and_extract(_DOUBLE_PENDULUM_URL)
    # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs={"dp_files": dp_files}),
    ]

  def _generate_examples(self, dp_files, input_size=4, output_size=1):
    csv_files_path = dp_files+_REL_CSV_PATH
    for file_path in glob.glob(csv_files_path):
      with tf.io.gfile.GFile(file_path) as f:
        raw_data = csv.reader(f, quote=csv.QUOTE_NONNUMERIC)
        for i, _ in enumerate(raw_data):
          raw_data.seek(i)
          yield i, {
            "input_sequence" : tf.convert_to_tensor([next(raw_data) for _ in range(input_size)]),
            "output_sequence" : tf.convert_to_tensor([next(raw_data) for _ in range(output_size)])
          }