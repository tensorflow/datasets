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

<img src="https://00f74ba44b7098b326b35dcd1b0119277e37f9c022-apidata.googleusercontent.com/download/storage/v1/b/tfds-data/o/website%2Fpartners%2FT5.png?jk=AFshE3VQdygRpsrYnsoIm5eItslOjTwm5So56yLSPnMiM3hkFXMBP6owr05HBMSqfB3m4Dy412liLVwr8XnND9Kiktnzb-xZw7CDkcNGBuC0AFuVuQ4jGhhzhGrUTACU2GZ9ddhrN53rMMfcFFXJvo17Cfd3vS5PzJfBC8WoFQU9m4CzBosD3P7ZJ5LuvC9YCOE4lNL4yWVJXCpcnOgoMRHWgym5_sZEvI0edCeIaZwHYNZaWhJODlHClAh-uctNQa3mTJuIuA7Ac8jM7sf2E9yc_6Y8bUeHn3vH0Y6VAMl_rXRhnATSPHYxhiYps_nXlGBBI44T6TAlkY2ftZQT7RPsbRlZ36b3GPhEg-xMLNfiZfwQohikm1O07KMllx-IwvF52cnapg-89M10XMmBRL81WacPessb6XUnSNx9om34Rd1Me4FFV45D1vVjw-Z2MWprSHB9UqrGgO98UHSBKnxOGBgPCQ8SweuV7c1HN8J5WD-fwmnGhk71DqRk4WknX12UIUb2GYDjF81FXJfaRN8ZOYSNoJqdh8QkIphPZP79CgkWDtS7RXwIcWMw-gsD7PO1WIgd5BMSVeiiOt6aWidN8QW6n0odrUJ4hgrHUzbg43jpN8X-ebeaLEsBVT6Af_g7sJjlufqEmtaSXNQuUTuKqsdS8y3k7ZLUUY554GsCnKbha3RfClfPqEwNME3psWRdUNc1gsHIOgho61Zyvw3BLJnrDIx2C-75qw93GvC4fq7uAbkSdM4bizsj-eOUyq8gEnFfva6gKXVxg3PMb-mxWfbB2gWg3y--j4B5fiY3gh3j5GUd-4HgX34fUQ9x2S0V0olbJNDm4s4qY6lO9Ht0Y2My64boTZPRq9JTCpJh_25-QWPXXH1EwjjnPrRSgSNOymS__8j9psU81wqanQcGwlySJaECleAUcDKknstfcPq1Gt2f6CGl2XoggsGh3RD59-UaFRRO7cpPOk8P&isca=1" alt="Visualization" width="150px">

Google's AI Research team, released a research paper on
[T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html),
a shared text-to-text framework, that produces state-of-the-art results on many
NLP benchmarks while being flexible enough to be fine-tuned to a variety of
important downstream tasks. Some applications of T5 include closed book
questions and fill in the blank text generation. The pre-training objective used
by T5 aligns more closely with a fill-in-the-blank task where the model predicts
missing words within a corrupted piece of text. The team utilized TFDS for
handling the dataset they created and used to train their models.

