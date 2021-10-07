<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="ref_coco" />
  <meta itemprop="description" content="A collection of 3 referring expression datasets based off images in the&#10;COCO dataset. A referring expression is a piece of text that describes a&#10;unique object in an image. These datasets are collected by asking human raters&#10;to disambiguate objects delineated by bounding boxes in the COCO dataset.&#10;&#10;RefCoco and RefCoco+ are from Kazemzadeh et al. 2014. RefCoco+ expressions&#10;are strictly appearance based descriptions, which they enforced by preventing&#10;raters from using location based descriptions (e.g., &quot;person to the right&quot; is&#10;not a valid description for RefCoco+). RefCocoG is from Mao et al. 2016, and&#10;has more rich description of objects compared to RefCoco due to differences&#10;in the annotation process. In particular, RefCoco was collected in an&#10;interactive game-based setting, while RefCocoG was collected in a&#10;non-interactive setting. On average, RefCocoG has 8.4 words per expression&#10;while RefCoco has 3.5 words.&#10;&#10;Each dataset has different split allocations that are typically all reported&#10;in papers. The &quot;testA&quot; and &quot;testB&quot; sets in RefCoco and RefCoco+ contain only&#10;people and only non-people respectively. Images are partitioned into the various&#10;splits. In the &quot;google&quot; split, objects, not images, are partitioned between the&#10;train and non-train splits. This means that the same image can appear in both&#10;the train and validation split, but the objects being referred to in the image&#10;will be different between the two sets. In contrast, the &quot;unc&quot; and &quot;umd&quot; splits&#10;partition images between the train, validation, and test split.&#10;In RefCocoG, the &quot;google&quot; split does not have a canonical test set,&#10;and the validation set is typically reported in papers as &quot;val*&quot;.&#10;&#10;Stats for each dataset and split (&quot;refs&quot; is the number of referring expressions,&#10;and &quot;images&quot; is the number of images):&#10;&#10;|  dataset  | partition |  split  | refs   | images |&#10;| --------- | --------- | ------- | ------ | ------ |&#10;|   refcoco |   google  |  train  | 40000  |  19213 |&#10;|   refcoco |   google  |    val  |  5000  |   4559 |&#10;|   refcoco |   google  |   test  |  5000  |   4527 |&#10;|   refcoco |      unc  |  train  | 42404  |  16994 |&#10;|   refcoco |      unc  |    val  |  3811  |   1500 |&#10;|   refcoco |      unc  |  testA  |  1975  |    750 |&#10;|   refcoco |      unc  |  testB  |  1810  |    750 |&#10;|  refcoco+ |      unc  |  train  | 42278  |  16992 |&#10;|  refcoco+ |      unc  |    val  |  3805  |   1500 |&#10;|  refcoco+ |      unc  |  testA  |  1975  |    750 |&#10;|  refcoco+ |      unc  |  testB  |  1798  |    750 |&#10;|  refcocog |   google  |  train  | 44822  |  24698 |&#10;|  refcocog |   google  |    val  |  5000  |   4650 |&#10;|  refcocog |      umd  |  train  | 42226  |  21899 |&#10;|  refcocog |      umd  |    val  |  2573  |   1300 |&#10;|  refcocog |      umd  |   test  |  5023  |   2600 |&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;ref_coco&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/ref_coco-refcoco_unc-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/ref_coco" />
  <meta itemprop="sameAs" content="https://github.com/lichengunc/refer" />
  <meta itemprop="citation" content="@inproceedings{kazemzadeh2014referitgame,&#10;  title={Referitgame: Referring to objects in photographs of natural scenes},&#10;  author={Kazemzadeh, Sahar and Ordonez, Vicente and Matten, Mark and Berg, Tamara},&#10;  booktitle={Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP)},&#10;  pages={787--798},&#10;  year={2014}&#10;}&#10;@inproceedings{yu2016modeling,&#10;  title={Modeling context in referring expressions},&#10;  author={Yu, Licheng and Poirson, Patrick and Yang, Shan and Berg, Alexander C and Berg, Tamara L},&#10;  booktitle={European Conference on Computer Vision},&#10;  pages={69--85},&#10;  year={2016},&#10;  organization={Springer}&#10;}&#10;@inproceedings{mao2016generation,&#10;  title={Generation and Comprehension of Unambiguous Object Descriptions},&#10;  author={Mao, Junhua and Huang, Jonathan and Toshev, Alexander and Camburu, Oana and Yuille, Alan and Murphy, Kevin},&#10;  booktitle={CVPR},&#10;  year={2016}&#10;}&#10;@inproceedings{nagaraja2016modeling,&#10;  title={Modeling context between objects for referring expression understanding},&#10;  author={Nagaraja, Varun K and Morariu, Vlad I and Davis, Larry S},&#10;  booktitle={European Conference on Computer Vision},&#10;  pages={792--807},&#10;  year={2016},&#10;  organization={Springer}&#10;}" />
