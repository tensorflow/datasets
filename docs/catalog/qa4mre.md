<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="qa4mre" />
  <meta itemprop="description" content="&#10;QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote research in &#10;question answering and reading comprehension. The dataset contains a supporting &#10;passage and a set of questions corresponding to the passage. Multiple options &#10;for answers are provided for each question, of which only one is correct. The &#10;training and test datasets are available for the main track.&#10;Additional gold standard documents are available for two pilot studies: one on &#10;alzheimers data, and the other on entrance exams data.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;qa4mre&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/qa4mre" />
  <meta itemprop="sameAs" content="http://nlp.uned.es/clef-qa/repository/pastCampaigns.php" />
  <meta itemprop="citation" content="&#10;@InProceedings{10.1007/978-3-642-40802-1_29,&#10;author=&quot;Pe{\~{n}}as, Anselmo&#10;and Hovy, Eduard&#10;and Forner, Pamela&#10;and Rodrigo, {&#x27;A}lvaro&#10;and Sutcliffe, Richard&#10;and Morante, Roser&quot;,&#10;editor=&quot;Forner, Pamela&#10;and M{&quot;u}ller, Henning&#10;and Paredes, Roberto&#10;and Rosso, Paolo&#10;and Stein, Benno&quot;,&#10;title=&quot;QA4MRE 2011-2013: Overview of Question Answering for Machine Reading Evaluation&quot;,&#10;booktitle=&quot;Information Access Evaluation. Multilinguality, Multimodality, and Visualization&quot;,&#10;year=&quot;2013&quot;,&#10;publisher=&quot;Springer Berlin Heidelberg&quot;,&#10;address=&quot;Berlin, Heidelberg&quot;,&#10;pages=&quot;303--320&quot;,&#10;abstract=&quot;This paper describes the methodology for testing the performance of Machine Reading systems through Question Answering and Reading Comprehension Tests. This was the attempt of the QA4MRE challenge which was run as a Lab at CLEF 2011--2013. The traditional QA task was replaced by a new Machine Reading task, whose intention was to ask questions that required a deep knowledge of individual short texts and in which systems were required to choose one answer, by analysing the corresponding test document in conjunction with background text collections provided by the organization. Four different tasks have been organized during these years: Main Task, Processing Modality and Negation for Machine Reading, Machine Reading of Biomedical Texts about Alzheimer&#x27;s disease, and Entrance Exams. This paper describes their motivation, their goals, their methodology for preparing the data sets, their background collections, their metrics used for the evaluation, and the lessons learned along these three years.&quot;,&#10;isbn=&quot;978-3-642-40802-1&quot;&#10;}&#10;" />
</div>
# `qa4mre`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data.

*   URL:
    [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)
*   `DatasetBuilder`:
    [`tfds.text.qa4mre.Qa4mre`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/qa4mre.py)

`qa4mre` is configured with `tfds.text.qa4mre.Qa4mreConfig` and has the
following configurations predefined (defaults to the first one):

