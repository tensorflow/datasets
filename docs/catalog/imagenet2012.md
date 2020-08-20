<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="imagenet2012" />
  <meta itemprop="description" content="ILSVRC 2012, commonly known as &#x27;ImageNet&#x27; is an image dataset organized&#10;according to the WordNet hierarchy. Each meaningful concept in WordNet,&#10;possibly described by multiple words or word phrases, is called a &quot;synonym set&quot;&#10;or &quot;synset&quot;. There are more than 100,000 synsets in WordNet, majority of them&#10;are nouns (80,000+). In ImageNet, we aim to provide on average 1000 images to&#10;illustrate each synset. Images of each concept are quality-controlled and&#10;human-annotated. In its completion, we hope ImageNet will offer tens of&#10;millions of cleanly sorted images for most of the concepts in the WordNet&#10;hierarchy.&#10;&#10;The test split contains 100K images but no labels because no labels have been&#10;publicly released. To assess the accuracy of a model on the ImageNet test split,&#10;one must run inference on all images in the split, export those results to a&#10;text file that must be uploaded to the ImageNet evaluation server. The&#10;maintainers of the ImageNet evaluation server permits a single user to submit up&#10;to 2 submissions per week in order to prevent overfitting.&#10;&#10;To evaluate the accuracy on the test split, one must first create an account at&#10;image-net.org. This account must be approved by the site administrator. After&#10;the account is created, one can submit the results to the test server at&#10;http://www.image-net.org/challenges/LSVRC/2013/test_server&#10;The submission consists of several ASCII text files corresponding to multiple&#10;tasks. The task of interest is &quot;Classification submission (top-5 cls error)&quot;.&#10;A sample of an exported text file looks like the following:&#10;&#10;```&#10;771 778 794 387 650&#10;363 691 764 923 427&#10;737 369 430 531 124&#10;755 930 755 59 168&#10;```&#10;&#10;The export format is described in full in &quot;readme.txt&quot; within the 2013&#10;development kit available here:&#10;http://imagenet.stanford.edu/image/ilsvrc2013/ILSVRC2013_devkit.tgz&#10;Please see the section entitled &quot;3.3 CLS-LOC submission format&quot;. Briefly, the&#10;format of the text file is 100,000 lines corresponding to each image in the test&#10;split. Each line of integers correspond to the rank-ordered, top 5 predictions&#10;for each test image. The integers are 1-indexed corresponding to the line number&#10;in the corresponding labels file. See imagenet2012_labels.txt.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;imagenet2012&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012-5.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/imagenet2012" />
  <meta itemprop="sameAs" content="http://image-net.org/" />
  <meta itemprop="citation" content="@article{ILSVRC15,&#10;Author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},&#10;Title = {{ImageNet Large Scale Visual Recognition Challenge}},&#10;Year = {2015},&#10;journal   = {International Journal of Computer Vision (IJCV)},&#10;doi = {10.1007/s11263-015-0816-y},&#10;volume={115},&#10;number={3},&#10;pages={211-252}&#10;}" />
</div>

# `imagenet2012`

Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

Warning: Manual download required. See instructions below.

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
publicly released. To assess the accuracy of a model on the ImageNet test split,
one must run inference on all images in the split, export those results to a
text file that must be uploaded to the ImageNet evaluation server. The
maintainers of the ImageNet evaluation server permits a single user to submit up
to 2 submissions per week in order to prevent overfitting.

To evaluate the accuracy on the test split, one must first create an account at
image-net.org. This account must be approved by the site administrator. After
the account is created, one can submit the results to the test server at
http://www.image-net.org/challenges/LSVRC/2013/test_server The submission
consists of several ASCII text files corresponding to multiple tasks. The task
of interest is "Classification submission (top-5 cls error)". A sample of an
exported text file looks like the following:

```
771 778 794 387 650
363 691 764 923 427
737 369 430 531 124
755 930 755 59 168
```

The export format is described in full in "readme.txt" within the 2013
development kit available here:
http://imagenet.stanford.edu/image/ilsvrc2013/ILSVRC2013_devkit.tgz Please see
the section entitled "3.3 CLS-LOC submission format". Briefly, the format of the
text file is 100,000 lines corresponding to each image in the test split. Each
line of integers correspond to the rank-ordered, top 5 predictions for each test
image. The integers are 1-indexed corresponding to the line number in the
corresponding labels file. See imagenet2012_labels.txt.

*   **Homepage**: [http://image-net.org/](http://image-net.org/)

*   **Source code**:
    [`tfds.image_classification.Imagenet2012`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image_classification/imagenet.py)

*   **Versions**:

    *   **`5.1.0`** (default)
        <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>:
        Added test split.
    *   `5.0.0`: No release notes.

*   **Download size**: `Unknown size`

*   **Dataset size**: `155.84 GiB`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    manual_dir should contain two files: ILSVRC2012_img_train.tar and
    ILSVRC2012_img_val.tar.
    You need to register on http://www.image-net.org/download-images in order
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

*   **Features**:

```python
FeaturesDict({
    'file_name': Text(shape=(), dtype=tf.string),
    'image': Image(shape=(None, None, 3), dtype=tf.uint8),
    'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=1000),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'label')`

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

*   **Visualization**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/imagenet2012-5.1.0.png" alt="Visualization" width="500px">
