<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dices" />
  <meta itemprop="description" content="# The Diversity in Conversational AI Evaluation for Safety (**DICES**) dataset&#10;&#10;Machine learning approaches are often trained and evaluated with datasets that&#10;require a clear separation between positive and negative examples. This approach&#10;overly simplifies the natural subjectivity present in many tasks and content&#10;items. It also obscures the inherent diversity in human perceptions and&#10;opinions. Often tasks that attempt to preserve the variance in content and&#10;diversity in humans are quite expensive and laborious. To fill in this gap and&#10;facilitate more in-depth model performance analyses we propose the DICES dataset&#10;- a unique dataset with diverse perspectives on safety of AI generated&#10;conversations. We focus on the task of safety evaluation of conversational AI&#10;systems. The DICES dataset contains detailed demographics information about each&#10;rater, extremely high replication of unique ratings per conversation to ensure&#10;statistical significance of further analyses and encodes rater votes as&#10;distributions across different demographics to allow for in-depth explorations&#10;of different rating aggregation strategies.&#10;&#10;This dataset is well suited to observe and measure variance, ambiguity and&#10;diversity in the context of safety of conversational AI. The dataset is&#10;accompanied by a paper describing a set of metrics that show how rater diversity&#10;influences the safety perception of raters from different geographic regions,&#10;ethnicity groups, age groups and genders. The goal of the DICES dataset is to be&#10;used as a shared benchmark for safety evaluation of conversational AI systems.&#10;&#10;**CONTENT WARNING**: This dataset contains adversarial examples of conversations&#10;that may be offensive.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dices&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dices" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/dices-dataset" />
  <meta itemprop="citation" content="@article{aroyo2024dices,&#10;  title={{DICES} dataset: Diversity in conversational {AI} evaluation for safety},&#10;  author={Aroyo, Lora and Taylor, Alex and Diaz, Mark and Homan, Christopher and Parrish, Alicia and Serapio-Garc{\&#x27;\i}a, Gregory and Prabhakaran, Vinodkumar and Wang, Ding},&#10;  journal={Advances in Neural Information Processing Systems},&#10;  volume={36},&#10;  year={2024}&#10;}" />
</div>

# `dices`


*   **Description**:

# The Diversity in Conversational AI Evaluation for Safety (**DICES**) dataset

Machine learning approaches are often trained and evaluated with datasets that
require a clear separation between positive and negative examples. This approach
overly simplifies the natural subjectivity present in many tasks and content
items. It also obscures the inherent diversity in human perceptions and
opinions. Often tasks that attempt to preserve the variance in content and
diversity in humans are quite expensive and laborious. To fill in this gap and
facilitate more in-depth model performance analyses we propose the DICES
dataset - a unique dataset with diverse perspectives on safety of AI generated
conversations. We focus on the task of safety evaluation of conversational AI
systems. The DICES dataset contains detailed demographics information about each
rater, extremely high replication of unique ratings per conversation to ensure
statistical significance of further analyses and encodes rater votes as
distributions across different demographics to allow for in-depth explorations
of different rating aggregation strategies.

This dataset is well suited to observe and measure variance, ambiguity and
diversity in the context of safety of conversational AI. The dataset is
accompanied by a paper describing a set of metrics that show how rater diversity
influences the safety perception of raters from different geographic regions,
ethnicity groups, age groups and genders. The goal of the DICES dataset is to be
used as a shared benchmark for safety evaluation of conversational AI systems.

**CONTENT WARNING**: This dataset contains adversarial examples of conversations
that may be offensive.

