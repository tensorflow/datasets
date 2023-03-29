# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Translation feature that supports multiple languages."""

from __future__ import annotations

import collections.abc as collections_abc
from typing import Union

from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import features_dict
from tensorflow_datasets.core.features import sequence_feature
from tensorflow_datasets.core.features import text_feature
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import type_utils


Json = type_utils.Json


class Translation(features_dict.FeaturesDict):
  """`FeatureConnector` for translations with fixed languages per example.

  Input: The Translate feature accepts a dictionary for each example mapping
    string language codes to string translations.

  Output: A dictionary mapping string language codes to translations as `Text`
    features.

  Example:
  At construction time:

  ```
  tfds.features.Translation(languages=['en', 'fr', 'de'])
  ```

  During data generation:

  ```
  yield {
      'en': 'the cat',
      'fr': 'le chat',
      'de': 'die katze'
  }
  ```

  Tensor returned by `.as_dataset()`:

  ```
  {
      'en': tf.Tensor(shape=(), dtype=np.str_, numpy='the cat'),
      'fr': tf.Tensor(shape=(), dtype=np.str_, numpy='le chat'),
      'de': tf.Tensor(shape=(), dtype=np.str_, numpy='die katze'),
  }
  ```
  """

  def __init__(
      self,
      languages,
      encoder=None,
      encoder_config=None,
      *,
      doc: feature_lib.DocArg = None,
  ):
    """Constructs a Translation FeatureConnector.

    Args:
      languages: `list<string>` Full list of languages codes.
      encoder: `tfds.deprecated.text.TextEncoder` or
        list<tfds.deprecated.text.TextEncoder> (optional), an encoder that can
        convert text to integer. One can be shared one per language provided. If
        None, the text will be utf-8 byte-encoded.
      encoder_config: `tfds.deprecated.text.TextEncoderConfig` or
        `list<tfds.deprecated.text.TextEncoderConfig>` (optional), needed if
        restoring from a file with `load_metadata`. One config can be shared or
        one per language can be provided.
      doc: Documentation of this feature (e.g. description).
    """
    # If encoder and encoder_config aren't lists, use the same values for all
    # languages.
    self._encoder = encoder
    self._encoder_config = encoder_config
    if not isinstance(encoder, collections_abc.Iterable):
      encoder = [encoder] * len(languages)
    if not isinstance(encoder_config, collections_abc.Iterable):
      encoder_config = [encoder_config] * len(languages)

    super(Translation, self).__init__(
        feature_dict={
            lang: text_feature.Text(enc, enc_conf)
            for lang, enc, enc_conf in zip(languages, encoder, encoder_config)
        },
        doc=doc,
    )

  @property
  def languages(self):
    """List of languages."""
    return sorted(self.keys())

  @classmethod
  def from_json_content(
      cls, value: Union[Json, feature_pb2.TranslationFeature]
  ) -> "Translation":
    if isinstance(value, dict):
      if "use_encoder" in value:
        raise ValueError(
            "TFDS does not support datasets with Encoder. Please use the plain "
            "text version with `tensorflow_text`."
        )
      return cls(**value)
    assert not value.variable_languages_per_example
    return cls(languages=value.languages)

  def to_json_content(self) -> feature_pb2.TranslationFeature:  # pytype: disable=signature-mismatch  # overriding-return-type-checks
    if self._encoder or self._encoder_config:
      raise ValueError(
          "TFDS encoder are deprecated and will be removed soon. "
          "Please use `tensorflow_text` instead with the plain text dataset."
      )
    return feature_pb2.TranslationFeature(
        languages=self.languages, variable_languages_per_example=False
    )


class TranslationVariableLanguages(sequence_feature.Sequence):
  """`FeatureConnector` for translations with variable languages per example.

  Input: The TranslationVariableLanguages feature accepts a dictionary for each
    example mapping string language codes to one or more string translations.
    The languages present may vary from example to example.

  Output:
    language: variable-length 1D tf.Tensor of np.str_ language codes, sorted
      in ascending order.
    translation: variable-length 1D tf.Tensor of np.str_ plain text
      translations, sorted to align with language codes.

  Example (fixed language list):
  At construction time:

  ```
  tfds.features.Translation(languages=['en', 'fr', 'de'])
  ```

  During data generation:

  ```
  yield {
      'en': 'the cat',
      'fr': ['le chat', 'la chatte,']
      'de': 'die katze'
  }
  ```

  Tensor returned by `.as_dataset()`:

  ```
  {
      'language': tf.Tensor(
          shape=(4,), dtype=np.str_, numpy=array(['en', 'de', 'fr', 'fr']),
      'translation': tf.Tensor(
          shape=(4,), dtype=np.str_,
          numpy=array(['the cat', 'die katze', 'la chatte', 'le chat'])),
  }
  ```
  """

  def __init__(
      self,
      languages=None,
      *,
      doc: feature_lib.DocArg = None,
  ):
    """Constructs a Translation FeatureConnector.

    Args:
      languages: `list<string>` (optional), full list of language codes if known
        in advance.
      doc: Documentation of this feature (e.g. description).
    """
    # TODO(adarob): Add optional text encoders once `Sequence` adds support
    # for FixedVarLenFeatures.

    self._languages = set(languages) if languages else None
    super(TranslationVariableLanguages, self).__init__(
        feature={
            "language": text_feature.Text(),
            "translation": text_feature.Text(),
        },
        doc=doc,
    )

  @property
  def num_languages(self):
    """Number of languages or None, if not specified in advance."""
    return len(self._languages) if self._languages else None

  @property
  def languages(self):
    """List of languages or None, if not specified in advance."""
    return sorted(list(self._languages)) if self._languages else None

  def encode_example(self, translation_dict):
    if self.languages and set(translation_dict) - self._languages:
      raise ValueError(
          "Some languages in example ({0}) are not in valid set ({1}).".format(
              ", ".join(sorted(set(translation_dict) - self._languages)),
              ", ".join(self.languages),
          )
      )

    # Convert dictionary into tuples, splitting out cases where there are
    # multiple translations for a single language.
    translation_tuples = []
    for lang, text in translation_dict.items():
      if isinstance(text, str):
        translation_tuples.append((lang, text))
      else:
        translation_tuples.extend([(lang, el) for el in text])

    # Ensure translations are in ascending order by language code.
    languages, translations = zip(*sorted(translation_tuples))

    return super(TranslationVariableLanguages, self).encode_example(
        {"language": languages, "translation": translations}
    )

  @classmethod
  def from_json_content(
      cls, value: Union[Json, feature_pb2.TranslationFeature]
  ) -> "TranslationVariableLanguages":
    if isinstance(value, dict):
      return cls(**value)
    assert value.variable_languages_per_example
    return cls(languages=value.languages)

  def to_json_content(self) -> feature_pb2.TranslationFeature:  # pytype: disable=signature-mismatch  # overriding-return-type-checks
    return feature_pb2.TranslationFeature(
        languages=self.languages, variable_languages_per_example=True
    )
