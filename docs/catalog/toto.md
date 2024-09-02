<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="toto" />
  <meta itemprop="description" content="Franka scooping and pouring tasks&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;toto&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/toto" />
  <meta itemprop="sameAs" content="https://toto-benchmark.org/" />
  <meta itemprop="citation" content="@inproceedings{zhou2023train,&#10;  author={Zhou, Gaoyue and Dean, Victoria and Srirama, Mohan Kumar and Rajeswaran, Aravind and Pari, Jyothish and Hatch, Kyle and Jain, Aryan and Yu, Tianhe and Abbeel, Pieter and Pinto, Lerrel and Finn, Chelsea and Gupta, Abhinav},&#10;  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)}, &#10;  title={Train Offline, Test Online: A Real Robot Learning Benchmark}, &#10;  year={2023},&#10; }" />
</div>

# `toto`


*   **Description**:

Franka scooping and pouring tasks

*   **Homepage**: [https://toto-benchmark.org/](https://toto-benchmark.org/)

*   **Source code**:
    [`tfds.robotics.rtx.Toto`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

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
    'steps': Dataset({
        'action': FeaturesDict({
            'open_gripper': bool,
            'rotation_delta': Tensor(shape=(3,), dtype=float32),
            'terminate_episode': float32,
            'world_vector': Tensor(shape=(3,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'image': Image(shape=(480, 640, 3), dtype=uint8),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
            'state': Tensor(shape=(7,), dtype=float32, description=numpy array of shape (7,). Contains the robot joint states (as absolute joint angles) at each timestep),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                        | Class        | Shape         | Dtype   | Description
:--------------------------------------------- | :----------- | :------------ | :------ | :----------
                                               | FeaturesDict |               |         |
steps                                          | Dataset      |               |         |
steps/action                                   | FeaturesDict |               |         |
steps/action/open_gripper                      | Tensor       |               | bool    |
steps/action/rotation_delta                    | Tensor       | (3,)          | float32 |
steps/action/terminate_episode                 | Tensor       |               | float32 |
steps/action/world_vector                      | Tensor       | (3,)          | float32 |
steps/is_first                                 | Tensor       |               | bool    |
steps/is_last                                  | Tensor       |               | bool    |
steps/is_terminal                              | Tensor       |               | bool    |
steps/observation                              | FeaturesDict |               |         |
steps/observation/image                        | Image        | (480, 640, 3) | uint8   |
steps/observation/natural_language_embedding   | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction | Tensor       |               | string  |
steps/observation/state                        | Tensor       | (7,)          | float32 | numpy array of shape (7,). Contains the robot joint states (as absolute joint angles) at each timestep
steps/reward                                   | Scalar       |               | float32 |

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
@inproceedings{zhou2023train,
  author={Zhou, Gaoyue and Dean, Victoria and Srirama, Mohan Kumar and Rajeswaran, Aravind and Pari, Jyothish and Hatch, Kyle and Jain, Aryan and Yu, Tianhe and Abbeel, Pieter and Pinto, Lerrel and Finn, Chelsea and Gupta, Abhinav},
  booktitle={2023 IEEE International Conference on Robotics and Automation (ICRA)},
  title={Train Offline, Test Online: A Real Robot Learning Benchmark},
  year={2023},
 }
```

