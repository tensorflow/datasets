<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="genomics_ood" />
  <meta itemprop="description" content="Bacteria identification based on genomic sequences holds the promise of early&#10;detection of diseases, but requires a model that can output low confidence&#10;predictions on out-of-distribution (OOD) genomic sequences from new bacteria&#10;that were not present in the training data.&#10;&#10;We introduce a genomics dataset for OOD detection that allows other researchers&#10;to benchmark progress on this important problem. New bacterial classes are&#10;gradually discovered over the years. Grouping classes by years is a natural way&#10;to mimic the in-distribution and OOD examples.&#10;&#10;The dataset contains genomic sequences sampled from 10 bacteria classes that&#10;were discovered before the year 2011 as in-distribution classes, 60 bacteria&#10;classes discovered between 2011-2016 as OOD for validation, and another 60&#10;different bacteria classes discovered after 2016 as OOD for test, in total 130&#10;bacteria classes. Note that training, validation, and test data are provided for&#10;the in-distribution classes, and validation and test data are proviede for OOD&#10;classes. By its nature, OOD data is not available at the training time.&#10;&#10;The genomic sequence is 250 long, composed by characters of {A, C, G, T}. The&#10;sample size of each class is 100,000 in the training and 10,000 for the&#10;validation and test sets.&#10;&#10;For each example, the features include:&#10;  seq: the input DNA sequence composed by {A, C, G, T}.&#10;  label: the name of the bacteria class.&#10;  seq_info: the source of the DNA sequence, i.e., the genome name, NCBI&#10;  accession number, and the position where it was sampled from.&#10;  domain: if the bacteria is in-distribution (in), or OOD (ood)&#10;&#10;The details of the dataset can be found in the paper supplemental.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;genomics_ood&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/genomics_ood" />
  <meta itemprop="sameAs" content="https://github.com/google-research/google-research/tree/master/genomics_ood" />
  <meta itemprop="citation" content="@inproceedings{ren2019likelihood,&#10;  title={Likelihood ratios for out-of-distribution detection},&#10;  author={Ren, Jie and&#10;  Liu, Peter J and&#10;  Fertig, Emily and&#10;  Snoek, Jasper and&#10;  Poplin, Ryan and&#10;  Depristo, Mark and&#10;  Dillon, Joshua and&#10;  Lakshminarayanan, Balaji},&#10;  booktitle={Advances in Neural Information Processing Systems},&#10;  pages={14707--14718},&#10;  year={2019}&#10;}" />
</div>

# `genomics_ood`


*   **Description**:

Bacteria identification based on genomic sequences holds the promise of early
detection of diseases, but requires a model that can output low confidence
predictions on out-of-distribution (OOD) genomic sequences from new bacteria
that were not present in the training data.

We introduce a genomics dataset for OOD detection that allows other researchers
to benchmark progress on this important problem. New bacterial classes are
gradually discovered over the years. Grouping classes by years is a natural way
to mimic the in-distribution and OOD examples.

The dataset contains genomic sequences sampled from 10 bacteria classes that
were discovered before the year 2011 as in-distribution classes, 60 bacteria
classes discovered between 2011-2016 as OOD for validation, and another 60
different bacteria classes discovered after 2016 as OOD for test, in total 130
bacteria classes. Note that training, validation, and test data are provided for
the in-distribution classes, and validation and test data are proviede for OOD
classes. By its nature, OOD data is not available at the training time.

The genomic sequence is 250 long, composed by characters of {A, C, G, T}. The
sample size of each class is 100,000 in the training and 10,000 for the
validation and test sets.

For each example, the features include: seq: the input DNA sequence composed by
{A, C, G, T}. label: the name of the bacteria class. seq_info: the source of the
DNA sequence, i.e., the genome name, NCBI accession number, and the position
where it was sampled from. domain: if the bacteria is in-distribution (in), or
OOD (ood)

The details of the dataset can be found in the paper supplemental.

*   **Homepage**:
    [https://github.com/google-research/google-research/tree/master/genomics_ood](https://github.com/google-research/google-research/tree/master/genomics_ood)

*   **Source code**:
    [`tfds.structured.GenomicsOod`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/structured/genomics_ood.py)

*   **Versions**:

    *   **`0.0.1`** (default): No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `926.87 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split              | Examples
:----------------- | --------:
`'test'`           | 100,000
`'test_ood'`       | 600,000
`'train'`          | 1,000,000
`'validation'`     | 100,000
`'validation_ood'` | 600,000

*   **Features**:

```python
FeaturesDict({
    'domain': Text(shape=(), dtype=tf.string),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=130),
    'seq': Text(shape=(), dtype=tf.string),
    'seq_info': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('seq', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/genomics_ood-0.0.1.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ren2019likelihood,
  title={Likelihood ratios for out-of-distribution detection},
  author={Ren, Jie and
  Liu, Peter J and
  Fertig, Emily and
  Snoek, Jasper and
  Poplin, Ryan and
  Depristo, Mark and
  Dillon, Joshua and
  Lakshminarayanan, Balaji},
  booktitle={Advances in Neural Information Processing Systems},
  pages={14707--14718},
  year={2019}
}
```
