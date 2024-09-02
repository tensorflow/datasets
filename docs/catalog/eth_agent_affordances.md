<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="eth_agent_affordances" />
  <meta itemprop="description" content="Franka opening ovens -- point cloud + proprio only&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;eth_agent_affordances&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/eth_agent_affordances" />
  <meta itemprop="sameAs" content="https://ieeexplore.ieee.org/iel7/10160211/10160212/10160747.pdf" />
  <meta itemprop="citation" content="@inproceedings{schiavi2023learning,&#10;  title={Learning agent-aware affordances for closed-loop interaction with articulated objects},&#10;  author={Schiavi, Giulio and Wulkop, Paula and Rizzi, Giuseppe and Ott, Lionel and Siegwart, Roland and Chung, Jen Jen},&#10;  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)},&#10;  pages={5916--5922},&#10;  year={2023},&#10;  organization={IEEE}&#10;}" />
</div>

# `eth_agent_affordances`


*   **Description**:

Franka opening ovens -- point cloud + proprio only

*   **Homepage**:
    [https://ieeexplore.ieee.org/iel7/10160211/10160212/10160747.pdf](https://ieeexplore.ieee.org/iel7/10160211/10160212/10160747.pdf)

*   **Source code**:
    [`tfds.robotics.rtx.EthAgentAffordances`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `17.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 118

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
        'input_point_cloud': Tensor(shape=(10000, 3), dtype=float16, description=Point cloud (geometry only) of the object at the beginning of the episode (world frame) as a numpy array (10000,3).),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32, description=Robot action, consists of [end-effector velocity (v_x,v_y,v_z,omega_x,omega_y,omega_z) in world frame),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(64, 64, 3), dtype=uint8, description=Main camera RGB observation. Not available for this dataset, will be set to np.zeros.),
            'input_point_cloud': Tensor(shape=(10000, 3), dtype=float16, description=Point cloud (geometry only) of the object at the beginning of the episode (world frame) as a numpy array (10000,3).),
            'state': Tensor(shape=(8,), dtype=float32, description=State, consists of [end-effector pose (x,y,z,yaw,pitch,roll) in world frame, 1x gripper open/close, 1x door opening angle].),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                             | Class        | Shape       | Dtype   | Description
:---------------------------------- | :----------- | :---------- | :------ | :----------
                                    | FeaturesDict |             |         |
episode_metadata                    | FeaturesDict |             |         |
episode_metadata/file_path          | Text         |             | string  | Path to the original data file.
episode_metadata/input_point_cloud  | Tensor       | (10000, 3)  | float16 | Point cloud (geometry only) of the object at the beginning of the episode (world frame) as a numpy array (10000,3).
steps                               | Dataset      |             |         |
steps/action                        | Tensor       | (6,)        | float32 | Robot action, consists of [end-effector velocity (v_x,v_y,v_z,omega_x,omega_y,omega_z) in world frame
steps/discount                      | Scalar       |             | float32 | Discount if provided, default to 1.
steps/is_first                      | Tensor       |             | bool    |
steps/is_last                       | Tensor       |             | bool    |
steps/is_terminal                   | Tensor       |             | bool    |
steps/language_embedding            | Tensor       | (512,)      | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction          | Text         |             | string  | Language Instruction.
steps/observation                   | FeaturesDict |             |         |
steps/observation/image             | Image        | (64, 64, 3) | uint8   | Main camera RGB observation. Not available for this dataset, will be set to np.zeros.
steps/observation/input_point_cloud | Tensor       | (10000, 3)  | float16 | Point cloud (geometry only) of the object at the beginning of the episode (world frame) as a numpy array (10000,3).
steps/observation/state             | Tensor       | (8,)        | float32 | State, consists of [end-effector pose (x,y,z,yaw,pitch,roll) in world frame, 1x gripper open/close, 1x door opening angle].
steps/reward                        | Scalar       |             | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/eth_agent_affordances-0.1.0.html";
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
@inproceedings{schiavi2023learning,
  title={Learning agent-aware affordances for closed-loop interaction with articulated objects},
  author={Schiavi, Giulio and Wulkop, Paula and Rizzi, Giuseppe and Ott, Lionel and Siegwart, Roland and Chung, Jen Jen},
  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)},
  pages={5916--5922},
  year={2023},
  organization={IEEE}
}
```

