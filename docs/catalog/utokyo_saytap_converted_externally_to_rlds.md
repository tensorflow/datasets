<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="utokyo_saytap_converted_externally_to_rlds" />
  <meta itemprop="description" content="A1 walking, no RGB&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;utokyo_saytap_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/utokyo_saytap_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://saytap.github.io/" />
  <meta itemprop="citation" content="@article{saytap2023,&#10;  author = {Yujin Tang and Wenhao Yu and Jie Tan and Heiga Zen and Aleksandra Faust and&#10;Tatsuya Harada},&#10;  title  = {SayTap: Language to Quadrupedal Locomotion},&#10;  eprint = {arXiv:2306.07580},&#10;  url    = {https://saytap.github.io},&#10;  note   = &quot;{https://saytap.github.io}&quot;,&#10;  year   = {2023}&#10;}" />
</div>

# `utokyo_saytap_converted_externally_to_rlds`


*   **Description**:

A1 walking, no RGB

*   **Homepage**: [https://saytap.github.io/](https://saytap.github.io/)

*   **Source code**:
    [`tfds.robotics.rtx.UtokyoSaytapConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `55.34 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 20

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=float32, description=Robot action, consists of [12x joint positios].),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'desired_pattern': Tensor(shape=(4, 5), dtype=bool, description=Desired foot contact pattern for the 4 legs, the 4 rows are for the front right, front left, rear right and rear left legs, the pattern length is 5 (=0.1s).),
            'desired_vel': Tensor(shape=(3,), dtype=float32, description=Desired velocites. The first 2 are linear velocities along and perpendicular to the heading direction, the 3rd is the desired angular velocity about the yaw axis.),
            'image': Image(shape=(64, 64, 3), dtype=uint8, description=Dummy camera RGB observation.),
            'prev_act': Tensor(shape=(12,), dtype=float32, description=Actions applied in the previous step.),
            'proj_grav_vec': Tensor(shape=(3,), dtype=float32, description=The gravity vector [0, 0, -1] in the robot base frame.),
            'state': Tensor(shape=(30,), dtype=float32, description=Robot state, consists of [3x robot base linear velocity, 3x base angular vel, 12x joint position, 12x joint velocity].),
            'wrist_image': Image(shape=(64, 64, 3), dtype=uint8, description=Dummy wrist camera RGB observation.),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward if provided, 1 on final step for demos.),
    }),
})
```

*   **Feature documentation**:

Feature                           | Class        | Shape       | Dtype   | Description
:-------------------------------- | :----------- | :---------- | :------ | :----------
                                  | FeaturesDict |             |         |
episode_metadata                  | FeaturesDict |             |         |
episode_metadata/file_path        | Text         |             | string  | Path to the original data file.
steps                             | Dataset      |             |         |
steps/action                      | Tensor       | (12,)       | float32 | Robot action, consists of [12x joint positios].
steps/discount                    | Scalar       |             | float32 | Discount if provided, default to 1.
steps/is_first                    | Tensor       |             | bool    |
steps/is_last                     | Tensor       |             | bool    |
steps/is_terminal                 | Tensor       |             | bool    |
steps/language_embedding          | Tensor       | (512,)      | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction        | Text         |             | string  | Language Instruction.
steps/observation                 | FeaturesDict |             |         |
steps/observation/desired_pattern | Tensor       | (4, 5)      | bool    | Desired foot contact pattern for the 4 legs, the 4 rows are for the front right, front left, rear right and rear left legs, the pattern length is 5 (=0.1s).
steps/observation/desired_vel     | Tensor       | (3,)        | float32 | Desired velocites. The first 2 are linear velocities along and perpendicular to the heading direction, the 3rd is the desired angular velocity about the yaw axis.
steps/observation/image           | Image        | (64, 64, 3) | uint8   | Dummy camera RGB observation.
steps/observation/prev_act        | Tensor       | (12,)       | float32 | Actions applied in the previous step.
steps/observation/proj_grav_vec   | Tensor       | (3,)        | float32 | The gravity vector [0, 0, -1] in the robot base frame.
steps/observation/state           | Tensor       | (30,)       | float32 | Robot state, consists of [3x robot base linear velocity, 3x base angular vel, 12x joint position, 12x joint velocity].
steps/observation/wrist_image     | Image        | (64, 64, 3) | uint8   | Dummy wrist camera RGB observation.
steps/reward                      | Scalar       |             | float32 | Reward if provided, 1 on final step for demos.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/utokyo_saytap_converted_externally_to_rlds-0.1.0.html";
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
@article{saytap2023,
  author = {Yujin Tang and Wenhao Yu and Jie Tan and Heiga Zen and Aleksandra Faust and
Tatsuya Harada},
  title  = {SayTap: Language to Quadrupedal Locomotion},
  eprint = {arXiv:2306.07580},
  url    = {https://saytap.github.io},
  note   = "{https://saytap.github.io}",
  year   = {2023}
}
```

