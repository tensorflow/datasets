<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="mt_opt" />
  <meta itemprop="description" content="Datasets for the [MT-Opt paper](https://arxiv.org/abs/2104.08212).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;mt_opt&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/mt_opt" />
  <meta itemprop="sameAs" content="https://karolhausman.github.io/mt-opt/" />
  <meta itemprop="citation" content="@misc{kalashnikov2021mtopt,&#10;      title={MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale},&#10;      author={Dmitry Kalashnikov and Jacob Varley and Yevgen Chebotar and Benjamin Swanson and Rico Jonschkowski and Chelsea Finn and Sergey Levine and Karol Hausman},&#10;      year={2021},&#10;      eprint={2104.08212},&#10;      archivePrefix={arXiv},&#10;      primaryClass={cs.RO}&#10;}" />
</div>

# `mt_opt`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

Datasets for the [MT-Opt paper](https://arxiv.org/abs/2104.08212).

*   **Homepage**:
    [https://karolhausman.github.io/mt-opt/](https://karolhausman.github.io/mt-opt/)

*   **Source code**:
    [`tfds.robotics.mt_opt.MtOpt`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/mt_opt/mt_opt.py)

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
@misc{kalashnikov2021mtopt,
      title={MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale},
      author={Dmitry Kalashnikov and Jacob Varley and Yevgen Chebotar and Benjamin Swanson and Rico Jonschkowski and Chelsea Finn and Sergey Levine and Karol Hausman},
      year={2021},
      eprint={2104.08212},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```


## mt_opt/rlds (default config)

*   **Config description**: This dataset contains task episodes collected across
    a fleet of real robots.

*   **Features**:

```python
FeaturesDict({
    'episode_id': tf.string,
    'skill': tf.uint8,
    'steps': Dataset({
        'action': FeaturesDict({
            'close_gripper': tf.bool,
            'open_gripper': tf.bool,
            'target_pose': Tensor(shape=(7,), dtype=tf.float32),
            'terminate': tf.bool,
        }),
        'is_first': tf.bool,
        'is_last': tf.bool,
        'is_terminal': tf.bool,
        'observation': FeaturesDict({
            'gripper_closed': tf.bool,
            'height_to_bottom': tf.float32,
            'image': Image(shape=(512, 640, 3), dtype=tf.uint8),
            'state_dense': Tensor(shape=(7,), dtype=tf.float32),
        }),
    }),
    'task_code': tf.string,
})
```

## mt_opt/sd

*   **Config description**: The success detectors dataset that contains human
    curated definitions of tasks completion.

*   **Features**:

```python
FeaturesDict({
    'image_0': Image(shape=(512, 640, 3), dtype=tf.uint8),
    'image_1': Image(shape=(480, 640, 3), dtype=tf.uint8),
    'image_2': Image(shape=(480, 640, 3), dtype=tf.uint8),
    'success': tf.bool,
    'task_code': tf.string,
})
```
