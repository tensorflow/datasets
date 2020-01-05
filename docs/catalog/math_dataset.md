<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="math_dataset" />
  <meta itemprop="description" content="&#10;Mathematics database.&#10;&#10;This dataset code generates mathematical question and answer pairs,&#10;from a range of question types at roughly school-level difficulty.&#10;This is designed to test the mathematical learning and algebraic&#10;reasoning skills of learning models.&#10;&#10;Original paper: Analysing Mathematical Reasoning Abilities of Neural Models&#10;(Saxton, Grefenstette, Hill, Kohli).&#10;&#10;Example usage:&#10;train_examples, val_examples = tfds.load(&#10;    'math_dataset/arithmetic__mul',&#10;    split=['train', 'test'],&#10;    as_supervised=True)&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('math_dataset', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/math_dataset" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/mathematics_dataset" />
  <meta itemprop="citation" content="&#10;@article{2019arXiv,&#10;  author = {Saxton, Grefenstette, Hill, Kohli},&#10;  title = {Analysing Mathematical Reasoning Abilities of Neural Models},&#10;  year = {2019},&#10;  journal = {arXiv:1904.01557}&#10;}&#10;" />
</div>
# `math_dataset`

Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   URL:
    [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)
*   `DatasetBuilder`:
    [`tfds.text.math_dataset.MathDataset`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/math_dataset.py)

`math_dataset` is configured with `tfds.core.dataset_builder.BuilderConfig` and
has the following configurations predefined (defaults to the first one):

*   `algebra__linear_1d` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `algebra__linear_1d_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `algebra__linear_2d` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `algebra__linear_2d_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `algebra__polynomial_roots` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `algebra__polynomial_roots_big` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `algebra__polynomial_roots_composed` (`v1.0.0`) (`Size: ?? GiB`):
    Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `algebra__sequence_next_term` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `algebra__sequence_nth_term` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__add_or_sub` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__add_or_sub_big` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__add_or_sub_in_base` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__add_sub_multiple` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__add_sub_multiple_longer` (`v1.0.0`) (`Size: ?? GiB`):
    Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__div` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__div_big` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__mixed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__mixed_longer` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__mul` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__mul_big` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__mul_div_multiple` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__mul_div_multiple_longer` (`v1.0.0`) (`Size: ?? GiB`):
    Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__nearest_integer_root` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `arithmetic__simplify_surd` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `calculus__differentiate` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `calculus__differentiate_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__closest` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__closest_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__closest_more` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__kth_biggest` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__kth_biggest_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__kth_biggest_more` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__pair` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__pair_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__sort` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__sort_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `comparison__sort_more` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `measurement__conversion` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `measurement__time` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__base_conversion` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__div_remainder` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__div_remainder_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__gcd` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__gcd_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__is_factor` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__is_factor_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__is_prime` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__is_prime_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__lcm` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__lcm_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__list_prime_factors` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__list_prime_factors_composed` (`v1.0.0`) (`Size: ?? GiB`):
    Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__place_value` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__place_value_big` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__place_value_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__round_number` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__round_number_big` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `numbers__round_number_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `polynomials__add` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `polynomials__coefficient_named` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `polynomials__collect` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `polynomials__compose` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `polynomials__evaluate` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `polynomials__evaluate_composed` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `polynomials__expand` (`v1.0.0`) (`Size: ?? GiB`): Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `polynomials__simplify_power` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `probability__swr_p_level_set` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `probability__swr_p_level_set_more_samples` (`v1.0.0`) (`Size: ?? GiB`):
    Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `probability__swr_p_sequence` (`v1.0.0`) (`Size: ?? GiB`): Mathematics
    database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

*   `probability__swr_p_sequence_more_samples` (`v1.0.0`) (`Size: ?? GiB`):
    Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

## `math_dataset/algebra__linear_1d`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/algebra__linear_1d_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/algebra__linear_2d`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/algebra__linear_2d_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/algebra__polynomial_roots`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/algebra__polynomial_roots_big`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/algebra__polynomial_roots_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/algebra__sequence_next_term`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/algebra__sequence_nth_term`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__add_or_sub`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__add_or_sub_big`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__add_or_sub_in_base`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__add_sub_multiple`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__add_sub_multiple_longer`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__div`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__div_big`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__mixed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__mixed_longer`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__mul`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__mul_big`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__mul_div_multiple`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__mul_div_multiple_longer`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__nearest_integer_root`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/arithmetic__simplify_surd`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/calculus__differentiate`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/calculus__differentiate_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__closest`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__closest_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__closest_more`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__kth_biggest`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__kth_biggest_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__kth_biggest_more`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__pair`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__pair_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__sort`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__sort_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/comparison__sort_more`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/measurement__conversion`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/measurement__time`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__base_conversion`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__div_remainder`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__div_remainder_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__gcd`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__gcd_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__is_factor`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__is_factor_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__is_prime`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__is_prime_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__lcm`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__lcm_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__list_prime_factors`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__list_prime_factors_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__place_value`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__place_value_big`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__place_value_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__round_number`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__round_number_big`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/numbers__round_number_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/polynomials__add`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/polynomials__coefficient_named`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/polynomials__collect`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/polynomials__compose`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/polynomials__evaluate`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/polynomials__evaluate_composed`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/polynomials__expand`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/polynomials__simplify_power`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/probability__swr_p_level_set`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/probability__swr_p_level_set_more_samples`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/probability__swr_p_sequence`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## `math_dataset/probability__swr_p_sequence_more_samples`
Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage: train_examples, val_examples = tfds.load(
'math_dataset/arithmetic__mul', split=['train', 'test'], as_supervised=True)

Versions:

*   **`1.0.0`** (default):

### Statistics
None computed

### Features
```python
FeaturesDict({
    'answer': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

### Homepage

*   [https://github.com/deepmind/mathematics_dataset](https://github.com/deepmind/mathematics_dataset)

### Supervised keys (for `as_supervised=True`)
`(u'question', u'answer')`

## Citation
```
@article{2019arXiv,
  author = {Saxton, Grefenstette, Hill, Kohli},
  title = {Analysing Mathematical Reasoning Abilities of Neural Models},
  year = {2019},
  journal = {arXiv:1904.01557}
}
```

--------------------------------------------------------------------------------
