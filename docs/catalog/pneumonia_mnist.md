<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="pneumonia_mnist" />
  <meta itemprop="description" content="# MedMNIST Pneumonia Dataset&#10;&#10;The PneumoniaMNIST is based on a prior dataset of 5,856 pediatric chest X-Ray&#10;images. The task is binary-class classification of pneumonia against normal. The&#10;source training set is split with a ratio of 9:1 into training and validation&#10;set, and use its source validation set as the test set. The source images are&#10;gray-scale, and their sizes are (384–2,916) × (127–2,713). The images are&#10;center-cropped with a window size of length of the short edge and resized into 1&#10;× 28 × 28.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;pneumonia_mnist&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/pneumonia_mnist" />
  <meta itemprop="sameAs" content="https://medmnist.com//" />
  <meta itemprop="citation" content="@article{yang2023medmnist,&#10;  title={Medmnist v2-a large-scale lightweight benchmark for 2d and 3d biomedical image classification},&#10;  author={Yang, Jiancheng and Shi, Rui and Wei, Donglai and Liu, Zequan and Zhao, Lin and Ke, Bilian and Pfister, Hanspeter and Ni, Bingbing},&#10;  journal={Scientific Data},&#10;  volume={10},&#10;  number={1},&#10;  pages={41},&#10;  year={2023},&#10;  publisher={Nature Publishing Group UK London}&#10;}" />
</div>

# `pneumonia_mnist`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

# MedMNIST Pneumonia Dataset

The PneumoniaMNIST is based on a prior dataset of 5,856 pediatric chest X-Ray
images. The task is binary-class classification of pneumonia against normal. The
source training set is split with a ratio of 9:1 into training and validation
set, and use its source validation set as the test set. The source images are
gray-scale, and their sizes are (384–2,916) × (127–2,713). The images are
center-cropped with a window size of length of the short edge and resized into 1
× 28 × 28.

*   **Homepage**: [https://medmnist.com//](https://medmnist.com//)

*   **Source code**:
    [`tfds.datasets.pneumonia_mnist.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/pneumonia_mnist/pneumonia_mnist_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(28, 28, 1), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature | Class        | Shape       | Dtype | Description
:------ | :----------- | :---------- | :---- | :----------
        | FeaturesDict |             |       |
image   | Image        | (28, 28, 1) | uint8 |
label   | ClassLabel   |             | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{yang2023medmnist,
  title={Medmnist v2-a large-scale lightweight benchmark for 2d and 3d biomedical image classification},
  author={Yang, Jiancheng and Shi, Rui and Wei, Donglai and Liu, Zequan and Zhao, Lin and Ke, Bilian and Pfister, Hanspeter and Ni, Bingbing},
  journal={Scientific Data},
  volume={10},
  number={1},
  pages={41},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
```

