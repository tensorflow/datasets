<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cos_e" />
  <meta itemprop="description" content="&#10;Common Sense Explanations (CoS-E) allows for training language models to&#10;automatically generate explanations that can be used during training and&#10;inference in a novel Commonsense Auto-Generated Explanation (CAGE) framework.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cos_e&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cos_e" />
  <meta itemprop="sameAs" content="https://github.com/salesforce/cos-e" />
  <meta itemprop="citation" content="&#10;@inproceedings{rajani2019explain,&#10;     title = &quot;Explain Yourself! Leveraging Language models for Commonsense Reasoning&quot;,&#10;    author = &quot;Rajani, Nazneen Fatema  and&#10;      McCann, Bryan  and&#10;      Xiong, Caiming  and&#10;      Socher, Richard&quot;,&#10;      year=&quot;2019&quot;,&#10;    booktitle = &quot;Proceedings of the 2019 Conference of the Association for Computational Linguistics (ACL2019)&quot;,&#10;    url =&quot;https://arxiv.org/abs/1906.02361&quot;&#10;}&#10;" />
</div>
# `cos_e`

Common Sense Explanations (CoS-E) allows for training language models to
automatically generate explanations that can be used during training and
inference in a novel Commonsense Auto-Generated Explanation (CAGE) framework.

*   URL:
    [https://github.com/salesforce/cos-e](https://github.com/salesforce/cos-e)
*   `DatasetBuilder`:
    [`tfds.text.cos_e.CosE`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/cos_e.py)
*   Version: `v0.0.1`
*   Versions:

    *   **`0.0.1`** (default):

*   Size: `6.23 MiB`

## Features
```python
FeaturesDict({
    'abstractive_explanation': Text(shape=(), dtype=tf.string),
    'answer': Text(shape=(), dtype=tf.string),
    'choices': Sequence(Text(shape=(), dtype=tf.string)),
    'extractive_explanation': Text(shape=(), dtype=tf.string),
    'id': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 10,962
TRAIN      | 9,741
VALIDATION | 1,221

## Homepage

*   [https://github.com/salesforce/cos-e](https://github.com/salesforce/cos-e)

## Citation
```
@inproceedings{rajani2019explain,
     title = "Explain Yourself! Leveraging Language models for Commonsense Reasoning",
    author = "Rajani, Nazneen Fatema  and
      McCann, Bryan  and
      Xiong, Caiming  and
      Socher, Richard",
      year="2019",
    booktitle = "Proceedings of the 2019 Conference of the Association for Computational Linguistics (ACL2019)",
    url ="https://arxiv.org/abs/1906.02361"
}
```

--------------------------------------------------------------------------------
