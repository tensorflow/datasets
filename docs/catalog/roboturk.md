<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="roboturk" />
  <meta itemprop="description" content="Cloth folding, bowl stacking&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;roboturk&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/roboturk" />
  <meta itemprop="sameAs" content="https://roboturk.stanford.edu/dataset_real.html" />
  <meta itemprop="citation" content="@inproceedings{mandlekar2019scaling,&#10;          title={Scaling robot supervision to hundreds of hours with roboturk: Robotic manipulation dataset through human reasoning and dexterity},&#10;          author={Mandlekar, Ajay and Booher, Jonathan and Spero, Max and Tung, Albert and Gupta, Anchit and Zhu, Yuke and Garg, Animesh and Savarese, Silvio and Fei-Fei, Li},&#10;          booktitle={2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},&#10;          pages={1048--1055},&#10;          year={2019},&#10;          organization={IEEE}&#10;        }" />
</div>

# `roboturk`


*   **Description**:

Cloth folding, bowl stacking

*   **Homepage**:
    [https://roboturk.stanford.edu/dataset_real.html](https://roboturk.stanford.edu/dataset_real.html)

*   **Source code**:
    [`tfds.robotics.rtx.Roboturk`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `45.39 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 199
`'train'` | 1,796

*   **Feature structure**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': FeaturesDict({
            'gripper_closedness_action': Tensor(shape=(1,), dtype=float32),
            'rotation_delta': Tensor(shape=(3,), dtype=float32),
            'terminate_episode': float32,
            'world_vector': Tensor(shape=(3,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'front_rgb': Image(shape=(480, 640, 3), dtype=uint8),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                        | Class        | Shape         | Dtype   | Description
:--------------------------------------------- | :----------- | :------------ | :------ | :----------
                                               | FeaturesDict |               |         |
steps                                          | Dataset      |               |         |
steps/action                                   | FeaturesDict |               |         |
steps/action/gripper_closedness_action         | Tensor       | (1,)          | float32 |
steps/action/rotation_delta                    | Tensor       | (3,)          | float32 |
steps/action/terminate_episode                 | Tensor       |               | float32 |
steps/action/world_vector                      | Tensor       | (3,)          | float32 |
steps/is_first                                 | Tensor       |               | bool    |
steps/is_last                                  | Tensor       |               | bool    |
steps/is_terminal                              | Tensor       |               | bool    |
steps/observation                              | FeaturesDict |               |         |
steps/observation/front_rgb                    | Image        | (480, 640, 3) | uint8   |
steps/observation/natural_language_embedding   | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction | Tensor       |               | string  |
steps/reward                                   | Scalar       |               | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/roboturk-0.1.0.html";
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
@inproceedings{mandlekar2019scaling,
          title={Scaling robot supervision to hundreds of hours with roboturk: Robotic manipulation dataset through human reasoning and dexterity},
          author={Mandlekar, Ajay and Booher, Jonathan and Spero, Max and Tung, Albert and Gupta, Anchit and Zhu, Yuke and Garg, Animesh and Savarese, Silvio and Fei-Fei, Li},
          booktitle={2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
          pages={1048--1055},
          year={2019},
          organization={IEEE}
        }
```

