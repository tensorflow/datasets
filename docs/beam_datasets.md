# Generating big datasets with Apache Beam

Some datasets are too big to be processed on a single machine. `tfds` supports
generating data across many machines by using
[Apache Beam](https://beam.apache.org/).

Note: This mode is still experimental, so the API may change in the future
depending on user feedback. Do not hesitate to
[submit your feedback](https://github.com/tensorflow/datasets/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=).

*   [Prerequisites](#prerequisites)
*   [Instructions](#instructions)
*   [Example](#example)
*   [Run your pipeline](#run-your-pipeline)

## Prerequisites

In order to write Apache Beam datasets, you should be familiar with the
following concepts:

*   Be familiar with the
    [`tfds` dataset creation guide](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md)
    as most of the content still applies for Beam datasets.
*   Get an introduction to Apache Beam with the
    [Beam programming guide](https://beam.apache.org/documentation/programming-guide/).
*   If you want to generate your dataset using Cloud Dataflow, read the
    [Google Cloud Documentation](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python)
    and the
    [Apache Beam dependency guide](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/).

## Instructions

If you are familiar with the
[dataset creation guide](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md),
adding a Beam dataset only requires a few modifications:

*   Your `DatasetBuilder` will inherit from `tfds.core.BeamBasedBuilder` instead
    of `tfds.core.GeneratorBasedBuilder`.
*   Beam datasets should implement the abstract method `_build_pcollection(self,
    **kwargs)` instead of the method `_generate_examples(self, **kwargs)`.
    `_build_pcollection` should return a `beam.PCollection` with the examples
    associated with the split.
*   Writing a unit test for your Beam dataset is the same as with other
    datasets.

Some additional considerations:

*   Use `tfds.core.lazy_imports` to import Apache Beam. By using a lazy
    dependency, users can still read the dataset after it has been generated
    without having to install Beam.
*   Be careful with Python closures. When running the pipeline, the `beam.Map`
    and `beam.DoFn` functions are serialized using `pickle` and sent to all
    workers. This can create bugs; for instance, if you are using a mutable
    object in your functions which has been declared outside of the function,
    you may encounter `pickle` errors or unexpected behavior. The fix is
    typically to avoid mutating closed-over objects.
*   Avoid using methods on `DatasetBuilder` in the Beam pipeline because
    Beam will try to pickle the class, including the `DatasetInfo` protocol
    buffer, which will fail.

## Example

Here is an example of a Beam dataset. For a more complicated real example, have
a look at the
[`Wikipedia` dataset](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/wikipedia.py).

```python
class DummyBeamDataset(tfds.core.BeamBasedBuilder):

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(16, 16, 1)),
            'label': tfds.features.ClassLabel(names=['dog', 'cat']),
        }),
    )

  def _split_generators(self, dl_manager):
    ...
    return [
        tfds.core.SplitGenerator(
            name=tfds..Split.TRAIN,
            num_shards=100,
            gen_kwargs=dict(file_dir='path/to/train_data/'),
        ),
        splits_lib.SplitGenerator(
            name=tfds..Split.TEST,
            num_shards=10,
            gen_kwargs=dict(file_dir='path/to/test_data/'),
        ),
    ]

  def _build_pcollection(self, pipeline, file_dir):
    """Generate examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam

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

## Run your pipeline

To generate the dataset on Beam, the API is the same as for other datasets, but
you have to pass the Beam options or runner to the `DownloadConfig`.

```
# To use Beam, you have to set at least one of `beam_options` or `beam_runner`
dl_config = tfds.download.DownloadConfig(
    beam_options=beam.options.pipeline_options.PipelineOptions()
)

builder = tfds.builder('wikipedia')
builder.download_and_prepare(
    download_dir=FLAGS.download_dir,
    download_config=dl_config,
)
```

To run your script locally using the default Apache Beam runner, the command is
the same as for other datasets:

```
python -m tensorflow_datasets.scripts.download_and_prepare \
  --register_checksums \
  --datasets=my_new_dataset
```

TODO(tfds): Add instructions to run with `Cloud Dataflow`
