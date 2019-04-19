<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.text.TokenTextEncoder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="lowercase"/>
<meta itemprop="property" content="oov_token"/>
<meta itemprop="property" content="tokenizer"/>
<meta itemprop="property" content="tokens"/>
<meta itemprop="property" content="vocab_size"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode"/>
<meta itemprop="property" content="encode"/>
<meta itemprop="property" content="load_from_file"/>
<meta itemprop="property" content="save_to_file"/>
</div>

# tfds.features.text.TokenTextEncoder

## Class `TokenTextEncoder`

Inherits From: [`TextEncoder`](../../../tfds/features/text/TextEncoder.md)



Defined in [`core/features/text/text_encoder.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py).

<!-- Placeholder for "Used in" -->

TextEncoder backed by a list of tokens.

Tokenization splits on (and drops) non-alphanumeric characters with
regex "\W+".

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    vocab_list,
    oov_buckets=1,
    oov_token='UNK',
    lowercase=False,
    tokenizer=None
)
```

Constructs a TokenTextEncoder.

To load from a file saved with `TokenTextEncoder.save_to_file`, use
`TokenTextEncoder.load_from_file`.

#### Args:

* <b>`vocab_list`</b>: `list<str>`, list of tokens.
* <b>`oov_buckets`</b>: `int`, the number of `int`s to reserve for OOV hash buckets.
    Tokens that are OOV will be hash-modded into a OOV bucket in `encode`.
* <b>`oov_token`</b>: `str`, the string to use for OOV ids in `decode`.
* <b>`lowercase`</b>: `bool`, whether to make all text and tokens lowercase.
* <b>`tokenizer`</b>: `Tokenizer`, responsible for converting incoming text into a
    list of tokens.



## Properties

<h3 id="lowercase"><code>lowercase</code></h3>



<h3 id="oov_token"><code>oov_token</code></h3>



<h3 id="tokenizer"><code>tokenizer</code></h3>



<h3 id="tokens"><code>tokens</code></h3>



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





