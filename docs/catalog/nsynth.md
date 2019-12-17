<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="nsynth" />
  <meta itemprop="description" content="The NSynth Dataset is an audio dataset containing ~300k musical notes, each&#10;with a unique pitch, timbre, and envelope. Each note is annotated with three&#10;additional pieces of information based on a combination of human evaluation&#10;and heuristic algorithms: Source, Family, and Qualities.&#10;&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load('nsynth', split='train')&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/nsynth" />
  <meta itemprop="sameAs" content="https://g.co/magenta/nsynth-dataset" />
  <meta itemprop="citation" content="@InProceedings{pmlr-v70-engel17a,&#10;  title =     {Neural Audio Synthesis of Musical Notes with {W}ave{N}et Autoencoders},&#10;  author =     {Jesse Engel and Cinjon Resnick and Adam Roberts and Sander Dieleman and Mohammad Norouzi and Douglas Eck and Karen Simonyan},&#10;  booktitle =    {Proceedings of the 34th International Conference on Machine Learning},&#10;  pages =   {1068--1077},&#10;  year =      {2017},&#10;  editor =      {Doina Precup and Yee Whye Teh},&#10;  volume =     {70},&#10;  series =    {Proceedings of Machine Learning Research},&#10;  address =     {International Convention Centre, Sydney, Australia},&#10;  month =     {06--11 Aug},&#10;  publisher =     {PMLR},&#10;  pdf =     {http://proceedings.mlr.press/v70/engel17a/engel17a.pdf},&#10;  url =   {http://proceedings.mlr.press/v70/engel17a.html},&#10;}&#10;" />
</div>

# `nsynth`

The NSynth Dataset is an audio dataset containing ~300k musical notes, each with
a unique pitch, timbre, and envelope. Each note is annotated with three
additional pieces of information based on a combination of human evaluation and
heuristic algorithms: Source, Family, and Qualities.

