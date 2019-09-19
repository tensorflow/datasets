<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="squad" />
  <meta itemprop="description" content="Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/squad" />
  <meta itemprop="sameAs" content="https://rajpurkar.github.io/SQuAD-explorer/" />
</div>

# `squad`

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset,
consisting of questions posed by crowdworkers on a set of Wikipedia articles,
where the answer to every question is a segment of text, or span, from the
corresponding reading passage, or the question might be unanswerable.

*   URL:
    [https://rajpurkar.github.io/SQuAD-explorer/](https://rajpurkar.github.io/SQuAD-explorer/)
*   `DatasetBuilder`:
    [`tfds.text.squad.Squad`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/squad.py)

`squad` is configured with `tfds.text.squad.SquadConfig` and has the following
configurations predefined (defaults to the first one):

*   `plain_text` (`v0.1.0`) (`Size: 33.51 MiB`): Plain text

## `squad/plain_text`

Plain text

### Statistics

Split      | Examples
:--------- | -------:
ALL        | 98,169
TRAIN      | 87,599
VALIDATION | 10,570

### Features

```python
FeaturesDict({
    'answers': Sequence({
        'answer_start': Tensor(shape=(), dtype=tf.int32),
        'text': Text(shape=(), dtype=tf.string),
    }),
    'context': Text(shape=(), dtype=tf.string),
    'id': Tensor(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
    'title': Text(shape=(), dtype=tf.string),
})
```

### Urls

*   [https://rajpurkar.github.io/SQuAD-explorer/](https://rajpurkar.github.io/SQuAD-explorer/)

## Citation
```
@article{2016arXiv160605250R,
       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},
                 Konstantin and {Liang}, Percy},
        title = "{SQuAD: 100,000+ Questions for Machine Comprehension of Text}",
      journal = {arXiv e-prints},
         year = 2016,
          eid = {arXiv:1606.05250},
        pages = {arXiv:1606.05250},
archivePrefix = {arXiv},
       eprint = {1606.05250},
}
```

--------------------------------------------------------------------------------
