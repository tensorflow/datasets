# Add a new dataset collection

Follow this guide to create a new dataset collection (either in TFDS or in your
own repository).

## Overview

To add a new dataset collection `my_collection` to TFDS, users need to generate
a `my_collection` folder containing the following files:

```sh
my_collection/
  __init__.py
  my_collection.py # Dataset collection definition
  my_collection_test.py # (Optional) test
  description.md # (Optional) collection description (if not included in my_collection.py)
  citations.md # (Optional) collection citations (if not included in my_collection.py)
```

As a convention, new dataset collections should be added to the
`tensorflow_datasets/dataset_collections/` folder in the TFDS repository.

## Write your dataset collection

All dataset collections are implemented subclasses of
[`tfds.core.dataset_collection_builder.DatasetCollection`](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/core/dataset_collection_builder.py).

Here is a minimal example of a dataset collection builder, defined in the file
`my_collection.py`:

```python
import collections
from typing import Mapping
from tensorflow_datasets.core import dataset_collection_builder
from tensorflow_datasets.core import naming

class MyCollection(dataset_collection_builder.DatasetCollection):
  """Dataset collection builder my_dataset_collection."""

  @property
  def info(self) -> dataset_collection_builder.DatasetCollectionInfo:
    return dataset_collection_builder.DatasetCollectionInfo.from_cls(
        dataset_collection_class=self.__class__,
        description="my_dataset_collection description.",
        release_notes={
            "1.0.0": "Initial release",
        },
    )

  @property
  def datasets(
      self,
  ) -> Mapping[str, Mapping[str, naming.DatasetReference]]:
    return collections.OrderedDict({
        "1.0.0":
            naming.references_for({
                "dataset_1": "natural_questions/default:0.0.2",
                "dataset_2": "media_sum:1.0.0",
            }),
        "1.1.0":
            naming.references_for({
                "dataset_1": "natural_questions/longt5:0.1.0",
                "dataset_2": "media_sum:1.0.0",
                "dataset_3": "squad:3.0.0"
            })
    })
```

The next sections describe the 2 abstract methods to overwrite.

### `info`: dataset collection metadata

The `info` method returns the
[`dataset_collection_builder.DatasetCollectionInfo`](https://github.com/tensorflow/datasets/blob/4854e55ddf5fb68c63ddbd502ad0ef4ec6e08b40/tensorflow_datasets/core/dataset_collection_builder.py#L66)
containing the collection's metadata.

The dataset collection info contains four fields:

*   name: the name of the dataset collection.
*   description: a markdown-formatted description of the dataset collection.
    There are two ways to define a dataset collection's description: (1) As a
    (multi-line) string directly in the collection's `my_collection.py` file -
    similarly as it is already done for TFDS datasets; (2) In a `description.md`
    file, which must be placed in the dataset collection folder.
*   release_notes: a mapping from the dataset collection's version to the
    corresponding release notes.
*   citation: An optional (list of) BibTeX citation(s) for the dataset
    collection. There are two ways to define a dataset collection's citation:
    (1) As a (multi-line) string directly in the colletion's `my_collection.py`
    file - similarly as it is already done for TFDS datasets; (2) In a
    `citations.bib` file, which must be placed in the dataset collection folder.

### `datasets`: define the datasets in the collection

The `datasets` method returns the TFDS datasets in the collection.

It is defined as a dictionary of versions, which describe the evolution of the
dataset collection.

For each version, the included TFDS datasets are stored as a dictionary from
dataset names to
[`naming.DatasetReference`](https://github.com/tensorflow/datasets/blob/4854e55ddf5fb68c63ddbd502ad0ef4ec6e08b40/tensorflow_datasets/core/naming.py#L187).
For example:

```python
class MyCollection(dataset_collection_builder.DatasetCollection):
  ...
  @property
  def datasets(self):
    return {
        "1.0.0": {
            "yes_no":
                naming.DatasetReference(
                    dataset_name="yes_no", version="1.0.0"),
            "sst2":
                naming.DatasetReference(
                    dataset_name="glue", config="sst2", version="2.0.0"),
            "assin2":
                naming.DatasetReference(
                    dataset_name="assin2", version="1.0.0"),
        },
        ...
    }
```

The
[`naming.references_for`](https://github.com/tensorflow/datasets/blob/4854e55ddf5fb68c63ddbd502ad0ef4ec6e08b40/tensorflow_datasets/core/naming.py#L257)
method provides a more compact way to express the same as above:

```python
class MyCollection(dataset_collection_builder.DatasetCollection):
  ...
  @property
  def datasets(self):
    return {
        "1.0.0":
            naming.references_for({
                "yes_no": "yes_no:1.0.0",
                "sst2": "glue/sst:2.0.0",
                "assin2": "assin2:1.0.0",
            }),
        ...
    }
```

## Unit-test your dataset collection

[DatasetCollectionTestBase](https://github.com/tensorflow/datasets/blob/4854e55ddf5fb68c63ddbd502ad0ef4ec6e08b40/tensorflow_datasets/testing/dataset_collection_builder_testing.py#L28)
is a base test class for dataset collections. It provides a number of simple
checks to guarantee that the dataset collection is correctly registered, and its
datasets exist in TFDS.

The only class attribute to set is `DATASET_COLLECTION_CLASS`, which specifies
the class object of dataset collection to test.

Additionally, users can set the following class attributes:

*   `VERSION`: The version of the dataset collection used to run the test
    (defaults to the latest version).
*   `DATASETS_TO_TEST`: List containing the datasets to test existence for in
    TFDS (defaults to all datasets in the collection).
*   `CHECK_DATASETS_VERSION`: Whether to check for the existence of the
    versioned datasets in the dataset collection, or for their default versions
    (defaults to true).

The simplest valid test for a dataset collection would be:

```python
from tensorflow_datasets.testing.dataset_collection_builder_testing import DatasetCollectionTestBase
from . import my_collection

class TestMyCollection(DatasetCollectionTestBase):
  DATASET_COLLECTION_CLASS = my_collection.MyCollection
```

Run the following command to test the dataset collection.

```sh
python my_dataset_test.py
```

## Feedback

We are continuously trying to improve the dataset creation workflow, but can
only do so if we are aware of the issues. Which issues or errors did you
encounter while creating the dataset collection? Was there a part which was
confusing, or wasn't working the first time?

Please share your feedback on
[GitHub](https://github.com/tensorflow/datasets/issues).
