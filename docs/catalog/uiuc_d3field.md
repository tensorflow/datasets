<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="uiuc_d3field" />
  <meta itemprop="description" content="Organizing office desk, utensils etc&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;uiuc_d3field&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/uiuc_d3field" />
  <meta itemprop="sameAs" content="https://robopil.github.io/d3fields/" />
  <meta itemprop="citation" content="@article{wang2023d3field,&#10;  title={D^3Field: Dynamic 3D Descriptor Fields for Generalizable Robotic Manipulation}, &#10;  author={Wang, Yixuan and Li, Zhuoran and Zhang, Mingtong and Driggs-Campbell, Katherine and Wu, Jiajun and Fei-Fei, Li and Li, Yunzhu},&#10;  journal={arXiv preprint arXiv:},&#10;  year={2023},&#10;}" />
</div>

# `uiuc_d3field`


*   **Description**:

Organizing office desk, utensils etc

*   **Homepage**:
    [https://robopil.github.io/d3fields/](https://robopil.github.io/d3fields/)

*   **Source code**:
    [`tfds.robotics.rtx.UiucD3field`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `15.82 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 192

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(3,), dtype=float32, description=Robot displacement from last frame),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'depth_1': Image(shape=(360, 640, 1), dtype=uint16, description=camera 1 depth observation.),
            'depth_2': Image(shape=(360, 640, 1), dtype=uint16, description=camera 2 depth observation.),
            'depth_3': Image(shape=(360, 640, 1), dtype=uint16, description=camera 3 depth observation.),
            'depth_4': Image(shape=(360, 640, 1), dtype=uint16, description=camera 4 depth observation.),
            'image_1': Image(shape=(360, 640, 3), dtype=uint8, description=camera 1 RGB observation.),
            'image_2': Image(shape=(360, 640, 3), dtype=uint8, description=camera 2 RGB observation.),
            'image_3': Image(shape=(360, 640, 3), dtype=uint8, description=camera 3 RGB observation.),
            'image_4': Image(shape=(360, 640, 3), dtype=uint8, description=camera 4 RGB observation.),
            'state': Tensor(shape=(4, 4), dtype=float32, description=Robot end-effector state),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape         | Dtype   | Description
:------------------------- | :----------- | :------------ | :------ | :----------
                           | FeaturesDict |               |         |
episode_metadata           | FeaturesDict |               |         |
episode_metadata/file_path | Text         |               | string  | Path to the original data file.
steps                      | Dataset      |               |         |
steps/action               | Tensor       | (3,)          | float32 | Robot displacement from last frame
steps/discount             | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first             | Tensor       |               | bool    |
steps/is_last              | Tensor       |               | bool    |
steps/is_terminal          | Tensor       |               | bool    |
steps/language_embedding   | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction | Text         |               | string  | Language Instruction.
steps/observation          | FeaturesDict |               |         |
steps/observation/depth_1  | Image        | (360, 640, 1) | uint16  | camera 1 depth observation.
steps/observation/depth_2  | Image        | (360, 640, 1) | uint16  | camera 2 depth observation.
steps/observation/depth_3  | Image        | (360, 640, 1) | uint16  | camera 3 depth observation.
steps/observation/depth_4  | Image        | (360, 640, 1) | uint16  | camera 4 depth observation.
steps/observation/image_1  | Image        | (360, 640, 3) | uint8   | camera 1 RGB observation.
steps/observation/image_2  | Image        | (360, 640, 3) | uint8   | camera 2 RGB observation.
steps/observation/image_3  | Image        | (360, 640, 3) | uint8   | camera 3 RGB observation.
steps/observation/image_4  | Image        | (360, 640, 3) | uint8   | camera 4 RGB observation.
steps/observation/state    | Tensor       | (4, 4)        | float32 | Robot end-effector state
steps/reward               | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/uiuc_d3field-0.1.0.html";
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
@article{wang2023d3field,
  title={D^3Field: Dynamic 3D Descriptor Fields for Generalizable Robotic Manipulation},
  author={Wang, Yixuan and Li, Zhuoran and Zhang, Mingtong and Driggs-Campbell, Katherine and Wu, Jiajun and Fei-Fei, Li and Li, Yunzhu},
  journal={arXiv preprint arXiv:},
  year={2023},
}
```

