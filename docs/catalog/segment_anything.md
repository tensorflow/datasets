<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="segment_anything" />
  <meta itemprop="description" content="# SA-1B Download&#10;&#10;Segment Anything 1 Billion (SA-1B) is a dataset designed for training&#10;general-purpose object segmentation models from open world images. The dataset&#10;was introduced in the paper&#10;[&quot;Segment Anything&quot;](https://arxiv.org/abs/2304.02643).&#10;&#10;The SA-1B dataset consists of 11M diverse, high-resolution, licensed, and&#10;privacy-protecting images and 1.1B mask annotations. Masks are given in the COCO&#10;run-length encoding (RLE) format, and do not have classes.&#10;&#10;The license is custom. Please, read the full terms and conditions on&#10;https://ai.facebook.com/datasets/segment-anything-downloads.&#10;&#10;All the features are in the original dataset except `image.content` (content&#10;of the image).&#10;&#10;You can decode segmentation masks with:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;pycocotools = tfds.core.lazy_imports.pycocotools&#10;&#10;ds = tfds.load(&#x27;segment_anything&#x27;, split=&#x27;train&#x27;)&#10;for example in tfds.as_numpy(ds):&#10;  segmentation = example[&#x27;annotations&#x27;][&#x27;segmentation&#x27;]&#10;  for counts, size in zip(segmentation[&#x27;counts&#x27;], segmentation[&#x27;size&#x27;]):&#10;    encoded_mask = {&#x27;size&#x27;: size, &#x27;counts&#x27;: counts}&#10;    mask = pycocotools.decode(encoded_mask)  # np.array(dtype=uint8) mask&#10;    ...&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;segment_anything&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/segment_anything" />
  <meta itemprop="sameAs" content="https://ai.facebook.com/datasets/segment-anything-downloads" />
  <meta itemprop="citation" content="@misc{kirillov2023segment,&#10;  title={Segment Anything},&#10;  author={Alexander Kirillov and Eric Mintun and Nikhila Ravi and Hanzi Mao and Chloe Rolland and Laura Gustafson and Tete Xiao and Spencer Whitehead and Alexander C. Berg and Wan-Yen Lo and Piotr Dollár and Ross Girshick},&#10;  year={2023},&#10;  eprint={2304.02643},&#10;  archivePrefix={arXiv},&#10;  primaryClass={cs.CV}&#10;}" />
</div>

# `segment_anything`


Warning: Manual download required. See instructions below.

*   **Description**:

# SA-1B Download

Segment Anything 1 Billion (SA-1B) is a dataset designed for training
general-purpose object segmentation models from open world images. The dataset
was introduced in the paper
["Segment Anything"](https://arxiv.org/abs/2304.02643).

The SA-1B dataset consists of 11M diverse, high-resolution, licensed, and
privacy-protecting images and 1.1B mask annotations. Masks are given in the COCO
run-length encoding (RLE) format, and do not have classes.

The license is custom. Please, read the full terms and conditions on
https://ai.facebook.com/datasets/segment-anything-downloads.

All the features are in the original dataset except `image.content` (content of
the image).

You can decode segmentation masks with:

```python
import tensorflow_datasets as tfds

pycocotools = tfds.core.lazy_imports.pycocotools

ds = tfds.load('segment_anything', split='train')
for example in tfds.as_numpy(ds):
  segmentation = example['annotations']['segmentation']
  for counts, size in zip(segmentation['counts'], segmentation['size']):
    encoded_mask = {'size': size, 'counts': counts}
    mask = pycocotools.decode(encoded_mask)  # np.array(dtype=uint8) mask
    ...
```

*   **Homepage**:
    [https://ai.facebook.com/datasets/segment-anything-downloads](https://ai.facebook.com/datasets/segment-anything-downloads)

*   **Source code**:
    [`tfds.datasets.segment_anything.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/segment_anything/segment_anything_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `10.28 TiB`

*   **Dataset size**: `10.59 TiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Download the links file from https://ai.facebook.com/datasets/segment-anything-downloads. `manual_dir` should contain the links file saved as segment_anything_links.txt.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | ---------:
`'train'` | 11,185,362

*   **Feature structure**:

```python
FeaturesDict({
    'annotations': Sequence({
        'area': Scalar(shape=(), dtype=uint64, description=The area in pixels of the mask.),
        'bbox': BBoxFeature(shape=(4,), dtype=float32, description=The box around the mask, in TFDS format.),
        'crop_box': BBoxFeature(shape=(4,), dtype=float32, description=The crop of the image used to generate the mask, in TFDS format.),
        'id': Scalar(shape=(), dtype=uint64, description=Identifier for the annotation.),
        'point_coords': Tensor(shape=(1, 2), dtype=float64, description=The point coordinates input to the model to generate the mask.),
        'predicted_iou': Scalar(shape=(), dtype=float64, description=The model's own prediction of the mask's quality.),
        'segmentation': FeaturesDict({
            'counts': string,
            'size': Tensor(shape=(2,), dtype=uint64),
        }),
        'stability_score': Scalar(shape=(), dtype=float64, description=A measure of the mask's quality.),
    }),
    'image': FeaturesDict({
        'content': Image(shape=(None, None, 3), dtype=uint8, description=Content of the image.),
        'file_name': string,
        'height': uint64,
        'image_id': uint64,
        'width': uint64,
    }),
})
```

*   **Feature documentation**:

Feature                         | Class        | Shape           | Dtype   | Description
:------------------------------ | :----------- | :-------------- | :------ | :----------
                                | FeaturesDict |                 |         |
annotations                     | Sequence     |                 |         |
annotations/area                | Scalar       |                 | uint64  | The area in pixels of the mask.
annotations/bbox                | BBoxFeature  | (4,)            | float32 | The box around the mask, in TFDS format.
annotations/crop_box            | BBoxFeature  | (4,)            | float32 | The crop of the image used to generate the mask, in TFDS format.
annotations/id                  | Scalar       |                 | uint64  | Identifier for the annotation.
annotations/point_coords        | Tensor       | (1, 2)          | float64 | The point coordinates input to the model to generate the mask.
annotations/predicted_iou       | Scalar       |                 | float64 | The model's own prediction of the mask's quality.
annotations/segmentation        | FeaturesDict |                 |         | Encoded segmentation mask in COCO RLE format (dict with keys `size` and `counts`).
annotations/segmentation/counts | Tensor       |                 | string  |
annotations/segmentation/size   | Tensor       | (2,)            | uint64  |
annotations/stability_score     | Scalar       |                 | float64 | A measure of the mask's quality.
image                           | FeaturesDict |                 |         |
image/content                   | Image        | (None, None, 3) | uint8   | Content of the image.
image/file_name                 | Tensor       |                 | string  |
image/height                    | Tensor       |                 | uint64  |
image/image_id                  | Tensor       |                 | uint64  |
image/width                     | Tensor       |                 | uint64  |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/segment_anything-1.0.0.html";
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
@misc{kirillov2023segment,
  title={Segment Anything},
  author={Alexander Kirillov and Eric Mintun and Nikhila Ravi and Hanzi Mao and Chloe Rolland and Laura Gustafson and Tete Xiao and Spencer Whitehead and Alexander C. Berg and Wan-Yen Lo and Piotr Dollár and Ross Girshick},
  year={2023},
  eprint={2304.02643},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```

