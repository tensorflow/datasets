# Adding a dataset

This page describes how to add support for a new dataset. If you want to use a
dataset which isn't listed
[here](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md),
then this document is for you.

*   [Overview](#overview)
*   [Writing my_dataset.py](#writing-my-datasetpy)
*   [Specifying DatasetInfo](#specifying-datasetinfo)
*   [Downloading / extracting the dataset](#downloading-extracting-the-dataset)
    *   [Manual download / extraction](#manual-download-extraction)
*   [Specifying how the data should be split](#specifying-how-the-data-should-be-split)
*   [Reading downloaded data and generating serialized dataset](#reading-downloaded-data-and-generating-serialized-dataset)
    *   [File access and tf.gfile](#file-access-and-tfgfile)
*   [Dataset configuration](#dataset-configuration)
*   [Create your own FeatureConnector](#create-your-own-featureconnector)
*   [Adding the dataset to `tensorflow/datasets`](#adding-the-dataset-to-tensorflowdatasets)
*   [Large datasets and distributed generation](#large-datasets-and-distributed-generation)
*   [Testing MyDataset](#testing-mydataset)

## Overview

Datasets come from various sources and in various formats. To use a dataset, one
must first download it and store it using a format enabling fast loading.

Adding support for a dataset means specifying:

-   Where the data is coming from (i.e. its URL);
-   What the dataset looks like (i.e. its features);
-   How the data should be split (e.g. `TRAIN` and `TEST`);
-   How the data should be stored on disk and fed to the model.

The first time a dataset is used, the dataset is downloaded and prepared and
pre-processed files are generated. The following times it is being used, the
dataset is loaded from the pre-prepared data directly.

**Note**: Currently we do not support datasets that take longer than 1 day to
generate on a single machine. See the
[section below](#large-datasets-and-distributed-generation).

## Writing `my_dataset.py`

To add support for a dataset, you must write its "Builder" class, subclass of
[`tfds.core.DatasetBuilder`](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds/core/DatasetBuilder.md)
and implement the following methods:

-   `_info`, to build the
    [`DatasetInfo`](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds/core/DatasetInfo.md)
    describing the dataset.
-   `_download_and_prepare`, to download and serialize the source data to disk;
-   `_as_dataset`, to produce a `tf.data.Dataset` from the serialized data.

As a convenience,
[`tfds.core.GeneratorBasedBuilder`](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds/core/GeneratorBasedBuilder.md)
is a subclass of `tfds.core.DatasetBuilder` that simplifies defining a dataset
and that works well for most datasets that can be generated on a single machine.
Instead of `_download_and_prepare` and `_as_dataset`, its subclasses must
implement:

-   `_generate_examples`: to generate the `tf.train.Example` records that will
    be written to disk, per dataset split.
-   `_split_generators`: to define the dataset splits and arguments for
    `_generate_examples` per split.

Let's use `GeneratorBasedBuilder`, the easier option. `my_dataset.py` first
looks like this:

```python
import tensorflow_datasets.public_api as tfds

class MyDataset(tfds.core.GeneratorBasedBuilder):
  """Short description of my dataset."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    pass # TODO

  def _split_generators(self, dl_manager):
    pass  # TODO

  def _generate_examples(self):
    pass  # TODO
```

Before implementing the methods, we recommend to add a test which can help you
iterate faster. If you'd like to follow a test-driven development workflow,
jump to the [testing instructions](#testing-mydataset) below, add the test,
and then return here.

## Specifying `DatasetInfo`

The
[`DatasetInfo`](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds/core/DatasetInfo.md)
stores the information we know about a dataset. For now, let's add what features
are part of the dataset and their types. For example:

```python
class MyDataset(tfds.core.GeneratorBasedBuilder):

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("This is the dataset for xxx. It contains yyy. The "
                     "images are kept at their original dimensions."),
        # Features specify the shape and dtype of the loaded data, as returned
        # by tf.data.Dataset. It also abstract the encoding/decoding of the
        # data into disk.
        features=tfds.features.FeaturesDict({
            "image_description": tfds.features.Text(),
            "image": tfds.features.Image(),
            # Here, labels can be of 5 distinct values.
            "label": tfds.features.ClassLabel(num_classes=5),
        }),
        # When using .as_dataset(split=..., as_supervised=True), a tuple
        # (input_feature, output_feature) will be returned instead of the
        # full dict.
        # This is useful as this correspond to Keras input format.
        supervised_keys=("image", "label"),
        # Homepage of the dataset. Not used anywhere except for documentation
        urls=["https://dataset-homepage.org"],
        # Citation to use for using this dataset in the Bibtex format.
        citation=r"""@article{my-awesome-dataset-2020,
                              author = {Smith, John},"}""",
    )
```

The features are what defines the shape of the loaded data. Have a look at the
[features package](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds/features.md)
for a complete list of available features and their description.

If you've implemented the test harness, `test_info` should now pass.

## Downloading / extracting the dataset

Most dataset builders need to download some data from the web. All downloads and
extractions must go through the
[`tfds.download.DownloadManager`](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds/download/DownloadManager.md).
`DownloadManager` currently
supports extracting `.zip`, `.gz`, and `.tar` files.

For example, one can do both download and extraction with
`download_and_extract`:

```python
def _split_generators(self, dl_manager):
  # Equivalent to dl_manager.extract(dl_manager.download(urls))
  dl_paths = dl_manager.download_and_extract({
      'foo': 'https://example.com/foo.zip',
      'bar': 'https://example.com/bar.zip',
  })
  dl_paths['foo'], dl_paths['bar']
```

### Manual download / extraction

If the dataset artifacts cannot be downloaded or extracted automatically (for
example, if there are no APIs and it needs a username/password), you can use
`path = dl_manager.manual_dir`. The user will need to manually download and
extract the source data into the `manual_dir` of this dataset (by default:
`~/tensorflow_datasets/manual/my_dataset`).

TODO(tfds): Add support for specifying checksums for manual_dir datasets.

## Specifying how the data should be split

Datasets usually come with some pre-defined splits (for example, MNIST has train
and test splits); the `DatasetBuilder` must reflect those splits on disk. If
this is your own data, we suggest using a split of `(TRAIN:80%, VALIDATION: 10%,
TEST: 10%)`. Users can always get subsplits through the `tfds` API.

```python
  def _split_generators(self, dl_manager):
    extracted_path = dl_manager.download_and_extract(...)
    return [
        tfds.core.SplitGenerator(
            name="train",
            num_shards=10,
            gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "train"),
                "labels": os.path.join(extracted_path, "train_labels.csv"),
            },
        ),
        tfds.core.SplitGenerator(
            name="test",
            ...
        ),
    ]
```

Use the `SplitGenerator` to describe how each split should be generated. The
`gen_kwargs` argument is what will be passed to the method writing the TF
`tf.train.Example` to be serialized and written to disk.

Note: When specifying the number of shards, make sure that no shard is bigger
than 4 GiB as shards will be loaded entirely in memory for shuffling.

## Reading downloaded data and generating serialized dataset

When using `GeneratorBasedBuilder` base class, the `_generate_examples` method
generates the examples to be stored for each split, out of the original source
data. With the previous example, it will be called as:

```python
builder._generate_examples(
    images_dir_path="{extracted_path}/train",
    labels="{extracted_path}/train_labels.csv",
)
```

This method will typically read source dataset artifacts (e.g. a CSV) and yield
examples like:

```python
def _generate_examples(self, images_dir_path, labels=None):
  ... # read data from CSV and build data
  for image_id, description, label in data:
    yield {
        "image_description": description,
        "image": "%s/%s.jpeg" % (images_dir_path, image_id),
        "label": label,
    }
```

These dictionaries will be encoded by `self.info.features.encode_example`, which
uses the feature definitions from `DatasetInfo` to encode the features passed
here into a `tf.train.Example`. In this case, the `ImageFeature` will encode the
jpeg content into the TFRecord file automatically.

If you've implemented the test harness, your builder test should now pass.

### File access and `tf.gfile`

In order to support Cloud storage systems, all file access must use `tf.gfile`
or other TensorFlow file APIs (for example, `tf.python_io`). Python built-ins
for file operations (e.g. `open`, `os.rename`, `gzip`, etc.) must be avoided.

## Dataset configuration

Some datasets may have variants that are best implemented through configuration
rather than being entirely separate `DatasetBuilder`s. For example, datasets
with text features may want to have different text encodings (e.g.
character-level vs subword-level vs word-level vocabularies). To enable
different configurations of your dataset, you must:

1. Define your own configuration object as a subclass of
   `tfds.core.BuilderConfig`. For example, `MyDatasetConfig`.
2. Define the `BUILDER_CONFIGS` class member in `MyDataset` that lists
   `MyDatasetConfig`s that the dataset exposes.
3. Use `self.builder_config` in `MyDataset` to configure data generation. This
   may include setting different values in `_info()` or changing download data
   access.

Each `MyDatasetConfig` would have a name and so the dataset would be addressed
as `my_dataset/my_config_name` in `tfds.builder` or `tfds.load`. You can also
instantiate the `MyDataset` class directly and pass the `config` kwarg which
can either be a config name or a `MyDatasetConfig` object.

See [`IMDBReviews`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/imdb.py)
for an example of a dataset that uses `BuilderConfig`s.

Note that `BuilderConfig`s are only for situations that would affect how the
data is written to disk, not for situations where alterations could be made
on-the-fly in the `tf.data` input pipeline. To add configuration that would
only affect data reading, add keyword arguments to the `MyDataset` constructor,
store them in member variables, and then use them later. For example,
you could override `_as_dataset()`, call `super()` to get the base
`tf.data.Dataset`, and then do additional transformations based on the member
variables.

## Create your own `FeatureConnector`

Note that most datasets will find the [current set of
`tfds.features.FeatureConnector`s](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds/features.md)
sufficient, but sometimes a new one may need to be defined.

[`tfds.features.FeatureConnector`s](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds/features/FeatureConnector.md)
in `DatasetInfo` correspond to the elements returned in the
`tf.data.Dataset` object. For instance, with:

```
tfds.DatasetInfo(features=tfds.features.FeatureDict({
    'input': tfds.features.Image(),
    'output': tfds.features.Text(encoder=tfds.text.ByteEncoder()),
    'metadata': {
        'description': tfds.features.Text(),
        'img_id': tf.int32,
    },
}))
```

The `tf.data.Dataset` object associated with the defined info will be:

```
{
    'input': tf.Tensor(shape=(None, None, 3), dtype=tf.uint8),
    'output': tf.Tensor(shape=(None,), dtype=tf.int32),  # Sequence of token ids
    'metadata': {
        'description': tf.Tensor(shape=(), dtype=tf.string),
        'img_id': tf.Tensor(shape=(), dtype=tf.int32),
    },
}
```

The `tfds.features.FeatureConnector` object abstracts the way the feature is
internally encoded on disk from how it is presented to the user. Below is a
diagram showing the abstraction layers of the dataset and the transformation
from the raw dataset files to the `tf.data.Dataset` object.

<p align="center">
  <img src="dataset_layers.png" alt="DatasetBuilder abstraction layers" width="700"/>
</p>

To create your own feature connector, subclass `tfds.features.FeatureConnector`
and implement the abstract methods.

*   `get_tensor_info()`: Indicates the shape/dtype of the tensor(s) returned by
    `tf.data.Dataset`
*   `encode_example(input_data)`: Defines how to encode the data given in the
    generator `_generate_examples()` into a `tf.train.Example` compatible data
*   `decode_example`: Defines how to decode the data from the tensor read from
    `tf.train.Example` into user tensor returned by `tf.data.Dataset`.
*   (optionally) `get_serialized_info()`: If the info returned by
    `get_tensor_info()` is different from how the data are actually written on
    disk, then you need to overwrite `get_serialized_info()` to match the specs
    of the `tf.train.Example`

1.  If your connector only contains one value, then the `get_tensor_info`,
    `encode_example`, and `decode_example` methods can directly return single
    value (without wrapping it in a dict).

2.  If your connector is a container of multiple sub-features, the easiest way
    is to inherit from `tfds.features.FeaturesDict` and use the `super()`
    methods to automatically encode/decode the sub-connectors.

Have a look at the doc of `tfds.features.FeatureConnector` for more details and
the
[features package](https://github.com/tensorflow/datasets/tree/master/docs/api_docs/python/tfds/features.md)
for more examples.

## Adding the dataset to `tensorflow/datasets`

If you'd like to share your work with the community, you can check in your
dataset implementation to `tensorflow/datasets`. Thanks for thinking of
contributing!

Before you send your pull request, follow these last few steps:

### 1. Add an import for registration

All subclasses of `tfds.core.DatasetBuilder` are automatically registered
when their module is imported such that they can be accessed through
`tfds.builder` and `tfds.load`.

If you're contributing the dataset to `tensorflow/datasets`, add the module
import to `tensorflow_datasets/__init__.py`.

### 2. Package `DatasetInfo` and metadata files

All datasets that ship with `tensorflow-datasets` have their
`dataset_info.json` and metadata files packaged in so that users can access
statistics and other information without needing to generate the dataset.

Run [`tensorflow_datasets/scripts/download_and_prepare`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/scripts/download_and_prepare.py)
to generate the dataset and then copy in the `dataset_info.json` and other
metadata files to [`tensorflow_datasets/dataset_info`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/dataset_info/).

### 3. Double-check the citation

If the paper is on [arXiv](https://arxiv.org/), find it there and click the
`bibtex` link on the right-hand side. Use this for `info.citation`.

If the paper is not on arXiv, find the paper on
[Google Scholar](https://scholar.google.com) and click the double-quotation mark
underneath the title and on the popup, click `BibTeX`. Use this for
`info.citation`.

### 4. Add a test

Adding a unit test is optional, however, it's recommended, especially for
important large datasets and datasets that require a new
`FeatureConnector`. See the [testing section](#testing-mydataset) below.

## Large datasets and distributed generation

Some datasets are so large as to require multiple machines to download and
generate. We intend to soon support this use case using Apache Beam. Follow
[our tracking issue](https://github.com/tensorflow/datasets/issues/10)
to be updated.


## Testing MyDataset

`dataset_builder_testing.TestCase` is a base `TestCase` to fully exercise a
dataset. It needs a "fake example" of the source dataset, to be used as testing
data.

The "fake example", to be stored in
[`testing/test_data/fake_examples/`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/test_data/fake_examples/)
under the `my_dataset` directory and should mimic the source dataset artifacts
as downloaded and extracted. It can be created manually or automatically with a
script ([example
script](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/cifar.py)).

Make sure to use different data in your fake example splits, as the test will
fail if your dataset splits overlap.

**The fake example should not contain any copyrighted material**. If in doubt,
do not create the example using material from the original dataset.

```python
import tensorflow as tf
from tensorflow_datasets import my_dataset
from tensorflow_datasets.testing import dataset_builder_testing


class MyDatasetTest(dataset_builder_testing.TestCase):
  DATASET_CLASS = my_dataset.MyDataset
  SPLITS = {  # Expected number of examples on each split from fake example.
      "train": 12,
      "test": 12,
  }
  # If dataset `download_and_extract` more than one resource:
  DL_EXTRACT_RESULT = {
      "name1": "path/to/file1",  # Relative to fake_examples/my_dataset dir.
      "name2": "file2",
  }

if __name__ == "__main__":
  dataset_builder_testing.main()
```

You can run the test as you proceed to implement `MyDataset`.
If you go through all the steps above, it should pass.
