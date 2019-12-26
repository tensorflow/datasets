<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.Version" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="tuple"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__ge__"/>
<meta itemprop="property" content="__gt__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__le__"/>
<meta itemprop="property" content="__lt__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="implements"/>
<meta itemprop="property" content="match"/>
</div>

# tfds.core.Version

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

## Class `Version`

Dataset version MAJOR.MINOR.PATCH.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

```python
__init__(
    version_str,
    description=None,
    experiments=None,
    tfds_version_to_prepare=None
)
```

Version init.

#### Args:

*   <b>`version_str`</b>: string. Eg: "1.2.3".
*   <b>`description`</b>: string, a description of what is new in this version.
*   <b>`experiments`</b>: dict of experiments. See Experiment.
*   <b>`tfds_version_to_prepare`</b>: string, defaults to None. If set,
    indicates that current version of TFDS cannot be used to
    `download_and_prepare` the dataset, but that TFDS at version
    {tfds_version_to_prepare} should be used instead.

## Properties

<h3 id="tuple"><code>tuple</code></h3>

## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

```python
__eq__(other)
```

<h3 id="__ge__"><code>__ge__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

```python
__ge__(other)
```

<h3 id="__gt__"><code>__gt__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

```python
__gt__(other)
```

<h3 id="__le__"><code>__le__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

```python
__le__(other)
```

<h3 id="__lt__"><code>__lt__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

```python
__lt__(other)
```

<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

```python
__ne__(other)
```

<h3 id="implements"><code>implements</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

```python
implements(experiment)
```

Returns True if version implements given experiment.

<h3 id="match"><code>match</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

```python
match(other_version)
```

Returns True if other_version matches.

#### Args:

*   <b>`other_version`</b>: string, of the form "x[.y[.x]]" where {x,y,z} can be
    a number or a wildcard.
