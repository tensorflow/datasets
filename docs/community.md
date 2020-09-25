# Product feedback for the TensorFlow Datasets team

## Overview

TensorFlow Datasets (TFDS) is a collection of datasets ready to use, with
TensorFlow or other Python ML frameworks, such as JAX. Consuming datasets with
TFDS enables your team to build easy-to-use and highly performant input
pipelines.

The TensorFlow team is excited to announce that we would like to work with
external teams who are using TensorFlow Datasets in their projects.

Did you know you can use TFDS for both public and private datasets?

## Qualifications:

We’re looking to work with companies who have a use case that falls into either
of the following category:

*   **Public use**: Anyone interested in sharing your dataset to the publicly
    available repository hosted on TFDS. This involves giving authorization to
    TFDS to host and redistribute the data ourselves.
*   **Private use**: Any enterprise, company, or institution that would like to
    utilize TFDS for internal datasets, while benefiting from its features such
    as extraction, formatting, and distribution but would like to keep access to
    the data restricted.

### What does working together with TFDS mean?

We’d like to work together and provide technical support to help you integrate
TFDS. This includes GitHub question support, and a consultation with the TFDS
team.

In return, we're looking to work with companies that will give us feedback. This
includes companies across all industry segments that include use cases from
startups, large enterprise companies or academic institutions. Working together
will help us ensure we build the right set of features that supports the TFDS
community.

## Why TFDS

TFDS already contains hundreds of public datasets, with an easy and flexible API
to access datasets of arbitrary size.

For partners who have a private use scenario, integrating your own internal
dataset enables easy transition between running/testing on public and internal
data.

In addition, adding your dataset to TFDS makes accessing it easier for
additional departments in your organization.

Datasets are distributed in all kinds of formats and in all kinds of places, and
they're not always stored in a format that's ready to feed into a machine
learning pipeline.

TFDS provides a way to transform all those datasets into a standard format, do
the preprocessing necessary to make them ready for a machine learning pipeline,
and provides a standard input pipeline.

Datasets provided through TFDS offers many features:

*   Expose datasets metadata through info objects (label names, number of
    examples, dataset size)
*   Use the default datasets for training and test splits or dynamically create
    your own custom sub-splits
*   Versioning

## Examples

Google Research utilizes TFDS heavily across projects.

<img src="https://storage.cloud.google.com/tfds-data/website/partners/T5.png" alt="Visualization" width="200px">

Google's AI Research team, released a research paper on
[T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html),
a shared text-to-text framework, that produces state-of-the-art results on many
NLP benchmarks while being flexible enough to be fine-tuned to a variety of
important downstream tasks. Some applications of T5 include closed book
questions and fill in the blank text generation. The pre-training objective used
by T5 aligns more closely with a fill-in-the-blank task where the model predicts
missing words within a corrupted piece of text. The team utilized TFDS for
handling the dataset they created and used to train their models.

<img src="https://storage.cloud.google.com/tfds-data/website/partners/VTAB.png" alt="Visualization" width="200px">

In addition, Google’s research team has utilized pre-trained representations in
TFDS to make advances in the field of Computer Vision. In
[VTAB](https://ai.googleblog.com/2019/11/the-visual-task-adaptation-benchmark.html),
they evaluated visual models on a challenging set of downstream vision tasks,
coming from diverse domains: natural images, artificial environments
(structured) and images captured with non-standard cameras (specialized). The
availability of the datasets helped enable their research to improve extracting
features from images.

<img src="https://storage.cloud.google.com/tfds-data/website/partners/NLP.png" alt="Visualization" width="200px">

Lastly, TFDS has been used in another NLP example. Google researcher's have
released
[EXTREME](https://ai.googleblog.com/2020/04/xtreme-massively-multilingual-multi.html),
a set of language tasks and benchmarks to encourage more research on
multilingual learning.

You can check out more repos that are using TFDS
[here](https://github.com/search?p=6&q=org%3Agoogle-research+%22import+tensorflow_datasets%22&type=Code).

## Contact

Please contact us at tfds-feedback@tensorflow.org and the Tensorflow Datasets
team will reach out to you.
