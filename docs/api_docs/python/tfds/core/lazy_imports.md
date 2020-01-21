<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.lazy_imports" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.core.lazy_imports

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/lazy_imports_lib.py">View
source</a>

## Class `lazy_imports`

Lazy importer for heavy dependencies.

<!-- Placeholder for "Used in" -->

Some datasets require heavy dependencies for data generation. To allow for
the default installation to remain lean, those heavy dependencies are
lazily imported here.
