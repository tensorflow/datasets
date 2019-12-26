<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.Metadata" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="load_metadata"/>
<meta itemprop="property" content="save_metadata"/>
</div>

# tfds.core.Metadata

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/dataset_info.py">View
source</a>

## Class `Metadata`

Abstract base class for DatasetInfo metadata container.

<!-- Placeholder for "Used in" -->

`builder.info.metadata` allows the dataset to expose additional general
information about the dataset which are not specific to a feature or individual
example.

To implement the interface, overwrite `save_metadata` and `load_metadata`.

See
<a href="../../tfds/core/MetadataDict.md"><code>tfds.core.MetadataDict</code></a>
for a simple implementation that acts as a dict that saves data to/from a JSON
file.

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
