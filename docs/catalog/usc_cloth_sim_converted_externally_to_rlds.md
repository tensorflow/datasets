<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="usc_cloth_sim_converted_externally_to_rlds" />
  <meta itemprop="description" content="Franka cloth interaction tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;usc_cloth_sim_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/usc_cloth_sim_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://uscresl.github.io/dmfd/" />
  <meta itemprop="citation" content="@article{salhotra2022dmfd,&#10;    author={Salhotra, Gautam and Liu, I-Chun Arthur and Dominguez-Kuhne, Marcus and Sukhatme, Gaurav S.},&#10;    journal={IEEE Robotics and Automation Letters},&#10;    title={Learning Deformable Object Manipulation From Expert Demonstrations},&#10;    year={2022},&#10;    volume={7},&#10;    number={4},&#10;    pages={8775-8782},&#10;    doi={10.1109/LRA.2022.3187843}&#10;}" />
</div>

# `usc_cloth_sim_converted_externally_to_rlds`


*   **Description**:

Franka cloth interaction tasks

*   **Homepage**:
    [https://uscresl.github.io/dmfd/](https://uscresl.github.io/dmfd/)

*   **Source code**:
    [`tfds.robotics.rtx.UscClothSimConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `254.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 800
`'val'`   | 200

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(4,), dtype=float32, description=Robot action, consists of x,y,z goal and picker commandpicker<0.5 = open, picker>0.5 = close.),
        'discount': Scalar(shape=(), dtype=float32, description=Discount if provided, default to 1.),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32, description=Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(32, 32, 3), dtype=uint8, description=Image observation of cloth.),
        }),
        'reward': Scalar(shape=(), dtype=float32, description=Reward as a normalized performance metric in [0, 1].0 = no change from initial state. 1 = perfect fold.-ve performance means the cloth is worse off than initial state.),
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
steps/action               | Tensor       | (4,)        | float32 | Robot action, consists of x,y,z goal and picker commandpicker<0.5 = open, picker>0.5 = close.
steps/discount             | Scalar       |             | float32 | Discount if provided, default to 1.
steps/is_first             | Tensor       |             | bool    |
steps/is_last              | Tensor       |             | bool    |
steps/is_terminal          | Tensor       |             | bool    |
steps/language_embedding   | Tensor       | (512,)      | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction | Text         |             | string  | Language Instruction.
steps/observation          | FeaturesDict |             |         |
steps/observation/image    | Image        | (32, 32, 3) | uint8   | Image observation of cloth.
steps/reward               | Scalar       |             | float32 | Reward as a normalized performance metric in [0, 1].0 = no change from initial state. 1 = perfect fold.-ve performance means the cloth is worse off than initial state.

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/usc_cloth_sim_converted_externally_to_rlds-0.1.0.html";
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
@article{salhotra2022dmfd,
    author={Salhotra, Gautam and Liu, I-Chun Arthur and Dominguez-Kuhne, Marcus and Sukhatme, Gaurav S.},
    journal={IEEE Robotics and Automation Letters},
    title={Learning Deformable Object Manipulation From Expert Demonstrations},
    year={2022},
    volume={7},
    number={4},
    pages={8775-8782},
    doi={10.1109/LRA.2022.3187843}
}
```

