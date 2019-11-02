<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="aeslc" />
  <meta itemprop="description" content="&#10;A collection of email messages of employees in the Enron Corporation.&#10;&#10;There are two features:&#10;  - email_body: email body text.&#10;  - subject_line: email subject text.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('aeslc', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/aeslc" />
  <meta itemprop="sameAs" content="https://github.com/ryanzhumich/AESLC" />
  <meta itemprop="citation" content="&#10;@misc{zhang2019email,&#10;    title={This Email Could Save Your Life: Introducing the Task of Email Subject Line Generation},&#10;    author={Rui Zhang and Joel Tetreault},&#10;    year={2019},&#10;    eprint={1906.03497},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}&#10;" />
</div>
# `aeslc`

A collection of email messages of employees in the Enron Corporation.

There are two features: - email_body: email body text. - subject_line: email
subject text.

*   URL:
    [https://github.com/ryanzhumich/AESLC](https://github.com/ryanzhumich/AESLC)
*   `DatasetBuilder`:
    [`tfds.summarization.aeslc.Aeslc`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/aeslc.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):

*   Size: `11.10 MiB`

## Features
```python
FeaturesDict({
    'email_body': Text(shape=(), dtype=tf.string),
    'subject_line': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 18,302
TRAIN      | 14,436
VALIDATION | 1,960
TEST       | 1,906

## Homepage

*   [https://github.com/ryanzhumich/AESLC](https://github.com/ryanzhumich/AESLC)

## Supervised keys (for `as_supervised=True`)
`(u'email_body', u'subject_line')`

## Citation
```
@misc{zhang2019email,
    title={This Email Could Save Your Life: Introducing the Task of Email Subject Line Generation},
    author={Rui Zhang and Joel Tetreault},
    year={2019},
    eprint={1906.03497},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

--------------------------------------------------------------------------------
