<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="gem" />
  <meta itemprop="description" content="**GEM** is a benchmark environment for Natural Language Generation with a focus&#10;on its Evaluation, both through human annotations and automated Metrics.&#10;&#10;GEM aims to: (1) measure NLG progress across 13 datasets spanning many NLG&#10;tasks and languages. (2) provide an in-depth analysis of data and models&#10;presented via data statements and challenge sets. (3) develop standards for&#10;evaluation of generated text using both automated and human metrics.&#10;&#10;More information can be found at&#10;[https://gem-benchmark.com](https://gem-benchmark.com).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;gem&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/gem" />
  <meta itemprop="sameAs" content="https://gem-benchmark.com" />
  <meta itemprop="citation" content="@inproceedings{lin2020commongen,&#10;  title = &quot;CommonGen: A Constrained Text Generation Challenge for Generative Commonsense Reasoning&quot;,&#10;  author = &quot;Lin, Bill Yuchen  and&#10;    Zhou, Wangchunshu  and&#10;    Shen, Ming  and&#10;    Zhou, Pei  and&#10;    Bhagavatula, Chandra  and&#10;    Choi, Yejin  and&#10;    Ren, Xiang&quot;,&#10;  booktitle = &quot;Findings of the Association for Computational Linguistics: EMNLP 2020&quot;,&#10;  month = nov,&#10;  year = &quot;2020&quot;,&#10;  address = &quot;Online&quot;,&#10;  publisher = &quot;Association for Computational Linguistics&quot;,&#10;  url = &quot;https://www.aclweb.org/anthology/2020.findings-emnlp.165&quot;,&#10;  pages = &quot;1823--1840&quot;,&#10;}&#10;@article{gehrmann2021gem,&#10;  author    = {Sebastian Gehrmann and&#10;               Tosin P. Adewumi and&#10;               Karmanya Aggarwal and&#10;               Pawan Sasanka Ammanamanchi and&#10;               Aremu Anuoluwapo and&#10;               Antoine Bosselut and&#10;               Khyathi Raghavi Chandu and&#10;               Miruna{-}Adriana Clinciu and&#10;               Dipanjan Das and&#10;               Kaustubh D. Dhole and&#10;               Wanyu Du and&#10;               Esin Durmus and&#10;               Ondrej Dusek and&#10;               Chris Emezue and&#10;               Varun Gangal and&#10;               Cristina Garbacea and&#10;               Tatsunori Hashimoto and&#10;               Yufang Hou and&#10;               Yacine Jernite and&#10;               Harsh Jhamtani and&#10;               Yangfeng Ji and&#10;               Shailza Jolly and&#10;               Dhruv Kumar and&#10;               Faisal Ladhak and&#10;               Aman Madaan and&#10;               Mounica Maddela and&#10;               Khyati Mahajan and&#10;               Saad Mahamood and&#10;               Bodhisattwa Prasad Majumder and&#10;               Pedro Henrique Martins and&#10;               Angelina McMillan{-}Major and&#10;               Simon Mille and&#10;               Emiel van Miltenburg and&#10;               Moin Nadeem and&#10;               Shashi Narayan and&#10;               Vitaly Nikolaev and&#10;               Rubungo Andre Niyongabo and&#10;               Salomey Osei and&#10;               Ankur P. Parikh and&#10;               Laura Perez{-}Beltrachini and&#10;               Niranjan Ramesh Rao and&#10;               Vikas Raunak and&#10;               Juan Diego Rodriguez and&#10;               Sashank Santhanam and&#10;               Jo{\~{a}}o Sedoc and&#10;               Thibault Sellam and&#10;               Samira Shaikh and&#10;               Anastasia Shimorina and&#10;               Marco Antonio Sobrevilla Cabezudo and&#10;               Hendrik Strobelt and&#10;               Nishant Subramani and&#10;               Wei Xu and&#10;               Diyi Yang and&#10;               Akhila Yerukola and&#10;               Jiawei Zhou},&#10;  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and&#10;               Metrics},&#10;  journal   = {CoRR},&#10;  volume    = {abs/2102.01672},&#10;  year      = {2021},&#10;  url       = {https://arxiv.org/abs/2102.01672},&#10;  archivePrefix = {arXiv},&#10;  eprint    = {2102.01672}&#10;}&#10;&#10;Note that each GEM dataset has its own citation. Please see the source to see&#10;the correct citation for each contained dataset.&quot;" />
