<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="assin2" />
  <meta itemprop="description" content="## Contextualization&#10;&#10;ASSIN 2 is the second edition of the Avaliação de Similaridade Semântica e&#10;Inferência Textual (Evaluating Semantic Similarity and Textual Entailment), and&#10;was a workshop collocated with&#10;[STIL 2019](http://www.google.com/url?q=http%3A%2F%2Fcomissoes.sbc.org.br%2Fce-pln%2Fstil2019%2F&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNHN8DosAsJ-gd48TfkXFX5YD6xM7g).&#10;It follows the&#10;[first edition of ASSIN](http://www.google.com/url?q=http%3A%2F%2Fpropor2016.di.fc.ul.pt%2F%3Fpage_id%3D381&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNHV7ySeNzH4k6MWKBLqO9yUkqiUqw),&#10;proposing a new shared task with new data.&#10;&#10;The workshop evaluated systems that assess two types of relations between two&#10;sentences: Semantic Textual Similarity and Textual Entailment.&#10;&#10;Semantic Textual Similarity consists of quantifying the level of semantic&#10;equivalence between sentences, while Textual Entailment Recognition consists of&#10;classifying whether the first sentence entails the second.&#10;&#10;## Data&#10;&#10;The corpus used in ASSIN 2 is composed of rather simple sentences. Following the&#10;procedures of SemEval 2014 Task 1, we tried to remove from the corpus named&#10;entities and indirect speech, and tried to have all verbs in the present tense.&#10;The&#10;[annotation instructions](https://drive.google.com/open?id=1aUPhywEHD0r_pxPiTqZwS0fRj-1Xda2w)&#10;given to annotators are available (in Portuguese).&#10;&#10;The training and validation data are composed, respectively, of 6,500 and 500&#10;sentence pairs in Brazilian Portuguese, annotated for entailment and semantic&#10;similarity. Semantic similarity values range from 1 to 5, and text entailment&#10;classes are either entailment or none. The test data are composed of&#10;approximately 3,000 sentence pairs with the same annotation. All data were&#10;manually annotated.&#10;&#10;## Evaluation&#10;&#10;Evaluation The evaluation of submissions to ASSIN 2 was with the same metrics as&#10;the first ASSIN, with the F1 of precision and recall as the main metric for text&#10;entailment and Pearson correlation for semantic similarity. The&#10;[evaluation scripts](https://github.com/erickrf/assin) are the same as in the&#10;last edition.&#10;&#10;PS.: Description is extracted from&#10;[official homepage](https://sites.google.com/view/assin2/english).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;assin2&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/assin2" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/assin2/english" />
  <meta itemprop="citation" content="@inproceedings{DBLP:conf/propor/RealFO20,&#10;  author    = {Livy Real and&#10;               Erick Fonseca and&#10;               Hugo Gon{\c{c}}alo Oliveira},&#10;  editor    = {Paulo Quaresma and&#10;               Renata Vieira and&#10;               Sandra M. Alu{\&#x27;{\i}}sio and&#10;               Helena Moniz and&#10;               Fernando Batista and&#10;               Teresa Gon{\c{c}}alves},&#10;  title     = {The {ASSIN} 2 Shared Task: {A} Quick Overview},&#10;  booktitle = {Computational Processing of the Portuguese Language - 14th International&#10;               Conference, {PROPOR} 2020, Evora, Portugal, March 2-4, 2020, Proceedings},&#10;  series    = {Lecture Notes in Computer Science},&#10;  volume    = {12037},&#10;  pages     = {406--412},&#10;  publisher = {Springer},&#10;  year      = {2020},&#10;  url       = {https://doi.org/10.1007/978-3-030-41505-1_39},&#10;  doi       = {10.1007/978-3-030-41505-1_39},&#10;  timestamp = {Tue, 03 Mar 2020 09:40:18 +0100},&#10;  biburl    = {https://dblp.org/rec/conf/propor/RealFO20.bib},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `assin2`


*   **Description**:

## Contextualization

