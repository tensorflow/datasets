<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="reddit_disentanglement" />
  <meta itemprop="description" content="This dataset contains ~3M messages from reddit. Every message is labeled with&#10;metadata. The task is to predict the id of its parent message in the&#10;corresponding thread. Each record contains a list of messages from one thread.&#10;Duplicated and broken records are removed from the dataset.&#10;&#10;Features are:&#10;&#10;- id - message id&#10;- text - message text&#10;- author - message author&#10;- created_utc - message UTC timestamp&#10;- link_id - id of the post that the comment relates to&#10;&#10;Target:&#10;&#10;- parent_id - id of the parent message in the current&#10;thread&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;reddit_disentanglement&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/reddit_disentanglement" />
  <meta itemprop="sameAs" content="https://github.com/henghuiz/MaskedHierarchicalTransformer" />
  <meta itemprop="citation" content="@article{zhu2019did,&#10;  title={Who did They Respond to? Conversation Structure Modeling using Masked Hierarchical Transformer},&#10;  author={Zhu, Henghui and Nan, Feng and Wang, Zhiguo and Nallapati, Ramesh and Xiang, Bing},&#10;  journal={arXiv preprint arXiv:1911.10666},&#10;  year={2019}&#10;}" />
</div>

# `reddit_disentanglement`


Warning: Manual download required. See instructions below.

*   **Description**:

This dataset contains ~3M messages from reddit. Every message is labeled with
metadata. The task is to predict the id of its parent message in the
corresponding thread. Each record contains a list of messages from one thread.
Duplicated and broken records are removed from the dataset.

Features are:

-   id - message id
-   text - message text
-   author - message author
-   created_utc - message UTC timestamp
-   link_id - id of the post that the comment relates to

Target:

-   parent_id - id of the parent message in the current thread

*   **Homepage**:
    [https://github.com/henghuiz/MaskedHierarchicalTransformer](https://github.com/henghuiz/MaskedHierarchicalTransformer)

*   **Source code**:
    [`tfds.datasets.reddit_disentanglement.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/reddit_disentanglement/reddit_disentanglement_dataset_builder.py)

*   **Versions**:

    *   **`2.0.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Download https://github.com/henghuiz/MaskedHierarchicalTransformer, decompress
    raw_data.zip and run generate_dataset.py with your reddit api credentials.
    Then put train.csv, val.csv and test.csv from the output directory into the
    manual folder.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'thread': Sequence({
        'author': Text(shape=(), dtype=string),
        'created_utc': Text(shape=(), dtype=string),
        'id': Text(shape=(), dtype=string),
        'link_id': Text(shape=(), dtype=string),
        'parent_id': Text(shape=(), dtype=string),
        'text': Text(shape=(), dtype=string),
    }),
})
```

*   **Feature documentation**:

Feature            | Class        | Shape | Dtype  | Description
:----------------- | :----------- | :---- | :----- | :----------
                   | FeaturesDict |       |        |
thread             | Sequence     |       |        |
thread/author      | Text         |       | string |
thread/created_utc | Text         |       | string |
thread/id          | Text         |       | string |
thread/link_id     | Text         |       | string |
thread/parent_id   | Text         |       | string |
thread/text        | Text         |       | string |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{zhu2019did,
  title={Who did They Respond to? Conversation Structure Modeling using Masked Hierarchical Transformer},
  author={Zhu, Henghui and Nan, Feng and Wang, Zhiguo and Nallapati, Ramesh and Xiang, Bing},
  journal={arXiv preprint arXiv:1911.10666},
  year={2019}
}
```

