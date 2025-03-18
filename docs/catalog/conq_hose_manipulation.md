<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="conq_hose_manipulation" />
  <meta itemprop="description" content="Mobile manipulation dataset&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;conq_hose_manipulation&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/conq_hose_manipulation" />
  <meta itemprop="sameAs" content="https://sites.google.com/corp/view/conq-hose-manipulation-dataset/home" />
  <meta itemprop="citation" content="@misc{ConqHoseManipData,&#10;author={Peter Mitrano and Dmitry Berenson},&#10;title={Conq Hose Manipulation Dataset, v1.15.0},&#10;year={2024},&#10;howpublished={https://sites.google.com/view/conq-hose-manipulation-dataset}&#10;}" />
</div>

# `conq_hose_manipulation`


*   **Description**:

Mobile manipulation dataset

*   **Homepage**:
    [https://sites.google.com/corp/view/conq-hose-manipulation-dataset/home](https://sites.google.com/corp/view/conq-hose-manipulation-dataset/home)

*   **Source code**:
    [`tfds.robotics.rtx.ConqHoseManipulation`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `2.72 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 113
`'val'`   | 26

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32),
        'language_instruction': string,
        'observation': FeaturesDict({
            'frontleft_fisheye_image': Image(shape=(726, 604, 3), dtype=uint8),
            'frontright_fisheye_image': Image(shape=(726, 604, 3), dtype=uint8),
            'hand_color_image': Image(shape=(480, 640, 3), dtype=uint8),
            'state': Tensor(shape=(66,), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                    | Class        | Shape         | Dtype   | Description
:----------------------------------------- | :----------- | :------------ | :------ | :----------
                                           | FeaturesDict |               |         |
episode_metadata                           | FeaturesDict |               |         |
episode_metadata/file_path                 | Tensor       |               | string  |
steps                                      | Dataset      |               |         |
steps/action                               | Tensor       | (7,)          | float32 |
steps/discount                             | Scalar       |               | float32 |
steps/is_first                             | Tensor       |               | bool    |
steps/is_last                              | Tensor       |               | bool    |
steps/is_terminal                          | Tensor       |               | bool    |
steps/language_embedding                   | Tensor       | (512,)        | float32 |
steps/language_instruction                 | Tensor       |               | string  |
steps/observation                          | FeaturesDict |               |         |
steps/observation/frontleft_fisheye_image  | Image        | (726, 604, 3) | uint8   |
steps/observation/frontright_fisheye_image | Image        | (726, 604, 3) | uint8   |
steps/observation/hand_color_image         | Image        | (480, 640, 3) | uint8   |
steps/observation/state                    | Tensor       | (66,)         | float32 |
steps/reward                               | Scalar       |               | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/conq_hose_manipulation-0.1.0.html";
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
@misc{ConqHoseManipData,
author={Peter Mitrano and Dmitry Berenson},
title={Conq Hose Manipulation Dataset, v1.15.0},
year={2024},
howpublished={https://sites.google.com/view/conq-hose-manipulation-dataset}
}
```

