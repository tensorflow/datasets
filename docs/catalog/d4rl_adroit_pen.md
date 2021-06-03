<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="d4rl_adroit_pen" />
  <meta itemprop="description" content="D4RL is an open-source benchmark for offline reinforcement learning. It provides&#10;standardized environments and datasets for training and benchmarking algorithms.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;d4rl_adroit_pen&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/d4rl_adroit_pen" />
  <meta itemprop="sameAs" content="https://sites.google.com/view/d4rl/home" />
  <meta itemprop="citation" content="@misc{fu2020d4rl,&#10;    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},&#10;    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},&#10;    year={2020},&#10;    eprint={2004.07219},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.LG}&#10;}" />
</div>

# `d4rl_adroit_pen`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

D4RL is an open-source benchmark for offline reinforcement learning. It provides
standardized environments and datasets for training and benchmarking algorithms.

*   **Homepage**:
    [https://sites.google.com/view/d4rl/home](https://sites.google.com/view/d4rl/home)

*   **Source code**:
    [`tfds.d4rl.d4rl_adroit_pen.D4rlAdroitPen`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/d4rl/d4rl_adroit_pen/d4rl_adroit_pen.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

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

## d4rl_adroit_pen/v0-human (default config)

*   **Download size**: `1.94 MiB`

*   **Dataset size**: `2.52 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 50

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(24,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'qpos': Tensor(shape=(30,), dtype=tf.float32),
            'qvel': Tensor(shape=(30,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(45,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_adroit_pen/v0-cloned

*   **Download size**: `292.85 MiB`

*   **Dataset size**: `251.96 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,023

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(24,), dtype=tf.float32),
        'discount': tf.float64,
        'infos': FeaturesDict({
            'qpos': Tensor(shape=(30,), dtype=tf.float64),
            'qvel': Tensor(shape=(30,), dtype=tf.float64),
        }),
        'is_first': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(45,), dtype=tf.float64),
        'reward': tf.float64,
    }),
})
```

## d4rl_adroit_pen/v0-expert

*   **Download size**: `250.13 MiB`

*   **Dataset size**: `343.83 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,000

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(24,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_logstd': Tensor(shape=(24,), dtype=tf.float32),
            'action_mean': Tensor(shape=(24,), dtype=tf.float32),
            'qpos': Tensor(shape=(30,), dtype=tf.float32),
            'qvel': Tensor(shape=(30,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(45,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_adroit_pen/v1-human

*   **Download size**: `1.95 MiB`

*   **Dataset size**: `2.59 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 25

*   **Features**:

```python
FeaturesDict({
    'steps': Dataset({
        'action': Tensor(shape=(24,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'desired_orien': Tensor(shape=(4,), dtype=tf.float32),
            'qpos': Tensor(shape=(30,), dtype=tf.float32),
            'qvel': Tensor(shape=(30,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(45,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_adroit_pen/v1-cloned

*   **Download size**: `147.89 MiB`

*   **Dataset size**: `1.43 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 3,755

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(45, 256), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(256,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 256), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(24,), dtype=tf.float32),
            'weight': Tensor(shape=(256, 24), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(24,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'desired_orien': Tensor(shape=(4,), dtype=tf.float32),
            'qpos': Tensor(shape=(30,), dtype=tf.float32),
            'qvel': Tensor(shape=(30,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(45,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```

## d4rl_adroit_pen/v1-expert

*   **Download size**: `249.90 MiB`

*   **Dataset size**: `547.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 5,000

*   **Features**:

```python
FeaturesDict({
    'algorithm': tf.string,
    'policy': FeaturesDict({
        'fc0': FeaturesDict({
            'bias': Tensor(shape=(64,), dtype=tf.float32),
            'weight': Tensor(shape=(64, 45), dtype=tf.float32),
        }),
        'fc1': FeaturesDict({
            'bias': Tensor(shape=(64,), dtype=tf.float32),
            'weight': Tensor(shape=(64, 64), dtype=tf.float32),
        }),
        'last_fc': FeaturesDict({
            'bias': Tensor(shape=(24,), dtype=tf.float32),
            'weight': Tensor(shape=(24, 64), dtype=tf.float32),
        }),
        'last_fc_log_std': FeaturesDict({
            'bias': Tensor(shape=(24,), dtype=tf.float32),
            'weight': Tensor(shape=(24, 64), dtype=tf.float32),
        }),
        'nonlinearity': tf.string,
        'output_distribution': tf.string,
    }),
    'steps': Dataset({
        'action': Tensor(shape=(24,), dtype=tf.float32),
        'discount': tf.float32,
        'infos': FeaturesDict({
            'action_log_std': Tensor(shape=(24,), dtype=tf.float32),
            'action_mean': Tensor(shape=(24,), dtype=tf.float32),
            'desired_orien': Tensor(shape=(4,), dtype=tf.float32),
            'qpos': Tensor(shape=(30,), dtype=tf.float32),
            'qvel': Tensor(shape=(30,), dtype=tf.float32),
        }),
        'is_first': tf.bool,
        'is_terminal': tf.bool,
        'observation': Tensor(shape=(45,), dtype=tf.float32),
        'reward': tf.float32,
    }),
})
```
