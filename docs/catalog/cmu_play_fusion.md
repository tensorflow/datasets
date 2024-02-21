<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cmu_play_fusion" />
  <meta itemprop="description" content="The robot plays with 3 complex scenes: a grill with many cooking objects like toaster, pan, etc. It has to pick, open, place, close. It  has to set a table, move plates, cups, utensils. And it has to place dishes in the sink, dishwasher, hand cups etc.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cmu_play_fusion&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cmu_play_fusion" />
  <meta itemprop="sameAs" content="https://play-fusion.github.io/" />
  <meta itemprop="citation" content="@inproceedings{chen2023playfusion,&#10;  title={PlayFusion: Skill Acquisition via Diffusion from Language-Annotated Play},&#10;  author={Chen, Lili and Bahl, Shikhar and Pathak, Deepak},&#10;  booktitle={CoRL},&#10;  year={2023}&#10;}" />
</div>

# `cmu_play_fusion`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

The robot plays with 3 complex scenes: a grill with many cooking objects like
toaster, pan, etc. It has to pick, open, place, close. It has to set a table,
move plates, cups, utensils. And it has to place dishes in the sink, dishwasher,
hand cups etc.

*   **Homepage**:
    [https://play-fusion.github.io/](https://play-fusion.github.io/)

*   **Source code**:
    [`tfds.robotics.rtx.CmuPlayFusion`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/robotics/rtx/rtx.py)

*   **Versions**:

    *   **`0.1.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `6.68 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split     | Examples
:-------- | -------:
`'train'` | 576

*   **Feature structure**:

```python
FeaturesDict({
    'episode_metadata': FeaturesDict({
        'file_path': Text(shape=(), dtype=string),
    }),
    'steps': Dataset({
        'action': Tensor(shape=(9,), dtype=float32),
        'discount': Scalar(shape=(), dtype=float32),
        'is_first': bool,
        'is_last': bool,
        'is_terminal': bool,
        'language_embedding': Tensor(shape=(512,), dtype=float32),
        'language_instruction': Text(shape=(), dtype=string),
        'observation': FeaturesDict({
            'image': Image(shape=(128, 128, 3), dtype=uint8),
            'state': Tensor(shape=(8,), dtype=float32),
        }),
        'reward': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                    | Class        | Shape         | Dtype   | Description
:------------------------- | :----------- | :------------ | :------ | :----------
                           | FeaturesDict |               |         |
episode_metadata           | FeaturesDict |               |         |
episode_metadata/file_path | Text         |               | string  | Path to the original data file.
steps                      | Dataset      |               |         |
steps/action               | Tensor       | (9,)          | float32 | Robot action, consists of [7x delta eef (pos + quat), 1x gripper open/close (binary), 1x terminate episode].
steps/discount             | Scalar       |               | float32 | Discount if provided, default to 1.
steps/is_first             | Tensor       |               | bool    |
steps/is_last              | Tensor       |               | bool    |
steps/is_terminal          | Tensor       |               | bool    |
steps/language_embedding   | Tensor       | (512,)        | float32 | Kona language embedding. See https://tfhub.dev/google/universal-sentence-encoder-large/5
steps/language_instruction | Text         |               | string  | Language Instruction.
steps/observation          | FeaturesDict |               |         |
steps/observation/image    | Image        | (128, 128, 3) | uint8   | Main camera RGB observation.
steps/observation/state    | Tensor       | (8,)          | float32 | Robot state, consists of [7x robot joint angles, 1x gripper position.
steps/reward               | Scalar       |               | float32 | Reward if provided, 1 on final step for demos.

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
@inproceedings{chen2023playfusion,
  title={PlayFusion: Skill Acquisition via Diffusion from Language-Annotated Play},
  author={Chen, Lili and Bahl, Shikhar and Pathak, Deepak},
  booktitle={CoRL},
  year={2023}
}
```