*   URL:
    [https://g.co/magenta/nsynth-dataset](https://g.co/magenta/nsynth-dataset)
*   `DatasetBuilder`:
    [`tfds.audio.nsynth.Nsynth`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/nsynth.py)

`nsynth` is configured with `tfds.audio.nsynth.NsynthConfig` and has the
following configurations predefined (defaults to the first one):

*   `full` (`v1.1.0`) (`Size: 73.07 GiB`): Full NSynth Dataset is split into
    train, valid, and test sets, with no instruments overlapping between the
    train set and the valid/test sets.

*   `gansynth_subset` (`v1.1.0`) (`Size: 73.08 GiB`): NSynth Dataset limited to
    acoustic instruments in the MIDI pitch interval [24, 84]. Uses alternate
    splits that have overlap in instruments (but not exact notes) between the
    train set and valid/test sets. This variant was originally introduced in the
    ICLR 2019 GANSynth paper (https://arxiv.org/abs/1902.08710).

*   `gansynth_subset.f0_and_loudness` (`v1.1.0`) (`Size: 73.08 GiB`): NSynth
    Dataset limited to acoustic instruments in the MIDI pitch interval [24, 84].
    Uses alternate splits that have overlap in instruments (but not exact notes)
    between the train set and valid/test sets. This variant was originally
    introduced in the ICLR 2019 GANSynth paper
    (https://arxiv.org/abs/1902.08710). This version additionally contains
    estimates for F0 using CREPE (Kim et al., 2018) and A-weighted perceptual
    loudness. Both signals are provided at a frame rate of 250Hz.

## `nsynth/full`
Full NSynth Dataset is split into train, valid, and test sets, with no
instruments overlapping between the train set and the valid/test sets.

Versions:

*   **`1.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics
None computed

### Features
```python
FeaturesDict({
    'audio': Tensor(shape=(64000,), dtype=tf.float32),
    'id': Tensor(shape=(), dtype=tf.string),
    'instrument': FeaturesDict({
        'family': ClassLabel(shape=(), dtype=tf.int64, num_classes=11),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1006),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    }),
    'pitch': ClassLabel(shape=(), dtype=tf.int64, num_classes=128),
    'qualities': FeaturesDict({
        'bright': Tensor(shape=(), dtype=tf.bool),
        'dark': Tensor(shape=(), dtype=tf.bool),
        'distortion': Tensor(shape=(), dtype=tf.bool),
        'fast_decay': Tensor(shape=(), dtype=tf.bool),
        'long_release': Tensor(shape=(), dtype=tf.bool),
        'multiphonic': Tensor(shape=(), dtype=tf.bool),
        'nonlinear_env': Tensor(shape=(), dtype=tf.bool),
        'percussive': Tensor(shape=(), dtype=tf.bool),
        'reverb': Tensor(shape=(), dtype=tf.bool),
        'tempo-synced': Tensor(shape=(), dtype=tf.bool),
    }),
    'velocity': ClassLabel(shape=(), dtype=tf.int64, num_classes=128),
})
```

### Homepage

*   [https://g.co/magenta/nsynth-dataset](https://g.co/magenta/nsynth-dataset)

## `nsynth/gansynth_subset`

NSynth Dataset limited to acoustic instruments in the MIDI pitch interval [24,
84]. Uses alternate splits that have overlap in instruments (but not exact
notes) between the train set and valid/test sets. This variant was originally
introduced in the ICLR 2019 GANSynth paper (https://arxiv.org/abs/1902.08710).

Versions:

*   **`1.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics
None computed

### Features
```python
FeaturesDict({
    'audio': Tensor(shape=(64000,), dtype=tf.float32),
    'id': Tensor(shape=(), dtype=tf.string),
    'instrument': FeaturesDict({
        'family': ClassLabel(shape=(), dtype=tf.int64, num_classes=11),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1006),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    }),
    'pitch': ClassLabel(shape=(), dtype=tf.int64, num_classes=128),
    'qualities': FeaturesDict({
        'bright': Tensor(shape=(), dtype=tf.bool),
        'dark': Tensor(shape=(), dtype=tf.bool),
        'distortion': Tensor(shape=(), dtype=tf.bool),
        'fast_decay': Tensor(shape=(), dtype=tf.bool),
        'long_release': Tensor(shape=(), dtype=tf.bool),
        'multiphonic': Tensor(shape=(), dtype=tf.bool),
        'nonlinear_env': Tensor(shape=(), dtype=tf.bool),
        'percussive': Tensor(shape=(), dtype=tf.bool),
        'reverb': Tensor(shape=(), dtype=tf.bool),
        'tempo-synced': Tensor(shape=(), dtype=tf.bool),
    }),
    'velocity': ClassLabel(shape=(), dtype=tf.int64, num_classes=128),
})
```

### Homepage

*   [https://g.co/magenta/nsynth-dataset](https://g.co/magenta/nsynth-dataset)

## `nsynth/gansynth_subset.f0_and_loudness`

NSynth Dataset limited to acoustic instruments in the MIDI pitch interval [24,
84]. Uses alternate splits that have overlap in instruments (but not exact
notes) between the train set and valid/test sets. This variant was originally
introduced in the ICLR 2019 GANSynth paper (https://arxiv.org/abs/1902.08710).
This version additionally contains estimates for F0 using CREPE (Kim et al.,
2018) and A-weighted perceptual loudness. Both signals are provided at a frame
rate of 250Hz.

Versions:

*   **`1.1.0`** (default):
*   `2.0.0`: New split API (https://tensorflow.org/datasets/splits)

### Statistics
None computed

### Features
```python
FeaturesDict({
    'audio': Tensor(shape=(64000,), dtype=tf.float32),
    'f0': FeaturesDict({
        'confidence': Tensor(shape=(1001,), dtype=tf.float32),
        'hz': Tensor(shape=(1001,), dtype=tf.float32),
        'midi': Tensor(shape=(1001,), dtype=tf.float32),
    }),
    'id': Tensor(shape=(), dtype=tf.string),
    'instrument': FeaturesDict({
        'family': ClassLabel(shape=(), dtype=tf.int64, num_classes=11),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1006),
        'source': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    }),
    'loudness': FeaturesDict({
        'db': Tensor(shape=(1001,), dtype=tf.float32),
    }),
    'pitch': ClassLabel(shape=(), dtype=tf.int64, num_classes=128),
    'qualities': FeaturesDict({
        'bright': Tensor(shape=(), dtype=tf.bool),
        'dark': Tensor(shape=(), dtype=tf.bool),
        'distortion': Tensor(shape=(), dtype=tf.bool),
        'fast_decay': Tensor(shape=(), dtype=tf.bool),
        'long_release': Tensor(shape=(), dtype=tf.bool),
        'multiphonic': Tensor(shape=(), dtype=tf.bool),
        'nonlinear_env': Tensor(shape=(), dtype=tf.bool),
        'percussive': Tensor(shape=(), dtype=tf.bool),
        'reverb': Tensor(shape=(), dtype=tf.bool),
        'tempo-synced': Tensor(shape=(), dtype=tf.bool),
    }),
    'velocity': ClassLabel(shape=(), dtype=tf.int64, num_classes=128),
})
```

### Homepage

*   [https://g.co/magenta/nsynth-dataset](https://g.co/magenta/nsynth-dataset)

## Citation

```
@InProceedings{pmlr-v70-engel17a,
  title =    {Neural Audio Synthesis of Musical Notes with {W}ave{N}et Autoencoders},
  author =   {Jesse Engel and Cinjon Resnick and Adam Roberts and Sander Dieleman and Mohammad Norouzi and Douglas Eck and Karen Simonyan},
  booktitle =    {Proceedings of the 34th International Conference on Machine Learning},
  pages =    {1068--1077},
  year =     {2017},
  editor =   {Doina Precup and Yee Whye Teh},
  volume =   {70},
  series =   {Proceedings of Machine Learning Research},
  address =      {International Convention Centre, Sydney, Australia},
  month =    {06--11 Aug},
  publisher =    {PMLR},
  pdf =      {http://proceedings.mlr.press/v70/engel17a/engel17a.pdf},
  url =      {http://proceedings.mlr.press/v70/engel17a.html},
}
```

--------------------------------------------------------------------------------
