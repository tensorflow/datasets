<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="imagenet2012" />
  <meta itemprop="description" content="ILSVRC 2012, commonly known as &#x27;ImageNet&#x27; is an image dataset organized&#10;according to the WordNet hierarchy. Each meaningful concept in WordNet, possibly&#10;described by multiple words or word phrases, is called a &quot;synonym set&quot; or&#10;&quot;synset&quot;. There are more than 100,000 synsets in WordNet, majority of them are&#10;nouns (80,000+). In ImageNet, we aim to provide on average 1000 images to&#10;illustrate each synset. Images of each concept are quality-controlled and&#10;human-annotated. In its completion, we hope ImageNet will offer tens of millions&#10;of cleanly sorted images for most of the concepts in the WordNet hierarchy.&#10;&#10;The test split contains 100K images but no labels because no labels have been&#10;publicly released. We provide support for the test split from 2012 with the&#10;minor patch released on October 10, 2019. In order to manually download this&#10;data, a user must perform the following operations:&#10;&#10;1.  Download the 2012 test split available&#10;    [here](https://image-net.org/challenges/LSVRC/2012/2012-downloads.php#Images).&#10;2.  Download the October 10, 2019 patch. There is a Google Drive link to the&#10;    patch provided on the same page.&#10;3.  Combine the two tar-balls, manually overwriting any images in the original&#10;    archive with images from the patch. According to the instructions on&#10;    image-net.org, this procedure overwrites just a few images.&#10;&#10;The resulting tar-ball may then be processed by TFDS.&#10;&#10;To assess the accuracy of a model on the ImageNet test split, one must run&#10;inference on all images in the split, export those results to a text file that&#10;must be uploaded to the ImageNet evaluation server. The maintainers of the&#10;ImageNet evaluation server permits a single user to submit up to 2 submissions&#10;per week in order to prevent overfitting.&#10;&#10;To evaluate the accuracy on the test split, one must first create an account at&#10;image-net.org. This account must be approved by the site administrator. After&#10;the account is created, one can submit the results to the test server at&#10;https://image-net.org/challenges/LSVRC/eval_server.php The submission consists&#10;of several ASCII text files corresponding to multiple tasks. The task of&#10;interest is &quot;Classification submission (top-5 cls error)&quot;. A sample of an&#10;exported text file looks like the following:&#10;&#10;```&#10;771 778 794 387 650&#10;363 691 764 923 427&#10;737 369 430 531 124&#10;755 930 755 59 168&#10;```&#10;&#10;The export format is described in full in &quot;readme.txt&quot; within the 2013&#10;development kit available here:&#10;https://image-net.org/data/ILSVRC/2013/ILSVRC2013_devkit.tgz Please see the&#10;section entitled &quot;3.3 CLS-LOC submission format&quot;. Briefly, the format of the&#10;text file is 100,000 lines corresponding to each image in the test split. Each&#10;line of integers correspond to the rank-ordered, top 5 predictions for each test&#10;image. The integers are 1-indexed corresponding to the line number in the&#10;corresponding labels file. See labels.txt.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet2012&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012-5.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet2012" />
  <meta itemprop="sameAs" content="https://image-net.org/" />
  <meta itemprop="citation" content="@article{ILSVRC15,&#10;Author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},&#10;Title = {{ImageNet Large Scale Visual Recognition Challenge}},&#10;Year = {2015},&#10;journal   = {International Journal of Computer Vision (IJCV)},&#10;doi = {10.1007/s11263-015-0816-y},&#10;volume={115},&#10;number={3},&#10;pages={211-252}&#10;}" />
</div>

# `imagenet2012`


Warning: Manual download required. See instructions below.

*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=imagenet2012">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