</div>

# `ref_coco`


Warning: Manual download required. See instructions below.

*   **Description**:

A collection of 3 referring expression datasets based off images in the COCO
dataset. A referring expression is a piece of text that describes a unique
object in an image. These datasets are collected by asking human raters to
disambiguate objects delineated by bounding boxes in the COCO dataset.

RefCoco and RefCoco+ are from Kazemzadeh et al. 2014. RefCoco+ expressions are
strictly appearance based descriptions, which they enforced by preventing raters
from using location based descriptions (e.g., "person to the right" is not a
valid description for RefCoco+). RefCocoG is from Mao et al. 2016, and has more
rich description of objects compared to RefCoco due to differences in the
annotation process. In particular, RefCoco was collected in an interactive
game-based setting, while RefCocoG was collected in a non-interactive setting.
On average, RefCocoG has 8.4 words per expression while RefCoco has 3.5 words.

Each dataset has different split allocations that are typically all reported in
papers. The "testA" and "testB" sets in RefCoco and RefCoco+ contain only people
and only non-people respectively. Images are partitioned into the various
splits. In the "google" split, objects, not images, are partitioned between the
train and non-train splits. This means that the same image can appear in both
the train and validation split, but the objects being referred to in the image
will be different between the two sets. In contrast, the "unc" and "umd" splits
partition images between the train, validation, and test split. In RefCocoG, the
"google" split does not have a canonical test set, and the validation set is
typically reported in papers as "val*".

Stats for each dataset and split ("refs" is the number of referring expressions,
and "images" is the number of images):

dataset  | partition | split | refs  | images
-------- | --------- | ----- | ----- | ------
refcoco  | google    | train | 40000 | 19213
refcoco  | google    | val   | 5000  | 4559
refcoco  | google    | test  | 5000  | 4527
refcoco  | unc       | train | 42404 | 16994
refcoco  | unc       | val   | 3811  | 1500
refcoco  | unc       | testA | 1975  | 750
refcoco  | unc       | testB | 1810  | 750
refcoco+ | unc       | train | 42278 | 16992
refcoco+ | unc       | val   | 3805  | 1500
refcoco+ | unc       | testA | 1975  | 750
refcoco+ | unc       | testB | 1798  | 750
refcocog | google    | train | 44822 | 24698
refcocog | google    | val   | 5000  | 4650
refcocog | umd       | train | 42226 | 21899
refcocog | umd       | val   | 2573  | 1300
refcocog | umd       | test  | 5023  | 2600

