<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="wider_face" />
  <meta itemprop="description" content="&#10;WIDER FACE dataset is a face detection benchmark dataset, of which images are &#10;selected from the publicly available WIDER dataset. We choose 32,203 images and &#10;label 393,703 faces with a high degree of variability in scale, pose and &#10;occlusion as depicted in the sample images. WIDER FACE dataset is organized &#10;based on 61 event classes. For each event class, we randomly select 40%/10%/50% &#10;data as training, validation and testing sets. We adopt the same evaluation &#10;metric employed in the PASCAL VOC dataset. Similar to MALF and Caltech datasets,&#10;we do not release bounding box ground truth for the test images. Users are &#10;required to submit final prediction files, which we shall proceed to evaluate.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('wider_face', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/wider_face" />
  <meta itemprop="sameAs" content="http://shuoyang1213.me/WIDERFACE/" />
  <meta itemprop="citation" content="&#10;@inproceedings{yang2016wider,&#10;    Author = {Yang, Shuo and Luo, Ping and Loy, Chen Change and Tang, Xiaoou},&#10; Booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},&#10;   Title = {WIDER FACE: A Face Detection Benchmark},&#10;  Year = {2016}}&#10;" />
</div>

# `wider_face`

WIDER FACE dataset is a face detection benchmark dataset, of which images are
selected from the publicly available WIDER dataset. We choose 32,203 images and
label 393,703 faces with a high degree of variability in scale, pose and
occlusion as depicted in the sample images. WIDER FACE dataset is organized
based on 61 event classes. For each event class, we randomly select 40%/10%/50%
data as training, validation and testing sets. We adopt the same evaluation
metric employed in the PASCAL VOC dataset. Similar to MALF and Caltech datasets,
we do not release bounding box ground truth for the test images. Users are
required to submit final prediction files, which we shall proceed to evaluate.

*   URL: [http://shuoyang1213.me/WIDERFACE/](http://shuoyang1213.me/WIDERFACE/)
*   `DatasetBuilder`:
    [`tfds.image.wider_face.WiderFace`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/object_detection/wider_face.py)
*   Version: `v0.1.0`
*   Versions:

    *   **`0.1.0`** (default):

*   Size: `3.42 GiB`

## Features
```python
FeaturesDict({
    'faces': Sequence({
        'bbox': BBoxFeature(shape=(4,), dtype=tf.float32),
        'blur': Tensor(shape=(), dtype=tf.uint8),
        'expression': Tensor(shape=(), dtype=tf.bool),
        'illumination': Tensor(shape=(), dtype=tf.bool),
        'invalid': Tensor(shape=(), dtype=tf.bool),
        'occlusion': Tensor(shape=(), dtype=tf.uint8),
        'pose': Tensor(shape=(), dtype=tf.bool),
    }),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image/filename': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 32,203
TEST       | 16,097
TRAIN      | 12,880
VALIDATION | 3,226

## Urls

*   [http://shuoyang1213.me/WIDERFACE/](http://shuoyang1213.me/WIDERFACE/)

## Citation

```
@inproceedings{yang2016wider,
    Author = {Yang, Shuo and Luo, Ping and Loy, Chen Change and Tang, Xiaoou},
    Booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    Title = {WIDER FACE: A Face Detection Benchmark},
    Year = {2016}}
```

--------------------------------------------------------------------------------
