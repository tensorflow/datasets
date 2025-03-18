# Datasets versioning

## Definition

Versioning can refer to different meaning:

*   The TFDS API version (pip version): `tfds.__version__`
*   The public dataset version, independent from TFDS (e.g.
    [Voc2007](https://pjreddie.com/projects/pascal-voc-dataset-mirror/),
    Voc2012). In TFDS each public dataset version should be implemented as an
    independent dataset:
    *   Either through
        [builder configs](https://www.tensorflow.org/datasets/add_dataset#dataset_configurationvariants_tfdscorebuilderconfig):
        E.g. `voc/2007`, `voc/2012`
    *   Either as 2 independent datasets: E.g. `wmt13_translate`,
        `wmt14_translate`
*   The dataset generation code version in TFDS (`my_dataset:1.0.0`): For
    example, if a bug is found in the TFDS implementation of `voc/2007`, the
    `voc.py` generation code will be updated (`voc/2007:1.0.0` ->
    `voc/2007:2.0.0`).

The rest of this guide only focus on the last definition (dataset code version
in the TFDS repository).

## Supported versions

As a general rule:

*   Only the last current version can be generated.
*   All previously generated dataset can be read (note: This require datasets
    generated with TFDS 4+).

```python
builder = tfds.builder('my_dataset')
builder.info.version  # Current version is: '2.0.0'

# download and load the last available version (2.0.0)
ds = tfds.load('my_dataset')

# Explicitly load a previous version (only works if
# `~/tensorflow_datasets/my_dataset/1.0.0/` already exists)
ds = tfds.load('my_dataset:1.0.0')
```

## Semantic

Every `DatasetBuilder` defined in TFDS comes with a version, for example:

```python
class MNIST(tfds.core.GeneratorBasedBuilder):
  VERSION = tfds.core.Version('2.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release',
      '2.0.0': 'Update dead download url',
  }
```

The version follows
[Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html):
`MAJOR.MINOR.PATCH`. The purpose of the version is to be able to guarantee
reproducibility: loading a given dataset at a fixed version yields the same
data. More specifically:

 - If `PATCH` version is incremented, data as read by the client is the same,
 although data might be serialized differently on disk, or the metadata might
 have changed. For any given slice, the slicing API returns the same set of
 records.
 - If `MINOR` version is incremented, existing data as read by the client is the
 same, but there is additional data (features in each record). For any given
 slice, the  slicing API returns the same set of records.
 - If `MAJOR` version is incremented, the existing data has been changed and/or
 the slicing API doesn't necessarily return the same set of records for a given
 slice.

When a code change is made to the TFDS library and that code change impacts the
way a dataset is being serialized and/or read by the client, then the
corresponding builder version is incremented according to the above guidelines.

Note that the above semantic is best effort, and there might be un-noticed bugs
impacting a dataset while the version was not incremented. Such bugs are
eventually fixed, but if you heavily rely on the versioning, we advise you to
use TFDS from a released version (as opposed to `HEAD`).

Also note that some datasets have another versioning scheme independent from
the TFDS version. For example, the Open Images dataset has several versions,
and in TFDS, the corresponding builders are `open_images_v4`, `open_images_v5`,
...

## Loading a specific version

When loading a dataset or a `DatasetBuilder`, you can specify the version to
use. For example:

```python
tfds.load('imagenet2012:2.0.1')
tfds.builder('imagenet2012:2.0.1')

tfds.load('imagenet2012:2.0.0')  # Error: unsupported version.

# Resolves to 3.0.0 for now, but would resolve to 3.1.1 if when added.
tfds.load('imagenet2012:3.*.*')
```

If using TFDS for a publication, we advise you to:

 - **fix the `MAJOR` component of the version only**;
 - **advertise which version of the dataset was used in your results.**

Doing so should make it easier for your future self, your readers and
reviewers to reproduce your results.

## BUILDER_CONFIGS and versions

Some datasets define several `BUILDER_CONFIGS`. When that is the case, `version`
and `supported_versions` are defined on the config objects themselves. Other
than that, semantics and usage are identical. For example:

```python
class OpenImagesV4(tfds.core.GeneratorBasedBuilder):

  BUILDER_CONFIGS = [
      OpenImagesV4Config(
          name='original',
          version=tfds.core.Version('0.2.0'),
          supported_versions=[
            tfds.core.Version('1.0.0', "Major change in data"),
          ],
          description='Images at their original resolution and quality.'),
      ...
  ]

tfds.load('open_images_v4/original:1.*.*')
```

## Experimental version

Note: The following is bad practice, error prone and should be discouraged.

It is possible to allow 2 versions to be generated at the same time. One default
and one experimental version. For example:

```python
class MNIST(tfds.core.GeneratorBasedBuilder):
  VERSION = tfds.core.Version("1.0.0")  # Default version
  SUPPORTED_VERSIONS = [
      tfds.core.Version("2.0.0"),  # Experimental version
  ]


# Download and load default version 1.0.0
builder = tfds.builder('mnist')

#  Download and load experimental version 2.0.0
builder = tfds.builder('mnist', version='experimental_latest')
```

In the code, you need to make sure to support the 2 versions:

```python
class MNIST(tfds.core.GeneratorBasedBuilder):

  ...

  def _generate_examples(self, path):
    if self.info.version >= '2.0.0':
      ...
    else:
      ...
```
