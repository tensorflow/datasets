<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="deep_weeds" />
  <meta itemprop="description" content="The DeepWeeds dataset consists of 17,509 images capturing eight different weed species native to Australia in situ with neighbouring flora.The selected weed species are local to pastoral grasslands across the state of Queensland.The images were collected from weed infestations at the following sites across Queensland: &quot;Black River&quot;, &quot;Charters Towers&quot;,  &quot;Cluden&quot;, &quot;Douglas&quot;, &quot;Hervey Range&quot;, &quot;Kelso&quot;, &quot;McKinlay&quot; and &quot;Paluma&quot;." />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/deep_weeds" />
  <meta itemprop="sameAs" content="https://nextcloud.qriscloud.org.au/index.php/s/a3KxPawpqkiorST/download" />
</div>

# `deep_weeds`

The DeepWeeds dataset consists of 17,509 images capturing eight different weed
species native to Australia in situ with neighbouring flora.The selected weed
species are local to pastoral grasslands across the state of Queensland.The
images were collected from weed infestations at the following sites across
Queensland: "Black River", "Charters Towers", "Cluden", "Douglas", "Hervey
Range", "Kelso", "McKinlay" and "Paluma".

*   URL:
    [https://nextcloud.qriscloud.org.au/index.php/s/a3KxPawpqkiorST/download](https://nextcloud.qriscloud.org.au/index.php/s/a3KxPawpqkiorST/download)
*   `DatasetBuilder`:
    [`tfds.image.deep_weeds.DeepWeeds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/deep_weeds.py)
*   Version: `v1.0.0`
*   Size: `891.95 MiB`

## Features
```python
FeaturesDict({
    'image': Image(shape=(256, 256, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=9),
})
```

## Statistics

Split | Examples
:---- | -------:
ALL   | 17,509
TRAIN | 17,509

## Urls

*   [https://nextcloud.qriscloud.org.au/index.php/s/a3KxPawpqkiorST/download](https://nextcloud.qriscloud.org.au/index.php/s/a3KxPawpqkiorST/download)

## Supervised keys (for `as_supervised=True`)
`(u'image', u'label')`

## Citation
```
@article{DeepWeeds2019,
  author = {Alex Olsen and
    Dmitry A. Konovalov and
    Bronson Philippa and
    Peter Ridd and
    Jake C. Wood and
    Jamie Johns and
    Wesley Banks and
    Benjamin Girgenti and
    Owen Kenny and
    James Whinney and
    Brendan Calvert and
    Mostafa {Rahimi Azghadi} and
    Ronald D. White},
  title = {{DeepWeeds: A Multiclass Weed Species Image Dataset for Deep Learning}},
  journal = {Scientific Reports},
  year = 2019,
  number = 2058,
  month = 2,
  volume = 9,
  issue = 1,
  day = 14,
  url = "https://doi.org/10.1038/s41598-018-38343-3",
  doi = "10.1038/s41598-018-38343-3"
}
```

--------------------------------------------------------------------------------
