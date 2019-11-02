<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="moving_mnist" />
  <meta itemprop="description" content="Moving variant of MNIST database of handwritten digits. This is the&#10;data used by the authors for reporting model performance. See&#10;`tfds.video.moving_mnist.image_as_moving_sequence`&#10;for generating training/validation data from the MNIST dataset.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('moving_mnist', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/moving_mnist" />
  <meta itemprop="sameAs" content="http://www.cs.toronto.edu/~nitish/unsupervised_video/" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/SrivastavaMS15,&#10;  author    = {Nitish Srivastava and&#10;               Elman Mansimov and&#10;               Ruslan Salakhutdinov},&#10;  title     = {Unsupervised Learning of Video Representations using LSTMs},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1502.04681},&#10;  year      = {2015},&#10;  url       = {http://arxiv.org/abs/1502.04681},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1502.04681},&#10;  timestamp = {Mon, 13 Aug 2018 16:47:05 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/SrivastavaMS15},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}&#10;" />
</div>
# `moving_mnist`

Moving variant of MNIST database of handwritten digits. This is the data used by
the authors for reporting model performance. See
`tfds.video.moving_mnist.image_as_moving_sequence` for generating
training/validation data from the MNIST dataset.

*   URL:
    [http://www.cs.toronto.edu/~nitish/unsupervised_video/](http://www.cs.toronto.edu/~nitish/unsupervised_video/)
*   `DatasetBuilder`:
    [`tfds.video.moving_mnist.MovingMnist`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/video/moving_mnist.py)
*   Version: `v0.1.0`
*   Versions:

    *   **`0.1.0`** (default):

*   Size: `781.25 MiB`

## Features
```python
FeaturesDict({
    'image_sequence': Video(Image(shape=(64, 64, 1), dtype=tf.uint8)),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 10,000
TEST  | 10,000

## Homepage

*   [http://www.cs.toronto.edu/~nitish/unsupervised_video/](http://www.cs.toronto.edu/~nitish/unsupervised_video/)

## Citation
```
@article{DBLP:journals/corr/SrivastavaMS15,
  author    = {Nitish Srivastava and
               Elman Mansimov and
               Ruslan Salakhutdinov},
  title     = {Unsupervised Learning of Video Representations using LSTMs},
  journal   = {CoRR},
  volume    = {abs/1502.04681},
  year      = {2015},
  url       = {http://arxiv.org/abs/1502.04681},
  archivePrefix = {arXiv},
  eprint    = {1502.04681},
  timestamp = {Mon, 13 Aug 2018 16:47:05 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/SrivastavaMS15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

--------------------------------------------------------------------------------
