<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.download.ComputeStatsMode" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="AUTO"/>
<meta itemprop="property" content="FORCE"/>
<meta itemprop="property" content="SKIP"/>
</div>

# tfds.download.ComputeStatsMode

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/download/util.py">View
source</a>

## Class `ComputeStatsMode`

Mode to decide if dynamic dataset info fields should be computed or not.

<!-- Placeholder for "Used in" -->

#### Mode can be:

* AUTO: Compute the DatasetInfo dynamic fields only if they haven't been
  restored from GCS.
* FORCE: Always recompute DatasetInfo dynamic  fields, even if they are
  already present
* SKIP: Ignore the dataset dynamic field computation (whether they already
  exist or not)

## Class Members

*   `AUTO` <a id="AUTO"></a>
*   `FORCE` <a id="FORCE"></a>
*   `SKIP` <a id="SKIP"></a>
