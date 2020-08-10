<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="xquad" />
  <meta itemprop="description" content="XQuAD (Cross-lingual Question Answering Dataset) is a benchmark dataset for evaluating cross-lingual question answering performance. The dataset consists of a subset of 240 paragraphs and 1190 question-answer pairs from the development set of SQuAD v1.1 (Rajpurkar et al., 2016) together with their professional translations into ten languages: Spanish, German, Greek, Russian, Turkish, Arabic, Vietnamese, Thai, Chinese, and Hindi. Consequently, the dataset is entirely parallel across 11 languages. To run XQuAD in the default zero-shot setting, use the SQuAD v1.1 training and validation data here: https://www.tensorflow.org/datasets/catalog/squad&#10;&#10;We also include &quot;translate-train&quot;, &quot;translate-dev&quot;, and &quot;translate-test&quot; splits for each non-English language from XTREME (Hu et al., 2020). These can be used to run XQuAD in the &quot;translate-train&quot; or &quot;translate-test&quot; settings.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;xquad&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/xquad" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/xquad" />
  <meta itemprop="citation" content="@article{Artetxe:etal:2019,&#10;      author    = {Mikel Artetxe and Sebastian Ruder and Dani Yogatama},&#10;      title     = {On the cross-lingual transferability of monolingual representations},&#10;      journal   = {CoRR},&#10;      volume    = {abs/1910.11856},&#10;      year      = {2019},&#10;      archivePrefix = {arXiv},&#10;      eprint    = {1910.11856}&#10;}" />
</div>

# `xquad`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

XQuAD (Cross-lingual Question Answering Dataset) is a benchmark dataset for
evaluating cross-lingual question answering performance. The dataset consists of
a subset of 240 paragraphs and 1190 question-answer pairs from the development
set of SQuAD v1.1 (Rajpurkar et al., 2016) together with their professional
translations into ten languages: Spanish, German, Greek, Russian, Turkish,
Arabic, Vietnamese, Thai, Chinese, and Hindi. Consequently, the dataset is
entirely parallel across 11 languages. To run XQuAD in the default zero-shot
setting, use the SQuAD v1.1 training and validation data here:
https://www.tensorflow.org/datasets/catalog/squad

We also include "translate-train", "translate-dev", and "translate-test" splits
for each non-English language from XTREME (Hu et al., 2020). These can be used
to run XQuAD in the "translate-train" or "translate-test" settings.

*   **Homepage**:
    [https://github.com/deepmind/xquad](https://github.com/deepmind/xquad)

*   **Source code**:
    [`tfds.question_answering.Xquad`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/question_answering/xquad.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Features**:

```python
FeaturesDict({
    'answers': Sequence({
        'answer_start': tf.int32,
        'text': Text(shape=(), dtype=tf.string),
    }),
    'context': Text(shape=(), dtype=tf.string),
    'id': tf.string,
    'question': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@article{Artetxe:etal:2019,
      author    = {Mikel Artetxe and Sebastian Ruder and Dani Yogatama},
      title     = {On the cross-lingual transferability of monolingual representations},
      journal   = {CoRR},
      volume    = {abs/1910.11856},
      year      = {2019},
      archivePrefix = {arXiv},
      eprint    = {1910.11856}
}
```

*   **Visualization**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

## xquad/ar (default config)

*   **Config description**: XQuAD 'ar' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `420.97 MiB`

*   **Dataset size**: `126.23 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,541
`'translate-test'`  | 1,151
`'translate-train'` | 86,787

## xquad/de

*   **Config description**: XQuAD 'de' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `127.04 MiB`

*   **Dataset size**: `80.44 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,371
`'translate-test'`  | 1,168
`'translate-train'` | 82,603

## xquad/el

*   **Config description**: XQuAD 'el' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `499.40 MiB`

*   **Dataset size**: `225.17 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, translate-test, translate-dev), Only when `shuffle_files=False`
    (translate-train)

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,100
`'translate-test'`  | 1,182
`'translate-train'` | 79,946

## xquad/es

*   **Config description**: XQuAD 'es' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `138.41 MiB`

*   **Dataset size**: `57.55 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,566
`'translate-test'`  | 1,188
`'translate-train'` | 87,488

## xquad/hi

*   **Config description**: XQuAD 'hi' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `472.23 MiB`

*   **Dataset size**: `186.49 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, translate-test, translate-dev), Only when `shuffle_files=False`
    (translate-train)

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,536
`'translate-test'`  | 1,184
`'translate-train'` | 85,804

## xquad/ru

*   **Config description**: XQuAD 'ru' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `513.80 MiB`

*   **Dataset size**: `164.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, translate-test, translate-dev), Only when `shuffle_files=False`
    (translate-train)

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,469
`'translate-test'`  | 1,190
`'translate-train'` | 84,869

## xquad/th

*   **Config description**: XQuAD 'th' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `461.54 MiB`

*   **Dataset size**: `306.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,516
`'translate-test'`  | 1,157
`'translate-train'` | 85,846

## xquad/tr

*   **Config description**: XQuAD 'tr' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `151.08 MiB`

*   **Dataset size**: `109.93 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,535
`'translate-test'`  | 1,112
`'translate-train'` | 86,511

## xquad/vi

*   **Config description**: XQuAD 'vi' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `218.09 MiB`

*   **Dataset size**: `84.57 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,555
`'translate-test'`  | 1,178
`'translate-train'` | 87,187

## xquad/zh

*   **Config description**: XQuAD 'zh' test split, with machine-translated
    translate-train/translate-dev/translate-test splits from XTREME (Hu et al.,
    2020).

*   **Download size**: `174.57 MiB`

*   **Dataset size**: `50.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split               | Examples
:------------------ | -------:
`'test'`            | 1,190
`'translate-dev'`   | 10,475
`'translate-test'`  | 1,186
`'translate-train'` | 85,700

## xquad/en

*   **Config description**: XQuAD 'en' test split.

*   **Download size**: `595.10 KiB`

*   **Dataset size**: `873.86 KiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 1,190
