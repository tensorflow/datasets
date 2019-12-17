<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.text.TextEncoder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="vocab_size"/>
<meta itemprop="property" content="decode"/>
<meta itemprop="property" content="encode"/>
<meta itemprop="property" content="load_from_file"/>
<meta itemprop="property" content="save_to_file"/>
</div>

# tfds.features.text.TextEncoder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

## Class `TextEncoder`

Abstract base class for converting between text and integers.

<!-- Placeholder for "Used in" -->

**A note on padding**:

  Because text data is typically variable length and nearly always requires
  padding during training, ID 0 is always reserved for padding. To accommodate
  this, all `TextEncoder`s behave in certain ways:

  * `encode`: never returns id 0 (all ids are 1+)
  * `decode`: drops 0 in the input ids
  * `vocab_size`: includes ID 0

  New subclasses should be careful to match this behavior.

## Properties

<h3 id="vocab_size"><code>vocab_size</code></h3>

Size of the vocabulary. Decode produces ints [1, vocab_size).

## Methods

<h3 id="decode"><code>decode</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
decode(ids)
```

Decodes a list of integers into text.

<h3 id="encode"><code>encode</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
encode(s)
```

Encodes text into a list of integers.

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

Load from file. Inverse of save_to_file.

<h3 id="save_to_file"><code>save_to_file</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
save_to_file(filename_prefix)
```

Store to file. Inverse of load_from_file.
