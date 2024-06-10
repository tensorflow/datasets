<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="spoc" />
  <meta itemprop="description" content="&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;spoc&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/spoc" />
  <meta itemprop="sameAs" content="https://spoc-robot.github.io/" />
  <meta itemprop="citation" content="@article{spoc2023,&#10;    author    = {Kiana Ehsani, Tanmay Gupta, Rose Hendrix, Jordi Salvador, Luca Weihs, Kuo-Hao Zeng, Kunal Pratap Singh, Yejin Kim, Winson Han, Alvaro Herrasti, Ranjay Krishna, Dustin Schwenk, Eli VanderBilt, Aniruddha Kembhavi},&#10;    title     = {Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World},&#10;    journal   = {arXiv},&#10;    year      = {2023},&#10;    eprint    = {2312.02976},&#10;}" />
</div>

# `spoc`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

*   **Homepage**: [https://spoc-robot.github.io/](https://spoc-robot.github.io/)

*   **Source code**:
    [`tfds.robotics.rtx.Spoc`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

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
        'file_path': string,
        'task_target_split': string,
        'task_type': string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(9,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_instruction': string,
        'observation': FeaturesDict({
            'an_object_is_in_hand': Scalar(shape=(), dtype=bool),
            'house_index': Scalar(shape=(), dtype=int64),
            'hypothetical_task_success': Scalar(shape=(), dtype=bool),
            'image': Image(shape=(224, 384, 3), dtype=uint8),
            'image_manipulation': Image(shape=(224, 384, 3), dtype=uint8),
            'last_action_is_random': Scalar(shape=(), dtype=bool),
            'last_action_str': string,
            'last_action_success': Scalar(shape=(), dtype=bool),
            'last_agent_location': Tensor(shape=(6,), dtype=float32),
            'manip_object_bbox': Tensor(shape=(10,), dtype=float32),
            'minimum_l2_target_distance': Scalar(shape=(), dtype=float32),
            'minimum_visible_target_alignment': Scalar(shape=(), dtype=float32),
            'nav_object_bbox': Tensor(shape=(10,), dtype=float32),
            'relative_arm_location_metadata': Tensor(shape=(4,), dtype=float32),
            'room_current_seen': Scalar(shape=(), dtype=bool),
            'rooms_seen': Scalar(shape=(), dtype=int64),
            'visible_target_4m_count': Scalar(shape=(), dtype=int64),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                            | Class        | Shape         | Dtype   | Description
:------------------------------------------------- | :----------- | :------------ | :------ | :----------
                                                   | FeaturesDict |               |         |
episode_metadata                                   | FeaturesDict |               |         |
episode_metadata/file_path                         | Tensor       |               | string  |
episode_metadata/task_target_split                 | Tensor       |               | string  |
episode_metadata/task_type                         | Tensor       |               | string  |
steps                                              | Dataset      |               |         |
steps/action                                       | Tensor       | (9,)          | float32 |
steps/discount                                     | Scalar       |               | float32 |
steps/is_first                                     | Tensor       |               | bool    |
steps/is_last                                      | Tensor       |               | bool    |
steps/is_terminal                                  | Tensor       |               | bool    |
steps/language_instruction                         | Tensor       |               | string  |
steps/observation                                  | FeaturesDict |               |         |
steps/observation/an_object_is_in_hand             | Scalar       |               | bool    |
steps/observation/house_index                      | Scalar       |               | int64   |
steps/observation/hypothetical_task_success        | Scalar       |               | bool    |
steps/observation/image                            | Image        | (224, 384, 3) | uint8   |
steps/observation/image_manipulation               | Image        | (224, 384, 3) | uint8   |
steps/observation/last_action_is_random            | Scalar       |               | bool    |
steps/observation/last_action_str                  | Tensor       |               | string  |
steps/observation/last_action_success              | Scalar       |               | bool    |
steps/observation/last_agent_location              | Tensor       | (6,)          | float32 |
steps/observation/manip_object_bbox                | Tensor       | (10,)         | float32 |
steps/observation/minimum_l2_target_distance       | Scalar       |               | float32 |
steps/observation/minimum_visible_target_alignment | Scalar       |               | float32 |
steps/observation/nav_object_bbox                  | Tensor       | (10,)         | float32 |
steps/observation/relative_arm_location_metadata   | Tensor       | (4,)          | float32 |
steps/observation/room_current_seen                | Scalar       |               | bool    |
steps/observation/rooms_seen                       | Scalar       |               | int64   |
steps/observation/visible_target_4m_count          | Scalar       |               | int64   |
steps/reward                                       | Scalar       |               | float32 |

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
@article{spoc2023,
    author    = {Kiana Ehsani, Tanmay Gupta, Rose Hendrix, Jordi Salvador, Luca Weihs, Kuo-Hao Zeng, Kunal Pratap Singh, Yejin Kim, Winson Han, Alvaro Herrasti, Ranjay Krishna, Dustin Schwenk, Eli VanderBilt, Aniruddha Kembhavi},
    title     = {Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World},
    journal   = {arXiv},
    year      = {2023},
    eprint    = {2312.02976},
}
```

