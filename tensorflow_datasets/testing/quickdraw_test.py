# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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
"""Tests for Quickdraw Sketch RNN data."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.sequence import quickdraw
import numpy as np
import os
import tensorflow as tf

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils


def _output_dir():
    return os.path.join(
        py_utils.tfds_dir(),
        "testing",
        "test_data",
        "fake_examples",
        "quickdraw_sketch_rnn",
    )


def _gen_stroke():
    delta_x = np.random.random_integers(-100, 100)
    delta_y = np.random.random_integers(-100, 100)
    pen_off = np.random.choice([0, 1])
    return np.array([delta_y, delta_x, pen_off], dtype=np.int16)


def _gen_sketch(max_strokes: int = 10):
    """Sketches are arrays of strokes."""
    return np.array(
        [_gen_stroke() for s in range(np.random.random_integers(max_strokes))]
    )


def _gen_file_content(sketches: int = 10):
    """Files ar arrays of sketches."""
    return np.array([_gen_sketch() for s in range(sketches)])


def _generate_dummies():
    dummy_strokes = {split: _gen_file_content() for split in ["train", "test", "valid"]}

    print(dummy_strokes["train"])
    print(dummy_strokes["train"].shape)
    np.savez(os.path.join(_output_dir(), "banana.npz"), **dummy_strokes)


def _unpack_dummies():
    download_dir = _output_dir()
    extract_dir = os.path.join(download_dir, "extracted")
    for path in tf.io.gfile.listdir(download_dir):
        if path == "extracted":
            continue
        data = np.load(os.path.join(download_dir, path))
        for split in ["train", "test", "valid"]:
            split_dir = os.path.join(extract_dir, split)
            if not tf.io.gfile.exists(split_dir):
                tf.io.gfile.makedirs(split_dir)
            np.save(os.path.join(split_dir, path.strip(".npz")), data[split])


class QuickdrawSketchRNNTest(testing.DatasetBuilderTestCase):

    DATASET_CLASS = quickdraw.QuickdrawSketchRNN
    SPLITS = {"train": 10, "test": 10, "validation": 10}
    DL_EXTRACT_RESULT = {"banana": "banana.npz"}


def main():
    _generate_dummies()
    _unpack_dummies()
    testing.test_main()


if __name__ == "__main__":
    main()
