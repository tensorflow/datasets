<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="berkeley_fanuc_manipulation" />
  <meta itemprop="description" content="Fanuc robot performing various manipulation tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;berkeley_fanuc_manipulation&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/berkeley_fanuc_manipulation" />
  <meta itemprop="sameAs" content="https://sites.google.com/berkeley.edu/fanuc-manipulation" />
  <meta itemprop="citation" content="@article{fanuc_manipulation2023,&#10;  title={Fanuc Manipulation: A Dataset for Learning-based Manipulation with FANUC Mate 200iD Robot},&#10;  author={Zhu, Xinghao and Tian, Ran and Xu, Chenfeng and Ding, Mingyu and Zhan, Wei and Tomizuka, Masayoshi},&#10;  year={2023},&#10;}" />
</div>

# `berkeley_fanuc_manipulation`


*   **Description**:

Fanuc robot performing various manipulation tasks

*   **Homepage**:
    [https://sites.google.com/berkeley.edu/fanuc-manipulation](https://sites.google.com/berkeley.edu/fanuc-manipulation)

*   **Source code**:
    [`tfds.robotics.rtx.BerkeleyFanucManipulation`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `8.85 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 415

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=float32, description=Robot action, consists of [dx, dy, dz] and [droll, dpitch, dyaw]),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'end_effector_state': Tensor(shape=(7,), dtype=float32, description=Robot gripper end effector state, consists of [x, y, z] and 4x quaternion),
            'image': Image(shape=(224, 224, 3), dtype=uint8, description=Main camera RGB observation.),
            'state': Tensor(shape=(13,), dtype=float32, description=Robot joints state, consists of [6x robot joint angles, 1x gripper open status, 6x robot joint velocities].),
            'wrist_image': Image(shape=(224, 224, 3), dtype=uint8, description=Wrist camera RGB observation.),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                              | Class        | Shape         | Dtype   | Description
:----------------------------------- | :----------- | :------------ | :------ | :----------
                                     | FeaturesDict |               |         |
episode_metadata                     | FeaturesDict |               |         |
episode_metadata/file_path           | Text         |               | string  | Path to the original data file.
steps                                | Dataset      |               |         |
steps/action                         | Tensor       | (6,)          | float32 | Robot action, consists of [dx, dy, dz] and [droll, dpitch, dyaw]
steps/discount                       | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first                       | Tensor       |               | bool    |
steps/is_last                        | Tensor       |               | bool    |
steps/is_terminal                    | Tensor       |               | bool    |
steps/language_embedding             | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction           | Text         |               | string  | Language Instruction.
steps/observation                    | FeaturesDict |               |         |
steps/observation/end_effector_state | Tensor       | (7,)          | float32 | Robot gripper end effector state, consists of [x, y, z] and 4x quaternion
steps/observation/image              | Image        | (224, 224, 3) | uint8   | Main camera RGB observation.
steps/observation/state              | Tensor       | (13,)         | float32 | Robot joints state, consists of [6x robot joint angles, 1x gripper open status, 6x robot joint velocities].
steps/observation/wrist_image        | Image        | (224, 224, 3) | uint8   | Wrist camera RGB observation.
steps/reward                         | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/berkeley_fanuc_manipulation-0.1.0.html";
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
@article{fanuc_manipulation2023,
  title={Fanuc Manipulation: A Dataset for Learning-based Manipulation with FANUC Mate 200iD Robot},
  author={Zhu, Xinghao and Tian, Ran and Xu, Chenfeng and Ding, Mingyu and Zhan, Wei and Tomizuka, Masayoshi},
  year={2023},
}
```

