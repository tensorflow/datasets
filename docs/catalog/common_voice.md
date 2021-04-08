<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="common_voice" />
  <meta itemprop="description" content="Mozilla Common Voice Dataset&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;common_voice&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/common_voice" />
  <meta itemprop="sameAs" content="https://voice.mozilla.org/en/datasets" />
  <meta itemprop="citation" content="" />
</div>

# `common_voice`

*   **Description**:

Mozilla Common Voice Dataset

*   **Homepage**:
    [https://voice.mozilla.org/en/datasets](https://voice.mozilla.org/en/datasets)

*   **Source code**:
    [`tfds.audio.CommonVoice`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/commonvoice.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

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

## common_voice/en (default config)

*   **Config description**: Language Code: en

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=17),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/de

*   **Config description**: Language Code: de

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/fr

*   **Config description**: Language Code: fr

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=19),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/cy

*   **Config description**: Language Code: cy

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/br

*   **Config description**: Language Code: br

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=1),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/cv

*   **Config description**: Language Code: cv

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=0),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/tr

*   **Config description**: Language Code: tr

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=1),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/tt

*   **Config description**: Language Code: tt

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=0),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/ky

*   **Config description**: Language Code: ky

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=1),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/ga-IE

*   **Config description**: Language Code: ga-IE

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/kab

*   **Config description**: Language Code: kab

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=1),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/ca

*   **Config description**: Language Code: ca

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=6),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/zh-TW

*   **Config description**: Language Code: zh-TW

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=1),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/sl

*   **Config description**: Language Code: sl

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=1),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/it

*   **Config description**: Language Code: it

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=1),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/nl

*   **Config description**: Language Code: nl

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/cnh

*   **Config description**: Language Code: cnh

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=1),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

## common_voice/eo

*   **Config description**: Language Code: eo

*   **Features**:

```python
FeaturesDict({
    'accent': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': tf.int32,
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': tf.int32,
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```