ILSVRC 2012, commonly known as 'ImageNet' is an image dataset organized
according to the WordNet hierarchy. Each meaningful concept in WordNet, possibly
described by multiple words or word phrases, is called a "synonym set" or
"synset". There are more than 100,000 synsets in WordNet, majority of them are
nouns (80,000+). In ImageNet, we aim to provide on average 1000 images to
illustrate each synset. Images of each concept are quality-controlled and
human-annotated. In its completion, we hope ImageNet will offer tens of millions
of cleanly sorted images for most of the concepts in the WordNet hierarchy.

The test split contains 100K images but no labels because no labels have been
publicly released. We provide support for the test split from 2012 with the
minor patch released on October 10, 2019. In order to manually download this
data, a user must perform the following operations:

1.  Download the 2012 test split available
    [here](https://image-net.org/challenges/LSVRC/2012/2012-downloads.php#Images).
2.  Download the October 10, 2019 patch. There is a Google Drive link to the
    patch provided on the same page.
3.  Combine the two tar-balls, manually overwriting any images in the original
    archive with images from the patch. According to the instructions on
    image-net.org, this procedure overwrites just a few images.

The resulting tar-ball may then be processed by TFDS.

To assess the accuracy of a model on the ImageNet test split, one must run
inference on all images in the split, export those results to a text file that
must be uploaded to the ImageNet evaluation server. The maintainers of the
ImageNet evaluation server permits a single user to submit up to 2 submissions
per week in order to prevent overfitting.

To evaluate the accuracy on the test split, one must first create an account at
image-net.org. This account must be approved by the site administrator. After
the account is created, one can submit the results to the test server at
https://image-net.org/challenges/LSVRC/eval_server.php The submission consists
of several ASCII text files corresponding to multiple tasks. The task of
interest is "Classification submission (top-5 cls error)". A sample of an
exported text file looks like the following:

```
771 778 794 387 650
363 691 764 923 427
737 369 430 531 124
755 930 755 59 168
```

The export format is described in full in "readme.txt" within the 2013
development kit available here:
https://image-net.org/data/ILSVRC/2013/ILSVRC2013_devkit.tgz Please see the
section entitled "3.3 CLS-LOC submission format". Briefly, the format of the
text file is 100,000 lines corresponding to each image in the test split. Each
line of integers correspond to the rank-ordered, top 5 predictions for each test
image. The integers are 1-indexed corresponding to the line number in the
corresponding labels file. See labels.txt.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/imagenet">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**: [https://image-net.org/](https://image-net.org/)

*   **Source code**:
    [`tfds.datasets.imagenet2012.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/imagenet2012/imagenet2012_dataset_builder.py)

*   **Versions**:

    *   `2.0.0`: Fix validation labels.
    *   `2.0.1`: Encoding fix. No changes from user point of view.
    *   `3.0.0`: Fix colorization on ~12 images (CMYK -> RGB). Fix format for
        consistency (convert the single png image to Jpeg). Faster generation
        reading directly from the archive.

    *   `4.0.0`: (unpublished)

    *   `5.0.0`: New split API (https://tensorflow.org/datasets/splits)

    *   **`5.1.0`** (default): Added test split.

*   **Download size**: `Unknown size`

*   **Dataset size**: `155.84 GiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    manual_dir should contain two files: ILSVRC2012_img_train.tar and
    ILSVRC2012_img_val.tar.
    You need to register on https://image-net.org/download-images in order
    to get the link to download the dataset.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | --------:
`'test'`       | 100,000
`'train'`      | 1,281,167
`'validation'` | 50,000

*   **Feature structure**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=string),
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'label': ClassLabel(shape=(), dtype=int64, num_classes=1000),
})
```

*   **Feature documentation**:

Feature   | Class        | Shape           | Dtype  | Description
:-------- | :----------- | :-------------- | :----- | :----------
          | FeaturesDict |                 |        |
file_name | Text         |                 | string |
image     | Image        | (None, None, 3) | uint8  |
label     | ClassLabel   |                 | int64  |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012-5.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/imagenet2012-5.1.0.html";
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

*   **Citation**:

```
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

