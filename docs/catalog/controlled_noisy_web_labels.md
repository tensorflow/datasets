<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="controlled_noisy_web_labels" />
  <meta itemprop="description" content="Controlled Noisy Web Labels is a collection of ~212,000 URLs to images in which&#10;every image is carefully annotated by 3-5 labeling professionals by Google Cloud&#10;Data Labeling Service. Using these annotations, it establishes the first&#10;benchmark of controlled real-world label noise from the web.&#10;&#10;We provide the Red Mini-ImageNet (real-world web noise) and Blue Mini-ImageNet&#10;configs:&#10;  - controlled_noisy_web_labels/mini_imagenet_red&#10;  - controlled_noisy_web_labels/mini_imagenet_blue&#10;&#10;Each config contains ten variants with ten noise-levels p from 0% to 80%. The&#10;validation set has clean labels and is shared across all noisy training sets.&#10;Therefore, each config has the following splits:&#10;&#10;  - train_00&#10;  - train_05&#10;  - train_10&#10;  - train_15&#10;  - train_20&#10;  - train_30&#10;  - train_40&#10;  - train_50&#10;  - train_60&#10;  - train_80&#10;  - validation&#10;&#10;The details for dataset construction and analysis can be found in the paper.&#10;All images are resized to 84x84 resolution.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;controlled_noisy_web_labels&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/controlled_noisy_web_labels-mini_imagenet_red-1.0.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/controlled_noisy_web_labels" />
  <meta itemprop="sameAs" content="https://google.github.io/controlled-noisy-web-labels/index.html" />
  <meta itemprop="citation" content="@inproceedings{jiang2020beyond,&#10;  title={Beyond synthetic noise: Deep learning on controlled noisy labels},&#10;  author={Jiang, Lu and Huang, Di and Liu, Mason and Yang, Weilong},&#10;  booktitle={International Conference on Machine Learning},&#10;  pages={4804--4815},&#10;  year={2020},&#10;  organization={PMLR}&#10;}" />
</div>

# `controlled_noisy_web_labels`


Warning: Manual download required. See instructions below.

*   **Description**:

Controlled Noisy Web Labels is a collection of ~212,000 URLs to images in which
every image is carefully annotated by 3-5 labeling professionals by Google Cloud
Data Labeling Service. Using these annotations, it establishes the first
benchmark of controlled real-world label noise from the web.

We provide the Red Mini-ImageNet (real-world web noise) and Blue Mini-ImageNet
configs: - controlled_noisy_web_labels/mini_imagenet_red -
controlled_noisy_web_labels/mini_imagenet_blue

Each config contains ten variants with ten noise-levels p from 0% to 80%. The
validation set has clean labels and is shared across all noisy training sets.
Therefore, each config has the following splits:

-   train_00
-   train_05
-   train_10
-   train_15
-   train_20
-   train_30
-   train_40
-   train_50
-   train_60
-   train_80
-   validation

The details for dataset construction and analysis can be found in the paper. All
images are resized to 84x84 resolution.

*   **Homepage**:
    [https://google.github.io/controlled-noisy-web-labels/index.html](https://google.github.io/controlled-noisy-web-labels/index.html)

*   **Source code**:
    [`tfds.image_classification.controlled_noisy_web_labels.ControlledNoisyWebLabels`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/controlled_noisy_web_labels/controlled_noisy_web_labels.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `1.83 MiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    In order to manually download this data, a user must perform the
    following operations:

1.  Download the splits and the annotations
    [here](https://storage.googleapis.com/cnlw/dataset_no_images.zip)
2.  Extract dataset_no_images.zip to dataset_no_images/.
3.  Download all images in dataset_no_images/mini-imagenet-annotations.json into
    a new folder named dataset_no_images/noisy_images/. The output filename must
    agree with the image id provided in mini-imagenet-annotations.json. For
    example, if "image/id": "5922767e5677aef4", then the downloaded image should
    be dataset_no_images/noisy_images/5922767e5677aef4.jpg. 4.Register on
    https://image-net.org/download-images and download ILSVRC2012_img_train.tar
    and ILSVRC2012_img_val.tar.

The resulting directory structure may then be processed by TFDS:

-   dataset_no_images/
    -   mini-imagenet/
    -   class_name.txt
    -   split/
        -   blue_noise_nl_0.0
        -   blue_noise_nl_0.1
        -   ...
        -   red_noise_nl_0.0
        -   red_noise_nl_0.1
        -   ...
        -   clean_validation
    -   mini-imagenet-annotations.json
-   ILSVRC2012_img_train.tar
-   ILSVRC2012_img_val.tar
-   noisy_images/

    -   5922767e5677aef4.jpg

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'id': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'is_clean': tf.bool,
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=100),
})
```

*   **Feature documentation**:

Feature  | Class        | Shape           | Dtype     | Description
:------- | :----------- | :-------------- | :-------- | :----------
         | FeaturesDict |                 |           |
id       | Text         |                 | tf.string |
image    | Image        | (None, None, 3) | tf.uint8  |
is_clean | Tensor       |                 | tf.bool   |
label    | ClassLabel   |                 | tf.int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Citation**:

```
@inproceedings{jiang2020beyond,
  title={Beyond synthetic noise: Deep learning on controlled noisy labels},
  author={Jiang, Lu and Huang, Di and Liu, Mason and Yang, Weilong},
  booktitle={International Conference on Machine Learning},
  pages={4804--4815},
  year={2020},
  organization={PMLR}
}
```


## controlled_noisy_web_labels/mini_imagenet_red (default config)

*   **Dataset size**: `1.19 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train_00'`   | 50,000
`'train_05'`   | 50,000
`'train_10'`   | 50,000
`'train_15'`   | 50,000
`'train_20'`   | 50,000
`'train_30'`   | 49,985
`'train_40'`   | 50,010
`'train_50'`   | 49,962
`'train_60'`   | 50,000
`'train_80'`   | 50,008
`'validation'` | 5,000

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/controlled_noisy_web_labels-mini_imagenet_red-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/controlled_noisy_web_labels-mini_imagenet_red-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

## controlled_noisy_web_labels/mini_imagenet_blue

*   **Dataset size**: `1.39 GiB`

*   **Splits**:

Split          | Examples
:------------- | -------:
`'train_00'`   | 60,000
`'train_05'`   | 60,000
`'train_10'`   | 60,000
`'train_15'`   | 60,000
`'train_20'`   | 60,000
`'train_30'`   | 60,000
`'train_40'`   | 60,000
`'train_50'`   | 60,000
`'train_60'`   | 60,000
`'train_80'`   | 60,000
`'validation'` | 5,000

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/controlled_noisy_web_labels-mini_imagenet_blue-1.0.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/controlled_noisy_web_labels-mini_imagenet_blue-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->