<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet2012" />
  <meta itemprop="description" content="ILSVRC 2012, aka ImageNet is an image dataset organized according to the&#10;WordNet hierarchy. Each meaningful concept in WordNet, possibly described by&#10;multiple words or word phrases, is called a &quot;synonym set&quot; or &quot;synset&quot;. There are&#10;more than 100,000 synsets in WordNet, majority of them are nouns (80,000+). In&#10;ImageNet, we aim to provide on average 1000 images to illustrate each synset.&#10;Images of each concept are quality-controlled and human-annotated. In its&#10;completion, we hope ImageNet will offer tens of millions of cleanly sorted&#10;images for most of the concepts in the WordNet hierarchy.&#10;&#10;Note that labels were never publicly released for the test set, so we only&#10;include splits for the training and validation sets here.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet2012" />
  <meta itemprop="sameAs" content="http://image-net.org/" />
</div>

# `imagenet2012`

ILSVRC 2012, aka ImageNet is an image dataset organized according to the WordNet
hierarchy. Each meaningful concept in WordNet, possibly described by multiple
words or word phrases, is called a "synonym set" or "synset". There are more
than 100,000 synsets in WordNet, majority of them are nouns (80,000+). In
ImageNet, we aim to provide on average 1000 images to illustrate each synset.
Images of each concept are quality-controlled and human-annotated. In its
completion, we hope ImageNet will offer tens of millions of cleanly sorted
images for most of the concepts in the WordNet hierarchy.

Note that labels were never publicly released for the test set, so we only
include splits for the training and validation sets here.

*   URL: [http://image-net.org/](http://image-net.org/)
*   `DatasetBuilder`:
    [`tfds.image.imagenet.Imagenet2012`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/imagenet.py)
*   Version: `v2.0.1`
*   Size: `?? GiB`

## Features
```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

## Statistics

Split      | Examples
:--------- | --------:
ALL        | 1,331,167
TRAIN      | 1,281,167
VALIDATION | 50,000

## Urls

*   [http://image-net.org/](http://image-net.org/)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{ILSVRC15,
Author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},
Title = {{ImageNet Large Scale Visual Recognition Challenge}},
Year = {2015},
journal   = {International Journal of Computer Vision (IJCV)},
doi = {10.1007/s11263-015-0816-y},
volume={115},
number={3},
pages={211-252}
}
```

--------------------------------------------------------------------------------
