<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="austin_sirius_dataset_converted_externally_to_rlds" />
  <meta itemprop="description" content="Franka tabletop manipulation tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;austin_sirius_dataset_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/austin_sirius_dataset_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://ut-austin-rpl.github.io/sirius/" />
  <meta itemprop="citation" content="@inproceedings{liu2022robot,&#10;    title = {Robot Learning on the Job: Human-in-the-Loop Autonomy and Learning During Deployment},&#10;    author = {Huihan Liu and Soroush Nasiriany and Lance Zhang and Zhiyao Bao and Yuke Zhu},&#10;    booktitle = {Robotics: Science and Systems (RSS)},&#10;    year = {2023}&#10;}" />
</div>

# `austin_sirius_dataset_converted_externally_to_rlds`


*   **Description**:

Franka tabletop manipulation tasks

*   **Homepage**:
    [https://ut-austin-rpl.github.io/sirius/](https://ut-austin-rpl.github.io/sirius/)

*   **Source code**:
    [`tfds.robotics.rtx.AustinSiriusDatasetConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `6.55 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 559

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32, description=Robot action, consists of [3x ee relative pos, 3x ee relative rotation, 1x gripper action].),
        'action_mode': Tensor(shape=(1,), dtype=float32, description=Type of interaction. -1: initial human demonstration. 1: intervention. 0: autonomuos robot execution (includes pre-intervention class)),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'intv_label': Tensor(shape=(1,), dtype=float32, description=Same as action_modes, except 15 timesteps preceding intervention are labeled as -10.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(84, 84, 3), dtype=uint8, description=Main camera RGB observation.),
            'state': Tensor(shape=(8,), dtype=float32, description=Default robot state, consists of [7x robot joint state, 1x gripper state].),
            'state_ee': Tensor(shape=(16,), dtype=float32, description=End-effector state, represented as 4x4 homogeneous transformation matrix of ee pose.),
            'state_gripper': Tensor(shape=(1,), dtype=float32, description=Robot gripper opening width. Ranges between ~0 (closed) to ~0.077 (open)),
            'state_joint': Tensor(shape=(7,), dtype=float32, description=Robot 7-dof joint information.),
            'wrist_image': Image(shape=(84, 84, 3), dtype=uint8, description=Wrist camera RGB observation.),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                         | Class        | Shape       | Dtype   | Description
:------------------------------ | :----------- | :---------- | :------ | :----------
                                | FeaturesDict |             |         |
episode_metadata                | FeaturesDict |             |         |
episode_metadata/file_path      | Text         |             | string  | Path to the original data file.
steps                           | Dataset      |             |         |
steps/action                    | Tensor       | (7,)        | float32 | Robot action, consists of [3x ee relative pos, 3x ee relative rotation, 1x gripper action].
steps/action_mode               | Tensor       | (1,)        | float32 | Type of interaction. -1: initial human demonstration. 1: intervention. 0: autonomuos robot execution (includes pre-intervention class)
steps/discount                  | Scalar       |             | float32 | Discount if provided, default to 1.
steps/intv_label                | Tensor       | (1,)        | float32 | Same as action_modes, except 15 timesteps preceding intervention are labeled as -10.
steps/is_first                  | Tensor       |             | bool    |
steps/is_last                   | Tensor       |             | bool    |
steps/is_terminal               | Tensor       |             | bool    |
steps/language_embedding        | Tensor       | (512,)      | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction      | Text         |             | string  | Language Instruction.
steps/observation               | FeaturesDict |             |         |
steps/observation/image         | Image        | (84, 84, 3) | uint8   | Main camera RGB observation.
steps/observation/state         | Tensor       | (8,)        | float32 | Default robot state, consists of [7x robot joint state, 1x gripper state].
steps/observation/state_ee      | Tensor       | (16,)       | float32 | End-effector state, represented as 4x4 homogeneous transformation matrix of ee pose.
steps/observation/state_gripper | Tensor       | (1,)        | float32 | Robot gripper opening width. Ranges between ~0 (closed) to ~0.077 (open)
steps/observation/state_joint   | Tensor       | (7,)        | float32 | Robot 7-dof joint information.
steps/observation/wrist_image   | Image        | (84, 84, 3) | uint8   | Wrist camera RGB observation.
steps/reward                    | Scalar       |             | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/austin_sirius_dataset_converted_externally_to_rlds-0.1.0.html";
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
@inproceedings{liu2022robot,
    title = {Robot Learning on the Job: Human-in-the-Loop Autonomy and Learning During Deployment},
    author = {Huihan Liu and Soroush Nasiriany and Lance Zhang and Zhiyao Bao and Yuke Zhu},
    booktitle = {Robotics: Science and Systems (RSS)},
    year = {2023}
}
```

