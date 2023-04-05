<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet_pi" />
  <meta itemprop="description" content="ImageNet-PI is a relabelled version of the standard ILSVRC2012 ImageNet&#10;dataset in which the labels are provided by a collection of 16 deep neural&#10;networks with different architectures pre-trained on the standard&#10;ILSVRC2012. Specifically, the pre-trained models are downloaded from&#10;tf.keras.applications.&#10;&#10;In addition to the new labels, ImageNet-PI also provides meta-data about the&#10;annotation process in the form of confidences of the models on their labels&#10;and additional information about each model.&#10;&#10;For more information see: [ImageNet-PI](https://github.com/google-research-datasets/imagenet_pi)&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet_pi&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet_pi" />
  <meta itemprop="sameAs" content="https://github.com/google-research-datasets/imagenet_pi/" />
  <meta itemprop="citation" content="@inproceedings{tram,&#10;  author    = {Mark Collier and&#10;               Rodolphe Jenatton and&#10;               Effrosyni Kokiopoulou and&#10;               Jesse Berent},&#10;  editor    = {Kamalika Chaudhuri and&#10;               Stefanie Jegelka and&#10;               Le Song and&#10;               Csaba Szepesv{\&#x27;{a}}ri and&#10;               Gang Niu and&#10;               Sivan Sabato},&#10;  title     = {Transfer and Marginalize: Explaining Away Label Noise with Privileged&#10;               Information},&#10;  booktitle = {International Conference on Machine Learning, {ICML} 2022, 17-23 July&#10;               2022, Baltimore, Maryland, {USA}},&#10;  series    = {Proceedings of Machine Learning Research},&#10;  volume    = {162},&#10;  pages     = {4219--4237},&#10;  publisher = {{PMLR}},&#10;  year      = {2022},&#10;  url       = {https://proceedings.mlr.press/v162/collier22a.html},&#10;}&#10;@article{ILSVRC15,&#10;Author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},&#10;Title = {{ImageNet Large Scale Visual Recognition Challenge}},&#10;Year = {2015},&#10;journal   = {International Journal of Computer Vision (IJCV)},&#10;doi = {10.1007/s11263-015-0816-y},&#10;volume={115},&#10;number={3},&#10;pages={211-252}&#10;}" />
</div>

# `imagenet_pi`


Warning: Manual download required. See instructions below.

*   **Description**:

ImageNet-PI is a relabelled version of the standard ILSVRC2012 ImageNet dataset
in which the labels are provided by a collection of 16 deep neural networks with
different architectures pre-trained on the standard ILSVRC2012. Specifically,
the pre-trained models are downloaded from tf.keras.applications.

In addition to the new labels, ImageNet-PI also provides meta-data about the
annotation process in the form of confidences of the models on their labels and
additional information about each model.

For more information see:
[ImageNet-PI](https://github.com/google-research-datasets/imagenet_pi)

*   **Homepage**:
    [https://github.com/google-research-datasets/imagenet_pi/](https://github.com/google-research-datasets/imagenet_pi/)

*   **Source code**:
    [`tfds.datasets.imagenet_pi.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/imagenet_pi/imagenet_pi_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    manual_dir should contain two files: ILSVRC2012_img_train.tar and
    ILSVRC2012_img_val.tar.
    You need to register on http://www.image-net.org/download-images in order
    to get the link to download the dataset.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Feature structure**:

```python
FeaturesDict({
    'annotator_confidences': Tensor(shape=(16,), dtype=float32),
    'annotator_labels': Tensor(shape=(16,), dtype=int64),
    'clean_label': ClassLabel(shape=(), dtype=int64, num_classes=1000),
    'file_name': Text(shape=(), dtype=string),
    'image': Image(shape=(None, None, 3), dtype=uint8),
})
```

*   **Feature documentation**:

Feature               | Class        | Shape           | Dtype   | Description
:-------------------- | :----------- | :-------------- | :------ | :----------
                      | FeaturesDict |                 |         |
annotator_confidences | Tensor       | (16,)           | float32 |
annotator_labels      | Tensor       | (16,)           | int64   |
clean_label           | ClassLabel   |                 | int64   |
file_name             | Text         |                 | string  |
image                 | Image        | (None, None, 3) | uint8   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'annotator_labels')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@inproceedings{tram,
  author    = {Mark Collier and
               Rodolphe Jenatton and
               Effrosyni Kokiopoulou and
               Jesse Berent},
  editor    = {Kamalika Chaudhuri and
               Stefanie Jegelka and
               Le Song and
               Csaba Szepesv{\'{a}}ri and
               Gang Niu and
               Sivan Sabato},
  title     = {Transfer and Marginalize: Explaining Away Label Noise with Privileged
               Information},
  booktitle = {International Conference on Machine Learning, {ICML} 2022, 17-23 July
               2022, Baltimore, Maryland, {USA}},
  series    = {Proceedings of Machine Learning Research},
  volume    = {162},
  pages     = {4219--4237},
  publisher = {{PMLR}},
  year      = {2022},
  url       = {https://proceedings.mlr.press/v162/collier22a.html},
}
@article{ILSVRC15,
Author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},
Title = {{ImageNet Large Scale Visual Recognition Challenge}},
Year = {2015},
journal   = {International Journal of Computer Vision (IJCV)},
doi = {10.1007/s11263-015-0816-y},
volume={115},
number={3},
pages={211-252}
}
```

