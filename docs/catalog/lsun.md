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

*   **Download size**: `3.06 GiB`

*   **Dataset size**: `3.15 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 168,103
`'validation'` | 300

## lsun/bedroom

*   **Config description**: Images of category bedroom

*   **Download size**: `42.77 GiB`

*   **Dataset size**: `44.48 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'train'`      | 3,033,042
`'validation'` | 300

## lsun/bridge

*   **Config description**: Images of category bridge

*   **Download size**: `15.35 GiB`

*   **Dataset size**: `15.80 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 818,687
`'validation'` | 300

## lsun/church_outdoor

*   **Config description**: Images of category church_outdoor

*   **Download size**: `2.29 GiB`

*   **Dataset size**: `2.36 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 126,227
`'validation'` | 300

## lsun/conference_room

*   **Config description**: Images of category conference_room

*   **Download size**: `3.78 GiB`

*   **Dataset size**: `3.90 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 229,069
`'validation'` | 300

## lsun/dining_room

*   **Config description**: Images of category dining_room

*   **Download size**: `10.80 GiB`

*   **Dataset size**: `11.17 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 657,571
`'validation'` | 300

## lsun/kitchen

*   **Config description**: Images of category kitchen

*   **Download size**: `33.34 GiB`

*   **Dataset size**: `34.61 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'train'`      | 2,212,277
`'validation'` | 300

## lsun/living_room

*   **Config description**: Images of category living_room

*   **Download size**: `21.23 GiB`

*   **Dataset size**: `21.97 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'train'`      | 1,315,802
`'validation'` | 300

## lsun/restaurant

*   **Config description**: Images of category restaurant

*   **Download size**: `12.57 GiB`

*   **Dataset size**: `12.88 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 626,331
`'validation'` | 300

## lsun/tower

*   **Config description**: Images of category tower

*   **Download size**: `11.19 GiB`

*   **Dataset size**: `11.61 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train'`      | 708,264
`'validation'` | 300

## lsun/airplane

*   **Config description**: Images of category airplane

*   **Download size**: `33.72 GiB`

*   **Dataset size**: `29.96 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,530,696

## lsun/bicycle

*   **Config description**: Images of category bicycle

*   **Download size**: `129.24 GiB`

*   **Dataset size**: `119.72 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,347,211

## lsun/bird

*   **Config description**: Images of category bird

*   **Download size**: `65.10 GiB`

*   **Dataset size**: `59.78 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,310,362

## lsun/boat

*   **Config description**: Images of category boat

*   **Download size**: `85.66 GiB`

*   **Dataset size**: `79.61 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,651,165

## lsun/bottle

*   **Config description**: Images of category bottle

*   **Download size**: `63.66 GiB`

*   **Dataset size**: `56.79 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 3,202,760

## lsun/bus

*   **Config description**: Images of category bus

*   **Download size**: `24.33 GiB`

*   **Dataset size**: `21.93 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 695,891

## lsun/car

*   **Config description**: Images of category car

*   **Download size**: `173.03 GiB`

*   **Dataset size**: `159.63 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,520,756

## lsun/cat

*   **Config description**: Images of category cat

*   **Download size**: `41.69 GiB`

*   **Dataset size**: `36.38 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,657,266

## lsun/chair

*   **Config description**: Images of category chair

*   **Download size**: `115.79 GiB`

*   **Dataset size**: `105.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,037,807

## lsun/cow

*   **Config description**: Images of category cow

*   **Download size**: `14.94 GiB`

*   **Dataset size**: `13.22 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 377,379

## lsun/dining_table

*   **Config description**: Images of category dining_table

*   **Download size**: `48.27 GiB`

*   **Dataset size**: `44.20 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,537,123

## lsun/dog

*   **Config description**: Images of category dog

*   **Download size**: `144.92 GiB`

*   **Dataset size**: `133.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 5,054,817

## lsun/horse

*   **Config description**: Images of category horse

*   **Download size**: `68.79 GiB`

*   **Dataset size**: `63.99 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,000,340

## lsun/motorbike

*   **Config description**: Images of category motorbike

*   **Download size**: `41.86 GiB`

*   **Dataset size**: `38.65 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,194,101

## lsun/potted_plant

*   **Config description**: Images of category potted_plant

*   **Download size**: `42.70 GiB`

*   **Dataset size**: `39.71 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 1,104,859

## lsun/sheep

*   **Config description**: Images of category sheep

*   **Download size**: `17.75 GiB`

*   **Dataset size**: `15.88 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 418,983

## lsun/sofa

*   **Config description**: Images of category sofa

*   **Download size**: `56.33 GiB`

*   **Dataset size**: `50.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | --------:
`'train'` | 2,365,870

## lsun/train

*   **Config description**: Images of category train

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## lsun/tv-monitor

*   **Config description**: Images of category tv-monitor

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:
