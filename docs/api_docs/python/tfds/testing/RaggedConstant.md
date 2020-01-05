<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.testing.RaggedConstant" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="build"/>
</div>

# tfds.testing.RaggedConstant

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/test_utils.py">View
source</a>

## Class `RaggedConstant`

Container of tf.ragged.constant values.

<!-- Placeholder for "Used in" -->

This simple wrapper forward the arguments to delay the RaggedTensor construction
after `@run_in_graph_and_eager_modes` has been called. This is required to avoid
incompabilities between Graph/eager.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/test_utils.py">View
source</a>

```python
__init__(
    *args,
    **kwargs
)
```

## Methods

<h3 id="build"><code>build</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/test_utils.py">View
source</a>

```python
build()
```