</div>

# `gem`


*   **Description**:

**GEM** is a benchmark environment for Natural Language Generation with a focus
on its Evaluation, both through human annotations and automated Metrics.

GEM aims to: (1) measure NLG progress across 13 datasets spanning many NLG tasks
and languages. (2) provide an in-depth analysis of data and models presented via
data statements and challenge sets. (3) develop standards for evaluation of
generated text using both automated and human metrics.

More information can be found at
[https://gem-benchmark.com](https://gem-benchmark.com).

*   **Homepage**: [https://gem-benchmark.com](https://gem-benchmark.com)

*   **Source code**:
    [`tfds.text.gem.Gem`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/text/gem/gem.py)

*   **Versions**:

    *   `1.0.0`: Initial version
    *   `1.0.1`: Update bad links filter for MLSum
    *   **`1.1.0`** (default): Release of the Challenge Sets

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

## gem/common_gen (default config)

*   **Config description**: CommonGen is a constrained text generation task,
    associated with a benchmark dataset, to explicitly test machines for the
    ability of generative commonsense reasoning. Given a set of common concepts;
    the task is to generate a coherent sentence describing an everyday scenario
    using these concepts.

*   **Download size**: `1.84 MiB`

*   **Dataset size**: `16.84 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split                           | Examples
:------------------------------ | -------:
`'challenge_test_scramble'`     | 500
`'challenge_train_sample'`      | 500
`'challenge_validation_sample'` | 500
`'test'`                        | 1,497
`'train'`                       | 67,389
`'validation'`                  | 993

*   **Features**:

```python
FeaturesDict({
    'concept_set_id': tf.int32,
    'concepts': Sequence(tf.string),
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-common_gen-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{lin2020commongen,
  title = "CommonGen: A Constrained Text Generation Challenge for Generative Commonsense Reasoning",
  author = "Lin, Bill Yuchen  and
    Zhou, Wangchunshu  and
    Shen, Ming  and
    Zhou, Pei  and
    Bhagavatula, Chandra  and
    Choi, Yejin  and
    Ren, Xiang",
  booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
  month = nov,
  year = "2020",
  address = "Online",
  publisher = "Association for Computational Linguistics",
  url = "https://www.aclweb.org/anthology/2020.findings-emnlp.165",
  pages = "1823--1840",
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/cs_restaurants

*   **Config description**: The task is generating responses in the context of a
    (hypothetical) dialogue system that provides information about restaurants.
    The input is a basic intent/dialogue act type and a list of slots
    (attributes) and their values. The output is a natural language sentence.

*   **Download size**: `1.46 MiB`

*   **Dataset size**: `2.71 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split                           | Examples
:------------------------------ | -------:
`'challenge_test_scramble'`     | 500
`'challenge_train_sample'`      | 500
`'challenge_validation_sample'` | 500
`'test'`                        | 842
`'train'`                       | 3,569
`'validation'`                  | 781

*   **Features**:

```python
FeaturesDict({
    'dialog_act': tf.string,
    'dialog_act_delexicalized': tf.string,
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
    'target_delexicalized': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-cs_restaurants-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{cs_restaurants,
  address = {Tokyo, Japan},
  title = {Neural {Generation} for {Czech}: {Data} and {Baselines}},
  shorttitle = {Neural {Generation} for {Czech}},
  url = {https://www.aclweb.org/anthology/W19-8670/},
  urldate = {2019-10-18},
  booktitle = {Proceedings of the 12th {International} {Conference} on {Natural} {Language} {Generation} ({INLG} 2019)},
  author = {Dušek, Ondřej and Jurčíček, Filip},
  month = oct,
  year = {2019},
  pages = {563--574}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/dart

*   **Config description**: DART is a large and open-domain structured DAta
    Record to Text generation corpus with high-quality sentence annotations with
    each input being a set of entity-relation triples following a
    tree-structured ontology.

*   **Download size**: `28.01 MiB`

*   **Dataset size**: `33.78 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 6,959
`'train'`      | 62,659
`'validation'` | 2,768

*   **Features**:

```python
FeaturesDict({
    'dart_id': tf.int32,
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'subtree_was_extended': tf.bool,
    'target': tf.string,
    'target_sources': Sequence(tf.string),
    'tripleset': Sequence(tf.string),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-dart-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@article{radev2020dart,
  title=Dart: Open-domain structured data record to text generation,
  author={Radev, Dragomir and Zhang, Rui and Rau, Amrit and Sivaprasad, Abhinand and Hsieh, Chiachun and Rajani, Nazneen Fatema and Tang, Xiangru and Vyas, Aadit and Verma, Neha and Krishna, Pranav and others},
  journal={arXiv preprint arXiv:2007.02871},
  year={2020}
}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/e2e_nlg

*   **Config description**: The E2E dataset is designed for a limited-domain
    data-to-text task -- generation of restaurant descriptions/recommendations
    based on up to 8 different attributes (name, area, price range etc.)

*   **Download size**: `13.99 MiB`

*   **Dataset size**: `16.92 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split                           | Examples
:------------------------------ | -------:
`'challenge_test_scramble'`     | 500
`'challenge_train_sample'`      | 500
`'challenge_validation_sample'` | 500
`'test'`                        | 4,693
`'train'`                       | 33,525
`'validation'`                  | 4,299

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'meaning_representation': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-e2e_nlg-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{e2e_cleaned,
  address = {Tokyo, Japan},
  title = {Semantic {Noise} {Matters} for {Neural} {Natural} {Language} {Generation}},
  url = {https://www.aclweb.org/anthology/W19-8652/},
  booktitle = {Proceedings of the 12th {International} {Conference} on {Natural} {Language} {Generation} ({INLG} 2019)},
  author = {Dušek, Ondřej and Howcroft, David M and Rieser, Verena},
  year = {2019},
  pages = {421--426},
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/mlsum_de

*   **Config description**: MLSum is a large-scale multiLingual summarization
    dataset. It is buillt from online news outlets, this split focusing on
    German.

*   **Download size**: `345.98 MiB`

*   **Dataset size**: `963.60 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split                           | Examples
:------------------------------ | -------:
`'challenge_test_covid'`        | 5,058
`'challenge_train_sample'`      | 500
`'challenge_validation_sample'` | 500
`'test'`                        | 10,695
`'train'`                       | 220,748
`'validation'`                  | 11,392

*   **Features**:

```python
FeaturesDict({
    'date': tf.string,
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
    'text': tf.string,
    'title': tf.string,
    'topic': tf.string,
    'url': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-mlsum_de-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{scialom-etal-2020-mlsum,
    title = "{MLSUM}: The Multilingual Summarization Corpus",
    author = {Scialom, Thomas  and Dray, Paul-Alexis  and Lamprier, Sylvain  and Piwowarski, Benjamin  and Staiano, Jacopo},
    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
    year = {2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/mlsum_es

*   **Config description**: MLSum is a large-scale multiLingual summarization
    dataset. It is buillt from online news outlets, this split focusing on
    Spanish.

*   **Download size**: `501.27 MiB`

*   **Dataset size**: `1.29 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split                           | Examples
:------------------------------ | -------:
`'challenge_test_covid'`        | 1,938
`'challenge_train_sample'`      | 500
`'challenge_validation_sample'` | 500
`'test'`                        | 13,366
`'train'`                       | 259,888
`'validation'`                  | 9,977

*   **Features**:

```python
FeaturesDict({
    'date': tf.string,
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
    'text': tf.string,
    'title': tf.string,
    'topic': tf.string,
    'url': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-mlsum_es-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{scialom-etal-2020-mlsum,
    title = "{MLSUM}: The Multilingual Summarization Corpus",
    author = {Scialom, Thomas  and Dray, Paul-Alexis  and Lamprier, Sylvain  and Piwowarski, Benjamin  and Staiano, Jacopo},
    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
    year = {2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/schema_guided_dialog

*   **Config description**: The Schema-Guided Dialogue (SGD) dataset contains
    18K multi-domain task-oriented dialogues between a human and a virtual
    assistant, which covers 17 domains ranging from banks and events to media,
    calendar, travel, and weather.

*   **Download size**: `17.00 MiB`

*   **Dataset size**: `201.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (challenge_test_backtranslation, challenge_test_bfp02,
    challenge_test_bfp05, challenge_test_nopunc, challenge_test_scramble,
    challenge_train_sample, challenge_validation_sample, test, validation), Only
    when `shuffle_files=False` (train)

*   **Splits**:

Split                              | Examples
:--------------------------------- | -------:
`'challenge_test_backtranslation'` | 500
`'challenge_test_bfp02'`           | 500
`'challenge_test_bfp05'`           | 500
`'challenge_test_nopunc'`          | 500
`'challenge_test_scramble'`        | 500
`'challenge_train_sample'`         | 500
`'challenge_validation_sample'`    | 500
`'test'`                           | 10,000
`'train'`                          | 164,982
`'validation'`                     | 10,000

*   **Features**:

```python
FeaturesDict({
    'context': Sequence(tf.string),
    'dialog_acts': Sequence({
        'act': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'slot': tf.string,
        'values': Sequence(tf.string),
    }),
    'dialog_id': tf.string,
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'prompt': tf.string,
    'references': Sequence(tf.string),
    'service': tf.string,
    'target': tf.string,
    'turn_id': tf.int32,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-schema_guided_dialog-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@article{rastogi2019towards,
  title={Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset},
  author={Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},
  journal={arXiv preprint arXiv:1909.05855},
  year={2019}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/totto

*   **Config description**: ToTTo is a Table-to-Text NLG task. The task is as
    follows: Given a Wikipedia table with row names, column names and table
    cells, with a subset of cells highlighted, generate a natural language
    description for the highlighted part of the table.

*   **Download size**: `180.75 MiB`

*   **Dataset size**: `645.86 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split                           | Examples
:------------------------------ | -------:
`'challenge_test_scramble'`     | 500
`'challenge_train_sample'`      | 500
`'challenge_validation_sample'` | 500
`'test'`                        | 7,700
`'train'`                       | 121,153
`'validation'`                  | 7,700

*   **Features**:

```python
FeaturesDict({
    'example_id': tf.string,
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'highlighted_cells': Sequence(Sequence(tf.int32)),
    'overlap_subset': tf.string,
    'references': Sequence(tf.string),
    'sentence_annotations': Sequence({
        'final_sentence': tf.string,
        'original_sentence': tf.string,
        'sentence_after_ambiguity': tf.string,
        'sentence_after_deletion': tf.string,
    }),
    'table': Sequence(Sequence({
        'column_span': tf.int32,
        'is_header': tf.bool,
        'row_span': tf.int32,
        'value': tf.string,
    })),
    'table_page_title': tf.string,
    'table_section_text': tf.string,
    'table_section_title': tf.string,
    'table_webpage_url': tf.string,
    'target': tf.string,
    'totto_id': tf.int32,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-totto-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{parikh2020totto,
  title=ToTTo: A Controlled Table-To-Text Generation Dataset,
  author={Parikh, Ankur and Wang, Xuezhi and Gehrmann, Sebastian and Faruqui, Manaal and Dhingra, Bhuwan and Yang, Diyi and Das, Dipanjan},
  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  pages={1173--1186},
  year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/web_nlg_en

*   **Config description**: WebNLG is a bi-lingual dataset (English, Russian) of
    parallel DBpedia triple sets and short texts that cover about 450 different
    DBpedia properties. The WebNLG data was originally created to promote the
    development of RDF verbalisers able to generate short text and to handle
    micro-planning.

*   **Download size**: `12.57 MiB`

*   **Dataset size**: `19.91 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split                           | Examples
:------------------------------ | -------:
`'challenge_test_numbers'`      | 500
`'challenge_test_scramble'`     | 500
`'challenge_train_sample'`      | 502
`'challenge_validation_sample'` | 499
`'test'`                        | 1,779
`'train'`                       | 35,426
`'validation'`                  | 1,667

*   **Features**:

```python
FeaturesDict({
    'category': tf.string,
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'input': Sequence(tf.string),
    'references': Sequence(tf.string),
    'target': tf.string,
    'webnlg_id': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-web_nlg_en-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{gardent2017creating,
  author =  "Gardent, Claire
    and Shimorina, Anastasia
    and Narayan, Shashi
    and Perez-Beltrachini, Laura",
  title =   "Creating Training Corpora for NLG Micro-Planners",
  booktitle =   "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  year =    "2017",
  publisher =   "Association for Computational Linguistics",
  pages =   "179--188",
  location =    "Vancouver, Canada",
  doi =     "10.18653/v1/P17-1017",
  url =     "http://www.aclweb.org/anthology/P17-1017"
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/web_nlg_ru

*   **Config description**: WebNLG is a bi-lingual dataset (English, Russian) of
    parallel DBpedia triple sets and short texts that cover about 450 different
    DBpedia properties. The WebNLG data was originally created to promote the
    development of RDF verbalisers able to generate short text and to handle
    micro-planning.

*   **Download size**: `7.49 MiB`

*   **Dataset size**: `11.30 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split                           | Examples
:------------------------------ | -------:
`'challenge_test_scramble'`     | 500
`'challenge_train_sample'`      | 501
`'challenge_validation_sample'` | 500
`'test'`                        | 1,102
`'train'`                       | 14,630
`'validation'`                  | 790

*   **Features**:

```python
FeaturesDict({
    'category': tf.string,
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'input': Sequence(tf.string),
    'references': Sequence(tf.string),
    'target': tf.string,
    'webnlg_id': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-web_nlg_ru-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{gardent2017creating,
  author =  "Gardent, Claire
    and Shimorina, Anastasia
    and Narayan, Shashi
    and Perez-Beltrachini, Laura",
  title =   "Creating Training Corpora for NLG Micro-Planners",
  booktitle =   "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  year =    "2017",
  publisher =   "Association for Computational Linguistics",
  pages =   "179--188",
  location =    "Vancouver, Canada",
  doi =     "10.18653/v1/P17-1017",
  url =     "http://www.aclweb.org/anthology/P17-1017"
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_auto_asset_turk

*   **Config description**: WikiAuto provides a set of aligned sentences from
    English Wikipedia and Simple English Wikipedia as a resource to train
    sentence simplification systems. ASSET and TURK are high-quality
    simplification datasets used for testing.

*   **Download size**: `121.01 MiB`

*   **Dataset size**: `202.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (challenge_test_asset_backtranslation, challenge_test_asset_bfp02,
    challenge_test_asset_bfp05, challenge_test_asset_nopunc,
    challenge_test_turk_backtranslation, challenge_test_turk_bfp02,
    challenge_test_turk_bfp05, challenge_test_turk_nopunc,
    challenge_train_sample, challenge_validation_sample, test_asset, test_turk,
    validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split                                    | Examples
:--------------------------------------- | -------:
`'challenge_test_asset_backtranslation'` | 359
`'challenge_test_asset_bfp02'`           | 359
`'challenge_test_asset_bfp05'`           | 359
`'challenge_test_asset_nopunc'`          | 359
`'challenge_test_turk_backtranslation'`  | 359
`'challenge_test_turk_bfp02'`            | 359
`'challenge_test_turk_bfp05'`            | 359
`'challenge_test_turk_nopunc'`           | 359
`'challenge_train_sample'`               | 500
`'challenge_validation_sample'`          | 500
`'test_asset'`                           | 359
`'test_turk'`                            | 359
`'train'`                                | 483,801
`'validation'`                           | 20,000

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'target': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_auto_asset_turk-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{jiang-etal-2020-neural,
    title = "Neural {CRF} Model for Sentence Alignment in Text Simplification",
    author = "Jiang, Chao  and
      Maddela, Mounica  and
      Lan, Wuwei  and
      Zhong, Yang  and
      Xu, Wei",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.709",
    doi = "10.18653/v1/2020.acl-main.709",
    pages = "7943--7960",
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/xsum

*   **Config description**: The dataset is for the task of abstractive
    summarization in its extreme form, its about summarizing a document in a
    single sentence.

*   **Download size**: `246.31 MiB`

*   **Dataset size**: `78.89 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split                              | Examples
:--------------------------------- | -------:
`'challenge_test_backtranslation'` | 500
`'challenge_test_bfp_02'`          | 500
`'challenge_test_bfp_05'`          | 500
`'challenge_test_covid'`           | 401
`'challenge_test_nopunc'`          | 500
`'challenge_train_sample'`         | 500
`'challenge_validation_sample'`    | 500
`'test'`                           | 1,166
`'train'`                          | 23,206
`'validation'`                     | 1,117

*   **Features**:

```python
FeaturesDict({
    'document': tf.string,
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
    'xsum_id': tf.string,
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-xsum-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{Narayan2018dont,
  author = "Shashi Narayan and Shay B. Cohen and Mirella Lapata",
  title = "Don't Give Me the Details, Just the Summary! {T}opic-Aware Convolutional Neural Networks for Extreme Summarization",
  booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing ",
  year = "2018",
  address = "Brussels, Belgium",
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_arabic_ar

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `56.25 MiB`

*   **Dataset size**: `291.42 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 5,841
`'train'`      | 20,441
`'validation'` | 2,919

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'ar': Text(shape=(), dtype=tf.string),
        'en': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'ar': Text(shape=(), dtype=tf.string),
        'en': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_arabic_ar-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_chinese_zh

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `31.38 MiB`

*   **Dataset size**: `122.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 3,775
`'train'`      | 13,211
`'validation'` | 1,886

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'zh': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'zh': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_chinese_zh-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_czech_cs

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `13.84 MiB`

*   **Dataset size**: `58.05 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,438
`'train'`      | 5,033
`'validation'` | 718

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'cs': Text(shape=(), dtype=tf.string),
        'en': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'cs': Text(shape=(), dtype=tf.string),
        'en': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_czech_cs-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_dutch_nl

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `53.88 MiB`

*   **Dataset size**: `237.97 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 6,248
`'train'`      | 21,866
`'validation'` | 3,123

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'nl': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'nl': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_dutch_nl-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_english_en

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `112.56 MiB`

*   **Dataset size**: `657.51 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 28,614
`'train'`      | 99,020
`'validation'` | 13,823

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_english_en-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_french_fr

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `113.26 MiB`

*   **Dataset size**: `522.28 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 12,731
`'train'`      | 44,556
`'validation'` | 6,364

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'fr': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'fr': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_french_fr-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_german_de

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `102.65 MiB`

*   **Dataset size**: `452.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 11,669
`'train'`      | 40,839
`'validation'` | 5,833

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'de': Text(shape=(), dtype=tf.string),
        'en': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'de': Text(shape=(), dtype=tf.string),
        'en': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_german_de-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_hindi_hi

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `20.07 MiB`

*   **Dataset size**: `138.06 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,984
`'train'`      | 6,942
`'validation'` | 991

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'hi': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'hi': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_hindi_hi-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_indonesian_id

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `80.08 MiB`

*   **Dataset size**: `370.63 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 9,497
`'train'`      | 33,237
`'validation'` | 4,747

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'id': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'id': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_indonesian_id-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_italian_it

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `84.80 MiB`

*   **Dataset size**: `374.40 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,189
`'train'`      | 35,661
`'validation'` | 5,093

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'it': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'it': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_italian_it-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_japanese_ja

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `21.75 MiB`

*   **Dataset size**: `103.19 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,530
`'train'`      | 8,853
`'validation'` | 1,264

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'ja': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'ja': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_japanese_ja-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_korean_ko

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `22.26 MiB`

*   **Dataset size**: `102.35 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,436
`'train'`      | 8,524
`'validation'` | 1,216

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'ko': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'ko': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_korean_ko-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_portuguese_pt

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `131.17 MiB`

*   **Dataset size**: `570.46 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 16,331
`'train'`      | 57,159
`'validation'` | 8,165

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'pt': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'pt': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_portuguese_pt-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_russian_ru

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `101.36 MiB`

*   **Dataset size**: `564.69 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 10,580
`'train'`      | 37,028
`'validation'` | 5,288

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'ru': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'ru': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_russian_ru-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_spanish_es

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `189.06 MiB`

*   **Dataset size**: `849.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 22,632
`'train'`      | 79,212
`'validation'` | 11,316

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'es': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'es': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_spanish_es-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_thai_th

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `28.60 MiB`

*   **Dataset size**: `193.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes (test, validation), Only when `shuffle_files=False` (train)

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 2,950
`'train'`      | 10,325
`'validation'` | 1,475

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'th': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'th': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_thai_th-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_turkish_tr

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `6.73 MiB`

*   **Dataset size**: `30.75 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 900
`'train'`      | 3,148
`'validation'` | 449

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'tr': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'tr': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_turkish_tr-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```

## gem/wiki_lingua_vietnamese_vi

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Download size**: `36.27 MiB`

*   **Dataset size**: `179.77 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Yes

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 3,917
`'train'`      | 13,707
`'validation'` | 1,957

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'gem_parent_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'vi': Text(shape=(), dtype=tf.string),
    }),
    'target': tf.string,
    'target_aligned': Translation({
        'en': Text(shape=(), dtype=tf.string),
        'vi': Text(shape=(), dtype=tf.string),
    }),
})
```

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:scroll"></div>
<script src="https://www.gstatic.com/external_hosted/jquery2.min.js"></script>
<script>
var url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/gem-wiki_lingua_vietnamese_vi-1.1.0.html";
$(document).ready(() => {
  $("#displaydataframe").click((event) => {
    // Disable the button after clicking (dataframe loaded only once).
    $("#displaydataframe").prop("disabled", true);

    // Pre-fetch and display the content
    $.get(url, (data) => {
      $("#dataframecontent").html(data);
    }).fail(() => {
      $("#dataframecontent").html(
        'Error loading examples. If the error persist, please open '
        + 'a new issue.'
      );
    });
  });
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
@inproceedings{ladhak-wiki-2020,
title=WikiLingua: A New Benchmark Dataset for Multilingual Abstractive Summarization,
author={Faisal Ladhak, Esin Durmus, Claire Cardie and Kathleen McKeown},
booktitle={Findings of EMNLP, 2020},
year={2020}
}
@article{gehrmann2021gem,
  author    = {Sebastian Gehrmann and
               Tosin P. Adewumi and
               Karmanya Aggarwal and
               Pawan Sasanka Ammanamanchi and
               Aremu Anuoluwapo and
               Antoine Bosselut and
               Khyathi Raghavi Chandu and
               Miruna{-}Adriana Clinciu and
               Dipanjan Das and
               Kaustubh D. Dhole and
               Wanyu Du and
               Esin Durmus and
               Ondrej Dusek and
               Chris Emezue and
               Varun Gangal and
               Cristina Garbacea and
               Tatsunori Hashimoto and
               Yufang Hou and
               Yacine Jernite and
               Harsh Jhamtani and
               Yangfeng Ji and
               Shailza Jolly and
               Dhruv Kumar and
               Faisal Ladhak and
               Aman Madaan and
               Mounica Maddela and
               Khyati Mahajan and
               Saad Mahamood and
               Bodhisattwa Prasad Majumder and
               Pedro Henrique Martins and
               Angelina McMillan{-}Major and
               Simon Mille and
               Emiel van Miltenburg and
               Moin Nadeem and
               Shashi Narayan and
               Vitaly Nikolaev and
               Rubungo Andre Niyongabo and
               Salomey Osei and
               Ankur P. Parikh and
               Laura Perez{-}Beltrachini and
               Niranjan Ramesh Rao and
               Vikas Raunak and
               Juan Diego Rodriguez and
               Sashank Santhanam and
               Jo{\~{a}}o Sedoc and
               Thibault Sellam and
               Samira Shaikh and
               Anastasia Shimorina and
               Marco Antonio Sobrevilla Cabezudo and
               Hendrik Strobelt and
               Nishant Subramani and
               Wei Xu and
               Diyi Yang and
               Akhila Yerukola and
               Jiawei Zhou},
  title     = {The {GEM} Benchmark: Natural Language Generation, its Evaluation and
               Metrics},
  journal   = {CoRR},
  volume    = {abs/2102.01672},
  year      = {2021},
  url       = {https://arxiv.org/abs/2102.01672},
  archivePrefix = {arXiv},
  eprint    = {2102.01672}
}

Note that each GEM dataset has its own citation. Please see the source to see
the correct citation for each contained dataset."
```
