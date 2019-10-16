<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="billsum" />
  <meta itemprop="description" content="&#10;BillSum, summarization of US Congressional and California state bills.&#10;&#10;There are several features:&#10;  - text: bill text.&#10;  - summary: summary of the bills.&#10;  - title: title of the bills.&#10;features for us bills. ca bills does not have.&#10;  - text_len: number of chars in text.&#10;  - sum_len: number of chars in summary.&#10;&#10;&#10;To use this dataset:&#10;&#10;```&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('billsum')&#10;```&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/billsum" />
  <meta itemprop="sameAs" content="https://github.com/FiscalNote/BillSum" />
  <meta itemprop="citation" content="&#10;@misc{kornilova2019billsum,&#10;    title={BillSum: A Corpus for Automatic Summarization of US Legislation},&#10;    author={Anastassia Kornilova and Vlad Eidelman},&#10;    year={2019},&#10;    eprint={1910.00523},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}&#10;" />
</div>
# `billsum`

BillSum, summarization of US Congressional and California state bills.

There are several features: - text: bill text. - summary: summary of the
bills. - title: title of the bills. features for us bills. ca bills does not
have. - text_len: number of chars in text. - sum_len: number of chars in
summary.

*   URL:
    [https://github.com/FiscalNote/BillSum](https://github.com/FiscalNote/BillSum)
*   `DatasetBuilder`:
    [`tfds.summarization.billsum.Billsum`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/billsum.py)
*   Version: `v1.0.0`
*   Versions:

    *   **`1.0.0`** (default):

*   Size: `390.52 MiB`

## Features
```python
FeaturesDict({
    'summary': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split   | Examples
:------ | -------:
ALL     | 34,659
TRAIN   | 28,408
TEST    | 5,014
CA_TEST | 1,237

## Urls

*   [https://github.com/FiscalNote/BillSum](https://github.com/FiscalNote/BillSum)

## Supervised keys (for `as_supervised=True`)
`(u'text', u'summary')`

## Citation
```
@misc{kornilova2019billsum,
    title={BillSum: A Corpus for Automatic Summarization of US Legislation},
    author={Anastassia Kornilova and Vlad Eidelman},
    year={2019},
    eprint={1910.00523},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

--------------------------------------------------------------------------------
