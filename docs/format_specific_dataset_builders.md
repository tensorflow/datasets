# Format-specific Dataset Builders

[TOC]

This guide documents all format-specific dataset builders currently available in
TFDS.

Format-specific dataset builders are subclasses of
[`tfds.core.GeneratorBasedBuilder`](https://www.tensorflow.org/datasets/api_docs/python/tfds/core/GeneratorBasedBuilder)
which take care of most data processing for a specific data format.

## Datasets based on `tf.data.Dataset`

If you want to create a TFDS dataset from a dataset that's in `tf.data.Dataset`
([reference](https://www.tensorflow.org/api_docs/python/tf/data/Dataset))
format, then you can use `tfds.dataset_builders.TfDataBuilder` (see
[API docs](https://www.tensorflow.org/datasets/api_docs/python/tfds/dataset_builders/TfDataBuilder)).

We envision two typical uses of this class:

*   Creating experimental datasets in a notebook-like environment
*   Defining a dataset builder in code

### Creating a new dataset from a notebook

Suppose you are working in a notebook, loaded some data as a `tf.data.Dataset`,
applied various transformations (map, filter, etc) and now you want to store
this data and easily share it with teammates or load it in other notebooks.
Instead of having to define a new dataset builder class, you can also
instantiate a `tfds.dataset_builders.TfDataBuilder` and call
`download_and_prepare` to store your dataset as a TFDS dataset.

Because it's a TFDS dataset, you can version it, use configs, have different
splits, and document it for easier use later. This means that you also have to
tell TFDS what the features are in your dataset.

Here's a dummy example of how you can use it.

```python
import tensorflow as tf
import tensorflow_datasets as tfds

my_ds_train = tf.data.Dataset.from_tensor_slices({"number": [1, 2, 3]})
my_ds_test = tf.data.Dataset.from_tensor_slices({"number": [4, 5]})

# Optionally define a custom `data_dir`.
# If None, then the default data dir is used.
custom_data_dir = "/my/folder"

# Define the builder.
single_number_builder = tfds.dataset_builders.TfDataBuilder(
    name="my_dataset",
    config="single_number",
    version="1.0.0",
    data_dir=custom_data_dir,
    split_datasets={
        "train": my_ds_train,
        "test": my_ds_test,
    },
    features=tfds.features.FeaturesDict({
        "number": tfds.features.Scalar(dtype=tf.int64),
    }),
    description="My dataset with a single number.",
    release_notes={
        "1.0.0": "Initial release with numbers up to 5!",
    }
)

# Make the builder store the data as a TFDS dataset.
single_number_builder.download_and_prepare()
```

The `download_and_prepare` method will iterate over the input `tf.data.Dataset`s
and store the corresponding TFDS dataset in
`/my/folder/my_dataset/single_number/1.0.0`, which will contain both the train
and test splits.

The `config` argument is optional and can be useful if you want to store
different configs under the same dataset.

The `data_dir` argument can be used to store the generated TFDS dataset in a
different folder, for example in your own sandbox if you don't want to share
this with others (yet). Note that when doing this, you also need to pass the
`data_dir` to `tfds.load`. If the `data_dir` argument is not specified, then the
default TFDS data dir will be used.

#### Loading your dataset

After the TFDS dataset has been stored, it can be loaded from other scripts or
by teammates if they have access to the data:

```python
# If no custom data dir was specified:
ds_test = tfds.load("my_dataset/single_number", split="test")

# When there are multiple versions, you can also specify the version.
ds_test = tfds.load("my_dataset/single_number:1.0.0", split="test")

# If the TFDS was stored in a custom folder, then it can be loaded as follows:
custom_data_dir = "/my/folder"
ds_test = tfds.load("my_dataset/single_number:1.0.0", split="test", data_dir=custom_data_dir)
```

#### Adding a new version or config

After iterating further on your dataset, you may have added or changed some of
the transformations of the source data. To store and share this dataset, you can
easily store this as a new version.

```python
def add_one(example):
  example["number"] = example["number"] + 1
  return example

my_ds_train_v2 = my_ds_train.map(add_one)
my_ds_test_v2 = my_ds_test.map(add_one)

single_number_builder_v2 = tfds.dataset_builders.TfDataBuilder(
    name="my_dataset",
    config="single_number",
    version="1.1.0",
    data_dir=custom_data_dir,
    split_datasets={
        "train": my_ds_train_v2,
        "test": my_ds_test_v2,
    },
    features=tfds.features.FeaturesDict({
        "number": tfds.features.Scalar(dtype=tf.int64, doc="Some number"),
    }),
    description="My dataset with a single number.",
    release_notes={
        "1.1.0": "Initial release with numbers up to 6!",
        "1.0.0": "Initial release with numbers up to 5!",
    }
)

# Make the builder store the data as a TFDS dataset.
single_number_builder_v2.download_and_prepare()
```

### Defining a new dataset builder class

You can also define a new `DatasetBuilder` based on this class.

```python
import tensorflow as tf
import tensorflow_datasets as tfds

class MyDatasetBuilder(tfds.dataset_builders.TfDataBuilder):
  def __init__(self):
    ds_train = tf.data.Dataset.from_tensor_slices([1, 2, 3])
    ds_test = tf.data.Dataset.from_tensor_slices([4, 5])
    super().__init__(
      name="my_dataset",
      version="1.0.0",
      split_datasets={
          "train": ds_train,
          "test": ds_test,
      },
      features=tfds.features.FeaturesDict({
          "number": tfds.features.Scalar(dtype=tf.int64),
      }),
      config="single_number",
      description="My dataset with a single number.",
      release_notes={
          "1.0.0": "Initial release with numbers up to 5!",
      }
    )
```

## CoNLL

### The format

[CoNLL](https://aclanthology.org/W03-0419.pdf) is a popular format used to
represent annotated text data.

CoNLL-formatted data usually contain one token with its linguistic annotations
per line; within the same line, annotations are usually separated by spaces or
tabs. Empty lines represent sentence boundaries.

Consider as an example the following sentence from the
[conll2003](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/text/conll2003/conll2003.py)
dataset, which follows the CoNLL annotation format:

```markdown
U.N. NNP I-NP I-ORG official
NN I-NP O
Ekeus NNP I-NP I-PER
heads VBZ I-VP O
for IN I-PP O
Baghdad NNP I-NP
I-LOC . . O O
```

### `ConllDatasetBuilder`

To add a new CoNLL-based dataset to TFDS, you can base your dataset builder
class on `tfds.dataset_builders.ConllDatasetBuilder`. This base class contains
common code to deal with the specificities of CoNLL datasets (iterating over the
column-based format, precompiled lists of features and tags, ...).

`tfds.dataset_builders.ConllDatasetBuilder` implements a CoNLL-specific
`GeneratorBasedBuilder`. Refer to the following class as a minimal example of a
CoNLL dataset builder:

```python
from tensorflow_datasets.core.dataset_builders.conll import conll_dataset_builder_utils as conll_lib
import tensorflow_datasets.public_api as tfds

class MyCoNNLDataset(tfds.dataset_builders.ConllDatasetBuilder):
  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {'1.0.0': 'Initial release.'}

  # conllu_lib contains a set of ready-to-use CONLL-specific configs.
  BUILDER_CONFIGS = [conll_lib.CONLL_2002_CONFIG]

  def _info(self) -> tfds.core.DatasetInfo:
    return self.create_dataset_info(
      description="My dataset description",
      citation="My dataset citation",
      # ...
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract('https://data-url')

    return {'train': self._generate_examples(path=path / 'train.txt'),
            'test': self._generate_examples(path=path / 'train.txt'),
    }
```

As for standard dataset builders, it requires to overwrite the class methods
`_info` and `_split_generators`. Depending on the dataset, you might need to
update also
[conll_dataset_builder_utils.py](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/core/dataset_builders/conll/conll_dataset_builder_utils.py)
to include the features and the list of tags specific to your dataset.

The `_generate_examples` method should not require further overwriting, unless
your dataset needs specific implementation.

### Examples

Consider
[conll2003](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/text/conll2003/conll2003.py)
as an example of a dataset implemented using the CoNLL-specific dataset builder.

### CLI

The easiest way to write a new CoNLL-based dataset is to use the
[TFDS CLI](https://www.tensorflow.org/datasets/cli):

```sh
cd path/to/my/project/datasets/
tfds new my_dataset --format=conll   # Create `my_dataset/my_dataset.py` CoNLL-specific template files
```

## CoNLL-U

### The format

[CoNLL-U](https://universaldependencies.org/format.html) is a popular format
used to represent annotated text data.

CoNLL-U enhances the CoNLL format by adding a number of features, such as
support for
[multi-token words](https://universaldependencies.org/u/overview/tokenization.html).
CoNLL-U formatted data usually contain one token with its linguistic annotations
per line; within the same line, annotations are usually separated by single tab
characters. Empty lines represent sentence boundaries.

Typically, each CoNLL-U annotated word line contains the following fields, as
reported in the
[official documentation](https://universaldependencies.org/format.html):

*   ID: Word index, integer starting at 1 for each new sentence; may be a range
    for multiword tokens; may be a decimal number for empty nodes (decimal
    numbers can be lower than 1 but must be greater than 0).
*   FORM: Word form or punctuation symbol.
*   LEMMA: Lemma or stem of word form.
*   UPOS: Universal part-of-speech tag.
*   XPOS: Language-specific part-of-speech tag; underscore if not available.
*   FEATS: List of morphological features from the universal feature inventory
    or from a defined language-specific extension; underscore if not available.
*   HEAD: Head of the current word, which is either a value of ID or zero (0).
*   DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0) or a
    defined language-specific subtype of one.
*   DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.
*   MISC: Any other annotation.

Consider as an example the following CoNLL-U annotated sentence from the
[official documentation](https://universaldependencies.org/format.html):

```markdown
1-2    vámonos   _
1      vamos     ir
2      nos       nosotros
3-4    al        _
3      a         a
4      el        el
5      mar       mar
```

### `ConllUDatasetBuilder`

To add a new CoNLL-U based dataset to TFDS, you can base your dataset builder
class on `tfds.dataset_builders.ConllUDatasetBuilder`. This base class contains
common code to deal with the specificities of CoNLL-U datasets (iterating over
the column-based format, precompiled lists of features and tags, ...).

`tfds.dataset_builders.ConllUDatasetBuilder` implements a CoNLL-U specific
`GeneratorBasedBuilder`. Refer to the following class as a minimal example of a
CoNLL-U dataset builder:

```python
from tensorflow_datasets.core.dataset_builders.conll import conllu_dataset_builder_utils as conllu_lib
import tensorflow_datasets.public_api as tfds

class MyCoNNLUDataset(tfds.dataset_builders.ConllUDatasetBuilder):
  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {'1.0.0': 'Initial release.'}

  # conllu_lib contains a set of ready-to-use features.
  BUILDER_CONFIGS = [
    conllu_lib.get_universal_morphology_config(
      language="en",
      features=conllu_lib.UNIVERSAL_DEPENDENCIES_FEATURES,)
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    return self.create_dataset_info(
      description="My dataset description",
      citation="My dataset citation",
      # ...
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract('https://data-url')

    return {'train':
               self._generate_examples(
                 path=path / 'train.txt',
                 # If necessary, add optional custom processing (see conllu_lib
                 # for examples).
                 # process_example_fn=...,
               )
    }
```

As for standard dataset builders, it requires to overwrite the class methods
`_info` and `_split_generators`. Depending on the dataset, you might need to
update also
[conllu_dataset_builder_utils.py](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/core/dataset_builders/conll/conllu_dataset_builder_utils.py)
to include the features and the list of tags specific to your dataset.

The `_generate_examples` method should not require further overwriting, unless
your dataset needs specific implementation. Note that, if your dataset requires
specific preprocessing - for example if it considers non-classic
[universal dependency features](https://universaldependencies.org/guidelines.html) -
you might need to update the `process_example_fn` attribute of your
[`generate_examples`](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/core/dataset_builders/conll/conllu_dataset_builder.py#L192)
function (see the
[xtreme_pos](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/text/universal_dependencies/xtreme_pos.py)
daset as an example).

### Examples

Consider the following datasets, which use the CoNNL-U specific dataset builder,
as examples:

*   [universal_dependencies](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/text/universal_dependencies/universal_dependencies.py)
*   [xtreme_pos](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/text/universal_dependencies/xtreme_pos.py)

### CLI

The easiest way to write a new CoNLL-U based dataset is to use the
[TFDS CLI](https://www.tensorflow.org/datasets/cli):

```sh
cd path/to/my/project/datasets/
tfds new my_dataset --format=conllu   # Create `my_dataset/my_dataset.py` CoNLL-U specific template files
```
