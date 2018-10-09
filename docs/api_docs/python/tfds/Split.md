<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.Split" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="TEST"/>
<meta itemprop="property" content="TRAIN"/>
<meta itemprop="property" content="VALIDATION"/>
<meta itemprop="property" content="__members__"/>
</div>

# tfds.Split

## Class `Split`



`Enum` for dataset splits.

Datasets are typically split into different subsets to be used at various
stages of training and evaluation. All datasets have at least the `TRAIN` and
`TEST` splits.

Note that for datasets without a `VALIDATION` split, you should use a fraction
of the `TRAIN` data for evaluation as you iterate on your model so as not to
overfit to the `TEST` data. You can do so by...

TODO(rsepassi): update when as_dataset supports this.

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

<h3 id="__members__"><code>__members__</code></h3>

