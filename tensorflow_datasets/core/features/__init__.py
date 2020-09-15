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

"""API defining dataset features (image, text, scalar,...).

FeatureConnector is a way of abstracting what data is returned by the
tensorflow/datasets builders from how they are encoded/decoded from file.

## Using `tfds.features.FeatureConnector` in `tfds.core.GeneratorBasedBuilder`

To implement a new dataset:

* In `tfds.core.DatasetInfo`: Define the features structure:

```py
tfds.core.DatasetInfo(
    features=tfds.features.FeaturesDict({
        'input': tfds.features.Image(shape=(28, 28, 1)),
        'target': tfds.features.ClassLabel(names=['no', 'yes']),
        'extra_data': {
            'label_id': tf.int64,
            'language': tf.string,
        }
    })
)
```

* In `tfds.core.GeneratorBasedBuilder._generate_examples`: Examples should be
  yield to match the structure defined in `tfds.core.DatasetInfo`. Values
  are automatically encoded.

```py
yield {
    'input': '/path/to/img0.png',  # `np.array`, bytes file object also accepted
    'target': 'yes',  # Converted to int id 1
    'extra_data': {
        'label_id': 43,
        'language': 'en',
    }
}
```

* `tfds.load` will automatically returns `tf.data.Dataset` matching the `dict`
  structure defined in `tfds.core.DatasetInfo`:

```py
ds = tfds.load(...)
ds.element_spec == {
    'input': tf.TensorSpec(shape=(28, 28, 1), tf.uint8),
    'target': tf.TensorSpec(shape=(), tf.int64),
    'extra_data': {
        'label_id': tf.TensorSpec(shape=(), tf.int64),
        'language': tf.TensorSpec(shape=(), tf.string),
    },
}
```

## Create your own `tfds.features.FeatureConnector`

To create your own feature connector, you need to inherit from
`tfds.features.FeatureConnector` and implement the abstract methods.

* If your feature is a single tensor, it's best to inherit from
  `tfds.feature.Tensor` and use `super()` when needed. See
  `tfds.features.BBoxFeature` source code for an example.

* If your feature is a container of multiple tensors, it's best to inherit from
  `tfds.feature.FeaturesDict` and use the `super()` to automatically encode
  sub-connectors.

"""

from tensorflow_datasets.core.features.audio_feature import Audio
from tensorflow_datasets.core.features.bounding_boxes import BBox
from tensorflow_datasets.core.features.bounding_boxes import BBoxFeature
from tensorflow_datasets.core.features.class_label_feature import ClassLabel
from tensorflow_datasets.core.features.feature import FeatureConnector
from tensorflow_datasets.core.features.feature import Tensor
from tensorflow_datasets.core.features.feature import TensorInfo
from tensorflow_datasets.core.features.features_dict import FeaturesDict
from tensorflow_datasets.core.features.image_feature import Image
from tensorflow_datasets.core.features.sequence_feature import Sequence
from tensorflow_datasets.core.features.text_feature import Text
from tensorflow_datasets.core.features.translation_feature import Translation
from tensorflow_datasets.core.features.translation_feature import TranslationVariableLanguages
from tensorflow_datasets.core.features.video_feature import Video

__all__ = [
    "Audio",
    "BBox",
    "BBoxFeature",
    "ClassLabel",
    "FeatureConnector",
    "FeaturesDict",
    "Tensor",
    "TensorInfo",
    "Sequence",
    "Image",
    "Text",
    "Video",
]
