<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="percent"/>
</div>

# Module: tfds



Defined in [`__init__.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/__init__.py).

`tensorflow_datasets` (<a href="./tfds.md"><code>tfds</code></a>) defines a collection of datasets ready-to-use with TensorFlow.

Each dataset is defined as a <a href="./tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a>.

See <a href="./tfds/builder.md"><code>tfds.builder</code></a>, <a href="./tfds/list_builders.md"><code>tfds.list_builders</code></a>, and <a href="./tfds/load.md"><code>tfds.load</code></a> for the main
entrypoints into the library, or take a look at
[our dataset documentation](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md).

## Modules

[`core`](./tfds/core.md) module: tensorflow_datasets.core.

[`download`](./tfds/download.md) module: Public API of the download manager.

[`features`](./tfds/features.md) module: Public tfds.features API.

[`file_adapter`](./tfds/file_adapter.md) module: FileFormatAdapters for GeneratorBasedBuilder.

[`units`](./tfds/units.md) module: Defines convenience constants/functions for converting various units.

## Classes

[`class GenerateMode`](./tfds/download/GenerateMode.md): Enum for the different version conflict resolution modes.

[`class Split`](./tfds/Split.md): `Enum` for dataset splits.

## Functions

[`builder(...)`](./tfds/builder.md): Fetches a <a href="./tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a> by string name.

[`list_builders(...)`](./tfds/list_builders.md): Returns the string names of all <a href="./tfds/core/DatasetBuilder.md"><code>tfds.core.DatasetBuilder</code></a>s.

[`load(...)`](./tfds/load.md): Loads the given <a href="./tfds/Split.md"><code>tfds.Split</code></a> as a `tf.data.Dataset`.

## Other Members

<h3 id="percent"><code>percent</code></h3>

