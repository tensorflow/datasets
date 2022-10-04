<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="civil_comments" />
  <meta itemprop="description" content="This version of the CivilComments Dataset provides access to the primary&#10;seven labels that were annotated by crowd workers, the toxicity and other&#10;tags are a value between 0 and 1 indicating the fraction of annotators that&#10;assigned these attributes to the comment text.&#10;&#10;The other tags are only available for a fraction of the input examples. They&#10;are currently ignored for the main dataset; the CivilCommentsIdentities set&#10;includes those labels, but only consists of the subset of the data with them.&#10;The other attributes that were part of the original CivilComments release are&#10;included only in the raw data. See the Kaggle documentation for more details&#10;about the available features.&#10;&#10;The comments in this dataset come from an archive of the Civil Comments&#10;platform, a commenting plugin for independent news sites. These public comments&#10;were created from 2015 - 2017 and appeared on approximately 50 English-language&#10;news sites across the world. When Civil Comments shut down in 2017, they chose&#10;to make the public comments available in a lasting open archive to enable future&#10;research. The original data, published on figshare, includes the public comment&#10;text, some associated metadata such as article IDs, timestamps and&#10;commenter-generated &quot;civility&quot; labels, but does not include user ids. Jigsaw&#10;extended this dataset by adding additional labels for toxicity, identity&#10;mentions, as well as covert offensiveness. This data set is an exact replica of&#10;the data released for the Jigsaw Unintended Bias in Toxicity Classification&#10;Kaggle challenge. This dataset is released under CC0, as is the underlying&#10;comment text.&#10;&#10;For comments that have a parent_id also in the civil comments data, the&#10;text of the previous comment is provided as the &quot;parent_text&quot; feature. Note&#10;that the splits were made without regard to this information, so using previous&#10;comments may leak some information. The annotators did not have access to the&#10;parent text when making the labels.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;civil_comments&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/civil_comments" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-1903-04561,&#10;  author    = {Daniel Borkan and&#10;               Lucas Dixon and&#10;               Jeffrey Sorensen and&#10;               Nithum Thain and&#10;               Lucy Vasserman},&#10;  title     = {Nuanced Metrics for Measuring Unintended Bias with Real Data for Text&#10;               Classification},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1903.04561},&#10;  year      = {2019},&#10;  url       = {http://arxiv.org/abs/1903.04561},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1903.04561},&#10;  timestamp = {Sun, 31 Mar 2019 19:01:24 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1903-04561},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `civil_comments`


*   **Description**:

This version of the CivilComments Dataset provides access to the primary seven
labels that were annotated by crowd workers, the toxicity and other tags are a
value between 0 and 1 indicating the fraction of annotators that assigned these
attributes to the comment text.

The other tags are only available for a fraction of the input examples. They are
currently ignored for the main dataset; the CivilCommentsIdentities set includes
those labels, but only consists of the subset of the data with them. The other
attributes that were part of the original CivilComments release are included
only in the raw data. See the Kaggle documentation for more details about the
available features.

The comments in this dataset come from an archive of the Civil Comments
platform, a commenting plugin for independent news sites. These public comments
were created from 2015 - 2017 and appeared on approximately 50 English-language
news sites across the world. When Civil Comments shut down in 2017, they chose
to make the public comments available in a lasting open archive to enable future
research. The original data, published on figshare, includes the public comment
text, some associated metadata such as article IDs, timestamps and
commenter-generated "civility" labels, but does not include user ids. Jigsaw
extended this dataset by adding additional labels for toxicity, identity
mentions, as well as covert offensiveness. This data set is an exact replica of
the data released for the Jigsaw Unintended Bias in Toxicity Classification
Kaggle challenge. This dataset is released under CC0, as is the underlying
comment text.

For comments that have a parent_id also in the civil comments data, the text of
the previous comment is provided as the "parent_text" feature. Note that the
splits were made without regard to this information, so using previous comments
may leak some information. The annotators did not have access to the parent text
when making the labels.

*   **Homepage**:
    [https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data)

*   **Source code**:
    [`tfds.text.CivilComments`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/civil_comments.py)

