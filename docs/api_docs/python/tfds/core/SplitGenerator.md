<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.SplitGenerator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tfds.core.SplitGenerator

## Class `SplitGenerator`





Defined in [`core/splits.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/splits.py).

Defines the split info for the generator.

This should be used as returned value of
`GeneratorBasedDatasetBuilder._split_generators`.
See `GeneratorBasedDatasetBuilder._split_generators` for more info and example
of usage.

#### Args:

name (str/list[str]): Name of the Split for which the generator will create
  the examples. If a list is given, the generator examples will be
  distributed among the splits proportionally to the num_shards
num_shards (int/list[int]): Number of shards between which the generated
  examples will be written. If name is a list, then num_shards should be a
  list with the same number of element.
gen_kwargs (dict): Kwargs to forward to the ._generate_examples() of the
  generator builder

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    name,
    num_shards=1,
    gen_kwargs=None
)
```





