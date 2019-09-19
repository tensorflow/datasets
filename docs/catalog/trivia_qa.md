<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="trivia_qa" />
  <meta itemprop="description" content="TriviaqQA is a reading comprehension dataset containing over 650K&#10;question-answer-evidence triples. TriviaqQA includes 95K question-answer&#10;pairs authored by trivia enthusiasts and independently gathered evidence&#10;documents, six per question on average, that provide high quality distant&#10;supervision for answering the questions.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/trivia_qa" />
  <meta itemprop="sameAs" content="http://nlp.cs.washington.edu/triviaqa/" />
</div>

# `trivia_qa`

TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer pairs
authored by trivia enthusiasts and independently gathered evidence documents,
six per question on average, that provide high quality distant supervision for
answering the questions.

*   URL:
    [http://nlp.cs.washington.edu/triviaqa/](http://nlp.cs.washington.edu/triviaqa/)
*   `DatasetBuilder`:
    [`tfds.text.trivia_qa.TriviaQA`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/trivia_qa.py)
*   Version: `v0.1.0`
*   Size: `2.48 GiB`

## Features
```python
FeaturesDict({
    'answer': FeaturesDict({
        'aliases': Sequence(Text(shape=(), dtype=tf.string)),
        'matched_wiki_entity_name': Text(shape=(), dtype=tf.string),
        'normalized_aliases': Sequence(Text(shape=(), dtype=tf.string)),
        'normalized_matched_wiki_entity_name': Text(shape=(), dtype=tf.string),
        'normalized_value': Text(shape=(), dtype=tf.string),
        'type': Text(shape=(), dtype=tf.string),
        'value': Text(shape=(), dtype=tf.string),
    }),
    'entity_pages': Sequence({
        'doc_source': Text(shape=(), dtype=tf.string),
        'file_name': Text(shape=(), dtype=tf.string),
        'title': Text(shape=(), dtype=tf.string),
        'wiki_context': Text(shape=(), dtype=tf.string),
    }),
    'question': Text(shape=(), dtype=tf.string),
    'question_id': Text(shape=(), dtype=tf.string),
    'question_source': Text(shape=(), dtype=tf.string),
    'search_results': Sequence({
        'description': Text(shape=(), dtype=tf.string),
        'file_name': Text(shape=(), dtype=tf.string),
        'rank': Tensor(shape=(), dtype=tf.int32),
        'search_context': Text(shape=(), dtype=tf.string),
        'title': Text(shape=(), dtype=tf.string),
        'url': Text(shape=(), dtype=tf.string),
    }),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 155,594
TRAIN | 138,384
TEST  | 17,210

## Urls

*   [http://nlp.cs.washington.edu/triviaqa/](http://nlp.cs.washington.edu/triviaqa/)

## Citation
```
@article{2017arXivtriviaqa,
       author = {{Joshi}, Mandar and {Choi}, Eunsol and {Weld},
                 Daniel and {Zettlemoyer}, Luke},
        title = "{triviaqa: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension}",
      journal = {arXiv e-prints},
         year = 2017,
          eid = {arXiv:1705.03551},
        pages = {arXiv:1705.03551},
archivePrefix = {arXiv},
       eprint = {1705.03551},
}
```

--------------------------------------------------------------------------------
