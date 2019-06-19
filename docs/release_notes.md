# Release notes

## Nightly

### New datasets

*   Image:
    [downsampled_imagenet](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md#downsampled_imagenet)
*   Image:
    [patch_camelyon](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md#patch_camelyon)

### Features

*   Add `in_memory` option to cache small dataset in RAM.
*   Better sharding, shuffling and sub-split
*   It is now possible to add arbitrary metadata to `tfds.core.DatasetInfo`
    which will be stored/restored with the dataset. See `tfds.core.Metadata`.
*   Better proxy support, possibility to add certificate
