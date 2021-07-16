<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="d4rl_mujoco_ant" />
  <meta itemprop="description" content="D4RL is an open-source benchmark for offline reinforcement learning. It provides&#10;standardized environments and datasets for training and benchmarking algorithms.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;d4rl_mujoco_ant&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/d4rl_mujoco_ant" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/d4rl/home" />
  <meta itemprop="citation" content="@misc{fu2020d4rl,&#10;    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},&#10;    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},&#10;    year={2020},&#10;    eprint={2004.07219},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `d4rl_mujoco_ant`


Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

*   **Description**:

D4RL is an open-source benchmark for offline reinforcement learning. It provides
standardized environments and datasets for training and benchmarking algorithms.

*   **Homepage**:
    [https://sites.google.com/view/d4rl/home](https://sites.google.com/view/d4rl/home)

*   **Source code**:
    [`tfds.d4rl.d4rl_mujoco_ant.D4rlMujocoAnt`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/d4rl/d4rl_mujoco_ant/d4rl_mujoco_ant.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`1.1.0`** (default)
        <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>:
        Added is_last.

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
@misc{fu2020d4rl,
    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},
    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},
    year={2020},
    eprint={2004.07219},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

## d4rl_mujoco_ant/v0-expert (default config)

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v0-medium

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v0-medium-expert

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v0-mixed

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v0-random

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v1-expert

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 111), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 256), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=tf.float32),
            'weight': Tensor(shape=(8, 256), dtype=tf.float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=tf.float32),
            'weight': Tensor(shape=(8, 256), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(15,), dtype=tf.float32),
            'qvel': Tensor(shape=(14,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v1-medium

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 111), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 256), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=tf.float32),
            'weight': Tensor(shape=(8, 256), dtype=tf.float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=tf.float32),
            'weight': Tensor(shape=(8, 256), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(15,), dtype=tf.float32),
            'qvel': Tensor(shape=(14,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v1-medium-expert

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(15,), dtype=tf.float32),
            'qvel': Tensor(shape=(14,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v1-medium-replay

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float64),
        'discount': tf.float64,
        'infos': FeaturesDict({
            'action_log_probs': tf.float64,
            'qpos': Tensor(shape=(15,), dtype=tf.float64),
            'qvel': Tensor(shape=(14,), dtype=tf.float64),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float64),
        'reward': tf.float64,
    }),
})
```

## d4rl_mujoco_ant/v1-full-replay

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float64),
        'discount': tf.float64,
        'infos': FeaturesDict({
            'action_log_probs': tf.float64,
            'qpos': Tensor(shape=(15,), dtype=tf.float64),
            'qvel': Tensor(shape=(14,), dtype=tf.float64),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float64),
        'reward': tf.float64,
    }),
})
```

## d4rl_mujoco_ant/v1-random

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(15,), dtype=tf.float32),
            'qvel': Tensor(shape=(14,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v2-expert

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 111), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 256), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=tf.float32),
            'weight': Tensor(shape=(8, 256), dtype=tf.float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=tf.float32),
            'weight': Tensor(shape=(8, 256), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(15,), dtype=tf.float32),
            'qvel': Tensor(shape=(14,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v2-full-replay

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float64),
        'discount': tf.float64,
        'infos': FeaturesDict({
            'action_log_probs': tf.float64,
            'qpos': Tensor(shape=(15,), dtype=tf.float64),
            'qvel': Tensor(shape=(14,), dtype=tf.float64),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float64),
        'reward': tf.float64,
    }),
})
```

## d4rl_mujoco_ant/v2-medium

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 111), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 256), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=tf.float32),
            'weight': Tensor(shape=(8, 256), dtype=tf.float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(8,), dtype=tf.float32),
            'weight': Tensor(shape=(8, 256), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(15,), dtype=tf.float32),
            'qvel': Tensor(shape=(14,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v2-medium-expert

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(15,), dtype=tf.float32),
            'qvel': Tensor(shape=(14,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_mujoco_ant/v2-medium-replay

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'iteration': tf.int32,
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float64),
        'discount': tf.float64,
        'infos': FeaturesDict({
            'action_log_probs': tf.float64,
            'qpos': Tensor(shape=(15,), dtype=tf.float64),
            'qvel': Tensor(shape=(14,), dtype=tf.float64),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float64),
        'reward': tf.float64,
    }),
})
```

## d4rl_mujoco_ant/v2-random

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(8,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_probs': tf.float32,
            'qpos': Tensor(shape=(15,), dtype=tf.float32),
            'qvel': Tensor(shape=(14,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(111,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```
