# Format-specific Dataset Builders

[TOC]

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
`GeneratorBasedBuilder`.

As for standard dataset builders, it requires to overwrite the class methods
`_info` and `_split_generators`. Depending on the dataset, you might need to
update also
[conll_dataset_builder_utils.py](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/core/dataset_builders/conll_dataset_builder_utils.py)
to include the features and the list of tags specific to your dataset.

The `_generate_examples` method should not require further overwriting, unless
your dataset needs specific implementation.

### Examples

Consider
[conll2003](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/text/conll2003/conll2003.py)
as an example of a dataset implemented using the CoNLL-specific dataset builder.
