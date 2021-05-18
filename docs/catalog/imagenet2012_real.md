<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet2012_real" />
  <meta itemprop="description" content="This dataset contains ILSVRC-2012 (ImageNet) validation images augmented with a&#10;new set of &quot;Re-Assessed&quot; (ReaL) labels from the &quot;Are we done with ImageNet&quot;&#10;paper, see https://arxiv.org/abs/2006.07159. These labels are collected using&#10;the enhanced protocol, resulting in multi-label and more accurate annotations.&#10;&#10;Important note: about 3500 examples contain no label, these should be [excluded&#10;from the averaging when computing the accuracy](https://github.com/google-research/reassessed-imagenet#numpy).&#10;One possible way of doing this is with the following NumPy code:&#10;&#10;```python&#10;is_correct = [pred in real_labels[i] for i, pred in enumerate(predictions) if real_labels[i]]&#10;real_accuracy = np.mean(is_correct)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet2012_real&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012_real-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet2012_real" />
  <meta itemprop="sameAs" content="https://github.com/google-research/reassessed-imagenet" />
  <meta itemprop="citation" content="@article{beyer2020imagenet,&#10;  title={Are we done with ImageNet?},&#10;  author={Lucas Beyer and Olivier J. Henaff and Alexander Kolesnikov and Xiaohua Zhai and Aaron van den Oord},&#10;  journal={arXiv preprint arXiv:2002.05709},&#10;  year={2020}&#10;}&#10;@article{ILSVRC15,&#10;  Author={Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},&#10;  Title={{ImageNet Large Scale Visual Recognition Challenge}},&#10;  Year={2015},&#10;  journal={International Journal of Computer Vision (IJCV)},&#10;  doi={10.1007/s11263-015-0816-y},&#10;  volume={115},&#10;  number={3},&#10;  pages={211-252}&#10;}" />
</div>

# `imagenet2012_real`

Warning: Manual download required. See instructions below.

*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=imagenet2012_real">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

This dataset contains ILSVRC-2012 (ImageNet) validation images augmented with a
new set of "Re-Assessed" (ReaL) labels from the "Are we done with ImageNet"
paper, see https://arxiv.org/abs/2006.07159. These labels are collected using
the enhanced protocol, resulting in multi-label and more accurate annotations.

Important note: about 3500 examples contain no label, these should be
[excluded from the averaging when computing the accuracy](https://github.com/google-research/reassessed-imagenet#numpy).
One possible way of doing this is with the following NumPy code:

```python
is_correct = [pred in real_labels[i] for i, pred in enumerate(predictions) if real_labels[i]]
real_accuracy = np.mean(is_correct)
```

*   **Homepage**:
    [https://github.com/google-research/reassessed-imagenet](https://github.com/google-research/reassessed-imagenet)

*   **Source code**:
    [`tfds.image_classification.Imagenet2012Real`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/imagenet2012_real.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release

*   **Download size**: `379.37 KiB`

*   **Dataset size**: `6.25 GiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    manual_dir should contain `ILSVRC2012_img_val.tar` file.
    You need to register on http://www.image-net.org/download-images in order
    to get the link to download the dataset.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'validation'` | 50,000

*   **Features**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'original_label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
    'real_label': Sequence(ClassLabel(shape=(), dtype=tf.int64, num_classes=1000)),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'real_label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012_real-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet2012_real-1.0.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@article{beyer2020imagenet,
  title={Are we done with ImageNet?},
  author={Lucas Beyer and Olivier J. Henaff and Alexander Kolesnikov and Xiaohua Zhai and Aaron van den Oord},
  journal={arXiv preprint arXiv:2002.05709},
  year={2020}
}
@article{ILSVRC15,
  Author={Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},
  Title={{ImageNet Large Scale Visual Recognition Challenge}},
  Year={2015},
  journal={International Journal of Computer Vision (IJCV)},
  doi={10.1007/s11263-015-0816-y},
  volume={115},
  number={3},
  pages={211-252}
}
```
