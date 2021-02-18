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

Note: This dataset was added recently and is only available in our
`tfds-nightly` package
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>.

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

    *   **`1.0.0`** (default): Initial version

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

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

## gem/common_gen (default config)

*   **Config description**: CommonGen is a constrained text generation task,
    associated with a benchmark dataset, to explicitly test machines for the
    ability of generative commonsense reasoning. Given a set of common concepts;
    the task is to generate a coherent sentence describing an everyday scenario
    using these concepts.

*   **Features**:

```python
FeaturesDict({
    'concept_set_id': tf.int32,
    'concepts': Sequence(tf.string),
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
})
```

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

*   **Features**:

```python
FeaturesDict({
    'dialog_act': tf.string,
    'dialog_act_delexicalized': tf.string,
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
    'target_delexicalized': tf.string,
})
```

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

*   **Features**:

```python
FeaturesDict({
    'dart_id': tf.int32,
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'subtree_was_extended': tf.bool,
    'target': tf.string,
    'target_sources': Sequence(tf.string),
    'tripleset': Sequence(tf.string),
})
```

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

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'meaning_representation': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
})
```

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

*   **Features**:

```python
FeaturesDict({
    'date': tf.string,
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
    'text': tf.string,
    'title': tf.string,
    'topic': tf.string,
    'url': tf.string,
})
```

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

*   **Features**:

```python
FeaturesDict({
    'date': tf.string,
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
    'text': tf.string,
    'title': tf.string,
    'topic': tf.string,
    'url': tf.string,
})
```

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

*   **Features**:

```python
FeaturesDict({
    'dialog_acts': Sequence({
        'act': ClassLabel(shape=(), dtype=tf.int64, num_classes=18),
        'slot': tf.string,
        'values': Sequence(tf.string),
    }),
    'dialog_id': tf.string,
    'gem_id': tf.string,
    'prompt': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
    'turn_id': tf.int32,
})
```

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

*   **Features**:

```python
FeaturesDict({
    'example_id': tf.string,
    'gem_id': tf.string,
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

*   **Features**:

```python
FeaturesDict({
    'category': tf.string,
    'gem_id': tf.string,
    'input': Sequence(tf.string),
    'references': Sequence(tf.string),
    'target': tf.string,
    'webnlg_id': tf.string,
})
```

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

*   **Features**:

```python
FeaturesDict({
    'category': tf.string,
    'gem_id': tf.string,
    'input': Sequence(tf.string),
    'references': Sequence(tf.string),
    'target': tf.string,
    'webnlg_id': tf.string,
})
```

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

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'source_id': tf.string,
    'target': tf.string,
    'target_id': tf.string,
})
```

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

## gem/wiki_lingua_es_en

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'target': tf.string,
})
```

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

## gem/wiki_lingua_ru_en

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'target': tf.string,
})
```

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

## gem/wiki_lingua_tr_en

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'target': tf.string,
})
```

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

## gem/wiki_lingua_vi_en

*   **Config description**: Wikilingua is a large-scale, multilingual dataset
    for the evaluation of cross-lingual abstractive summarization systems..

*   **Features**:

```python
FeaturesDict({
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'source': tf.string,
    'target': tf.string,
})
```

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

## gem/xsum

*   **Config description**: The dataset is for the task of abstractive
    summarization in its extreme form, its about summarizing a document in a
    single sentence.

*   **Features**:

```python
FeaturesDict({
    'document': tf.string,
    'gem_id': tf.string,
    'references': Sequence(tf.string),
    'target': tf.string,
    'xsum_id': tf.string,
})
```

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
