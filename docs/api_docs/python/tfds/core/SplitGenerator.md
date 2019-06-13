<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.SplitGenerator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tfds.core.SplitGenerator

## Class `SplitGenerator`

Defines the split information for the generator.

Defined in [`core/splits.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py).

<!-- Placeholder for "Used in" -->

This should be used as returned value of
`GeneratorBasedBuilder._split_generators`.
See `GeneratorBasedBuilder._split_generators` for more info and example
of usage.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name,
    num_shards=1,
    gen_kwargs=None
)
```

Constructs a `SplitGenerator`.

#### Args:

*   <b>`name`</b>: `str`, name of the Split for which the generator will create
    the examples.
*   <b>`num_shards`</b>: `int`, number of shards between which the generated
    examples will be written.
*   <b>`gen_kwargs`</b>: `dict`, kwargs to forward to the _generate_examples()
    method of the builder.
