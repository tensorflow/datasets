<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="reddit_tifu" />
  <meta itemprop="description" content="&#10;Reddit dataset, where TIFU denotes the name of subbreddit /r/tifu.&#10;As defined in the publication, styel &quot;short&quot; uses title as summary and&#10;&quot;long&quot; uses tldr as summary.&#10;&#10;Features includes:&#10;  - document: post text without tldr.&#10;  - tldr: tldr line.&#10;  - title: trimmed title without tldr.&#10;  - ups: upvotes.&#10;  - score: score.&#10;  - num_comments: number of comments.&#10;  - upvote_ratio: upvote ratio.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('reddit_tifu', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/reddit_tifu" />
  <meta itemprop="sameAs" content="https://github.com/ctr4si/MMN" />
  <meta itemprop="citation" content="&#10;@misc{kim2018abstractive,&#10;    title={Abstractive Summarization of Reddit Posts with Multi-level Memory Networks},&#10;    author={Byeongchang Kim and Hyunwoo Kim and Gunhee Kim},&#10;    year={2018},&#10;    eprint={1811.00783},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.CL}&#10;}&#10;" />
</div>
# `reddit_tifu`

Reddit dataset, where TIFU denotes the name of subbreddit /r/tifu. As defined in
the publication, styel "short" uses title as summary and "long" uses tldr as
summary.

Features includes: - document: post text without tldr. - tldr: tldr line. -
title: trimmed title without tldr. - ups: upvotes. - score: score. -
num_comments: number of comments. - upvote_ratio: upvote ratio.

*   URL: [https://github.com/ctr4si/MMN](https://github.com/ctr4si/MMN)
*   `DatasetBuilder`:
    [`tfds.summarization.reddit_tifu.RedditTifu`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/summarization/reddit_tifu.py)

`reddit_tifu` is configured with
`tfds.summarization.reddit_tifu.RedditTifuConfig` and has the following
configurations predefined (defaults to the first one):

*   `short` (`v1.1.0`) (`Size: 639.54 MiB`): Using title as summary.

*   `long` (`v1.1.0`) (`Size: 639.54 MiB`): Using TLDR as summary.

## `reddit_tifu/short`
Using title as summary.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 79,740
TRAIN | 79,740

### Features
```python
FeaturesDict({
    'documents': Text(shape=(), dtype=tf.string),
    'num_comments': Tensor(shape=[], dtype=tf.float32),
    'score': Tensor(shape=[], dtype=tf.float32),
    'title': Text(shape=(), dtype=tf.string),
    'tldr': Text(shape=(), dtype=tf.string),
    'ups': Tensor(shape=[], dtype=tf.float32),
    'upvote_ratio': Tensor(shape=[], dtype=tf.float32),
})
```

### Homepage

*   [https://github.com/ctr4si/MMN](https://github.com/ctr4si/MMN)

### Supervised keys (for `as_supervised=True`)
`(u'documents', u'title')`

## `reddit_tifu/long`
Using TLDR as summary.

Versions:

*   **`1.1.0`** (default):

### Statistics

Split | Examples
:---- | -------:
ALL   | 42,139
TRAIN | 42,139

### Features
```python
FeaturesDict({
    'documents': Text(shape=(), dtype=tf.string),
    'num_comments': Tensor(shape=[], dtype=tf.float32),
    'score': Tensor(shape=[], dtype=tf.float32),
    'title': Text(shape=(), dtype=tf.string),
    'tldr': Text(shape=(), dtype=tf.string),
    'ups': Tensor(shape=[], dtype=tf.float32),
    'upvote_ratio': Tensor(shape=[], dtype=tf.float32),
})
```

### Homepage

*   [https://github.com/ctr4si/MMN](https://github.com/ctr4si/MMN)

### Supervised keys (for `as_supervised=True`)
`(u'documents', u'tldr')`

## Citation
```
@misc{kim2018abstractive,
    title={Abstractive Summarization of Reddit Posts with Multi-level Memory Networks},
    author={Byeongchang Kim and Hyunwoo Kim and Gunhee Kim},
    year={2018},
    eprint={1811.00783},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

--------------------------------------------------------------------------------
