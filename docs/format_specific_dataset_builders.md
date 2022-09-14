# Format-specific Dataset Builders

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
