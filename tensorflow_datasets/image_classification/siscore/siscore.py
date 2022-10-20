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

"""SI-SCORE synthetic dataset."""

import dataclasses
import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.image_classification.siscore import siscore_labels
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@misc{djolonga2020robustness,
      title={On Robustness and Transferability of Convolutional Neural Networks},
      author={Josip Djolonga and Jessica Yung and Michael Tschannen and Rob Romijnders and Lucas Beyer and Alexander Kolesnikov and Joan Puigcerver and Matthias Minderer and Alexander D'Amour and Dan Moldovan and Sylvain Gelly and Neil Houlsby and Xiaohua Zhai and Mario Lucic},
      year={2020},
      eprint={2007.08558},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
"""

_DESCRIPTION = """
SI-Score (Synthetic Interventions on Scenes for Robustness Evaluation) is a
dataset to evaluate robustness of image classification models to changes in
object size, location and rotation angle.

In SI-SCORE, we take objects and backgrounds and systematically vary object
size, location and rotation angle so we can study the effect of changing these
factors on model performance. The image label space is the ImageNet
label space (1k classes) for easy evaluation of models.

More information about the dataset can be found at https://github.com/google-research/si-score.
"""

_NUM_CLASSES = 61

_BASE_URL = "https://s3.us-east-1.amazonaws.com/si-score-dataset"

_VARIANT_EXPANDED_DIR_NAMES = {
    "size": "area",
    "rotation": "rotation",
    "location": "location20_area02_min0pc",
}


@dataclasses.dataclass
class SiscoreConfig(tfds.core.BuilderConfig):
  """BuilderConfig for SI-Score.

  Attributes:
      variant: str. The synthetic dataset variant. One of 'rotation', 'size' and
        'location'.
      name: str. The name of the factor to vary (same as variant).
      description: str. A brief description of the config (different from the
        global dataset description).
  """
  variant: str = ""


class Siscore(tfds.core.GeneratorBasedBuilder):
  """SI-Score synthetic image dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  BUILDER_CONFIGS = [
      SiscoreConfig(variant=x, name=x, description=f"factor of variation: {x}")
      for x in ["rotation", "size", "location"]  # pytype: disable=wrong-keyword-args
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        features=tfds.features.FeaturesDict({
            "image_id":
                tf.int64,
            "image":
                tfds.features.Image(),
            # ImageNet label space
            "label":
                tfds.features.ClassLabel(num_classes=1000),
            "dataset_label":
                tfds.features.ClassLabel(
                    names=siscore_labels.IMAGENET_LABELS_LIST),
        }),
        supervised_keys=("image", "label"),
        # Homepage of the dataset for documentation
        homepage="https://github.com/google-research/si-score",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerator."""
    # using rotation link only for now
    variant = self.builder_config.variant
    dataset_url = "/".join((_BASE_URL, f"{variant}.zip"))
    path = dl_manager.download_and_extract(dataset_url)
    path = os.path.join(path, _VARIANT_EXPANDED_DIR_NAMES[variant])
    return {"test": self._generate_examples(datapath=path)}

  def _generate_examples(self, datapath):
    """Yields examples of synthetic data images and labels."""
    for fpath in tf.io.gfile.glob(os.path.join(datapath, "*", "*.jpg")):
      label = fpath.split("/")[-2]
      fname = os.path.basename(fpath)
      record = {
          "image": fpath,
          "image_id": int(fname.split(".")[0]),
          "label": siscore_labels.IMAGENET_LABELS[label],
          "dataset_label": siscore_labels.DATASET_LABELS[label],
      }
      yield fname, record
