<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="s3o4d" />
  <meta itemprop="description" content="The dataset first described in the &quot;Stanford 3D Objects&quot; section of the paper&#10;[Disentangling by Subspace Diffusion](https://arxiv.org/abs/2006.12982). The&#10;data consists of 100,000 renderings each of the Bunny and Dragon objects from&#10;the&#10;[Stanford 3D Scanning Repository](http://graphics.stanford.edu/data/3Dscanrep/).&#10;More objects may be added in the future, but only the Bunny and Dragon are used&#10;in the paper. Each object is rendered with a uniformly sampled illumination from&#10;a point on the 2-sphere, and a uniformly sampled 3D rotation. The true latent&#10;states are provided as NumPy arrays along with the images. The lighting is given&#10;as a 3-vector with unit norm, while the rotation is provided both as a&#10;quaternion and a 3x3 orthogonal matrix.&#10;&#10;There are many similarities between S3O4D and existing ML benchmark datasets&#10;like [NORB](https://cs.nyu.edu/~ylclab/data/norb-v1.0/),&#10;[3D Chairs](https://github.com/mathieuaubry/seeing3Dchairs),&#10;[3D Shapes](https://github.com/deepmind/3d-shapes) and many others, which also&#10;include renderings of a set of objects under different pose and illumination&#10;conditions. However, none of these existing datasets include the *full manifold*&#10;of rotations in 3D - most include only a subset of changes to elevation and&#10;azimuth. S3O4D images are sampled uniformly and independently from the full&#10;space of rotations and illuminations, meaning the dataset contains objects that&#10;are upside down and illuminated from behind or underneath. We believe that this&#10;makes S3O4D uniquely suited for research on generative models where the latent&#10;space has non-trivial topology, as well as for general manifold learning methods&#10;where the curvature of the manifold is important.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;s3o4d&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/s3o4d-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/s3o4d" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/deepmind-research/tree/master/geomancer#stanford-3d-objects-for-disentangling-s3o4d" />
  <meta itemprop="citation" content="@article{pfau2020disentangling,&#10;  title={Disentangling by Subspace Diffusion},&#10;  author={Pfau, David and Higgins, Irina and Botev, Aleksandar and Racani\`ere,&#10;  S{\&#x27;e}bastian},&#10;  journal={Advances in Neural Information Processing Systems (NeurIPS)},&#10;  year={2020}&#10;}" />
</div>

# `s3o4d`


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

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/s3o4d">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://github.com/deepmind/deepmind-research/tree/master/geomancer#stanford-3d-objects-for-disentangling-s3o4d](https://github.com/deepmind/deepmind-research/tree/master/geomancer#stanford-3d-objects-for-disentangling-s3o4d)

*   **Source code**:
    [`tfds.datasets.s3o4d.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/s3o4d/s3o4d_dataset_builder.py)

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

*   **Feature structure**:

```python
FeaturesDict({
    'illumination': Tensor(shape=(3,), dtype=float32),
    'image': Image(shape=(256, 256, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=2),
    'pose_mat': Tensor(shape=(3, 3), dtype=float32),
    'pose_quat': Tensor(shape=(4,), dtype=float32),
})
```

*   **Feature documentation**:

Feature      | Class        | Shape         | Dtype   | Description
:----------- | :----------- | :------------ | :------ | :----------
             | FeaturesDict |               |         |
illumination | Tensor       | (3,)          | float32 |
image        | Image        | (256, 256, 3) | uint8   |
label        | ClassLabel   |               | int64   |
pose_mat     | Tensor       | (3, 3)        | float32 |
pose_quat    | Tensor       | (4,)          | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/s3o4d-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/s3o4d-1.0.0.html";
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
@article{pfau2020disentangling,
  title={Disentangling by Subspace Diffusion},
  author={Pfau, David and Higgins, Irina and Botev, Aleksandar and Racani\`ere,
  S{\'e}bastian},
  journal={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2020}
}
```

