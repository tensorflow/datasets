# SA-1B Download

Segment Anything 1 Billion (SA-1B) is a dataset designed for training
general-purpose object segmentation models from open world images. The dataset
was introduced in the paper
["Segment Anything"](https://arxiv.org/abs/2304.02643).

The SA-1B dataset consists of 11M diverse, high-resolution, licensed, and
privacy-protecting images and 1.1B mask annotations. Masks are given in the COCO
run-length encoding (RLE) format, and do not have classes.

The license is custom. Please, read the full terms and conditions on
https://ai.facebook.com/datasets/segment-anything-downloads.

All the features are in the original dataset except `image.content` (content
of the image).

You can decode segmentation masks with:

```python
import tensorflow_datasets as tfds

pycocotools = tfds.core.lazy_imports.pycocotools

ds = tfds.load('segment_anything', split='train')
for example in tfds.as_numpy(ds):
  segmentation = example['annotations']['segmentation']
  for counts, size in zip(segmentation['counts'], segmentation['size']):
    encoded_mask = {'size': size, 'counts': counts}
    mask = pycocotools.decode(encoded_mask)  # np.array(dtype=uint8) mask
    ...
```
