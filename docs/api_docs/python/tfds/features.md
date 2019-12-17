<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tfds.features

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/__init__.py">View
source</a>

<a href="../tfds/features/FeatureConnector.md"><code>tfds.features.FeatureConnector</code></a>
API defining feature types.

## Modules

[`text`](../tfds/features/text.md) module: Text utilities.

## Classes

[`class Audio`](../tfds/features/Audio.md): `FeatureConnector` for audio, encoded as raw integer wave form.

[`class BBox`](../tfds/features/BBox.md): BBox(ymin, xmin, ymax, xmax)

[`class BBoxFeature`](../tfds/features/BBoxFeature.md): `FeatureConnector` for a normalized bounding box.

[`class ClassLabel`](../tfds/features/ClassLabel.md): `FeatureConnector` for integer class labels.

[`class FeatureConnector`](../tfds/features/FeatureConnector.md): Abstract base class for feature types.

[`class FeaturesDict`](../tfds/features/FeaturesDict.md): Composite `FeatureConnector`; each feature in `dict` has its own connector.

[`class Image`](../tfds/features/Image.md): `FeatureConnector` for images.

[`class Sequence`](../tfds/features/Sequence.md): Composite `FeatureConnector`
for a `dict` where each value is a list.

[`class Tensor`](../tfds/features/Tensor.md): `FeatureConnector` for generic
data of arbitrary shape and type.

[`class TensorInfo`](../tfds/features/TensorInfo.md): Structure containing info
on the `tf.Tensor` shape/dtype.

[`class Text`](../tfds/features/Text.md): `FeatureConnector` for text, encoding to integers with a `TextEncoder`.

[`class Video`](../tfds/features/Video.md): `FeatureConnector` for videos, encoding frames individually on disk.
