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

# coding=utf-8
"""Tests for tensorflow_datasets.core.features.text_feature."""

import tensorflow.compat.v2 as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features

tf.enable_v2_behavior()

DE_HELLO = "hallo "
EN_HELLO = "hello "
FR_HELLO = "bonjour "
ZH_HELLO = "你好 "

DE_B = tf.compat.as_bytes("de")
EN_B = tf.compat.as_bytes("en")
FR_B = tf.compat.as_bytes("fr")
ZH_B = tf.compat.as_bytes("zh")


class TranslationFeatureTest(testing.FeatureExpectationsTestCase):

  def test_translation(self):
    self.assertFeature(
        feature=features.Translation(["en", "zh"]),
        shape={"en": (), "zh": ()},
        dtype={"en": tf.string, "zh": tf.string},
        tests=[
            testing.FeatureExpectationItem(
                value={"en": EN_HELLO, "zh": ZH_HELLO},
                expected={"en": tf.compat.as_bytes(EN_HELLO),
                          "zh": tf.compat.as_bytes(ZH_HELLO)}
            ),
        ],
    )


class TranslationVariableLanguagesFeatureTest(
    testing.FeatureExpectationsTestCase):

  def test_translation_variable_languages_nolist(self):
    self.assertFeature(
        feature=features.TranslationVariableLanguages(),
        shape={"language": (None,), "translation": (None,)},
        dtype={"language": tf.string, "translation": tf.string},
        tests=[
            testing.FeatureExpectationItem(
                value={"en": EN_HELLO, "zh": ZH_HELLO},
                expected={"language": [EN_B, ZH_B],
                          "translation": [tf.compat.as_bytes(EN_HELLO),
                                          tf.compat.as_bytes(ZH_HELLO)]}
            ),
            testing.FeatureExpectationItem(
                value={"fr": FR_HELLO, "de": DE_HELLO, "zh": ZH_HELLO},
                expected={"language": [DE_B, FR_B, ZH_B],
                          "translation": [tf.compat.as_bytes(DE_HELLO),
                                          tf.compat.as_bytes(FR_HELLO),
                                          tf.compat.as_bytes(ZH_HELLO)]}
            ),
            testing.FeatureExpectationItem(
                value={"fr": [FR_HELLO, FR_HELLO[0:-1]],
                       "en": EN_HELLO},
                expected={"language": [EN_B, FR_B, FR_B],
                          "translation": [tf.compat.as_bytes(EN_HELLO),
                                          tf.compat.as_bytes(FR_HELLO[0:-1]),
                                          tf.compat.as_bytes(FR_HELLO)]}
            ),
        ],
    )

  def test_translation_variable_languages_list(self):
    self.assertFeature(
        feature=features.TranslationVariableLanguages(
            languages=["en", "de", "zh"]),
        shape={"language": (None,), "translation": (None,)},
        dtype={"language": tf.string, "translation": tf.string},
        tests=[
            testing.FeatureExpectationItem(
                value={"en": EN_HELLO, "zh": ZH_HELLO},
                expected={"language": [EN_B, ZH_B],
                          "translation": [tf.compat.as_bytes(EN_HELLO),
                                          tf.compat.as_bytes(ZH_HELLO)]}
            ),
            testing.FeatureExpectationItem(
                value={"fr": FR_HELLO, "de": DE_HELLO, "zh": ZH_HELLO},
                raise_cls=ValueError,
                raise_msg="Some languages in example (fr) are not in valid set "
                          "(de, en, zh)",
            ),
        ],
    )

if __name__ == "__main__":
  testing.test_main()
