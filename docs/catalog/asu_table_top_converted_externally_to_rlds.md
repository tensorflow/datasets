<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="asu_table_top_converted_externally_to_rlds" />
  <meta itemprop="description" content="UR5 performing table-top pick/place/rotate tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;asu_table_top_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/asu_table_top_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://link.springer.com/article/10.1007/s10514-023-10129-1" />
  <meta itemprop="citation" content="@inproceedings{zhou2023modularity,&#10;  title={Modularity through Attention: Efficient Training and Transfer of Language-Conditioned Policies for Robot Manipulation},&#10;  author={Zhou, Yifan and Sonawani, Shubham and Phielipp, Mariano and Stepputtis, Simon and Amor, Heni},&#10;  booktitle={Conference on Robot Learning},&#10;  pages={1684--1695},&#10;  year={2023},&#10;  organization={PMLR}&#10;}&#10;@article{zhou2023learning,&#10;  title={Learning modular language-conditioned robot policies through attention},&#10;  author={Zhou, Yifan and Sonawani, Shubham and Phielipp, Mariano and Ben Amor, Heni and Stepputtis, Simon},&#10;  journal={Autonomous Robots},&#10;  pages={1--21},&#10;  year={2023},&#10;  publisher={Springer}&#10;}" />
</div>

# `asu_table_top_converted_externally_to_rlds`


*   **Description**:

UR5 performing table-top pick/place/rotate tasks

*   **Homepage**:
    [https://link.springer.com/article/10.1007/s10514-023-10129-1](https://link.springer.com/article/10.1007/s10514-023-10129-1)

*   **Source code**:
    [`tfds.robotics.rtx.AsuTableTopConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `737.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 110

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32, description=Robot action, consists of [7x joint velocities, 2x gripper velocities, 1x terminate episode].),
        'action_delta': Tensor(shape=(7,), dtype=float32, description=Robot delta action, consists of [7x joint velocities, 2x gripper velocities, 1x terminate episode].),
        'action_inst': Text(shape=(), dtype=string),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'goal_object': Text(shape=(), dtype=string),
        'ground_truth_states': FeaturesDict({
            'EE': Tensor(shape=(6,), dtype=float32, description=xyzrpy),
            'bottle': Tensor(shape=(6,), dtype=float32, description=xyzrpy),
            'bread': Tensor(shape=(6,), dtype=float32, description=xyzrpy),
            'coke': Tensor(shape=(6,), dtype=float32, description=xyzrpy),
            'cube': Tensor(shape=(6,), dtype=float32, description=xyzrpy),
            'milk': Tensor(shape=(6,), dtype=float32, description=xyzrpy),
            'pepsi': Tensor(shape=(6,), dtype=float32, description=xyzrpy),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(224, 224, 3), dtype=uint8, description=Main camera RGB observation.),
            'state': Tensor(shape=(7,), dtype=float32, description=Robot state, consists of [6x robot joint angles, 1x gripper position].),
            'state_vel': Tensor(shape=(7,), dtype=float32, description=Robot joint velocity, consists of [6x robot joint angles, 1x gripper position].),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                          | Class        | Shape         | Dtype   | Description
:------------------------------- | :----------- | :------------ | :------ | :----------
                                 | FeaturesDict |               |         |
episode_metadata                 | FeaturesDict |               |         |
episode_metadata/file_path       | Text         |               | string  | Path to the original data file.
steps                            | Dataset      |               |         |
steps/action                     | Tensor       | (7,)          | float32 | Robot action, consists of [7x joint velocities, 2x gripper velocities, 1x terminate episode].
steps/action_delta               | Tensor       | (7,)          | float32 | Robot delta action, consists of [7x joint velocities, 2x gripper velocities, 1x terminate episode].
steps/action_inst                | Text         |               | string  | Action to be performed.
steps/discount                   | Scalar       |               | float32 | Discount if provided, default to 1.
steps/goal_object                | Text         |               | string  | Object to be manipulated with.
steps/ground_truth_states        | FeaturesDict |               |         |
steps/ground_truth_states/EE     | Tensor       | (6,)          | float32 | xyzrpy
steps/ground_truth_states/bottle | Tensor       | (6,)          | float32 | xyzrpy
steps/ground_truth_states/bread  | Tensor       | (6,)          | float32 | xyzrpy
steps/ground_truth_states/coke   | Tensor       | (6,)          | float32 | xyzrpy
steps/ground_truth_states/cube   | Tensor       | (6,)          | float32 | xyzrpy
steps/ground_truth_states/milk   | Tensor       | (6,)          | float32 | xyzrpy
steps/ground_truth_states/pepsi  | Tensor       | (6,)          | float32 | xyzrpy
steps/is_first                   | Tensor       |               | bool    |
steps/is_last                    | Tensor       |               | bool    |
steps/is_terminal                | Tensor       |               | bool    |
steps/language_embedding         | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction       | Text         |               | string  | Language Instruction.
steps/observation                | FeaturesDict |               |         |
steps/observation/image          | Image        | (224, 224, 3) | uint8   | Main camera RGB observation.
steps/observation/state          | Tensor       | (7,)          | float32 | Robot state, consists of [6x robot joint angles, 1x gripper position].
steps/observation/state_vel      | Tensor       | (7,)          | float32 | Robot joint velocity, consists of [6x robot joint angles, 1x gripper position].
steps/reward                     | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/asu_table_top_converted_externally_to_rlds-0.1.0.html";
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
@inproceedings{zhou2023modularity,
  title={Modularity through Attention: Efficient Training and Transfer of Language-Conditioned Policies for Robot Manipulation},
  author={Zhou, Yifan and Sonawani, Shubham and Phielipp, Mariano and Stepputtis, Simon and Amor, Heni},
  booktitle={Conference on Robot Learning},
  pages={1684--1695},
  year={2023},
  organization={PMLR}
}
@article{zhou2023learning,
  title={Learning modular language-conditioned robot policies through attention},
  author={Zhou, Yifan and Sonawani, Shubham and Phielipp, Mariano and Ben Amor, Heni and Stepputtis, Simon},
  journal={Autonomous Robots},
  pages={1--21},
  year={2023},
  publisher={Springer}
}
```