*   **Homepage**:
    [https://github.com/google-research-datasets/dices-dataset](https://github.com/google-research-datasets/dices-dataset)

*   **Source code**:
    [`tfds.datasets.dices.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/dices/dices_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{aroyo2024dices,
  title={{DICES} dataset: Diversity in conversational {AI} evaluation for safety},
  author={Aroyo, Lora and Taylor, Alex and Diaz, Mark and Homan, Christopher and Parrish, Alicia and Serapio-Garc{\'\i}a, Gregory and Prabhakaran, Vinodkumar and Wang, Ding},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  year={2024}
}
```


## dices/350 (default config)

*   **Config description**: Dataset 350 contains 350 conversations rated by a
    diverse rater pool of 123 unique raters. Each conversation is rated with
    five safety top-level categories and one overall comprehension question of
    the conversation. Raters were recruited were balanced by gender (man or
    woman), race/ethnicity (White, Black, Latine, Asian, Multiracial) and each
    rater rated all items. Each rater rated all conversations. Each conversation
    has 123 unique ratings. Total number of rows in this dataset is 43050.

*   **Download size**: `29.70 MiB`

*   **Dataset size**: `74.43 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 43,050

*   **Feature structure**:

```python
FeaturesDict({
    'Q1_whole_conversation_evaluation': ClassLabel(shape=(), dtype=int64, num_classes=4),
    'Q2_harmful_content_dangerous_content': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_derogation_of_boat': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_insensitive': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_medical_legal_financial_or_relationship_advice': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_obscene_and_profane': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_other': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_overall': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_personal_information': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_regulated_goods': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_sexually_suggestive_content': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_other': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_overall': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_targeting_beliefs': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_targeting_gender_sexual_orientation': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_targeting_inherited_attributes': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_targeting_status': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q4_misinformation': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q5_political_affiliation': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q6_policy_guidelines_making_endorsement': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q6_policy_guidelines_other': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q6_policy_guidelines_overall': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q6_policy_guidelines_polarizing_topics': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q_overall': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'answer_time_ms': Scalar(shape=(), dtype=int64, description=Amount of time spent by each rater on each safety annotation question.),
    'answer_timestamp': Scalar(shape=(), dtype=int64, description=Time when each conversation was rated by each rater.),
    'context': Text(shape=(), dtype=string),
    'degree_of_harm': ClassLabel(shape=(), dtype=int64, num_classes=5),
    'harm_type': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=32)),
    'id': Scalar(shape=(), dtype=int64, description=Numerical identifier for each row, representing all ratings by a single rater to a single conversation.),
    'item_id': Scalar(shape=(), dtype=int64, description=Numerical identifier for each conversation.),
    'phase': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'rater_age': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'rater_education': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'rater_gender': ClassLabel(shape=(), dtype=int64, num_classes=4),
    'rater_id': Scalar(shape=(), dtype=int64, description=Numerical identifier for each rater.),
    'rater_race': ClassLabel(shape=(), dtype=int64, num_classes=6),
    'rater_raw_race': Text(shape=(), dtype=string),
    'response': Text(shape=(), dtype=string),
    'safety_gold': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'safety_gold_reason': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature                                                           | Class                | Shape   | Dtype  | Description
:---------------------------------------------------------------- | :------------------- | :------ | :----- | :----------
                                                                  | FeaturesDict         |         |        |
Q1_whole_conversation_evaluation                                  | ClassLabel           |         | int64  | Rating about the understandability of a conversation.
Q2_harmful_content_dangerous_content                              | ClassLabel           |         | int64  |
Q2_harmful_content_derogation_of_boat                             | ClassLabel           |         | int64  |
Q2_harmful_content_insensitive                                    | ClassLabel           |         | int64  |
Q2_harmful_content_medical_legal_financial_or_relationship_advice | ClassLabel           |         | int64  |
Q2_harmful_content_obscene_and_profane                            | ClassLabel           |         | int64  |
Q2_harmful_content_other                                          | ClassLabel           |         | int64  |
Q2_harmful_content_overall                                        | ClassLabel           |         | int64  |
Q2_harmful_content_personal_information                           | ClassLabel           |         | int64  |
Q2_harmful_content_regulated_goods                                | ClassLabel           |         | int64  |
Q2_harmful_content_sexually_suggestive_content                    | ClassLabel           |         | int64  |
Q3_bias_other                                                     | ClassLabel           |         | int64  |
Q3_bias_overall                                                   | ClassLabel           |         | int64  |
Q3_bias_targeting_beliefs                                         | ClassLabel           |         | int64  |
Q3_bias_targeting_gender_sexual_orientation                       | ClassLabel           |         | int64  |
Q3_bias_targeting_inherited_attributes                            | ClassLabel           |         | int64  |
Q3_bias_targeting_status                                          | ClassLabel           |         | int64  |
Q4_misinformation                                                 | ClassLabel           |         | int64  |
Q5_political_affiliation                                          | ClassLabel           |         | int64  |
Q6_policy_guidelines_making_endorsement                           | ClassLabel           |         | int64  |
Q6_policy_guidelines_other                                        | ClassLabel           |         | int64  |
Q6_policy_guidelines_overall                                      | ClassLabel           |         | int64  |
Q6_policy_guidelines_polarizing_topics                            | ClassLabel           |         | int64  |
Q_overall                                                         | ClassLabel           |         | int64  |
answer_time_ms                                                    | Scalar               |         | int64  | Amount of time spent by each rater on each safety annotation question.
answer_timestamp                                                  | Scalar               |         | int64  | Time when each conversation was rated by each rater.
context                                                           | Text                 |         | string | The conversation turns before the final chatbot response.
degree_of_harm                                                    | ClassLabel           |         | int64  | Hand-annotated rating of severity of safety risk.
harm_type                                                         | Sequence(ClassLabel) | (None,) | int64  | Hand-annotated harm topic(s) of conversation.
id                                                                | Scalar               |         | int64  | Numerical identifier for each row, representing all ratings by a single rater to a single conversation.
item_id                                                           | Scalar               |         | int64  | Numerical identifier for each conversation.
phase                                                             | ClassLabel           |         | int64  | One of three distinct time periods.
rater_age                                                         | ClassLabel           |         | int64  | The age group of the rater.
rater_education                                                   | ClassLabel           |         | int64  | The education of the rater.
rater_gender                                                      | ClassLabel           |         | int64  | The gender of the rater.
rater_id                                                          | Scalar               |         | int64  | Numerical identifier for each rater.
rater_race                                                        | ClassLabel           |         | int64  | The race/ethnicity of the rater.
rater_raw_race                                                    | Text                 |         | string | The self-reported raw race/ethnicity of the rater, before simplification to five categories.
response                                                          | Text                 |         | string | The final chatbot response in the conversation.
safety_gold                                                       | ClassLabel           |         | int64  | The gold standard safety label provided by experts.
safety_gold_reason                                                | Text                 |         | string | The reason(s) (if given) for the gold safety label provided by experts.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dices-350-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## dices/990

*   **Config description**: Dataset 990 contains 990 conversations rated by a
    diverse rater pool of 173 unique raters. Each conversation is rated with
    three safety top-level categories and one overall conversation comprehension
    question. Raters were recruited so that the number of raters for each
    conversation was balanced by gender (Man, Woman) and locale (US, India).
    Each rater rated only a sample of the conversation. Each conversation has
    60-70 unique ratings. Total number of rows in this dataset is 72103.

*   **Download size**: `48.06 MiB`

*   **Dataset size**: `150.38 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Only when `shuffle_files=False` (train)

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 72,103

*   **Feature structure**:

```python
FeaturesDict({
    'Q1_whole_conversation_evaluation': ClassLabel(shape=(), dtype=int64, num_classes=4),
    'Q2_harmful_content_explicitly_sexual': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_financial_advice': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_harm_to_people_or_animals': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_health_and_safety_claims': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_how_tos_about_harmful_activities': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_obscenities_or_profanities': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_other': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_overall': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_personal_information': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_promotes_or_condones_use_of_harmful_regulated_goods': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_promotes_or_condones_violence': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q2_harmful_content_violent_or_gory': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_3_Racial_religious_or_other_slurs_and_stereotypes_that_incites_or_promote_hatred_based_on_any_of_the_attributes_noted_above': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_calling_individuals_or_groups_evil_corrupt_or_malicious': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_incites_hatred': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_insults_about_emotional_romantic_and_or_sexual_attraction': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_other': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_physically_or_mentally_inferior': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_subhuman_comparisons': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_bias_superiority_or_subjugation_of_a_group': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q3_unfair_bias_overall': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q4_misinformation_conspiracy_theories': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q4_misinformation_contradicts_expert_consensus': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q4_misinformation_false_theories': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q4_misinformation_other': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q4_misinformation_overall': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q4_misinformation_political': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'Q_overall': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'context': Text(shape=(), dtype=string),
    'degree_of_harm': ClassLabel(shape=(), dtype=int64, num_classes=5),
    'harm_type': Sequence(ClassLabel(shape=(), dtype=int64, num_classes=32)),
    'id': Scalar(shape=(), dtype=int64, description=Numerical identifier for each row, representing all ratings by a single rater to a single conversation.),
    'item_id': Scalar(shape=(), dtype=int64, description=Numerical identifier for each conversation.),
    'phase': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'rater_age': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'rater_education': ClassLabel(shape=(), dtype=int64, num_classes=3),
    'rater_gender': ClassLabel(shape=(), dtype=int64, num_classes=4),
    'rater_id': Scalar(shape=(), dtype=int64, description=Numerical identifier for each rater.),
    'rater_locale': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'rater_race': ClassLabel(shape=(), dtype=int64, num_classes=6),
    'rater_raw_race': Text(shape=(), dtype=string),
    'response': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature                                                                                                                        | Class                | Shape   | Dtype  | Description
:----------------------------------------------------------------------------------------------------------------------------- | :------------------- | :------ | :----- | :----------
                                                                                                                               | FeaturesDict         |         |        |
Q1_whole_conversation_evaluation                                                                                               | ClassLabel           |         | int64  | Rating about the understandability of a conversation.
Q2_harmful_content_explicitly_sexual                                                                                           | ClassLabel           |         | int64  |
Q2_harmful_content_financial_advice                                                                                            | ClassLabel           |         | int64  |
Q2_harmful_content_harm_to_people_or_animals                                                                                   | ClassLabel           |         | int64  |
Q2_harmful_content_health_and_safety_claims                                                                                    | ClassLabel           |         | int64  |
Q2_harmful_content_how_tos_about_harmful_activities                                                                            | ClassLabel           |         | int64  |
Q2_harmful_content_obscenities_or_profanities                                                                                  | ClassLabel           |         | int64  |
Q2_harmful_content_other                                                                                                       | ClassLabel           |         | int64  |
Q2_harmful_content_overall                                                                                                     | ClassLabel           |         | int64  |
Q2_harmful_content_personal_information                                                                                        | ClassLabel           |         | int64  |
Q2_harmful_content_promotes_or_condones_use_of_harmful_regulated_goods                                                         | ClassLabel           |         | int64  |
Q2_harmful_content_promotes_or_condones_violence                                                                               | ClassLabel           |         | int64  |
Q2_harmful_content_violent_or_gory                                                                                             | ClassLabel           |         | int64  |
Q3_3_Racial_religious_or_other_slurs_and_stereotypes_that_incites_or_promote_hatred_based_on_any_of_the_attributes_noted_above | ClassLabel           |         | int64  |
Q3_bias_calling_individuals_or_groups_evil_corrupt_or_malicious                                                                | ClassLabel           |         | int64  |
Q3_bias_incites_hatred                                                                                                         | ClassLabel           |         | int64  |
Q3_bias_insults_about_emotional_romantic_and_or_sexual_attraction                                                              | ClassLabel           |         | int64  |
Q3_bias_other                                                                                                                  | ClassLabel           |         | int64  |
Q3_bias_physically_or_mentally_inferior                                                                                        | ClassLabel           |         | int64  |
Q3_bias_subhuman_comparisons                                                                                                   | ClassLabel           |         | int64  |
Q3_bias_superiority_or_subjugation_of_a_group                                                                                  | ClassLabel           |         | int64  |
Q3_unfair_bias_overall                                                                                                         | ClassLabel           |         | int64  |
Q4_misinformation_conspiracy_theories                                                                                          | ClassLabel           |         | int64  |
Q4_misinformation_contradicts_expert_consensus                                                                                 | ClassLabel           |         | int64  |
Q4_misinformation_false_theories                                                                                               | ClassLabel           |         | int64  |
Q4_misinformation_other                                                                                                        | ClassLabel           |         | int64  |
Q4_misinformation_overall                                                                                                      | ClassLabel           |         | int64  |
Q4_misinformation_political                                                                                                    | ClassLabel           |         | int64  |
Q_overall                                                                                                                      | ClassLabel           |         | int64  |
context                                                                                                                        | Text                 |         | string | The conversation turns before the final chatbot response.
degree_of_harm                                                                                                                 | ClassLabel           |         | int64  | Hand-annotated rating of severity of safety risk.
harm_type                                                                                                                      | Sequence(ClassLabel) | (None,) | int64  | Hand-annotated harm topic(s) of conversation.
id                                                                                                                             | Scalar               |         | int64  | Numerical identifier for each row, representing all ratings by a single rater to a single conversation.
item_id                                                                                                                        | Scalar               |         | int64  | Numerical identifier for each conversation.
phase                                                                                                                          | ClassLabel           |         | int64  | One of three distinct time periods.
rater_age                                                                                                                      | ClassLabel           |         | int64  | The age group of the rater.
rater_education                                                                                                                | ClassLabel           |         | int64  | The education of the rater.
rater_gender                                                                                                                   | ClassLabel           |         | int64  | The gender of the rater.
rater_id                                                                                                                       | Scalar               |         | int64  | Numerical identifier for each rater.
rater_locale                                                                                                                   | ClassLabel           |         | int64  | The locale of the rater.
rater_race                                                                                                                     | ClassLabel           |         | int64  | The race/ethnicity of the rater.
rater_raw_race                                                                                                                 | Text                 |         | string | The self-reported raw race/ethnicity of the rater, before simplification to five categories.
response                                                                                                                       | Text                 |         | string | The final chatbot response in the conversation.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dices-990-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->