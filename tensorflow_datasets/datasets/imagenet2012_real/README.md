This dataset contains ILSVRC-2012 (ImageNet) validation images augmented with a
new set of "Re-Assessed" (ReaL) labels from the "Are we done with ImageNet"
paper, see https://arxiv.org/abs/2006.07159. These labels are collected using
the enhanced protocol, resulting in multi-label and more accurate annotations.

Important note: about 3500 examples contain no label, these should be
[excluded from the averaging when computing the accuracy](https://github.com/google-research/reassessed-imagenet#numpy).
One possible way of doing this is with the following NumPy code:

```python
is_correct = [pred in real_labels[i] for i, pred in enumerate(predictions) if real_labels[i]]
real_accuracy = np.mean(is_correct)
```
