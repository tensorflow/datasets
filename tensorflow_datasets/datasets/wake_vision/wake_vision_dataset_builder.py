# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""wake_vision dataset."""

from collections.abc import Sequence
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_TRAIN_IMAGE_IDS = [
    9270320,
    9270321,
    9270322,
    9270323,
    9270324,
    9270325,
    9270326,
    9270327,
    9270328,
    9270329,
    9270330,
    9270331,
    9270332,
    9270333,
    9270334,
    9270335,
    9270336,
    9270337,
    9270338,
    9270339,
    9270340,
    9270341,
    9270342,
    9270343,
    9270344,
    9270345,
    9270346,
    9270347,
    9270348,
    9270349,
    9270350,
    9270351,
    9270352,
    9270353,
    9270354,
    9270356,
    9270357,
    9270358,
    9270359,
    9270360,
    9270361,
    9270362,
    9270363,
    9270364,
    9270366,
    9270367,
    9270368,
    9270369,
    9270370,
    9270371,
    9270372,
    9270373,
    9270374,
    9270375,
    9270376,
    9270377,
    9270378,
    9270379,
    9270380,
    9270381,
    9270382,
    9270383,
    9270384,
    9270385,
    9270386,
    9270387,
    9270388,
    9270390,
    9270391,
    9270392,
    9270393,
    9270394,
    9270395,
    9270396,
    9270397,
    9270398,
    9270399,
    9270400,
    9270401,
    9270402,
    9270403,
    9270404,
    9270405,
    9270406,
    9270407,
    9270408,
    9270409,
    9270410,
    9270411,
    9270412,
]
_URL_TEMPLATE = (
    'https://dataverse.harvard.edu/api/access/datafile/{id}?format=original'
)
_IMAGE_URLS = {
    'train_images': [
        tfds.download.Resource(
            url=_URL_TEMPLATE.format(id=id),
            extract_method=tfds.download.ExtractMethod.GZIP,
        )
        for id in _TRAIN_IMAGE_IDS
    ],
    'validation_images': [
        tfds.download.Resource(
            url=_URL_TEMPLATE.format(id=9270355),
            extract_method=tfds.download.ExtractMethod.GZIP,
        )
    ],
    'test_images': [
        tfds.download.Resource(
            url=_URL_TEMPLATE.format(id=9270389),
            extract_method=tfds.download.ExtractMethod.GZIP,
        )
    ],
}
_METADATA_URLS = {
    'train_large_metadata': _URL_TEMPLATE.format(id=9844933),
    'train_quality_metadata': _URL_TEMPLATE.format(id=9844934),
    'validation_metadata': _URL_TEMPLATE.format(id=10243658),
    'test_metadata': _URL_TEMPLATE.format(id=10243659),
}

