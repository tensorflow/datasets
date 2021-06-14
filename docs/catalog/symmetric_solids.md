<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="symmetric_solids" />
  <meta itemprop="description" content="This is a pose estimation dataset, consisting of symmetric 3D shapes where &#10;multiple orientations are visually indistinguishable. &#10;The challenge is to predict all equivalent orientations when only one &#10;orientation is paired with each image during training (as is the scenario for &#10;most pose estimation datasets). In contrast to most pose estimation datasets, &#10;the full set of equivalent orientations is available for evaluation.&#10;&#10;There are eight shapes total, each rendered from 50,000 viewpoints distributed &#10;uniformly at random over the full space of 3D rotations.&#10;Five of the shapes are featureless -- tetrahedron, cube, icosahedron, cone, and &#10;cylinder.&#10;Of those, the three Platonic solids (tetrahedron, cube, icosahedron) are &#10;annotated with their 12-, 24-, and 60-fold discrete symmetries, respectively.&#10;The cone and cylinder are annotated with their continuous symmetries discretized&#10; at 1 degree intervals. These symmetries are provided for evaluation; the &#10; intended supervision is only a single rotation with each image.&#10;&#10;The remaining three shapes are marked with a distinguishing feature.&#10;There is a tetrahedron with one red-colored face, a cylinder with an off-center &#10;dot, and a sphere with an X capped by a dot. Whether or not the distinguishing &#10;feature is visible, the space of possible orientations is reduced.  We do not &#10;provide the set of equivalent rotations for these shapes.&#10;&#10;Each example contains of &#10;&#10;- the 224x224 RGB image&#10;- a shape index so that the dataset may be filtered by shape.  &#10;The indices correspond to: &#10;&#10;  - 0 = tetrahedron&#10;  - 1 = cube&#10;  - 2 = icosahedron&#10;  - 3 = cone&#10;  - 4 = cylinder&#10;  - 5 = marked tetrahedron&#10;  - 6 = marked cylinder&#10;  - 7 = marked sphere&#10;&#10;- the rotation used in the rendering process, represented as a 3x3 rotation matrix&#10;- the set of known equivalent rotations under symmetry, for evaluation.  &#10;&#10;In the case of the three marked shapes, this is only the rendering rotation.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;symmetric_solids&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/symmetric_solids-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/symmetric_solids" />
  <meta itemprop="sameAs" content="https://implicit-pdf.github.io" />
  <meta itemprop="citation" content="@inproceedings{implicitpdf2021,&#10;  title = {Implicit Representation of Probability Distributions on the Rotation &#10;  Manifold},&#10;  author = {Murphy, Kieran and Esteves, Carlos and Jampani, Varun and &#10;  Ramalingam, Srikumar and Makadia, Ameesh}&#10;  booktitle = {International Conference on Machine Learning}&#10;  year = {2021}&#10;}" />
</div>

# `symmetric_solids`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

This is a pose estimation dataset, consisting of symmetric 3D shapes where
multiple orientations are visually indistinguishable. The challenge is to
predict all equivalent orientations when only one orientation is paired with
each image during training (as is the scenario for most pose estimation
datasets). In contrast to most pose estimation datasets, the full set of
equivalent orientations is available for evaluation.

There are eight shapes total, each rendered from 50,000 viewpoints distributed
uniformly at random over the full space of 3D rotations. Five of the shapes are
featureless -- tetrahedron, cube, icosahedron, cone, and cylinder. Of those, the
three Platonic solids (tetrahedron, cube, icosahedron) are annotated with their
12-, 24-, and 60-fold discrete symmetries, respectively. The cone and cylinder
are annotated with their continuous symmetries discretized at 1 degree
intervals. These symmetries are provided for evaluation; the intended
supervision is only a single rotation with each image.

The remaining three shapes are marked with a distinguishing feature. There is a
tetrahedron with one red-colored face, a cylinder with an off-center dot, and a
sphere with an X capped by a dot. Whether or not the distinguishing feature is
visible, the space of possible orientations is reduced. We do not provide the
set of equivalent rotations for these shapes.

Each example contains of

-   the 224x224 RGB image
-   a shape index so that the dataset may be filtered by shape. \
    The indices correspond to:

    -   0 = tetrahedron
    -   1 = cube
    -   2 = icosahedron
    -   3 = cone
    -   4 = cylinder
    -   5 = marked tetrahedron
    -   6 = marked cylinder
    -   7 = marked sphere

-   the rotation used in the rendering process, represented as a 3x3 rotation
    matrix

-   the set of known equivalent rotations under symmetry, for evaluation.

In the case of the three marked shapes, this is only the rendering rotation.

*   **Homepage**:
    [https://implicit-pdf.github.io](https://implicit-pdf.github.io)

*   **Source code**:
    [`tfds.image.symmetric_solids.SymmetricSolids`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/symmetric_solids/symmetric_solids.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `3.10 GiB`

*   **Dataset size**: `3.94 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 40,000
`'train'` | 360,000

*   **Features**:

```python
FeaturesDict({
    'image': Image(shape=(224, 224, 3), dtype=tf.uint8),
    'label_shape': ClassLabel(shape=(), dtype=tf.int64, num_classes=8),
    'rotation': Tensor(shape=(3, 3), dtype=tf.float32),
    'rotations_equivalent': Tensor(shape=(None, 3, 3), dtype=tf.float32),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'rotation')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/symmetric_solids-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/symmetric_solids-1.0.0.html";
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
@inproceedings{implicitpdf2021,
  title = {Implicit Representation of Probability Distributions on the Rotation
  Manifold},
  author = {Murphy, Kieran and Esteves, Carlos and Jampani, Varun and
  Ramalingam, Srikumar and Makadia, Ameesh}
  booktitle = {International Conference on Machine Learning}
  year = {2021}
}
```
