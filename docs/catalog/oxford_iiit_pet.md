<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="oxford_iiit_pet" />
  <meta itemprop="description" content="The Oxford-IIIT pet dataset is a 37 category pet image dataset with roughly 200&#10;images for each class. The images have large variations in scale, pose and&#10;lighting. All images have an associated ground truth annotation of breed.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('oxford_iiit_pet', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/oxford_iiit_pet" />
  <meta itemprop="sameAs" content="http://www.robots.ox.ac.uk/~vgg/data/pets/" />
  <meta itemprop="citation" content="@InProceedings{parkhi12a,&#10;  author       = &quot;Parkhi, O. M. and Vedaldi, A. and Zisserman, A. and Jawahar, C.~V.&quot;,&#10;  title        = &quot;Cats and Dogs&quot;,&#10;  booktitle    = &quot;IEEE Conference on Computer Vision and Pattern Recognition&quot;,&#10;  year         = &quot;2012&quot;,&#10;}&#10;" />
</div>
# `oxford_iiit_pet`

The Oxford-IIIT pet dataset is a 37 category pet image dataset with roughly 200
images for each class. The images have large variations in scale, pose and
lighting. All images have an associated ground truth annotation of breed.

*   URL:
    [http://www.robots.ox.ac.uk/~vgg/data/pets/](http://www.robots.ox.ac.uk/~vgg/data/pets/)
*   `DatasetBuilder`:
    [`tfds.image.oxford_iiit_pet.OxfordIIITPet`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/oxford_iiit_pet.py)
*   Version: `v1.2.0`
*   Versions:

    *   **`1.2.0`** (default):
    *   `3.1.0`: Added species and labels.

*   Size: `?? GiB`

## Features
```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=37),
    'segmentation_mask': Image(shape=(None, None, 1), dtype=tf.uint8),
    'species': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
})
```

## Statistics
None computed

## Homepage

*   [http://www.robots.ox.ac.uk/~vgg/data/pets/](http://www.robots.ox.ac.uk/~vgg/data/pets/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@InProceedings{parkhi12a,
  author       = "Parkhi, O. M. and Vedaldi, A. and Zisserman, A. and Jawahar, C.~V.",
  title        = "Cats and Dogs",
  booktitle    = "IEEE Conference on Computer Vision and Pattern Recognition",
  year         = "2012",
}
```

--------------------------------------------------------------------------------
