<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="xsum" />
  <meta itemprop="description" content="&#10;Extreme Summarization (XSum) Dataset.&#10;&#10;There are two features:&#10;  - document: Input news article.&#10;  - summary: One sentence summary of the article.&#10;&#10;This data need to manaully downloaded and extracted as described in&#10;https://github.com/EdinburghNLP/XSum/blob/master/XSum-Dataset/README.md.&#10;The folder 'xsum-extracts-from-downloads' need to be compressed as&#10;'xsum-extracts-from-downloads.tar.gz' and put in manually downloaded folder.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('xsum', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/xsum" />
  <meta itemprop="sameAs" content="https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset" />
  <meta itemprop="citation" content="&#10;@article{Narayan2018DontGM,&#10;  title={Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization},&#10;  author={Shashi Narayan and Shay B. Cohen and Mirella Lapata},&#10;  journal={ArXiv},&#10;  year={2018},&#10;  volume={abs/1808.08745}&#10;}&#10;" />
</div>
# `xsum` (Manual download)

Extreme Summarization (XSum) Dataset.

There are two features: - document: Input news article. - summary: One sentence
summary of the article.

This data need to manaully downloaded and extracted as described in
https://github.com/EdinburghNLP/XSum/blob/master/XSum-Dataset/README.md. The
folder 'xsum-extracts-from-downloads' need to be compressed as
'xsum-extracts-from-downloads.tar.gz' and put in manually downloaded folder.

*   URL:
    [https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset](https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset)
*   `DatasetBuilder`:
    [`tfds.summarization.xsum.Xsum`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/xsum.py)
*   Version: `v1.1.0`
*   Versions:

    *   **`1.1.0`** (default):
    *   `1.0.0`: Dataset without cleaning.

*   Size: `2.59 MiB`

WARNING: This dataset requires you to download the source data manually into
manual_dir (defaults to `~/tensorflow_datasets/manual/xsum/`): Detailed download
instructions (which require running a custom script) are here:
https://github.com/EdinburghNLP/XSum/blob/master/XSum-Dataset/README.md#running-the-download-and-extraction-scripts
Afterwards, please put xsum-extracts-from-downloads.tar.gz file in the
manual_dir.

## Features
```python
FeaturesDict({
    'document': Text(shape=(), dtype=tf.string),
    'summary': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 226,183
TRAIN      | 203,577
VALIDATION | 11,305
TEST       | 11,301

## Homepage

*   [https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset](https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset)

## Supervised keys (for `as_supervised=True`)
`(u'document', u'summary')`

## Citation
```
@article{Narayan2018DontGM,
  title={Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization},
  author={Shashi Narayan and Shay B. Cohen and Mirella Lapata},
  journal={ArXiv},
  year={2018},
  volume={abs/1808.08745}
}
```

--------------------------------------------------------------------------------
