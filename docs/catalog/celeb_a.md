<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="celeb_a" />
  <meta itemprop="description" content="CelebFaces Attributes Dataset (CelebA) is a large-scale face attributes dataset with more than 200K celebrity images, each with 40 attribute annotations. The images in this dataset cover large pose variations and background clutter. CelebA has large diversities, large quantities, and rich annotations, including&#10; - 10,177 number of identities,&#10; - 202,599 number of face images, and&#10; - 5 landmark locations, 40 binary attributes annotations per image.&#10;&#10;The dataset can be employed as the training and test sets for the following computer vision tasks: face attribute recognition, face detection, and landmark (or facial part) localization.&#10;&#10;Note: CelebA dataset may contain potential bias. The fairness indicators&#10;[example](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_CelebA_Case_Study)&#10;goes into detail about several considerations to keep in mind while using the&#10;CelebA dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;celeb_a&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a-2.0.1.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/celeb_a" />
  <meta itemprop="sameAs" content="http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html" />
  <meta itemprop="citation" content="@inproceedings{conf/iccv/LiuLWT15,&#10;  added-at = {2018-10-09T00:00:00.000+0200},&#10;  author = {Liu, Ziwei and Luo, Ping and Wang, Xiaogang and Tang, Xiaoou},&#10;  biburl = {https://www.bibsonomy.org/bibtex/250e4959be61db325d2f02c1d8cd7bfbb/dblp},&#10;  booktitle = {ICCV},&#10;  crossref = {conf/iccv/2015},&#10;  ee = {http://doi.ieeecomputersociety.org/10.1109/ICCV.2015.425},&#10;  interhash = {3f735aaa11957e73914bbe2ca9d5e702},&#10;  intrahash = {50e4959be61db325d2f02c1d8cd7bfbb},&#10;  isbn = {978-1-4673-8391-2},&#10;  keywords = {dblp},&#10;  pages = {3730-3738},&#10;  publisher = {IEEE Computer Society},&#10;  timestamp = {2018-10-11T11:43:28.000+0200},&#10;  title = {Deep Learning Face Attributes in the Wild.},&#10;  url = {http://dblp.uni-trier.de/db/conf/iccv/iccv2015.html#LiuLWT15},&#10;  year = 2015&#10;}" />
</div>

# `celeb_a`


*   **Visualization**:
    <a class="button button-with-icon" href="https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=celeb_a">
    Explore in Know Your Data
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Description**:

CelebFaces Attributes Dataset (CelebA) is a large-scale face attributes dataset
with more than 200K celebrity images, each with 40 attribute annotations. The
images in this dataset cover large pose variations and background clutter.
CelebA has large diversities, large quantities, and rich annotations,
including - 10,177 number of identities, - 202,599 number of face images, and -
5 landmark locations, 40 binary attributes annotations per image.

The dataset can be employed as the training and test sets for the following
computer vision tasks: face attribute recognition, face detection, and landmark
(or facial part) localization.

Note: CelebA dataset may contain potential bias. The fairness indicators
[example](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_CelebA_Case_Study)
goes into detail about several considerations to keep in mind while using the
CelebA dataset.

