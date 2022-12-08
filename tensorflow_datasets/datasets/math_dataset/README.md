Mathematics database.

This dataset code generates mathematical question and answer pairs, from a range
of question types at roughly school-level difficulty. This is designed to test
the mathematical learning and algebraic reasoning skills of learning models.

Original paper: Analysing Mathematical Reasoning Abilities of Neural Models
(Saxton, Grefenstette, Hill, Kohli).

Example usage:

```
train_examples, val_examples = tfds.load(
    'math_dataset/arithmetic__mul',
    split=['train', 'test'],
    as_supervised=True)
```
