<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="vima_converted_externally_to_rlds" />
  <meta itemprop="description" content="SIM dataset of a single robot arm performing procedurally-generated tabletop tasks with multimodal prompts, 600K+ trajectories&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;vima_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/vima_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://vimalabs.github.io/" />
  <meta itemprop="citation" content="@inproceedings{jiang2023vima,  title     = {VIMA: General Robot Manipulation with Multimodal Prompts},  author    = {Yunfan Jiang and Agrim Gupta and Zichen Zhang and Guanzhi Wang and Yongqiang Dou and Yanjun Chen and Li Fei-Fei and Anima Anandkumar and Yuke Zhu and Linxi Fan}, booktitle = {Fortieth International Conference on Machine Learning},  year      = {2023}. }" />
</div>

# `vima_converted_externally_to_rlds`


*   **Description**:

SIM dataset of a single robot arm performing procedurally-generated tabletop
tasks with multimodal prompts, 600K+ trajectories

*   **Homepage**: [https://vimalabs.github.io/](https://vimalabs.github.io/)

*   **Source code**:
    [`tfds.robotics.rtx.VimaConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

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
        'action_bounds': FeaturesDict({
            'high': Tensor(shape=(3,), dtype=float32),
            'low': Tensor(shape=(3,), dtype=float32),
        }),
        'end-effector type': string,
        'failure': Scalar(shape=(), dtype=bool),
        'file_path': string,
        'n_objects': Scalar(shape=(), dtype=int64),
        'num_steps': Scalar(shape=(), dtype=int64),
        'robot_components_seg_ids': Sequence(Scalar(shape=(), dtype=int64)),
        'seed': Scalar(shape=(), dtype=int64),
        'success': Scalar(shape=(), dtype=bool),
        'task': string,
    }),
    'steps': Dataset({
        'action': FeaturesDict({
            'pose0_position': Tensor(shape=(3,), dtype=float32),
            'pose0_rotation': Tensor(shape=(4,), dtype=float32),
            'pose1_position': Tensor(shape=(3,), dtype=float32),
            'pose1_rotation': Tensor(shape=(4,), dtype=float32),
        }),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'multimodal_instruction': string,
        'multimodal_instruction_assets': FeaturesDict({
            'asset_type': Sequence(string),
            'frontal_image': Sequence(Tensor(shape=(128, 256, 3), dtype=uint8)),
            'frontal_segmentation': Sequence(Tensor(shape=(128, 256), dtype=uint8)),
            'image': Sequence(Tensor(shape=(128, 256, 3), dtype=uint8)),
            'key_name': Sequence(string),
            'segmentation': Sequence(Tensor(shape=(128, 256), dtype=uint8)),
            'segmentation_obj_info': Sequence({
                'obj_name': Sequence(string),
                'segm_id': Sequence(Scalar(shape=(), dtype=int64)),
                'texture_name': Sequence(string),
            }),
        }),
        'observation': FeaturesDict({
            'ee': int64,
            'frontal_image': Tensor(shape=(128, 256, 3), dtype=uint8),
            'frontal_segmentation': Tensor(shape=(128, 256), dtype=uint8),
            'image': Tensor(shape=(128, 256, 3), dtype=uint8),
            'segmentation': Tensor(shape=(128, 256), dtype=uint8),
            'segmentation_obj_info': FeaturesDict({
                'obj_name': Sequence(string),
                'segm_id': Sequence(Scalar(shape=(), dtype=int64)),
                'texture_name': Sequence(string),
            }),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                                                | Class            | Shape               | Dtype   | Description
:--------------------------------------------------------------------- | :--------------- | :------------------ | :------ | :----------
                                                                       | FeaturesDict     |                     |         |
episode_metadata                                                       | FeaturesDict     |                     |         |
episode_metadata/action_bounds                                         | FeaturesDict     |                     |         |
episode_metadata/action_bounds/high                                    | Tensor           | (3,)                | float32 |
episode_metadata/action_bounds/low                                     | Tensor           | (3,)                | float32 |
episode_metadata/end-effector type                                     | Tensor           |                     | string  |
episode_metadata/failure                                               | Scalar           |                     | bool    |
episode_metadata/file_path                                             | Tensor           |                     | string  |
episode_metadata/n_objects                                             | Scalar           |                     | int64   |
episode_metadata/num_steps                                             | Scalar           |                     | int64   |
episode_metadata/robot_components_seg_ids                              | Sequence(Scalar) | (None,)             | int64   |
episode_metadata/seed                                                  | Scalar           |                     | int64   |
episode_metadata/success                                               | Scalar           |                     | bool    |
episode_metadata/task                                                  | Tensor           |                     | string  |
steps                                                                  | Dataset          |                     |         |
steps/action                                                           | FeaturesDict     |                     |         |
steps/action/pose0_position                                            | Tensor           | (3,)                | float32 |
steps/action/pose0_rotation                                            | Tensor           | (4,)                | float32 |
steps/action/pose1_position                                            | Tensor           | (3,)                | float32 |
steps/action/pose1_rotation                                            | Tensor           | (4,)                | float32 |
steps/discount                                                         | Scalar           |                     | float32 |
steps/is_first                                                         | Tensor           |                     | bool    |
steps/is_last                                                          | Tensor           |                     | bool    |
steps/is_terminal                                                      | Tensor           |                     | bool    |
steps/multimodal_instruction                                           | Tensor           |                     | string  |
steps/multimodal_instruction_assets                                    | FeaturesDict     |                     |         |
steps/multimodal_instruction_assets/asset_type                         | Sequence(Tensor) | (None,)             | string  |
steps/multimodal_instruction_assets/frontal_image                      | Sequence(Tensor) | (None, 128, 256, 3) | uint8   |
steps/multimodal_instruction_assets/frontal_segmentation               | Sequence(Tensor) | (None, 128, 256)    | uint8   |
steps/multimodal_instruction_assets/image                              | Sequence(Tensor) | (None, 128, 256, 3) | uint8   |
steps/multimodal_instruction_assets/key_name                           | Sequence(Tensor) | (None,)             | string  |
steps/multimodal_instruction_assets/segmentation                       | Sequence(Tensor) | (None, 128, 256)    | uint8   |
steps/multimodal_instruction_assets/segmentation_obj_info              | Sequence         |                     |         |
steps/multimodal_instruction_assets/segmentation_obj_info/obj_name     | Sequence(Tensor) | (None,)             | string  |
steps/multimodal_instruction_assets/segmentation_obj_info/segm_id      | Sequence(Scalar) | (None,)             | int64   |
steps/multimodal_instruction_assets/segmentation_obj_info/texture_name | Sequence(Tensor) | (None,)             | string  |
steps/observation                                                      | FeaturesDict     |                     |         |
steps/observation/ee                                                   | Tensor           |                     | int64   |
steps/observation/frontal_image                                        | Tensor           | (128, 256, 3)       | uint8   |
steps/observation/frontal_segmentation                                 | Tensor           | (128, 256)          | uint8   |
steps/observation/image                                                | Tensor           | (128, 256, 3)       | uint8   |
steps/observation/segmentation                                         | Tensor           | (128, 256)          | uint8   |
steps/observation/segmentation_obj_info                                | FeaturesDict     |                     |         |
steps/observation/segmentation_obj_info/obj_name                       | Sequence(Tensor) | (None,)             | string  |
steps/observation/segmentation_obj_info/segm_id                        | Sequence(Scalar) | (None,)             | int64   |
steps/observation/segmentation_obj_info/texture_name                   | Sequence(Tensor) | (None,)             | string  |
steps/reward                                                           | Scalar           |                     | float32 |

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
@inproceedings{jiang2023vima,  title     = {VIMA: General Robot Manipulation with Multimodal Prompts},  author    = {Yunfan Jiang and Agrim Gupta and Zichen Zhang and Guanzhi Wang and Yongqiang Dou and Yanjun Chen and Li Fei-Fei and Anima Anandkumar and Yuke Zhu and Linxi Fan}, booktitle = {Fortieth International Conference on Machine Learning},  year      = {2023}. }
```

