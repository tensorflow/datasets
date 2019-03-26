from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import numpy as np

IRIS_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

_CITATION = """\
@misc{Dua:2019 ,
author = "Dua, Dheeru and Graff, Casey",
year = "2017",
title = "{UCI} Machine Learning Repository",
url = "http://archive.ics.uci.edu/ml",
institution = "University of California, Irvine, School of Information and Computer Sciences"
}
"""

_DESCRIPTION = """\
This is perhaps the best known database to be found in the pattern recognition
literature. Fisher's paper is a classic in the field and is referenced
frequently to this day. (See Duda & Hart, for example.) The data set contains
3 classes of 50 instances each, where each class refers to a type of iris
plant. One class is linearly separable from the other 2; the latter are NOT
linearly separable from each other.
"""


class Iris(tfds.core.GeneratorBasedBuilder):
    """Iris flower dataset"""

    NUM_CLASSES = 3
    VERSION = tfds.core.Version("0.1.0")

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            # tfds.features.FeatureConnectors
            features=tfds.features.FeaturesDict(
                {
                    "features": tfds.features.Tensor(shape=(4,), dtype=tf.float32),
                    # Here, labels can be one of 3 classes
                    "label": tfds.features.ClassLabel(
                        names=["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
                    ),
                }
            ),
            supervised_keys=("features", "label"),
            urls=["https://archive.ics.uci.edu/ml/datasets/iris"],
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        iris_file = dl_manager.download(IRIS_URL)
        all_lines = tf.io.gfile.GFile(iris_file).read().split("\n")
        records = [l for l in all_lines if l]  # get rid of empty lines

        split = 0.8
        total = len(records)
        per_class = total // self.NUM_CLASSES
        train_per_class = int(per_class * split)
        test_per_class = per_class - train_per_class

        train_lines = []
        for offset in range(0, total, per_class):
            train_lines += records[offset : (offset + train_per_class)]

        test_lines = []
        for offset in range(train_per_class, total, per_class):
            test_lines += records[offset : (offset + test_per_class)]

        # Specify the splits
        return [
            tfds.core.SplitGenerator(
                name="train", num_shards=1, gen_kwargs={"records": train_lines}
            ),
            tfds.core.SplitGenerator(
                name="test", num_shards=1, gen_kwargs={"records": test_lines}
            ),
        ]

    def _generate_examples(self, records):
        for record in records:
            elems = record.split(",")
            yield {
                "features": np.fromstring(" ".join(elems[:4]), dtype="f4", sep=" "),
                "label": elems[4],
            }
