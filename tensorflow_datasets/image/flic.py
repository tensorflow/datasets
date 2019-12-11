"""Frames Labeled In Cinema (FLIC)"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import scipy.io

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """@inproceedings{modec13,
    title={MODEC: Multimodal Decomposable Models for Human Pose Estimation},
    author={Sapp, Benjamin and Taskar, Ben},
    booktitle={In Proc. CVPR},
    year={2013},
  }
"""

_DESCRIPTION = """
From the paper: We collected a 5003 image dataset automatically from popular
Hollywood movies. The images were obtained by running a state-of-the-art person
detector on every tenth frame of 30 movies. People detected with high confidence
(roughly 20K candidates) were then sent to the crowdsourcing marketplace Amazon
Mechanical Turk to obtain groundtruthlabeling. Each image was annotated by five
Turkers for $0.01 each to label 10 upperbody joints. The median-of-five labeling
was taken in each image to be robust to outlier annotation. Finally, images were
rejected manually by us if the person was occluded or severely non-frontal. We
set aside 20% (1016 images) of the data for testing. 
"""

_URL = "https://drive.google.com/uc?id=0B4K3PZp8xXDJN0Fpb0piVjQ3Y3M&export=download"

class Flic(tfds.core.GeneratorBasedBuilder):
  """Frames Labeled In Cinema (FLIC)"""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "poselet_hit_idx": tfds.features.Sequence(tf.uint16),
            "moviename": tfds.features.Text(),
            "xcoords": tfds.features.Sequence(tf.float64),
            "ycoords": tfds.features.Sequence(tf.float64),
            "filepath": tfds.features.Text(),
            "imgdims": tfds.features.Tensor(shape=(3,), dtype=tf.float64),
            "currframe": tfds.features.Tensor(shape=(), dtype=tf.float64),
            "torsobox": tfds.features.Tensor(shape=(4,), dtype=tf.float32),
        }),
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extract_path = dl_manager.download_and_extract(_URL)
    data = scipy.io.loadmat(os.path.join(extract_path, "FLIC", "examples.mat"),
                                       struct_as_record=True, squeeze_me=True,
                                       mat_dtype=True)

    train_list = []
    test_list = []

    for i in range(len(data["examples"])):
      if data["examples"][i][7]:
        train_list.append(i)
      elif data["examples"][i][8]:
        test_list.append(i)

    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.TRAIN,
        gen_kwargs={
          "extract_path": extract_path,
          "data": data,
          "split": train_list,
        },
      ),
      tfds.core.SplitGenerator(
        name=tfds.Split.TEST,
        gen_kwargs={
          "extract_path": extract_path,
          "data": data,
          "split": test_list,
        },
      ),
    ]

  def _generate_examples(self, extract_path, data, split):
    """Yields examples."""
    for index in split:
      yield index, {
        "image": os.path.join(extract_path, "FLIC", "images", data["examples"][index][3]),
        "poselet_hit_idx": list(data["examples"][index][0]),
        "moviename": data["examples"][index][1],
        "xcoords": data["examples"][index][2][0],
        "ycoords": data["examples"][index][2][1],
        "filepath": data["examples"][index][3],
        "imgdims": data["examples"][index][4],
        "currframe": data["examples"][index][5],
        "torsobox": data["examples"][index][6],
      }