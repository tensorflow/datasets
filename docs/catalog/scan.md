<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="scan" />
  <meta itemprop="description" content="SCAN tasks with various splits.&#10;&#10;SCAN is a set of simple language-driven navigation tasks for studying&#10;compositional learning and zero-shot generalization.&#10;&#10;Most splits are described at https://github.com/brendenlake/SCAN. For the MCD&#10;splits please see https://arxiv.org/abs/1912.09713.pdf.&#10;&#10;Basic usage:&#10;&#10;```&#10;data = tfds.load(&#x27;scan/length&#x27;)&#10;```&#10;&#10;More advanced example:&#10;&#10;```&#10;data = tfds.load(&#10;    &#x27;scan&#x27;,&#10;    builder_kwargs=dict(&#10;        config=tfds.text.ScanConfig(&#10;            name=&#x27;simple_p8&#x27;, directory=&#x27;simple_split/size_variations&#x27;)))&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;scan&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/scan" />
  <meta itemprop="sameAs" content="https://github.com/brendenlake/SCAN" />
  <meta itemprop="citation" content="@inproceedings{Lake2018GeneralizationWS,&#10;  title={Generalization without Systematicity: On the Compositional Skills of&#10;         Sequence-to-Sequence Recurrent Networks},&#10;  author={Brenden M. Lake and Marco Baroni},&#10;  booktitle={ICML},&#10;  year={2018},&#10;  url={https://arxiv.org/pdf/1711.00350.pdf},&#10;}&#10;@inproceedings{Keysers2020,&#10;  title={Measuring Compositional Generalization: A Comprehensive Method on&#10;         Realistic Data},&#10;  author={Daniel Keysers and Nathanael Sch&quot;{a}rli and Nathan Scales and&#10;          Hylke Buisman and Daniel Furrer and Sergii Kashubin and&#10;          Nikola Momchev and Danila Sinopalnikov and Lukasz Stafiniak and&#10;          Tibor Tihon and Dmitry Tsarkov and Xiao Wang and Marc van Zee and&#10;          Olivier Bousquet},&#10;  note={Additional citation for MCD splits},&#10;  booktitle={ICLR},&#10;  year={2020},&#10;  url={https://arxiv.org/abs/1912.09713.pdf},&#10;}" />
</div>
# `scan`

Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

*   **Description**:

SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

Most splits are described at https://github.com/brendenlake/SCAN. For the MCD
splits please see https://arxiv.org/abs/1912.09713.pdf.

Basic usage:

```
data = tfds.load('scan/length')
```

More advanced example:

```
data = tfds.load(
    'scan',
    builder_kwargs=dict(
        config=tfds.text.ScanConfig(
            name='simple_p8', directory='simple_split/size_variations')))
```

*   **Config description**: SCAN tasks with various splits.

SCAN is a set of simple language-driven navigation tasks for studying
compositional learning and zero-shot generalization.

Most splits are described at https://github.com/brendenlake/SCAN. For the MCD
splits please see https://arxiv.org/abs/1912.09713.pdf.

Basic usage:

```
data = tfds.load('scan/length')
```

More advanced example:

```
data = tfds.load(
    'scan',
    builder_kwargs=dict(
        config=tfds.text.ScanConfig(
            name='simple_p8', directory='simple_split/size_variations')))
```

*   **Homepage**:
    [https://github.com/brendenlake/SCAN](https://github.com/brendenlake/SCAN)
*   **Source code**:
    [`tfds.text.scan.Scan`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/scan.py)
*   **Versions**:
    *   **`1.1.1`** (default)
        <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>:
        No release notes.
*   **Features**:

```python
FeaturesDict({
    'actions': Text(shape=(), dtype=tf.string),
    'commands': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('commands', 'actions')`
*   **Citation**:

```
@inproceedings{Lake2018GeneralizationWS,
  title={Generalization without Systematicity: On the Compositional Skills of
         Sequence-to-Sequence Recurrent Networks},
  author={Brenden M. Lake and Marco Baroni},
  booktitle={ICML},
  year={2018},
  url={https://arxiv.org/pdf/1711.00350.pdf},
}
@inproceedings{Keysers2020,
  title={Measuring Compositional Generalization: A Comprehensive Method on
         Realistic Data},
  author={Daniel Keysers and Nathanael Sch"{a}rli and Nathan Scales and
          Hylke Buisman and Daniel Furrer and Sergii Kashubin and
          Nikola Momchev and Danila Sinopalnikov and Lukasz Stafiniak and
          Tibor Tihon and Dmitry Tsarkov and Xiao Wang and Marc van Zee and
          Olivier Bousquet},
  note={Additional citation for MCD splits},
  booktitle={ICLR},
  year={2020},
  url={https://arxiv.org/abs/1912.09713.pdf},
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.

## scan/simple (default config)

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `4.47 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 4,182
'train' | 16,728

## scan/addprim_jump

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `4.53 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 7,706
'train' | 14,670

## scan/addprim_turn_left

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `4.58 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 1,208
'train' | 21,890

## scan/filler_num0

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `3.20 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 1,173
'train' | 15,225

## scan/filler_num1

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `3.51 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 1,173
'train' | 16,290

## scan/filler_num2

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `3.84 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 1,173
'train' | 17,391

## scan/filler_num3

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `4.17 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 1,173
'train' | 18,528

## scan/length

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `4.47 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 3,920
'train' | 16,990

## scan/template_around_right

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `4.17 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 4,476
'train' | 15,225

## scan/template_jump_around_right

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `4.17 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 1,173
'train' | 18,528

## scan/template_opposite_right

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `4.22 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 4,476
'train' | 15,225

## scan/template_right

*   **Download size**: `17.82 MiB`
*   **Dataset size**: `4.26 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 4,476
'train' | 15,225

## scan/mcd1

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## scan/mcd2

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:

## scan/mcd3

*   **Download size**: `Unknown size`
*   **Dataset size**: `Unknown size`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown
*   **Splits**:

Split | Examples
:---- | -------:
