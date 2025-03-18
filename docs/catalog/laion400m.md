<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="laion400m" />
  <meta itemprop="description" content="The LAION-400M dataset is completely openly, freely accessible.&#10;&#10;Check&#10;[https://laion.ai/laion-400-open-dataset/](https://laion.ai/laion-400-open-dataset/)&#10;for the full description of this dataset.&#10;&#10;All images and texts in the LAION-400M dataset have been filtered with OpenAI‘s&#10;CLIP by calculating the cosine similarity between the text and image embeddings&#10;and dropping those with a similarity below 0.3. The threshold of 0.3 had been&#10;determined through human evaluations and seemed to be a good heuristic for&#10;estimating semantic image-text-content matching.&#10;&#10;The image-text-pairs have been extracted from the Common Crawl web data dump and&#10;are from random web pages crawled between 2014 and 2021.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;laion400m&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/laion400m" />
  <meta itemprop="sameAs" content="https://laion.ai/blog/laion-400-open-dataset/" />
  <meta itemprop="citation" content="@article{DBLP:journals/corr/abs-2111-02114,&#10;  author    = {Christoph Schuhmann and&#10;               Richard Vencu and&#10;               Romain Beaumont and&#10;               Robert Kaczmarczyk and&#10;               Clayton Mullis and&#10;               Aarush Katta and&#10;               Theo Coombes and&#10;               Jenia Jitsev and&#10;               Aran Komatsuzaki},&#10;  title     = {{LAION-400M:} Open Dataset of CLIP-Filtered 400 Million Image-Text&#10;               Pairs},&#10;  journal   = {CoRR},&#10;  volume    = {abs/2111.02114},&#10;  year      = {2021},&#10;  url       = {https://arxiv.org/abs/2111.02114},&#10;  eprinttype = {arXiv},&#10;  eprint    = {2111.02114},&#10;  timestamp = {Fri, 05 Nov 2021 15:25:54 +0100},&#10;  biburl    = {https://dblp.org/rec/journals/corr/abs-2111-02114.bib},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `laion400m`


Warning: Manual download required. See instructions below.

*   **Description**:

The LAION-400M dataset is completely openly, freely accessible.

