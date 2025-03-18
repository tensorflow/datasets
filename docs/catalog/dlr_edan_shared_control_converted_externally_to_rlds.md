<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="dlr_edan_shared_control_converted_externally_to_rlds" />
  <meta itemprop="description" content="wheelchair with arm performing shelf pick tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;dlr_edan_shared_control_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/dlr_edan_shared_control_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://ieeexplore.ieee.org/document/9341156" />
  <meta itemprop="citation" content="@inproceedings{vogel_edan_2020,&#10;   title = {EDAN - an EMG-Controlled Daily Assistant to Help People with Physical Disabilities},&#10;  language = {en},&#10;   booktitle = {2020 {IEEE}/{RSJ} {International} {Conference} on {Intelligent} {Robots} and {Systems} ({IROS})},&#10; author = {Vogel, Jörn and Hagengruber, Annette and Iskandar, Maged and Quere, Gabriel and Leipscher, Ulrike and Bustamante, Samuel and Dietrich, Alexander and Hoeppner, Hannes and Leidner, Daniel and Albu-Schäffer, Alin},&#10;  year = {2020}&#10;}&#10;@inproceedings{quere_shared_2020,&#10;  address = {Paris, France},&#10; title = {Shared {Control} {Templates} for {Assistive} {Robotics}},&#10; language = {en},&#10;   booktitle = {2020 {IEEE} {International} {Conference} on {Robotics} and {Automation} ({ICRA})},&#10;    author = {Quere, Gabriel and Hagengruber, Annette and Iskandar, Maged and Bustamante, Samuel and Leidner, Daniel and Stulp, Freek and Vogel, Joern},&#10;   year = {2020},&#10; pages = {7},&#10;}" />
</div>

# `dlr_edan_shared_control_converted_externally_to_rlds`


*   **Description**:

wheelchair with arm performing shelf pick tasks

*   **Homepage**:
    [https://ieeexplore.ieee.org/document/9341156](https://ieeexplore.ieee.org/document/9341156)

*   **Source code**:
    [`tfds.robotics.rtx.DlrEdanSharedControlConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `3.09 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 104

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32, description=Robot action, consists of [3x robot EEF position, 3x robot EEF orientation yaw/pitch/roll calculated with scipy Rotation.as_euler(="zxy") Class].),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(360, 640, 3), dtype=uint8, description=Main camera RGB observation.),
            'state': Tensor(shape=(7,), dtype=float32, description=Robot state, consists of [3x robot EEF position, 3x robot EEF orientation yaw/pitch/roll calculated with scipy Rotation.as_euler(="zxy") Class].),
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
steps/action               | Tensor       | (7,)          | float32 | Robot action, consists of [3x robot EEF position, 3x robot EEF orientation yaw/pitch/roll calculated with scipy Rotation.as_euler(="zxy") Class].
steps/discount             | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first             | Tensor       |               | bool    |
steps/is_last              | Tensor       |               | bool    |
steps/is_terminal          | Tensor       |               | bool    |
steps/language_embedding   | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction | Text         |               | string  | Pour into the mug.
steps/observation          | FeaturesDict |               |         |
steps/observation/image    | Image        | (360, 640, 3) | uint8   | Main camera RGB observation.
steps/observation/state    | Tensor       | (7,)          | float32 | Robot state, consists of [3x robot EEF position, 3x robot EEF orientation yaw/pitch/roll calculated with scipy Rotation.as_euler(="zxy") Class].
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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/dlr_edan_shared_control_converted_externally_to_rlds-0.1.0.html";
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
@inproceedings{vogel_edan_2020,
    title = {EDAN - an EMG-Controlled Daily Assistant to Help People with Physical Disabilities},
    language = {en},
    booktitle = {2020 {IEEE}/{RSJ} {International} {Conference} on {Intelligent} {Robots} and {Systems} ({IROS})},
    author = {Vogel, Jörn and Hagengruber, Annette and Iskandar, Maged and Quere, Gabriel and Leipscher, Ulrike and Bustamante, Samuel and Dietrich, Alexander and Hoeppner, Hannes and Leidner, Daniel and Albu-Schäffer, Alin},
    year = {2020}
}
@inproceedings{quere_shared_2020,
    address = {Paris, France},
    title = {Shared {Control} {Templates} for {Assistive} {Robotics}},
    language = {en},
    booktitle = {2020 {IEEE} {International} {Conference} on {Robotics} and {Automation} ({ICRA})},
    author = {Quere, Gabriel and Hagengruber, Annette and Iskandar, Maged and Bustamante, Samuel and Leidner, Daniel and Stulp, Freek and Vogel, Joern},
    year = {2020},
    pages = {7},
}
```

