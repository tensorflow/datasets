<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__all__"/>
</div>

# Module: tfds

`tensorflow_datasets` package.

`tensorflow_datasets` (<a href="./tfds.md"><code>tfds</code></a>) defines a collection of datasets ready-to-use
with TensorFlow.

Each dataset is defined as a <a href="./tfds/DatasetBuilder.md"><code>tfds.DatasetBuilder</code></a>.

## Modules

[`download`](./tfds/download.md) module: Public API of the download manager.

## Classes

[`class DatasetBuilder`](./tfds/DatasetBuilder.md): Abstract base class for datasets.

[`class GenerateMode`](./tfds/download/GenerateMode.md): Enum for the different version conflict resolution modes.

[`class Split`](./tfds/Split.md): `Enum` for dataset splits.

## Functions

[`builder(...)`](./tfds/builder.md): Fetches a <a href="./tfds/DatasetBuilder.md"><code>tfds.DatasetBuilder</code></a> by string name.

[`list_builders(...)`](./tfds/list_builders.md): Returns the string names of all <a href="./tfds/DatasetBuilder.md"><code>tfds.DatasetBuilder</code></a>s.

[`load(...)`](./tfds/load.md): Loads the given <a href="./tfds/Split.md"><code>tfds.Split</code></a> as a `tf.data.Dataset`.

## Other Members

<h3 id="__all__"><code>__all__</code></h3>

