<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="s3_o4_d" />
  <meta itemprop="description" content="The dataset first described in the &quot;Stanford 3D Objects&quot;&#10;section of the paper [Disentangling by Subspace Diffusion](https://arxiv.org/abs/2006.12982).&#10;The data consists of 100,000 renderings each of the Bunny and Dragon objects&#10;from the [Stanford 3D Scanning Repository](http://graphics.stanford.edu/data/3Dscanrep/).&#10;More objects may be added in the future, but only the Bunny and Dragon are used&#10;in the paper. Each object is rendered with a uniformly sampled illumination from&#10;a point on the 2-sphere, and a uniformly sampled 3D rotation. The true latent&#10;states are provided as NumPy arrays along with the images. The lighting is given&#10;as a 3-vector with unit norm, while the rotation is provided both as a&#10;quaternion and a 3x3 orthogonal matrix.&#10;&#10;There are many similarities between S3O4D and existing ML benchmark datasets&#10;like [NORB](https://cs.nyu.edu/~ylclab/data/norb-v1.0/),&#10;[3D Chairs](https://github.com/mathieuaubry/seeing3Dchairs),&#10;[3D Shapes](https://github.com/deepmind/3d-shapes) and many others, which also&#10;include renderings of a set of objects under different pose and illumination&#10;conditions. However, none of these existing datasets include the *full manifold*&#10;of rotations in 3D - most include only a subset of changes to elevation and&#10;azimuth. S3O4D images are sampled uniformly and independently from the full space&#10;of rotations and illuminations, meaning the dataset contains objects that are&#10;upside down and illuminated from behind or underneath. We believe that this&#10;makes S3O4D uniquely suited for research on generative models where the latent&#10;space has non-trivial topology, as well as for general manifold learning&#10;methods where the curvature of the manifold is important.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;s3_o4_d&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/s3_o4_d-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/s3_o4_d" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/deepmind-research/tree/master/geomancer#stanford-3d-objects-for-disentangling-s3o4d" />
  <meta itemprop="citation" content="@article{pfau2020disentangling,&#10;  title={Disentangling by Subspace Diffusion},&#10;  author={Pfau, David and Higgins, Irina and Botev, Aleksandar and Racani\`ere,&#10;  S{\&#x27;e}bastian},&#10;  journal={Advances in Neural Information Processing Systems (NeurIPS)},&#10;  year={2020}&#10;}" />
</div>

# `s3_o4_d`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

The dataset first described in the "Stanford 3D Objects" section of the paper
[Disentangling by Subspace Diffusion](https://arxiv.org/abs/2006.12982). The
data consists of 100,000 renderings each of the Bunny and Dragon objects from
the
[Stanford 3D Scanning Repository](http://graphics.stanford.edu/data/3Dscanrep/).
More objects may be added in the future, but only the Bunny and Dragon are used
in the paper. Each object is rendered with a uniformly sampled illumination from
a point on the 2-sphere, and a uniformly sampled 3D rotation. The true latent
states are provided as NumPy arrays along with the images. The lighting is given
as a 3-vector with unit norm, while the rotation is provided both as a
quaternion and a 3x3 orthogonal matrix.

There are many similarities between S3O4D and existing ML benchmark datasets
like [NORB](https://cs.nyu.edu/~ylclab/data/norb-v1.0/),
[3D Chairs](https://github.com/mathieuaubry/seeing3Dchairs),
[3D Shapes](https://github.com/deepmind/3d-shapes) and many others, which also
include renderings of a set of objects under different pose and illumination
conditions. However, none of these existing datasets include the *full manifold*
of rotations in 3D - most include only a subset of changes to elevation and
azimuth. S3O4D images are sampled uniformly and independently from the full
space of rotations and illuminations, meaning the dataset contains objects that
are upside down and illuminated from behind or underneath. We believe that this
makes S3O4D uniquely suited for research on generative models where the latent
space has non-trivial topology, as well as for general manifold learning methods
where the curvature of the manifold is important.

*   **Homepage**:
    [https://github.com/deepmind/deepmind-research/tree/master/geomancer#stanford-3d-objects-for-disentangling-s3o4d](https://github.com/deepmind/deepmind-research/tree/master/geomancer#stanford-3d-objects-for-disentangling-s3o4d)

*   **Source code**:
    [`tfds.image.s3o4d.S3O4D`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/s3o4d/s3o4d.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `911.68 MiB`

*   **Dataset size**: `1.01 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split            | Examples
:--------------- | -------:
`'bunny_test'`   | 20,000
`'bunny_train'`  | 80,000
`'dragon_test'`  | 20,000
`'dragon_train'` | 80,000

*   **Features**:

```python
FeaturesDict({
    'illumination': Tensor(shape=(3,), dtype=tf.float32),
    'image': Image(shape=(256, 256, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=2),
    'pose_mat': Tensor(shape=(3, 3), dtype=tf.float32),
    'pose_quat': Tensor(shape=(4,), dtype=tf.float32),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Citation**:

```
@article{pfau2020disentangling,
  title={Disentangling by Subspace Diffusion},
  author={Pfau, David and Higgins, Irina and Botev, Aleksandar and Racani\`ere,
  S{\'e}bastian},
  journal={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2020}
}
```

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/s3_o4_d-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/s3_o4_d-1.0.0.html";
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