ASSIN 2 is the second edition of the Avaliação de Similaridade Semântica e
Inferência Textual (Evaluating Semantic Similarity and Textual Entailment), and
was a workshop collocated with
[STIL 2019](http://www.google.com/url?q=http%3A%2F%2Fcomissoes.sbc.org.br%2Fce-pln%2Fstil2019%2F&sa=D&sntz=1&usg=AFQjCNHN8DosAsJ-gd48TfkXFX5YD6xM7g).
It follows the
[first edition of ASSIN](http://www.google.com/url?q=http%3A%2F%2Fpropor2016.di.fc.ul.pt%2F%3Fpage_id%3D381&sa=D&sntz=1&usg=AFQjCNHV7ySeNzH4k6MWKBLqO9yUkqiUqw),
proposing a new shared task with new data.

The workshop evaluated systems that assess two types of relations between two
sentences: Semantic Textual Similarity and Textual Entailment.

Semantic Textual Similarity consists of quantifying the level of semantic
equivalence between sentences, while Textual Entailment Recognition consists of
classifying whether the first sentence entails the second.

## Data

The corpus used in ASSIN 2 is composed of rather simple sentences. Following the
procedures of SemEval 2014 Task 1, we tried to remove from the corpus named
entities and indirect speech, and tried to have all verbs in the present tense.
The
[annotation instructions](https://drive.google.com/open?id=1aUPhywEHD0r_pxPiTqZwS0fRj-1Xda2w)
given to annotators are available (in Portuguese).

The training and validation data are composed, respectively, of 6,500 and 500
sentence pairs in Brazilian Portuguese, annotated for entailment and semantic
similarity. Semantic similarity values range from 1 to 5, and text entailment
classes are either entailment or none. The test data are composed of
approximately 3,000 sentence pairs with the same annotation. All data were
manually annotated.

## Evaluation

Evaluation The evaluation of submissions to ASSIN 2 was with the same metrics as
the first ASSIN, with the F1 of precision and recall as the main metric for text
entailment and Pearson correlation for semantic similarity. The
[evaluation scripts](https://github.com/erickrf/assin) are the same as in the
last edition.

PS.: Description is extracted from
[official homepage](https://sites.google.com/view/assin2/english).

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/assin2">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://sites.google.com/view/assin2/english](https://sites.google.com/view/assin2/english)

*   **Source code**:
    [`tfds.datasets.assin2.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/assin2/assin2_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `2.02 MiB`

*   **Dataset size**: `1.82 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,448
`'train'`      | 6,500
`'validation'` | 500

*   **Feature structure**:

```python
FeaturesDict({
    'entailment': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'hypothesis': Text(shape=(), dtype=string),
    'id': int32,
    'similarity': float32,
    'text': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature    | Class        | Shape | Dtype   | Description
:--------- | :----------- | :---- | :------ | :----------
           | FeaturesDict |       |         |
entailment | ClassLabel   |       | int64   |
hypothesis | Text         |       | string  |
id         | Tensor       |       | int32   |
similarity | Tensor       |       | float32 |
text       | Text         |       | string  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/assin2-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{DBLP:conf/propor/RealFO20,
  author    = {Livy Real and
               Erick Fonseca and
               Hugo Gon{\c{c}}alo Oliveira},
  editor    = {Paulo Quaresma and
               Renata Vieira and
               Sandra M. Alu{\'{\i}}sio and
               Helena Moniz and
               Fernando Batista and
               Teresa Gon{\c{c}}alves},
  title     = {The {ASSIN} 2 Shared Task: {A} Quick Overview},
  booktitle = {Computational Processing of the Portuguese Language - 14th International
               Conference, {PROPOR} 2020, Evora, Portugal, March 2-4, 2020, Proceedings},
  series    = {Lecture Notes in Computer Science},
  volume    = {12037},
  pages     = {406--412},
  publisher = {Springer},
  year      = {2020},
  url       = {https://doi.org/10.1007/978-3-030-41505-1_39},
  doi       = {10.1007/978-3-030-41505-1_39},
  timestamp = {Tue, 03 Mar 2020 09:40:18 +0100},
  biburl    = {https://dblp.org/rec/conf/propor/RealFO20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

