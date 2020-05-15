<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="cfq" />
  <meta itemprop="description" content="The CFQ dataset (and it&#x27;s splits) for measuring compositional generalization.&#10;&#10;See https://arxiv.org/abs/1912.09713.pdf for background.&#10;&#10;A note about the validation set: Since it has the same distribution as the test&#10;set and we are interested in measuring the compositional generalization of a&#10;*model* with respect to an *unknown* test distribution we suggest that any&#10;tuning should be done on a subset of the train set only (see section 5.1 of the&#10;paper).&#10;&#10;Example usage:&#10;&#10;```&#10;data = tfds.load(&#x27;cfq/mcd1&#x27;)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cfq&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cfq" />
  <meta itemprop="sameAs" content="https://github.com/google-research/google-research/tree/master/cfq" />
  <meta itemprop="citation" content="@inproceedings{Keysers2020,&#10;  title={Measuring Compositional Generalization: A Comprehensive Method on&#10;         Realistic Data},&#10;  author={Daniel Keysers and Nathanael Sch&quot;{a}rli and Nathan Scales and&#10;          Hylke Buisman and Daniel Furrer and Sergii Kashubin and&#10;          Nikola Momchev and Danila Sinopalnikov and Lukasz Stafiniak and&#10;          Tibor Tihon and Dmitry Tsarkov and Xiao Wang and Marc van Zee and&#10;          Olivier Bousquet},&#10;  booktitle={ICLR},&#10;  year={2020},&#10;  url={https://arxiv.org/abs/1912.09713.pdf},&#10;}" />
</div>

# `cfq`

Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

*   **Description**:

The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

A note about the validation set: Since it has the same distribution as the test
set and we are interested in measuring the compositional generalization of a
*model* with respect to an *unknown* test distribution we suggest that any
tuning should be done on a subset of the train set only (see section 5.1 of the
paper).

Example usage:

```
data = tfds.load('cfq/mcd1')
```

*   **Config description**: The CFQ dataset (and it's splits) for measuring
    compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

A note about the validation set: Since it has the same distribution as the test
set and we are interested in measuring the compositional generalization of a
*model* with respect to an *unknown* test distribution we suggest that any
tuning should be done on a subset of the train set only (see section 5.1 of the
paper).

Example usage:

```
data = tfds.load('cfq/mcd1')
```

*   **Homepage**:
    [https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)
*   **Source code**:
    [`tfds.text.cfq.CFQ`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/cfq.py)
*   **Versions**:
    *   **`1.2.0`** (default)
        <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>:
        No release notes.
*   **Features**:

```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```
*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('question', 'query')`
*   **Citation**:

```
@inproceedings{Keysers2020,
  title={Measuring Compositional Generalization: A Comprehensive Method on
         Realistic Data},
  author={Daniel Keysers and Nathanael Sch"{a}rli and Nathan Scales and
          Hylke Buisman and Daniel Furrer and Sergii Kashubin and
          Nikola Momchev and Danila Sinopalnikov and Lukasz Stafiniak and
          Tibor Tihon and Dmitry Tsarkov and Xiao Wang and Marc van Zee and
          Olivier Bousquet},
  booktitle={ICLR},
  year={2020},
  url={https://arxiv.org/abs/1912.09713.pdf},
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.

## cfq/mcd1 (default config)

*   **Download size**: `255.20 MiB`
*   **Dataset size**: `49.75 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 11,968
'train'      | 95,743
'validation' | 11,968

## cfq/mcd2

*   **Download size**: `255.20 MiB`
*   **Dataset size**: `51.39 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 11,968
'train'      | 95,743
'validation' | 11,968

## cfq/mcd3

*   **Download size**: `255.20 MiB`
*   **Dataset size**: `50.22 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 11,968
'train'      | 95,743
'validation' | 11,968

## cfq/question_complexity_split

*   **Download size**: `255.20 MiB`
*   **Dataset size**: `52.81 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 10,340
'train'      | 98,999
'validation' | 10,339

## cfq/question_pattern_split

*   **Download size**: `255.20 MiB`
*   **Dataset size**: `52.81 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 11,909
'train'      | 95,654
'validation' | 12,115

## cfq/query_complexity_split

*   **Download size**: `255.20 MiB`
*   **Dataset size**: `52.81 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 9,512
'train'      | 100,654
'validation' | 9,512

## cfq/query_pattern_split

*   **Download size**: `255.20 MiB`
*   **Dataset size**: `52.81 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 12,589
'train'      | 94,600
'validation' | 12,489

## cfq/random_split

*   **Download size**: `255.20 MiB`
*   **Dataset size**: `52.81 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 11,967
'train'      | 95,744
'validation' | 11,967

## cfq/cd0_r1 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0_r2 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0_r3 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0_r4 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0_r5 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0_r6 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0_r7 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0_r8 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0_r9 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.1_r1 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.1_r2 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.1_r3 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.1_r4 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.1_r5 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.1_r6 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.1_r7 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.1_r8 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.1_r9 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.2_r1 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.2_r2 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.2_r3 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.2_r4 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.2_r5 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.2_r6 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.2_r7 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.2_r8 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.2_r9 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.3_r1 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.3_r2 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.3_r3 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.3_r4 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.3_r5 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.3_r6 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.3_r7 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.3_r8 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.3_r9 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.4_r1 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.4_r2 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.4_r3 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.4_r4 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.4_r5 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.4_r6 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.4_r7 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.4_r8 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.4_r9 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.5_r1 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.5_r2 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.5_r3 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.5_r4 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.5_r5 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.5_r6 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.5_r7 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.5_r8 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.5_r9 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.6_r1 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.6_r2 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.6_r3 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.6_r4 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.6_r5 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.6_r6 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.6_r7 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.6_r8 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd0.6_r9 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd1_r1 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd1_r2 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd1_r3 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd1_r4 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd1_r5 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd1_r6 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd1_r7 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd1_r8 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## cfq/cd1_r9 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:
