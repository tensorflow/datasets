<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="nsynth" />
  <meta itemprop="description" content="The NSynth Dataset is an audio dataset containing ~300k musical notes, each&#10;with a unique pitch, timbre, and envelope. Each note is annotated with three&#10;additional pieces of information based on a combination of human evaluation&#10;and heuristic algorithms:&#10; -Source: The method of sound production for the note's instrument.&#10; -Family: The high-level family of which the note's instrument is a member.&#10; -Qualities: Sonic qualities of the note.&#10;&#10;The dataset is split into train, valid, and test sets, with no instruments&#10;overlapping between the train set and the valid/test sets.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/nsynth" />
  <meta itemprop="sameAs" content="https://g.co/magenta/nsynth-dataset" />
</div>

# `nsynth`

The NSynth Dataset is an audio dataset containing ~300k musical notes, each with
a unique pitch, timbre, and envelope. Each note is annotated with three
additional pieces of information based on a combination of human evaluation and
heuristic algorithms: -Source: The method of sound production for the note's
instrument. -Family: The high-level family of which the note's instrument is a
member. -Qualities: Sonic qualities of the note.

The dataset is split into train, valid, and test sets, with no instruments
overlapping between the train set and the valid/test sets.

*   URL:
    [https://g.co/magenta/nsynth-dataset](https://g.co/magenta/nsynth-dataset)
*   `DatasetBuilder`:
    [`tfds.audio.nsynth.Nsynth`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/nsynth.py)
*   Version: `v1.0.0`
*   Size: `73.07 GiB`

## Features
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

## Statistics

Split | Examples
:---- | -------:
ALL   | 305,979
TRAIN | 289,205
VALID | 12,678
TEST  | 4,096

## Urls

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
