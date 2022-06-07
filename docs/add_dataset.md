# Writing custom datasets

Follow this guide to create a new dataset (either in TFDS or in your own
repository).

Check our [list of datasets](catalog/overview.md) to see if the dataset you want
is already present.

## TL;DR

The easiest way to write a new dataset is to use the
[TFDS CLI](https://www.tensorflow.org/datasets/cli):

```sh
cd path/to/my/project/datasets/
tfds new my_dataset  # Create `my_dataset/my_dataset.py` template files
# [...] Manually modify `my_dataset/my_dataset.py` to implement your dataset.
cd my_dataset/
tfds build  # Download and prepare the dataset to `~/tensorflow_datasets/`
```

To use the new dataset with `tfds.load('my_dataset')`:

*   `tfds.load` will automatically detect and load the dataset generated in
    `~/tensorflow_datasets/my_dataset/` (e.g. by `tfds build`).
*   Alternatively, you can explicitly `import my.project.datasets.my_dataset` to
    register your dataset:

```python
import my.project.datasets.my_dataset  # Register `my_dataset`

ds = tfds.load('my_dataset')  # `my_dataset` registered
```

## Overview

Datasets are distributed in all kinds of formats and in all kinds of places, and
they're not always stored in a format that's ready to feed into a machine
learning pipeline. Enter TFDS.

TFDS process those datasets into a standard format (external data -> serialized
files), which can then be loaded as machine learning pipeline (serialized files
-> `tf.data.Dataset`). The serialization is done only once. Subsequent access
will read from those pre-processed files directly.

Most of the preprocessing is done automatically. Each dataset implements a
subclass of `tfds.core.DatasetBuilder`, which specifies:

*   Where the data is coming from (i.e. its URLs);
*   What the dataset looks like (i.e. its features);
*   How the data should be split (e.g. `TRAIN` and `TEST`);
*   and the individual examples in the dataset.

## Write your dataset

### Default template: `tfds new`

Use [TFDS CLI](https://www.tensorflow.org/datasets/cli) to generate the required
template python files.

```sh
cd path/to/project/datasets/  # Or use `--dir=path/to/project/datasets/` below
tfds new my_dataset
```

This command will generate a new `my_dataset/` folder with the following
structure:

```sh
my_dataset/
    __init__.py
    my_dataset.py # Dataset definition
    my_dataset_test.py # (optional) Test
    dummy_data/ # (optional) Fake data (used for testing)
    checksum.tsv # (optional) URL checksums (see `checksums` section).
```

Search for `TODO(my_dataset)` here and modify accordingly.

### Dataset example

All datasets are implemented as `tfds.core.GeneratorBasedBuilder`, a subclasses
of `tfds.core.DatasetBuilder` which takes care of most boilerplate. It supports:

*   Small/medium datasets which can be generated on a single machine (this
    tutorial).
*   Very large datasets which require distributed generation (using
    [Apache Beam](https://beam.apache.org/), see our
    [huge dataset guide](https://www.tensorflow.org/datasets/beam_datasets#implementing_a_beam_dataset))

Here is a minimal example of dataset class:

```python
class MyDataset(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for my_dataset dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Dataset metadata (homepage, citation,...)."""
    return tfds.core.DatasetInfo(
        builder=self,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(256, 256, 3)),
            'label': tfds.features.ClassLabel(
                names=['no', 'yes'],
                doc='Whether this is a picture of a cat'),
        }),
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Download the data and define splits."""
    extracted_path = dl_manager.download_and_extract('http://data.org/data.zip')
    # dl_manager returns pathlib-like objects with `path.read_text()`,
    # `path.iterdir()`,...
    return {
        'train': self._generate_examples(path=extracted_path / 'train_images'),
        'test': self._generate_examples(path=extracted_path / 'test_images'),
    }

  def _generate_examples(self, path) -> Iterator[Tuple[Key, Example]]:
    """Generator of examples for each split."""
    for img_path in path.glob('*.jpeg'):
      # Yields (key, example)
      yield img_path.name, {
          'image': img_path,
          'label': 'yes' if img_path.name.startswith('yes_') else 'no',
      }
```

Let's see in detail the 3 abstract methods to overwrite.

### `_info`: dataset metadata

`_info` returns the `tfds.core.DatasetInfo` containing the
[dataset metadata](https://www.tensorflow.org/datasets/overview#access_the_dataset_metadata).

```python
def _info(self):
  return tfds.core.DatasetInfo(
      builder=self,
      # Description and homepage used for documentation
      description="""
      Markdown description of the dataset. The text will be automatically
      stripped and dedent.
      """,
      homepage='https://dataset-homepage.org',
      features=tfds.features.FeaturesDict({
          'image_description': tfds.features.Text(),
          'image': tfds.features.Image(),
          # Here, 'label' can be 0-4.
          'label': tfds.features.ClassLabel(num_classes=5),
      }),
      # If there's a common `(input, target)` tuple from the features,
      # specify them here. They'll be used if as_supervised=True in
      # builder.as_dataset.
      supervised_keys=('image', 'label'),
      # Specify whether to disable shuffling on the examples. Set to False by default.
      disable_shuffling=False,
      # Bibtex citation for the dataset
      citation=r"""
      @article{my-awesome-dataset-2020,
               author = {Smith, John},}
      """,
  )
```

Most fields should be self-explanatory. Some precisions:

*   `features`: This specify the dataset structure, shape,... Support complex
    data types (audio, video, nested sequences,...). See the
    [available features](https://www.tensorflow.org/datasets/api_docs/python/tfds/features#classes)
    or the
    [feature connector guide](https://www.tensorflow.org/datasets/features) for
    more info.
*   `disable_shuffling`: See section
    [Maintain dataset order](#maintain-dataset-order).
*   `citation`: To find the `BibText` citation:
    *   Search the dataset website for citation instruction (use that in BibTex
        format).
    *   For [arXiv](https://arxiv.org/) papers: find the paper and click the
        `BibText` link on the right-hand side.
    *   Find the paper on [Google Scholar](https://scholar.google.com) and click
        the double-quotation mark underneath the title and on the popup, click
        `BibTeX`.
    *   If there is no associated paper (for example, there's just a website),
        you can use the [BibTeX Online Editor](https://truben.no/latex/bibtex/)
        to create a custom BibTeX entry (the drop-down menu has an `Online`
        entry type).

#### Maintain dataset order

By default, the records of the datasets are shuffled when stored in order to
make the distribution of classes more uniform across the dataset, since often
records belonging to the same class are contiguous. In order to specify that the
dataset should be sorted by the key generated provided by `_generate_examples`
the field `disable_shuffling` should be set to `True`. By default it is set to
`False`.

```python
def _info(self):
  return tfds.core.DatasetInfo(
    # [...]
    disable_shuffling=True,
    # [...]
  )
```

Keep in mind that disabling shuffling has a performance impact as shards cannot
be read in parallel anymore.

### `_split_generators`: downloads and splits data

#### Downloading and extracting source data

Most datasets need to download data from the web. This is done using the
`tfds.download.DownloadManager` input argument of `_split_generators`.
`dl_manager` has the following methods:

*   `download`: supports `http(s)://`, `ftp(s)://`
*   `extract`: currently supports `.zip`, `.gz`, and `.tar` files.
*   `download_and_extract`: Same as
    `dl_manager.extract(dl_manager.download(urls))`

All those methods returns `tfds.core.Path` (aliases for
[`epath.Path`](https://github.com/google/etils)), which are
[pathlib.Path-like](https://docs.python.org/3/library/pathlib.html) objects.

Those methods supports arbitrary nested structure (`list`, `dict`), like:

```python
extracted_paths = dl_manager.download_and_extract({
    'foo': 'https://example.com/foo.zip',
    'bar': 'https://example.com/bar.zip',
})
# This returns:
assert extracted_paths == {
    'foo': Path('/path/to/extracted_foo/'),
    'bar': Path('/path/extracted_bar/'),
}
```

#### Manual download and extraction

Some data cannot be automatically downloaded (e.g. require a login), in this
case, user will manually download the source data and place it in `manual_dir/`
(defaults to `~/tensorflow_datasets/downloads/manual/`).

Files can then be accessed through `dl_manager.manual_dir`:

```python
class MyDataset(tfds.core.GeneratorBasedBuilder):

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  Register into https://example.org/login to get the data. Place the `data.zip`
  file in the `manual_dir/`.
  """

  def _split_generators(self, dl_manager):
    # data_path is a pathlib-like `Path('<manual_dir>/data.zip')`
    archive_path = dl_manager.manual_dir / 'data.zip'
    # Extract the manually downloaded `data.zip`
    extracted_path = dl_manager.extract(archive_path)
    ...
```

The `manual_dir` location can be customized with `tfds build --manual_dir=` or
using `tfds.download.DownloadConfig`.

#### Read archive directly

`dl_manager.iter_archive` reads an archives sequentially without extracting
them. This can save storage space and improve performances on some file systems.

```python
for filename, fobj in dl_manager.iter_archive('path/to/archive.zip'):
  ...
```

`fobj` has the same methods as `with open('rb') as fobj:` (e.g. `fobj.read()`)

#### Specifying dataset splits

If the dataset comes with pre-defined splits (e.g. `MNIST` has `train` and
`test` splits), keep those. Otherwise, only specify a single `tfds.Split.TRAIN`
split. Users can dynamically create their own subsplits with the
[subsplit API](https://www.tensorflow.org/datasets/splits) (e.g.
`split='train[80%:]'`).

```python
def _split_generators(self, dl_manager):
  # Download source data
  extracted_path = dl_manager.download_and_extract(...)

  # Specify the splits
  return {
      'train': self._generate_examples(
          images_path=extracted_path / 'train_imgs',
          label_path=extracted_path / 'train_labels.csv',
      ),
      'test': self._generate_examples(
          images_path=extracted_path / 'test_imgs',
          label_path=extracted_path / 'test_labels.csv',
      ),
  }
```

### `_generate_examples`: Example generator

`_generate_examples` generates the examples for each split from the source data.

This method will typically read source dataset artifacts (e.g. a CSV file) and
yield `(key, feature_dict)` tuples:

*   `key`: Example identifier. Used to deterministically shuffle the examples
    using `hash(key)` or to sort by key when shuffling is disabled (see section
    [Maintain dataset order](#maintain-dataset-order)). Should be:
    *   **unique**: If two examples use the same key, an exception will be
        raised.
    *   **deterministic**: Should not depend on `download_dir`,
        `os.path.listdir` order,... Generating the data twice should yield the
        same key.
    *   **comparable**: If shuffling is disabled the key will be used to sort
        the dataset.
*   `feature_dict`: A `dict` containing the example values.
    *   The structure should match the `features=` structure defined in
        `tfds.core.DatasetInfo`.
    *   Complex data types (image, video, audio,...) will be automatically
        encoded.
    *   Each feature often accept multiple input types (e.g. video accept
        `/path/to/vid.mp4`, `np.array(shape=(l, h, w, c))`, `List[paths]`,
        `List[np.array(shape=(h, w, c)]`, `List[img_bytes]`,...)
    *   See the
        [feature connector guide](https://www.tensorflow.org/datasets/features)
        for more info.

```python
def _generate_examples(self, images_path, label_path):
  # Read the input data out of the source files
  with label_path.open() as f:
    for row in csv.DictReader(f):
      image_id = row['image_id']
      # And yield (key, feature_dict)
      yield image_id, {
          'image_description': row['description'],
          'image': images_path / f'{image_id}.jpeg',
          'label': row['label'],
      }
```

#### File access and `tf.io.gfile`

In order to support Cloud storage systems, avoid the use of the Python built-in
I/O ops.

Instead, the `dl_manager` returns
[pathlib-like](https://docs.python.org/3/library/pathlib.html) objects directly
compatible with Google Cloud storage:

```python
path = dl_manager.download_and_extract('http://some-website/my_data.zip')

json_path = path / 'data/file.json'

json.loads(json_path.read_text())
```

Alternatively, use `tf.io.gfile` API instead of built-in for file operations:

*   `open` -> `tf.io.gfile.GFile`
*   `os.rename` -> `tf.io.gfile.rename`
*   ...

Pathlib should be prefered to `tf.io.gfile` (see
[rational](https://www.tensorflow.org/datasets/common_gotchas#prefer_to_use_pathlib_api).

#### Extra dependencies

Some datasets require additional Python dependencies only during generation. For
example, the SVHN dataset uses `scipy` to load some data.

If you're adding dataset into the TFDS repository, please use
`tfds.core.lazy_imports` to keep the `tensorflow-datasets` package small. Users
will install additional dependencies only as needed.

To use `lazy_imports`:

*   Add an entry for your dataset into `DATASET_EXTRAS` in
    [`setup.py`](https://github.com/tensorflow/datasets/tree/master/setup.py).
    This makes it so that users can do, for example, `pip install
    'tensorflow-datasets[svhn]'` to install the extra dependencies.
*   Add an entry for your import to
    [`LazyImporter`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/lazy_imports_lib.py)
    and to the
    [`LazyImportsTest`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/lazy_imports_lib_test.py).
*   Use `tfds.core.lazy_imports` to access the dependency (for example,
    `tfds.core.lazy_imports.scipy`) in your `DatasetBuilder`.

#### Corrupted data

Some datasets are not perfectly clean and contain some corrupt data (for
example, the images are in JPEG files but some are invalid JPEG). These examples
should be skipped, but leave a note in the dataset description how many examples
were dropped and why.

### Dataset configuration/variants (tfds.core.BuilderConfig)

Some datasets may have multiple variants, or options for how the data is
preprocessed and written to disk. For example,
[cycle_gan](https://www.tensorflow.org/datasets/catalog/cycle_gan) has one
config per object pairs (`cycle_gan/horse2zebra`, `cycle_gan/monet2photo`,...).

This is done through `tfds.core.BuilderConfig`s:

1.  Define your configuration object as a subclass of `tfds.core.BuilderConfig`.
    For example, `MyDatasetConfig`.

    ```python
    @dataclasses.dataclass
    class MyDatasetConfig(tfds.core.BuilderConfig):
      img_size: Tuple[int, int] = (0, 0)
    ```

    Note: Default values are required because of
    https://bugs.python.org/issue33129.

1.  Define the `BUILDER_CONFIGS = []` class member in `MyDataset` that lists
    `MyDatasetConfig`s that the dataset exposes.

    ```python
    class MyDataset(tfds.core.GeneratorBasedBuilder):
      VERSION = tfds.core.Version('1.0.0')
      # pytype: disable=wrong-keyword-args
      BUILDER_CONFIGS = [
          # `name` (and optionally `description`) are required for each config
          MyDatasetConfig(name='small', description='Small ...', img_size=(8, 8)),
          MyDatasetConfig(name='big', description='Big ...', img_size=(32, 32)),
      ]
      # pytype: enable=wrong-keyword-args
    ```

    Note: `# pytype: disable=wrong-keyword-args` is required because of
    [Pytype bug](https://github.com/google/pytype/issues/628) with dataclasses
    inheritance.

1.  Use `self.builder_config` in `MyDataset` to configure data generation (e.g.
    `shape=self.builder_config.img_size`). This may include setting different
    values in `_info()` or changing download data access.

Notes:

*   Each config has a unique name. The fully qualified name of a config is
    `dataset_name/config_name` (e.g. `coco/2017`).
*   If not specified, the first config in `BUILDER_CONFIGS` will be used (e.g.
    `tfds.load('c4')` default to `c4/en`)

See
[`anli`](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/text/anli.py#L69)
for an example of a dataset that uses `BuilderConfig`s.

### Version

Version can refer to two different meaning:

*   The "external" original data version: e.g. COCO v2019, v2017,...
*   The "internal" TFDS code version: e.g. rename a feature in
    `tfds.features.FeaturesDict`, fix a bug in `_generate_examples`

To update a dataset:

*   For "external" data update: Multiple users may want to access a specific
    year/version simultaneously. This is done by using one
    `tfds.core.BuilderConfig` per version (e.g. `coco/2017`, `coco/2019`) or one
    class per version (e.g. `Voc2007`, `Voc2012`).
*   For "internal" code update: Users only download the most recent version. Any
    code update should increase the `VERSION` class attribute (e.g. from `1.0.0`
    to `VERSION = tfds.core.Version('2.0.0')`) following
    [semantic versioning](https://www.tensorflow.org/datasets/datasets_versioning#semantic).

### Add an import for registration

Don't forget to import the dataset module to your project `__init__` to be
automatically registered in `tfds.load`, `tfds.builder`.

```python
import my_project.datasets.my_dataset  # Register MyDataset

ds = tfds.load('my_dataset')  # MyDataset available
```

For example, if you're contributing to `tensorflow/datasets`, add the module
import to its subdirectory's `__init__.py` (e.g.
[`image/__init__.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/__init__.py).

### Check for common implementation gotchas

Please check for the
[common implementation gotchas](https://www.tensorflow.org/datasets/common_gotchas).

## Test your dataset

### Download and prepare: `tfds build`

To generate the dataset, run `tfds build` from the `my_dataset/` directory:

```sh
cd path/to/datasets/my_dataset/
tfds build --register_checksums
```

Some useful flags for development:

*   `--pdb`: Enter debugging mode if an exception is raised.
*   `--overwrite`: Delete existing files if the dataset was already generated.
*   `--max_examples_per_split`: Only generate the first X examples (default to
    1), rather than the full dataset.
*   `--register_checksums`: Record the checksums of downloaded urls. Should only
    be used while in development.

See the
[CLI documentation](https://www.tensorflow.org/datasets/cli#tfds_build_download_and_prepare_a_dataset)
for full list of flags.

### Checksums

It is recommended to record the checksums of your datasets to guarantee
determinism, help with documentation,... This is done by generating the dataset
with the `--register_checksums` (see previous section).

If you are releasing your datasets through PyPI, don't forget to export the
`checksums.tsv` files (e.g. in the `package_data` of your `setup.py`).

### Unit-test your dataset

`tfds.testing.DatasetBuilderTestCase` is a base `TestCase` to fully exercise a
dataset. It uses "dummy data" as test data that mimic the structure of the
source dataset.

*   The test data should be put in `my_dataset/dummy_data/` directory and should
    mimic the source dataset artifacts as downloaded and extracted. It can be
    created manually or automatically with a script
    ([example script](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/bccd/dummy_data_generation.py)).
*   Make sure to use different data in your test data splits, as the test will
    fail if your dataset splits overlap.
*   **The test data should not contain any copyrighted material**. If in doubt,
    do not create the data using material from the original dataset.

```python
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
      'name1': 'path/to/file1',  # Relative to my_dataset/dummy_data dir.
      'name2': 'file2',
  }


if __name__ == '__main__':
  tfds.testing.test_main()
```

Run the following command to test the dataset.

```sh
python my_dataset_test.py
```

## Send us feedback

We are continuously trying to improve the dataset creation workflow, but can
only do so if we are aware of the issues. Which issues, errors did you
encountered while creating the dataset ? Was there a part which was confusing,
boilerplate or wasn't working the first time ? Please share your
[feedback on github](https://github.com/tensorflow/datasets/issues).
