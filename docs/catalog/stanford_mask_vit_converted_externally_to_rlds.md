<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="stanford_mask_vit_converted_externally_to_rlds" />
  <meta itemprop="description" content="Sawyer pushing and picking objects in a bin&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;stanford_mask_vit_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/stanford_mask_vit_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="https://arxiv.org/abs/2206.11894" />
  <meta itemprop="citation" content="@inproceedings{gupta2022maskvit,&#10;  title={MaskViT: Masked Visual Pre-Training for Video Prediction},&#10;  author={Agrim Gupta and Stephen Tian and Yunzhi Zhang and Jiajun Wu and Roberto Martín-Martín and Li Fei-Fei},&#10;  booktitle={International Conference on Learning Representations},&#10;  year={2022}&#10;}" />
</div>

# `stanford_mask_vit_converted_externally_to_rlds`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Sawyer pushing and picking objects in a bin

*   **Homepage**:
    [https://arxiv.org/abs/2206.11894](https://arxiv.org/abs/2206.11894)

*   **Source code**:
    [`tfds.robotics.rtx.StanfordMaskVitConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `76.17 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 9,109
`'val'`   | 91

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(5,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'end_effector_pose': Tensor(shape=(5,), dtype=float32),
            'finger_sensors': Tensor(shape=(1,), dtype=float32),
            'high_bound': Tensor(shape=(5,), dtype=float32),
            'image': Image(shape=(480, 480, 3), dtype=uint8),
            'low_bound': Tensor(shape=(5,), dtype=float32),
            'state': Tensor(shape=(15,), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                             | Class        | Shape         | Dtype   | Description
:---------------------------------- | :----------- | :------------ | :------ | :----------
                                    | FeaturesDict |               |         |
episode_metadata                    | FeaturesDict |               |         |
episode_metadata/file_path          | Text         |               | string  | Path to the original data file.
steps                               | Dataset      |               |         |
steps/action                        | Tensor       | (5,)          | float32 | Robot action, consists of [3x change in end effector position, 1x gripper yaw, 1x open/close gripper (-1 means to open the gripper, 1 means close)].
steps/discount                      | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first                      | Tensor       |               | bool    |
steps/is_last                       | Tensor       |               | bool    |
steps/is_terminal                   | Tensor       |               | bool    |
steps/language_embedding            | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction          | Text         |               | string  | Language Instruction.
steps/observation                   | FeaturesDict |               |         |
steps/observation/end_effector_pose | Tensor       | (5,)          | float32 | Robot end effector pose, consists of [3x Cartesian position, 1x gripper yaw, 1x gripper position]. This is the state used in the MaskViT paper.
steps/observation/finger_sensors    | Tensor       | (1,)          | float32 | 1x Sawyer gripper finger sensors.
steps/observation/high_bound        | Tensor       | (5,)          | float32 | High bound for end effector pose normalization. Consists of [3x Cartesian position, 1x gripper yaw, 1x gripper position].
steps/observation/image             | Image        | (480, 480, 3) | uint8   | Main camera RGB observation.
steps/observation/low_bound         | Tensor       | (5,)          | float32 | Low bound for end effector pose normalization. Consists of [3x Cartesian position, 1x gripper yaw, 1x gripper position].
steps/observation/state             | Tensor       | (15,)         | float32 | Robot state, consists of [7x robot joint angles, 7x robot joint velocities,1x gripper position].
steps/reward                        | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
@inproceedings{gupta2022maskvit,
  title={MaskViT: Masked Visual Pre-Training for Video Prediction},
  author={Agrim Gupta and Stephen Tian and Yunzhi Zhang and Jiajun Wu and Roberto Martín-Martín and Li Fei-Fei},
  booktitle={International Conference on Learning Representations},
  year={2022}
}
```

