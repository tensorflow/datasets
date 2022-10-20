# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Cassava leaf dataset with images of health and diseased leaves."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@misc{mwebaze2019icassava,
    title={iCassava 2019Fine-Grained Visual Categorization Challenge},
    author={Ernest Mwebaze and Timnit Gebru and Andrea Frome and Solomon Nsumba and Jeremy Tusubira},
    year={2019},
    eprint={1908.02900},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
"""

_DESCRIPTION = """\
Cassava consists of leaf images for the cassava plant depicting healthy and
four (4) disease conditions; Cassava Mosaic Disease (CMD), Cassava Bacterial
Blight (CBB), Cassava Greem Mite (CGM) and Cassava Brown Streak Disease (CBSD).
Dataset consists of a total of 9430 labelled images.
The 9430 labelled images are split into a training set (5656), a test set(1885)
and a validation set (1889). The number of images per class are unbalanced with
the two disease classes CMD and CBSD having 72% of the images.
"""

_BASE_URL = "https://storage.googleapis.com/emcassavadata/cassavaleafdata.zip"
_LABELS = ["cbb", "cbsd", "cgm", "cmd", "healthy"]


class Cassava(tfds.core.GeneratorBasedBuilder):
  """Cassava leaf image dataset."""

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "image/filename": tfds.features.Text(),  # test-cbb-0.jpg
            "label": tfds.features.ClassLabel(names=_LABELS)
        }),
        supervised_keys=("image", "label"),
        homepage="https://www.kaggle.com/c/cassava-disease/overview",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_BASE_URL)
    train_path = os.path.join(path, "cassavaleafdata/train")
    test_path = os.path.join(path, "cassavaleafdata/test")
    validation_path = os.path.join(path, "cassavaleafdata/validation")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"datapath": train_path},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"datapath": test_path},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"datapath": validation_path},
        ),
    ]

  def _generate_examples(self, datapath):
    """Yields examples of cassava leaf images and labels."""
    for label in tf.io.gfile.listdir(datapath):
      for fpath in tf.io.gfile.glob(os.path.join(datapath, label, "*.jpg")):
        fname = os.path.basename(fpath)
        record = {
            "image": fpath,
            "image/filename": fname,
            "label": label,
        }
        yield fname, record
