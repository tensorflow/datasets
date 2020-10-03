# Create a dataset

Follow this guide to create a new dataset using TFDS.

Check our [list of datasets](catalog/overview.md) to see if the dataset you want
is already present.

*   [Overview](#overview)
*   [Writing `my_dataset.py`](#writing-my_datasetpy)
    *   [Use the default template](#use-the-default-template)
    *   [DatasetBuilder](#datasetbuilder)
    *   [my_dataset.py](#my_datasetpy)
*   [Specifying `DatasetInfo`](#specifying-datasetinfo)
    *   [`FeatureConnector`s](#featureconnectors)
*   [Downloading and extracting source data](#downloading-and-extracting-source-data)
    *   [Manual download and extraction](#manual-download-and-extraction)
*   [Specifying dataset splits](#specifying-dataset-splits)
*   [Writing an example generator](#writing-an-example-generator)
    *   [File access and `tf.io.gfile`](#file-access-and-tfiogfile)
    *   [Corrupted data](#corrupted-data)
    *   [Inconsistent data](#inconsistent-data)
*   [Dataset configuration](#dataset-configuration)
    *   [Heavy configuration with BuilderConfig](#heavy-configuration-with-builderconfig)
*   [Create your own `FeatureConnector`](#create-your-own-featureconnector)
*   [Large datasets and distributed generation](#large-datasets-and-distributed-generation)
*   [Run your Code](#run-your-code)
*   [Testing `MyDataset`](#testing-mydataset)

## Overview

Datasets are distributed in all kinds of formats and in all kinds of places,
and they're not always stored in a format that's ready to feed into a machine
learning pipeline. Enter TFDS.

TFDS provides a way to transform all those datasets into a standard format,
do the preprocessing necessary to make them ready for a machine learning
pipeline, and provides a standard input pipeline using `tf.data`.

To enable this, each dataset implements a subclass of `DatasetBuilder`, which
specifies:

* Where the data is coming from (i.e. its URL);
* What the dataset looks like (i.e. its features);
* How the data should be split (e.g. `TRAIN` and `TEST`);
* and the individual records in the dataset.

The first time a dataset is used, the dataset is downloaded, prepared, and
written to disk in a standard format. Subsequent access will read from those
pre-processed files directly.


## Writing `my_dataset.py`

### Use the default template

Use TFDS CLI to generate the required template python files.

``` sh
tfds new my_dataset
```

This command will generate dataset files needed for creating a new dataset in
the `my_dataset/` folder located in the current directory.

The `my_dataset/` folder has the following directory structure:

```
my_dataset/
    __init__.py
    my_dataset.py       # Script for Downloading and preparing dataset.
    my_dataset_test.py  # Script for testing dataset generation.
    dummy_data/         # Folder of Dummy dataset files. (required for testing)
    checksum.tsv        # URL checksums of the dataset.
```

Search for `TODO(my_dataset)` here and modify accordingly.

### `DatasetBuilder`

Each dataset is defined as a subclass of `tfds.core.DatasetBuilder` implementing
the following methods:

*   `_info`: builds the `tfds.core.DatasetInfo` object describing the dataset
*   `_download_and_prepare`: to download and serialize the source data to disk
*   `_as_dataset`: to produce a `tf.data.Dataset` from the serialized data

Most datasets are defined as subclass `tfds.core.GeneratorBasedBuilder`, which
is a subclass of `tfds.core.DatasetBuilder` that simplifies defining a dataset.
It works well for datasets that can be generated on a single machine. Its
subclasses implement:

*   `_info`: builds the `tfds.core.DatasetInfo` object describing the dataset
*   `_split_generators`: downloads the source data and defines the dataset
    splits
*   `_generate_examples`: yields `(key, example)` tuples in the dataset from the
    source data

This guide will use `GeneratorBasedBuilder`.

### `my_dataset.py`

`my_dataset.py` first looks like this:

``` python
import tensorflow_datasets as tfds

class MyDataset(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for my_dataset dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    # Specifies the tfds.core.DatasetInfo object
    pass # TODO

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    # Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    pass  # TODO

  def _generate_examples(self):
    # Yields (key, example) tuples from the dataset
    yield 'key', {}
```

## Specifying `DatasetInfo`

`tfds.core.DatasetInfo` describes the dataset.

```python
class MyDataset(tfds.core.GeneratorBasedBuilder):

  def _info(self):
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=("This is the dataset for xxx. It contains yyy. The "
                     "images are kept at their original dimensions."),
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "image_description": tfds.features.Text(),
            "image": tfds.features.Image(),
            # Here, labels can be of 5 distinct values.
            "label": tfds.features.ClassLabel(num_classes=5),
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=("image", "label"),
        # Homepage of the dataset for documentation
        homepage="https://dataset-homepage.org",
        # Bibtex citation for the dataset
        citation=r"""@article{my-awesome-dataset-2020,
                              author = {Smith, John},"}""",
    )
```

### `FeatureConnector`s

Each feature is specified in `DatasetInfo` as a
`tfds.features.FeatureConnector`. `FeatureConnector`s document each feature,
provide shape and type checks, and abstract away serialization to and from disk.
There are many feature types already defined and you can also
[add a new one](#create-your-own-featureconnector).


## Downloading and extracting source data

Most datasets need to download data from the web. All downloads and extractions
must go through the `tfds.download.DownloadManager`. `DownloadManager` currently
supports extracting `.zip`, `.gz`, and `.tar` files.

For example, one can both download and extract URLs with `download_and_extract`:

```python
def _split_generators(self, dl_manager):
  # Equivalent to dl_manager.extract(dl_manager.download(urls))
  dl_paths = dl_manager.download_and_extract({
      'foo': 'https://example.com/foo.zip',
      'bar': 'https://example.com/bar.zip',
  })
  dl_paths['foo'], dl_paths['bar']
```

### Manual download and extraction

For source data that cannot be automatically downloaded (for example, it may
require a login), the user will manually download the source data and place it
in `manual_dir`, which you can access with `dl_manager.manual_dir` (defaults to
`~/tensorflow_datasets/manual/`).

## Specifying dataset splits

If the dataset comes with pre-defined splits (for example, MNIST has train and
test splits), keep those splits in the `DatasetBuilder`. If the dataset does not
have predefined splits, `DatasetBuilder` should only specify a single
`tfds.Split.TRAIN` split. Users can dynamically create their own subsplits
with the
[subsplit API](https://github.com/tensorflow/datasets/tree/master/docs/splits.md)
(e.g. `split='train[80%:]'`).

```python
  def _split_generators(self, dl_manager):
    # Download source data
    extracted_path = dl_manager.download_and_extract(...)

    # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "train"),
                "labels": os.path.join(extracted_path, "train_labels.csv"),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "test"),
                "labels": os.path.join(extracted_path, "test_labels.csv"),
            },
        ),
    ]
```

`SplitGenerator` describes how a split should be generated. `gen_kwargs`
will be passed as keyword arguments to `_generate_examples`, which we'll define
next.

## Writing an example generator

`_generate_examples` generates the examples for each split from the
source data. For the `TRAIN` split with the `gen_kwargs` defined above,
`_generate_examples` will be called as:

```python
builder._generate_examples(
    images_dir_path="{extracted_path}/train",
    labels="{extracted_path}/train_labels.csv",
)
```

This method will typically read source dataset artifacts (e.g. a CSV file) and
yield (key, feature dictionary) tuples that correspond to the features specified
in `DatasetInfo`.

```python
def _generate_examples(self, images_dir_path, labels):
  # Read the input data out of the source files
  for image_file in tf.io.gfile.listdir(images_dir_path):
    ...
  with tf.io.gfile.GFile(labels) as f:
    ...

  # And yield examples as feature dictionaries
  for image_id, description, label in data:
    yield image_id, {
        "image_description": description,
        "image": "%s/%s.jpeg" % (images_dir_path, image_id),
        "label": label,
    }
```

`DatasetInfo.features.encode_example` will encode these dictionaries into a
format suitable for writing to disk (currently we use `tf.train.Example`
protocol buffers). For example, `tfds.features.Image` will copy out the
JPEG content of the passed image files automatically.

The key (here: `image_id`) should uniquely identify the record. It is used to
shuffle the dataset globally. If two records are yielded using the same key,
an exception will be raised during preparation of the dataset.

### File access and `tf.io.gfile`

In order to support Cloud storage systems, use
`tf.io.gfile` or other TensorFlow file APIs (for example, `tf.python_io`)
for all filesystem access. Avoid using Python built-ins for file operations
(e.g. `open`, `os.rename`, `gzip`, etc.).

### Corrupted data

Some datasets are not perfectly clean and contain some corrupt data
(for example, the images are in JPEG files but some are invalid JPEG). These
examples should be skipped, but leave a note in the dataset description how
many examples were dropped and why.

### Inconsistent data

Some datasets provide a set of URLs for individual records or features
(for example, URLs to various images around the web) that may or may not
exist anymore. These datasets are difficult to version properly because the
source data is unstable (URLs come and go).

If the dataset is inherently unstable (that is, if multiple runs over time
may not yield the same data), mark the dataset as unstable by adding a
class constant to the `DatasetBuilder`:
`UNSTABLE = "<why this dataset is unstable">`. For example,
`UNSTABLE = "Downloads URLs from the web."`

## Dataset configuration

Some datasets may have variants that should be exposed, or options for how the
data is preprocessed.

### Heavy configuration with `BuilderConfig`

Heavy configuration affects how the data is written to disk. For example, for
text datasets, different `TextEncoder`s and vocabularies affect the token ids
that are written to disk.

Heavy configuration is done through `tfds.core.BuilderConfig`s:

1. Define your own configuration object as a subclass of
   `tfds.core.BuilderConfig`. For example, `MyDatasetConfig`.
2. Define the `BUILDER_CONFIGS` class member in `MyDataset` that lists
   `MyDatasetConfig`s that the dataset exposes.
3. Use `self.builder_config` in `MyDataset` to configure data generation. This
   may include setting different values in `_info()` or changing download data
   access.

Datasets with `BuilderConfig`s have a name and version per config,
so the fully qualified name of a particular variant would be
`dataset_name/config_name` (for example, `"lm1b/bytes"`). The config defaults
to the first one in `BUILDER_CONFIGS` (for example "`lm1b`" defaults to
`"lm1b/plain_text"`).

See [`Lm1b`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/lm1b.py)
for an example of a dataset that uses `BuilderConfig`s.

## Create your own `FeatureConnector`

Note that most datasets will find the current set of
`tfds.features.FeatureConnector`s sufficient, but sometimes a new one may need
to be defined.

Note: If you need a new `FeatureConnector` not present in the default set and
are planning to submit it to `tensorflow/datasets`, please open a
[new issue](https://github.com/tensorflow/datasets/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=)
on GitHub with your proposal.

`tfds.features.FeatureConnector`s in `DatasetInfo` correspond to the elements
returned in the `tf.data.Dataset` object. For instance, with:

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

The items in `tf.data.Dataset` object would look like:

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

The `tfds.features.FeatureConnector` object abstracts away how the feature is
encoded on disk from how it is presented to the user. Below is a
diagram showing the abstraction layers of the dataset and the transformation
from the raw dataset files to the `tf.data.Dataset` object.

<p align="center">
  <img src="dataset_layers.png" alt="DatasetBuilder abstraction layers" width="700"/>
</p>

To create your own feature connector, subclass `tfds.features.FeatureConnector`
and implement the abstract methods:

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

Have a look at `tfds.features.FeatureConnector` for more details and the
`tfds.features` package for more examples.

## Large datasets and distributed generation

Some datasets are so large as to require multiple machines to download and
generate. We support this use case using Apache Beam. Please read the
[Beam Dataset Guide](beam_datasets.md) to get started.

## Run your Code

From the `my_dataset/` directory, run `download_and_prepare` to ensure that
data generation works:

``` sh
# default data_dir is ~/tensorflow_datasets
python -m tensorflow_datasets.scripts.download_and_prepare \
    --register_checksums \
    --module_import=my_dataset \
    --datasets=my_dataset
```

## Testing MyDataset

`tfds.testing.DatasetBuilderTestCase` is a base `TestCase` to fully exercise a
dataset. It uses "dummy data" as test data that mimic the structure of the
source dataset.

The test data should be put in `dummy_data/` under the `my_dataset/` directory
and should mimic the source dataset artifacts as downloaded and extracted.
It can be created manually or automatically with a script
([example script](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/fake_data_generation/cifar.py)).

Make sure to use different data in your test data splits, as the test will
fail if your dataset splits overlap.

``` python
import tensorflow_datasets as tfds
from . import my_dataset


class MyDatasetTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for my_dataset dataset."""
  DATASET_CLASS = my_dataset.MyDataset
  SPLITS = {
      'train': 3,  # Number of fake train example
      'test': 1,  # Number of fake test example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  DL_EXTRACT_RESULT = {
      "name1": "path/to/file1",  # Relative to fake_examples/my_dataset dir.
      "name2": "file2",
  }


if __name__ == '__main__':
  tfds.testing.test_main()
```

Run the following command to test the dataset.

``` sh
python my_dataset_test.py
```

If you go through all the steps above, it should pass.
