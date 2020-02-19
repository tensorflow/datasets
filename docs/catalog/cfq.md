<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cfq" />
  <meta itemprop="description" content="&#10;The CFQ dataset (and it&#x27;s splits) for measuring compositional generalization.&#10;&#10;See https://arxiv.org/abs/1912.09713.pdf for background.&#10;&#10;Example usage:&#10;data = tfds.load(&#x27;cfq/mcd1&#x27;)&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cfq&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cfq" />
  <meta itemprop="sameAs" content="https://github.com/google-research/google-research/tree/master/cfq" />
  <meta itemprop="citation" content="&#10;@inproceedings{Lake2018GeneralizationWS,&#10;  title={Measuring Compositional Generalization: A Comprehensive Method on&#10;         Realistic Data},&#10;  author={Daniel Keysers, et al.},&#10;  booktitle={ICLR},&#10;  year={2020},&#10;  url={https://arxiv.org/abs/1912.09713.pdf},&#10;}&#10;" />
</div>
# `cfq`

*   **Description**:

The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1')

*   **Config description**: The CFQ dataset (and it's splits) for measuring
    compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage: data = tfds.load('cfq/mcd1') * **Homepage**:
[https://github.com/google-research/google-research/tree/master/cfq](https://github.com/google-research/google-research/tree/master/cfq)
* **Source code**:
[`tfds.text.cfq.CFQ`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/cfq.py)
* **Versions**: * **`1.0.0`** (default): No release notes. * **Download size**:
`255.20 MiB` * **Dataset size**: `Unknown size` * **Auto-cached**
([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
No * **Features**:

```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```
*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load)):
    `('question', 'query')`
*   **Citation**:

```
@inproceedings{Lake2018GeneralizationWS,
  title={Measuring Compositional Generalization: A Comprehensive Method on
         Realistic Data},
  author={Daniel Keysers, et al.},
  booktitle={ICLR},
  year={2020},
  url={https://arxiv.org/abs/1912.09713.pdf},
}
```

## cfq/mcd1 (default config)

*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 11,968
'train' | 95,743

## cfq/mcd2

*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 11,968
'train' | 95,743

## cfq/mcd3

*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 11,968
'train' | 95,743

## cfq/question_complexity_split

*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 10,340
'train' | 98,999

## cfq/question_pattern_split

*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 11,909
'train' | 95,654

## cfq/query_complexity_split

*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 9,512
'train' | 100,654

## cfq/query_pattern_split

*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 12,589
'train' | 94,600

## cfq/random_split

*   **Splits**:

Split   | Examples
:------ | -------:
'test'  | 11,967
'train' | 95,744
