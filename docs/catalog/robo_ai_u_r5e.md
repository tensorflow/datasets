<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robo_ai_u_r5e" />
  <meta itemprop="description" content="Universal Robots UR5e demonstration dataset for VLA model training. Data collected from real-world robot workspace with preprogrammed robot routines.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robo_ai_u_r5e&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robo_ai_u_r5e" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/roboai-ur5e/home" />
  <meta itemprop="citation" content="@article{RoboAIUR5e2025,&#10;  title        = {RoboAI UR5e Training Dataset},&#10;  author       = {Joonas Rouhiainen},&#10;  institution  = {RoboAI Research Center, Satakunta University of Applied Sciences},&#10;  year         = {2025},&#10;  howpublished = {\url{https://sites.google.com/view/roboai-ur5e/home}},&#10;}" />
</div>

# `robo_ai_u_r5e`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Universal Robots UR5e demonstration dataset for VLA model training. Data
collected from real-world robot workspace with preprogrammed robot routines.

*   **Homepage**:
    [https://sites.google.com/view/roboai-ur5e/home](https://sites.google.com/view/roboai-ur5e/home)

*   **Source code**:
    [`tfds.robotics.rtx.RoboAiUR5e`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'episode_index': int32,
        'file_name': string,
    }),
    'steps': Dataset({
        'absolute_action_mask': Tensor(shape=(7,), dtype=bool),
        'action': Tensor(shape=(7,), dtype=float32),
        'action_normalization_mask': Tensor(shape=(7,), dtype=bool),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_instruction': string,
        'observation': FeaturesDict({
            'image': Image(shape=(480, 640, 3), dtype=uint8),
            'robot_state': Tensor(shape=(15,), dtype=float32),
        }),
    }),
})
```

*   **Feature documentation**:

Feature                         | Class        | Shape         | Dtype   | Description
:------------------------------ | :----------- | :------------ | :------ | :----------
                                | FeaturesDict |               |         |
episode_metadata                | FeaturesDict |               |         |
episode_metadata/episode_index  | Tensor       |               | int32   |
episode_metadata/file_name      | Tensor       |               | string  |
steps                           | Dataset      |               |         |
steps/absolute_action_mask      | Tensor       | (7,)          | bool    |
steps/action                    | Tensor       | (7,)          | float32 |
steps/action_normalization_mask | Tensor       | (7,)          | bool    |
steps/is_first                  | Tensor       |               | bool    |
steps/is_last                   | Tensor       |               | bool    |
steps/is_terminal               | Tensor       |               | bool    |
steps/language_instruction      | Tensor       |               | string  |
steps/observation               | FeaturesDict |               |         |
steps/observation/image         | Image        | (480, 640, 3) | uint8   |
steps/observation/robot_state   | Tensor       | (15,)         | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{RoboAIUR5e2025,
  title        = {RoboAI UR5e Training Dataset},
  author       = {Joonas Rouhiainen},
  institution  = {RoboAI Research Center, Satakunta University of Applied Sciences},
  year         = {2025},
  howpublished = {\url{https://sites.google.com/view/roboai-ur5e/home}},
}
```

