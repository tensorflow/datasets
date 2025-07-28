<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="covr" />
  <meta itemprop="description" content="[COVR](https://covr-dataset.github.io/) dataset with [imSitu](https://github.com/my89/imSitu) and [Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/index.html) images.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;covr&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/covr" />
  <meta itemprop="sameAs" content="https://covr-dataset.github.io/" />
  <meta itemprop="citation" content="@inproceedings{bogin-etal-2021-covr,&#10;    title = &quot;{COVR}: A Test-Bed for Visually Grounded Compositional Generalization with Real Images&quot;,&#10;    author = &quot;Bogin, Ben  and&#10;      Gupta, Shivanshu  and&#10;      Gardner, Matt  and&#10;      Berant, Jonathan&quot;,&#10;    editor = &quot;Moens, Marie-Francine  and&#10;      Huang, Xuanjing  and&#10;      Specia, Lucia  and&#10;      Yih, Scott Wen-tau&quot;,&#10;    booktitle = &quot;Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing&quot;,&#10;    month = nov,&#10;    year = &quot;2021&quot;,&#10;    address = &quot;Online and Punta Cana, Dominican Republic&quot;,&#10;    publisher = &quot;Association for Computational Linguistics&quot;,&#10;    url = &quot;https://aclanthology.org/2021.emnlp-main.774/&quot;,&#10;    doi = &quot;10.18653/v1/2021.emnlp-main.774&quot;,&#10;    pages = &quot;9824--9846&quot;,&#10;    abstract = &quot;While interest in models that generalize at test time to new compositions has risen in recent years, benchmarks in the visually-grounded domain have thus far been restricted to synthetic images. In this work, we propose COVR, a new test-bed for visually-grounded compositional generalization with real images. To create COVR, we use real images annotated with scene graphs, and propose an almost fully automatic procedure for generating question-answer pairs along with a set of context images. COVR focuses on questions that require complex reasoning, including higher-order operations such as quantification and aggregation. Due to the automatic generation process, COVR facilitates the creation of compositional splits, where models at test time need to generalize to new concepts and compositions in a zero- or few-shot setting. We construct compositional splits using COVR and demonstrate a myriad of cases where state-of-the-art pre-trained language-and-vision models struggle to compositionally generalize.&quot;&#10;}&#10;&#10;@inproceedings{yatskar2016,&#10;  title={Situation Recognition: Visual Semantic Role Labeling for Image Understanding},&#10;  author={Yatskar, Mark and Zettlemoyer, Luke and Farhadi, Ali},&#10;  booktitle={Conference on Computer Vision and Pattern Recognition},&#10;  year={2016}&#10;}&#10;&#10;@article{cite-key,&#10;  abstract = {Despite progress in perceptual tasks such as image classification, computers still perform poorly on cognitive tasks such as image description and question answering. Cognition is core to tasks that involve not just recognizing, but reasoning about our visual world. However, models used to tackle the rich content in images for cognitive tasks are still being trained using the same datasets designed for perceptual tasks. To achieve success at cognitive tasks, models need to understand the interactions and relationships between objects in an image. When asked ``What vehicle is the person riding?&#x27;&#x27;, computers will need to identify the objects in an image as well as the relationships riding(man, carriage) and pulling(horse, carriage) to answer correctly that ``the person is riding a horse-drawn carriage.&#x27;&#x27;In this paper, we present the Visual Genome dataset to enable the modeling of such relationships. We collect dense annotations of objects, attributes, and relationships within each image to learn these models. Specifically, our dataset contains over 108K images where each image has an average of {\$}{\$}35{\$}{\$}objects, {\$}{\$}26{\$}{\$}attributes, and {\$}{\$}21{\$}{\$}pairwise relationships between objects. We canonicalize the objects, attributes, relationships, and noun phrases in region descriptions and questions answer pairs to WordNet synsets. Together, these annotations represent the densest and largest dataset of image descriptions, objects, attributes, relationships, and question answer pairs.},&#10;  author = {Krishna, Ranjay and Zhu, Yuke and Groth, Oliver and Johnson, Justin and Hata, Kenji and Kravitz, Joshua and Chen, Stephanie and Kalantidis, Yannis and Li, Li-Jia and Shamma, David A. and Bernstein, Michael S. and Fei-Fei, Li},&#10;   date = {2017/05/01},&#10;   date-added = {2025-07-10 08:32:03 -0700},&#10;  date-modified = {2025-07-10 08:32:03 -0700},&#10;   doi = {10.1007/s11263-016-0981-7},&#10; id = {Krishna2017},&#10;    isbn = {1573-1405},&#10;    journal = {International Journal of Computer Vision},&#10;  number = {1},&#10;  pages = {32--73},&#10;  title = {Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations},&#10;    url = {https://doi.org/10.1007/s11263-016-0981-7},&#10; volume = {123},&#10;    year = {2017},&#10; bdsk-url-1 = {https://doi.org/10.1007/s11263-016-0981-7}}" />
</div>

# `covr`


Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

*   **Description**:

