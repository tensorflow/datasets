<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="kitti" />
  <meta itemprop="description" content="Kitti contains a suite of vision tasks built using an autonomous driving&#10;platform. The full benchmark contains many tasks such as stereo, optical flow,&#10;visual odometry, etc. This dataset contains the object detection dataset,&#10;including the monocular images and bounding boxes. The dataset contains 7481&#10;training images annotated with 3D bounding boxes. A full description of the&#10;annotations can be found in the readme of the object development kit readme on&#10;the Kitti homepage.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;kitti&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/kitti-3.3.0.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/kitti" />
  <meta itemprop="sameAs" content="http://www.cvlibs.net/datasets/kitti/" />
  <meta itemprop="citation" content="@inproceedings{Geiger2012CVPR,&#10;  author = {Andreas Geiger and Philip Lenz and Raquel Urtasun},&#10;  title = {Are we ready for Autonomous Driving? The KITTI Vision Benchmark Suite},&#10;  booktitle = {Conference on Computer Vision and Pattern Recognition (CVPR)},&#10;  year = {2012}&#10;}" />
</div>

# `kitti`


*   **Description**:

Kitti contains a suite of vision tasks built using an autonomous driving
platform. The full benchmark contains many tasks such as stereo, optical flow,
visual odometry, etc. This dataset contains the object detection dataset,
including the monocular images and bounding boxes. The dataset contains 7481
training images annotated with 3D bounding boxes. A full description of the
annotations can be found in the readme of the object development kit readme on
the Kitti homepage.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/kitti">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [http://www.cvlibs.net/datasets/kitti/](http://www.cvlibs.net/datasets/kitti/)

*   **Source code**:
    [`tfds.datasets.kitti.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/kitti/kitti_dataset_builder.py)

*   **Versions**:

    *   `3.1.0`: No release notes.
    *   `3.2.0`: Devkit updated.
    *   **`3.3.0`** (default): Added labels for the `occluded` feature.

*   **Download size**: `11.71 GiB`

*   **Dataset size**: `5.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 711
`'train'`      | 6,347
`'validation'` | 423

*   **Feature structure**:

```python
FeaturesDict({
    'image': Image(shape=(None, None, 3), dtype=uint8),
    'image/file_name': Text(shape=(), dtype=string),
    'objects': Sequence({
        'alpha': float32,
        'bbox': BBoxFeature(shape=(4,), dtype=float32, description=2D bounding box of object in the image),
        'dimensions': Tensor(shape=(3,), dtype=float32, description=3D object dimensions: height, width, length (in meters)),
        'location': Tensor(shape=(3,), dtype=float32, description=3D object location x,y,z in camera coordinates (in meters)),
        'occluded': ClassLabel(shape=(), dtype=int64, num_classes=4),
        'rotation_y': float32,
        'truncated': float32,
        'type': ClassLabel(shape=(), dtype=int64, num_classes=8),
    }),
})
```

*   **Feature documentation**:

| Feature            | Class        | Shape        | Dtype   | Description     |
| :----------------- | :----------- | :----------- | :------ | :-------------- |
|                    | FeaturesDict |              |         |                 |
| image              | Image        | (None, None, | uint8   |                 |
:                    :              : 3)           :         :                 :
| image/file_name    | Text         |              | string  |                 |
| objects            | Sequence     |              |         |                 |
| objects/alpha      | Tensor       |              | float32 | Observation     |
:                    :              :              :         : angle of        :
:                    :              :              :         : object, ranging :
:                    :              :              :         : [-pi..pi]       :
| objects/bbox       | BBoxFeature  | (4,)         | float32 | 2D bounding box |
:                    :              :              :         : of object in    :
:                    :              :              :         : the image       :
| objects/dimensions | Tensor       | (3,)         | float32 | 3D object       |
:                    :              :              :         : dimensions\:    :
:                    :              :              :         : height, width,  :
:                    :              :              :         : length (in      :
:                    :              :              :         : meters)         :
| objects/location   | Tensor       | (3,)         | float32 | 3D object       |
:                    :              :              :         : location x,y,z  :
:                    :              :              :         : in camera       :
:                    :              :              :         : coordinates (in :
:                    :              :              :         : meters)         :
| objects/occluded   | ClassLabel   |              | int64   | Integer         |
:                    :              :              :         : (0,1,2,3)       :
:                    :              :              :         : indicating      :
:                    :              :              :         : occlusion       :
:                    :              :              :         : state\: 0 =     :
:                    :              :              :         : fully visible,  :
:                    :              :              :         : 1 = partly      :
:                    :              :              :         : occluded2 =     :
:                    :              :              :         : largely         :
:                    :              :              :         : occluded, 3 =   :
:                    :              :              :         : unknown         :
| objects/rotation_y | Tensor       |              | float32 | Rotation ry     |
:                    :              :              :         : around Y-axis   :
:                    :              :              :         : in camera       :
:                    :              :              :         : coordinates     :
:                    :              :              :         : [-pi..pi]       :
| objects/truncated  | Tensor       |              | float32 | Float from 0    |
:                    :              :              :         : (non-truncated) :
:                    :              :              :         : to 1            :
:                    :              :              :         : (truncated),    :
:                    :              :              :         : wheretruncated  :
:                    :              :              :         : refers to the   :
:                    :              :              :         : object leaving  :
:                    :              :              :         : image           :
:                    :              :              :         : boundaries      :
| objects/type       | ClassLabel   |              | int64   | The type of     |
:                    :              :              :         : object, e.g.    :
:                    :              :              :         : 'Car' or 'Van'  :

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/kitti-3.3.0.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/kitti-3.3.0.html";
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
@inproceedings{Geiger2012CVPR,
  author = {Andreas Geiger and Philip Lenz and Raquel Urtasun},
  title = {Are we ready for Autonomous Driving? The KITTI Vision Benchmark Suite},
  booktitle = {Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2012}
}
```

