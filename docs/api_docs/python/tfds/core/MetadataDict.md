<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.MetadataDict" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.core.MetadataDict

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py">View
source</a>

## Class `MetadataDict`

A <a href="../../tfds/core/Metadata.md"><code>tfds.core.Metadata</code></a>
object that acts as a `dict`.

Inherits From: [`Metadata`](../../tfds/core/Metadata.md)

<!-- Placeholder for "Used in" -->

By default, the metadata will be serialized as JSON.

## Methods

<h3 id="load_metadata"><code>load_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py">View
source</a>

```python
load_metadata(data_dir)
```

Restore the metadata.

<h3 id="save_metadata"><code>save_metadata</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py">View
source</a>

```python
save_metadata(data_dir)
```

Save the metadata.
