<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="movie_rationales" />
  <meta itemprop="description" content="The movie rationale dataset contains human annotated rationales for movie&#10;reviews.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;movie_rationales&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/movie_rationales" />
  <meta itemprop="sameAs" content="http://www.cs.jhu.edu/~ozaidan/rationales/" />
  <meta itemprop="citation" content="@unpublished{eraser2019,&#10;    title = {ERASER: A Benchmark to Evaluate Rationalized NLP Models},&#10;    author = {Jay DeYoung and Sarthak Jain and Nazneen Fatema Rajani and Eric Lehman and Caiming Xiong and Richard Socher and Byron C. Wallace}&#10;}&#10;@InProceedings{zaidan-eisner-piatko-2008:nips,&#10;  author    =  {Omar F. Zaidan  and  Jason Eisner  and  Christine Piatko},&#10;  title     =  {Machine Learning with Annotator Rationales to Reduce Annotation Cost},&#10;  booktitle =  {Proceedings of the NIPS*2008 Workshop on Cost Sensitive Learning},&#10;  month     =  {December},&#10;  year      =  {2008}&#10;}" />
</div>

# `movie_rationales`


*   **Description**:

The movie rationale dataset contains human annotated rationales for movie
reviews.

*   **Homepage**:
    [http://www.cs.jhu.edu/~ozaidan/rationales/](http://www.cs.jhu.edu/~ozaidan/rationales/)

*   **Source code**:
    [`tfds.text.MovieRationales`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/movie_rationales.py)

*   **Versions**:

    *   **`0.1.0`** (default): No release notes.

*   **Download size**: `3.72 MiB`

*   **Dataset size**: `8.37 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 199
`'train'`      | 1,600
`'validation'` | 200

*   **Feature structure**:

```python
FeaturesDict({
    'evidences': Sequence(Text(shape=(), dtype=string)),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'review': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature   | Class          | Shape   | Dtype  | Description
:-------- | :------------- | :------ | :----- | :----------
          | FeaturesDict   |         |        |
evidences | Sequence(Text) | (None,) | string |
label     | ClassLabel     |         | int64  |
review    | Text           |         | string |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/movie_rationales-0.1.0.html";
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
@unpublished{eraser2019,
    title = {ERASER: A Benchmark to Evaluate Rationalized NLP Models},
    author = {Jay DeYoung and Sarthak Jain and Nazneen Fatema Rajani and Eric Lehman and Caiming Xiong and Richard Socher and Byron C. Wallace}
}
@InProceedings{zaidan-eisner-piatko-2008:nips,
  author    =  {Omar F. Zaidan  and  Jason Eisner  and  Christine Piatko},
  title     =  {Machine Learning with Annotator Rationales to Reduce Annotation Cost},
  booktitle =  {Proceedings of the NIPS*2008 Workshop on Cost Sensitive Learning},
  month     =  {December},
  year      =  {2008}
}
```

