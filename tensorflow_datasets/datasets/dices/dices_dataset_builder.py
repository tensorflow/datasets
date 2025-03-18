# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""DICES dataset."""

import ast
import dataclasses

from absl import logging
import numpy as np
import pandas as pd
import tensorflow_datasets.public_api as tfds

_BASE_URL = (
    'https://raw.githubusercontent.com/google-research-datasets/'
    'dices-dataset/main/'
)


@dataclasses.dataclass
class DICESConfig(tfds.core.BuilderConfig):
  """Builder configuration for the DICES dataset."""

  rater_gender_names: tuple[str, ...] = (
      'Man',
      'Woman',
      'Nonbinary',
      'Self-describe (below)',
  )
  rater_locale_names: tuple[str, ...] | None = None
  rater_race_names: tuple[str, ...] = (
      'Asian/Asian subcontinent',
      'Black/African American',
      'LatinX, Latino, Hispanic or Spanish Origin',
      'Multiracial',
      'Other',
      'White',
  )
  rater_age_names: tuple[str, ...] = (
      'millenial',
      'gen x+',
      'gen z',
  )
  rater_education_names: tuple[str, ...] = (
      'College degree or higher',
      'High school or below',
      'Other',
  )
  phase_names: tuple[str, ...] = (
      'Phase1',
      'Phase2',
      'Phase3',
  )
  includes_time_information: bool = True
  degree_of_harm_names: tuple[str, ...] = (
      'No annotation',
      'Benign',
      'Debatable',
      'Extreme',
      'Moderate',
  )
  harm_type_names: tuple[str, ...] = (
      'No annotation',
      'Ablist',
      'Abortion',
      'Ageism',
      'Aggressive',
      'Banter',
      'Bigoted',
      'Celebrity',
      'Criminal/carceral',
      'Drugs/alcohol',
      'Entertainment',
      'Environment/climate',
      'Gendered & sexist',
      'Health',
      'Identity',
      'Insurgency',
      'Legal',
      'Lgbtq+ & homophobic',
      'Mental health/self harm',
      'Miscellaneous',
      'Misinformation',
      'National/regional',
      'Personal',
      'Political',
      'Racial',
      'Regulated goods',
      'Religious',
      'Senseless',
      'Sexual',
      'Terrorism ',
      'Violent/gory',
      'Wealth/finance',
  )
  safety_gold_names: tuple[str, ...] | None = ('No', 'Yes')
  q1_whole_conversation_evaluation_names: tuple[str, ...] = (
      (
          'None of the above - it is in English, it makes sense, and I am'
          ' familiar with the topic'
      ),
      'It is nonsensical (repetitive, incomprehensible, gibberish)',
      'I am not familiar with the topic of the conversation',
      'It is in a language other than English',
  )
  questions: tuple[str, ...] = ()


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for the DICES dataset."""

  VERSION = tfds.core.Version('1.0.0')
  # pytype: disable=wrong-keyword-args
  BUILDER_CONFIGS = [
      DICESConfig(
          name='350',
          description=(
              'Dataset 350 contains 350 conversations rated by a diverse rater'
              ' pool of 123 unique raters. Each conversation is rated with five'
              ' safety top-level categories and one overall comprehension'
              ' question of the conversation. Raters were recruited were'
              ' balanced by gender (man or woman), race/ethnicity (White,'
              ' Black, Latine, Asian, Multiracial) and each rater rated all'
              ' items. Each rater rated all conversations. Each conversation'
              ' has 123 unique ratings. Total number of rows in this dataset is'
              ' 43050.'
          ),
          questions=(
              'Q2_harmful_content_dangerous_content',
              'Q2_harmful_content_derogation_of_boat',
              'Q2_harmful_content_insensitive',
              (
                  'Q2_harmful_content_medical_legal_'
                  'financial_or_relationship_advice'
              ),
              'Q2_harmful_content_obscene_and_profane',
              'Q2_harmful_content_other',
              'Q2_harmful_content_overall',
              'Q2_harmful_content_personal_information',
              'Q2_harmful_content_regulated_goods',
              'Q2_harmful_content_sexually_suggestive_content',
              'Q3_bias_other',
              'Q3_bias_overall',
              'Q3_bias_targeting_beliefs',
              'Q3_bias_targeting_gender_sexual_orientation',
              'Q3_bias_targeting_inherited_attributes',
              'Q3_bias_targeting_status',
              'Q4_misinformation',
              'Q5_political_affiliation',
              'Q6_policy_guidelines_making_endorsement',
              'Q6_policy_guidelines_other',
              'Q6_policy_guidelines_overall',
              'Q6_policy_guidelines_polarizing_topics',
              'Q_overall',
          ),
      ),
      DICESConfig(
          name='990',
          description=(
              'Dataset 990 contains 990 conversations rated by a diverse rater'
              ' pool of 173 unique raters. Each conversation is rated with'
              ' three safety top-level categories and one overall conversation'
              ' comprehension question. Raters were recruited so that the'
              ' number of raters for each conversation was balanced by gender'
              ' (Man, Woman) and locale (US, India). Each rater rated only a'
              ' sample of the conversation. Each conversation has 60-70 unique'
              ' ratings. Total number of rows in this dataset is 72103.'
          ),
          rater_locale_names=('IN', 'US'),
          includes_time_information=False,
          safety_gold_names=None,
          questions=(
              'Q2_harmful_content_harm_to_people_or_animals',
              'Q2_harmful_content_violent_or_gory',
              (
                  'Q2_harmful_content_promotes_or_condones_'
                  'use_of_harmful_regulated_goods'
              ),
              'Q2_harmful_content_health_and_safety_claims',
              'Q2_harmful_content_financial_advice',
              'Q2_harmful_content_promotes_or_condones_violence',
              'Q2_harmful_content_how_tos_about_harmful_activities',
              'Q2_harmful_content_personal_information',
              'Q2_harmful_content_explicitly_sexual',
              'Q2_harmful_content_obscenities_or_profanities',
              'Q2_harmful_content_other',
              'Q3_bias_incites_hatred',
              'Q3_bias_subhuman_comparisons',
              (
                  'Q3_3_Racial_religious_or_other_slurs_and_'
                  'stereotypes_that_incites_or_promote_hatred_'
                  'based_on_any_of_the_attributes_noted_above'
              ),
              'Q3_bias_physically_or_mentally_inferior',
              'Q3_bias_superiority_or_subjugation_of_a_group',
              'Q3_bias_calling_individuals_or_groups_evil_corrupt_or_malicious',
              'Q3_bias_insults_about_emotional_romantic_and_or_sexual_attraction',
              'Q3_bias_other',
              'Q4_misinformation_false_theories',
              'Q4_misinformation_contradicts_expert_consensus',
              'Q4_misinformation_conspiracy_theories',
              'Q4_misinformation_political',
              'Q4_misinformation_other',
              'Q2_harmful_content_overall',
              'Q3_unfair_bias_overall',
              'Q4_misinformation_overall',
              'Q_overall',
          ),
      ),
  ]
  # pytype: enable=wrong-keyword-args
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features = {
        'id': tfds.features.Scalar(
            dtype=np.int64,
            doc=(
                'Numerical identifier for each row, representing all ratings by'
                ' a single rater to a single conversation.'
            ),
        ),
        'rater_id': tfds.features.Scalar(
            dtype=np.int64,
            doc='Numerical identifier for each rater.',
        ),
        'rater_gender': tfds.features.ClassLabel(
            names=self.builder_config.rater_gender_names,
            doc='The gender of the rater.',
        ),
        'rater_race': tfds.features.ClassLabel(
            names=self.builder_config.rater_race_names,
            doc='The race/ethnicity of the rater.',
        ),
        'rater_raw_race': tfds.features.Text(
            doc=(
                'The self-reported raw race/ethnicity of the rater, before'
                ' simplification to five categories.'
            ),
        ),
        'rater_age': tfds.features.ClassLabel(
            names=self.builder_config.rater_age_names,
            doc='The age group of the rater.',
        ),
        'rater_education': tfds.features.ClassLabel(
            names=self.builder_config.rater_education_names,
            doc='The education of the rater.',
        ),
        'phase': tfds.features.ClassLabel(
            names=self.builder_config.phase_names,
            doc='One of three distinct time periods.',
        ),
        'item_id': tfds.features.Scalar(
            dtype=np.int64,
            doc='Numerical identifier for each conversation.',
        ),
        'context': tfds.features.Text(
            doc='The conversation turns before the final chatbot response.'
        ),
        'response': tfds.features.Text(
            doc='The final chatbot response in the conversation.'
        ),
        'degree_of_harm': tfds.features.ClassLabel(
            names=self.builder_config.degree_of_harm_names,
            doc='Hand-annotated rating of severity of safety risk.',
        ),
        'harm_type': tfds.features.Sequence(
            tfds.features.ClassLabel(
                names=self.builder_config.harm_type_names,
                doc='Hand-annotated harm topic(s) of conversation.',
            )
        ),
        'Q1_whole_conversation_evaluation': tfds.features.ClassLabel(
            names=self.builder_config.q1_whole_conversation_evaluation_names,
            doc='Rating about the understandability of a conversation.',
        ),
    }

    if self.builder_config.rater_locale_names is not None:
      features |= {
          'rater_locale': tfds.features.ClassLabel(
              names=self.builder_config.rater_locale_names,
              doc='The locale of the rater.',
          )
      }

    if self.builder_config.includes_time_information:
      features |= {
          'answer_time_ms': tfds.features.Scalar(
              dtype=np.int64,
              doc=(
                  'Amount of time spent by each rater on each safety annotation'
                  ' question.'
              ),
          ),
          'answer_timestamp': tfds.features.Scalar(
              dtype=np.int64,
              doc='Time when each conversation was rated by each rater.',
          ),
      }

    if self.builder_config.safety_gold_names is not None:
      features |= {
          'safety_gold': tfds.features.ClassLabel(
              names=self.builder_config.safety_gold_names,
              doc='The gold standard safety label provided by experts.',
          ),
          'safety_gold_reason': tfds.features.Text(
              doc=(
                  'The reason(s) (if given) for the gold safety label provided'
                  ' by experts.'
              )
          ),
      }

    features |= {
        question: tfds.features.ClassLabel(names=['No', 'Yes', 'Unsure'])
        for question in self.builder_config.questions
    }

    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(features),
        supervised_keys=None,
        homepage='https://github.com/google-research-datasets/dices-dataset',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    name = self.builder_config.name
    filename = f'diverse_safety_adversarial_dialog_{name}.csv'
    paths = dl_manager.download_and_extract(
        {filename: _BASE_URL + f'{name}/{filename}'}
    )

    return {'train': self._generate_examples(paths[filename])}

  def _generate_examples(self, path):
    """Yields examples."""
    df = pd.read_csv(path).rename(columns={'rater_race_raw': 'rater_raw_race'})

    df['rater_raw_race'] = df['rater_raw_race'].fillna('')
    df['degree_of_harm'] = df['degree_of_harm'].fillna('No annotation')
    df['harm_type'] = (
        # NaN means there are no annotations
        df['harm_type']
        .fillna('No annotation')
        .str.split(',')
        # Standardize harm type names
        .map(lambda ts: [t.capitalize() for t in ts])
    )

    if self.builder_config.safety_gold_names is not None:

      def _is_parsable(s):
        try:
          ast.literal_eval(s)
        except (SyntaxError, ValueError):
          return False
        return True

      logging.info(
          'Fixing %d malformed safety_gold_reason strings',
          (~df['safety_gold_reason'].map(_is_parsable)).sum(),
      )

      df['safety_gold_reason'] = (
          df['safety_gold_reason']
          # Some safety gold reason features cannot be parsed by
          # `ast.literal_eval` because the string is malformed. To fix that, we
          # first pare the string down to a comma-separated sequence of safety
          # gold reason labels.
          .str.replace(r'[\[" \]]', '', regex=True)
          # We then recombine the sequence into a well-formed representation of
          # the list of safety gold reason string labels.
          .str.split(',').map(lambda lst: '["' + '","'.join(lst) + '"]')
      )

      # Complain loudly if the above fix does not work.
      if not df['safety_gold_reason'].map(_is_parsable).all():
        raise RuntimeError(
            'unable to fix all malformed safety_gold_reason strings'
        )

    for i, row in df.to_dict(orient='index').items():
      yield i, row
