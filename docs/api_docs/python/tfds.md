<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tfds

`tensorflow_datasets` (<a href="./tfds.md"><code>tfds</code></a>) defines a
collection of datasets ready-to-use with TensorFlow.

Defined in [`__init__.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/__init__.py).

<!-- Placeholder for "Used in" -->

Each dataset is defined as a <a href="./tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a>, which encapsulates
the logic to download the dataset and construct an input pipeline, as well as
contains the dataset documentation (version, splits, number of examples, etc.).

The main library entrypoints are:

* <a href="./tfds/builder.md"><code>tfds.builder</code></a>: fetch a <a href="./tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a> by name
* <a href="./tfds/load.md"><code>tfds.load</code></a>: convenience method to construct a builder, download the data, and
  create an input pipeline, returning a `tf.data.Dataset`.

#### Documentation:

*   These API docs
*   [Available datasets](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md)
*   [Colab tutorial](https://colab.research.google.com/github/tensorflow/datasets/blob/master/docs/overview.ipynb)
*   [Add a dataset](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md)

## Modules

[`core`](./tfds/core.md) module: API to define datasets.

[`download`](./tfds/download.md) module: <a href="./tfds/download/DownloadManager.md"><code>tfds.download.DownloadManager</code></a> API.

[`features`](./tfds/features.md) module: <a href="./tfds/features/FeatureConnector.md"><code>tfds.features.FeatureConnector</code></a> API defining feature types.

[`file_adapter`](./tfds/file_adapter.md) module: <a href="./tfds/file_adapter/FileFormatAdapter.md"><code>tfds.file_adapter.FileFormatAdapter</code></a>s for GeneratorBasedBuilder.

[`testing`](./tfds/testing.md) module: Testing utilities.

[`units`](./tfds/units.md) module: Defines convenience constants/functions for
converting various units.

## Classes

[`class GenerateMode`](./tfds/download/GenerateMode.md): `Enum` for how to treat pre-existing downloads and data.

[`class Split`](./tfds/Split.md): `Enum` for dataset splits.

[`class percent`](./tfds/percent.md): Syntactic sugar for defining slice subsplits: `tfds.percent[75:-5]`.

## Functions

[`as_numpy(...)`](./tfds/as_numpy.md): Converts a `tf.data.Dataset` to an iterable of NumPy arrays.

[`builder(...)`](./tfds/builder.md): Fetches a <a href="./tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a> by string name.

[`disable_progress_bar(...)`](./tfds/disable_progress_bar.md): Disabled Tqdm
progress bar.

[`is_dataset_on_gcs(...)`](./tfds/is_dataset_on_gcs.md): If the dataset is
available on the GCS bucket gs://tfds-data/datasets.

[`list_builders(...)`](./tfds/list_builders.md): Returns the string names of all <a href="./tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a>s.

[`load(...)`](./tfds/load.md): Loads the named dataset into a `tf.data.Dataset`.

