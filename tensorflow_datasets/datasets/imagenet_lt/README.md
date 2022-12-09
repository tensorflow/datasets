ImageNet-LT is a subset of original ImageNet ILSVRC 2012 dataset. The training
set is subsampled such that the number of images per class follows a long-tailed
distribution. The class with the maximum number of images contains 1,280
examples, whereas the class with the minumum number of images contains only 5
examples. The dataset also has a balanced validation set, which is also a subset
of the ImageNet ILSVRC 2012 training set and contains 20 images per class. The
test set of this dataset is the same as the validation set of the original
ImageNet ILSVRC 2012 dataset.

The original ImageNet ILSVRC 2012 dataset must be downloaded manually, and its
path should be set with --manual_dir in order to generate this dataset.
