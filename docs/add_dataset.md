# Add a dataset

All datasets subclass
[`DatasetBuilder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_builder.py).
`DatasetBuilder` subclasses must override 2 methods: `_download_and_prepare`,
which is responsible for downloading the source data and putting it into some
format on disk, and `_as_dataset`, which is responsible for producing a
`tf.data.Dataset` from the data on disk.

As a convenience,
[`GeneratorBasedDatasetBuilder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_builder.py)
is a subclass of `DatasetBuilder` that works well for most datasets that can be
generated on a single machine. It expects subclasses to provide generators that
produce examples that will be written across sharded files. See its docstring
for more details.

Here is a diagram showing the abstraction layers of the dataset, from the raw
compressed data files to the `tf.data.Dataset` object.

<p align="center">
  <img src="dataset_layers.png" alt="DatasetBuilder abstraction layers" width="700"/>
</p>

## Downloading data

Most datasets will need to download some data from the web. All downloads must
go through the `DownloadManager`:
`self._download_manager.download([url1, url2])`.

## File access and `tf.gfile`

In order to support Cloud storage systems, all file access must use `tf.gfile`
or other TensorFlow file APIs (for example, `tf.python_io`). Python built-ins
for file operations (e.g. `open`, `os.rename`, `gzip`, etc.) must be avoided.

Datasets often need to extract data using `gzip`, `zlib`, etc.; these
extractions must use `DownloadManager.extract` instead of using the extraction
libraries directly. `DownloadManager` currently supports extracting `.zip`,
`.gz`, and `.tar` files.

## Dataset splits

Datasets usually come with some pre-defined splits (for example, MNIST has train
and test splits); the `DatasetBuilder` must reflect those splits on disk.

For datasets that have no such pre-defined splits, a default split of `(TRAIN:
80%, VALIDATION: 10%, TEST: 10%)` must be used.

## Dataset info

TODO(rsepassi): Document how to fill in and expose `DatasetInfo`

## Large datasets and distributed generation (coming soon)

Some datasets are so large as to require multiple machines to download and
generate. We intend to soon support this use case using Apache Beam. Stay tuned.
