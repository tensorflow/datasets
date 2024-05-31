<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="celeb_a" />
  <meta itemprop="description" content="CelebFaces Attributes Dataset (CelebA) is a large-scale face attributes dataset&#10;with more than 200K celebrity images, each with 40 attribute annotations. The&#10;images in this dataset cover large pose variations and background clutter.&#10;CelebA has large diversities, large quantities, and rich annotations,&#10;including - 10,177 number of identities, - 202,599 number of face images, and -&#10;5 landmark locations, 40 binary attributes annotations per image.&#10;&#10;The dataset can be employed as the training and test sets for the following&#10;computer vision tasks: face attribute recognition, face detection, and landmark&#10;(or facial part) localization.&#10;&#10;Note: CelebA dataset may contain potential bias. The fairness indicators&#10;[example](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_CelebA_Case_Study)&#10;goes into detail about several considerations to keep in mind while using the&#10;CelebA dataset.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;celeb_a&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a-2.1.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/celeb_a" />
  <meta itemprop="sameAs" content="http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html" />
  <meta itemprop="citation" content="@inproceedings{conf/iccv/LiuLWT15,&#10;  added-at = {2018-10-09T00:00:00.000+0200},&#10;  author = {Liu, Ziwei and Luo, Ping and Wang, Xiaogang and Tang, Xiaoou},&#10;  biburl = {https://www.bibsonomy.org/bibtex/250e4959be61db325d2f02c1d8cd7bfbb/dblp},&#10;  booktitle = {ICCV},&#10;  crossref = {conf/iccv/2015},&#10;  ee = {http://doi.ieeecomputersociety.org/10.1109/ICCV.2015.425},&#10;  interhash = {3f735aaa11957e73914bbe2ca9d5e702},&#10;  intrahash = {50e4959be61db325d2f02c1d8cd7bfbb},&#10;  isbn = {978-1-4673-8391-2},&#10;  keywords = {dblp},&#10;  pages = {3730-3738},&#10;  publisher = {IEEE Computer Society},&#10;  timestamp = {2018-10-11T11:43:28.000+0200},&#10;  title = {Deep Learning Face Attributes in the Wild.},&#10;  url = {http://dblp.uni-trier.de/db/conf/iccv/iccv2015.html#LiuLWT15},&#10;  year = 2015&#10;}" />
</div>

# `celeb_a`


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

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/celeba">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

