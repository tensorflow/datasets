# Beam Datasets

TODO(tfds): Document how to generate BeamBasedBuilder datasets.

Warning: To work with Python3, Beam generation won't work with 2.11 or previous
version. It require
[this fix](https://github.com/apache/beam/commit/46a70a8b4691a169c9e018299765e1bdb88239f4)
.

The current public version "release-2.11.0"

Example:

```python
class DummyBeamDataset(dataset_builder.BeamBasedBuilder):

  VERSION = utils.Version('1.0.0')

  def _info(self):

    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({
            'image': features.Image(shape=(16, 16, 1)),
            'label': features.ClassLabel(names=['dog', 'cat']),
        }),
    )

  def _split_generators(self, dl_manager):
    ...
    return [
        splits_lib.SplitGenerator(
            name=splits_lib.Split.TRAIN,
            num_shards=100,
            gen_kwargs=dict(file_dir='path/to/train_data/'),
        ),
        splits_lib.SplitGenerator(
            name=splits_lib.Split.TEST,
            num_shards=10,
            gen_kwargs=dict(file_dir='path/to/test_data/'),
        ),
    ]

  def _build_pcollection(self, pipeline, file_dir):
    """Generate examples as dicts."""

    beam = lazy_imports.lazy_imports.apache_beam

    def _process_example(filename):
      return {
          'image': os.path.join(file_dir, filename),
          'label': filename.split('.')[1],  # Extract label: "0010102.dog.jpeg"
      }

    return (
        pipeline
        | beam.Create(tf.io.gfile.listdir(file_dir))
        | beam.Map(_process_example)
    )

```

Relevant links:

*   https://cloud.google.com/dataflow/docs/guides/installing-beam-sdk
*   https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/