*   **Versions**:

    *   `1.0.0`: Initial full release.
    *   `1.0.1`: Added a unique id for each comment.
    *   `1.1.0`: Added CivilCommentsCovert config.
    *   `1.1.1`: Added CivilCommentsCovert config with correct checksum.
    *   `1.1.2`: Added separate citation for CivilCommentsCovert dataset.
    *   `1.1.3`: Corrected id types from float to string.
    *   `1.2.0`: Add toxic spans, context, and parent comment text features.
    *   `1.2.1`: Fix incorrect formatting in context splits.
    *   `1.2.2`: Update to reflect context only having a train split.
    *   **`1.2.3`** (default): Add warning to CivilCommentsCovert as we fix a
        data issue.

*   **Download size**: `427.41 MiB`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.


## civil_comments/CivilComments (default config)

*   **Config description**: The CivilComments set here includes all the data,
    but only the basic seven labels (toxicity, severe_toxicity, obscene, threat,
    insult, identity_attack, and sexual_explicit).

*   **Dataset size**: `1.39 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 97,320
`'train'`      | 1,804,874
`'validation'` | 97,320

*   **Feature structure**:

```python
FeaturesDict({
    'article_id': tf.int32,
    'id': tf.string,
    'identity_attack': tf.float32,
    'insult': tf.float32,
    'obscene': tf.float32,
    'parent_id': tf.int32,
    'parent_text': Text(shape=(), dtype=tf.string),
    'severe_toxicity': tf.float32,
    'sexual_explicit': tf.float32,
    'text': Text(shape=(), dtype=tf.string),
    'threat': tf.float32,
    'toxicity': tf.float32,
})
```

*   **Feature documentation**:

Feature         | Class        | Shape | Dtype      | Description
:-------------- | :----------- | :---- | :--------- | :----------
                | FeaturesDict |       |            |
article_id      | Tensor       |       | tf.int32   |
id              | Tensor       |       | tf.string  |
identity_attack | Tensor       |       | tf.float32 |
insult          | Tensor       |       | tf.float32 |
obscene         | Tensor       |       | tf.float32 |
parent_id       | Tensor       |       | tf.int32   |
parent_text     | Text         |       | tf.string  |
severe_toxicity | Tensor       |       | tf.float32 |
sexual_explicit | Tensor       |       | tf.float32 |
text            | Text         |       | tf.string  |
threat          | Tensor       |       | tf.float32 |
toxicity        | Tensor       |       | tf.float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'toxicity')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/civil_comments-CivilComments-1.2.3.html";
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

*   **Citation**:

```
@article{DBLP:journals/corr/abs-1903-04561,
  author    = {Daniel Borkan and
               Lucas Dixon and
               Jeffrey Sorensen and
               Nithum Thain and
               Lucy Vasserman},
  title     = {Nuanced Metrics for Measuring Unintended Bias with Real Data for Text
               Classification},
  journal   = {CoRR},
  volume    = {abs/1903.04561},
  year      = {2019},
  url       = {http://arxiv.org/abs/1903.04561},
  archivePrefix = {arXiv},
  eprint    = {1903.04561},
  timestamp = {Sun, 31 Mar 2019 19:01:24 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1903-04561},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## civil_comments/CivilCommentsIdentities

*   **Config description**: The CivilCommentsIdentities set here includes an
    extended set of identity labels in addition to the basic seven labels.
    However, it only includes the subset (roughly a quarter) of the data with
    all these features.

*   **Dataset size**: `622.02 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 21,577
`'train'`      | 405,130
`'validation'` | 21,293

*   **Feature structure**:

```python
FeaturesDict({
    'article_id': tf.int32,
    'asian': tf.float32,
    'atheist': tf.float32,
    'bisexual': tf.float32,
    'black': tf.float32,
    'buddhist': tf.float32,
    'christian': tf.float32,
    'female': tf.float32,
    'heterosexual': tf.float32,
    'hindu': tf.float32,
    'homosexual_gay_or_lesbian': tf.float32,
    'id': tf.string,
    'identity_attack': tf.float32,
    'insult': tf.float32,
    'intellectual_or_learning_disability': tf.float32,
    'jewish': tf.float32,
    'latino': tf.float32,
    'male': tf.float32,
    'muslim': tf.float32,
    'obscene': tf.float32,
    'other_disability': tf.float32,
    'other_gender': tf.float32,
    'other_race_or_ethnicity': tf.float32,
    'other_religion': tf.float32,
    'other_sexual_orientation': tf.float32,
    'parent_id': tf.int32,
    'parent_text': Text(shape=(), dtype=tf.string),
    'physical_disability': tf.float32,
    'psychiatric_or_mental_illness': tf.float32,
    'severe_toxicity': tf.float32,
    'sexual_explicit': tf.float32,
    'text': Text(shape=(), dtype=tf.string),
    'threat': tf.float32,
    'toxicity': tf.float32,
    'transgender': tf.float32,
    'white': tf.float32,
})
```

*   **Feature documentation**:

Feature                             | Class        | Shape | Dtype      | Description
:---------------------------------- | :----------- | :---- | :--------- | :----------
                                    | FeaturesDict |       |            |
article_id                          | Tensor       |       | tf.int32   |
asian                               | Tensor       |       | tf.float32 |
atheist                             | Tensor       |       | tf.float32 |
bisexual                            | Tensor       |       | tf.float32 |
black                               | Tensor       |       | tf.float32 |
buddhist                            | Tensor       |       | tf.float32 |
christian                           | Tensor       |       | tf.float32 |
female                              | Tensor       |       | tf.float32 |
heterosexual                        | Tensor       |       | tf.float32 |
hindu                               | Tensor       |       | tf.float32 |
homosexual_gay_or_lesbian           | Tensor       |       | tf.float32 |
id                                  | Tensor       |       | tf.string  |
identity_attack                     | Tensor       |       | tf.float32 |
insult                              | Tensor       |       | tf.float32 |
intellectual_or_learning_disability | Tensor       |       | tf.float32 |
jewish                              | Tensor       |       | tf.float32 |
latino                              | Tensor       |       | tf.float32 |
male                                | Tensor       |       | tf.float32 |
muslim                              | Tensor       |       | tf.float32 |
obscene                             | Tensor       |       | tf.float32 |
other_disability                    | Tensor       |       | tf.float32 |
other_gender                        | Tensor       |       | tf.float32 |
other_race_or_ethnicity             | Tensor       |       | tf.float32 |
other_religion                      | Tensor       |       | tf.float32 |
other_sexual_orientation            | Tensor       |       | tf.float32 |
parent_id                           | Tensor       |       | tf.int32   |
parent_text                         | Text         |       | tf.string  |
physical_disability                 | Tensor       |       | tf.float32 |
psychiatric_or_mental_illness       | Tensor       |       | tf.float32 |
severe_toxicity                     | Tensor       |       | tf.float32 |
sexual_explicit                     | Tensor       |       | tf.float32 |
text                                | Text         |       | tf.string  |
threat                              | Tensor       |       | tf.float32 |
toxicity                            | Tensor       |       | tf.float32 |
transgender                         | Tensor       |       | tf.float32 |
white                               | Tensor       |       | tf.float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'toxicity')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/civil_comments-CivilCommentsIdentities-1.2.3.html";
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

*   **Citation**:

```
@article{DBLP:journals/corr/abs-1903-04561,
  author    = {Daniel Borkan and
               Lucas Dixon and
               Jeffrey Sorensen and
               Nithum Thain and
               Lucy Vasserman},
  title     = {Nuanced Metrics for Measuring Unintended Bias with Real Data for Text
               Classification},
  journal   = {CoRR},
  volume    = {abs/1903.04561},
  year      = {2019},
  url       = {http://arxiv.org/abs/1903.04561},
  archivePrefix = {arXiv},
  eprint    = {1903.04561},
  timestamp = {Sun, 31 Mar 2019 19:01:24 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1903-04561},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## civil_comments/CivilCommentsCovert

*   **Config description**: WARNING: there's a potential data quality issue with
    CivilCommentsCovert that we're actively working on fixing (06/28/22); the
    underlying data may change!

The CivilCommentsCovert set is a subset of CivilCommentsIdentities with ~20% of
the train and test splits further annotated for covert offensiveness, in
addition to the toxicity and identity labels. Raters were asked to categorize
comments as one of explicitly, implicitly, not, or not sure if offensive, as
well as whether it contained different types of covert offensiveness. The full
annotation procedure is detailed in a forthcoming paper at
https://sites.google.com/corp/view/hciandnlp/accepted-papers.

*   **Dataset size**: `94.12 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,455
`'train'` | 48,074

*   **Feature structure**:

```python
FeaturesDict({
    'article_id': tf.int32,
    'asian': tf.float32,
    'atheist': tf.float32,
    'bisexual': tf.float32,
    'black': tf.float32,
    'buddhist': tf.float32,
    'christian': tf.float32,
    'covert_emoticons_emojis': tf.float32,
    'covert_humor': tf.float32,
    'covert_masked_harm': tf.float32,
    'covert_microaggression': tf.float32,
    'covert_obfuscation': tf.float32,
    'covert_political': tf.float32,
    'covert_sarcasm': tf.float32,
    'explicitly_offensive': tf.float32,
    'female': tf.float32,
    'heterosexual': tf.float32,
    'hindu': tf.float32,
    'homosexual_gay_or_lesbian': tf.float32,
    'id': tf.string,
    'identity_attack': tf.float32,
    'implicitly_offensive': tf.float32,
    'insult': tf.float32,
    'intellectual_or_learning_disability': tf.float32,
    'jewish': tf.float32,
    'latino': tf.float32,
    'male': tf.float32,
    'muslim': tf.float32,
    'not_offensive': tf.float32,
    'not_sure_offensive': tf.float32,
    'obscene': tf.float32,
    'other_disability': tf.float32,
    'other_gender': tf.float32,
    'other_race_or_ethnicity': tf.float32,
    'other_religion': tf.float32,
    'other_sexual_orientation': tf.float32,
    'parent_id': tf.int32,
    'parent_text': Text(shape=(), dtype=tf.string),
    'physical_disability': tf.float32,
    'psychiatric_or_mental_illness': tf.float32,
    'severe_toxicity': tf.float32,
    'sexual_explicit': tf.float32,
    'text': Text(shape=(), dtype=tf.string),
    'threat': tf.float32,
    'toxicity': tf.float32,
    'transgender': tf.float32,
    'white': tf.float32,
})
```

*   **Feature documentation**:

Feature                             | Class        | Shape | Dtype      | Description
:---------------------------------- | :----------- | :---- | :--------- | :----------
                                    | FeaturesDict |       |            |
article_id                          | Tensor       |       | tf.int32   |
asian                               | Tensor       |       | tf.float32 |
atheist                             | Tensor       |       | tf.float32 |
bisexual                            | Tensor       |       | tf.float32 |
black                               | Tensor       |       | tf.float32 |
buddhist                            | Tensor       |       | tf.float32 |
christian                           | Tensor       |       | tf.float32 |
covert_emoticons_emojis             | Tensor       |       | tf.float32 |
covert_humor                        | Tensor       |       | tf.float32 |
covert_masked_harm                  | Tensor       |       | tf.float32 |
covert_microaggression              | Tensor       |       | tf.float32 |
covert_obfuscation                  | Tensor       |       | tf.float32 |
covert_political                    | Tensor       |       | tf.float32 |
covert_sarcasm                      | Tensor       |       | tf.float32 |
explicitly_offensive                | Tensor       |       | tf.float32 |
female                              | Tensor       |       | tf.float32 |
heterosexual                        | Tensor       |       | tf.float32 |
hindu                               | Tensor       |       | tf.float32 |
homosexual_gay_or_lesbian           | Tensor       |       | tf.float32 |
id                                  | Tensor       |       | tf.string  |
identity_attack                     | Tensor       |       | tf.float32 |
implicitly_offensive                | Tensor       |       | tf.float32 |
insult                              | Tensor       |       | tf.float32 |
intellectual_or_learning_disability | Tensor       |       | tf.float32 |
jewish                              | Tensor       |       | tf.float32 |
latino                              | Tensor       |       | tf.float32 |
male                                | Tensor       |       | tf.float32 |
muslim                              | Tensor       |       | tf.float32 |
not_offensive                       | Tensor       |       | tf.float32 |
not_sure_offensive                  | Tensor       |       | tf.float32 |
obscene                             | Tensor       |       | tf.float32 |
other_disability                    | Tensor       |       | tf.float32 |
other_gender                        | Tensor       |       | tf.float32 |
other_race_or_ethnicity             | Tensor       |       | tf.float32 |
other_religion                      | Tensor       |       | tf.float32 |
other_sexual_orientation            | Tensor       |       | tf.float32 |
parent_id                           | Tensor       |       | tf.int32   |
parent_text                         | Text         |       | tf.string  |
physical_disability                 | Tensor       |       | tf.float32 |
psychiatric_or_mental_illness       | Tensor       |       | tf.float32 |
severe_toxicity                     | Tensor       |       | tf.float32 |
sexual_explicit                     | Tensor       |       | tf.float32 |
text                                | Text         |       | tf.string  |
threat                              | Tensor       |       | tf.float32 |
toxicity                            | Tensor       |       | tf.float32 |
transgender                         | Tensor       |       | tf.float32 |
white                               | Tensor       |       | tf.float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'toxicity')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/civil_comments-CivilCommentsCovert-1.2.3.html";
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

*   **Citation**:

```
@inproceedings{lees-etal-2021-capturing,
    title = "Capturing Covertly Toxic Speech via Crowdsourcing",
    author = "Lees, Alyssa  and
      Borkan, Daniel  and
      Kivlichan, Ian  and
      Nario, Jorge  and
      Goyal, Tesh",
    booktitle = "Proceedings of the First Workshop on Bridging Human{--}Computer Interaction and Natural Language Processing",
    month = apr,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2021.hcinlp-1.3",
    pages = "14--20"
}
```

## civil_comments/CivilCommentsToxicSpans

*   **Config description**: The CivilComments Toxic Spans are a subset of
    CivilComments that is labeled at the span level - the indices of all
    character (unicode codepoints) boundaries that were tagged as toxic by a
    majority of the annotators is returned in a 'spans' feature.

*   **Dataset size**: `5.03 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,000
`'train'`      | 7,939
`'validation'` | 682

*   **Feature structure**:

```python
FeaturesDict({
    'article_id': tf.int32,
    'id': tf.string,
    'parent_id': tf.int32,
    'parent_text': Text(shape=(), dtype=tf.string),
    'spans': Tensor(shape=(None,), dtype=tf.int32),
    'text': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature     | Class        | Shape   | Dtype     | Description
:---------- | :----------- | :------ | :-------- | :----------
            | FeaturesDict |         |           |
article_id  | Tensor       |         | tf.int32  |
id          | Tensor       |         | tf.string |
parent_id   | Tensor       |         | tf.int32  |
parent_text | Text         |         | tf.string |
spans       | Tensor       | (None,) | tf.int32  |
text        | Text         |         | tf.string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'spans')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/civil_comments-CivilCommentsToxicSpans-1.2.3.html";
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

*   **Citation**:

```
@inproceedings{pavlopoulos-etal-2021-semeval,
    title = "{S}em{E}val-2021 Task 5: Toxic Spans Detection",
    author = "Pavlopoulos, John  and Sorensen, Jeffrey  and Laugier, L{'e}o and Androutsopoulos, Ion",
    booktitle = "Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.semeval-1.6",
    doi = "10.18653/v1/2021.semeval-1.6",
    pages = "59--69",
}
```

## civil_comments/CivilCommentsInContext

*   **Config description**: The CivilComments in Context is a subset of
    CivilComments that was labeled by making available to the labelers the
    parent_text. It includes a contextual_toxicity feature.

*   **Dataset size**: `8.90 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,969

*   **Feature structure**:

```python
FeaturesDict({
    'article_id': tf.int32,
    'contextual_toxicity': tf.float32,
    'id': tf.string,
    'identity_attack': tf.float32,
    'insult': tf.float32,
    'obscene': tf.float32,
    'parent_id': tf.int32,
    'parent_text': Text(shape=(), dtype=tf.string),
    'severe_toxicity': tf.float32,
    'sexual_explicit': tf.float32,
    'text': Text(shape=(), dtype=tf.string),
    'threat': tf.float32,
    'toxicity': tf.float32,
})
```

*   **Feature documentation**:

Feature             | Class        | Shape | Dtype      | Description
:------------------ | :----------- | :---- | :--------- | :----------
                    | FeaturesDict |       |            |
article_id          | Tensor       |       | tf.int32   |
contextual_toxicity | Tensor       |       | tf.float32 |
id                  | Tensor       |       | tf.string  |
identity_attack     | Tensor       |       | tf.float32 |
insult              | Tensor       |       | tf.float32 |
obscene             | Tensor       |       | tf.float32 |
parent_id           | Tensor       |       | tf.int32   |
parent_text         | Text         |       | tf.string  |
severe_toxicity     | Tensor       |       | tf.float32 |
sexual_explicit     | Tensor       |       | tf.float32 |
text                | Text         |       | tf.string  |
threat              | Tensor       |       | tf.float32 |
toxicity            | Tensor       |       | tf.float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'toxicity')`

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/civil_comments-CivilCommentsInContext-1.2.3.html";
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

*   **Citation**:

```
@misc{pavlopoulos2020toxicity,
    title={Toxicity Detection: Does Context Really Matter?},
    author={John Pavlopoulos and Jeffrey Sorensen and Lucas Dixon and Nithum Thain and Ion Androutsopoulos},
    year={2020}, eprint={2006.00998}, archivePrefix={arXiv}, primaryClass={cs.CL}
}
```
