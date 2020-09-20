# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""Frames Labeled In Cinema (FLIC)."""

import os

import tensorflow.compat.v2 as tf
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

_DATA_OPTIONS = ["small", "full"]

_HOMEPAGE_URL = "https://bensapp.github.io/flic-dataset.html"

_URL_SUBSET = "https://drive.google.com/uc?id=0B4K3PZp8xXDJN0Fpb0piVjQ3Y3M&export=download"
_URL_SUPERSET = "https://drive.google.com/uc?id=0B4K3PZp8xXDJd2VwblhhOVBfMDg&export=download"


def _normalize_bbox(raw_bbox, img_path):
  """Normalize torsobox bbox values."""
  with tf.io.gfile.GFile(img_path, "rb") as fp:
    img = tfds.core.lazy_imports.PIL_Image.open(fp)
    width, height = img.size

  return tfds.features.BBox(
      ymin=raw_bbox[1] / height,
      ymax=raw_bbox[3] / height,
      xmin=raw_bbox[0] / width,
      xmax=raw_bbox[2] / width,
  )


class FlicConfig(tfds.core.BuilderConfig):
  """BuilderConfig for FLIC."""

  def __init__(self, *, data, **kwargs):
    """Constructs a FlicConfig."""
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)

    descriptions = {
        "small": "5003 examples used in CVPR13 MODEC paper.",
        "full":
            "20928 examples, a superset of FLIC consisting of more difficult "
            "examples."
    }
    description = kwargs.get("description", "Uses %s" % descriptions[data])
    kwargs["description"] = description

    super(FlicConfig, self).__init__(**kwargs)
    self.data = data
    self.url = _URL_SUBSET if data == "small" else _URL_SUPERSET
    self.dir = "FLIC" if data == "small" else "FLIC-full"


def _make_builder_configs():
  configs = []
  for data in _DATA_OPTIONS:
    configs.append(
        FlicConfig(name=data, version=tfds.core.Version("2.0.0"), data=data))
  return configs


class Flic(tfds.core.GeneratorBasedBuilder):
  """Frames Labeled In Cinema (FLIC)."""

  BUILDER_CONFIGS = _make_builder_configs()

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(
                    shape=(480, 720, 3), encoding_format="jpeg"),
            "poselet_hit_idx":
                tfds.features.Sequence(tf.uint16),
            "moviename":
                tfds.features.Text(),
            "xcoords":
                tfds.features.Sequence(tf.float64),
            "ycoords":
                tfds.features.Sequence(tf.float64),
            "currframe":
                tfds.features.Tensor(shape=(), dtype=tf.float64),
            "torsobox":
                tfds.features.BBoxFeature(),
        }),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extract_path = dl_manager.download_and_extract(self.builder_config.url)

    mat_path = os.path.join(extract_path, self.builder_config.dir,
                            "examples.mat")
    with tf.io.gfile.GFile(mat_path, "rb") as f:
      data = tfds.core.lazy_imports.scipy.io.loadmat(
          f, struct_as_record=True, squeeze_me=True, mat_dtype=True)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "extract_path": extract_path,
                "data": data,
                "selection_column": 7,  # indicates train split selection
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "extract_path": extract_path,
                "data": data,
                "selection_column": 8,  # indicates test split selection
            },
        ),
    ]

  def _generate_examples(self, extract_path, data, selection_column):
    """Yields examples."""
    for u_id, example in enumerate(data["examples"]):
      if example[selection_column]:
        img_path = os.path.join(extract_path, self.builder_config.dir, "images",
                                example[3])
        yield u_id, {
            "image": img_path,
            "poselet_hit_idx": example[0],
            "moviename": example[1],
            "xcoords": example[2][0],
            "ycoords": example[2][1],
            "currframe": example[5],
            "torsobox": _normalize_bbox(example[6], img_path),
        }
