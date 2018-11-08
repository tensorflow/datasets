<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.Split" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="TEST"/>
<meta itemprop="property" content="TRAIN"/>
<meta itemprop="property" content="VALIDATION"/>
</div>

# tfds.Split

## Class `Split`





Defined in [`core/splits.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py).

`Enum` for dataset splits.

Datasets are typically split into different subsets to be used at various
stages of training and evaluation.

* `TRAIN`: the training data.
* `VALIDATION`: the validation data. If present, this is typically used as
  evaluation data while iterating on a model (e.g. changing hyperparameters,
  model architecture, etc.).
* `TEST`: the testing data. This is the data to report metrics on. Typically
  you do not want to use this during model iteration as you may overfit to it.

## Class Members

<h3 id="TEST"><code>TEST</code></h3>

<h3 id="TRAIN"><code>TRAIN</code></h3>

<h3 id="VALIDATION"><code>VALIDATION</code></h3>