<img src="https://00f74ba44bf2b6d09a7470235045591ec901476cb3-apidata.googleusercontent.com/download/storage/v1/b/tfds-data/o/website%2Fpartners%2FVTAB.png?jk=AFshE3X2Y5zKLe0wGTcM_DhyIh7eqL3ThILSwnJNyIrA9-GxiemT8b7fSB_HuL3e24rRqHO-ngy-uEUx3oJ0Vn9I41yqg68oAd4txZchGxomLN3-E-WBF9OZscQ2Ygc_8jalx5HWEmzwpKPl3YpTyhB3Un5VPOb3i9qyYSfEdw0KXRkzzBQRa6RO8iRhI6pcgv_r6yDF164RFSxLdTGyBb4LwwVi4Z2X1OCvGnZ81Ion3d6QUiiyvwV-TVVc5gry-kTPZJ-wH2WxZbS93NEUi1cLZnZpwj669_KWzzwpNBQsvi-iA10tS81QZNEcmj5pfJqoq8Q7E4ocyYAlDpb3jnfSuLlE0mW_yPJr9M5yWWZ5tHdUPRN9dJdSGrkkcMZ79NQvw3PJuxpzPdnrTVql_Az81N4aKXVgZS5YpLojJp812aZlCZuZcybquOJmLOrE-Uy_wXPJFVxgU1dOe2Sr2yweiHeo1mv0aWYDXws3HPhIM4iNUj6tZZkXcvBA6XRCBlOBK4_Sv6jFm8TpQKUHcIHmR2Yn09ai_0YlmSRzmBgBuNns9rjPgj5djkjb8LaW37KE246BBZ7PP9T15x16xHyxc6_P0Ll8VjrgrdUtbXzK6ghiV5D-qM8hHQNRWs1fvugEEl2s-uHgCtBpd2GQpHkjr0ezNrGDXOZUeF9Vp_zm1EjITiRejWblctAJXL8pPD3hfTuzbccxL3SgxxCwgVTHcf8IPalikeSLrcHuNi7Xg31ZlrOW7PV9QYeMHV-Zmdmfpo16M6jbwtqxZYoLoByXalM31HNWJ_95t4pbPcqD3DVQ7XvJMniKEaMjLOjE30SvRNYQ9uAn7Yv6eASF0o0fhLRpTD4r54zJtsq5rUURotDtjCUHMYLbTZS0DWHCPTKwJmFgwy7yd6UN3oK2QtsKI-NvbaePmMyP8X4fUhtcAgX9M1qTkn_Eg-DaLmol1wXw7BPxh3JXXtq1_9FhCLU&isca=1" alt="Visualization" width="200px">

In addition, Google’s research team has utilized pre-trained representations in
TFDS to make advances in the field of Computer Vision. In
[VTAB](https://ai.googleblog.com/2019/11/the-visual-task-adaptation-benchmark.html),
they evaluated visual models on a challenging set of downstream vision tasks,
coming from diverse domains: natural images, artificial environments
(structured) and images captured with non-standard cameras (specialized). The
availability of the datasets helped enable their research to improve extracting
features from images.

<img src="https://00f74ba44bc0a0e48fe3a4518bc56c34c728018bc8-apidata.googleusercontent.com/download/storage/v1/b/tfds-data/o/website%2Fpartners%2FNLP.png?jk=AFshE3WlS99dCOyzdTxRidjahZR6c9_iApu376vUUrrflsR-Y_eqbGckZWUn2h0e9Zxj0U-zS8vioTqNMs19LhrandQGvxRt0EQxDWLGX3sswB7InKBJ6IRXF7arU8A4nEX2Bs9HdGM5w1ly4XCnKCojitzjxk0gIoJwysrMcCfq2EO1rmPdBoBFBy4qgPH3SIRX19-KvxCy2lWh7ELIjPRb8ffCaZKH713btXps0JMT1YfnAc95T99VDCALKlpBvIWQ7gWiVsnWssA0io4D7n8XDzj6PESfVaXQezaXeQ74HhpYLJlwUwAjlRjtnnoPI5cQxiHJa7Wz6LD2Et3a7m5Gyh_CmqFj17N-CbkyT0rcEYRPns2FGhvyXHOZ-XkGpwfNctnLSxH6nTZCBNDZJUubUwsyz4NR5lTXClHUitYcnJrXDX081YlMoR9SxGMapVK8RsSQEv4wmAYM5_oopr6SX3gKnJTabfBqTfgIxSyXGwB4XuS3lPTfebjpVRaQTufYDN4kseK8lEHoKIRhroPQKywP5kpzsQKOE9r53qyTb_GIPratGq1qigImyWiGL2iXu0pRvBN5rexmjTPRYTw8HdsmrZ1zTOLu7W_1hklByHIMblOhMjMb5qVj6HaXL7QSbtetGqei31MLfu4aLMoey27XU9jajh9v02q3MVhED33B3UYIvPaWd12kSWN2-Xq54QG-2QoIFcJhh7GmS7OcjGrAwmalNXdkGZ2b4GlYjkVYSFVBbRJwL9R2rxTHokRr02bD3ri5QRXpnWCnmL8hYKTk4OPOl3CZAkFlcWL6WMSaFWTURFmfv4_ds23MWxnVQxxF2crP5oAvrNhqHkFtBtUk4P6Q3Tz218uZogSqHG9IKgATHRBPHDZTpOB7Fqph8BfXfS2lg9NRcHiEGIkLSP0m-_vswMQbuUUfXAQQTO-jcqQJIqN53Xq7htykb5S6OHCv0YQKCHsikyB6jg&isca=1" alt="Visualization" width="200px">

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
