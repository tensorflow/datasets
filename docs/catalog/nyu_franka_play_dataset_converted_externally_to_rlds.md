<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="nyu_franka_play_dataset_converted_externally_to_rlds" />
  <meta itemprop="description" content="Franka interacting with toy kitchens&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;nyu_franka_play_dataset_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/nyu_franka_play_dataset_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://play-to-policy.github.io/" />
  <meta itemprop="citation" content="@article{cui2022play,&#10;  title   = {From Play to Policy: Conditional Behavior Generation from Uncurated Robot Data},&#10;  author  = {Cui, Zichen Jeff and Wang, Yibin and Shafiullah, Nur Muhammad Mahi and Pinto, Lerrel},&#10;  journal = {arXiv preprint arXiv:2210.10047},&#10;  year    = {2022}&#10;}" />
</div>

# `nyu_franka_play_dataset_converted_externally_to_rlds`


*   **Description**:

Franka interacting with toy kitchens

*   **Homepage**:
    [https://play-to-policy.github.io/](https://play-to-policy.github.io/)

*   **Source code**:
    [`tfds.robotics.rtx.NyuFrankaPlayDatasetConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `5.18 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 365
`'val'`   | 91

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(15,), dtype=float32, description=Robot action, consists of [7x joint velocities, 3x EE delta xyz, 3x EE delta rpy, 1x gripper position, 1x terminate episode].),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'depth': Tensor(shape=(128, 128, 1), dtype=int32, description=Right camera depth observation.),
            'depth_additional_view': Tensor(shape=(128, 128, 1), dtype=int32, description=Left camera depth observation.),
            'image': Image(shape=(128, 128, 3), dtype=uint8, description=Right camera RGB observation.),
            'image_additional_view': Image(shape=(128, 128, 3), dtype=uint8, description=Left camera RGB observation.),
            'state': Tensor(shape=(13,), dtype=float32, description=Robot state, consists of [7x robot joint angles, 3x EE xyz, 3x EE rpy.),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                                 | Class        | Shape         | Dtype   | Description
:-------------------------------------- | :----------- | :------------ | :------ | :----------
                                        | FeaturesDict |               |         |
episode_metadata                        | FeaturesDict |               |         |
episode_metadata/file_path              | Text         |               | string  | Path to the original data file.
steps                                   | Dataset      |               |         |
steps/action                            | Tensor       | (15,)         | float32 | Robot action, consists of [7x joint velocities, 3x EE delta xyz, 3x EE delta rpy, 1x gripper position, 1x terminate episode].
steps/discount                          | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first                          | Tensor       |               | bool    |
steps/is_last                           | Tensor       |               | bool    |
steps/is_terminal                       | Tensor       |               | bool    |
steps/language_embedding                | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction              | Text         |               | string  | Language Instruction.
steps/observation                       | FeaturesDict |               |         |
steps/observation/depth                 | Tensor       | (128, 128, 1) | int32   | Right camera depth observation.
steps/observation/depth_additional_view | Tensor       | (128, 128, 1) | int32   | Left camera depth observation.
steps/observation/image                 | Image        | (128, 128, 3) | uint8   | Right camera RGB observation.
steps/observation/image_additional_view | Image        | (128, 128, 3) | uint8   | Left camera RGB observation.
steps/observation/state                 | Tensor       | (13,)         | float32 | Robot state, consists of [7x robot joint angles, 3x EE xyz, 3x EE rpy.
steps/reward                            | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/nyu_franka_play_dataset_converted_externally_to_rlds-0.1.0.html";
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
@article{cui2022play,
  title   = {From Play to Policy: Conditional Behavior Generation from Uncurated Robot Data},
  author  = {Cui, Zichen Jeff and Wang, Yibin and Shafiullah, Nur Muhammad Mahi and Pinto, Lerrel},
  journal = {arXiv preprint arXiv:2210.10047},
  year    = {2022}
}
```

