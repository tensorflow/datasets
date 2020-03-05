# tfds.core.DatasetBuilder


#### Abstract base class for all datasets.

```py
tfds.core.DatasetBuilder(
    data_dir=None, config=None, version=None
)
```

`DatasetBuilder` has 3 key methods:

* `tfds.DatasetBuilder.info`: documents the dataset, including feature names, types, and shapes, version, splits, citation, etc.
* `tfds.DatasetBuilder.download_and_prepare`: downloads the source data and writes it to disk.
* `tfds.DatasetBuilder.as_dataset`: builds an input pipeline using [`tf.data.Datasets`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset).

**Configuration**: Some `DatasetBuilder`s expose multiple variants of the dataset by defining a [`tfds.core.BuilderConfig`](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/BuilderConfig) subclass and accepting a config object (or name) on construction. Configurable datasets expose a pre-defined set of configurations in `tfds.DatasetBuilder.builder_configs`.

Typical `DatasetBuilder` usage:

```py
mnist_builder = tfds.builder("mnist")
mnist_info = mnist_builder.info
mnist_builder.download_and_prepare()
datasets = mnist_builder.as_dataset()

train_dataset, test_dataset = datasets["train"], datasets["test"]
assert isinstance(train_dataset, tf.data.Dataset)

# And then the rest of your input pipeline
train_dataset = train_dataset.repeat().shuffle(1024).batch(128)
train_dataset = train_dataset.prefetch(2)
features = tf.compat.v1.data.make_one_shot_iterator(train_dataset).get_next()
image, label = features['image'], features['label']
```

**Args:**
* **`data_dir`**: `str`, directory to read/write data. Defaults to "~/tensorflow_datasets".
* **`config`**: [`tfds.core.BuilderConfig`](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/BuilderConfig) or `str` name, optional configuration for the dataset that affects the data generated on disk. Different `builder_configs` will have their own subdirectories and versions.
* **`version`**: `str`. Optional version at which to load the dataset. An error is raised if specified version cannot be satisfied. Eg: '1.2.3', '1.2.*'. The special value "experimental_latest" will use the highest version, even if not default. This is not recommended unless you know what you are doing, as the version could be broken.

**Attributes:**
* **builder_config**: [`tfds.core.BuilderConfig`](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/BuilderConfig) for this builder.
* **`canonical_version`**
* **`data_dir`**
* **`info`**: [`tfds.core.DatasetInfo`](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/DatasetInfo) for this builder.
* **`supported_version`**
* **`version`**
* **`versions`**: Versions (canonical + availables), in preference order.
### Methods
#### as_dataset
[View source](https://github.com/tensorflow/datasets/blob/v2.1.0/tensorflow_datasets/core/dataset_builder.py#L366-L483)

```py
as_dataset(
    split=None, batch_size=None, shuffle_files=False, decoders=None,
    read_config=None, as_supervised=False, in_memory=None
)
```

Constructs a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset).

Callers must pass arguments as keyword arguments.

The output types vary depending on the parameters. Examples:

```py
builder = tfds.builder('imdb_reviews')
builder.download_and_prepare()

# Default parameters: Returns the dict of tf.data.Dataset
ds_all_dict = builder.as_dataset()
assert isinstance(ds_all_dict, dict)
print(ds_all_dict.keys())  # ==> ['test', 'train', 'unsupervised']

assert isinstance(ds_all_dict['test'], tf.data.Dataset)
# Each dataset (test, train, unsup.) consists of dictionaries
# {'label': <tf.Tensor: .. dtype=int64, numpy=1>,
#  'text': <tf.Tensor: .. dtype=string, numpy=b"I've watched the movie ..">}
# {'label': <tf.Tensor: .. dtype=int64, numpy=1>,
#  'text': <tf.Tensor: .. dtype=string, numpy=b'If you love Japanese ..'>}

# With as_supervised: tf.data.Dataset only contains (feature, label) tuples
ds_all_supervised = builder.as_dataset(as_supervised=True)
assert isinstance(ds_all_supervised, dict)
print(ds_all_supervised.keys())  # ==> ['test', 'train', 'unsupervised']

assert isinstance(ds_all_supervised['test'], tf.data.Dataset)
# Each dataset (test, train, unsup.) consists of tuples (text, label)
# (<tf.Tensor: ... dtype=string, numpy=b"I've watched the movie ..">,
#  <tf.Tensor: ... dtype=int64, numpy=1>)
# (<tf.Tensor: ... dtype=string, numpy=b"If you love Japanese ..">,
#  <tf.Tensor: ... dtype=int64, numpy=1>)

# Same as above plus requesting a particular split
ds_test_supervised = builder.as_dataset(as_supervised=True, split='test')
assert isinstance(ds_test_supervised, tf.data.Dataset)
# The dataset consists of tuples (text, label)
# (<tf.Tensor: ... dtype=string, numpy=b"I've watched the movie ..">,
#  <tf.Tensor: ... dtype=int64, numpy=1>)
# (<tf.Tensor: ... dtype=string, numpy=b"If you love Japanese ..">,
#  <tf.Tensor: ... dtype=int64, numpy=1>)
```

**Args:**
* **`split`**: [`tfds.core.SplitBase`](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/SplitBase), which subset(s) of the data to read. If None (default), returns all splits in a dict `<key: tfds.Split, value: tf.data.Dataset>`.
* **`batch_size`**: `int`, batch size. Note that variable-length features will be 0-padded if `batch_size` is set. Users that want more custom behavior should use `batch_size=None` and use the [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) API to construct a custom pipeline. If `batch_size == -1`, will return feature dictionaries of the whole dataset with [`tf.Tensors`](https://www.tensorflow.org/api_docs/python/tf/Tensor) instead of a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset).
* **`shuffle_files`**: `bool`, whether to shuffle the input files. Defaults to `False`.
* **`decoders`**: Nested dict of `Decoder` objects which allow to customize the decoding. The structure should match the feature structure, but only customized feature keys need to be present. See [`the guide`](https://github.com/tensorflow/datasets/tree/master/docs/decode.md) for more info.
* **`read_config`**`: `[tfds.ReadConfig](https://www.tensorflow.org/datasets/api_docs/python/tfds/ReadConfig)`, Additional options to configure the input pipeline (e.g. seed, num parallel reads,...).
* **`as_supervised`**: `bool`, if `True`, the returned [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) will have a 2-tuple structure `(input, label)` according to `builder.info.supervised_keys`. If `False`, the default, the returned [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) will have a dictionary with all the features.
* **`in_memory`**: `bool`, if `True`, loads the dataset in memory which increases iteration speeds. Note that if `True` and the dataset has unknown dimensions, the features will be padded to the maximum size across the dataset.
**Returns**:
[`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset), or if `split=None`, `dict<key: tfds.Split, value: tfds.data.Dataset>`.

If `batch_size` is -1, will return feature dictionaries containing the entire dataset in [`tf.Tensors`](https://www.tensorflow.org/api_docs/python/tf/Tensor) instead of a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset).

### download_and_prepare
[View source](https://github.com/tensorflow/datasets/blob/v2.1.0/tensorflow_datasets/core/dataset_builder.py#L268-L364)

```py
download_and_prepare(
    download_dir=None, download_config=None
)
```

Downloads and prepares dataset for reading.

**Args**:
* **`download_dir`**: `str`, directory where downloaded files are stored. Defaults to "~/tensorflow-datasets/downloads".
* **`download_config`**: [`tfds.download.DownloadConfig`](https://www.tensorflow.org/datasets/api_docs/python/tfds/download/DownloadConfig), further configuration for downloading and preparing dataset.
**Raises**:
* **`IOError`**: if there is not enough disk space available.
#### Class Variables`
* `BUILDER_CONFIGS`
* `SUPPORTED_VERSIONS`
* `builder_configs`
* `name = 'dataset_builder'`
