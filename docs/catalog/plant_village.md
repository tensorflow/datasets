<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="plant_village" />
  <meta itemprop="description" content="The PlantVillage dataset consists of 54303 healthy and unhealthy leaf images&#10;divided into 38 categories by species and disease.&#10;&#10;NOTE: The original dataset is not available from the original source&#10;(plantvillage.org), therefore we get the unaugmented dataset from a paper that&#10;used that dataset and republished it. Moreover, we dropped images with&#10;Background_without_leaves label, because these were not present in the original&#10;dataset.&#10;&#10;Original paper URL: https://arxiv.org/abs/1511.08060&#10;Dataset URL: https://data.mendeley.com/datasets/tywbtsjrjv/1&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;plant_village&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/plant_village-1.0.2.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/plant_village" />
  <meta itemprop="sameAs" content="https://arxiv.org/abs/1511.08060" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/HughesS15,&#10;  author    = {David P. Hughes and&#10;               Marcel Salath{&#x27;{e}}},&#10;  title     = {An open access repository of images on plant health to enable the&#10;               development of mobile disease diagnostics through machine&#10;               learning and crowdsourcing},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1511.08060},&#10;  year      = {2015},&#10;  url       = {http://arxiv.org/abs/1511.08060},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1511.08060},&#10;  timestamp = {Mon, 13 Aug 2018 16:48:21 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/HughesS15},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `plant_village`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=plant_village">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

The PlantVillage dataset consists of 54303 healthy and unhealthy leaf images
divided into 38 categories by species and disease.

NOTE: The original dataset is not available from the original source
(plantvillage.org), therefore we get the unaugmented dataset from a paper that
used that dataset and republished it. Moreover, we dropped images with
Background_without_leaves label, because these were not present in the original
dataset.

Original paper URL: https://arxiv.org/abs/1511.08060 Dataset URL:
https://data.mendeley.com/datasets/tywbtsjrjv/1

*   **Homepage**:
    [https://arxiv.org/abs/1511.08060](https://arxiv.org/abs/1511.08060)

*   **Source code**:
    [`tfds.image_classification.PlantVillage`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/plant_village.py)

*   **Versions**:

    *   **`1.0.2`** (default): No release notes.

*   **Download size**: `827.82 MiB`

*   **Dataset size**: `815.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 54,303

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=38),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/plant_village-1.0.2.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/plant_village-1.0.2.html";
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
@article{DBLP:journals/corr/HughesS15,
  author    = {David P. Hughes and
               Marcel Salath{'{e}}},
  title     = {An open access repository of images on plant health to enable the
               development of mobile disease diagnostics through machine
               learning and crowdsourcing},
  journal   = {CoRR},
  volume    = {abs/1511.08060},
  year      = {2015},
  url       = {http://arxiv.org/abs/1511.08060},
  archivePrefix = {arXiv},
  eprint    = {1511.08060},
  timestamp = {Mon, 13 Aug 2018 16:48:21 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/HughesS15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
