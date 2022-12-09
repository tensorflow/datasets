This dataset consists of the ImageNet dataset resized to fixed size. The images
here are the ones provided by Chrabaszcz et. al. using the box resize method.

For [downsampled ImageNet](http://image-net.org/download.php) for unsupervised
learning see `downsampled_imagenet`.

WARNING: The integer labels used are defined by the authors and do not match
those from the other ImageNet datasets provided by Tensorflow datasets. See the
original
[label list](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts/blob/master/map_clsloc.txt),
and the
[labels used by this dataset](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/image_classification/imagenet_resized_labels.txt).
Additionally, the original authors 1 index there labels which we convert to 0
indexed by subtracting one.
