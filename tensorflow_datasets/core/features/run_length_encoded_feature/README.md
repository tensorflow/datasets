# Run Length Encoded Features

Encoding/decoding functions for run length encoded data.

We include code for two variations:

* run length encoding (RLE)
* binary run length encdoing (BRLE)

RLE stores sequences of repeated values as the value followed by its count, e.g.

```python
dense_to_rle([5, 5, 3, 2, 2, 2, 2, 6]) == [5, 2, 3, 1, 2, 4, 6, 1]
```

i.e. the value `5` is repeated `2` times, then `3` is repeated `1` time, `2` is repeated `4` times and `6` is repeated `1` time.

BRLE is an optimized form for when the stored values can only be `0` or `1`. This means we only need to save the counts, and assume the values alternate (starting at `0`). For decoding simplicity, we ensure the encoded sequence ends with a count of `1`s so the length is necessarily even.

```python
dense_to_brle([1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]) == \
              [0, 2, 4, 7, 2, 0]
```

i.e. the value zero occurs `0` times, followed by `2` ones, `4` zeros, `7` ones, `2` zeros and `0` ones.

Sequences with counts exceeding the data type's maximum value have to be handled carefully. For example, the `uint8` encoding of 300 zeros
(`uint8` has a max value of 255) is:

* RLE: `[0, 255, 0, 45]`  (`0` repeated `255` times + `0` repeated `45` times)
* BRLE: `[255, 0, 45, 0]` (`255` zeros + `0` ones + `45` zeros + `0` ones)

## Module Layout

The `rle` submodule contains `numpy` and _limited_ `tensorflow` implementations of RLE/BRLE encoding, decoding and utility functions. For use with `DatasetBuilder`s we provide the `RunLengthEncodedFeature` and `BinaryRunLengthEncodedFeature` `FeatureConnector`s for (B)RLE-to-dense connections.

Note `RunLengthEncodedFeature` connectors depend on `rle.tf_impl.rle_to_dense` which is currently implemented using `tf.py_function`. This may cause issues on some systems.

## Example

See [image/shapenet_r2n2.py](../../../image/shapenet_r2n2.py) for a `DatasetBuilder` which uses a `BinaryRunLengthEncodedFeature` to encode voxel data.
