<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="coco_captions" />
  <meta itemprop="description" content="COCO is a large-scale object detection, segmentation, and&#10;captioning dataset. This version contains images, bounding boxes, labels, and&#10;captions from COCO 2014, split into the subsets defined by Karpathy and Li&#10;(2015). This effectively divides the original COCO 2014 validation data into&#10;new 5000-image validation and test sets, plus a &quot;restval&quot; set containing the&#10;remaining ~30k images. All splits have caption annotations.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;coco_captions&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/coco_captions-2014-1.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/coco_captions" />
  <meta itemprop="sameAs" content="http://cocodataset.org/#home" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/LinMBHPRDZ14,&#10;  author    = {Tsung{-}Yi Lin and&#10;               Michael Maire and&#10;               Serge J. Belongie and&#10;               Lubomir D. Bourdev and&#10;               Ross B. Girshick and&#10;               James Hays and&#10;               Pietro Perona and&#10;               Deva Ramanan and&#10;               Piotr Doll{&#x27;{a}}r and&#10;               C. Lawrence Zitnick},&#10;  title     = {Microsoft {COCO:} Common Objects in Context},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1405.0312},&#10;  year      = {2014},&#10;  url       = {http://arxiv.org/abs/1405.0312},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1405.0312},&#10;  timestamp = {Mon, 13 Aug 2018 16:48:13 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/LinMBHPRDZ14},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}@inproceedings{DBLP:conf/cvpr/KarpathyL15,&#10;  author    = {Andrej Karpathy and&#10;               Fei{-}Fei Li},&#10;  title     = {Deep visual-semantic alignments for generating image&#10;               descriptions},&#10;  booktitle = {{IEEE} Conference on Computer Vision and Pattern Recognition,&#10;               {CVPR} 2015, Boston, MA, USA, June 7-12, 2015},&#10;  pages     = {3128--3137},&#10;  publisher = {{IEEE} Computer Society},&#10;  year      = {2015},&#10;  url       = {https://doi.org/10.1109/CVPR.2015.7298932},&#10;  doi       = {10.1109/CVPR.2015.7298932},&#10;  timestamp = {Wed, 16 Oct 2019 14:14:50 +0200},&#10;  biburl    = {https://dblp.org/rec/conf/cvpr/KarpathyL15.bib},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `coco_captions`

*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=coco_captions">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

COCO is a large-scale object detection, segmentation, and captioning dataset.
This version contains images, bounding boxes, labels, and captions from COCO
2014, split into the subsets defined by Karpathy and Li (2015). This effectively
divides the original COCO 2014 validation data into new 5000-image validation
and test sets, plus a "restval" set containing the remaining ~30k images. All
splits have caption annotations.

*   **Config description**: This version contains images, bounding boxes and
    labels for the 2014 version.

*   **Homepage**: [http://cocodataset.org/#home](http://cocodataset.org/#home)

*   **Source code**:
    [`tfds.object_detection.CocoCaptions`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/object_detection/coco_captions.py)

*   **Versions**:

    *   **`1.1.0`** (default): No release notes.

*   **Download size**: `37.61 GiB`

*   **Dataset size**: `18.83 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split       | Examples
:---------- | -------:
`'restval'` | 30,504
`'test'`    | 5,000
`'train'`   | 82,783
`'val'`     | 5,000

*   **Features**:

```python
FeaturesDict({
    'captions': Sequence({
        'id': tf.int64,
        'text': tf.string,
    }),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
    'image/id': tf.int64,
    'objects': Sequence({
        'area': tf.int64,
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'id': tf.int64,
        'is_crowd': tf.bool,
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=80),
    }),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/coco_captions-2014-1.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/coco_captions-2014-1.1.0.html";
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
@article{DBLP:journals/corr/LinMBHPRDZ14,
  author    = {Tsung{-}Yi Lin and
               Michael Maire and
               Serge J. Belongie and
               Lubomir D. Bourdev and
               Ross B. Girshick and
               James Hays and
               Pietro Perona and
               Deva Ramanan and
               Piotr Doll{'{a}}r and
               C. Lawrence Zitnick},
  title     = {Microsoft {COCO:} Common Objects in Context},
  journal   = {CoRR},
  volume    = {abs/1405.0312},
  year      = {2014},
  url       = {http://arxiv.org/abs/1405.0312},
  archivePrefix = {arXiv},
  eprint    = {1405.0312},
  timestamp = {Mon, 13 Aug 2018 16:48:13 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/LinMBHPRDZ14},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}@inproceedings{DBLP:conf/cvpr/KarpathyL15,
  author    = {Andrej Karpathy and
               Fei{-}Fei Li},
  title     = {Deep visual-semantic alignments for generating image
               descriptions},
  booktitle = {{IEEE} Conference on Computer Vision and Pattern Recognition,
               {CVPR} 2015, Boston, MA, USA, June 7-12, 2015},
  pages     = {3128--3137},
  publisher = {{IEEE} Computer Society},
  year      = {2015},
  url       = {https://doi.org/10.1109/CVPR.2015.7298932},
  doi       = {10.1109/CVPR.2015.7298932},
  timestamp = {Wed, 16 Oct 2019 14:14:50 +0200},
  biburl    = {https://dblp.org/rec/conf/cvpr/KarpathyL15.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

## coco_captions/2014 (default config)
