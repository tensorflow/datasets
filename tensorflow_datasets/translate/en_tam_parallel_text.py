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

"""English-Tamil parallel text corpus"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds


DESCRIPTION = """\
	The parallel corpora covers texts from bible, cinema and news domains.The dataset is split
	into train, test and validation set comprising a total of 170000 lines of ENGLISH and TAMIL texts.
"""

_CITATION = """
  @inproceedings {biblio:RaBoMorphologicalProcessing2012,
	title = {Morphological Processing for English-Tamil Statistical Machine Translation},
	author = {Loganathan Ramasamy and Ond{\v{r}}ej Bojar and Zden{\v{e}}k {\v{Z}}abokrtsk{\'{y}}},
	year = {2012},
	pages = {113--122},
	Booktitle = {Proceedings of the Workshop on Machine Translation and Parsing in Indian Languages ({MTPIL}-2012)},
}"""

url = "http://ufal.mff.cuni.cz/~ramasamy/parallel/data/v2/en-ta-parallel-v2.tar.gz"
links = [
    "http://ufal.mff.cuni.cz/~ramasamy/parallel/data/v2/en-ta-parallel-v2.tar.gz"
]

class EnTamParallelTextConfig(tfds.core.BuilderConfig):
  """BuilderConfig for English & Tamil parallel text data."""
  @api_utils.disallow_positional_args
  def __init__(self, download_link=None, **kwargs):
    """
    Args:
      download_link: links of the files to be downloaded
      **kwargs: keyword arguments forwarded to super.
    """
    self.link = download_link
    name = 'ufal_en_tam'
    description = ("Translation dataset from %s to %s in plain text.") % (
        "en", "ta")
    self.language_pair = ("en", "ta")
    super(EnTamParallelTextConfig, self).__init__(
        name=name, description=description, **kwargs)
class EnTamParallelText(tfds.core.GeneratorBasedBuilder):
  """(en_tam_parallel_text): English_Tamil parallel text corpus"""

  BUILDER_CONFIGS = [
      EnTamParallelTextConfig(download_link=link, version=tfds.core.Version(
          "0.0.1", experiments={tfds.core.Experiment.S3: False}))
      for link in links
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=DESCRIPTION,
        features=tfds.features.Translation(
            languages=("en", "ta"),
            encoder_config=tfds.features.text.TextEncoderConfig()
        ),
        urls=[url],
        supervised_keys=("en", "ta"),
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Download the links and pass the filenames to split generator"""
    dl_dir = dl_manager.download_and_extract(url)
    data_dir = os.path.join(dl_dir, 'en-ta-parallel-v2')
    head = 'corpus.bcn'
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs={
                "source_file":
                    os.path.join(data_dir, head+'.train.en'),
                "target_file":
                    os.path.join(data_dir, head+'.train.ta')
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={
                "source_file":
                    os.path.join(data_dir, head+'.dev.en'),
                "target_file":
                    os.path.join(data_dir, head+'.dev.ta')
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={
                "source_file":
                    os.path.join(data_dir, head+'.test.en'),
                "target_file":
                    os.path.join(data_dir, head+'.test.ta')
            }),
    ]
  def _generate_examples(self, source_file, target_file):
    """Return the examples in text form."""
    with tf.io.gfile.GFile(source_file) as f:
      source_sentences = f.read().split("\n")
    with tf.io.gfile.GFile(target_file) as f:
      target_sentences = f.read().split("\n")
    assert len(target_sentences) == len(
        source_sentences), "Sizes do not match: %d vs %d for %s vs %s." % (len(
            source_sentences), len(target_sentences), source_file, target_file)
    source, target = ('en', 'ta')
	#create pattern to find html tags in the raw text
    cleantxt = re.compile('<.*?>')
    for l1, l2 in zip(source_sentences, target_sentences):
      # Remove unwanted html tags from text
      cleaned_l1 = re.sub(cleantxt, '', l1)
      cleaned_l2 = re.sub(cleantxt, '', l2)
      result = {source: cleaned_l1, target: cleaned_l2}
      # Make sure that both translations are non-empty.
      if all(result.values()):
        yield result
		