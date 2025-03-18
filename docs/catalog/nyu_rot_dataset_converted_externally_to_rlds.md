<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="nyu_rot_dataset_converted_externally_to_rlds" />
  <meta itemprop="description" content="xArm short-horizon table-top tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;nyu_rot_dataset_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/nyu_rot_dataset_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://rot-robot.github.io/" />
  <meta itemprop="citation" content="@inproceedings{haldar2023watch,&#10;  title={Watch and match: Supercharging imitation with regularized optimal transport},&#10;  author={Haldar, Siddhant and Mathur, Vaibhav and Yarats, Denis and Pinto, Lerrel},&#10;  booktitle={Conference on Robot Learning},&#10;  pages={32--43},&#10;  year={2023},&#10;  organization={PMLR}&#10;}" />
</div>

# `nyu_rot_dataset_converted_externally_to_rlds`


*   **Description**:

xArm short-horizon table-top tasks

*   **Homepage**: [https://rot-robot.github.io/](https://rot-robot.github.io/)

*   **Source code**:
    [`tfds.robotics.rtx.NyuRotDatasetConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `5.33 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 14

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32, description=Robot action, consists of [3x robot end effector delta positions, 3x robot end effector rotations (roll, pitch, yaw),1x gripper open/close (0-open, 1-closed)].),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(84, 84, 3), dtype=uint8, description=Main camera RGB observation.),
            'state': Tensor(shape=(7,), dtype=float32, description=Robot state, consists of [3x robot end effector positions, 3x robot end effector rotations (roll, pitch, yaw),1x gripper open/close (0-open, 1-closed)].),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape       | Dtype   | Description
:------------------------- | :----------- | :---------- | :------ | :----------
                           | FeaturesDict |             |         |
episode_metadata           | FeaturesDict |             |         |
episode_metadata/file_path | Text         |             | string  | Path to the original data file.
steps                      | Dataset      |             |         |
steps/action               | Tensor       | (7,)        | float32 | Robot action, consists of [3x robot end effector delta positions, 3x robot end effector rotations (roll, pitch, yaw),1x gripper open/close (0-open, 1-closed)].
steps/discount             | Scalar       |             | float32 | Discount if provided, default to 1.
steps/is_first             | Tensor       |             | bool    |
steps/is_last              | Tensor       |             | bool    |
steps/is_terminal          | Tensor       |             | bool    |
steps/language_embedding   | Tensor       | (512,)      | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction | Text         |             | string  | Language Instruction.
steps/observation          | FeaturesDict |             |         |
steps/observation/image    | Image        | (84, 84, 3) | uint8   | Main camera RGB observation.
steps/observation/state    | Tensor       | (7,)        | float32 | Robot state, consists of [3x robot end effector positions, 3x robot end effector rotations (roll, pitch, yaw),1x gripper open/close (0-open, 1-closed)].
steps/reward               | Scalar       |             | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/nyu_rot_dataset_converted_externally_to_rlds-0.1.0.html";
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
@inproceedings{haldar2023watch,
  title={Watch and match: Supercharging imitation with regularized optimal transport},
  author={Haldar, Siddhant and Mathur, Vaibhav and Yarats, Denis and Pinto, Lerrel},
  booktitle={Conference on Robot Learning},
  pages={32--43},
  year={2023},
  organization={PMLR}
}
```

