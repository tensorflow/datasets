<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="user_libri_text" />
  <meta itemprop="description" content="UserLibri is a dataset containing paired audio-transcripts and additional text&#10;only data for each of 107 users. It is a reformatting of the LibriSpeech dataset&#10;found at http://www.openslr.org/12, reorganizing the data into users with an&#10;average of 52 LibriSpeech utterances and about 6,700 text example sentences per&#10;user. The UserLibriAudio class provides access to the audio-transcript pairs.&#10;See UserLibriText for the additional text data.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;user_libri_text&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/user_libri_text" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/datasets/google/userlibri" />
  <meta itemprop="citation" content="@inproceedings{breiner2022userlibri,&#10;  title={UserLibri: A Dataset for ASR Personalization Using Only Text},&#10;  author={Breiner, Theresa and Ramaswamy, Swaroop and Variani, Ehsan and Garg, Shefali and Mathews, Rajiv and Sim, Khe Chai and Gupta, Kilol and Chen, Mingqing and McConnaughey, Lara},&#10;  booktitle={Proc. Interspeech 2022},&#10;  year={2022}&#10;}" />
</div>

# `user_libri_text`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

UserLibri is a dataset containing paired audio-transcripts and additional text
only data for each of 107 users. It is a reformatting of the LibriSpeech dataset
found at http://www.openslr.org/12, reorganizing the data into users with an
average of 52 LibriSpeech utterances and about 6,700 text example sentences per
user. The UserLibriAudio class provides access to the audio-transcript pairs.
See UserLibriText for the additional text data.

*   **Homepage**:
    [https://www.kaggle.com/datasets/google/userlibri](https://www.kaggle.com/datasets/google/userlibri)

*   **Source code**:
    [`tfds.text.userlibri_lm_data.UserLibriText`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/userlibri_lm_data/userlibri_lm_data.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'book_id': Text(shape=(), dtype=tf.string),
    'text': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

| Feature | Class        | Shape | Dtype     | Description                  |
| :------ | :----------- | :---- | :-------- | :--------------------------- |
|         | FeaturesDict |       |           |                              |
| book_id | Text         |       | tf.string | The book that this text was  |
:         :              :       :           : pulled from                  :
| text    | Text         |       | tf.string | A sentence of text extracted |
:         :              :       :           : from a book                  :

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('text', 'text')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@inproceedings{breiner2022userlibri,
  title={UserLibri: A Dataset for ASR Personalization Using Only Text},
  author={Breiner, Theresa and Ramaswamy, Swaroop and Variani, Ehsan and Garg, Shefali and Mathews, Rajiv and Sim, Khe Chai and Gupta, Kilol and Chen, Mingqing and McConnaughey, Lara},
  booktitle={Proc. Interspeech 2022},
  year={2022}
}
```

