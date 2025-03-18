Imagenet2012Subset is a subset of original ImageNet ILSVRC 2012 dataset. The
dataset share the *same* validation set as the original ImageNet ILSVRC 2012
dataset. However, the training set is subsampled in a label balanced fashion. In
`1pct` configuration, 1%, or 12811, images are sampled, most classes have the
same number of images (average 12.8), some classes randomly have 1 more example
than others; and in `10pct` configuration, ~10%, or 128116, most classes have
the same number of images (average 128), and some classes randomly have 1 more
example than others.

This is supposed to be used as a benchmark for semi-supervised learning, and has
been originally used in SimCLR paper (https://arxiv.org/abs/2002.05709).