[COVR](https://covr-dataset.github.io/) dataset with
[imSitu](https://github.com/my89/imSitu) and
[Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/index.html)
images.

*   **Homepage**:
    [https://covr-dataset.github.io/](https://covr-dataset.github.io/)

*   **Source code**:
    [`tfds.datasets.covr.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/covr/covr_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `48.35 GiB`

*   **Dataset size**: `173.96 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 7,024
`'train'`      | 248,154
`'validation'` | 6,891

*   **Feature structure**:

```python
FeaturesDict({
    'images': Sequence(Image(shape=(None, None, 3), dtype=uint8)),
    'label': Text(shape=(), dtype=string),
    'pattern_name': Text(shape=(), dtype=string),
    'program': Text(shape=(), dtype=string),
    'properties': Sequence(Text(shape=(), dtype=string)),
    'scenes': Sequence(Text(shape=(), dtype=string)),
    'utterance': Text(shape=(), dtype=string),
})
```

*   **Feature documentation**:

Feature      | Class           | Shape                 | Dtype  | Description
:----------- | :-------------- | :-------------------- | :----- | :----------
             | FeaturesDict    |                       |        |
images       | Sequence(Image) | (None, None, None, 3) | uint8  |
label        | Text            |                       | string |
pattern_name | Text            |                       | string |
program      | Text            |                       | string |
properties   | Sequence(Text)  | (None,)               | string |
scenes       | Sequence(Text)  | (None,)               | string |
utterance    | Text            |                       | string |

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
@inproceedings{bogin-etal-2021-covr,
    title = "{COVR}: A Test-Bed for Visually Grounded Compositional Generalization with Real Images",
    author = "Bogin, Ben  and
      Gupta, Shivanshu  and
      Gardner, Matt  and
      Berant, Jonathan",
    editor = "Moens, Marie-Francine  and
      Huang, Xuanjing  and
      Specia, Lucia  and
      Yih, Scott Wen-tau",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.774/",
    doi = "10.18653/v1/2021.emnlp-main.774",
    pages = "9824--9846",
    abstract = "While interest in models that generalize at test time to new compositions has risen in recent years, benchmarks in the visually-grounded domain have thus far been restricted to synthetic images. In this work, we propose COVR, a new test-bed for visually-grounded compositional generalization with real images. To create COVR, we use real images annotated with scene graphs, and propose an almost fully automatic procedure for generating question-answer pairs along with a set of context images. COVR focuses on questions that require complex reasoning, including higher-order operations such as quantification and aggregation. Due to the automatic generation process, COVR facilitates the creation of compositional splits, where models at test time need to generalize to new concepts and compositions in a zero- or few-shot setting. We construct compositional splits using COVR and demonstrate a myriad of cases where state-of-the-art pre-trained language-and-vision models struggle to compositionally generalize."
}

@inproceedings{yatskar2016,
  title={Situation Recognition: Visual Semantic Role Labeling for Image Understanding},
  author={Yatskar, Mark and Zettlemoyer, Luke and Farhadi, Ali},
  booktitle={Conference on Computer Vision and Pattern Recognition},
  year={2016}
}

@article{cite-key,
    abstract = {Despite progress in perceptual tasks such as image classification, computers still perform poorly on cognitive tasks such as image description and question answering. Cognition is core to tasks that involve not just recognizing, but reasoning about our visual world. However, models used to tackle the rich content in images for cognitive tasks are still being trained using the same datasets designed for perceptual tasks. To achieve success at cognitive tasks, models need to understand the interactions and relationships between objects in an image. When asked ``What vehicle is the person riding?'', computers will need to identify the objects in an image as well as the relationships riding(man, carriage) and pulling(horse, carriage) to answer correctly that ``the person is riding a horse-drawn carriage.''In this paper, we present the Visual Genome dataset to enable the modeling of such relationships. We collect dense annotations of objects, attributes, and relationships within each image to learn these models. Specifically, our dataset contains over 108K images where each image has an average of {\$}{\$}35{\$}{\$}objects, {\$}{\$}26{\$}{\$}attributes, and {\$}{\$}21{\$}{\$}pairwise relationships between objects. We canonicalize the objects, attributes, relationships, and noun phrases in region descriptions and questions answer pairs to WordNet synsets. Together, these annotations represent the densest and largest dataset of image descriptions, objects, attributes, relationships, and question answer pairs.},
    author = {Krishna, Ranjay and Zhu, Yuke and Groth, Oliver and Johnson, Justin and Hata, Kenji and Kravitz, Joshua and Chen, Stephanie and Kalantidis, Yannis and Li, Li-Jia and Shamma, David A. and Bernstein, Michael S. and Fei-Fei, Li},
    date = {2017/05/01},
    date-added = {2025-07-10 08:32:03 -0700},
    date-modified = {2025-07-10 08:32:03 -0700},
    doi = {10.1007/s11263-016-0981-7},
    id = {Krishna2017},
    isbn = {1573-1405},
    journal = {International Journal of Computer Vision},
    number = {1},
    pages = {32--73},
    title = {Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations},
    url = {https://doi.org/10.1007/s11263-016-0981-7},
    volume = {123},
    year = {2017},
    bdsk-url-1 = {https://doi.org/10.1007/s11263-016-0981-7}}
```

