<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.Split" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="ALL"/>
<meta itemprop="property" content="TEST"/>
<meta itemprop="property" content="TRAIN"/>
<meta itemprop="property" content="VALIDATION"/>
</div>

# tfds.Split

## Class `Split`

`Enum` for dataset splits.

Defined in [`core/splits.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py).

<!-- Placeholder for "Used in" -->

Datasets are typically split into different subsets to be used at various
stages of training and evaluation.

* `TRAIN`: the training data.
* `VALIDATION`: the validation data. If present, this is typically used as
  evaluation data while iterating on a model (e.g. changing hyperparameters,
  model architecture, etc.).
* `TEST`: the testing data. This is the data to report metrics on. Typically
  you do not want to use this during model iteration as you may overfit to it.
* `ALL`: Special value, never defined by a dataset, but corresponding to all
  defined splits of a dataset merged together.

Note: All splits, including compositions inherit from <a href="../tfds/core/SplitBase.md"><code>tfds.core.SplitBase</code></a>

See the
[guide on splits](https://github.com/tensorflow/datasets/tree/master/docs/splits.md)
for more information.

## Class Members

*   `ALL` <a id="ALL"></a>
*   `TEST` <a id="TEST"></a>
*   `TRAIN` <a id="TRAIN"></a>
*   `VALIDATION` <a id="VALIDATION"></a>
