<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mimic_play" />
  <meta itemprop="description" content="Real dataset of 14 long horizon manipulation tasks. A mix of human play data and single robot arm data performing the same tasks.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;mimic_play&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mimic_play" />
  <meta itemprop="sameAs" content="https://mimic-play.github.io/" />
  <meta itemprop="citation" content="@article{wang2023mimicplay,title={Mimicplay: Long-horizon imitation learning by watching human play},author={Wang, Chen and Fan, Linxi and Sun, Jiankai and Zhang, Ruohan and Fei-Fei, Li and Xu, Danfei and Zhu, Yuke and Anandkumar, Anima},journal={arXiv preprint arXiv:2302.12422},year={2023}}" />
</div>

# `mimic_play`


*   **Description**:

Real dataset of 14 long horizon manipulation tasks. A mix of human play data and
single robot arm data performing the same tasks.

*   **Homepage**: [https://mimic-play.github.io/](https://mimic-play.github.io/)

*   **Source code**:
    [`tfds.robotics.rtx.MimicPlay`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `7.14 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 378

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32),
        'language_instruction': string,
        'observation': FeaturesDict({
            'image': FeaturesDict({
                'front_image_1': Image(shape=(120, 120, 3), dtype=uint8),
                'front_image_2': Image(shape=(120, 120, 3), dtype=uint8),
            }),
            'state': FeaturesDict({
                'ee_pose': Tensor(shape=(7,), dtype=float32),
                'gripper_position': float32,
                'joint_positions': Tensor(shape=(7,), dtype=float32),
                'joint_velocities': Tensor(shape=(7,), dtype=float32),
            }),
            'wrist_image': FeaturesDict({
                'wrist_image': Image(shape=(120, 120, 3), dtype=uint8),
            }),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                   | Class        | Shape         | Dtype   | Description
:---------------------------------------- | :----------- | :------------ | :------ | :----------
                                          | FeaturesDict |               |         |
episode_metadata                          | FeaturesDict |               |         |
episode_metadata/file_path                | Tensor       |               | string  |
steps                                     | Dataset      |               |         |
steps/action                              | Tensor       | (7,)          | float32 |
steps/discount                            | Scalar       |               | float32 |
steps/is_first                            | Tensor       |               | bool    |
steps/is_last                             | Tensor       |               | bool    |
steps/is_terminal                         | Tensor       |               | bool    |
steps/language_embedding                  | Tensor       | (512,)        | float32 |
steps/language_instruction                | Tensor       |               | string  |
steps/observation                         | FeaturesDict |               |         |
steps/observation/image                   | FeaturesDict |               |         |
steps/observation/image/front_image_1     | Image        | (120, 120, 3) | uint8   |
steps/observation/image/front_image_2     | Image        | (120, 120, 3) | uint8   |
steps/observation/state                   | FeaturesDict |               |         |
steps/observation/state/ee_pose           | Tensor       | (7,)          | float32 |
steps/observation/state/gripper_position  | Tensor       |               | float32 |
steps/observation/state/joint_positions   | Tensor       | (7,)          | float32 |
steps/observation/state/joint_velocities  | Tensor       | (7,)          | float32 |
steps/observation/wrist_image             | FeaturesDict |               |         |
steps/observation/wrist_image/wrist_image | Image        | (120, 120, 3) | uint8   |
steps/reward                              | Scalar       |               | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/mimic_play-0.1.0.html";
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
@article{wang2023mimicplay,title={Mimicplay: Long-horizon imitation learning by watching human play},author={Wang, Chen and Fan, Linxi and Sun, Jiankai and Zhang, Ruohan and Fei-Fei, Li and Xu, Danfei and Zhu, Yuke and Anandkumar, Anima},journal={arXiv preprint arXiv:2302.12422},year={2023}}
```

