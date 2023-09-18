<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cycle_gan" />
  <meta itemprop="description" content="A dataset consisting of images from two classes A and B (For example: horses/zebras, apple/orange,...)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cycle_gan&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cycle_gan" />
  <meta itemprop="sameAs" content="https://junyanz.github.io/CycleGAN/" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/ZhuPIE17,&#10;  author    = {Jun{-}Yan Zhu and&#10;               Taesung Park and&#10;               Phillip Isola and&#10;               Alexei A. Efros},&#10;  title     = {Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial&#10;               Networks},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1703.10593},&#10;  year      = {2017},&#10;  url       = {http://arxiv.org/abs/1703.10593},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1703.10593},&#10;  timestamp = {Mon, 13 Aug 2018 16:48:06 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhuPIE17},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `cycle_gan`


Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=cycle_gan">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

A dataset consisting of images from two classes A and B (For example:
horses/zebras, apple/orange,...)

*   **Homepage**:
    [https://junyanz.github.io/CycleGAN/](https://junyanz.github.io/CycleGAN/)

*   **Source code**:
    [`tfds.image_classification.CycleGAN`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/cycle_gan.py)

*   **Versions**:

    *   **`3.0.0`** (default)
        <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>:
        Cityscapes dataset is removed due to license issue.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
})
```

*   **Feature documentation**:

Feature | Class        | Shape           | Dtype | Description
:------ | :----------- | :-------------- | :---- | :----------
        | FeaturesDict |                 |       |
image   | Image        | (None, None, 3) | uint8 |
label   | ClassLabel   |                 | int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{DBLP:journals/corr/ZhuPIE17,
  author    = {Jun{-}Yan Zhu and
               Taesung Park and
               Phillip Isola and
               Alexei A. Efros},
  title     = {Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial
               Networks},
  journal   = {CoRR},
  volume    = {abs/1703.10593},
  year      = {2017},
  url       = {http://arxiv.org/abs/1703.10593},
  archivePrefix = {arXiv},
  eprint    = {1703.10593},
  timestamp = {Mon, 13 Aug 2018 16:48:06 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhuPIE17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


## cycle_gan/apple2orange (default config)

## cycle_gan/summer2winter_yosemite

## cycle_gan/horse2zebra

## cycle_gan/monet2photo

## cycle_gan/cezanne2photo

## cycle_gan/ukiyoe2photo

## cycle_gan/vangogh2photo

## cycle_gan/maps

## cycle_gan/facades

## cycle_gan/iphone2dslr_flower
