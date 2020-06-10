<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>

  <meta itemprop="name" content="nyu_depth_v2" />
  <meta itemprop="description" content="The NYU-Depth V2 data set is comprised of video sequences from a variety of&#10;indoor scenes as recorded by both the RGB and Depth cameras from the&#10;Microsoft Kinect.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;nyu_depth_v2&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/nyu_depth_v2-0.0.1.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/nyu_depth_v2" />
  <meta itemprop="sameAs" content="https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html" />
  <meta itemprop="citation" content="@inproceedings{Silberman:ECCV12,&#10;  author    = {Nathan Silberman, Derek Hoiem, Pushmeet Kohli and Rob Fergus},&#10;  title     = {Indoor Segmentation and Support Inference from RGBD Images},&#10;  booktitle = {ECCV},&#10;  year      = {2012}&#10;}&#10;@inproceedings{icra_2019_fastdepth,&#10;  author    = {Wofk, Diana and Ma, Fangchang and Yang, Tien-Ju and Karaman, Sertac and Sze, Vivienne},&#10;  title     = {FastDepth: Fast Monocular Depth Estimation on Embedded Systems},&#10;  booktitle = {IEEE International Conference on Robotics and Automation (ICRA)},&#10;  year      = {2019}&#10;}" />
</div>

# `nyu_depth_v2`

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

The NYU-Depth V2 data set is comprised of video sequences from a variety of
indoor scenes as recorded by both the RGB and Depth cameras from the Microsoft
Kinect.

*   **Homepage**:
    [https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html)
*   **Source code**:
    [`tfds.image.nyu_depth_v2.NyuDepthV2`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/image/nyu_depth_v2.py)
*   **Versions**:
    *   **`0.0.1`** (default): No release notes.
*   **Download size**: `31.92 GiB`
*   **Dataset size**: `74.03 GiB`
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Splits**:

Split        | Examples
:----------- | -------:
'train'      | 47,584
'validation' | 654

*   **Features**:

```python
FeaturesDict({
    'depth': Tensor(shape=(480, 640), dtype=tf.float16),
    'image': Image(shape=(480, 640, 3), dtype=tf.uint8),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('image', 'depth')`
*   **Citation**:

```
@inproceedings{Silberman:ECCV12,
  author    = {Nathan Silberman, Derek Hoiem, Pushmeet Kohli and Rob Fergus},
  title     = {Indoor Segmentation and Support Inference from RGBD Images},
  booktitle = {ECCV},
  year      = {2012}
}
@inproceedings{icra_2019_fastdepth,
  author    = {Wofk, Diana and Ma, Fangchang and Yang, Tien-Ju and Karaman, Sertac and Sze, Vivienne},
  title     = {FastDepth: Fast Monocular Depth Estimation on Embedded Systems},
  booktitle = {IEEE International Conference on Robotics and Automation (ICRA)},
  year      = {2019}
}
```

*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:

<img src="https://storage.googleapis.com/tfds-data/visualization/nyu_depth_v2-0.0.1.png" alt="Visualization" width="500px">