*   **Source code**:
    [`tfds.datasets.celeb_a.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/celeb_a/celeb_a_dataset_builder.py)

*   **Versions**:

    *   `2.0.1`: New split API (https://tensorflow.org/datasets/splits)
    *   **`2.1.0`** (default): Identity feature added.

*   **Download size**: `1.39 GiB`

*   **Dataset size**: `1.63 GiB`

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
        '5_o_Clock_Shadow': bool,
        'Arched_Eyebrows': bool,
        'Attractive': bool,
        'Bags_Under_Eyes': bool,
        'Bald': bool,
        'Bangs': bool,
        'Big_Lips': bool,
        'Big_Nose': bool,
        'Black_Hair': bool,
        'Blond_Hair': bool,
        'Blurry': bool,
        'Brown_Hair': bool,
        'Bushy_Eyebrows': bool,
        'Chubby': bool,
        'Double_Chin': bool,
        'Eyeglasses': bool,
        'Goatee': bool,
        'Gray_Hair': bool,
        'Heavy_Makeup': bool,
        'High_Cheekbones': bool,
        'Male': bool,
        'Mouth_Slightly_Open': bool,
        'Mustache': bool,
        'Narrow_Eyes': bool,
        'No_Beard': bool,
        'Oval_Face': bool,
        'Pale_Skin': bool,
        'Pointy_Nose': bool,
        'Receding_Hairline': bool,
        'Rosy_Cheeks': bool,
        'Sideburns': bool,
        'Smiling': bool,
        'Straight_Hair': bool,
        'Wavy_Hair': bool,
        'Wearing_Earrings': bool,
        'Wearing_Hat': bool,
        'Wearing_Lipstick': bool,
        'Wearing_Necklace': bool,
        'Wearing_Necktie': bool,
        'Young': bool,
    }),
    'identity': FeaturesDict({
        'Identity_No': int64,
    }),
    'image': Image(shape=(218, 178, 3), dtype=uint8),
    'landmarks': FeaturesDict({
        'lefteye_x': int64,
        'lefteye_y': int64,
        'leftmouth_x': int64,
        'leftmouth_y': int64,
        'nose_x': int64,
        'nose_y': int64,
        'righteye_x': int64,
        'righteye_y': int64,
        'rightmouth_x': int64,
        'rightmouth_y': int64,
    }),
})
```

*   **Feature documentation**:

| Feature                        | Class        | Shape | Dtype | Description |
| :----------------------------- | :----------- | :---- | :---- | :---------- |
|                                | FeaturesDict |       |       |             |
| attributes                     | FeaturesDict |       |       |             |
| attributes/5_o_Clock_Shadow    | Tensor       |       | bool  |             |
| attributes/Arched_Eyebrows     | Tensor       |       | bool  |             |
| attributes/Attractive          | Tensor       |       | bool  |             |
| attributes/Bags_Under_Eyes     | Tensor       |       | bool  |             |
| attributes/Bald                | Tensor       |       | bool  |             |
| attributes/Bangs               | Tensor       |       | bool  |             |
| attributes/Big_Lips            | Tensor       |       | bool  |             |
| attributes/Big_Nose            | Tensor       |       | bool  |             |
| attributes/Black_Hair          | Tensor       |       | bool  |             |
| attributes/Blond_Hair          | Tensor       |       | bool  |             |
| attributes/Blurry              | Tensor       |       | bool  |             |
| attributes/Brown_Hair          | Tensor       |       | bool  |             |
| attributes/Bushy_Eyebrows      | Tensor       |       | bool  |             |
| attributes/Chubby              | Tensor       |       | bool  |             |
| attributes/Double_Chin         | Tensor       |       | bool  |             |
| attributes/Eyeglasses          | Tensor       |       | bool  |             |
| attributes/Goatee              | Tensor       |       | bool  |             |
| attributes/Gray_Hair           | Tensor       |       | bool  |             |
| attributes/Heavy_Makeup        | Tensor       |       | bool  |             |
| attributes/High_Cheekbones     | Tensor       |       | bool  |             |
| attributes/Male                | Tensor       |       | bool  |             |
| attributes/Mouth_Slightly_Open | Tensor       |       | bool  |             |
| attributes/Mustache            | Tensor       |       | bool  |             |
| attributes/Narrow_Eyes         | Tensor       |       | bool  |             |
| attributes/No_Beard            | Tensor       |       | bool  |             |
| attributes/Oval_Face           | Tensor       |       | bool  |             |
| attributes/Pale_Skin           | Tensor       |       | bool  |             |
| attributes/Pointy_Nose         | Tensor       |       | bool  |             |
| attributes/Receding_Hairline   | Tensor       |       | bool  |             |
| attributes/Rosy_Cheeks         | Tensor       |       | bool  |             |
| attributes/Sideburns           | Tensor       |       | bool  |             |
| attributes/Smiling             | Tensor       |       | bool  |             |
| attributes/Straight_Hair       | Tensor       |       | bool  |             |
| attributes/Wavy_Hair           | Tensor       |       | bool  |             |
| attributes/Wearing_Earrings    | Tensor       |       | bool  |             |
| attributes/Wearing_Hat         | Tensor       |       | bool  |             |
| attributes/Wearing_Lipstick    | Tensor       |       | bool  |             |
| attributes/Wearing_Necklace    | Tensor       |       | bool  |             |
| attributes/Wearing_Necktie     | Tensor       |       | bool  |             |
| attributes/Young               | Tensor       |       | bool  |             |
| identity                       | FeaturesDict |       |       |             |
| identity/Identity_No           | Tensor       |       | int64 |             |
| image                          | Image        | (218, | uint8 |             |
:                                :              : 178,  :       :             :
:                                :              : 3)    :       :             :
| landmarks                      | FeaturesDict |       |       |             |
| landmarks/lefteye_x            | Tensor       |       | int64 |             |
| landmarks/lefteye_y            | Tensor       |       | int64 |             |
| landmarks/leftmouth_x          | Tensor       |       | int64 |             |
| landmarks/leftmouth_y          | Tensor       |       | int64 |             |
| landmarks/nose_x               | Tensor       |       | int64 |             |
| landmarks/nose_y               | Tensor       |       | int64 |             |
| landmarks/righteye_x           | Tensor       |       | int64 |             |
| landmarks/righteye_y           | Tensor       |       | int64 |             |
| landmarks/rightmouth_x         | Tensor       |       | int64 |             |
| landmarks/rightmouth_y         | Tensor       |       | int64 |             |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/celeb_a-2.1.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/celeb_a-2.1.0.html";
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

