<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.show_examples" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.show_examples

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/visualization.py">View
source</a>

Visualize images (and labels) from an image classification dataset.

```python
tfds.show_examples(
    ds_info,
    ds,
    rows=3,
    cols=3,
    plot_scale=3.0,
    image_key=None
)
```

<!-- Placeholder for "Used in" -->

Only works with datasets that have 1 image feature and optionally 1 label
feature (both inferred from `ds_info`). Note the dataset should be unbatched.
Requires matplotlib to be installed.

This function is for interactive use (Colab, Jupyter). It displays and return a
plot of (rows*columns) images from a tf.data.Dataset.

#### Usage:

```python
ds, ds_info = tfds.load('cifar10', split='train', with_info=True)
fig = tfds.show_examples(ds_info, ds)
```

#### Args:

*   <b>`ds_info`</b>: The dataset info object to which extract the label and
    features info. Available either through `tfds.load('mnist', with_info=True)`
    or `tfds.builder('mnist').info`
*   <b>`ds`</b>: `tf.data.Dataset`. The tf.data.Dataset object to visualize.
    Examples should not be batched. Examples will be consumed in order until
    (rows * cols) are read or the dataset is consumed.
*   <b>`rows`</b>: `int`, number of rows of the display grid.
*   <b>`cols`</b>: `int`, number of columns of the display grid.
*   <b>`plot_scale`</b>: `float`, controls the plot size of the images. Keep
    this value around 3 to get a good plot. High and low values may cause the
    labels to get overlapped.
*   <b>`image_key`</b>: `string`, name of the feature that contains the image.
    If not set, the system will try to auto-detect it.

#### Returns:

*   <b>`fig`</b>: The `matplotlib.Figure` object
