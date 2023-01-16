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

"""ImageNet-Sketch dataset."""

from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
import tensorflow_datasets.public_api as tfds

_BASE_URL = 'https://github.com/HaohanWang/ImageNet-Sketch'
_IMAGENET_SKETCH_URL = 'https://drive.google.com/u/0/uc?id=1Mj0i5HBthqH1p_yeXzsg22gZduvgoNeA&export=download'


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for imagenet_sketch dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    imagenet_names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
            'label': tfds.features.ClassLabel(names_file=imagenet_names_file),
            'file_name': tfds.features.Text(),
        }),
        supervised_keys=('image', 'label'),
        homepage=_BASE_URL,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download(_IMAGENET_SKETCH_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'archive': dl_manager.iter_archive(path),
            },
        ),
    ]

  def _generate_examples(self, archive):
    """Generate images and labels for splits."""
    for fname, fobj in archive:
      assert fname.startswith('sketch/') and fname.endswith('.JPEG')
      fname = fname[len('sketch/') :]
      yield fname, {'image': fobj, 'file_name': fname, 'label': fname[:9]}
