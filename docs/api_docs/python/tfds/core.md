<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tfds.core

API to define datasets.

Defined in [`core/__init__.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/__init__.py).

<!-- Placeholder for "Used in" -->


## Classes

[`class BeamBasedBuilder`](../tfds/core/BeamBasedBuilder.md): Beam based Builder.

[`class BuilderConfig`](../tfds/core/BuilderConfig.md): Base class for `DatasetBuilder` data configuration.

[`class DatasetBuilder`](../tfds/core/DatasetBuilder.md): Abstract base class for all datasets.

[`class DatasetInfo`](../tfds/core/DatasetInfo.md): Information about a dataset.

[`class Experiment`](../tfds/core/Experiment.md): Experiments which can be
enabled/disabled on a per version basis.

[`class GeneratorBasedBuilder`](../tfds/core/GeneratorBasedBuilder.md): Base class for datasets with data generation based on dict generators.

[`class Metadata`](../tfds/core/Metadata.md): Abstract base class for
DatasetInfo metadata container.

[`class MetadataDict`](../tfds/core/MetadataDict.md): A
<a href="../tfds/core/Metadata.md"><code>tfds.core.Metadata</code></a> object
that acts as a `dict`.

[`class NamedSplit`](../tfds/core/NamedSplit.md): Descriptor corresponding to a named split (train, test, ...).

[`class SplitBase`](../tfds/core/SplitBase.md): Abstract base class for Split compositionality.

[`class SplitDict`](../tfds/core/SplitDict.md): Split info object.

[`class SplitGenerator`](../tfds/core/SplitGenerator.md): Defines the split information for the generator.

[`class SplitInfo`](../tfds/core/SplitInfo.md): Wraps `proto.SplitInfo` with an additional property.

[`class Version`](../tfds/core/Version.md): Dataset version MAJOR.MINOR.PATCH.

[`class lazy_imports`](../tfds/core/lazy_imports.md): Lazy importer for heavy
dependencies.

## Functions

[`get_tfds_path(...)`](../tfds/core/get_tfds_path.md): Returns absolute path to file given path relative to tfds root.

