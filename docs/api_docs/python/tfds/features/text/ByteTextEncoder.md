<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.text.ByteTextEncoder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="additional_tokens"/>
<meta itemprop="property" content="vocab_size"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode"/>
<meta itemprop="property" content="encode"/>
<meta itemprop="property" content="load_from_file"/>
<meta itemprop="property" content="save_to_file"/>
</div>

# tfds.features.text.ByteTextEncoder

## Class `ByteTextEncoder`

Byte-encodes text.

Inherits From: [`TextEncoder`](../../../tfds/features/text/TextEncoder.md)



Defined in [`core/features/text/text_encoder.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(additional_tokens=None)
```

Constructs ByteTextEncoder.

#### Args:

*   <b>`additional_tokens`</b>: `list<str>`, list of additional tokens. These
    will be assigned vocab ids `[1, 1+len(additional_tokens)]`. Useful for
    things like "end-of-string" tokens (e.g. "<EOS>").

## Properties

<h3 id="additional_tokens"><code>additional_tokens</code></h3>

<h3 id="vocab_size"><code>vocab_size</code></h3>

## Methods

<h3 id="decode"><code>decode</code></h3>

``` python
decode(ids)
```

<h3 id="encode"><code>encode</code></h3>

``` python
encode(s)
```

<h3 id="load_from_file"><code>load_from_file</code></h3>

``` python
@classmethod
load_from_file(
    cls,
    filename_prefix
)
```

<h3 id="save_to_file"><code>save_to_file</code></h3>

``` python
save_to_file(filename_prefix)
```
