<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.decode.make_decoder" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.decode.make_decoder

Decorator to create a decoder.

```python
tfds.decode.make_decoder(output_dtype=None)
```

<a target="_blank" href=https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/decode/base.py>View
source</a>

<!-- Placeholder for "Used in" -->

The decorated function should have the signature `(example, feature, *args,
**kwargs) -> decoded_example`.

*   `example`: Serialized example before decoding
*   `feature`: `FeatureConnector` associated with the example
*   `*args, **kwargs`: Optional additional kwargs forwarded to the function

#### Example:

```
@tfds.decode.make_decoder(output_dtype=tf.string)
def no_op_decoder(example, feature):
  """Decoder simply decoding feature normally."""
  return feature.decode_example(example)

tfds.load('mnist', split='train', decoder: {
    'image': no_op_decoder(),
})
```

#### Args:

*   <b>`output_dtype`</b>: The output dtype after decoding. Required only if the
    decoded example has a different type than the
    <a href="../../tfds/features/FeatureConnector.md#dtype"><code>FeatureConnector.dtype</code></a>
    and is used to decode features inside sequences (ex: videos)

#### Returns:

The decoder object