_DESCRIPTION = (
    'Wake Vision is a large, high-quality dataset featuring over 6 million'
    ' images, significantly exceeding the scale and diversity of current tinyML'
    ' datasets (100x). This dataset includes images with annotations of whether'
    ' each image contains aperson. Additionally, it incorporates a'
    ' comprehensive fine-grained benchmark to assess fairness and robustness,'
    ' covering perceived gender, perceived age, subject distance, lighting'
    ' conditions, and depictions. The Wake Vision labels are derived from Open'
    " Image's annotations which are licensed by Google LLC under CC BY 4.0"
    ' license. The images are listed as having a CC BY 2.0 license. Note from'
    ' Open Images: "while we tried to identify images that are licensed under a'
    ' Creative Commons Attribution license, we make no representations or'
    ' warranties regarding the license status of each image and you should'
    ' verify the license for each image yourself."'
)


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wake_vision dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': (
          'Initial TensorFlow Datasets release. Note that this is based on the'
          ' 2.0 version of Wake Vision on Harvard Dataverse.'
      ),
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(None, None, 3)),
            'filename': tfds.features.Text(),
            'person': tfds.features.ClassLabel(names=['No', 'Yes']),
            'depiction': tfds.features.ClassLabel(names=['No', 'Yes']),
            'body_part': tfds.features.ClassLabel(names=['No', 'Yes']),
            'predominantly_female': tfds.features.ClassLabel(
                names=['No', 'Yes']
            ),
            'predominantly_male': tfds.features.ClassLabel(names=['No', 'Yes']),
            'gender_unknown': tfds.features.ClassLabel(names=['No', 'Yes']),
            'young': tfds.features.ClassLabel(names=['No', 'Yes']),
            'middle_age': tfds.features.ClassLabel(names=['No', 'Yes']),
            'older': tfds.features.ClassLabel(names=['No', 'Yes']),
            'age_unknown': tfds.features.ClassLabel(names=['No', 'Yes']),
            'near': tfds.features.ClassLabel(names=['No', 'Yes']),
            'medium_distance': tfds.features.ClassLabel(names=['No', 'Yes']),
            'far': tfds.features.ClassLabel(names=['No', 'Yes']),
            'dark': tfds.features.ClassLabel(names=['No', 'Yes']),
            'normal_lighting': tfds.features.ClassLabel(names=['No', 'Yes']),
            'bright': tfds.features.ClassLabel(names=['No', 'Yes']),
            'person_depiction': tfds.features.ClassLabel(names=['No', 'Yes']),
            'non-person_depiction': tfds.features.ClassLabel(
                names=['No', 'Yes']
            ),
            'non-person_non-depiction': tfds.features.ClassLabel(
                names=['No', 'Yes']
            ),
        }),
        supervised_keys=('image', 'person'),
        homepage='https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2F1HOPXC',
        license='See homepage for license information.',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    metadata_paths = dl_manager.download_and_extract(_METADATA_URLS)
    image_paths = dl_manager.download_and_extract(_IMAGE_URLS)

    return {
        'train_large': self._generate_examples(
            image_paths['train_images'], metadata_paths['train_large_metadata']
        ),
        'train_quality': self._generate_examples(
            image_paths['train_images'],
            metadata_paths['train_quality_metadata'],
        ),
        'validation': self._generate_examples(
            image_paths['validation_images'],
            metadata_paths['validation_metadata'],
        ),
        'test': self._generate_examples(
            image_paths['test_images'], metadata_paths['test_metadata']
        ),
    }

  def _generate_examples(
      self, image_paths: Sequence[epath.Path], metadata_path: epath.Path
  ):
    """Yields examples."""
    metadata = tfds.core.lazy_imports.pandas.read_csv(
        metadata_path, index_col='filename'
    )

    for tar_file in image_paths:
      for sample_path, sample_object in tfds.download.iter_archive(
          tar_file, tfds.download.ExtractMethod.TAR_STREAM
      ):
        file_name = os.path.basename(sample_path)

        if file_name not in metadata.index:
          continue

        sample_metadata = metadata.loc[file_name]

        yield file_name, {
            'image': sample_object,
            'filename': file_name,
            'person': sample_metadata['person'],
            'depiction': sample_metadata.get('depiction', -1),
            'body_part': sample_metadata.get('body_part', -1),
            'predominantly_female': sample_metadata.get(
                'predominantly_female', -1
            ),
            'predominantly_male': sample_metadata.get('predominantly_male', -1),
            'gender_unknown': sample_metadata.get('gender_unknown', -1),
            'young': sample_metadata.get('young', -1),
            'middle_age': sample_metadata.get('middle_age', -1),
            'older': sample_metadata.get('older', -1),
            'age_unknown': sample_metadata.get('age_unknown', -1),
            'near': sample_metadata.get('near', -1),
            'medium_distance': sample_metadata.get('medium_distance', -1),
            'far': sample_metadata.get('far', -1),
            'dark': sample_metadata.get('dark', -1),
            'normal_lighting': sample_metadata.get('normal_lighting', -1),
            'bright': sample_metadata.get('bright', -1),
            'person_depiction': sample_metadata.get('person_depiction', -1),
            'non-person_depiction': sample_metadata.get(
                'non-person_depiction', -1
            ),
            'non-person_non-depiction': sample_metadata.get(
                'non-person_non-depiction', -1
            ),
        }
