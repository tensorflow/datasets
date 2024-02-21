<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="kaist_nonprehensile_converted_externally_to_rlds" />
  <meta itemprop="description" content="Franka manipulating ungraspable objects&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;kaist_nonprehensile_converted_externally_to_rlds&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/kaist_nonprehensile_converted_externally_to_rlds" />
  <meta itemprop="sameAs" content="--" />
  <meta itemprop="citation" content="@article{kimpre,&#10;  title={Pre-and post-contact policy decomposition for non-prehensile manipulation with zero-shot sim-to-real transfer},&#10;  author={Kim, Minchan and Han, Junhyek and Kim, Jaehyung and Kim, Beomjoon},&#10;  booktitle={2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},&#10;  year={2023},&#10;  organization={IEEE}&#10;}" />
</div>

# `kaist_nonprehensile_converted_externally_to_rlds`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Franka manipulating ungraspable objects

*   **Homepage**: [--](--)

*   **Source code**:
    [`tfds.robotics.rtx.KaistNonprehensileConvertedExternallyToRlds`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `11.71 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 201

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(20,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(480, 640, 3), dtype=uint8),
            'partial_pointcloud': Tensor(shape=(512, 3), dtype=float32),
            'state': Tensor(shape=(21,), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                              | Class        | Shape         | Dtype   | Description
:----------------------------------- | :----------- | :------------ | :------ | :----------
                                     | FeaturesDict |               |         |
episode_metadata                     | FeaturesDict |               |         |
episode_metadata/file_path           | Text         |               | string  | Path to the original data file.
steps                                | Dataset      |               |         |
steps/action                         | Tensor       | (20,)         | float32 | Robot action, consists of [3x end-effector position residual, 3x end-effector axis-angle residual, 7x robot joint k_p gain coefficient, 7x robot joint damping ratio coefficient].The action residuals are global, i.e. multiplied on theleft-hand side of the current end-effector state.
steps/discount                       | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first                       | Tensor       |               | bool    |
steps/is_last                        | Tensor       |               | bool    |
steps/is_terminal                    | Tensor       |               | bool    |
steps/language_embedding             | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction           | Text         |               | string  | Language Instruction.
steps/observation                    | FeaturesDict |               |         |
steps/observation/image              | Image        | (480, 640, 3) | uint8   | Main camera RGB observation.
steps/observation/partial_pointcloud | Tensor       | (512, 3)      | float32 | Partial pointcloud observation
steps/observation/state              | Tensor       | (21,)         | float32 | Robot state, consists of [joint_states, end_effector_pose].Joint states are 14-dimensional, formatted in the order of [q_0, w_0, q_1, w_0, ...].In other words, joint positions and velocities are interleaved.The end-effector pose is 7-dimensional, formatted in the order of [position, quaternion].The quaternion is formatted in (x,y,z,w) order. The end-effector pose references the tool frame, in the center of the two fingers of the gripper.
steps/reward                         | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
@article{kimpre,
  title={Pre-and post-contact policy decomposition for non-prehensile manipulation with zero-shot sim-to-real transfer},
  author={Kim, Minchan and Han, Junhyek and Kim, Jaehyung and Kim, Beomjoon},
  booktitle={2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year={2023},
  organization={IEEE}
}
```

