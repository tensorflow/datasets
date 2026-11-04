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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import os
from absl import logging
import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{DBLP:journals/corr/WestonBCM15,
  author    = {Jason Weston and
               Antoine Bordes and
               Sumit Chopra and
               Tomas Mikolov},
  title     = {Towards AI-Complete Question Answering: {A} Set of Prerequisite Toy
               Tasks},
  journal   = {CoRR},
  volume    = {abs/1502.05698},
  year      = {2015},
  url       = {http://arxiv.org/abs/1502.05698},
  archivePrefix = {arXiv},
  eprint    = {1502.05698},
  timestamp = {Mon, 13 Aug 2018 16:47:58 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/WestonBCM15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

"""
_DESCRIPTION = """\
This dataset is the collection of 1000 training and test data which deals with the collection of certain \
text with every 3rd line containing some questions based on the previous values giving certain answers \
related to the dataset and with the id number related to the answer
"""

_DOWNLOAD_URL = ("http://www.thespermwhale.com/jaseweston/babi/"
                 "tasks_1-20_v1-2.tar.gz")
_TOP_LEVEL_DIR = "tasks_1-29_v1-2"

_TRAIN_FILE_FORMAT = os.path.join(_TOP_LEVEL_DIR, "shuffled-10k", "qa*train.txt")
_TEST_FILE_FORMAT = os.path.join(_TOP_LEVEL_DIR, "shuffled-10k", "qa*test.txt")

class TasksConfig(tfds.core.BuilderConfig):
    """ Builder config for tasks dataset"""
    @api_utils.disallow_positional_args
    def __init__(self, text_encoder_config=None, **kwargs):
        """ BuilderConfig for tasks.
        Args:
        text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the tasks `"text"`
        feature.
      **kwargs: keyword arguments forwarded to super.
    """
        super(TasksConfig, self).__init__(**kwargs)
        self.text_encoder_config = (
            text_encoder_config or tfds.features.text.TextEncoderConfig())

def _train_data_filenames(tmp_dir):
    return tf.io.gfile.glob(os.path.join(tmp_dir, _TRAIN_FILE_FORMAT))

def _test_data_filenames(tmp_dir):
    return tf.io.gfile.glob(os.path.join(tmp_dir, _TEST_FILE_FORMAT))

class BablTasks(tfds.core.GeneratorBasedBuilder):
    """ Tasks dataset combining useful information of training and test data """
    BUILDER_CONFIGS = [
        TasksConfig(
            name="plain_text",
            version="0.0.1",
            description="Plain text",
        ),
        TasksConfig(
            name="bytes",
            version="0.0.1",
            description=("Uses byte-level text encoding with "
                         "`tfds.features.text.ByteTextEncoder`"),
            text_encoder_config=tfds.features.text.TextEncoderConfig(
                encoder=tfds.features.text.ByteTextEncoder()),
        ),
        TasksConfig(
            name="subwords8k",
            version="0.0.2",
            description=("Uses `tfds.features.text.SubwordTextEncoder` with 8k "
                         "vocab size"),
            text_encoder_config=tfds.features.text.TextEncoderConfig(
                encoder_cls=tfds.features.text.SubwordTextEncoder,
                vocab_size=2**13),
        ),
        TasksConfig(
            name="subwords32k",
            version="0.0.2",
            description=("Uses `tfds.features.text.SubwordTextEncoder` with "
                         "32k vocab size"),
            text_encoder_config=tfds.features.text.TextEncoderConfig(
                encoder_cls=tfds.features.text.SubwordTextEncoder,
                vocab_size=2**15),
        ),
    ]


    def _info(self):
        # Specifies tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.SequenceDict({
                "text":tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
                "id":tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config)
                        }),
            supervised_keys=None,
            urls=["http://www.thespermwhale.com/jaseweston/babi/"],
            citation=_CITATION
                )

    def _vocab_text_gen(self, training_files):
        for ex in self._generate_examples(training_files):
            yield ex["text"]

    def _split_generators(self, dl_manager):
        tasks_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
        train_files = _train_data_filenames(tasks_path)
        test_files = _test_data_filenames(tasks_path)
        # Generate vocabulary from training data if SubwordTextEncoder configured
        self.info.features["text"].maybe_build_from_corpus(
            self._vocab_text_gen(train_files))

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=1,
                gen_kwargs={"files": train_files}),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=1,
                gen_kwargs={"files": test_files}),
            ]

    def _generate_examples(self, files):
        for filepath in files:
            logging.info("generating examples from = %s", filepath)
            with tf.io.gfile.GFile(filepath) as f:
                for line in f:
                    yield [{
                        "id": line[0],
                        "text": line[2:],
                        }]
