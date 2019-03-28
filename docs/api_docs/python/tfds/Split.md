<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.Split" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="ALL"/>
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
* `ALL`: Special value, never defined by a dataset, but corresponding to all
  defined splits of a dataset merged together.

Note: All splits, including compositions inherit from <a href="../tfds/core/SplitBase.md"><code>tfds.core.SplitBase</code></a>

See the
[guide on splits](https://github.com/tensorflow/datasets/tree/master/docs/splits.md)
for more information.

<h2 id="__new__"><code>__new__</code></h2>

``` python
@staticmethod
__new__(
    cls,
    name
)
```

Create a custom split with tfds.Split('custom_name').



## Class Members

<h3 id="ALL"><code>ALL</code></h3>

<h3 id="TEST"><code>TEST</code></h3>

<h3 id="TRAIN"><code>TRAIN</code></h3>

<h3 id="VALIDATION"><code>VALIDATION</code></h3>

