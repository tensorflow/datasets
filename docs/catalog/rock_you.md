<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rock_you" />
  <meta itemprop="description" content="This dataset contains 14,344,391 passwords that were leaked or stolen from from various sites. The author of this dataset states that &quot;I'm hosting them because it seems like nobody else does (hopefully it isn't because hosting them is illegal :)). Naturally, I'm not the one who stole these; I simply found them online, removed any names/email addresses/etc.&quot;. This dataset is used to train Machine Learning models for password guessing and cracking.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rock_you" />
  <meta itemprop="sameAs" content="https://wiki.skullsecurity.org/Passwords" />
</div>

# `rock_you`

This dataset contains 14,344,391 passwords that were leaked or stolen from from
various sites. The author of this dataset states that "I'm hosting them because
it seems like nobody else does (hopefully it isn't because hosting them is
illegal :)). Naturally, I'm not the one who stole these; I simply found them
online, removed any names/email addresses/etc.". This dataset is used to train
Machine Learning models for password guessing and cracking.

*   URL:
    [https://wiki.skullsecurity.org/Passwords](https://wiki.skullsecurity.org/Passwords)
*   `DatasetBuilder`:
    [`tfds.structured.rock_you.RockYou`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/rock_you.py)
*   Version: `v0.1.0`
*   Size: `133.44 MiB`

## Features
```python
FeaturesDict({
    'password': Text(shape=(None,), dtype=tf.int64, encoder=<ByteTextEncoder vocab_size=257>),
})
```

## Statistics

Split | Examples
:---- | ---------:
ALL   | 14,344,391
TRAIN | 14,344,391

## Urls

*   [https://wiki.skullsecurity.org/Passwords](https://wiki.skullsecurity.org/Passwords)

--------------------------------------------------------------------------------
