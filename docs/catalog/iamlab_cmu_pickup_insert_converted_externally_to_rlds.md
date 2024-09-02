<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="iamlab_cmu_pickup_insert_converted_externally_to_rlds" />
  <meta itemprop="description" content="Franka picking objects and insertion tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;iamlab_cmu_pickup_insert_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/iamlab_cmu_pickup_insert_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://openreview.net/forum?id=WuBv9-IGDUA" />
  <meta itemprop="citation" content="@inproceedings{&#10;saxena2023multiresolution,&#10;title={Multi-Resolution Sensing for Real-Time Control with Vision-Language Models},&#10;author={Saumya Saxena and Mohit Sharma and Oliver Kroemer},&#10;booktitle={7th Annual Conference on Robot Learning},&#10;year={2023},&#10;url={https://openreview.net/forum?id=WuBv9-IGDUA}&#10;}" />
</div>

# `iamlab_cmu_pickup_insert_converted_externally_to_rlds`


*   **Description**:

Franka picking objects and insertion tasks

*   **Homepage**:
    [https://openreview.net/forum?id=WuBv9-IGDUA](https://openreview.net/forum?id=WuBv9-IGDUA)

*   **Source code**:
    [`tfds.robotics.rtx.IamlabCmuPickupInsertConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `50.29 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 631

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=float32, description=Robot action, consists of [3x end-effector position, 4x end-effector quaternion, 1x gripper open/close].),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(360, 640, 3), dtype=uint8, description=Main camera RGB observation.),
            'state': Tensor(shape=(20,), dtype=float32, description=Robot state, consists of [7x robot joint angles, 1x gripper status, 6x joint torques, 6x end-effector force].),
            'wrist_image': Image(shape=(240, 320, 3), dtype=uint8, description=Wrist camera RGB observation.),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                       | Class        | Shape         | Dtype   | Description
:---------------------------- | :----------- | :------------ | :------ | :----------
                              | FeaturesDict |               |         |
episode_metadata              | FeaturesDict |               |         |
episode_metadata/file_path    | Text         |               | string  | Path to the original data file.
steps                         | Dataset      |               |         |
steps/action                  | Tensor       | (8,)          | float32 | Robot action, consists of [3x end-effector position, 4x end-effector quaternion, 1x gripper open/close].
steps/discount                | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first                | Tensor       |               | bool    |
steps/is_last                 | Tensor       |               | bool    |
steps/is_terminal             | Tensor       |               | bool    |
steps/language_embedding      | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction    | Text         |               | string  | Language Instruction.
steps/observation             | FeaturesDict |               |         |
steps/observation/image       | Image        | (360, 640, 3) | uint8   | Main camera RGB observation.
steps/observation/state       | Tensor       | (20,)         | float32 | Robot state, consists of [7x robot joint angles, 1x gripper status, 6x joint torques, 6x end-effector force].
steps/observation/wrist_image | Image        | (240, 320, 3) | uint8   | Wrist camera RGB observation.
steps/reward                  | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/iamlab_cmu_pickup_insert_converted_externally_to_rlds-0.1.0.html";
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
@inproceedings{
saxena2023multiresolution,
title={Multi-Resolution Sensing for Real-Time Control with Vision-Language Models},
author={Saumya Saxena and Mohit Sharma and Oliver Kroemer},
booktitle={7th Annual Conference on Robot Learning},
year={2023},
url={https://openreview.net/forum?id=WuBv9-IGDUA}
}
```

