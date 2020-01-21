<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.text.Tokenizer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="alphanum_only"/>
<meta itemprop="property" content="reserved_tokens"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="join"/>
<meta itemprop="property" content="load_from_file"/>
<meta itemprop="property" content="save_to_file"/>
<meta itemprop="property" content="tokenize"/>
</div>

# tfds.features.text.Tokenizer

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

## Class `Tokenizer`

Splits a string into tokens, and joins them back.

<!-- Placeholder for "Used in" -->

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
__init__(
    alphanum_only=True,
    reserved_tokens=None
)
```

Constructs a Tokenizer.

Note that the Tokenizer is invertible if `alphanum_only=False`.
i.e. `s == t.join(t.tokenize(s))`.

#### Args:

*   <b>`alphanum_only`</b>: `bool`, if `True`, only parse out alphanumeric
    tokens (non-alphanumeric characters are dropped); otherwise, keep all
    characters (individual tokens will still be either all alphanumeric or all
    non-alphanumeric).
*   <b>`reserved_tokens`</b>: `list<str>`, a list of strings that, if any are in
    `s`, will be preserved as whole tokens, even if they contain mixed
    alphanumeric/non-alphanumeric characters.

## Properties

<h3 id="alphanum_only"><code>alphanum_only</code></h3>

<h3 id="reserved_tokens"><code>reserved_tokens</code></h3>

## Methods

<h3 id="join"><code>join</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
join(tokens)
```

Joins tokens into a string.

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

<h3 id="tokenize"><code>tokenize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py">View
source</a>

``` python
tokenize(s)
```

Splits a string into tokens.