*   **Homepage**:
    [http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

*   **Source code**:
    [`tfds.image.CelebA`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/celeba.py)

*   **Versions**:

    *   `2.0.0`: No release notes.
    *   **`2.0.1`** (default): New split API
        (https://tensorflow.org/datasets/splits)

*   **Download size**: `1.38 GiB`

*   **Dataset size**: `1.62 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 19,962
`'train'`      | 162,770
`'validation'` | 19,867

*   **Feature structure**:

```python
FeaturesDict({
    'attributes': FeaturesDict({
        '5_o_Clock_Shadow': tf.bool,
        'Arched_Eyebrows': tf.bool,
        'Attractive': tf.bool,
        'Bags_Under_Eyes': tf.bool,
        'Bald': tf.bool,
        'Bangs': tf.bool,
        'Big_Lips': tf.bool,
        'Big_Nose': tf.bool,
        'Black_Hair': tf.bool,
        'Blond_Hair': tf.bool,
        'Blurry': tf.bool,
        'Brown_Hair': tf.bool,
        'Bushy_Eyebrows': tf.bool,
        'Chubby': tf.bool,
        'Double_Chin': tf.bool,
        'Eyeglasses': tf.bool,
        'Goatee': tf.bool,
        'Gray_Hair': tf.bool,
        'Heavy_Makeup': tf.bool,
        'High_Cheekbones': tf.bool,
        'Male': tf.bool,
        'Mouth_Slightly_Open': tf.bool,
        'Mustache': tf.bool,
        'Narrow_Eyes': tf.bool,
        'No_Beard': tf.bool,
        'Oval_Face': tf.bool,
        'Pale_Skin': tf.bool,
        'Pointy_Nose': tf.bool,
        'Receding_Hairline': tf.bool,
        'Rosy_Cheeks': tf.bool,
        'Sideburns': tf.bool,
        'Smiling': tf.bool,
        'Straight_Hair': tf.bool,
        'Wavy_Hair': tf.bool,
        'Wearing_Earrings': tf.bool,
        'Wearing_Hat': tf.bool,
        'Wearing_Lipstick': tf.bool,
        'Wearing_Necklace': tf.bool,
        'Wearing_Necktie': tf.bool,
        'Young': tf.bool,
    }),
    'image': Image(shape=(218, 178, 3), dtype=tf.uint8),
    'landmarks': FeaturesDict({
        'lefteye_x': tf.int64,
        'lefteye_y': tf.int64,
        'leftmouth_x': tf.int64,
        'leftmouth_y': tf.int64,
        'nose_x': tf.int64,
        'nose_y': tf.int64,
        'righteye_x': tf.int64,
        'righteye_y': tf.int64,
        'rightmouth_x': tf.int64,
        'rightmouth_y': tf.int64,
    }),
})
```

*   **Feature documentation**:

Feature                        | Class        | Shape         | Dtype    | Description
:----------------------------- | :----------- | :------------ | :------- | :----------
                               | FeaturesDict |               |          |
attributes                     | FeaturesDict |               |          |
attributes/5_o_Clock_Shadow    | Tensor       |               | tf.bool  |
attributes/Arched_Eyebrows     | Tensor       |               | tf.bool  |
attributes/Attractive          | Tensor       |               | tf.bool  |
attributes/Bags_Under_Eyes     | Tensor       |               | tf.bool  |
attributes/Bald                | Tensor       |               | tf.bool  |
attributes/Bangs               | Tensor       |               | tf.bool  |
attributes/Big_Lips            | Tensor       |               | tf.bool  |
attributes/Big_Nose            | Tensor       |               | tf.bool  |
attributes/Black_Hair          | Tensor       |               | tf.bool  |
attributes/Blond_Hair          | Tensor       |               | tf.bool  |
attributes/Blurry              | Tensor       |               | tf.bool  |
attributes/Brown_Hair          | Tensor       |               | tf.bool  |
attributes/Bushy_Eyebrows      | Tensor       |               | tf.bool  |
attributes/Chubby              | Tensor       |               | tf.bool  |
attributes/Double_Chin         | Tensor       |               | tf.bool  |
attributes/Eyeglasses          | Tensor       |               | tf.bool  |
attributes/Goatee              | Tensor       |               | tf.bool  |
attributes/Gray_Hair           | Tensor       |               | tf.bool  |
attributes/Heavy_Makeup        | Tensor       |               | tf.bool  |
attributes/High_Cheekbones     | Tensor       |               | tf.bool  |
attributes/Male                | Tensor       |               | tf.bool  |
attributes/Mouth_Slightly_Open | Tensor       |               | tf.bool  |
attributes/Mustache            | Tensor       |               | tf.bool  |
attributes/Narrow_Eyes         | Tensor       |               | tf.bool  |
attributes/No_Beard            | Tensor       |               | tf.bool  |
attributes/Oval_Face           | Tensor       |               | tf.bool  |
attributes/Pale_Skin           | Tensor       |               | tf.bool  |
attributes/Pointy_Nose         | Tensor       |               | tf.bool  |
attributes/Receding_Hairline   | Tensor       |               | tf.bool  |
attributes/Rosy_Cheeks         | Tensor       |               | tf.bool  |
attributes/Sideburns           | Tensor       |               | tf.bool  |
attributes/Smiling             | Tensor       |               | tf.bool  |
attributes/Straight_Hair       | Tensor       |               | tf.bool  |
attributes/Wavy_Hair           | Tensor       |               | tf.bool  |
attributes/Wearing_Earrings    | Tensor       |               | tf.bool  |
attributes/Wearing_Hat         | Tensor       |               | tf.bool  |
attributes/Wearing_Lipstick    | Tensor       |               | tf.bool  |
attributes/Wearing_Necklace    | Tensor       |               | tf.bool  |
attributes/Wearing_Necktie     | Tensor       |               | tf.bool  |
attributes/Young               | Tensor       |               | tf.bool  |
image                          | Image        | (218, 178, 3) | tf.uint8 |
landmarks                      | FeaturesDict |               |          |
landmarks/lefteye_x            | Tensor       |               | tf.int64 |
landmarks/lefteye_y            | Tensor       |               | tf.int64 |
landmarks/leftmouth_x          | Tensor       |               | tf.int64 |
landmarks/leftmouth_y          | Tensor       |               | tf.int64 |
landmarks/nose_x               | Tensor       |               | tf.int64 |
landmarks/nose_y               | Tensor       |               | tf.int64 |
landmarks/righteye_x           | Tensor       |               | tf.int64 |
landmarks/righteye_y           | Tensor       |               | tf.int64 |
landmarks/rightmouth_x         | Tensor       |               | tf.int64 |
landmarks/rightmouth_y         | Tensor       |               | tf.int64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a-2.0.1.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a-2.0.1.html";
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
@inproceedings{conf/iccv/LiuLWT15,
  added-at = {2018-10-09T00:00:00.000+0200},
  author = {Liu, Ziwei and Luo, Ping and Wang, Xiaogang and Tang, Xiaoou},
  biburl = {https://www.bibsonomy.org/bibtex/250e4959be61db325d2f02c1d8cd7bfbb/dblp},
  booktitle = {ICCV},
  crossref = {conf/iccv/2015},
  ee = {http://doi.ieeecomputersociety.org/10.1109/ICCV.2015.425},
  interhash = {3f735aaa11957e73914bbe2ca9d5e702},
  intrahash = {50e4959be61db325d2f02c1d8cd7bfbb},
  isbn = {978-1-4673-8391-2},
  keywords = {dblp},
  pages = {3730-3738},
  publisher = {IEEE Computer Society},
  timestamp = {2018-10-11T11:43:28.000+0200},
  title = {Deep Learning Face Attributes in the Wild.},
  url = {http://dblp.uni-trier.de/db/conf/iccv/iccv2015.html#LiuLWT15},
  year = 2015
}
```

