# Adding a dataset

All datasets subclass
[`DatasetBuilder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_builder.py).

Most datasets should be a subclass of
[`GeneratorBasedDatasetBuilder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_builder.py).
See its docstring for which methods to implement.

## Downloading data

Most datasets will need to download some data from the web. All downloads should
go through the `DownloadManager`:
`self._download_manager.download([url1, url2])`.

## File access and `tf.gfile`

To ensure support across Cloud storage systems, all file access should use
`tf.gfile` or other TensorFlow file APIs (for example, `tf.python_io`). Python
built-ins (e.g. `open`, `os.rename`, etc.) should be avoided.

Datasets often need to extract data using `gzip`, `zlib`, etc.; these
extractions should use `DownloadManager.extract` instead of using the extraction
libraries directly.

## Dataset splits

Datasets usually come with some pre-defined splits (for example, MNIST has train
and test splits) and the `DatasetBuilder` should reflect that.

For datasets that have no such splits, a default split of
`(TRAIN: 80%, VALIDATION: 10%, TEST: 10%)` should be used.

## Dataset info

TODO(rsepassi): Document how to fill in and expose `DatasetInfo`

## Large datasets and distributed generation

Some datasets are so large as to require multiple machines to download and
generate. We intend to soon support this use case using Apache Beam. Stay tuned.
