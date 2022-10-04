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

*   **Dataset size**: `86.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'10136'` | 38,496
`'1041'`  | 970
`'10540'` | 3,283
`'108'`   | 5,864
`'11'`    | 1,348
`'11667'` | 3,312
`'1184'`  | 22,062
`'12176'` | 1,467
`'12434'` | 2,796
`'12544'` | 4,080
`'13110'` | 2,634
`'13158'` | 3,440
`'13441'` | 4,145
`'135'`   | 37,263
`'1353'`  | 4,889
`'1399'`  | 18,914
`'14420'` | 6,950
`'14566'` | 3,810
`'1477'`  | 2,526
`'14958'` | 1,495
`'15263'` | 21,085
`'15265'` | 7,647
`'1549'`  | 5,439
`'1572'`  | 2,882
`'1597'`  | 3,586
`'1608'`  | 3,605
`'16127'` | 3,588
`'16653'` | 7,600
`'18096'` | 2,384
`'1827'`  | 4,806
`'19019'` | 3,248
`'19215'` | 13,542
`'19717'` | 3,762
`'1989'`  | 1,105
`'1998'`  | 8,923
`'20019'` | 966
`'2002'`  | 239
`'20212'` | 3,363
`'209'`   | 2,090
`'21297'` | 4,165
`'22002'` | 4,044
`'2300'`  | 22,201
`'24'`    | 3,537
`'24585'` | 1,789
`'24811'` | 2,399
`'2488'`  | 8,239
`'2529'`  | 3,934
`'26177'` | 3,598
`'26379'` | 379
`'2681'`  | 8,872
`'27067'` | 3,149
`'27090'` | 3,217
`'2770'`  | 3,750
`'2787'`  | 4,603
`'28700'` | 5,547
`'28725'` | 3,899
`'28952'` | 2,909
`'2981'`  | 54,305
`'3076'`  | 7,124
`'30905'` | 2,140
`'3178'`  | 8,454
`'33'`    | 3,569
`'33800'` | 5,145
`'3436'`  | 5,899
`'3440'`  | 5,087
`'3441'`  | 6,042
`'36508'` | 521
`'3748'`  | 4,767
`'38675'` | 2,696
`'38804'` | 5,653
`'39159'` | 2,729
`'4028'`  | 9,633
`'40359'` | 7,821
`'41326'` | 6,181
`'4217'`  | 6,003
`'4276'`  | 10,461
`'434'`   | 4,319
`'4602'`  | 4,421
`'507'`   | 9,093
`'540'`   | 5,452
`'5516'`  | 4,963
`'5630'`  | 1,130
`'574'`   | 452
`'5921'`  | 6,040
`'6328'`  | 5,926
`'6812'`  | 5,839
`'732'`   | 22,971
`'76'`    | 6,454
`'7891'`  | 1,476
`'8166'`  | 3,190
`'820'`   | 11,054
`'833'`   | 3,638
`'9189'`  | 8,387
`'94'`    | 1,722
`'940'`   | 6,172
`'9464'`  | 1,695
`'955'`   | 3,051
`'969'`   | 7,799
`'9983'`  | 8,898

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

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/user_libri_text-1.0.0.html";
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

