<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="nyu_door_opening_surprising_effectiveness" />
  <meta itemprop="description" content="Hello robot opening cabinets, microwaves etc&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;nyu_door_opening_surprising_effectiveness&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/nyu_door_opening_surprising_effectiveness" />
  <meta itemprop="sameAs" content="https://jyopari.github.io/VINN/" />
  <meta itemprop="citation" content="@misc{pari2021surprising,&#10;    title={The Surprising Effectiveness of Representation Learning for Visual Imitation}, &#10;    author={Jyothish Pari and Nur Muhammad Shafiullah and Sridhar Pandian Arunachalam and Lerrel Pinto},&#10;    year={2021},&#10;    eprint={2112.01511},&#10;    archivePrefix={arXiv},&#10;    primaryClass={cs.RO}&#10;}" />
</div>

# `nyu_door_opening_surprising_effectiveness`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Hello robot opening cabinets, microwaves etc

*   **Homepage**:
    [https://jyopari.github.io/VINN/](https://jyopari.github.io/VINN/)

*   **Source code**:
    [`tfds.robotics.rtx.NyuDoorOpeningSurprisingEffectiveness`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

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
            'gripper_closedness_action': Tensor(shape=(1,), dtype=float32),
            'rotation_delta': Tensor(shape=(3,), dtype=float32),
            'terminate_episode': float32,
            'world_vector': Tensor(shape=(3,), dtype=float32),
        }),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'observation': FeaturesDict({
            'image': Image(shape=(720, 960, 3), dtype=uint8),
            'natural_language_embedding': Tensor(shape=(512,), dtype=float32),
            'natural_language_instruction': string,
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
steps/action/gripper_closedness_action         | Tensor       | (1,)          | float32 |
steps/action/rotation_delta                    | Tensor       | (3,)          | float32 | Angular velocity around x, y and z axis.
steps/action/terminate_episode                 | Tensor       |               | float32 |
steps/action/world_vector                      | Tensor       | (3,)          | float32 | Velocity in XYZ.
steps/is_first                                 | Tensor       |               | bool    |
steps/is_last                                  | Tensor       |               | bool    |
steps/is_terminal                              | Tensor       |               | bool    |
steps/observation                              | FeaturesDict |               |         |
steps/observation/image                        | Image        | (720, 960, 3) | uint8   |
steps/observation/natural_language_embedding   | Tensor       | (512,)        | float32 |
steps/observation/natural_language_instruction | Tensor       |               | string  |
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
@misc{pari2021surprising,
    title={The Surprising Effectiveness of Representation Learning for Visual Imitation},
    author={Jyothish Pari and Nur Muhammad Shafiullah and Sridhar Pandian Arunachalam and Lerrel Pinto},
    year={2021},
    eprint={2112.01511},
    archivePrefix={arXiv},
    primaryClass={cs.RO}
}
```

