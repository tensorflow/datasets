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

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

## Class `ByteTextEncoder`

Byte-encodes text.

Inherits From: [`TextEncoder`](../../../tfds/features/text/TextEncoder.md)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

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

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
decode(ids)
```

<h3 id="encode"><code>encode</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
encode(s)
```

<h3 id="load_from_file"><code>load_from_file</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
@classmethod
load_from_file(
    cls,
    filename_prefix
)
```

<h3 id="save_to_file"><code>save_to_file</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
save_to_file(filename_prefix)
```
