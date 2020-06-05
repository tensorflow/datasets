<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="winogrande" />
  <meta itemprop="description" content="The  WinoGrande, a large-scale dataset of 44k problems, inspired by the original&#10; Winograd Schema Challenge design, but adjusted to improve both the scale and&#10; the hardness of the dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;winogrande&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/winogrande" />
  <meta itemprop="sameAs" content="http://winogrande.allenai.org/" />
  <meta itemprop="citation" content="@article{sakaguchi2019winogrande,&#10;    title={WinoGrande: An Adversarial Winograd Schema Challenge at Scale},&#10;    author={Sakaguchi, Keisuke and Bras, Ronan Le and Bhagavatula, Chandra and Choi, Yejin},&#10;    journal={arXiv preprint arXiv:1907.10641},&#10;    year={2019}&#10;}" />
</div>

# `winogrande`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

The WinoGrande, a large-scale dataset of 44k problems, inspired by the original
Winograd Schema Challenge design, but adjusted to improve both the scale and the
hardness of the dataset.

*   **Homepage**:
    [http://winogrande.allenai.org/](http://winogrande.allenai.org/)
*   **Source code**:
    [`tfds.text.winogrande.Winogrande`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/winogrande.py)
*   **Versions**:
    *   **`1.1.0`** (default): No release notes.
*   **Download size**: `2.67 MiB`
*   **Dataset size**: `9.97 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 1,767
'train_l'    | 10,234
'train_m'    | 2,558
'train_s'    | 640
'train_xl'   | 40,398
'train_xs'   | 160
'validation' | 1,267

*   **Features**:

```python
FeaturesDict({
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'option1': Text(shape=(), dtype=tf.string),
    'option2': Text(shape=(), dtype=tf.string),
    'sentence': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`
*   **Citation**:

```
@article{sakaguchi2019winogrande,
    title={WinoGrande: An Adversarial Winograd Schema Challenge at Scale},
    author={Sakaguchi, Keisuke and Bras, Ronan Le and Bhagavatula, Chandra and Choi, Yejin},
    journal={arXiv preprint arXiv:1907.10641},
    year={2019}
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
