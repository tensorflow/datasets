The database contains 108,753 images of 397 categories, used in the Scene
UNderstanding (SUN) benchmark. The number of images varies across categories,
but there are at least 100 images per category.

Several configs of the dataset are made available through TFDS:

 - A custom (random) partition of the whole dataset with 76,128 training images,
10,875 validation images and 21,750 test images. Images have been resized to
have at most 120,000 pixels, and encoded as JPEG with quality of 72.

- "standard-part1-120k", "standard-part2-120k", ..., "standard-part10-120k":
Each of the 10 official train/test partitions with 50 images per class in each
split. Images have been resized to have at most 120,000 pixels, and encoded as
JPEG with quality of 72.
