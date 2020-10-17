<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="story_cloze" />
  <meta itemprop="description" content="Story Cloze Test is a new commonsense reasoning framework&#10;for evaluating story understanding, story generation, and script learning.&#10;This test requires a system to choose the correct ending to a four-sentence&#10;story.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;story_cloze&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/story_cloze" />
  <meta itemprop="sameAs" content="https://www.cs.rochester.edu/nlp/rocstories/" />
  <meta itemprop="citation" content="@inproceedings{sharma-etal-2018-tackling,&#10;    title = &quot;Tackling the Story Ending Biases in The Story Cloze Test&quot;,&#10;    author = &quot;Sharma, Rishi  and&#10;      Allen, James  and&#10;      Bakhshandeh, Omid  and&#10;      Mostafazadeh, Nasrin&quot;,&#10;    booktitle = &quot;Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)&quot;,&#10;    month = jul,&#10;    year = &quot;2018&quot;,&#10;    address = &quot;Melbourne, Australia&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://www.aclweb.org/anthology/P18-2119&quot;,&#10;    doi = &quot;10.18653/v1/P18-2119&quot;,&#10;    pages = &quot;752--757&quot;,&#10;    abstract = &quot;The Story Cloze Test (SCT) is a recent framework for evaluating story comprehension and script learning. There have been a variety of models tackling the SCT so far. Although the original goal behind the SCT was to require systems to perform deep language understanding and commonsense reasoning for successful narrative understanding, some recent models could perform significantly better than the initial baselines by leveraging human-authorship biases discovered in the SCT dataset. In order to shed some light on this issue, we have performed various data analysis and analyzed a variety of top performing models presented for this task. Given the statistics we have aggregated, we have designed a new crowdsourcing scheme that creates a new SCT dataset, which overcomes some of the biases. We benchmark a few models on the new dataset and show that the top-performing model on the original SCT dataset fails to keep up its performance. Our findings further signify the importance of benchmarking NLP systems on various evolving test sets.&quot;,&#10;}" />
</div>

# `story_cloze`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

Warning: Manual download required. See instructions below.

*   **Description**:

Story Cloze Test is a new commonsense reasoning framework for evaluating story
understanding, story generation, and script learning. This test requires a
system to choose the correct ending to a four-sentence story.

*   **Homepage**:
    [https://www.cs.rochester.edu/nlp/rocstories/](https://www.cs.rochester.edu/nlp/rocstories/)

*   **Source code**:
    [`tfds.text.story_cloze.StoryCloze`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/story_cloze/story_cloze.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Visit https://www.cs.rochester.edu/nlp/rocstories/ and fill out the google
    form to obtain the datasets. You will receive an email with the link to
    download the datasets. For the StoryCloze dataset, use the 2018 versions. The
    validation csv file needs to be renamed to cloze_test_val__winter2018.csv and
    the test csv file needs to be renamed to cloze_test_test__winter2018.csv. Move
    both these files to the manual directory.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Features**:

```python
FeaturesDict({
    'context': Text(shape=(), dtype=tf.string),
    'endings': Sequence(Text(shape=(), dtype=tf.string)),
    'label': tf.int32,
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@inproceedings{sharma-etal-2018-tackling,
    title = "Tackling the Story Ending Biases in The Story Cloze Test",
    author = "Sharma, Rishi  and
      Allen, James  and
      Bakhshandeh, Omid  and
      Mostafazadeh, Nasrin",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P18-2119",
    doi = "10.18653/v1/P18-2119",
    pages = "752--757",
    abstract = "The Story Cloze Test (SCT) is a recent framework for evaluating story comprehension and script learning. There have been a variety of models tackling the SCT so far. Although the original goal behind the SCT was to require systems to perform deep language understanding and commonsense reasoning for successful narrative understanding, some recent models could perform significantly better than the initial baselines by leveraging human-authorship biases discovered in the SCT dataset. In order to shed some light on this issue, we have performed various data analysis and analyzed a variety of top performing models presented for this task. Given the statistics we have aggregated, we have designed a new crowdsourcing scheme that creates a new SCT dataset, which overcomes some of the biases. We benchmark a few models on the new dataset and show that the top-performing model on the original SCT dataset fails to keep up its performance. Our findings further signify the importance of benchmarking NLP systems on various evolving test sets.",
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.
