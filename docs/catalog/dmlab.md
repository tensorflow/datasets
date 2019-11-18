<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dmlab" />
  <meta itemprop="description" content="&#10;        The Dmlab dataset contains frames observed by the agent acting in the&#10;        DeepMind Lab environment, which are annotated by the distance between&#10;        the agent and various objects present in the environment. The goal is to&#10;        is to evaluate the ability of a visual model to reason about distances&#10;        from the visual input in 3D environments. The Dmlab dataset consists of&#10;        360x480 color images in 6 classes. The classes are&#10;        {close, far, very far} x {positive reward, negative reward}&#10;        respectively.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('dmlab', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dmlab" />
  <meta itemprop="sameAs" content="https://github.com/google-research/task_adaptation" />
  <meta itemprop="citation" content="@article{zhai2019visual,&#10;        title={The Visual Task Adaptation Benchmark},&#10;        author={Xiaohua Zhai and Joan Puigcerver and Alexander Kolesnikov and&#10;               Pierre Ruyssen and Carlos Riquelme and Mario Lucic and&#10;               Josip Djolonga and Andre Susano Pinto and Maxim Neumann and&#10;               Alexey Dosovitskiy and Lucas Beyer and Olivier Bachem and&#10;               Michael Tschannen and Marcin Michalski and Olivier Bousquet and&#10;               Sylvain Gelly and Neil Houlsby},&#10;                              year={2019},&#10;                              eprint={1910.04867},&#10;                              archivePrefix={arXiv},&#10;                              primaryClass={cs.CV},&#10;                              url = {https://arxiv.org/abs/1910.04867}&#10;                          }" />
</div>
# `dmlab`

The Dmlab dataset contains frames observed by the agent acting in the DeepMind
Lab environment, which are annotated by the distance between the agent and
various objects present in the environment. The goal is to is to evaluate the
ability of a visual model to reason about distances from the visual input in 3D
environments. The Dmlab dataset consists of 360x480 color images in 6 classes.
The classes are {close, far, very far} x {positive reward, negative reward}
respectively.

*   URL:
    [https://github.com/google-research/task_adaptation](https://github.com/google-research/task_adaptation)
*   `DatasetBuilder`:
    [`tfds.image.dmlab.Dmlab`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/dmlab.py)
*   Version: `v2.0.0`
*   Versions:

    *   **`2.0.0`** (default):

*   Size: `2.81 GiB`

## Features
```python
FeaturesDict({
    'filename': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(360, 480, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 110,913
TRAIN      | 65,550
TEST       | 22,735
VALIDATION | 22,628

## Homepage

*   [https://github.com/google-research/task_adaptation](https://github.com/google-research/task_adaptation)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{zhai2019visual,
        title={The Visual Task Adaptation Benchmark},
        author={Xiaohua Zhai and Joan Puigcerver and Alexander Kolesnikov and
               Pierre Ruyssen and Carlos Riquelme and Mario Lucic and
               Josip Djolonga and Andre Susano Pinto and Maxim Neumann and
               Alexey Dosovitskiy and Lucas Beyer and Olivier Bachem and
               Michael Tschannen and Marcin Michalski and Olivier Bousquet and
               Sylvain Gelly and Neil Houlsby},
                              year={2019},
                              eprint={1910.04867},
                              archivePrefix={arXiv},
                              primaryClass={cs.CV},
                              url = {https://arxiv.org/abs/1910.04867}
                          }
```

--------------------------------------------------------------------------------