*   **Homepage**:
    [https://github.com/lichengunc/refer](https://github.com/lichengunc/refer)

*   **Source code**:
    [`tfds.vision_language.refcoco.RefCoco`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/vision_language/refcoco/refcoco.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>

*   Follow the instructions in https://github.com/lichengunc/refer and download
    the annotations and the images, matching the data/ directory specified in
    the repo.

1.  Follow the instructions of PythonAPI in
    https://github.com/cocodataset/cocoapi to get pycocotools and the
    instances_train2014 annotations file from https://cocodataset.org/#download

2.  Add both refer.py from (1) and pycocotools from (2) to your PYTHONPATH.

3.  Run manual_download_process.py to generate refcoco.json, replacing
    `ref_data_root`, `coco_annotations_file`, and `out_file` with the values
    corresponding to where you have downloaded / want to save these files. Note
    that manual_download_process.py can be found in the TFDS repository.

4.  Download the COCO training set from https://cocodataset.org/#download and
    stick it into a folder called `coco_train2014/`. Move `refcoco.json` to the
    same level as `coco_train2014`.

5.  Follow the standard manual download instructions.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Features**:

```python
FeaturesDict({
    'coco_annotations': Sequence({
        'area': tf.int64,
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'id': tf.int64,
        'label': tf.int64,
    }),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/id': tf.int64,
    'objects': Sequence({
        'area': tf.int64,
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'gt_box_index': tf.int64,
        'id': tf.int64,
        'label': tf.int64,
        'refexp': Sequence({
            'raw': Text(shape=(), dtype=tf.string),
            'refexp_id': tf.int64,
        }),
    }),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@inproceedings{kazemzadeh2014referitgame,
  title={Referitgame: Referring to objects in photographs of natural scenes},
  author={Kazemzadeh, Sahar and Ordonez, Vicente and Matten, Mark and Berg, Tamara},
  booktitle={Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP)},
  pages={787--798},
  year={2014}
}
@inproceedings{yu2016modeling,
  title={Modeling context in referring expressions},
  author={Yu, Licheng and Poirson, Patrick and Yang, Shan and Berg, Alexander C and Berg, Tamara L},
  booktitle={European Conference on Computer Vision},
  pages={69--85},
  year={2016},
  organization={Springer}
}
@inproceedings{mao2016generation,
  title={Generation and Comprehension of Unambiguous Object Descriptions},
  author={Mao, Junhua and Huang, Jonathan and Toshev, Alexander and Camburu, Oana and Yuille, Alan and Murphy, Kevin},
  booktitle={CVPR},
  year={2016}
}
@inproceedings{nagaraja2016modeling,
  title={Modeling context between objects for referring expression understanding},
  author={Nagaraja, Varun K and Morariu, Vlad I and Davis, Larry S},
  booktitle={European Conference on Computer Vision},
  pages={792--807},
  year={2016},
  organization={Springer}
}
```

## ref_coco/refcoco_unc (default config)

*   **Dataset size**: `3.24 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'testA'`      | 750
`'testB'`      | 750
`'train'`      | 16,994
`'validation'` | 1,500

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/ref_coco-refcoco_unc-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ref_coco-refcoco_unc-1.0.0.html";
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

## ref_coco/refcoco_google

*   **Dataset size**: `4.60 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 4,527
`'train'`      | 19,213
`'validation'` | 4,559

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/ref_coco-refcoco_google-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ref_coco-refcoco_google-1.0.0.html";
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

## ref_coco/refcocoplus_unc

*   **Dataset size**: `3.24 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'testA'`      | 750
`'testB'`      | 750
`'train'`      | 16,992
`'validation'` | 1,500

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/ref_coco-refcocoplus_unc-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ref_coco-refcocoplus_unc-1.0.0.html";
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

## ref_coco/refcocog_google

*   **Dataset size**: `4.59 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 24,698
`'validation'` | 4,650

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/ref_coco-refcocog_google-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ref_coco-refcocog_google-1.0.0.html";
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

## ref_coco/refcocog_umd

*   **Dataset size**: `4.04 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,600
`'train'`      | 21,899
`'validation'` | 1,300

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/ref_coco-refcocog_umd-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ref_coco-refcocog_umd-1.0.0.html";
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