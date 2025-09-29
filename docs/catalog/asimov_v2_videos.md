<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="asimov_v2_videos" />
  <meta itemprop="description" content="Photorealistic videos involving potential physical injury scenarios.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;asimov_v2_videos&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/asimov_v2_videos" />
  <meta itemprop="sameAs" content="https://asimov-benchmark.github.io/v2/" />
  <meta itemprop="citation" content="" />
</div>

# `asimov_v2_videos`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Photorealistic videos involving potential physical injury scenarios.

*   **Homepage**:
    [https://asimov-benchmark.github.io/v2/](https://asimov-benchmark.github.io/v2/)

*   **Source code**:
    [`tfds.robotics.asimov.AsimovV2Videos`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/asimov/asimov_v2.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `647.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split   | Examples
:------ | -------:
`'val'` | 287

*   **Feature structure**:

```python
FeaturesDict({
    'answer': Text(shape=(), dtype=string),
    'prompt': Text(shape=(), dtype=string),
    'video': FeaturesDict({
        'frames': Sequence(Image(shape=(None, None, 3), dtype=uint8)),
        'timestamps': Sequence(Text(shape=(), dtype=string)),
    }),
})
```

*   **Feature documentation**:

| Feature          | Class           | Shape        | Dtype  | Description |
| :--------------- | :-------------- | :----------- | :----- | :---------- |
|                  | FeaturesDict    |              |        |             |
| answer           | Text            |              | string |             |
| prompt           | Text            |              | string |             |
| video            | FeaturesDict    |              |        |             |
| video/frames     | Sequence(Image) | (None, None, | uint8  |             |
:                  :                 : None, 3)     :        :             :
| video/timestamps | Sequence(Text)  | (None,)      | string |             |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/asimov_v2_videos-0.1.0.html";
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

