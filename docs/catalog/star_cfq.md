<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="star_cfq" />
  <meta itemprop="description" content="The *-CFQ datasets (and their splits) for measuring the scalability of&#10;compositional generalization.&#10;&#10;See https://arxiv.org/abs/2012.08266 for background.&#10;&#10;Example usage:&#10;&#10;```&#10;data = tfds.load(&#x27;star_cfq/single_pool_10x_b_cfq&#x27;)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;star_cfq&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/star_cfq" />
  <meta itemprop="sameAs" content="https://github.com/google-research/google-research/tree/master/star-cfq" />
  <meta itemprop="citation" content="@inproceedings{Tsarkov2021,&#10;  title={*-CFQ: Analyzing the Scalability of Machine Learning on a Compositional Task},&#10;  author={Dmitry Tsarkov and Tibor Tihon and Nathan Scales and Nikola Momchev and Danila Sinopalnikov and Nathanael Sch&quot;{a}rli},&#10;  booktitle={AAAI},&#10;  year={2021},&#10;  url={https://arxiv.org/abs/2012.08266},&#10;}" />
</div>

# `star_cfq`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

The *-CFQ datasets (and their splits) for measuring the scalability of
compositional generalization.

See https://arxiv.org/abs/2012.08266 for background.

Example usage:

```
data = tfds.load('star_cfq/single_pool_10x_b_cfq')
```

