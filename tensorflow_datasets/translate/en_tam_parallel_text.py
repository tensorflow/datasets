# # coding=utf-8
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
#pylint: disable=blacklist
#pylint: disable=en_tam
"""English-Tamil parallel text corpus"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re

import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_CITATION = {}
DESCRIPTION = {}
DESCRIPTION['MTPIL'] = """\
	The parallel corpora cover texts from bible, cinema and news domains.
"""
DESCRIPTION['opus'] = """\
	OPUS project focuses on converting and aligning free online data, to add linguistic annotation, and to provide the community with a publicly available parallel corpus.
"""
_CITATION['MTPIL'] = """
  @inproceedings {biblio:RaBoMorphologicalProcessing2012,
	title = {Morphological Processing for English-Tamil Statistical Machine Translation},
	author = {Loganathan Ramasamy and Ond{\v{r}}ej Bojar and Zden{\v{e}}k {\v{Z}}abokrtsk{\'{y}}},
	year = {2012},
	pages = {113--122},
	Booktitle = {Proceedings of the Workshop on Machine Translation and Parsing in Indian Languages ({MTPIL}-2012)},
}"""
_CITATION['opus'] = """
    @InProceedings{TIEDEMANN12.463,
  	author = {J�rg Tiedemann},
  	title = {Parallel Data, Tools and Interfaces in OPUS},
  	booktitle = {Proceedings of the Eight International Conference on Language Resources and Evaluation (LREC'12)},
  	year = {2012},
  	month = {may},
  	date = {23-25},
  	address = {Istanbul, Turkey},
  	editor = {Nicoletta Calzolari (Conference Chair) and Khalid Choukri and Thierry Declerck and Mehmet Ugur Dogan and Bente Maegaard and Joseph Mariani and Jan Odijk and Stelios Piperidis},
  	publisher = {European Language Resources Association (ELRA)},
  	isbn = {978-2-9517408-7-7},
  	language = {english}
 }"""
download_links = [
    'http://ufal.mff.cuni.cz/~ramasamy/parallel/data/v2/en-ta-parallel-v2.tar.gz',
    'http://opus.nlpl.eu/download.php?f=GNOME/v1/moses/en-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=GNOME/v1/moses/en_AU-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=GNOME/v1/moses/en_CA-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=GNOME/v1/moses/en_GB-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=GNOME/v1/moses/en_US-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=KDE4/v2/moses/en-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=KDE4/v2/moses/en_GB-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Tatoeba/v20190709/moses/en-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en-ta_LK.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en_GB-ta_LK.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en_AU-ta_LK.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en_CA-ta_LK.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en_US-ta_LK.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en_GB-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en_AU-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en_CA-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en_NZ-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/en_US-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/moses/en-ta.txt.zip',
    'http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2016/moses/en-ta.txt.zip']

_VALID_LANGUAGE_PAIRS = [
    ("en", "ta"),
    ("en_AU", "ta"),
    ("en_CA", "ta"),
    ("en_GB", "ta"),
    ("en_NZ", "ta"),
    ("en_US", "ta"),
    ("en", "ta_LK"),
    ("en_AU", "ta_LK"),
    ("en_CA", "ta_LK"),
    ("en_GB", "ta_LK"),
    ('en_US', 'ta_LK')
]


class EnTamParallelTextConfig(tfds.core.BuilderConfig):
  """BuilderConfig for English & Tamil parallel text data."""

  @api_utils.disallow_positional_args
  def __init__(self, download_link=None, **kwargs):
    """
    Create source and target filenames from the link which
	can be consumed by the download & extract function
    Args:
      download_link: links of the files to be downloaded
      **kwargs: keyword arguments forwarded to super.
      
    """
    self.language_pair = ("en", "ta")
    if 'opus' in download_link:
      language_pair = download_link.split('/')[-1].split('.')[0].split('-')
      language_pair = tuple(language_pair)
      typ_name = download_link.split('?f=')[1].split('/moses')[0].replace('/', '_')
      name = "%s_to_%s" % (language_pair[0], language_pair[1])
      name = typ_name+'_'+name
      description = ("Translation dataset from %s to %s in plain text.") % (
          language_pair[0], language_pair[1])
      self.citation = _CITATION['opus']
      self.descrp = DESCRIPTION['opus']
      # Validate language pair.
      assert language_pair in _VALID_LANGUAGE_PAIRS, (
          "Config language pair (%s, "
          "%s) not supported") % language_pair
      if 'GNOME' in download_link:
        typ = 'GNOME'
        self.sname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[0]#pylint: disable=en_tam
        self.tname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[1]#pylint: disable=en_tam
        self.link = download_link
      elif 'KDE4' in download_link:
        typ = 'KDE4'
        self.sname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[0]#pylint: disable=en_tam
        self.tname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[1]#pylint: disable=en_tam
        self.link = download_link
      elif 'Tatoeba' in download_link:
        typ = 'Tatoeba'
        self.sname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[0]#pylint: disable=en_tam
        self.tname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[1]#pylint: disable=en_tam
        self.link = download_link
      elif 'Ubuntu' in download_link:
        typ = 'Ubuntu'
        self.sname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[0]#pylint: disable=en_tam
        self.tname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[1]# pylint: disable=en_tam
        self.link = download_link
      elif 'OpenSubtitles' in download_link:
        typ = 'OpenSubtitles'
        self.sname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[0]#pylint: disable=en_tam
        self.tname = typ+'.'+language_pair[0]+'-'+language_pair[1]+'.'+language_pair[1]#pylint: disable=en_tam
        self.link = download_link
    elif 'ufal.mff.cuni.cz/~ramasamy' in download_link:
      name = "en_ta"
      self.citation = _CITATION['MTPIL']
      self.descrp = DESCRIPTION['MTPIL']
      description = ("Translation dataset from %s to %s in plain text.") % (
          'en', 'ta')
      self.link = download_link
    super(EnTamParallelTextConfig, self).__init__(
        name=name, description=description, **kwargs)

class EnTamParallelText(tfds.core.GeneratorBasedBuilder):
  """(en_tam_parallel_text): English_Tamil parallel text corpus"""
  BUILDER_CONFIGS = [
      EnTamParallelTextConfig(download_link=link, version=tfds.core.Version(
          "0.0.1", experiments={tfds.core.Experiment.S3: False}))
      for link in download_links
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=self.builder_config.descrp,
        features=tfds.features.Translation(
            languages=("en", "ta")),
        urls=[self.builder_config.link],
        supervised_keys=("en", "ta"),
        citation=self.builder_config.citation,
    )

  def _split_generators(self, dl_manager):
    """Download the links and pass the filenames to split generator"""
    link_dict = {}
    head = 'corpus.bcn.'
    if 'opus' in self.builder_config.link:
      link_dict['OPUS'] = self.builder_config.link
    elif 'ufal.mff.cuni.cz' in self.builder_config.link:
      link_dict['MTPIL'] = self.builder_config.link
    dl_dir = dl_manager.download_and_extract(link_dict)
    for site in dl_dir:
      if site == 'MTPIL':
        data_dir = os.path.join(dl_dir[site], 'en-ta-parallel-v2')
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=1,
                gen_kwargs={
                    "source_file": os.path.join(data_dir, head+'train.en'),
                    "target_file": os.path.join(data_dir, head+'train.ta')
                }),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=1,
                gen_kwargs={
                    "source_file": os.path.join(data_dir, head+'dev.en'),
                    "target_file": os.path.join(data_dir, head+'dev.ta')
                }),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                num_shards=1,
                gen_kwargs={
                    "source_file": os.path.join(data_dir, head+'test.en'),
                    "target_file": os.path.join(data_dir, head+'test.ta')
                })]
      else:
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=1,
                gen_kwargs={
                    "source_file": os.path.join(dl_dir[site], self.builder_config.sname),
                    "target_file": os.path.join(dl_dir[site], self.builder_config.tname)
                })]
  def _generate_examples(self, source_file, target_file):
    """This function returns the filtered text pairs.Some filtering techniques were inspired from https://github.com/himanshudce/MIDAS-NMT-English-Tamil/blob/master/Data%20perprocessing/data.py"""
    with tf.io.gfile.GFile(source_file) as f:
      source_sentences = f.read().split("\n")
    with tf.io.gfile.GFile(target_file) as f:
      target_sentences = f.read().split("\n")

    assert len(target_sentences) == len(
        source_sentences), "Sizes do not match: %d vs %d for %s vs %s." % (len(
            source_sentences), len(target_sentences), source_file, target_file)
    source, target = self.builder_config.language_pair
    ta_blacklist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-(\')''/[]♪/%#$&\/_"{.}|=<>@~`'
    en_blacklist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ"#$%&\()*+-./:;<=>@[\\]^_`♪{|}~='
    cleantxt = re.compile('<.*?>')
    for l1, l2 in zip(source_sentences, target_sentences):
      # Lower case english lines
      l1 = l1.lower()
      # Remove unwanted html tags from text
      l1 = re.sub(cleantxt, '', l1)
      l2 = re.sub(cleantxt, '', l2)
	  # Remove english text in tamil sentence and tamil text in english sentence
      cleaned_l1 = ''.join([ch for ch in l1 if ch not in en_blacklist])
      cleaned_l2 = ''.join([ch for ch in l2 if ch not in ta_blacklist])
      result = {source: cleaned_l1, target: cleaned_l2}
      # Make sure that both translations are non-empty
      if all(result.values()):
        yield result
