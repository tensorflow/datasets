<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.BeamMetadataDict" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.core.BeamMetadataDict

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py">View
source</a>

## Class `BeamMetadataDict`

A <a href="../../tfds/core/Metadata.md"><code>tfds.core.Metadata</code></a>
object supporting Beam-generated datasets.

Inherits From: [`MetadataDict`](../../tfds/core/MetadataDict.md)

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py">View
source</a>

```python
__init__()
```

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

Save the metadata inside the beam job.
