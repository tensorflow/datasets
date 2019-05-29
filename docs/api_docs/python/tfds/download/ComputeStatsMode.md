<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.ComputeStatsMode" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="AUTO"/>
<meta itemprop="property" content="FORCE"/>
<meta itemprop="property" content="SKIP"/>
<meta itemprop="property" content="__members__"/>
</div>

# tfds.download.ComputeStatsMode

## Class `ComputeStatsMode`

Mode to decide if dynamic dataset info fields should be computed or not.

Defined in [`core/download/util.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/util.py).

<!-- Placeholder for "Used in" -->

#### Mode can be:

* AUTO: Compute the DatasetInfo dynamic fields only if they haven't been
  restored from GCS.
* FORCE: Always recompute DatasetInfo dynamic  fields, even if they are
  already present
* SKIP: Ignore the dataset dynamic field computation (whether they already
  exist or not)

## Class Members

<h3 id="AUTO"><code>AUTO</code></h3>

<h3 id="FORCE"><code>FORCE</code></h3>

<h3 id="SKIP"><code>SKIP</code></h3>

<h3 id="__members__"><code>__members__</code></h3>

