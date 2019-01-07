<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tfds.features



Defined in [`core/features/__init__.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/__init__.py).

<a href="../tfds/features/FeatureConnector.md"><code>tfds.features.FeatureConnector</code></a> API defining feature types.

## Modules

[`text`](../tfds/features/text.md) module: Text utilities.

## Classes

[`class ClassLabel`](../tfds/features/ClassLabel.md): `FeatureConnector` for integer class labels.

[`class FeatureConnector`](../tfds/features/FeatureConnector.md): Abstract base class for feature types.

[`class FeaturesDict`](../tfds/features/FeaturesDict.md): Composite `FeatureConnector`; each feature in `dict` has its own connector.

[`class Tensor`](../tfds/features/Tensor.md): `FeatureConnector` for generic data of arbitrary shape and type.

[`class TensorInfo`](../tfds/features/TensorInfo.md): TensorInfo(shape, dtype)

[`class Sequence`](../tfds/features/Sequence.md): Similar to `tfds.featuresSequenceDict`, but only contains a single feature.

[`class SequenceDict`](../tfds/features/SequenceDict.md): Composite `FeatureConnector` for a `dict` where each value is a list.

[`class Image`](../tfds/features/Image.md): `FeatureConnector` for images.

[`class Text`](../tfds/features/Text.md): `FeatureConnector` for text, encoding to integers with a `TextEncoder`.

[`class Video`](../tfds/features/Video.md): `FeatureConnector` for videos, png-encoding frames on disk.

