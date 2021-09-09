<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="rlu_rwrl" />
  <meta itemprop="description" content="RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL&#10;Unplugged is designed around the following considerations: to facilitate ease of&#10;use, we provide the datasets with a unified API which makes it easy for the&#10;practitioner to work with all data in the suite once a general pipeline has been&#10;established.&#10;&#10;&#10;Examples in the dataset represent SAR transitions stored when running a&#10;partially online trained agent as described in https://arxiv.org/abs/1904.12901.&#10;We follow the RLDS dataset format, as specified in&#10;https://github.com/google-research/rlds#dataset-format.&#10;&#10;&#10;We release 40 datasets on 8 tasks in total -- with no combined challenge and&#10;easy combined challenge on the cartpole, walker, quadruped, and humanoid tasks.&#10;Each task contains 5 different sizes of datasets, 1%, 5%, 20%, 40%, and 100%.&#10;Note that the smaller dataset is not guaranteed to be a subset of the larger&#10;ones. For details on how the dataset was generated, please refer to the paper.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;rlu_rwrl&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/rlu_rwrl" />
  <meta itemprop="sameAs" content="https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged" />
  <meta itemprop="citation" content="@misc{gulcehre2020rl,&#10;    title={RL Unplugged: Benchmarks for Offline Reinforcement Learning},&#10;    author={Caglar Gulcehre and Ziyu Wang and Alexander Novikov and Tom Le Paine&#10;        and  Sergio Gómez Colmenarejo and Konrad Zolna and Rishabh Agarwal and&#10;        Josh Merel and Daniel Mankowitz and Cosmin Paduraru and Gabriel&#10;        Dulac-Arnold and Jerry Li and Mohammad Norouzi and Matt Hoffman and&#10;        Ofir Nachum and George Tucker and Nicolas Heess and Nando deFreitas},&#10;    year={2020},&#10;    eprint={2006.13888},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `rlu_rwrl`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

RL Unplugged is suite of benchmarks for offline reinforcement learning. The RL
Unplugged is designed around the following considerations: to facilitate ease of
use, we provide the datasets with a unified API which makes it easy for the
practitioner to work with all data in the suite once a general pipeline has been
established.

Examples in the dataset represent SAR transitions stored when running a
partially online trained agent as described in https://arxiv.org/abs/1904.12901.
We follow the RLDS dataset format, as specified in
https://github.com/google-research/rlds#dataset-format.

We release 40 datasets on 8 tasks in total -- with no combined challenge and
easy combined challenge on the cartpole, walker, quadruped, and humanoid tasks.
Each task contains 5 different sizes of datasets, 1%, 5%, 20%, 40%, and 100%.
Note that the smaller dataset is not guaranteed to be a subset of the larger
ones. For details on how the dataset was generated, please refer to the paper.

*   **Homepage**:
    [https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged](https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged)

*   **Source code**:
    [`tfds.rl_unplugged.rlu_rwrl.RluRwrl`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/rl_unplugged/rlu_rwrl/rlu_rwrl.py)

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
@misc{gulcehre2020rl,
    title={RL Unplugged: Benchmarks for Offline Reinforcement Learning},
    author={Caglar Gulcehre and Ziyu Wang and Alexander Novikov and Tom Le Paine
        and  Sergio Gómez Colmenarejo and Konrad Zolna and Rishabh Agarwal and
        Josh Merel and Daniel Mankowitz and Cosmin Paduraru and Gabriel
        Dulac-Arnold and Jerry Li and Mohammad Norouzi and Matt Hoffman and
        Ofir Nachum and George Tucker and Nicolas Heess and Nando deFreitas},
    year={2020},
    eprint={2006.13888},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

## rlu_rwrl/cartpole_swingup_combined_challenge_none_1_percent (default config)

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/cartpole_swingup_combined_challenge_none_5_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/cartpole_swingup_combined_challenge_none_20_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/cartpole_swingup_combined_challenge_none_40_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/cartpole_swingup_combined_challenge_none_100_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_none_1_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_none_5_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_none_20_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_none_40_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_none_100_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_none_1_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_none_5_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_none_20_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_none_40_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_none_100_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_none_1_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_none_5_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_none_20_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_none_40_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_none_100_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_1_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_5_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_20_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_40_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/cartpole_swingup_combined_challenge_easy_100_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(1,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'position': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(2,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_easy_1_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_easy_5_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_easy_20_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_easy_40_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/quadruped_walk_combined_challenge_easy_100_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(12,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'egocentric_state': Tensor(shape=(44,), dtype=tf.float32),
            'force_torque': Tensor(shape=(24,), dtype=tf.float32),
            'imu': Tensor(shape=(6,), dtype=tf.float32),
            'torso_upright': Tensor(shape=(1,), dtype=tf.float32),
            'torso_velocity': Tensor(shape=(3,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_easy_1_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_easy_5_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_easy_20_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_easy_40_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/walker_walk_combined_challenge_easy_100_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(6,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'height': Tensor(shape=(1,), dtype=tf.float32),
            'orientations': Tensor(shape=(14,), dtype=tf.float32),
            'velocity': Tensor(shape=(9,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_easy_1_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_easy_5_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_easy_20_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_easy_40_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```

## rlu_rwrl/humanoid_walk_combined_challenge_easy_100_percent

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.int64,
    'episode_return': tf.float32,
    'steps': Dataset({
        'action': Tensor(shape=(21,), dtype=tf.float32),
        'discount': Tensor(shape=(1,), dtype=tf.float32),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'com_velocity': Tensor(shape=(3,), dtype=tf.float32),
            'dummy-0': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-1': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-2': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-3': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-4': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-5': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-6': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-7': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-8': Tensor(shape=(1,), dtype=tf.float32),
            'dummy-9': Tensor(shape=(1,), dtype=tf.float32),
            'extremities': Tensor(shape=(12,), dtype=tf.float32),
            'head_height': Tensor(shape=(1,), dtype=tf.float32),
            'joint_angles': Tensor(shape=(21,), dtype=tf.float32),
            'torso_vertical': Tensor(shape=(3,), dtype=tf.float32),
            'velocity': Tensor(shape=(27,), dtype=tf.float32),
        }),
        'reward': Tensor(shape=(1,), dtype=tf.float32),
    }),
})
```
