<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="deep_weeds" />
  <meta itemprop="description" content="The DeepWeeds dataset consists of 17,509 images capturing eight different weed species native to Australia in situ with neighbouring flora.The selected weed species are local to pastoral grasslands across the state of Queensland.The images were collected from weed infestations at the following sites across Queensland: &quot;Black River&quot;, &quot;Charters Towers&quot;,  &quot;Cluden&quot;, &quot;Douglas&quot;, &quot;Hervey Range&quot;, &quot;Kelso&quot;, &quot;McKinlay&quot; and &quot;Paluma&quot;.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;deep_weeds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/deep_weeds-3.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/deep_weeds" />
  <meta itemprop="sameAs" content="https://github.com/AlexOlsen/DeepWeeds" />
  <meta itemprop="citation" content="@article{DeepWeeds2019,&#10;  author = {Alex Olsen and&#10;    Dmitry A. Konovalov and&#10;    Bronson Philippa and&#10;    Peter Ridd and&#10;    Jake C. Wood and&#10;    Jamie Johns and&#10;    Wesley Banks and&#10;    Benjamin Girgenti and&#10;    Owen Kenny and&#10;    James Whinney and&#10;    Brendan Calvert and&#10;    Mostafa {Rahimi Azghadi} and&#10;    Ronald D. White},&#10;  title = {{DeepWeeds: A Multiclass Weed Species Image Dataset for Deep Learning}},&#10;  journal = {Scientific Reports},&#10;  year = 2019,&#10;  number = 2058,&#10;  month = 2,&#10;  volume = 9,&#10;  issue = 1,&#10;  day = 14,&#10;  url = &quot;https://doi.org/10.1038/s41598-018-38343-3&quot;,&#10;  doi = &quot;10.1038/s41598-018-38343-3&quot;&#10;}" />
</div>

# `deep_weeds`

*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=deep_weeds">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

The DeepWeeds dataset consists of 17,509 images capturing eight different weed
species native to Australia in situ with neighbouring flora.The selected weed
species are local to pastoral grasslands across the state of Queensland.The
images were collected from weed infestations at the following sites across
Queensland: "Black River", "Charters Towers", "Cluden", "Douglas", "Hervey
Range", "Kelso", "McKinlay" and "Paluma".

*   **Homepage**:
    [https://github.com/AlexOlsen/DeepWeeds](https://github.com/AlexOlsen/DeepWeeds)

*   **Source code**:
    [`tfds.image_classification.DeepWeeds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/deep_weeds.py)

*   **Versions**:

    *   `2.0.0`: Fixes wrong labels in V1.
    *   **`3.0.0`** (default): Update download URL.

*   **Download size**: `469.32 MiB`

*   **Dataset size**: `469.99 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 17,509

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(256, 256, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=9),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/deep_weeds-3.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/deep_weeds-3.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@article{DeepWeeds2019,
  author = {Alex Olsen and
    Dmitry A. Konovalov and
    Bronson Philippa and
    Peter Ridd and
    Jake C. Wood and
    Jamie Johns and
    Wesley Banks and
    Benjamin Girgenti and
    Owen Kenny and
    James Whinney and
    Brendan Calvert and
    Mostafa {Rahimi Azghadi} and
    Ronald D. White},
  title = {{DeepWeeds: A Multiclass Weed Species Image Dataset for Deep Learning}},
  journal = {Scientific Reports},
  year = 2019,
  number = 2058,
  month = 2,
  volume = 9,
  issue = 1,
  day = 14,
  url = "https://doi.org/10.1038/s41598-018-38343-3",
  doi = "10.1038/s41598-018-38343-3"
}
```
