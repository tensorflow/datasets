# Generating big datasets with Apache Beam

Some datasets are too big to be processed on a single machine. `tfds` supports
generating data across many machines by using
[Apache Beam](https://beam.apache.org/).

This doc has two sections:

*   For user who want to generate an existing Beam dataset
*   For developers who want to create a new Beam dataset

## Generating a Beam dataset

Below are different examples of generating a Beam dataset, both on the cloud or
locally.

**Warning**: When generating the dataset with the
[`tfds build` CLI](https://www.tensorflow.org/datasets/cli#tfds_build_download_and_prepare_a_dataset),
make sure to specify the dataset config you want to generate or it will default
to generate all existing configs. For example, for
[wikipedia](https://www.tensorflow.org/datasets/catalog/wikipedia), use `tfds
build wikipedia/20200301.en` instead of `tfds build wikipedia`.

### On Google Cloud Dataflow

To run the pipeline using
[Google Cloud Dataflow](https://cloud.google.com/dataflow/) and take advantage
of distributed computation, first follow the
[Quickstart instructions](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python).

Once your environment is set up, you can run the
[`tfds build` CLI](https://www.tensorflow.org/datasets/cli#tfds_build_download_and_prepare_a_dataset)
using a data directory on [GCS](https://cloud.google.com/storage/) and
specifying the
[required options](https://cloud.google.com/dataflow/docs/guides/specifying-exec-params#configuring-pipelineoptions-for-execution-on-the-cloud-dataflow-service)
for the `--beam_pipeline_options` flag.

To make it easier to launch the script, it's helpful to define the following
variables using the actual values for your GCP/GCS setup and the dataset you
want to generate:

```sh
DATASET_NAME=<dataset-name>
DATASET_CONFIG=<dataset-config>
GCP_PROJECT=my-project-id
GCS_BUCKET=gs://my-gcs-bucket
```

You will then need to create a file to tell Dataflow to install `tfds` on the
workers:

```sh
echo "tensorflow_datasets[$DATASET_NAME]" > /tmp/beam_requirements.txt
```

If you're using `tfds-nightly`, make sure to to echo from `tfds-nightly` in case
the dataset has been updated since the last release.

```sh
echo "tfds-nightly[$DATASET_NAME]" > /tmp/beam_requirements.txt
```

Finally, you can launch the job using the command below:

```sh
tfds build $DATASET_NAME/$DATASET_CONFIG \
  --data_dir=$GCS_BUCKET/tensorflow_datasets \
  --beam_pipeline_options=\
"runner=DataflowRunner,project=$GCP_PROJECT,job_name=$DATASET_NAME-gen,"\
"staging_location=$GCS_BUCKET/binaries,temp_location=$GCS_BUCKET/temp,"\
"requirements_file=/tmp/beam_requirements.txt"
```

### Locally

To run your script locally using the default Apache Beam runner, the command is
the same as for other datasets:

```sh
tfds build my_dataset
```

**Warning**: Beam datasets can be **huge** (terabytes or larger) and take a
significant amount of resources to be generated (can take weeks on a local
computer). It is recommended to generate the datasets using a distributed
environment. Have a look at the
[Apache Beam Documentation](https://beam.apache.org/) for a list of supported
runtimes.

### With a custom script

To generate the dataset on Beam, the API is the same as for other datasets. You
can customize the
[`beam.Pipeline`](https://beam.apache.org/documentation/programming-guide/#creating-a-pipeline)
using the `beam_options` (and `beam_runner`) arguments of `DownloadConfig`.

```python
# If you are running on Dataflow, Spark,..., you may have to set-up runtime
# flags. Otherwise, you can leave flags empty [].
flags = ['--runner=DataflowRunner', '--project=<project-name>', ...]

# `beam_options` (and `beam_runner`) will be forwarded to `beam.Pipeline`
dl_config = tfds.download.DownloadConfig(
    beam_options=beam.options.pipeline_options.PipelineOptions(flags=flags)
)
data_dir = 'gs://my-gcs-bucket/tensorflow_datasets'
builder = tfds.builder('wikipedia/20190301.en', data_dir=data_dir)
builder.download_and_prepare(download_config=dl_config)
```

## Implementing a Beam dataset

### Prerequisites

In order to write Apache Beam datasets, you should be familiar with the
following concepts:

*   Be familiar with the
    [`tfds` dataset creation guide](https://github.com/tensorflow/datasets/blob/master/docs/add_dataset.md)
    as most of the content still applies for Beam datasets.
*   Get an introduction to Apache Beam with the
    [Beam programming guide](https://beam.apache.org/documentation/programming-guide/).
*   If you want to generate your dataset using Cloud Dataflow, read the
    [Google Cloud Documentation](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python)
    and the
    [Apache Beam dependency guide](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/).

### Instructions

If you are familiar with the
[dataset creation guide](https://github.com/tensorflow/datasets/blob/master/docs/add_dataset.md),
adding a Beam dataset only requires to modify the `_generate_examples` function.
The function should returns a beam object, rather than a generator:

Non-beam dataset:

```python
def _generate_examples(self, path):
  for f in path.iterdir():
    yield _process_example(f)
```

Beam dataset:

```python
def _generate_examples(self, path):
  return (
      beam.Create(path.iterdir())
      | beam.Map(_process_example)
  )
```

All the rest can be 100% identical, including tests.

Some additional considerations:

*   Use `tfds.core.lazy_imports` to import Apache Beam. By using a lazy
    dependency, users can still read the dataset after it has been generated
    without having to install Beam.
*   Be careful with Python closures. When running the pipeline, the `beam.Map`
    and `beam.DoFn` functions are serialized using `pickle` and sent to all
    workers. Do not use mutable objects inside a `beam.PTransform` if the state
    has to be shared across workers.
*   Due to the way `tfds.core.DatasetBuilder` is serialized with pickle,
    mutating `tfds.core.DatasetBuilder` during data creation will be ignored on
    the workers (e.g. it's not possible to set `self.info.metadata['offset'] =
    123` in `_split_generators` and access it from the workers like
    `beam.Map(lambda x: x + self.info.metadata['offset'])`)
*   If you need to share some pipeline steps between the splits, you can add add
    an extra `pipeline: beam.Pipeline` kwarg to `_split_generator` and control
    the full generation pipeline. See `_generate_examples` documentation of
    `tfds.core.GeneratorBasedBuilder`.

### Example

Here is an example of a Beam dataset.

```python
class DummyBeamDataset(tfds.core.GeneratorBasedBuilder):

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
    return {
        'train': self._generate_examples(file_dir='path/to/train_data/'),
        'test': self._generate_examples(file_dir='path/to/test_data/'),
    }

  def _generate_examples(self, file_dir: str):
    """Generate examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam

    def _process_example(filename):
      # Use filename as key
      return filename, {
          'image': os.path.join(file_dir, filename),
          'label': filename.split('.')[1],  # Extract label: "0010102.dog.jpeg"
      }

    return (
        beam.Create(tf.io.gfile.listdir(file_dir))
        | beam.Map(_process_example)
    )

```

### Running your pipeline

To run the pipeline, have a look at the above section.

**Note**: Like for non-beam datasets, do not forget to register download
checksums with `--register_checksums` (only the first time to register the
downloads).

```sh
tfds build my_dataset --register_checksums
```

## Pipeline using TFDS as input

If you want to create a beam pipeline which takes a TFDS dataset as source, you
can use the `tfds.beam.ReadFromTFDS`:

```python
builder = tfds.builder('my_dataset')

_ = (
    pipeline
    | tfds.beam.ReadFromTFDS(builder, split='train')
    | beam.Map(tfds.as_numpy)
    | ...
)
```

It will process each shard of the dataset in parallel.

Note: This require the dataset to be already generated. To generate datasets
using beam, see the other sections.