Check
[https://laion.ai/laion-400-open-dataset/](https://laion.ai/laion-400-open-dataset/)
for the full description of this dataset.

All images and texts in the LAION-400M dataset have been filtered with OpenAI‘s
CLIP by calculating the cosine similarity between the text and image embeddings
and dropping those with a similarity below 0.3. The threshold of 0.3 had been
determined through human evaluations and seemed to be a good heuristic for
estimating semantic image-text-content matching.

The image-text-pairs have been extracted from the Common Crawl web data dump and
are from random web pages crawled between 2014 and 2021.

*   **Additional Documentation**:
    <a class="button button-with-icon" href="https://paperswithcode.com/dataset/laion-400m">
    Explore on Papers With Code
    <span class="material-icons icon-after" aria-hidden="true"> north_east
    </span> </a>

*   **Homepage**:
    [https://laion.ai/blog/laion-400-open-dataset/](https://laion.ai/blog/laion-400-open-dataset/)

*   **Source code**:
    [`tfds.vision_language.laion400m.Laion400m`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/vision_language/laion400m/laion400m.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Manual download instructions**: This dataset requires you to
    download the source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
    Refer to "Download Information" section on https://laion.ai/blog/laion-400-open-dataset/

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{DBLP:journals/corr/abs-2111-02114,
  author    = {Christoph Schuhmann and
               Richard Vencu and
               Romain Beaumont and
               Robert Kaczmarczyk and
               Clayton Mullis and
               Aarush Katta and
               Theo Coombes and
               Jenia Jitsev and
               Aran Komatsuzaki},
  title     = {{LAION-400M:} Open Dataset of CLIP-Filtered 400 Million Image-Text
               Pairs},
  journal   = {CoRR},
  volume    = {abs/2111.02114},
  year      = {2021},
  url       = {https://arxiv.org/abs/2111.02114},
  eprinttype = {arXiv},
  eprint    = {2111.02114},
  timestamp = {Fri, 05 Nov 2021 15:25:54 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2111-02114.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


## laion400m/images (default config)

*   **Feature structure**:

```python
FeaturesDict({
    'caption': Text(shape=(), dtype=string),
    'image': Image(shape=(None, None, 3), dtype=uint8, description=image),
    'license': Text(shape=(), dtype=string),
    'nsfw': ClassLabel(shape=(), dtype=int64, num_classes=4),
    'original_height': Scalar(shape=(), dtype=int32, description=original height of the image),
    'original_width': Scalar(shape=(), dtype=int32, description=original width of the image),
    'similarity': Scalar(shape=(), dtype=float64, description=cosine similarity score between the text and image embedding. Missing values default to -1.0),
    'url': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

| Feature         | Class        | Shape  | Dtype   | Description | Value      |
:                 :              :        :         :             : range      :
| :-------------- | :----------- | :----- | :------ | :---------- | :--------- |
|                 | FeaturesDict |        |         |             |            |
| caption         | Text         |        | string  | HTML        |            |
:                 :              :        :         : alt-text    :            :
:                 :              :        :         : attribute   :            :
| image           | Image        | (None, | uint8   | image       |            |
:                 :              : None,  :         :             :            :
:                 :              : 3)     :         :             :            :
| license         | Text         |        | string  | type of     |            |
:                 :              :        :         : Creative    :            :
:                 :              :        :         : Commons     :            :
:                 :              :        :         : license (if :            :
:                 :              :        :         : applicable) :            :
| nsfw            | ClassLabel   |        | int64   | NSFW tag    |            |
:                 :              :        :         : (detected   :            :
:                 :              :        :         : with CLIP). :            :
:                 :              :        :         : Incohesive  :            :
:                 :              :        :         : and missing :            :
:                 :              :        :         : tags are    :            :
:                 :              :        :         : replaced    :            :
:                 :              :        :         : with        :            :
:                 :              :        :         : UNTAGGED    :            :
| original_height | Scalar       |        | int32   | original    |            |
:                 :              :        :         : height of   :            :
:                 :              :        :         : the image   :            :
| original_width  | Scalar       |        | int32   | original    |            |
:                 :              :        :         : width of    :            :
:                 :              :        :         : the image   :            :
| similarity      | Scalar       |        | float64 | cosine      | [0.0, 1.0] |
:                 :              :        :         : similarity  :            :
:                 :              :        :         : score       :            :
:                 :              :        :         : between the :            :
:                 :              :        :         : text and    :            :
:                 :              :        :         : image       :            :
:                 :              :        :         : embedding.  :            :
:                 :              :        :         : Missing     :            :
:                 :              :        :         : values      :            :
:                 :              :        :         : default to  :            :
:                 :              :        :         : -1.0        :            :
| url             | Text         |        | string  | image URL   |            |

## laion400m/embeddings

*   **Feature structure**:

```python
FeaturesDict({
    'caption': Text(shape=(), dtype=string),
    'image_embedding': Tensor(shape=(512,), dtype=float16, description=CLIP image embedding),
    'license': Text(shape=(), dtype=string),
    'nsfw': ClassLabel(shape=(), dtype=int64, num_classes=4),
    'original_height': Scalar(shape=(), dtype=int32, description=original height of the image),
    'original_width': Scalar(shape=(), dtype=int32, description=original width of the image),
    'similarity': Scalar(shape=(), dtype=float64, description=cosine similarity score between the text and image embedding. Missing values default to -1.0),
    'text_embedding': Tensor(shape=(512,), dtype=float16, description=CLIP text embedding),
    'url': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

| Feature         | Class        | Shape  | Dtype   | Description | Value      |
:                 :              :        :         :             : range      :
| :-------------- | :----------- | :----- | :------ | :---------- | :--------- |
|                 | FeaturesDict |        |         |             |            |
| caption         | Text         |        | string  | HTML        |            |
:                 :              :        :         : alt-text    :            :
:                 :              :        :         : attribute   :            :
| image_embedding | Tensor       | (512,) | float16 | CLIP image  |            |
:                 :              :        :         : embedding   :            :
| license         | Text         |        | string  | type of     |            |
:                 :              :        :         : Creative    :            :
:                 :              :        :         : Commons     :            :
:                 :              :        :         : license (if :            :
:                 :              :        :         : applicable) :            :
| nsfw            | ClassLabel   |        | int64   | NSFW tag    |            |
:                 :              :        :         : (detected   :            :
:                 :              :        :         : with CLIP). :            :
:                 :              :        :         : Incohesive  :            :
:                 :              :        :         : and missing :            :
:                 :              :        :         : tags are    :            :
:                 :              :        :         : replaced    :            :
:                 :              :        :         : with        :            :
:                 :              :        :         : UNTAGGED    :            :
| original_height | Scalar       |        | int32   | original    |            |
:                 :              :        :         : height of   :            :
:                 :              :        :         : the image   :            :
| original_width  | Scalar       |        | int32   | original    |            |
:                 :              :        :         : width of    :            :
:                 :              :        :         : the image   :            :
| similarity      | Scalar       |        | float64 | cosine      | [0.0, 1.0] |
:                 :              :        :         : similarity  :            :
:                 :              :        :         : score       :            :
:                 :              :        :         : between the :            :
:                 :              :        :         : text and    :            :
:                 :              :        :         : image       :            :
:                 :              :        :         : embedding.  :            :
:                 :              :        :         : Missing     :            :
:                 :              :        :         : values      :            :
:                 :              :        :         : default to  :            :
:                 :              :        :         : -1.0        :            :
| text_embedding  | Tensor       | (512,) | float16 | CLIP text   |            |
:                 :              :        :         : embedding   :            :
| url             | Text         |        | string  | image URL   |            |
