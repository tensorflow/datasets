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

"""API defining dataset features (image, text, scalar,...).

See [the guide](https://www.tensorflow.org/datasets/features).

"""

from tensorflow_datasets.core.features.audio_feature import Audio
from tensorflow_datasets.core.features.bounding_boxes import BBox
from tensorflow_datasets.core.features.bounding_boxes import BBoxFeature
from tensorflow_datasets.core.features.class_label_feature import ClassLabel
from tensorflow_datasets.core.features.dataset_feature import Dataset
from tensorflow_datasets.core.features.feature import DocArg
from tensorflow_datasets.core.features.feature import Documentation
from tensorflow_datasets.core.features.feature import FeatureConnector
from tensorflow_datasets.core.features.feature import TensorInfo
from tensorflow_datasets.core.features.features_dict import FeaturesDict
from tensorflow_datasets.core.features.image_feature import Image
from tensorflow_datasets.core.features.labeled_image import LabeledImage
from tensorflow_datasets.core.features.scalar import Scalar
from tensorflow_datasets.core.features.sequence_feature import Sequence
from tensorflow_datasets.core.features.tensor_feature import Encoding
from tensorflow_datasets.core.features.tensor_feature import Tensor
from tensorflow_datasets.core.features.text_feature import Text
from tensorflow_datasets.core.features.translation_feature import Translation
from tensorflow_datasets.core.features.translation_feature import TranslationVariableLanguages
from tensorflow_datasets.core.features.video_feature import Video

__all__ = [
    "Audio",
    "BBox",
    "BBoxFeature",
    "ClassLabel",
    "Dataset",
    "DocArg",
    "Documentation",
    "Encoding",
    "FeatureConnector",
    "FeaturesDict",
    "LabeledImage",
    "Tensor",
    "TensorInfo",
    "Scalar",
    "Sequence",
    "Image",
    "Text",
    "Video",
]
