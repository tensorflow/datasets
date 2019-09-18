<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="celeb_a" />
  <meta itemprop="description" content="CelebFaces Attributes Dataset (CelebA) is a large-scale face attributes dataset with more than 200K celebrity images, each with 40 attribute annotations. The images in this dataset cover large pose variations and background clutter. CelebA has large diversities, large quantities, and rich annotations, including&#10; - 10,177 number of identities,&#10; - 202,599 number of face images, and&#10; - 5 landmark locations, 40 binary attributes annotations per image.&#10;&#10;The dataset can be employed as the training and test sets for the following computer vision tasks: face attribute recognition, face detection, and landmark (or facial part) localization.&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/celeb_a" />
  <meta itemprop="sameAs" content="http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html" />
</div>

# `celeb_a`

CelebFaces Attributes Dataset (CelebA) is a large-scale face attributes dataset
with more than 200K celebrity images, each with 40 attribute annotations. The
images in this dataset cover large pose variations and background clutter.
CelebA has large diversities, large quantities, and rich annotations,
including - 10,177 number of identities, - 202,599 number of face images, and -
5 landmark locations, 40 binary attributes annotations per image.

The dataset can be employed as the training and test sets for the following
computer vision tasks: face attribute recognition, face detection, and landmark
(or facial part) localization.

*   URL:
    [http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
*   `DatasetBuilder`:
    [`tfds.image.celeba.CelebA`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/celeba.py)
*   Version: `v0.3.0`
*   Size: `1.38 GiB`

## Features
```python
FeaturesDict({
    'attributes': FeaturesDict({
        '5_o_Clock_Shadow': Tensor(shape=(), dtype=tf.bool),
        'Arched_Eyebrows': Tensor(shape=(), dtype=tf.bool),
        'Attractive': Tensor(shape=(), dtype=tf.bool),
        'Bags_Under_Eyes': Tensor(shape=(), dtype=tf.bool),
        'Bald': Tensor(shape=(), dtype=tf.bool),
        'Bangs': Tensor(shape=(), dtype=tf.bool),
        'Big_Lips': Tensor(shape=(), dtype=tf.bool),
        'Big_Nose': Tensor(shape=(), dtype=tf.bool),
        'Black_Hair': Tensor(shape=(), dtype=tf.bool),
        'Blond_Hair': Tensor(shape=(), dtype=tf.bool),
        'Blurry': Tensor(shape=(), dtype=tf.bool),
        'Brown_Hair': Tensor(shape=(), dtype=tf.bool),
        'Bushy_Eyebrows': Tensor(shape=(), dtype=tf.bool),
        'Chubby': Tensor(shape=(), dtype=tf.bool),
        'Double_Chin': Tensor(shape=(), dtype=tf.bool),
        'Eyeglasses': Tensor(shape=(), dtype=tf.bool),
        'Goatee': Tensor(shape=(), dtype=tf.bool),
        'Gray_Hair': Tensor(shape=(), dtype=tf.bool),
        'Heavy_Makeup': Tensor(shape=(), dtype=tf.bool),
        'High_Cheekbones': Tensor(shape=(), dtype=tf.bool),
        'Male': Tensor(shape=(), dtype=tf.bool),
        'Mouth_Slightly_Open': Tensor(shape=(), dtype=tf.bool),
        'Mustache': Tensor(shape=(), dtype=tf.bool),
        'Narrow_Eyes': Tensor(shape=(), dtype=tf.bool),
        'No_Beard': Tensor(shape=(), dtype=tf.bool),
        'Oval_Face': Tensor(shape=(), dtype=tf.bool),
        'Pale_Skin': Tensor(shape=(), dtype=tf.bool),
        'Pointy_Nose': Tensor(shape=(), dtype=tf.bool),
        'Receding_Hairline': Tensor(shape=(), dtype=tf.bool),
        'Rosy_Cheeks': Tensor(shape=(), dtype=tf.bool),
        'Sideburns': Tensor(shape=(), dtype=tf.bool),
        'Smiling': Tensor(shape=(), dtype=tf.bool),
        'Straight_Hair': Tensor(shape=(), dtype=tf.bool),
        'Wavy_Hair': Tensor(shape=(), dtype=tf.bool),
        'Wearing_Earrings': Tensor(shape=(), dtype=tf.bool),
        'Wearing_Hat': Tensor(shape=(), dtype=tf.bool),
        'Wearing_Lipstick': Tensor(shape=(), dtype=tf.bool),
        'Wearing_Necklace': Tensor(shape=(), dtype=tf.bool),
        'Wearing_Necktie': Tensor(shape=(), dtype=tf.bool),
        'Young': Tensor(shape=(), dtype=tf.bool),
    }),
    'image': Image(shape=(218, 178, 3), dtype=tf.uint8),
    'landmarks': FeaturesDict({
        'lefteye_x': Tensor(shape=(), dtype=tf.int64),
        'lefteye_y': Tensor(shape=(), dtype=tf.int64),
        'leftmouth_x': Tensor(shape=(), dtype=tf.int64),
        'leftmouth_y': Tensor(shape=(), dtype=tf.int64),
        'nose_x': Tensor(shape=(), dtype=tf.int64),
        'nose_y': Tensor(shape=(), dtype=tf.int64),
        'righteye_x': Tensor(shape=(), dtype=tf.int64),
        'righteye_y': Tensor(shape=(), dtype=tf.int64),
        'rightmouth_x': Tensor(shape=(), dtype=tf.int64),
        'rightmouth_y': Tensor(shape=(), dtype=tf.int64),
    }),
})
```

## Statistics

Split      | Examples
:--------- | -------:
ALL        | 202,599
TRAIN      | 162,770
TEST       | 19,962
VALIDATION | 19,867

## Urls

*   [http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

## Supervised keys (for `as_supervised=True`)
`None`

## Citation
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

--------------------------------------------------------------------------------
