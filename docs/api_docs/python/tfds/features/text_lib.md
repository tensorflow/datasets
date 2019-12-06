<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.text" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tfds.features.text

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/__init__.py">View
source</a>

Text utilities.


<a href="../../tfds.md"><code>tfds</code></a> includes a set of `TextEncoder`s as well as a `Tokenizer` to enable
expressive, performant, and reproducible natural language research.

## Classes

[`class ByteTextEncoder`](../../tfds/features/text/ByteTextEncoder.md): Byte-encodes text.

[`class SubwordTextEncoder`](../../tfds/features/text/SubwordTextEncoder.md): Invertible `TextEncoder` using word pieces with a byte-level fallback.

[`class TextEncoder`](../../tfds/features/text/TextEncoder.md): Abstract base class for converting between text and integers.

[`class TextEncoderConfig`](../../tfds/features/text/TextEncoderConfig.md): Configuration for <a href="../../tfds/features/Text.md"><code>tfds.features.Text</code></a>.

[`class TokenTextEncoder`](../../tfds/features/text/TokenTextEncoder.md): TextEncoder backed by a list of tokens.

[`class Tokenizer`](../../tfds/features/text/Tokenizer.md): Splits a string into
tokens, and joins them back.
