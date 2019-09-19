<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="ted_hrlr_translate" />
  <meta itemprop="description" content="Data sets derived from TED talk transcripts for comparing similar language pairs&#10;where one is high resource and the other is low resource.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/ted_hrlr_translate" />
  <meta itemprop="sameAs" content="https://github.com/neulab/word-embeddings-for-nmt" />
</div>

# `ted_hrlr_translate`

Data sets derived from TED talk transcripts for comparing similar language pairs
where one is high resource and the other is low resource.

*   URL:
    [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)
*   `DatasetBuilder`:
    [`tfds.translate.ted_hrlr.TedHrlrTranslate`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/translate/ted_hrlr.py)

`ted_hrlr_translate` is configured with `tfds.translate.ted_hrlr.TedHrlrConfig`
and has the following configurations predefined (defaults to the first one):

*   `az_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from az to
    en in plain text.

*   `aztr_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from az_tr
    to en in plain text.

*   `be_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from be to
    en in plain text.

*   `beru_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from be_ru
    to en in plain text.

*   `es_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from es to
    pt in plain text.

*   `fr_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from fr to
    pt in plain text.

*   `gl_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from gl to
    en in plain text.

*   `glpt_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from gl_pt
    to en in plain text.

*   `he_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from he to
    pt in plain text.

*   `it_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from it to
    pt in plain text.

*   `pt_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from pt to
    en in plain text.

*   `ru_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from ru to
    en in plain text.

*   `ru_to_pt` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from ru to
    pt in plain text.

*   `tr_to_en` (`v0.0.1`) (`Size: 124.94 MiB`): Translation dataset from tr to
    en in plain text.

## `ted_hrlr_translate/az_to_en`

```python
Translation({
    'az': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/aztr_to_en`

```python
Translation({
    'az_tr': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/be_to_en`

```python
Translation({
    'be': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/beru_to_en`

```python
Translation({
    'be_ru': Text(shape=(), dtype=tf.string),
    'en': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/es_to_pt`

```python
Translation({
    'es': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/fr_to_pt`

```python
Translation({
    'fr': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/gl_to_en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'gl': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/glpt_to_en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'gl_pt': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/he_to_pt`

```python
Translation({
    'he': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/it_to_pt`

```python
Translation({
    'it': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/pt_to_en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'pt': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/ru_to_en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/ru_to_pt`

```python
Translation({
    'pt': Text(shape=(), dtype=tf.string),
    'ru': Text(shape=(), dtype=tf.string),
})
```

## `ted_hrlr_translate/tr_to_en`

```python
Translation({
    'en': Text(shape=(), dtype=tf.string),
    'tr': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 191,524
TRAIN      | 182,450
TEST       | 5,029
VALIDATION | 4,045

## Urls

*   [https://github.com/neulab/word-embeddings-for-nmt](https://github.com/neulab/word-embeddings-for-nmt)

## Supervised keys (for `as_supervised=True`)
`(u'tr', u'en')`

## Citation
```
@inproceedings{Ye2018WordEmbeddings,
  author  = {Ye, Qi and Devendra, Sachan and Matthieu, Felix and Sarguna, Padmanabhan and Graham, Neubig},
  title   = {When and Why are pre-trained word embeddings useful for Neural Machine Translation},
  booktitle = {HLT-NAACL},
  year    = {2018},
  }
```

--------------------------------------------------------------------------------
