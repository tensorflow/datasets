<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="the300w_lp" />
  <meta itemprop="description" content="300W-LP Dataset is expanded from 300W, which standardises multiple alignment&#10;databases with 68 landmarks, including AFW, LFPW, HELEN, IBUG and XM2VTS. With&#10;300W, 300W-LP adopt the proposed face profiling to generate 61,225 samples&#10;across large poses (1,786 from IBUG, 5,207 from AFW, 16,556 from LFPW and 37,676&#10;from HELEN, XM2VTS is not used).&#10;&#10;The dataset can be employed as the training set for the following computer&#10;vision tasks: face attribute recognition and landmark (or facial part)&#10;localization.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;the300w_lp&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/the300w_lp-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/the300w_lp" />
  <meta itemprop="sameAs" content="http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/ZhuLLSL15,&#10;  author    = {Xiangyu Zhu and&#10;               Zhen Lei and&#10;               Xiaoming Liu and&#10;               Hailin Shi and&#10;               Stan Z. Li},&#10;  title     = {Face Alignment Across Large Poses: {A} 3D Solution},&#10;  journal   = {CoRR},&#10;  volume    = {abs/1511.07212},&#10;  year      = {2015},&#10;  url       = {http://arxiv.org/abs/1511.07212},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {1511.07212},&#10;  timestamp = {Mon, 13 Aug 2018 16:48:23 +0200},&#10;  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhuLLSL15},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `the300w_lp`


*   **Description**:

300W-LP Dataset is expanded from 300W, which standardises multiple alignment
databases with 68 landmarks, including AFW, LFPW, HELEN, IBUG and XM2VTS. With
300W, 300W-LP adopt the proposed face profiling to generate 61,225 samples
across large poses (1,786 from IBUG, 5,207 from AFW, 16,556 from LFPW and 37,676
from HELEN, XM2VTS is not used).

The dataset can be employed as the training set for the following computer
vision tasks: face attribute recognition and landmark (or facial part)
localization.

*   **Homepage**:
    [http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm](http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm)

*   **Source code**:
    [`tfds.datasets.the300w_lp.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/the300w_lp/the300w_lp_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): No release notes.

*   **Download size**: `2.63 GiB`

*   **Dataset size**: `1.33 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 61,225

*   **Feature structure**:

```python
FeaturesDict({
    'color_params': Tensor(shape=(7,), dtype=float32),
    'exp_params': Tensor(shape=(29,), dtype=float32),
    'illum_params': Tensor(shape=(10,), dtype=float32),
    'image': Image(shape=(450, 450, 3), dtype=uint8),
    'landmarks_2d': Tensor(shape=(68, 2), dtype=float32),
    'landmarks_3d': Tensor(shape=(68, 2), dtype=float32),
    'landmarks_origin': Tensor(shape=(68, 2), dtype=float32),
    'pose_params': Tensor(shape=(7,), dtype=float32),
    'roi': Tensor(shape=(4,), dtype=float32),
    'shape_params': Tensor(shape=(199,), dtype=float32),
    'tex_params': Tensor(shape=(199,), dtype=float32),
})
```

*   **Feature documentation**:

Feature          | Class        | Shape         | Dtype   | Description
:--------------- | :----------- | :------------ | :------ | :----------
                 | FeaturesDict |               |         |
color_params     | Tensor       | (7,)          | float32 |
exp_params       | Tensor       | (29,)         | float32 |
illum_params     | Tensor       | (10,)         | float32 |
image            | Image        | (450, 450, 3) | uint8   |
landmarks_2d     | Tensor       | (68, 2)       | float32 |
landmarks_3d     | Tensor       | (68, 2)       | float32 |
landmarks_origin | Tensor       | (68, 2)       | float32 |
pose_params      | Tensor       | (7,)          | float32 |
roi              | Tensor       | (4,)          | float32 |
shape_params     | Tensor       | (199,)        | float32 |
tex_params       | Tensor       | (199,)        | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/the300w_lp-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/the300w_lp-1.0.0.html";
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
@article{DBLP:journals/corr/ZhuLLSL15,
  author    = {Xiangyu Zhu and
               Zhen Lei and
               Xiaoming Liu and
               Hailin Shi and
               Stan Z. Li},
  title     = {Face Alignment Across Large Poses: {A} 3D Solution},
  journal   = {CoRR},
  volume    = {abs/1511.07212},
  year      = {2015},
  url       = {http://arxiv.org/abs/1511.07212},
  archivePrefix = {arXiv},
  eprint    = {1511.07212},
  timestamp = {Mon, 13 Aug 2018 16:48:23 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhuLLSL15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

