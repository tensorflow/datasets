<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="chexpert" />
  <meta itemprop="description" content="CheXpert is a large dataset of chest X-rays and competition for automated chest &#10;x-ray interpretation, which features uncertainty labels and radiologist-labeled &#10;reference standard evaluation sets. It consists of 224,316 chest radiographs &#10;of 65,240 patients, where the chest radiographic examinations and the associated &#10;radiology reports were retrospectively collected from Stanford Hospital. Each &#10;report was labeled for the presence of 14 observations as positive, negative, &#10;or uncertain. We decided on the 14 observations based on the prevalence in the &#10;reports and clinical relevance.&#10;&#10;The CheXpert dataset must be downloaded separately after reading and agreeing &#10;to a Research Use Agreement. To do so, please follow the instructions on the &#10;website, https://stanfordmlgroup.github.io/competitions/chexpert/.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;chexpert&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/chexpert" />
  <meta itemprop="sameAs" content="https://stanfordmlgroup.github.io/competitions/chexpert/" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-1901-07031,&#10;  author    = {Jeremy Irvin and Pranav Rajpurkar and Michael Ko and Yifan Yu and Silviana Ciurea{-}Ilcus and Chris Chute and Henrik Marklund and Behzad Haghgoo and Robyn L. Ball and Katie Shpanskaya and Jayne Seekins and David A. Mong and Safwan S. Halabi and Jesse K. Sandberg and Ricky Jones and David B. Larson and Curtis P. Langlotz and Bhavik N. Patel and Matthew P. Lungren and Andrew Y. Ng},&#10;  title     = {CheXpert: {A} Large Chest Radiograph Dataset with Uncertainty Labels and Expert Comparison},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1901.07031},&#10;  year      = {2019},&#10;  url       = {http://arxiv.org/abs/1901.07031},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1901.07031},&#10;  timestamp = {Fri, 01 Feb 2019 13:39:59 +0100},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1901-07031},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `chexpert`

Warning: Manual download required. See instructions below.

*   **Description**:

CheXpert is a large dataset of chest X-rays and competition for automated chest
x-ray interpretation, which features uncertainty labels and radiologist-labeled
reference standard evaluation sets. It consists of 224,316 chest radiographs of
65,240 patients, where the chest radiographic examinations and the associated
radiology reports were retrospectively collected from Stanford Hospital. Each
report was labeled for the presence of 14 observations as positive, negative, or
uncertain. We decided on the 14 observations based on the prevalence in the
reports and clinical relevance.

The CheXpert dataset must be downloaded separately after reading and agreeing to
a Research Use Agreement. To do so, please follow the instructions on the
website, https://stanfordmlgroup.github.io/competitions/chexpert/.

*   **Homepage**:
    [https://stanfordmlgroup.github.io/competitions/chexpert/](https://stanfordmlgroup.github.io/competitions/chexpert/)

*   **Source code**:
    [`tfds.image_classification.Chexpert`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/chexpert.py)

*   **Versions**:

    *   **`3.1.0`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    You must register and agree to user agreement on the dataset page:
    https://stanfordmlgroup.github.io/competitions/chexpert/
    Afterwards, you have to put the CheXpert-v1.0-small directory in the
    manual_dir. It should contain subdirectories: train/ and valid/ with images
    and also train.csv and valid.csv files.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'image_view': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'label': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=4)),
    'name': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{DBLP:journals/corr/abs-1901-07031,
  author    = {Jeremy Irvin and Pranav Rajpurkar and Michael Ko and Yifan Yu and Silviana Ciurea{-}Ilcus and Chris Chute and Henrik Marklund and Behzad Haghgoo and Robyn L. Ball and Katie Shpanskaya and Jayne Seekins and David A. Mong and Safwan S. Halabi and Jesse K. Sandberg and Ricky Jones and David B. Larson and Curtis P. Langlotz and Bhavik N. Patel and Matthew P. Lungren and Andrew Y. Ng},
  title     = {CheXpert: {A} Large Chest Radiograph Dataset with Uncertainty Labels and Expert Comparison},
  journal   = {CoRR},
  volume    = {abs/1901.07031},
  year      = {2019},
  url       = {http://arxiv.org/abs/1901.07031},
  archivePrefix = {arXiv},
  eprint    = {1901.07031},
  timestamp = {Fri, 01 Feb 2019 13:39:59 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1901-07031},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
