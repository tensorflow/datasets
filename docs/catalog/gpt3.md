<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="gpt3" />
  <meta itemprop="description" content="Synthetic datasets for word scramble and arithmetic tasks described in the GPT3 paper.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;gpt3&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/gpt3" />
  <meta itemprop="sameAs" content="https://github.com/openai/gpt-3" />
  <meta itemprop="citation" content="@article{brown2020language,&#10;    title={Language Models are Few-Shot Learners},&#10;    author={Tom B. Brown et. al.}&#10;    year={2020},&#10;    eprint={2005.14165},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}" />
</div>

# `gpt3`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Synthetic datasets for word scramble and arithmetic tasks described in the GPT3
paper.

*   **Config description**: Synthetic datasets for word scramble and arithmetic
    tasks described in the GPT3 paper.

*   **Homepage**:
    [https://github.com/openai/gpt-3](https://github.com/openai/gpt-3)

*   **Source code**:
    [`tfds.text.Gpt3`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/gpt3.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `2.15 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Features**:

```python
FeaturesDict({
    'completion': Text(shape=(), dtype=tf.string),
    'context': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('context', 'completion')`

*   **Citation**:

```
@article{brown2020language,
    title={Language Models are Few-Shot Learners},
    author={Tom B. Brown et. al.}
    year={2020},
    eprint={2005.14165},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

*   **Visualization**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

## gpt3/cycle_letters_in_word (default config)

*   **Dataset size**: `578.76 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 10,000

## gpt3/five_digit_addition

*   **Dataset size**: `154.76 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/five_digit_subtraction

*   **Dataset size**: `156.37 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/four_digit_addition

*   **Dataset size**: `148.99 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/four_digit_subtraction

*   **Dataset size**: `150.54 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/mid_word_1_anagrams

*   **Dataset size**: `567.89 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 10,000

## gpt3/mid_word_2_anagrams

*   **Dataset size**: `578.76 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 10,000

## gpt3/random_insertion_in_word

*   **Dataset size**: `648.42 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 10,000

## gpt3/reversed_words

*   **Dataset size**: `578.76 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 10,000

## gpt3/single_digit_three_ops

*   **Dataset size**: `138.33 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/six_digit_addition

*   **Dataset size**: `160.70 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/six_digit_subtraction

*   **Dataset size**: `162.26 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/sum_of_digits

*   **Dataset size**: `194.95 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/three_digit_addition

*   **Dataset size**: `143.18 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/three_digit_subtraction

*   **Dataset size**: `144.68 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/two_digit_addition

*   **Dataset size**: `137.33 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/two_digit_multiplication

*   **Dataset size**: `141.29 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000

## gpt3/two_digit_subtraction

*   **Dataset size**: `138.88 KiB`

*   **Splits**:

Split    | Examples
:------- | -------:
`'test'` | 2,000
