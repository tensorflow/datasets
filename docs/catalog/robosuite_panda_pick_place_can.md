<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="robosuite_panda_pick_place_can" />
  <meta itemprop="description" content="These datasets have been created with the PickPlaceCan environment of the&#10;[robosuite robotic arm simulator](https://robosuite.ai/).&#10;`human_dc29b40a` is a set of 50 episodes recorded by a single operator using&#10;the [RLDS Creator](https://github.com/google-research/rlds-creator) and a&#10;gamepad controller. Episodes consist of 400 steps. In each episode, a tag is&#10;added when the task is completed, this tag is stored as part of the custom step&#10;metadata .&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;robosuite_panda_pick_place_can&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/robosuite_panda_pick_place_can" />
  <meta itemprop="sameAs" content="https://www.tensorflow.org/datasets/catalog/robosuite_panda_pick_place_can" />
  <meta itemprop="citation" content="@misc{google-research, title={RLDS},&#10;url={https://github.com/google-research/rlds}, journal={GitHub},&#10;author={S. Ramos, S. Girgin et al.}}" />
</div>

# `robosuite_panda_pick_place_can`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

These datasets have been created with the PickPlaceCan environment of the
[robosuite robotic arm simulator](https://robosuite.ai/). `human_dc29b40a` is a
set of 50 episodes recorded by a single operator using the
[RLDS Creator](https://github.com/google-research/rlds-creator) and a gamepad
controller. Episodes consist of 400 steps. In each episode, a tag is added when
the task is completed, this tag is stored as part of the custom step metadata .

*   **Homepage**:
    [https://www.tensorflow.org/datasets/catalog/robosuite_panda_pick_place_can](https://www.tensorflow.org/datasets/catalog/robosuite_panda_pick_place_can)

*   **Source code**:
    [`tfds.rlds.robosuite_panda_pick_place_can.RobosuitePandaPickPlaceCan`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/rlds/robosuite_panda_pick_place_can/robosuite_panda_pick_place_can.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

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
@misc{google-research, title={RLDS},
url={https://github.com/google-research/rlds}, journal={GitHub},
author={S. Ramos, S. Girgin et al.}}
```

## robosuite_panda_pick_place_can/human_dc29b40a (default config)

*   **Config description**: Human generated dataset.

*   **Features**:

```python
FeaturesDict({
    'agent_id': tf.string,
    'episode_id': tf.string,
    'episode_index': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float64),
        'discount': tf.float64,
        'image': Image(shape=(None, None, 3), dtype=tf.uint8),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'Can_pos': Tensor(shape=(3,), dtype=tf.float64),
            'Can_quat': Tensor(shape=(4,), dtype=tf.float64),
            'Can_to_robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'Can_to_robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float32),
            'object-state': Tensor(shape=(14,), dtype=tf.float64),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float64),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float64),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float64),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float64),
            'robot0_proprio-state': Tensor(shape=(32,), dtype=tf.float64),
        }),
        'reward': tf.float64,
        'tag:placed': tf.bool,
    }),
})
```

## robosuite_panda_pick_place_can/synthetic_stochastic_sac_afe13968

*   **Config description**: Synthetic dataset.

*   **Features**:

```python
FeaturesDict({
    'agent_id': tf.string,
    'episode_id': tf.string,
    'episode_index': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(7,), dtype=tf.float32),
        'discount': tf.float64,
        'image': Image(shape=(None, None, 3), dtype=tf.uint8),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'Can_pos': Tensor(shape=(3,), dtype=tf.float32),
            'Can_quat': Tensor(shape=(4,), dtype=tf.float32),
            'Can_to_robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float32),
            'Can_to_robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float32),
            'object-state': Tensor(shape=(14,), dtype=tf.float32),
            'robot0_eef_pos': Tensor(shape=(3,), dtype=tf.float32),
            'robot0_eef_quat': Tensor(shape=(4,), dtype=tf.float32),
            'robot0_gripper_qpos': Tensor(shape=(2,), dtype=tf.float32),
            'robot0_gripper_qvel': Tensor(shape=(2,), dtype=tf.float32),
            'robot0_joint_pos_cos': Tensor(shape=(7,), dtype=tf.float32),
            'robot0_joint_pos_sin': Tensor(shape=(7,), dtype=tf.float32),
            'robot0_joint_vel': Tensor(shape=(7,), dtype=tf.float32),
            'robot0_proprio-state': Tensor(shape=(32,), dtype=tf.float32),
        }),
        'reward': tf.float64,
        'tag:placed': tf.bool,
    }),
})
```
