<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.text.SubwordTextEncoder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="subwords"/>
<meta itemprop="property" content="vocab_size"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="build_from_corpus"/>
<meta itemprop="property" content="decode"/>
<meta itemprop="property" content="encode"/>
<meta itemprop="property" content="load_from_file"/>
<meta itemprop="property" content="save_to_file"/>
</div>

# tfds.features.text.SubwordTextEncoder

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/subword_text_encoder.py">View
source</a>

## Class `SubwordTextEncoder`

Invertible `TextEncoder` using word pieces with a byte-level fallback.

Inherits From: [`TextEncoder`](../../../tfds/features/text/TextEncoder.md)

<!-- Placeholder for "Used in" -->

Encoding is fully invertible because all out-of-vocab wordpieces are
byte-encoded.

The vocabulary is "trained" on a corpus and all wordpieces are stored in a
vocabulary file. To generate a vocabulary from a corpus, use
<a href="../../../tfds/features/text/SubwordTextEncoder.md#build_from_corpus"><code>tfds.features.text.SubwordTextEncoder.build_from_corpus</code></a>.

#### Typical usage:

```
# Build
encoder = tfds.features.text.SubwordTextEncoder.build_from_corpus(
    corpus_generator, target_vocab_size=2**15)
encoder.save_to_file(vocab_filename)

# Load
encoder = tfds.features.text.SubwordTextEncoder.load_from_file(vocab_filename)
ids = encoder.encode("hello world")
text = encoder.decode([1, 2, 3, 4])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/subword_text_encoder.py">View
source</a>

``` python
__init__(vocab_list=None)
```

Constructs a SubwordTextEncoder from a vocabulary list.

Note: To generate a vocabulary from a corpus, use
<a href="../../../tfds/features/text/SubwordTextEncoder.md#build_from_corpus"><code>tfds.features.text.SubwordTextEncoder.build_from_corpus</code></a>.

#### Args:

*   <b>`vocab_list`</b>: `list<str>`, list of subwords for the vocabulary. Note
    that an underscore at the end of a subword indicates the end of the word
    (i.e. a space will be inserted afterwards when decoding). Underscores in the
    interior of subwords are disallowed and should use the underscore escape
    sequence.

## Properties

<h3 id="subwords"><code>subwords</code></h3>

<h3 id="vocab_size"><code>vocab_size</code></h3>

## Methods

<h3 id="build_from_corpus"><code>build_from_corpus</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/subword_text_encoder.py">View
source</a>

``` python
@classmethod
build_from_corpus(
    cls,
    corpus_generator,
    target_vocab_size,
    max_subword_length=20,
    max_corpus_chars=None,
    reserved_tokens=None
)
```

Builds a `SubwordTextEncoder` based on the `corpus_generator`.

#### Args:

*   <b>`corpus_generator`</b>: generator yielding `str`, from which subwords
    will be constructed.
*   <b>`target_vocab_size`</b>: `int`, approximate size of the vocabulary to
    create.
*   <b>`max_subword_length`</b>: `int`, maximum length of a subword. Note that
    memory and compute scale quadratically in the length of the longest token.
*   <b>`max_corpus_chars`</b>: `int`, the maximum number of characters to
    consume from `corpus_generator` for the purposes of building the subword
    vocabulary.
*   <b>`reserved_tokens`</b>: `list<str>`, list of tokens that will always be
    treated as whole tokens and not split up. Note that these must contain a mix
    of alphanumeric and non-alphanumeric characters (e.g. "<EOS>") and not end
    in an underscore.

#### Returns:

`SubwordTextEncoder`.

<h3 id="decode"><code>decode</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/subword_text_encoder.py">View
source</a>

``` python
decode(ids)
```

Decodes a list of integers into text.

<h3 id="encode"><code>encode</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/subword_text_encoder.py">View
source</a>

``` python
encode(s)
```

Encodes text into a list of integers.

<h3 id="load_from_file"><code>load_from_file</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/subword_text_encoder.py">View
source</a>

``` python
@classmethod
load_from_file(
    cls,
    filename_prefix
)
```

Extracts list of subwords from file.

<h3 id="save_to_file"><code>save_to_file</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/subword_text_encoder.py">View
source</a>

``` python
save_to_file(filename_prefix)
```

Save the vocabulary to a file.
