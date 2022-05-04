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

"""BLiMP dataset with minimal pairs of grammatical phenomena in English."""

import json

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{warstadt2019blimp,
  title={BLiMP: A Benchmark of Linguistic Minimal Pairs for English},
  author={Warstadt, Alex and Parrish, Alicia and Liu, Haokun and Mohananey, Anhad and Peng, Wei, and Wang, Sheng-Fu and Bowman, Samuel R},
  journal={arXiv preprint arXiv:1912.00582},
  year={2019}
}
"""

_DESCRIPTION = """
BLiMP is a challenge set for evaluating what language models (LMs) know about
major grammatical phenomena in English. BLiMP consists of 67 sub-datasets, each
containing 1000 minimal pairs isolating specific contrasts in syntax,
morphology, or semantics. The data is automatically generated according to
expert-crafted grammars.
"""

_PROJECT_URL = 'https://github.com/alexwarstadt/blimp/tree/master/'
_DOWNLOAD_URL = 'https://raw.githubusercontent.com/alexwarstadt/blimp/master'


class BlimpConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Blimp."""

  def __init__(self, *, paradigm_uid, **kwargs):
    """BuilderConfig for Blimp.

    Args:
      paradigm_uid: string, UID of the linguistic paradigm
      **kwargs: keyword arguments forwarded to super.
    """
    name = paradigm_uid
    super(BlimpConfig, self).__init__(
        name=name,
        description=f'This configuration includes the paradigm {name}.',
        version=tfds.core.Version('0.1.0'),
        **kwargs)


class Blimp(tfds.core.GeneratorBasedBuilder):
  """Minimal grammatical and ungrammatical pairs of 67 linguistic paradigms."""

  all_paradigms = [
      'adjunct_island',
      'anaphor_gender_agreement',
      'anaphor_number_agreement',
      'animate_subject_passive',
      'animate_subject_trans',
      'causative',
      'complex_NP_island',
      'coordinate_structure_constraint_complex_left_branch',
      'coordinate_structure_constraint_object_extraction',
      'determiner_noun_agreement_1',
      'determiner_noun_agreement_2',
      'determiner_noun_agreement_irregular_1',
      'determiner_noun_agreement_irregular_2',
      'determiner_noun_agreement_with_adj_2',
      'determiner_noun_agreement_with_adj_irregular_1',
      'determiner_noun_agreement_with_adj_irregular_2',
      'determiner_noun_agreement_with_adjective_1',
      'distractor_agreement_relational_noun',
      'distractor_agreement_relative_clause',
      'drop_argument',
      'ellipsis_n_bar_1',
      'ellipsis_n_bar_2',
      'existential_there_object_raising',
      'existential_there_quantifiers_1',
      'existential_there_quantifiers_2',
      'existential_there_subject_raising',
      'expletive_it_object_raising',
      'inchoative',
      'intransitive',
      'irregular_past_participle_adjectives',
      'irregular_past_participle_verbs',
      'irregular_plural_subject_verb_agreement_1',
      'irregular_plural_subject_verb_agreement_2',
      'left_branch_island_echo_question',
      'left_branch_island_simple_question',
      'matrix_question_npi_licensor_present',
      'npi_present_1',
      'npi_present_2',
      'only_npi_licensor_present',
      'only_npi_scope',
      'passive_1',
      'passive_2',
      'principle_A_c_command',
      'principle_A_case_1',
      'principle_A_case_2',
      'principle_A_domain_1',
      'principle_A_domain_2',
      'principle_A_domain_3',
      'principle_A_reconstruction',
      'regular_plural_subject_verb_agreement_1',
      'regular_plural_subject_verb_agreement_2',
      'sentential_negation_npi_licensor_present',
      'sentential_negation_npi_scope',
      'sentential_subject_island',
      'superlative_quantifiers_1',
      'superlative_quantifiers_2',
      'tough_vs_raising_1',
      'tough_vs_raising_2',
      'transitive',
      'wh_island',
      'wh_questions_object_gap',
      'wh_questions_subject_gap',
      'wh_questions_subject_gap_long_distance',
      'wh_vs_that_no_gap',
      'wh_vs_that_no_gap_long_distance',
      'wh_vs_that_with_gap',
      'wh_vs_that_with_gap_long_distance',
  ]

  BUILDER_CONFIGS = [
      BlimpConfig(paradigm_uid=paradigm) for paradigm in all_paradigms
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'sentence_good': tfds.features.Text(),
            'sentence_bad': tfds.features.Text(),
            'field': tfds.features.Text(),
            'linguistics_term': tfds.features.Text(),
            'UID': tfds.features.Text(),
            'simple_LM_method': tf.bool,
            'one_prefix_method': tf.bool,
            'two_prefix_method': tf.bool,
            'lexically_identical': tf.bool,
            'pair_id': tf.int32,
        }),
        supervised_keys=None,
        # Homepage of the dataset for documentation
        homepage=_PROJECT_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    cfg = self.builder_config
    download_urls = {
        cfg.name: '/'.join([_DOWNLOAD_URL, 'data', cfg.name + '.jsonl'])
    }

    downloaded_files = dl_manager.download_and_extract(download_urls)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'filepath': downloaded_files[cfg.name]})
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""
    with tf.io.gfile.GFile(filepath, 'rb') as f:
      for line in f:
        line_dict = json.loads(line)
        id_ = line_dict['UID'] + '_' + line_dict['pairID']
        feats = {
            'sentence_good': line_dict['sentence_good'],
            'sentence_bad': line_dict['sentence_bad'],
            'field': line_dict['field'],
            'linguistics_term': line_dict['linguistics_term'],
            'UID': line_dict['UID'],
            'simple_LM_method': line_dict['simple_LM_method'],
            'one_prefix_method': line_dict['one_prefix_method'],
            'two_prefix_method': line_dict['two_prefix_method'],
            'lexically_identical': line_dict['lexically_identical'],
            'pair_id': line_dict['pairID'],
        }
        yield id_, feats