*   **Homepage**:
    [https://github.com/google-research/google-research/tree/master/star-cfq](https://github.com/google-research/google-research/tree/master/star-cfq)

*   **Source code**:
    [`tfds.text.star_cfq.StarCFQ`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/star_cfq/star_cfq.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Features**:

```python
FeaturesDict({
    'query': Text(shape=(), dtype=tf.string),
    'question': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('question', 'query')`

*   **Citation**:

```
@inproceedings{Tsarkov2021,
  title={*-CFQ: Analyzing the Scalability of Machine Learning on a Compositional Task},
  author={Dmitry Tsarkov and Tibor Tihon and Nathan Scales and Nikola Momchev and Danila Sinopalnikov and Nathanael Sch"{a}rli},
  booktitle={AAAI},
  year={2021},
  url={https://arxiv.org/abs/2012.08266},
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

## star_cfq/single_pool_0.1x_cfq (default config)

## star_cfq/single_pool_0.2x_cfq

## star_cfq/single_pool_0.3x_cfq

## star_cfq/single_pool_0.5x_cfq

## star_cfq/single_pool_1x_cfq

## star_cfq/single_pool_2x_cfq

## star_cfq/single_pool_0.1x_o_cfq

## star_cfq/single_pool_0.2x_o_cfq

## star_cfq/single_pool_0.3x_o_cfq

## star_cfq/single_pool_0.5x_o_cfq

## star_cfq/single_pool_1x_o_cfq

## star_cfq/single_pool_2x_o_cfq

## star_cfq/single_pool_0.1x_u_cfq

## star_cfq/single_pool_0.2x_u_cfq

## star_cfq/single_pool_0.3x_u_cfq

## star_cfq/single_pool_0.5x_u_cfq

## star_cfq/single_pool_1x_u_cfq

## star_cfq/single_pool_2x_u_cfq

## star_cfq/single_pool_3x_u_cfq

## star_cfq/single_pool_6x_u_cfq

## star_cfq/single_pool_10x_u_cfq

## star_cfq/single_pool_30x_u_cfq

## star_cfq/single_pool_100x_u_cfq

## star_cfq/single_pool_0.1x_b_cfq

## star_cfq/single_pool_0.2x_b_cfq

## star_cfq/single_pool_0.25x_b_cfq

## star_cfq/single_pool_0.3x_b_cfq

## star_cfq/single_pool_0.4x_b_cfq

## star_cfq/single_pool_0.5x_b_cfq

## star_cfq/single_pool_0.6x_b_cfq

## star_cfq/single_pool_0.7x_b_cfq

## star_cfq/single_pool_0.75x_b_cfq

## star_cfq/single_pool_0.8x_b_cfq

## star_cfq/single_pool_1x_b_cfq

## star_cfq/single_pool_1.5x_b_cfq

## star_cfq/single_pool_2x_b_cfq

## star_cfq/single_pool_3x_b_cfq

## star_cfq/single_pool_4x_b_cfq

## star_cfq/single_pool_5x_b_cfq

## star_cfq/single_pool_6x_b_cfq

## star_cfq/single_pool_8x_b_cfq

## star_cfq/single_pool_10x_b_cfq

## star_cfq/single_pool_11x_b_cfq

## star_cfq/single_pool_12x_b_cfq

## star_cfq/single_pool_13x_b_cfq

## star_cfq/single_pool_15x_b_cfq

## star_cfq/single_pool_30x_b_cfq

## star_cfq/single_pool_35x_b_cfq

## star_cfq/single_pool_80x_b_cfq

## star_cfq/single_pool_85x_b_cfq

## star_cfq/single_pool_100x_b_cfq

## star_cfq/single_pool_0.25x_l_cfq

## star_cfq/single_pool_0.5x_l_cfq

## star_cfq/single_pool_0.75x_l_cfq

## star_cfq/single_pool_1x_l_cfq

## star_cfq/single_pool_3x_l_cfq

## star_cfq/single_pool_10x_l_cfq

## star_cfq/single_pool_30x_l_cfq

## star_cfq/single_pool_80x_l_cfq

## star_cfq/single_pool_100x_l_cfq

## star_cfq/single_pool_0.25x_half_l_cfq

## star_cfq/single_pool_0.5x_half_l_cfq

## star_cfq/single_pool_0.75x_half_l_cfq

## star_cfq/single_pool_1x_half_l_cfq

## star_cfq/single_pool_3x_half_l_cfq

## star_cfq/single_pool_10x_half_l_cfq

## star_cfq/single_pool_30x_half_l_cfq

## star_cfq/single_pool_80x_half_l_cfq

## star_cfq/single_pool_100x_half_l_cfq

## star_cfq/single_pool_0.25x_n_cfq

## star_cfq/single_pool_0.5x_n_cfq

## star_cfq/single_pool_0.75x_n_cfq

## star_cfq/single_pool_1x_n_cfq

## star_cfq/single_pool_3x_n_cfq

## star_cfq/single_pool_10x_n_cfq

## star_cfq/single_pool_30x_n_cfq

## star_cfq/single_pool_80x_n_cfq

## star_cfq/single_pool_100x_n_cfq

## star_cfq/single_pool_0.25x_half_n_cfq

## star_cfq/single_pool_0.5x_half_n_cfq

## star_cfq/single_pool_0.75x_half_n_cfq

## star_cfq/single_pool_1x_half_n_cfq

## star_cfq/single_pool_3x_half_n_cfq

## star_cfq/single_pool_10x_half_n_cfq

## star_cfq/single_pool_30x_half_n_cfq

## star_cfq/single_pool_80x_half_n_cfq

## star_cfq/single_pool_100x_half_n_cfq

## star_cfq/single_pool_0.25x_x_cfq

## star_cfq/single_pool_0.5x_x_cfq

## star_cfq/single_pool_0.75x_x_cfq

## star_cfq/single_pool_1x_x_cfq

## star_cfq/single_pool_3x_x_cfq

## star_cfq/single_pool_10x_x_cfq

## star_cfq/single_pool_30x_x_cfq

## star_cfq/single_pool_80x_x_cfq

## star_cfq/single_pool_100x_x_cfq

## star_cfq/single_pool_0.25x_half_x_cfq

## star_cfq/single_pool_0.5x_half_x_cfq

## star_cfq/single_pool_0.75x_half_x_cfq

## star_cfq/single_pool_1x_half_x_cfq

## star_cfq/single_pool_3x_half_x_cfq

## star_cfq/single_pool_10x_half_x_cfq

## star_cfq/single_pool_30x_half_x_cfq

## star_cfq/single_pool_80x_half_x_cfq

## star_cfq/single_pool_100x_half_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.1x_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.3x_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_1x_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_2x_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_3x_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_10x_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_30x_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_80x_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_100x_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_1x_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_2x_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_3x_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_10x_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_30x_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_80x_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_100x_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_1x_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_2x_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_3x_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_10x_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_30x_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_100x_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_1x_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_2x_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_3x_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_10x_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_30x_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_100x_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_1x_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_2x_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_3x_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_10x_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_30x_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_100x_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.1x_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.3x_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_1x_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_2x_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_3x_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_10x_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_30x_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_80x_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_100x_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.1x_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.3x_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_1x_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_2x_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_3x_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_10x_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_30x_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_100x_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.1x_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.3x_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_1x_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_2x_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_3x_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_10x_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_30x_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_100x_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.1x_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.3x_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_1x_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_2x_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_3x_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_10x_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_30x_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_100x_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.1x_half_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.3x_half_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_1x_half_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_2x_half_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_3x_half_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_10x_half_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_30x_half_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_80x_half_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_100x_half_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_half_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_half_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_1x_half_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_2x_half_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_3x_half_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_10x_half_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_30x_half_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_80x_half_l_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_100x_half_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_half_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_half_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_1x_half_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_2x_half_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_3x_half_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_10x_half_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_30x_half_l_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_100x_half_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_half_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_half_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_1x_half_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_2x_half_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_3x_half_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_10x_half_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_30x_half_l_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_100x_half_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_half_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_half_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_1x_half_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_2x_half_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_3x_half_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_10x_half_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_30x_half_l_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_100x_half_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.1x_half_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.3x_half_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_1x_half_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_2x_half_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_3x_half_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_10x_half_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_30x_half_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_80x_half_l_cfq

## star_cfq/equal_weighting_1x_b_cfq_100x_half_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.1x_half_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.3x_half_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_1x_half_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_2x_half_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_3x_half_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_10x_half_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_30x_half_l_cfq

## star_cfq/equal_weighting_2x_b_cfq_100x_half_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.1x_half_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.3x_half_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_1x_half_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_2x_half_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_3x_half_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_10x_half_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_30x_half_l_cfq

## star_cfq/equal_weighting_3x_b_cfq_100x_half_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.1x_half_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.3x_half_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_1x_half_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_2x_half_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_3x_half_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_10x_half_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_30x_half_l_cfq

## star_cfq/equal_weighting_5x_b_cfq_100x_half_l_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.1x_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.3x_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_1x_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_2x_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_3x_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_10x_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_30x_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_100x_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_1x_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_2x_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_3x_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_10x_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_30x_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_100x_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_1x_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_2x_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_3x_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_10x_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_30x_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_100x_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_1x_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_2x_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_3x_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_10x_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_30x_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_100x_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_1x_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_2x_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_3x_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_10x_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_30x_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_100x_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.1x_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.3x_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_1x_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_2x_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_3x_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_10x_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_30x_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_100x_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.1x_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.3x_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_1x_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_2x_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_3x_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_10x_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_30x_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_100x_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.1x_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.3x_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_1x_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_2x_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_3x_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_10x_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_30x_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_100x_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.1x_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.3x_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_1x_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_2x_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_3x_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_10x_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_30x_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_100x_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.1x_half_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.3x_half_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_1x_half_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_2x_half_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_3x_half_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_10x_half_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_30x_half_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_100x_half_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_half_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_half_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_1x_half_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_2x_half_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_3x_half_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_10x_half_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_30x_half_n_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_100x_half_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_half_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_half_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_1x_half_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_2x_half_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_3x_half_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_10x_half_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_30x_half_n_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_100x_half_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_half_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_half_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_1x_half_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_2x_half_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_3x_half_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_10x_half_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_30x_half_n_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_100x_half_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_half_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_half_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_1x_half_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_2x_half_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_3x_half_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_10x_half_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_30x_half_n_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_100x_half_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.1x_half_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.3x_half_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_1x_half_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_2x_half_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_3x_half_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_10x_half_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_30x_half_n_cfq

## star_cfq/equal_weighting_1x_b_cfq_100x_half_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.1x_half_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.3x_half_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_1x_half_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_2x_half_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_3x_half_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_10x_half_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_30x_half_n_cfq

## star_cfq/equal_weighting_2x_b_cfq_100x_half_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.1x_half_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.3x_half_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_1x_half_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_2x_half_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_3x_half_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_10x_half_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_30x_half_n_cfq

## star_cfq/equal_weighting_3x_b_cfq_100x_half_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.1x_half_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.3x_half_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_1x_half_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_2x_half_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_3x_half_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_10x_half_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_30x_half_n_cfq

## star_cfq/equal_weighting_5x_b_cfq_100x_half_n_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.1x_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.3x_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_1x_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_2x_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_3x_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_10x_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_30x_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_80x_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_100x_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_1x_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_2x_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_3x_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_10x_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_30x_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_80x_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_100x_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_1x_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_2x_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_3x_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_10x_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_30x_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_100x_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_1x_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_2x_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_3x_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_10x_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_30x_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_100x_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_1x_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_2x_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_3x_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_10x_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_30x_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_100x_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.1x_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.3x_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_1x_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_2x_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_3x_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_10x_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_30x_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_80x_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_100x_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.1x_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.3x_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_1x_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_2x_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_3x_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_10x_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_30x_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_100x_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.1x_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.3x_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_1x_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_2x_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_3x_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_10x_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_30x_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_100x_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.1x_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.3x_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_1x_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_2x_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_3x_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_10x_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_30x_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_100x_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.1x_half_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_0.3x_half_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_1x_half_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_2x_half_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_3x_half_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_10x_half_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_30x_half_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_80x_half_x_cfq

## star_cfq/equal_weighting_0x_b_cfq_100x_half_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.1x_half_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_0.3x_half_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_1x_half_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_2x_half_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_3x_half_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_10x_half_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_30x_half_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_80x_half_x_cfq

## star_cfq/equal_weighting_0.1x_b_cfq_100x_half_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.1x_half_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_0.3x_half_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_1x_half_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_2x_half_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_3x_half_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_10x_half_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_30x_half_x_cfq

## star_cfq/equal_weighting_0.2x_b_cfq_100x_half_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.1x_half_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_0.3x_half_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_1x_half_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_2x_half_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_3x_half_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_10x_half_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_30x_half_x_cfq

## star_cfq/equal_weighting_0.3x_b_cfq_100x_half_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.1x_half_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_0.3x_half_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_1x_half_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_2x_half_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_3x_half_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_10x_half_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_30x_half_x_cfq

## star_cfq/equal_weighting_0.5x_b_cfq_100x_half_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.1x_half_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_0.3x_half_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_1x_half_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_2x_half_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_3x_half_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_10x_half_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_30x_half_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_80x_half_x_cfq

## star_cfq/equal_weighting_1x_b_cfq_100x_half_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.1x_half_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_0.3x_half_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_1x_half_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_2x_half_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_3x_half_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_10x_half_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_30x_half_x_cfq

## star_cfq/equal_weighting_2x_b_cfq_100x_half_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.1x_half_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_0.3x_half_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_1x_half_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_2x_half_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_3x_half_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_10x_half_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_30x_half_x_cfq

## star_cfq/equal_weighting_3x_b_cfq_100x_half_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.1x_half_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_0.3x_half_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_1x_half_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_2x_half_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_3x_half_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_10x_half_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_30x_half_x_cfq

## star_cfq/equal_weighting_5x_b_cfq_100x_half_x_cfq

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_l_cfq

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_l_cfq

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_l_cfq

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_l_cfq

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_l_cfq

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_l_cfq

## star_cfq/overweighting_0.1x_unique_80x_b_cfq_80x_l_cfq

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_half_l_cfq

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_half_l_cfq

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_half_l_cfq

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_half_l_cfq

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_half_l_cfq

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_half_l_cfq

## star_cfq/overweighting_0.1x_unique_80x_b_cfq_80x_half_l_cfq

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_n_cfq

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_n_cfq

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_n_cfq

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_n_cfq

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_n_cfq

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_n_cfq

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_half_n_cfq

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_half_n_cfq

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_half_n_cfq

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_half_n_cfq

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_half_n_cfq

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_half_n_cfq

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_x_cfq

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_x_cfq

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_x_cfq

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_x_cfq

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_x_cfq

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_x_cfq

## star_cfq/overweighting_0.1x_unique_80x_b_cfq_80x_x_cfq

## star_cfq/overweighting_0.1x_unique_0.1x_b_cfq_0.1x_half_x_cfq

## star_cfq/overweighting_0.1x_unique_0.3x_b_cfq_0.3x_half_x_cfq

## star_cfq/overweighting_0.1x_unique_1x_b_cfq_1x_half_x_cfq

## star_cfq/overweighting_0.1x_unique_3x_b_cfq_3x_half_x_cfq

## star_cfq/overweighting_0.1x_unique_10x_b_cfq_10x_half_x_cfq

## star_cfq/overweighting_0.1x_unique_30x_b_cfq_30x_half_x_cfq

## star_cfq/overweighting_0.1x_unique_80x_b_cfq_80x_half_x_cfq

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_l_cfq

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_l_cfq

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_l_cfq

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_l_cfq

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_l_cfq

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_l_cfq

## star_cfq/overweighting_1x_unique_80x_b_cfq_80x_l_cfq

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_half_l_cfq

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_half_l_cfq

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_half_l_cfq

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_half_l_cfq

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_half_l_cfq

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_half_l_cfq

## star_cfq/overweighting_1x_unique_80x_b_cfq_80x_half_l_cfq

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_n_cfq

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_n_cfq

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_n_cfq

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_n_cfq

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_n_cfq

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_n_cfq

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_half_n_cfq

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_half_n_cfq

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_half_n_cfq

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_half_n_cfq

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_half_n_cfq

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_x_cfq

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_x_cfq

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_x_cfq

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_x_cfq

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_x_cfq

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_x_cfq

## star_cfq/overweighting_1x_unique_80x_b_cfq_80x_x_cfq

## star_cfq/overweighting_1x_unique_0.1x_b_cfq_0.1x_half_x_cfq

## star_cfq/overweighting_1x_unique_0.3x_b_cfq_0.3x_half_x_cfq

## star_cfq/overweighting_1x_unique_1x_b_cfq_1x_half_x_cfq

## star_cfq/overweighting_1x_unique_3x_b_cfq_3x_half_x_cfq

## star_cfq/overweighting_1x_unique_10x_b_cfq_10x_half_x_cfq

## star_cfq/overweighting_1x_unique_30x_b_cfq_30x_half_x_cfq

## star_cfq/overweighting_1x_unique_80x_b_cfq_80x_half_x_cfq

## star_cfq/ungrounded_on_grounded_0.1x

## star_cfq/ungrounded_on_grounded_0.2x

## star_cfq/ungrounded_on_grounded_0.3x

## star_cfq/ungrounded_on_grounded_0.5x

## star_cfq/ungrounded_on_grounded_1x

## star_cfq/ungrounded_on_grounded_2x

## star_cfq/ungrounded_on_grounded_3x

## star_cfq/ungrounded_on_grounded_10x

## star_cfq/ungrounded_on_grounded_30x

## star_cfq/ungrounded_on_grounded_100x

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r0

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r1

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r2

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r3

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r4

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r5

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r6

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r7

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r8

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r9

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r10

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r11

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r12

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r13

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r14

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r15

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r16

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r17

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r18

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r19

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r20

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r21

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r22

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r23

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r24

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r25

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r26

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r27

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r28

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r29

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r30

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r31

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r32

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r33

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r34

## star_cfq/u_cfq_compound_divergence_0.00333333_0_r35

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r0

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r1

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r2

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r3

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r4

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r5

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r6

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r7

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r8

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r9

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r10

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r11

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r12

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r13

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r14

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r15

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r16

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r17

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r18

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r19

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r20

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r21

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r22

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r23

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r24

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r25

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r26

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r27

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r28

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r29

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r30

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r31

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r32

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r33

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r34

## star_cfq/u_cfq_compound_divergence_0.00333333_0.1_r35

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r0

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r1

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r2

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r3

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r4

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r5

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r6

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r7

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r8

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r9

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r10

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r11

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r12

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r13

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r14

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r15

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r16

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r17

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r18

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r19

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r20

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r21

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r22

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r23

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r24

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r25

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r26

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r27

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r28

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r29

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r30

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r31

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r32

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r33

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r34

## star_cfq/u_cfq_compound_divergence_0.00333333_0.2_r35

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r0

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r1

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r2

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r3

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r4

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r5

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r6

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r7

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r8

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r9

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r10

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r11

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r12

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r13

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r14

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r15

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r16

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r17

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r18

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r19

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r20

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r21

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r22

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r23

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r24

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r25

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r26

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r27

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r28

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r29

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r30

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r31

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r32

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r33

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r34

## star_cfq/u_cfq_compound_divergence_0.00333333_0.3_r35

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r0

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r1

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r2

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r3

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r4

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r5

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r6

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r7

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r8

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r9

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r10

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r11

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r12

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r13

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r14

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r15

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r16

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r17

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r18

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r19

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r20

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r21

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r22

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r23

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r24

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r25

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r26

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r27

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r28

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r29

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r30

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r31

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r32

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r33

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r34

## star_cfq/u_cfq_compound_divergence_0.00333333_0.4_r35

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r0

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r1

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r2

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r3

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r4

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r5

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r6

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r7

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r8

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r9

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r10

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r11

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r12

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r13

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r14

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r15

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r16

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r17

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r18

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r19

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r20

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r21

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r22

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r23

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r24

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r25

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r26

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r27

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r28

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r29

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r30

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r31

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r32

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r33

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r34

## star_cfq/u_cfq_compound_divergence_0.00333333_0.5_r35

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r0

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r1

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r2

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r3

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r4

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r5

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r6

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r7

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r8

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r9

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r10

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r11

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r12

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r13

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r14

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r15

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r16

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r17

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r18

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r19

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r20

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r21

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r22

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r23

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r24

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r25

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r26

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r27

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r28

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r29

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r30

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r31

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r32

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r33

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r34

## star_cfq/u_cfq_compound_divergence_0.00333333_0.6_r35

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r0

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r1

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r2

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r3

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r4

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r5

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r6

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r7

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r8

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r9

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r10

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r11

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r12

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r13

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r14

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r15

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r16

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r17

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r18

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r19

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r20

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r21

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r22

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r23

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r24

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r25

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r26

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r27

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r28

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r29

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r30

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r31

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r32

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r33

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r34

## star_cfq/u_cfq_compound_divergence_0.00666667_0_r35

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r0

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r1

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r2

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r3

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r4

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r5

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r6

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r7

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r8

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r9

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r10

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r11

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r12

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r13

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r14

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r15

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r16

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r17

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r18

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r19

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r20

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r21

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r22

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r23

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r24

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r25

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r26

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r27

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r28

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r29

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r30

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r31

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r32

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r33

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r34

## star_cfq/u_cfq_compound_divergence_0.00666667_0.1_r35

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r0

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r1

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r2

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r3

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r4

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r5

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r6

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r7

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r8

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r9

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r10

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r11

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r12

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r13

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r14

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r15

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r16

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r17

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r18

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r19

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r20

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r21

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r22

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r23

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r24

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r25

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r26

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r27

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r28

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r29

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r30

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r31

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r32

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r33

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r34

## star_cfq/u_cfq_compound_divergence_0.00666667_0.2_r35

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r0

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r1

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r2

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r3

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r4

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r5

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r6

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r7

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r8

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r9

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r10

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r11

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r12

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r13

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r14

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r15

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r16

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r17

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r18

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r19

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r20

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r21

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r22

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r23

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r24

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r25

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r26

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r27

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r28

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r29

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r30

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r31

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r32

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r33

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r34

## star_cfq/u_cfq_compound_divergence_0.00666667_0.3_r35

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r0

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r1

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r2

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r3

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r4

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r5

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r6

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r7

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r8

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r9

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r10

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r11

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r12

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r13

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r14

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r15

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r16

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r17

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r18

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r19

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r20

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r21

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r22

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r23

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r24

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r25

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r26

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r27

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r28

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r29

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r30

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r31

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r32

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r33

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r34

## star_cfq/u_cfq_compound_divergence_0.00666667_0.4_r35

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r0

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r1

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r2

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r3

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r4

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r5

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r6

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r7

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r8

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r9

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r10

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r11

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r12

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r13

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r14

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r15

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r16

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r17

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r18

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r19

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r20

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r21

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r22

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r23

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r24

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r25

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r26

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r27

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r28

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r29

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r30

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r31

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r32

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r33

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r34

## star_cfq/u_cfq_compound_divergence_0.00666667_0.5_r35

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r0

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r1

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r2

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r3

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r4

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r5

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r6

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r7

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r8

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r9

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r10

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r11

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r12

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r13

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r14

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r15

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r16

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r17

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r18

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r19

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r20

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r21

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r22

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r23

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r24

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r25

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r26

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r27

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r28

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r29

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r30

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r31

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r32

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r33

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r34

## star_cfq/u_cfq_compound_divergence_0.00666667_0.6_r35

## star_cfq/u_cfq_compound_divergence_0.01_0_r0

## star_cfq/u_cfq_compound_divergence_0.01_0_r1

## star_cfq/u_cfq_compound_divergence_0.01_0_r2

## star_cfq/u_cfq_compound_divergence_0.01_0_r3

## star_cfq/u_cfq_compound_divergence_0.01_0_r4

## star_cfq/u_cfq_compound_divergence_0.01_0_r5

## star_cfq/u_cfq_compound_divergence_0.01_0_r6

## star_cfq/u_cfq_compound_divergence_0.01_0_r7

## star_cfq/u_cfq_compound_divergence_0.01_0_r8

## star_cfq/u_cfq_compound_divergence_0.01_0_r9

## star_cfq/u_cfq_compound_divergence_0.01_0_r10

## star_cfq/u_cfq_compound_divergence_0.01_0_r11

## star_cfq/u_cfq_compound_divergence_0.01_0_r12

## star_cfq/u_cfq_compound_divergence_0.01_0_r13

## star_cfq/u_cfq_compound_divergence_0.01_0_r14

## star_cfq/u_cfq_compound_divergence_0.01_0_r15

## star_cfq/u_cfq_compound_divergence_0.01_0_r16

## star_cfq/u_cfq_compound_divergence_0.01_0_r17

## star_cfq/u_cfq_compound_divergence_0.01_0_r18

## star_cfq/u_cfq_compound_divergence_0.01_0_r19

## star_cfq/u_cfq_compound_divergence_0.01_0_r20

## star_cfq/u_cfq_compound_divergence_0.01_0_r21

## star_cfq/u_cfq_compound_divergence_0.01_0_r22

## star_cfq/u_cfq_compound_divergence_0.01_0_r23

## star_cfq/u_cfq_compound_divergence_0.01_0_r24

## star_cfq/u_cfq_compound_divergence_0.01_0_r25

## star_cfq/u_cfq_compound_divergence_0.01_0_r26

## star_cfq/u_cfq_compound_divergence_0.01_0_r27

## star_cfq/u_cfq_compound_divergence_0.01_0_r28

## star_cfq/u_cfq_compound_divergence_0.01_0_r29

## star_cfq/u_cfq_compound_divergence_0.01_0_r30

## star_cfq/u_cfq_compound_divergence_0.01_0_r31

## star_cfq/u_cfq_compound_divergence_0.01_0_r32

## star_cfq/u_cfq_compound_divergence_0.01_0_r33

## star_cfq/u_cfq_compound_divergence_0.01_0_r34

## star_cfq/u_cfq_compound_divergence_0.01_0_r35

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r0

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r1

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r2

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r3

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r4

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r5

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r6

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r7

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r8

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r9

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r10

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r11

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r12

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r13

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r14

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r15

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r16

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r17

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r18

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r19

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r20

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r21

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r22

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r23

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r24

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r25

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r26

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r27

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r28

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r29

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r30

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r31

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r32

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r33

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r34

## star_cfq/u_cfq_compound_divergence_0.01_0.1_r35

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r0

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r1

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r2

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r3

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r4

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r5

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r6

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r7

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r8

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r9

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r10

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r11

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r12

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r13

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r14

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r15

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r16

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r17

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r18

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r19

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r20

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r21

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r22

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r23

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r24

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r25

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r26

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r27

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r28

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r29

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r30

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r31

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r32

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r33

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r34

## star_cfq/u_cfq_compound_divergence_0.01_0.2_r35

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r0

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r1

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r2

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r3

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r4

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r5

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r6

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r7

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r8

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r9

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r10

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r11

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r12

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r13

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r14

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r15

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r16

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r17

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r18

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r19

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r20

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r21

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r22

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r23

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r24

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r25

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r26

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r27

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r28

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r29

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r30

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r31

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r32

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r33

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r34

## star_cfq/u_cfq_compound_divergence_0.01_0.3_r35

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r0

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r1

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r2

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r3

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r4

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r5

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r6

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r7

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r8

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r9

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r10

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r11

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r12

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r13

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r14

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r15

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r16

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r17

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r18

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r19

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r20

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r21

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r22

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r23

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r24

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r25

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r26

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r27

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r28

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r29

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r30

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r31

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r32

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r33

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r34

## star_cfq/u_cfq_compound_divergence_0.01_0.4_r35

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r0

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r1

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r2

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r3

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r4

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r5

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r6

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r7

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r8

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r9

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r10

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r11

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r12

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r13

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r14

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r15

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r16

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r17

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r18

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r19

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r20

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r21

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r22

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r23

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r24

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r25

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r26

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r27

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r28

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r29

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r30

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r31

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r32

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r33

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r34

## star_cfq/u_cfq_compound_divergence_0.01_0.5_r35

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r0

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r1

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r2

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r3

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r4

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r5

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r6

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r7

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r8

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r9

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r10

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r11

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r12

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r13

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r14

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r15

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r16

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r17

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r18

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r19

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r20

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r21

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r22

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r23

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r24

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r25

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r26

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r27

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r28

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r29

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r30

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r31

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r32

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r33

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r34

## star_cfq/u_cfq_compound_divergence_0.01_0.6_r35

## star_cfq/u_cfq_compound_divergence_0.02_0_r0

## star_cfq/u_cfq_compound_divergence_0.02_0_r1

## star_cfq/u_cfq_compound_divergence_0.02_0_r2

## star_cfq/u_cfq_compound_divergence_0.02_0_r3

## star_cfq/u_cfq_compound_divergence_0.02_0_r4

## star_cfq/u_cfq_compound_divergence_0.02_0_r5

## star_cfq/u_cfq_compound_divergence_0.02_0_r6

## star_cfq/u_cfq_compound_divergence_0.02_0_r7

## star_cfq/u_cfq_compound_divergence_0.02_0_r8

## star_cfq/u_cfq_compound_divergence_0.02_0_r9

## star_cfq/u_cfq_compound_divergence_0.02_0_r10

## star_cfq/u_cfq_compound_divergence_0.02_0_r11

## star_cfq/u_cfq_compound_divergence_0.02_0_r12

## star_cfq/u_cfq_compound_divergence_0.02_0_r13

## star_cfq/u_cfq_compound_divergence_0.02_0_r14

## star_cfq/u_cfq_compound_divergence_0.02_0_r15

## star_cfq/u_cfq_compound_divergence_0.02_0_r16

## star_cfq/u_cfq_compound_divergence_0.02_0_r17

## star_cfq/u_cfq_compound_divergence_0.02_0_r18

## star_cfq/u_cfq_compound_divergence_0.02_0_r19

## star_cfq/u_cfq_compound_divergence_0.02_0_r20

## star_cfq/u_cfq_compound_divergence_0.02_0_r21

## star_cfq/u_cfq_compound_divergence_0.02_0_r22

## star_cfq/u_cfq_compound_divergence_0.02_0_r23

## star_cfq/u_cfq_compound_divergence_0.02_0_r24

## star_cfq/u_cfq_compound_divergence_0.02_0_r25

## star_cfq/u_cfq_compound_divergence_0.02_0_r26

## star_cfq/u_cfq_compound_divergence_0.02_0_r27

## star_cfq/u_cfq_compound_divergence_0.02_0_r28

## star_cfq/u_cfq_compound_divergence_0.02_0_r29

## star_cfq/u_cfq_compound_divergence_0.02_0_r30

## star_cfq/u_cfq_compound_divergence_0.02_0_r31

## star_cfq/u_cfq_compound_divergence_0.02_0_r32

## star_cfq/u_cfq_compound_divergence_0.02_0_r33

## star_cfq/u_cfq_compound_divergence_0.02_0_r34

## star_cfq/u_cfq_compound_divergence_0.02_0_r35

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r0

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r1

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r2

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r3

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r4

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r5

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r6

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r7

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r8

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r9

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r10

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r11

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r12

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r13

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r14

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r15

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r16

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r17

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r18

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r19

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r20

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r21

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r22

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r23

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r24

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r25

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r26

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r27

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r28

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r29

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r30

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r31

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r32

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r33

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r34

## star_cfq/u_cfq_compound_divergence_0.02_0.1_r35

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r0

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r1

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r2

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r3

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r4

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r5

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r6

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r7

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r8

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r9

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r10

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r11

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r12

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r13

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r14

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r15

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r16

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r17

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r18

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r19

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r20

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r21

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r22

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r23

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r24

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r25

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r26

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r27

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r28

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r29

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r30

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r31

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r32

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r33

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r34

## star_cfq/u_cfq_compound_divergence_0.02_0.2_r35

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r0

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r1

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r2

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r3

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r4

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r5

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r6

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r7

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r8

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r9

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r10

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r11

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r12

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r13

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r14

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r15

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r16

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r17

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r18

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r19

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r20

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r21

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r22

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r23

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r24

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r25

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r26

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r27

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r28

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r29

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r30

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r31

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r32

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r33

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r34

## star_cfq/u_cfq_compound_divergence_0.02_0.3_r35

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r0

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r1

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r2

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r3

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r4

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r5

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r6

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r7

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r8

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r9

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r10

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r11

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r12

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r13

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r14

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r15

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r16

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r17

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r18

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r19

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r20

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r21

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r22

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r23

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r24

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r25

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r26

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r27

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r28

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r29

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r30

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r31

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r32

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r33

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r34

## star_cfq/u_cfq_compound_divergence_0.02_0.4_r35

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r0

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r1

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r2

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r3

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r4

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r5

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r6

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r7

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r8

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r9

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r10

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r11

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r12

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r13

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r14

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r15

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r16

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r17

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r18

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r19

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r20

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r21

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r22

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r23

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r24

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r25

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r26

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r27

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r28

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r29

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r30

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r31

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r32

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r33

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r34

## star_cfq/u_cfq_compound_divergence_0.02_0.5_r35

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r0

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r1

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r2

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r3

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r4

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r5

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r6

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r7

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r8

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r9

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r10

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r11

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r12

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r13

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r14

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r15

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r16

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r17

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r18

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r19

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r20

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r21

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r22

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r23

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r24

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r25

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r26

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r27

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r28

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r29

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r30

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r31

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r32

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r33

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r34

## star_cfq/u_cfq_compound_divergence_0.02_0.6_r35

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r0

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r1

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r2

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r3

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r4

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r5

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r6

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r7

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r8

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r9

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r10

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r11

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r12

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r13

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r14

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r15

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r16

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r17

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r18

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r19

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r20

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r21

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r22

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r23

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r24

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r25

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r26

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r27

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r28

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r29

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r30

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r31

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r32

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r33

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r34

## star_cfq/u_cfq_compound_divergence_0.0333333_0_r35

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r0

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r1

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r2

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r3

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r4

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r5

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r6

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r7

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r8

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r9

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r10

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r11

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r12

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r13

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r14

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r15

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r16

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r17

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r18

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r19

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r20

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r21

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r22

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r23

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r24

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r25

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r26

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r27

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r28

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r29

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r30

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r31

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r32

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r33

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r34

## star_cfq/u_cfq_compound_divergence_0.0333333_0.1_r35

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r0

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r1

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r2

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r3

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r4

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r5

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r6

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r7

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r8

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r9

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r10

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r11

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r12

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r13

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r14

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r15

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r16

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r17

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r18

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r19

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r20

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r21

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r22

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r23

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r24

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r25

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r26

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r27

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r28

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r29

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r30

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r31

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r32

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r33

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r34

## star_cfq/u_cfq_compound_divergence_0.0333333_0.2_r35

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r0

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r1

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r2

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r3

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r4

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r5

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r6

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r7

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r8

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r9

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r10

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r11

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r12

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r13

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r14

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r15

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r16

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r17

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r18

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r19

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r20

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r21

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r22

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r23

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r24

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r25

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r26

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r27

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r28

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r29

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r30

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r31

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r32

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r33

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r34

## star_cfq/u_cfq_compound_divergence_0.0333333_0.3_r35

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r0

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r1

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r2

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r3

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r4

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r5

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r6

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r7

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r8

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r9

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r10

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r11

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r12

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r13

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r14

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r15

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r16

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r17

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r18

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r19

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r20

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r21

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r22

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r23

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r24

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r25

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r26

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r27

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r28

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r29

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r30

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r31

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r32

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r33

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r34

## star_cfq/u_cfq_compound_divergence_0.0333333_0.4_r35

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r0

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r1

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r2

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r3

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r4

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r5

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r6

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r7

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r8

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r9

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r10

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r11

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r12

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r13

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r14

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r15

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r16

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r17

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r18

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r19

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r20

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r21

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r22

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r23

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r24

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r25

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r26

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r27

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r28

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r29

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r30

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r31

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r32

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r33

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r34

## star_cfq/u_cfq_compound_divergence_0.0333333_0.5_r35

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r0

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r1

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r2

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r3

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r4

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r5

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r6

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r7

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r8

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r9

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r10

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r11

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r12

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r13

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r14

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r15

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r16

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r17

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r18

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r19

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r20

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r21

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r22

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r23

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r24

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r25

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r26

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r27

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r28

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r29

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r30

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r31

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r32

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r33

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r34

## star_cfq/u_cfq_compound_divergence_0.0333333_0.6_r35

## star_cfq/u_cfq_compound_divergence_0.1_0_r0

## star_cfq/u_cfq_compound_divergence_0.1_0_r1

## star_cfq/u_cfq_compound_divergence_0.1_0_r2

## star_cfq/u_cfq_compound_divergence_0.1_0_r3

## star_cfq/u_cfq_compound_divergence_0.1_0_r4

## star_cfq/u_cfq_compound_divergence_0.1_0_r5

## star_cfq/u_cfq_compound_divergence_0.1_0_r6

## star_cfq/u_cfq_compound_divergence_0.1_0_r7

## star_cfq/u_cfq_compound_divergence_0.1_0_r8

## star_cfq/u_cfq_compound_divergence_0.1_0_r9

## star_cfq/u_cfq_compound_divergence_0.1_0_r10

## star_cfq/u_cfq_compound_divergence_0.1_0_r11

## star_cfq/u_cfq_compound_divergence_0.1_0_r12

## star_cfq/u_cfq_compound_divergence_0.1_0_r13

## star_cfq/u_cfq_compound_divergence_0.1_0_r14

## star_cfq/u_cfq_compound_divergence_0.1_0_r15

## star_cfq/u_cfq_compound_divergence_0.1_0_r16

## star_cfq/u_cfq_compound_divergence_0.1_0_r17

## star_cfq/u_cfq_compound_divergence_0.1_0_r18

## star_cfq/u_cfq_compound_divergence_0.1_0_r19

## star_cfq/u_cfq_compound_divergence_0.1_0_r20

## star_cfq/u_cfq_compound_divergence_0.1_0_r21

## star_cfq/u_cfq_compound_divergence_0.1_0_r22

## star_cfq/u_cfq_compound_divergence_0.1_0_r23

## star_cfq/u_cfq_compound_divergence_0.1_0_r24

## star_cfq/u_cfq_compound_divergence_0.1_0_r25

## star_cfq/u_cfq_compound_divergence_0.1_0_r26

## star_cfq/u_cfq_compound_divergence_0.1_0_r27

## star_cfq/u_cfq_compound_divergence_0.1_0_r28

## star_cfq/u_cfq_compound_divergence_0.1_0_r29

## star_cfq/u_cfq_compound_divergence_0.1_0_r30

## star_cfq/u_cfq_compound_divergence_0.1_0_r31

## star_cfq/u_cfq_compound_divergence_0.1_0_r32

## star_cfq/u_cfq_compound_divergence_0.1_0_r33

## star_cfq/u_cfq_compound_divergence_0.1_0_r34

## star_cfq/u_cfq_compound_divergence_0.1_0_r35

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r0

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r1

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r2

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r3

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r4

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r5

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r6

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r7

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r8

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r9

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r10

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r11

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r12

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r13

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r14

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r15

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r16

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r17

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r18

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r19

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r20

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r21

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r22

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r23

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r24

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r25

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r26

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r27

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r28

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r29

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r30

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r31

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r32

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r33

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r34

## star_cfq/u_cfq_compound_divergence_0.1_0.1_r35

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r0

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r1

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r2

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r3

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r4

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r5

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r6

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r7

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r8

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r9

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r10

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r11

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r12

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r13

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r14

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r15

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r16

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r17

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r18

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r19

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r20

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r21

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r22

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r23

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r24

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r25

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r26

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r27

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r28

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r29

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r30

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r31

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r32

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r33

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r34

## star_cfq/u_cfq_compound_divergence_0.1_0.2_r35

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r0

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r1

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r2

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r3

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r4

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r5

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r6

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r7

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r8

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r9

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r10

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r11

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r12

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r13

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r14

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r15

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r16

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r17

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r18

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r19

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r20

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r21

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r22

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r23

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r24

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r25

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r26

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r27

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r28

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r29

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r30

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r31

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r32

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r33

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r34

## star_cfq/u_cfq_compound_divergence_0.1_0.3_r35

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r0

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r1

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r2

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r3

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r4

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r5

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r6

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r7

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r8

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r9

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r10

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r11

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r12

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r13

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r14

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r15

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r16

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r17

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r18

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r19

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r20

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r21

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r22

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r23

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r24

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r25

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r26

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r27

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r28

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r29

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r30

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r31

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r32

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r33

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r34

## star_cfq/u_cfq_compound_divergence_0.1_0.4_r35

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r0

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r1

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r2

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r3

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r4

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r5

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r6

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r7

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r8

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r9

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r10

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r11

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r12

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r13

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r14

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r15

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r16

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r17

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r18

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r19

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r20

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r21

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r22

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r23

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r24

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r25

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r26

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r27

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r28

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r29

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r30

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r31

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r32

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r33

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r34

## star_cfq/u_cfq_compound_divergence_0.1_0.5_r35

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r0

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r1

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r2

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r3

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r4

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r5

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r6

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r7

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r8

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r9

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r10

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r11

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r12

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r13

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r14

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r15

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r16

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r17

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r18

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r19

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r20

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r21

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r22

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r23

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r24

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r25

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r26

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r27

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r28

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r29

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r30

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r31

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r32

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r33

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r34

## star_cfq/u_cfq_compound_divergence_0.1_0.6_r35

## star_cfq/u_cfq_compound_divergence_0.2_0_r0

## star_cfq/u_cfq_compound_divergence_0.2_0_r1

## star_cfq/u_cfq_compound_divergence_0.2_0_r2

## star_cfq/u_cfq_compound_divergence_0.2_0_r3

## star_cfq/u_cfq_compound_divergence_0.2_0_r4

## star_cfq/u_cfq_compound_divergence_0.2_0_r5

## star_cfq/u_cfq_compound_divergence_0.2_0_r6

## star_cfq/u_cfq_compound_divergence_0.2_0_r7

## star_cfq/u_cfq_compound_divergence_0.2_0_r8

## star_cfq/u_cfq_compound_divergence_0.2_0_r9

## star_cfq/u_cfq_compound_divergence_0.2_0_r10

## star_cfq/u_cfq_compound_divergence_0.2_0_r11

## star_cfq/u_cfq_compound_divergence_0.2_0_r12

## star_cfq/u_cfq_compound_divergence_0.2_0_r13

## star_cfq/u_cfq_compound_divergence_0.2_0_r14

## star_cfq/u_cfq_compound_divergence_0.2_0_r15

## star_cfq/u_cfq_compound_divergence_0.2_0_r16

## star_cfq/u_cfq_compound_divergence_0.2_0_r17

## star_cfq/u_cfq_compound_divergence_0.2_0_r18

## star_cfq/u_cfq_compound_divergence_0.2_0_r19

## star_cfq/u_cfq_compound_divergence_0.2_0_r20

## star_cfq/u_cfq_compound_divergence_0.2_0_r21

## star_cfq/u_cfq_compound_divergence_0.2_0_r22

## star_cfq/u_cfq_compound_divergence_0.2_0_r23

## star_cfq/u_cfq_compound_divergence_0.2_0_r24

## star_cfq/u_cfq_compound_divergence_0.2_0_r25

## star_cfq/u_cfq_compound_divergence_0.2_0_r26

## star_cfq/u_cfq_compound_divergence_0.2_0_r27

## star_cfq/u_cfq_compound_divergence_0.2_0_r28

## star_cfq/u_cfq_compound_divergence_0.2_0_r29

## star_cfq/u_cfq_compound_divergence_0.2_0_r30

## star_cfq/u_cfq_compound_divergence_0.2_0_r31

## star_cfq/u_cfq_compound_divergence_0.2_0_r32

## star_cfq/u_cfq_compound_divergence_0.2_0_r33

## star_cfq/u_cfq_compound_divergence_0.2_0_r34

## star_cfq/u_cfq_compound_divergence_0.2_0_r35

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r0

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r1

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r2

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r3

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r4

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r5

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r6

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r7

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r8

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r9

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r10

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r11

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r12

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r13

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r14

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r15

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r16

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r17

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r18

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r19

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r20

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r21

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r22

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r23

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r24

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r25

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r26

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r27

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r28

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r29

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r30

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r31

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r32

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r33

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r34

## star_cfq/u_cfq_compound_divergence_0.2_0.1_r35

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r0

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r1

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r2

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r3

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r4

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r5

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r6

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r7

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r8

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r9

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r10

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r11

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r12

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r13

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r14

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r15

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r16

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r17

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r18

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r19

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r20

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r21

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r22

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r23

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r24

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r25

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r26

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r27

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r28

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r29

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r30

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r31

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r32

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r33

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r34

## star_cfq/u_cfq_compound_divergence_0.2_0.2_r35

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r0

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r1

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r2

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r3

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r4

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r5

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r6

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r7

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r8

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r9

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r10

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r11

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r12

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r13

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r14

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r15

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r16

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r17

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r18

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r19

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r20

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r21

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r22

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r23

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r24

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r25

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r26

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r27

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r28

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r29

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r30

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r31

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r32

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r33

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r34

## star_cfq/u_cfq_compound_divergence_0.2_0.3_r35

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r0

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r1

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r2

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r3

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r4

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r5

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r6

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r7

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r8

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r9

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r10

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r11

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r12

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r13

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r14

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r15

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r16

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r17

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r18

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r19

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r20

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r21

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r22

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r23

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r24

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r25

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r26

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r27

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r28

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r29

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r30

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r31

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r32

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r33

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r34

## star_cfq/u_cfq_compound_divergence_0.2_0.4_r35

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r0

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r1

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r2

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r3

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r4

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r5

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r6

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r7

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r8

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r9

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r10

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r11

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r12

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r13

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r14

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r15

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r16

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r17

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r18

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r19

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r20

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r21

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r22

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r23

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r24

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r25

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r26

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r27

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r28

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r29

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r30

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r31

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r32

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r33

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r34

## star_cfq/u_cfq_compound_divergence_0.2_0.5_r35

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r0

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r1

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r2

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r3

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r4

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r5

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r6

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r7

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r8

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r9

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r10

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r11

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r12

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r13

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r14

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r15

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r16

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r17

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r18

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r19

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r20

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r21

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r22

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r23

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r24

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r25

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r26

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r27

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r28

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r29

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r30

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r31

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r32

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r33

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r34

## star_cfq/u_cfq_compound_divergence_0.2_0.6_r35

## star_cfq/u_cfq_compound_divergence_0.333333_0_r0

## star_cfq/u_cfq_compound_divergence_0.333333_0_r1

## star_cfq/u_cfq_compound_divergence_0.333333_0_r2

## star_cfq/u_cfq_compound_divergence_0.333333_0_r3

## star_cfq/u_cfq_compound_divergence_0.333333_0_r4

## star_cfq/u_cfq_compound_divergence_0.333333_0_r5

## star_cfq/u_cfq_compound_divergence_0.333333_0_r6

## star_cfq/u_cfq_compound_divergence_0.333333_0_r7

## star_cfq/u_cfq_compound_divergence_0.333333_0_r8

## star_cfq/u_cfq_compound_divergence_0.333333_0_r9

## star_cfq/u_cfq_compound_divergence_0.333333_0_r10

## star_cfq/u_cfq_compound_divergence_0.333333_0_r11

## star_cfq/u_cfq_compound_divergence_0.333333_0_r12

## star_cfq/u_cfq_compound_divergence_0.333333_0_r13

## star_cfq/u_cfq_compound_divergence_0.333333_0_r14

## star_cfq/u_cfq_compound_divergence_0.333333_0_r15

## star_cfq/u_cfq_compound_divergence_0.333333_0_r16

## star_cfq/u_cfq_compound_divergence_0.333333_0_r17

## star_cfq/u_cfq_compound_divergence_0.333333_0_r18

## star_cfq/u_cfq_compound_divergence_0.333333_0_r19

## star_cfq/u_cfq_compound_divergence_0.333333_0_r20

## star_cfq/u_cfq_compound_divergence_0.333333_0_r21

## star_cfq/u_cfq_compound_divergence_0.333333_0_r22

## star_cfq/u_cfq_compound_divergence_0.333333_0_r23

## star_cfq/u_cfq_compound_divergence_0.333333_0_r24

## star_cfq/u_cfq_compound_divergence_0.333333_0_r25

## star_cfq/u_cfq_compound_divergence_0.333333_0_r26

## star_cfq/u_cfq_compound_divergence_0.333333_0_r27

## star_cfq/u_cfq_compound_divergence_0.333333_0_r28

## star_cfq/u_cfq_compound_divergence_0.333333_0_r29

## star_cfq/u_cfq_compound_divergence_0.333333_0_r30

## star_cfq/u_cfq_compound_divergence_0.333333_0_r31

## star_cfq/u_cfq_compound_divergence_0.333333_0_r32

## star_cfq/u_cfq_compound_divergence_0.333333_0_r33

## star_cfq/u_cfq_compound_divergence_0.333333_0_r34

## star_cfq/u_cfq_compound_divergence_0.333333_0_r35

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r0

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r1

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r2

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r3

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r4

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r5

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r6

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r7

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r8

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r9

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r10

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r11

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r12

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r13

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r14

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r15

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r16

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r17

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r18

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r19

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r20

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r21

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r22

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r23

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r24

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r25

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r26

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r27

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r28

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r29

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r30

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r31

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r32

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r33

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r34

## star_cfq/u_cfq_compound_divergence_0.333333_0.1_r35

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r0

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r1

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r2

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r3

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r4

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r5

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r6

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r7

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r8

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r9

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r10

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r11

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r12

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r13

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r14

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r15

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r16

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r17

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r18

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r19

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r20

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r21

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r22

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r23

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r24

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r25

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r26

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r27

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r28

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r29

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r30

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r31

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r32

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r33

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r34

## star_cfq/u_cfq_compound_divergence_0.333333_0.2_r35

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r0

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r1

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r2

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r3

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r4

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r5

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r6

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r7

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r8

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r9

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r10

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r11

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r12

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r13

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r14

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r15

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r16

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r17

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r18

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r19

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r20

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r21

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r22

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r23

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r24

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r25

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r26

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r27

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r28

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r29

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r30

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r31

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r32

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r33

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r34

## star_cfq/u_cfq_compound_divergence_0.333333_0.3_r35

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r0

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r1

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r2

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r3

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r4

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r5

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r6

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r7

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r8

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r9

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r10

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r11

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r12

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r13

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r14

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r15

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r16

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r17

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r18

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r19

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r20

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r21

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r22

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r23

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r24

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r25

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r26

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r27

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r28

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r29

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r30

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r31

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r32

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r33

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r34

## star_cfq/u_cfq_compound_divergence_0.333333_0.4_r35

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r0

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r1

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r2

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r3

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r4

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r5

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r6

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r7

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r8

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r9

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r10

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r11

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r12

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r13

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r14

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r15

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r16

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r17

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r18

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r19

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r20

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r21

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r22

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r23

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r24

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r25

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r26

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r27

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r28

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r29

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r30

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r31

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r32

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r33

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r34

## star_cfq/u_cfq_compound_divergence_0.333333_0.5_r35

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r0

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r1

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r2

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r3

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r4

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r5

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r6

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r7

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r8

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r9

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r10

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r11

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r12

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r13

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r14

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r15

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r16

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r17

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r18

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r19

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r20

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r21

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r22

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r23

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r24

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r25

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r26

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r27

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r28

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r29

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r30

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r31

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r32

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r33

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r34

## star_cfq/u_cfq_compound_divergence_0.333333_0.6_r35
