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

"""Malaria Infected Human Blood Smears Dataset"""

import json
import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds


_CITATION = """\
@misc{BBBC041v1,
	author = "Ljosa, Vebjorn and Sokolnicki, Katherine L. and Carpenter, Anne E.",
  year = "2012",
	title = "Annotated high-throughput microscopy image sets for validation",
	url = "https://data.broadinstitute.org/bbbc/BBBC041/"}
"""

_DESCRIPTION = """\
The data consists of two classes of uninfected cells (RBCs and leukocytes) and 
four classes of infected cells (gametocytes, rings, trophozoites, and schizonts). Annotators 
were permitted to mark some cells as difficult if not clearly in one of the cell classes. 
The data had a heavy imbalance towards uninfected RBCs versus uninfected leukocytes and 
infected cells, making up over 95% of all cells.
A class label and set of bounding box coordinates were given for each cell. 
For all data sets, infected cells were given a class label by Stefanie Lopes, 
malaria researcher at the Dr. Heitor Vieira Dourado Tropical Medicine Foundation 
hospital, indicating stage of development or marked as difficult.
"""

_URL = "https://data.broadinstitute.org/bbbc/BBBC041/malaria.zip"
_LABELS = (
    'red blood cell',
    'leukocyte',
    'gametocyte',
    'ring',
    'trophozoite',
    'schizont',
    'difficult',
)

def _generate_example_objects(data_dict):
  """Function to get all the objects from the json file."""
  height = data_dict['image']['shape']['r']
  width = data_dict['image']['shape']['c']

  objects = data_dict['objects']

  for obj in objects:
    ymin = obj['bounding_box']['minimum']['r']
    xmin = obj['bounding_box']['minimum']['c']

    ymax = obj['bounding_box']['maximum']['r']
    xmax = obj['bounding_box']['maximum']['c']

    label = obj['category']

    bbox = tfds.features.BBox(
        ymin / height, xmin / width, ymax / height, xmax / width
    )

    yield {
        "bbox": bbox,
        "label": label,
    }

class MalariaInfectedSmears(tfds.core.GeneratorBasedBuilder):
  """Malaria Infected Human Blood Smears Dataset"""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "pathname": tfds.features.Text(),
            "objects": tfds.features.Sequence({
                "bbox": tfds.features.BBoxFeature(),
                "label": tfds.features.ClassLabel(names=_LABELS)
            })
        }),
        # Homepage of the dataset for documentation
        homepage='https://data.broadinstitute.org/bbbc/BBBC041/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_URL)
    path = os.path.join(path, "malaria")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "path": path,
                "data": "training.json"
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "path": path,
                "data": "test.json"
            },
        ),
    ]

  def _generate_examples(self, path, data):
    """Yields examples."""
    with tf.io.gfile.GFile(os.path.join(path, data), "r") as f:
      data = json.load(f)

      for i, val in enumerate(data):
        image_path = val['image']['pathname'][1:]
        image = os.path.join(path, image_path)
        objects = list(_generate_example_objects(val))

        yield i, {
            "image": image,
            "pathname": image_path,
            "objects": objects,
        }
