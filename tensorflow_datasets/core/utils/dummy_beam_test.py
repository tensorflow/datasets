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

# Lint as: python3
"""Test for dummy_beam."""

import tensorflow_datasets as tfds
from tensorflow_datasets.core.utils import dummy_beam


class DummyBeamTest(tfds.testing.TestCase): # pylint: disable=too-few-public-methods
    """Testing class for dummy_beam."""

    def test_dummy_beam(self):
        """Test for DummyBeam."""
        _err_msg = ("Failed importing apache_beam."
                    " Please install apache_beam. Using pip install apache_beam")
        try:
            import apache_beam as beam
        except ImportError:
            beam = dummy_beam.DummyBeam()
        with self.assertRaisesWithPredicateMatch(ImportError, _err_msg):
            beam = dummy_beam.DummyBeam()

            class SomeFn(beam.DoFn): # pylint: disable=unused-variable, too-few-public-methods
                """Empty class for test beam Wrapper"""
                pass # pylint: disable=unnecessary-pass

if __name__ == '__main__':
    tfds.testing.test_main()
