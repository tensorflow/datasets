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
"""QuickDraw dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import tqdm

# Shared constants
_QUICKDRAW_BASE_URL = (
    "https://storage.googleapis.com/quickdraw_dataset"
)  # pylint: disable=line-too-long
_QUICKDRAW_LABELS_FNAME = "sequence/quickdraw_labels.txt"

_CITATION = """\
@misc{1704.03477,
Author = {David Ha and Douglas Eck},
Title = {A Neural Representation of Sketch Drawings},
Year = {2017},
Eprint = {arXiv:1704.03477},
}
"""


class QuickdrawSketchRNN(tfds.core.GeneratorBasedBuilder):
    """Quickdraw sequence of strokes dataset used for Sketch RNN.

    This is the version of the QuickDraw data used to train the SketchRNN model.
    """

    VERSION = tfds.core.Version("1.0.0")

    def _info(self):
        labels_path = tfds.core.get_tfds_path(_QUICKDRAW_LABELS_FNAME)
        return tfds.core.DatasetInfo(
            builder=self,
            description=("In this dataset, 75K samples (70K Training, "
                         "2.5K Validation, 2.5K Test) has been randomly "
                         "selected from each category, "
                         "processed with RDP line simplification "
                         "with an epsilon parameter of 2.0. "
                         "Each category will be stored in its "
                         "own .npz file, for example, cat.npz."),
            features=tfds.features.FeaturesDict({
                "sketch":
                tfds.features.FeaturesDict({
                    "stroke_3":
                    tfds.features.Tensor(shape=(None, 3), dtype=tf.int16),
                    "stroke_5":
                    tfds.features.Tensor(shape=(None, 5), dtype=tf.int16),
                }),
                "label":
                tfds.features.ClassLabel(names_file=labels_path),
            }),
            supervised_keys=("sketch", "label"),
            urls=["https://github.com/googlecreativelab/quickdraw-dataset"],
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        # The QuickDraw bitmap repository is structured as one .npz file per label
        # containing the three splits.
        labels = self.info.features["label"].names
        urls = {
            label: "{}/sketchrnn/{}.npz".format(_QUICKDRAW_BASE_URL, label)
            for label in labels
        }

        file_paths = dl_manager.download(urls)

        # Prepare the destinations used to unpack the split
        extract_dir = dl_manager._extract_dir
        for label in tqdm.tqdm(
                file_paths, desc="Unpacking downloaded archives."):
            data = np.load(file_paths[label], encoding="latin1")
            for split in ["train", "test", "valid"]:
                split_dir = os.path.join(extract_dir, split)
                if not tf.io.gfile.exists(split_dir):
                    tf.io.gfile.makedirs(split_dir)
                np.save(os.path.join(split_dir, label), data[split])
                assert os.path.exists(
                    os.path.join(split_dir, "{}.npy".format(label)))

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=20,
                gen_kwargs={"file_paths": os.path.join(extract_dir, "train")},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=5,
                gen_kwargs={"file_paths": os.path.join(extract_dir, "test")},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=5,
                gen_kwargs={"file_paths": os.path.join(extract_dir, "valid")},
            ),
        ]

    def _generate_examples(self, file_paths):
        """Generate QuickDraw bitmap examples.

        Given the path of the folder containing all the class data

        Args:
            file_paths: (dict of {str: str}) the paths to files containing the data.

        Yields:
            The QuickDraw examples, as defined in the dataset info features.

        """
        for path in tf.io.gfile.listdir(file_paths):
            data = np.load(os.path.join(file_paths, path))
            for sketch in data:
                stroke_5 = self._stroke_3_to_stroke_5(sketch)
                yield {
                    "sketch": {
                        "stroke_5": stroke_5,
                        "stroke_3": sketch,
                    },
                    "label": path.rstrip(".npy")
                }

    @staticmethod
    def _stroke_3_to_stroke_5(sketch_3):
        sketch_5 = []
        seq_len = len(sketch_3)
        for i, stroke_3 in enumerate(sketch_3, start=1):
            stroke_5 = [*stroke_3[:2], 0, 0, 1] if i == seq_len else [
                *stroke_3[:2],
                int(stroke_3[2] == 0),
                int(stroke_3[2] == 1),
                0,
            ]
            sketch_5.append(stroke_5)
        return sketch_5
