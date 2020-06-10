<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="irc_disentanglement" />
  <meta itemprop="description" content="IRC Disentanglement dataset contains over 77,563 messages from Ubuntu IRC&#10;channel.&#10;&#10;Features include message id, message text and timestamp.&#10;Target is list of messages that current message replies to.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;irc_disentanglement&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/irc_disentanglement" />
  <meta itemprop="sameAs" content="https://jkk.name/irc-disentanglement" />
  <meta itemprop="citation" content="@InProceedings{acl19disentangle,&#10;  author    = {Jonathan K. Kummerfeld and Sai R. Gouravajhala and Joseph Peper and Vignesh Athreya and Chulaka Gunasekara and Jatin Ganhotra and Siva Sankalp Patel and Lazaros Polymenakos and Walter S. Lasecki},&#10;  title     = {A Large-Scale Corpus for Conversation Disentanglement},&#10;  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},&#10;  location  = {Florence, Italy},&#10;  month     = {July},&#10;  year      = {2019},&#10;  doi       = {10.18653/v1/P19-1374},&#10;  pages     = {3846--3856},&#10;  url       = {https://aclweb.org/anthology/papers/P/P19/P19-1374/},&#10;  arxiv     = {https://arxiv.org/abs/1810.11118},&#10;  software  = {https://jkk.name/irc-disentanglement},&#10;  data      = {https://jkk.name/irc-disentanglement},&#10;}" />
</div>

# `irc_disentanglement`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

IRC Disentanglement dataset contains over 77,563 messages from Ubuntu IRC
channel.

Features include message id, message text and timestamp. Target is list of
messages that current message replies to.

*   **Homepage**:
    [https://jkk.name/irc-disentanglement](https://jkk.name/irc-disentanglement)
*   **Source code**:
    [`tfds.text.irc_disentanglement.IrcDisentanglement`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/irc_disentanglement.py)
*   **Versions**:
    *   **`1.0.0`** (default): No release notes.
*   **Download size**: `113.53 MiB`
*   **Dataset size**: `39.84 MiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes
*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 15,000
'train'      | 220,463
'validation' | 12,500

*   **Features**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=tf.string),
    'parents': Sequence(Text(shape=(), dtype=tf.string)),
    'text': Text(shape=(), dtype=tf.string),
    'timestamp': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`
*   **Citation**:

```
@InProceedings{acl19disentangle,
  author    = {Jonathan K. Kummerfeld and Sai R. Gouravajhala and Joseph Peper and Vignesh Athreya and Chulaka Gunasekara and Jatin Ganhotra and Siva Sankalp Patel and Lazaros Polymenakos and Walter S. Lasecki},
  title     = {A Large-Scale Corpus for Conversation Disentanglement},
  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  location  = {Florence, Italy},
  month     = {July},
  year      = {2019},
  doi       = {10.18653/v1/P19-1374},
  pages     = {3846--3856},
  url       = {https://aclweb.org/anthology/papers/P/P19/P19-1374/},
  arxiv     = {https://arxiv.org/abs/1810.11118},
  software  = {https://jkk.name/irc-disentanglement},
  data      = {https://jkk.name/irc-disentanglement},
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.
