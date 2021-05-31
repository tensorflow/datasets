<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="lsun" />
  <meta itemprop="description" content="Large scale images showing different objects from given categories like bedroom, tower etc.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;lsun&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/lsun" />
  <meta itemprop="sameAs" content="https://www.yf.io/p/lsun" />
  <meta itemprop="citation" content="@article{journals/corr/YuZSSX15,&#10;  added-at = {2018-08-13T00:00:00.000+0200},&#10;  author = {Yu, Fisher and Zhang, Yinda and Song, Shuran and Seff, Ari and Xiao, Jianxiong},&#10;  biburl = {https://www.bibsonomy.org/bibtex/2446d4ffb99a5d7d2ab6e5417a12e195f/dblp},&#10;  ee = {http://arxiv.org/abs/1506.03365},&#10;  interhash = {3e9306c4ce2ead125f3b2ab0e25adc85},&#10;  intrahash = {446d4ffb99a5d7d2ab6e5417a12e195f},&#10;  journal = {CoRR},&#10;  keywords = {dblp},&#10;  timestamp = {2018-08-14T15:08:59.000+0200},&#10;  title = {LSUN: Construction of a Large-scale Image Dataset using Deep Learning with Humans in the Loop.},&#10;  url = {http://dblp.uni-trier.de/db/journals/corr/corr1506.html#YuZSSX15},&#10;  volume = {abs/1506.03365},&#10;  year = 2015&#10;}" />
</div>

# `lsun`

Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

*   **Description**:

Large scale images showing different objects from given categories like bedroom,
tower etc.

*   **Homepage**: [https://www.yf.io/p/lsun](https://www.yf.io/p/lsun)

*   **Source code**:
    [`tfds.image.Lsun`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/lsun.py)

*   **Versions**:

    *   `3.0.0`: New split API (https://tensorflow.org/datasets/splits)
    *   **`3.1.0`** (default)
        <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>:
        Add builder config for missing `person` object category, and add `id` to
        the feature dict

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Features**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{journals/corr/YuZSSX15,
  added-at = {2018-08-13T00:00:00.000+0200},
  author = {Yu, Fisher and Zhang, Yinda and Song, Shuran and Seff, Ari and Xiao, Jianxiong},
  biburl = {https://www.bibsonomy.org/bibtex/2446d4ffb99a5d7d2ab6e5417a12e195f/dblp},
  ee = {http://arxiv.org/abs/1506.03365},
  interhash = {3e9306c4ce2ead125f3b2ab0e25adc85},
  intrahash = {446d4ffb99a5d7d2ab6e5417a12e195f},
  journal = {CoRR},
  keywords = {dblp},
  timestamp = {2018-08-14T15:08:59.000+0200},
  title = {LSUN: Construction of a Large-scale Image Dataset using Deep Learning with Humans in the Loop.},
  url = {http://dblp.uni-trier.de/db/journals/corr/corr1506.html#YuZSSX15},
  volume = {abs/1506.03365},
  year = 2015
}
```

## lsun/classroom (default config)

*   **Config description**: Images of category classroom

## lsun/bedroom

*   **Config description**: Images of category bedroom

## lsun/bridge

*   **Config description**: Images of category bridge

## lsun/church_outdoor

*   **Config description**: Images of category church_outdoor

## lsun/conference_room

*   **Config description**: Images of category conference_room

## lsun/dining_room

*   **Config description**: Images of category dining_room

## lsun/kitchen

*   **Config description**: Images of category kitchen

## lsun/living_room

*   **Config description**: Images of category living_room

## lsun/restaurant

*   **Config description**: Images of category restaurant

## lsun/tower

*   **Config description**: Images of category tower

## lsun/airplane

*   **Config description**: Images of category airplane

## lsun/bicycle

*   **Config description**: Images of category bicycle

## lsun/bird

*   **Config description**: Images of category bird

## lsun/boat

*   **Config description**: Images of category boat

## lsun/bottle

*   **Config description**: Images of category bottle

## lsun/bus

*   **Config description**: Images of category bus

## lsun/car

*   **Config description**: Images of category car

## lsun/cat

*   **Config description**: Images of category cat

## lsun/chair

*   **Config description**: Images of category chair

## lsun/cow

*   **Config description**: Images of category cow

## lsun/dining_table

*   **Config description**: Images of category dining_table

## lsun/dog

*   **Config description**: Images of category dog

## lsun/horse

*   **Config description**: Images of category horse

## lsun/motorbike

*   **Config description**: Images of category motorbike

## lsun/person <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Images of category person

## lsun/potted_plant

*   **Config description**: Images of category potted_plant

## lsun/sheep

*   **Config description**: Images of category sheep

## lsun/sofa

*   **Config description**: Images of category sofa

## lsun/train

*   **Config description**: Images of category train

## lsun/tv-monitor

*   **Config description**: Images of category tv-monitor
