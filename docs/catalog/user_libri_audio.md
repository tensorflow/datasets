<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="user_libri_audio" />
  <meta itemprop="description" content="UserLibri is a dataset containing paired audio-transcripts and additional text&#10;only data for each of 107 users. It is a reformatting of the LibriSpeech dataset&#10;found at http://www.openslr.org/12, reorganizing the data into users with an&#10;average of 52 LibriSpeech utterances and about 6,700 text example sentences per&#10;user. The UserLibriAudio class provides access to the audio-transcript pairs.&#10;See UserLibriText for the additional text data.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;user_libri_audio&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/user_libri_audio" />
  <meta itemprop="sameAs" content="https://www.kaggle.com/datasets/google/userlibri" />
  <meta itemprop="citation" content="@inproceedings{breiner2022userlibri,&#10;  title={UserLibri: A Dataset for ASR Personalization Using Only Text},&#10;  author={Breiner, Theresa and Ramaswamy, Swaroop and Variani, Ehsan and Garg, Shefali and Mathews, Rajiv and Sim, Khe Chai and Gupta, Kilol and Chen, Mingqing and McConnaughey, Lara},&#10;  booktitle={Proc. Interspeech 2022},&#10;  year={2022}&#10;}" />
</div>

# `user_libri_audio`


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
    [`tfds.audio.userlibri_audio_data.UserLibriAudio`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/userlibri_audio_data/userlibri_audio_data.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `3.37 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split                                  | Examples
:------------------------------------- | -------:
`'test-clean_speaker-1089-book-4217'`  | 64
`'test-clean_speaker-1188-book-20019'` | 45
`'test-clean_speaker-121-book-1041'`   | 10
`'test-clean_speaker-121-book-1989'`   | 15
`'test-clean_speaker-121-book-209'`    | 37
`'test-clean_speaker-1221-book-33'`    | 41
`'test-clean_speaker-1284-book-732'`   | 8
`'test-clean_speaker-1284-book-955'`   | 55
`'test-clean_speaker-1320-book-940'`   | 59
`'test-clean_speaker-1580-book-108'`   | 105
`'test-clean_speaker-1995-book-15265'` | 72
`'test-clean_speaker-2094-book-507'`   | 61
`'test-clean_speaker-2300-book-820'`   | 42
`'test-clean_speaker-237-book-24'`     | 62
`'test-clean_speaker-237-book-2770'`   | 26
`'test-clean_speaker-260-book-11'`     | 21
`'test-clean_speaker-260-book-3748'`   | 61
`'test-clean_speaker-2830-book-1549'`  | 90
`'test-clean_speaker-2961-book-1572'`  | 46
`'test-clean_speaker-3570-book-833'`   | 50
`'test-clean_speaker-3575-book-1827'`  | 57
`'test-clean_speaker-3729-book-2981'`  | 47
`'test-clean_speaker-4077-book-5630'`  | 39
`'test-clean_speaker-4446-book-94'`    | 108
`'test-clean_speaker-4507-book-135'`   | 60
`'test-clean_speaker-4970-book-3178'`  | 63
`'test-clean_speaker-4992-book-10540'` | 41
`'test-clean_speaker-4992-book-22002'` | 21
`'test-clean_speaker-5105-book-1353'`  | 56
`'test-clean_speaker-5142-book-2300'`  | 7
`'test-clean_speaker-5142-book-24811'` | 69
`'test-clean_speaker-5142-book-7891'`  | 26
`'test-clean_speaker-5639-book-14420'` | 42
`'test-clean_speaker-5683-book-9983'`  | 75
`'test-clean_speaker-61-book-28700'`   | 104
`'test-clean_speaker-672-book-1597'`   | 75
`'test-clean_speaker-6829-book-13110'` | 91
`'test-clean_speaker-6930-book-13158'` | 28
`'test-clean_speaker-6930-book-2681'`  | 21
`'test-clean_speaker-6930-book-30905'` | 29
`'test-clean_speaker-7021-book-11667'` | 31
`'test-clean_speaker-7021-book-26177'` | 28
`'test-clean_speaker-7127-book-2681'`  | 71
`'test-clean_speaker-7176-book-13441'` | 46
`'test-clean_speaker-7176-book-38675'` | 28
`'test-clean_speaker-7729-book-6812'`  | 47
`'test-clean_speaker-8224-book-19215'` | 32
`'test-clean_speaker-8230-book-2529'`  | 44
`'test-clean_speaker-8455-book-27067'` | 71
`'test-clean_speaker-8463-book-15263'` | 15
`'test-clean_speaker-8463-book-2488'`  | 59
`'test-clean_speaker-8555-book-36508'` | 16
`'test-clean_speaker-8555-book-39159'` | 46
`'test-clean_speaker-908-book-2002'`   | 26
`'test-clean_speaker-908-book-574'`    | 31
`'test-other_speaker-1688-book-4276'`  | 96
`'test-other_speaker-1998-book-19019'` | 28
`'test-other_speaker-1998-book-28725'` | 87
`'test-other_speaker-2033-book-3436'`  | 52
`'test-other_speaker-2414-book-1998'`  | 60
`'test-other_speaker-2414-book-26379'` | 2
`'test-other_speaker-2414-book-40359'` | 36
`'test-other_speaker-2609-book-12434'` | 39
`'test-other_speaker-2609-book-18096'` | 15
`'test-other_speaker-2609-book-27090'` | 25
`'test-other_speaker-3005-book-76'`    | 108
`'test-other_speaker-3080-book-12544'` | 61
`'test-other_speaker-3331-book-2787'`  | 73
`'test-other_speaker-3528-book-135'`   | 144
`'test-other_speaker-3538-book-10136'` | 27
`'test-other_speaker-3538-book-540'`   | 67
`'test-other_speaker-367-book-5921'`   | 21
`'test-other_speaker-367-book-9464'`   | 34
`'test-other_speaker-3764-book-135'`   | 113
`'test-other_speaker-3997-book-14958'` | 21
`'test-other_speaker-3997-book-1608'`  | 66
`'test-other_speaker-4198-book-16653'` | 31
`'test-other_speaker-4198-book-8166'`  | 60
`'test-other_speaker-4294-book-12176'` | 27
`'test-other_speaker-4294-book-135'`   | 30
`'test-other_speaker-4294-book-4028'`  | 19
`'test-other_speaker-4294-book-9983'`  | 6
`'test-other_speaker-4350-book-1399'`  | 34
`'test-other_speaker-4350-book-4602'`  | 61
`'test-other_speaker-4852-book-28952'` | 113
`'test-other_speaker-533-book-434'`    | 25
`'test-other_speaker-533-book-969'`    | 71
`'test-other_speaker-5442-book-1399'`  | 60
`'test-other_speaker-5442-book-9983'`  | 20
`'test-other_speaker-5484-book-5516'`  | 72
`'test-other_speaker-5764-book-38804'` | 98
`'test-other_speaker-6070-book-1184'`  | 50
`'test-other_speaker-6070-book-33800'` | 19
`'test-other_speaker-6128-book-19717'` | 68
`'test-other_speaker-6432-book-16127'` | 118
`'test-other_speaker-6938-book-3076'`  | 31
`'test-other_speaker-7018-book-3440'`  | 52
`'test-other_speaker-7105-book-1477'`  | 80
`'test-other_speaker-7902-book-21297'` | 135
`'test-other_speaker-7975-book-24585'` | 100
`'test-other_speaker-8131-book-20212'` | 118
`'test-other_speaker-8188-book-19215'` | 12
`'test-other_speaker-8188-book-41326'` | 116
`'test-other_speaker-8280-book-14566'` | 66
`'test-other_speaker-8461-book-3441'`  | 17
`'test-other_speaker-8461-book-6328'`  | 39
`'test-other_speaker-8461-book-9189'`  | 16

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=tf.int64),
    'book_id': Text(shape=(), dtype=tf.string),
    'id': Text(shape=(), dtype=tf.string),
    'speaker_id': Text(shape=(), dtype=tf.string),
    'transcript': Text(shape=(), dtype=tf.string),
    'user_id': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

| Feature    | Class        | Shape   | Dtype     | Description                |
| :--------- | :----------- | :------ | :-------- | :------------------------- |
|            | FeaturesDict |         |           |                            |
| audio      | Audio        | (None,) | tf.int64  | The audio clip containing  |
:            :              :         :           : a snippet from a book read :
:            :              :         :           : aloud                      :
| book_id    | Text         |         | tf.string | The book that this         |
:            :              :         :           : utterance is read from     :
| id         | Text         |         | tf.string | The id of this unique      |
:            :              :         :           : utterance                  :
| speaker_id | Text         |         | tf.string | The speaker who read this  |
:            :              :         :           : utterance                  :
| transcript | Text         |         | tf.string | The text that the speaker  |
:            :              :         :           : read to produce the audio  :
| user_id    | Text         |         | tf.string | The user that this         |
:            :              :         :           : utterance belongs to       :
:            :              :         :           : (unique speaker and book)  :

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('audio', 'transcript')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/user_libri_audio-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{breiner2022userlibri,
  title={UserLibri: A Dataset for ASR Personalization Using Only Text},
  author={Breiner, Theresa and Ramaswamy, Swaroop and Variani, Ehsan and Garg, Shefali and Mathews, Rajiv and Sim, Khe Chai and Gupta, Kilol and Chen, Mingqing and McConnaughey, Lara},
  booktitle={Proc. Interspeech 2022},
  year={2022}
}
```