*   `2011.main.DE` (`v0.1.0`) (`Size: 1.69 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for DE language in 2011 year.

*   `2011.main.EN` (`v0.1.0`) (`Size: 1.52 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for EN language in 2011 year.

*   `2011.main.ES` (`v0.1.0`) (`Size: 1.64 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for ES language in 2011 year.

*   `2011.main.IT` (`v0.1.0`) (`Size: 1.61 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for IT language in 2011 year.

*   `2011.main.RO` (`v0.1.0`) (`Size: 1.68 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for RO language in 2011 year.

*   `2012.main.AR` (`v0.1.0`) (`Size: 2.62 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for AR language in 2012 year.

*   `2012.main.BG` (`v0.1.0`) (`Size: 3.33 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for BG language in 2012 year.

*   `2012.main.DE` (`v0.1.0`) (`Size: 2.02 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for DE language in 2012 year.

*   `2012.main.EN` (`v0.1.0`) (`Size: 1.71 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for EN language in 2012 year.

*   `2012.main.ES` (`v0.1.0`) (`Size: 1.99 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for ES language in 2012 year.

*   `2012.main.IT` (`v0.1.0`) (`Size: 2.01 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for IT language in 2012 year.

*   `2012.main.RO` (`v0.1.0`) (`Size: 2.01 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for RO language in 2012 year.

*   `2012.alzheimers.EN` (`v0.1.0`) (`Size: 1.57 MiB`): QA4MRE dataset was
    created for the CLEF 2011/2012/2013 shared tasks to promote research in
    question answering and reading comprehension. The dataset contains a
    supporting passage and a set of questions corresponding to the passage.
    Multiple options for answers are provided for each question, of which only
    one is correct. The training and test datasets are available for the main
    track. Additional gold standard documents are available for two pilot
    studies: one on alzheimers data, and the other on entrance exams data. This
    configuration includes the alzheimers track for EN language in 2012 year.

*   `2013.main.AR` (`v0.1.0`) (`Size: 4.04 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for AR language in 2013 year.

*   `2013.main.BG` (`v0.1.0`) (`Size: 5.21 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for BG language in 2013 year.

*   `2013.main.EN` (`v0.1.0`) (`Size: 2.81 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for EN language in 2013 year.

*   `2013.main.ES` (`v0.1.0`) (`Size: 3.35 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for ES language in 2013 year.

*   `2013.main.RO` (`v0.1.0`) (`Size: 3.26 MiB`): QA4MRE dataset was created for
    the CLEF 2011/2012/2013 shared tasks to promote research in question
    answering and reading comprehension. The dataset contains a supporting
    passage and a set of questions corresponding to the passage. Multiple
    options for answers are provided for each question, of which only one is
    correct. The training and test datasets are available for the main track.
    Additional gold standard documents are available for two pilot studies: one
    on alzheimers data, and the other on entrance exams data. This configuration
    includes the main track for RO language in 2013 year.

*   `2013.alzheimers.EN` (`v0.1.0`) (`Size: 2.50 MiB`): QA4MRE dataset was
    created for the CLEF 2011/2012/2013 shared tasks to promote research in
    question answering and reading comprehension. The dataset contains a
    supporting passage and a set of questions corresponding to the passage.
    Multiple options for answers are provided for each question, of which only
    one is correct. The training and test datasets are available for the main
    track. Additional gold standard documents are available for two pilot
    studies: one on alzheimers data, and the other on entrance exams data. This
    configuration includes the alzheimers track for EN language in 2013 year.

*   `2013.entrance_exam.EN` (`v0.1.0`) (`Size: 186.01 KiB`): QA4MRE dataset was
    created for the CLEF 2011/2012/2013 shared tasks to promote research in
    question answering and reading comprehension. The dataset contains a
    supporting passage and a set of questions corresponding to the passage.
    Multiple options for answers are provided for each question, of which only
    one is correct. The training and test datasets are available for the main
    track. Additional gold standard documents are available for two pilot
    studies: one on alzheimers data, and the other on entrance exams data. This
    configuration includes the entrance_exam track for EN language in 2013 year.

## `qa4mre/2011.main.DE`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for DE language in 2011 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 120
TRAIN | 120

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2011.main.EN`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for EN language in 2011 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 120
TRAIN | 120

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2011.main.ES`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for ES language in 2011 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 120
TRAIN | 120

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2011.main.IT`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for IT language in 2011 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 120
TRAIN | 120

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2011.main.RO`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for RO language in 2011 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 120
TRAIN | 120

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2012.main.AR`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for AR language in 2012 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 160
TRAIN | 160

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2012.main.BG`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for BG language in 2012 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 160
TRAIN | 160

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2012.main.DE`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for DE language in 2012 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 160
TRAIN | 160

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2012.main.EN`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for EN language in 2012 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 160
TRAIN | 160

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2012.main.ES`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for ES language in 2012 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 160
TRAIN | 160

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2012.main.IT`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for IT language in 2012 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 160
TRAIN | 160

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2012.main.RO`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for RO language in 2012 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 160
TRAIN | 160

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2012.alzheimers.EN`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the alzheimers track for EN language in 2012 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 40
TRAIN | 40

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2013.main.AR`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for AR language in 2013 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 284
TRAIN | 284

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2013.main.BG`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for BG language in 2013 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 284
TRAIN | 284

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2013.main.EN`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for EN language in 2013 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 284
TRAIN | 284

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2013.main.ES`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for ES language in 2013 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 284
TRAIN | 284

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2013.main.RO`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the main track for RO language in 2013 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 284
TRAIN | 284

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2013.alzheimers.EN`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the alzheimers track for EN language in 2013 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 40
TRAIN | 40

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## `qa4mre/2013.entrance_exam.EN`

QA4MRE dataset was created for the CLEF 2011/2012/2013 shared tasks to promote
research in question answering and reading comprehension. The dataset contains a
supporting passage and a set of questions corresponding to the passage. Multiple
options for answers are provided for each question, of which only one is
correct. The training and test datasets are available for the main track.
Additional gold standard documents are available for two pilot studies: one on
alzheimers data, and the other on entrance exams data. This configuration
includes the entrance_exam track for EN language in 2013 year.

Versions:

*   **`0.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 46
TRAIN | 46

### Features
```python
FeaturesDict({
    'answer_options': Sequence({
        'answer_id': Text(shape=(), dtype=tf.string),
        'answer_str': Text(shape=(), dtype=tf.string),
    }),
    'correct_answer_id': Text(shape=(), dtype=tf.string),
    'correct_answer_str': Text(shape=(), dtype=tf.string),
    'document_id': Text(shape=(), dtype=tf.string),
    'document_str': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_str': Text(shape=(), dtype=tf.string),
    'test_id': Text(shape=(), dtype=tf.string),
    'topic_id': Text(shape=(), dtype=tf.string),
    'topic_name': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [http://nlp.uned.es/clef-qa/repository/pastCampaigns.php](http://nlp.uned.es/clef-qa/repository/pastCampaigns.php)

## Citation
```
@InProceedings{10.1007/978-3-642-40802-1_29,
author="Pe{\~{n}}as, Anselmo
and Hovy, Eduard
and Forner, Pamela
and Rodrigo, {'A}lvaro
and Sutcliffe, Richard
and Morante, Roser",
editor="Forner, Pamela
and M{"u}ller, Henning
and Paredes, Roberto
and Rosso, Paolo
and Stein, Benno",
title="QA4MRE 2011-2013: Overview of Question Answering for Machine Reading Evaluation",
booktitle="Information Access Evaluation. Multilinguality, Multimodality, and Visualization",
year="2013",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="303--320",
abstract="This paper describes the methodology for testing the performance of Machine Reading systems through Question Answering and Reading Comprehension Tests. This was the attempt of the QA4MRE challenge which was run as a Lab at CLEF 2011--2013. The traditional QA task was replaced by a new Machine Reading task, whose intention was to ask questions that required a deep knowledge of individual short texts and in which systems were required to choose one answer, by analysing the corresponding test document in conjunction with background text collections provided by the organization. Four different tasks have been organized during these years: Main Task, Processing Modality and Negation for Machine Reading, Machine Reading of Biomedical Texts about Alzheimer's disease, and Entrance Exams. This paper describes their motivation, their goals, their methodology for preparing the data sets, their background collections, their metrics used for the evaluation, and the lessons learned along these three years.",
isbn="978-3-642-40802-1"
}
```

--------------------------------------------------------------------------------
