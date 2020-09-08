  
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
"""covid_cxr dataset."""

import tensorflow_datasets.public_api as tfds
import os

# TODO(covid_cxr): BibTeX citation
_CITATION = """Wang, Linda, et al. COVID-Net: A Tailored Deep Convolutional Neural Network ... 2020, arxiv.org/pdf/2003.09871.pdf. 
"""

# TODO(covid_cxr):
_DESCRIPTION = """Dataset with radiography images belonging to three different classes 
                    - normal
                    - pneumonia
                    - COVID - 19
                    
"""

_TRAIN_URL = 'https://drive.google.com/uc?export=download&id=1FE57dEo6xKK9goxd8trERz_Y_vdP3GCX'
_TEST_URL = 'https://drive.google.com/uc?export=download&id=12sq9rO5nSgl-fmWD2KtHocU2xUyX38qP'

_IMAGE_SHAPE = (512, 512, 3)

class CovidCxr(tfds.core.GeneratorBasedBuilder):
  """TODO(covid_cxr): Short description of my dataset."""

  # TODO(covid_cxr): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(covid_cxr): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE, dtype='uint8', encoding_format='png'),
            "label": tfds.features.ClassLabel(
                names=["COVID-19", "normal", "pneumonia"]),
            # These are the features of your dataset like images, labels ...
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('image', 'label'),
        # Homepage of the dataset for documentation
        homepage='https://github.com/lindawangg/COVID-Net',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(covid_cxr): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    
    train_path, test_path = dl_manager.download([_TRAIN_URL, _TEST_URL])
        
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": dl_manager.iter_archive(train_path),
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": dl_manager.iter_archive(test_path),
            }),
    ]

  def _generate_examples(self, archive):
    """Yields examples."""
    # TODO(covid_cxr): Yields (key, example) tuples from the dataset
    for fname, fobj in archive:
            image_dir, image_file = os.path.split(fname)
            d = os.path.basename(image_dir)
            record = {"image": fobj, "label": d}
            yield "%s/%s" % (image_file, d), record

