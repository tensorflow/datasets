<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="istella" />
  <meta itemprop="description" content="The Istella datasets are three large-scale Learning-to-Rank datasets released by&#10;Istella. Each dataset consists of query-document pairs represented as feature&#10;vectors and corresponding relevance judgment labels.&#10;&#10;The dataset contains three versions:&#10;&#10; * `main` (&quot;Istella LETOR&quot;): Containing 10,454,629 query-document pairs.&#10; * `s` (&quot;Istella-S LETOR&quot;): Containing 3,408,630 query-document pairs.&#10; * `x` (&quot;Istella-X LETOR&quot;): Containing 26,791,447 query-document pairs.&#10;&#10;You can specify whether to use the `main`, `s` or `x` version of the dataset as&#10;follows:&#10;&#10;```python&#10;ds = tfds.load(&quot;istella/main&quot;)&#10;ds = tfds.load(&quot;istella/s&quot;)&#10;ds = tfds.load(&quot;istella/x&quot;)&#10;```&#10;&#10;If only `istella` is specified, the `istella/main` option is selected by&#10;default:&#10;&#10;```python&#10;# This is the same as `tfds.load(&quot;istella/main&quot;)`&#10;ds = tfds.load(&quot;istella&quot;)&#10;```&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;istella&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/istella" />
  <meta itemprop="sameAs" content="http://quickrank.isti.cnr.it/istella-dataset/" />
  <meta itemprop="citation" content="@article{10.1145/2987380,&#10;  author = {Dato, Domenico and Lucchese, Claudio and Nardini, Franco Maria and Orlando, Salvatore and Perego, Raffaele and Tonellotto, Nicola and Venturini, Rossano},&#10;  title = {Fast Ranking with Additive Ensembles of Oblivious and Non-Oblivious Regression Trees},&#10;  year = {2016},&#10;  publisher = {ACM},&#10;  address = {New York, NY, USA},&#10;  volume = {35},&#10;  number = {2},&#10;  issn = {1046-8188},&#10;  url = {https://doi.org/10.1145/2987380},&#10;  doi = {10.1145/2987380},&#10;  journal = {ACM Transactions on Information Systems},&#10;  articleno = {15},&#10;  numpages = {31},&#10;}" />
</div>

# `istella`


*   **Description**:

The Istella datasets are three large-scale Learning-to-Rank datasets released by
Istella. Each dataset consists of query-document pairs represented as feature
vectors and corresponding relevance judgment labels.

The dataset contains three versions:

*   `main` ("Istella LETOR"): Containing 10,454,629 query-document pairs.
*   `s` ("Istella-S LETOR"): Containing 3,408,630 query-document pairs.
*   `x` ("Istella-X LETOR"): Containing 26,791,447 query-document pairs.

You can specify whether to use the `main`, `s` or `x` version of the dataset as
follows:

```python
ds = tfds.load("istella/main")
ds = tfds.load("istella/s")
ds = tfds.load("istella/x")
```

If only `istella` is specified, the `istella/main` option is selected by
default:

```python
# This is the same as `tfds.load("istella/main")`
ds = tfds.load("istella")
```

*   **Homepage**:
    [http://quickrank.isti.cnr.it/istella-dataset/](http://quickrank.isti.cnr.it/istella-dataset/)

*   **Source code**:
    [`tfds.ranking.istella.Istella`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/ranking/istella/istella.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`1.0.1`** (default): Fix serialization to support float64.

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Feature structure**:

```python
FeaturesDict({
    'feature_1': Tensor(shape=(None,), dtype=tf.float64),
    'feature_10': Tensor(shape=(None,), dtype=tf.float64),
    'feature_100': Tensor(shape=(None,), dtype=tf.float64),
    'feature_101': Tensor(shape=(None,), dtype=tf.float64),
    'feature_102': Tensor(shape=(None,), dtype=tf.float64),
    'feature_103': Tensor(shape=(None,), dtype=tf.float64),
    'feature_104': Tensor(shape=(None,), dtype=tf.float64),
    'feature_105': Tensor(shape=(None,), dtype=tf.float64),
    'feature_106': Tensor(shape=(None,), dtype=tf.float64),
    'feature_107': Tensor(shape=(None,), dtype=tf.float64),
    'feature_108': Tensor(shape=(None,), dtype=tf.float64),
    'feature_109': Tensor(shape=(None,), dtype=tf.float64),
    'feature_11': Tensor(shape=(None,), dtype=tf.float64),
    'feature_110': Tensor(shape=(None,), dtype=tf.float64),
    'feature_111': Tensor(shape=(None,), dtype=tf.float64),
    'feature_112': Tensor(shape=(None,), dtype=tf.float64),
    'feature_113': Tensor(shape=(None,), dtype=tf.float64),
    'feature_114': Tensor(shape=(None,), dtype=tf.float64),
    'feature_115': Tensor(shape=(None,), dtype=tf.float64),
    'feature_116': Tensor(shape=(None,), dtype=tf.float64),
    'feature_117': Tensor(shape=(None,), dtype=tf.float64),
    'feature_118': Tensor(shape=(None,), dtype=tf.float64),
    'feature_119': Tensor(shape=(None,), dtype=tf.float64),
    'feature_12': Tensor(shape=(None,), dtype=tf.float64),
    'feature_120': Tensor(shape=(None,), dtype=tf.float64),
    'feature_121': Tensor(shape=(None,), dtype=tf.float64),
    'feature_122': Tensor(shape=(None,), dtype=tf.float64),
    'feature_123': Tensor(shape=(None,), dtype=tf.float64),
    'feature_124': Tensor(shape=(None,), dtype=tf.float64),
    'feature_125': Tensor(shape=(None,), dtype=tf.float64),
    'feature_126': Tensor(shape=(None,), dtype=tf.float64),
    'feature_127': Tensor(shape=(None,), dtype=tf.float64),
    'feature_128': Tensor(shape=(None,), dtype=tf.float64),
    'feature_129': Tensor(shape=(None,), dtype=tf.float64),
    'feature_13': Tensor(shape=(None,), dtype=tf.float64),
    'feature_130': Tensor(shape=(None,), dtype=tf.float64),
    'feature_131': Tensor(shape=(None,), dtype=tf.float64),
    'feature_132': Tensor(shape=(None,), dtype=tf.float64),
    'feature_133': Tensor(shape=(None,), dtype=tf.float64),
    'feature_134': Tensor(shape=(None,), dtype=tf.float64),
    'feature_135': Tensor(shape=(None,), dtype=tf.float64),
    'feature_136': Tensor(shape=(None,), dtype=tf.float64),
    'feature_137': Tensor(shape=(None,), dtype=tf.float64),
    'feature_138': Tensor(shape=(None,), dtype=tf.float64),
    'feature_139': Tensor(shape=(None,), dtype=tf.float64),
    'feature_14': Tensor(shape=(None,), dtype=tf.float64),
    'feature_140': Tensor(shape=(None,), dtype=tf.float64),
    'feature_141': Tensor(shape=(None,), dtype=tf.float64),
    'feature_142': Tensor(shape=(None,), dtype=tf.float64),
    'feature_143': Tensor(shape=(None,), dtype=tf.float64),
    'feature_144': Tensor(shape=(None,), dtype=tf.float64),
    'feature_145': Tensor(shape=(None,), dtype=tf.float64),
    'feature_146': Tensor(shape=(None,), dtype=tf.float64),
    'feature_147': Tensor(shape=(None,), dtype=tf.float64),
    'feature_148': Tensor(shape=(None,), dtype=tf.float64),
    'feature_149': Tensor(shape=(None,), dtype=tf.float64),
    'feature_15': Tensor(shape=(None,), dtype=tf.float64),
    'feature_150': Tensor(shape=(None,), dtype=tf.float64),
    'feature_151': Tensor(shape=(None,), dtype=tf.float64),
    'feature_152': Tensor(shape=(None,), dtype=tf.float64),
    'feature_153': Tensor(shape=(None,), dtype=tf.float64),
    'feature_154': Tensor(shape=(None,), dtype=tf.float64),
    'feature_155': Tensor(shape=(None,), dtype=tf.float64),
    'feature_156': Tensor(shape=(None,), dtype=tf.float64),
    'feature_157': Tensor(shape=(None,), dtype=tf.float64),
    'feature_158': Tensor(shape=(None,), dtype=tf.float64),
    'feature_159': Tensor(shape=(None,), dtype=tf.float64),
    'feature_16': Tensor(shape=(None,), dtype=tf.float64),
    'feature_160': Tensor(shape=(None,), dtype=tf.float64),
    'feature_161': Tensor(shape=(None,), dtype=tf.float64),
    'feature_162': Tensor(shape=(None,), dtype=tf.float64),
    'feature_163': Tensor(shape=(None,), dtype=tf.float64),
    'feature_164': Tensor(shape=(None,), dtype=tf.float64),
    'feature_165': Tensor(shape=(None,), dtype=tf.float64),
    'feature_166': Tensor(shape=(None,), dtype=tf.float64),
    'feature_167': Tensor(shape=(None,), dtype=tf.float64),
    'feature_168': Tensor(shape=(None,), dtype=tf.float64),
    'feature_169': Tensor(shape=(None,), dtype=tf.float64),
    'feature_17': Tensor(shape=(None,), dtype=tf.float64),
    'feature_170': Tensor(shape=(None,), dtype=tf.float64),
    'feature_171': Tensor(shape=(None,), dtype=tf.float64),
    'feature_172': Tensor(shape=(None,), dtype=tf.float64),
    'feature_173': Tensor(shape=(None,), dtype=tf.float64),
    'feature_174': Tensor(shape=(None,), dtype=tf.float64),
    'feature_175': Tensor(shape=(None,), dtype=tf.float64),
    'feature_176': Tensor(shape=(None,), dtype=tf.float64),
    'feature_177': Tensor(shape=(None,), dtype=tf.float64),
    'feature_178': Tensor(shape=(None,), dtype=tf.float64),
    'feature_179': Tensor(shape=(None,), dtype=tf.float64),
    'feature_18': Tensor(shape=(None,), dtype=tf.float64),
    'feature_180': Tensor(shape=(None,), dtype=tf.float64),
    'feature_181': Tensor(shape=(None,), dtype=tf.float64),
    'feature_182': Tensor(shape=(None,), dtype=tf.float64),
    'feature_183': Tensor(shape=(None,), dtype=tf.float64),
    'feature_184': Tensor(shape=(None,), dtype=tf.float64),
    'feature_185': Tensor(shape=(None,), dtype=tf.float64),
    'feature_186': Tensor(shape=(None,), dtype=tf.float64),
    'feature_187': Tensor(shape=(None,), dtype=tf.float64),
    'feature_188': Tensor(shape=(None,), dtype=tf.float64),
    'feature_189': Tensor(shape=(None,), dtype=tf.float64),
    'feature_19': Tensor(shape=(None,), dtype=tf.float64),
    'feature_190': Tensor(shape=(None,), dtype=tf.float64),
    'feature_191': Tensor(shape=(None,), dtype=tf.float64),
    'feature_192': Tensor(shape=(None,), dtype=tf.float64),
    'feature_193': Tensor(shape=(None,), dtype=tf.float64),
    'feature_194': Tensor(shape=(None,), dtype=tf.float64),
    'feature_195': Tensor(shape=(None,), dtype=tf.float64),
    'feature_196': Tensor(shape=(None,), dtype=tf.float64),
    'feature_197': Tensor(shape=(None,), dtype=tf.float64),
    'feature_198': Tensor(shape=(None,), dtype=tf.float64),
    'feature_199': Tensor(shape=(None,), dtype=tf.float64),
    'feature_2': Tensor(shape=(None,), dtype=tf.float64),
    'feature_20': Tensor(shape=(None,), dtype=tf.float64),
    'feature_200': Tensor(shape=(None,), dtype=tf.float64),
    'feature_201': Tensor(shape=(None,), dtype=tf.float64),
    'feature_202': Tensor(shape=(None,), dtype=tf.float64),
    'feature_203': Tensor(shape=(None,), dtype=tf.float64),
    'feature_204': Tensor(shape=(None,), dtype=tf.float64),
    'feature_205': Tensor(shape=(None,), dtype=tf.float64),
    'feature_206': Tensor(shape=(None,), dtype=tf.float64),
    'feature_207': Tensor(shape=(None,), dtype=tf.float64),
    'feature_208': Tensor(shape=(None,), dtype=tf.float64),
    'feature_209': Tensor(shape=(None,), dtype=tf.float64),
    'feature_21': Tensor(shape=(None,), dtype=tf.float64),
    'feature_210': Tensor(shape=(None,), dtype=tf.float64),
    'feature_211': Tensor(shape=(None,), dtype=tf.float64),
    'feature_212': Tensor(shape=(None,), dtype=tf.float64),
    'feature_213': Tensor(shape=(None,), dtype=tf.float64),
    'feature_214': Tensor(shape=(None,), dtype=tf.float64),
    'feature_215': Tensor(shape=(None,), dtype=tf.float64),
    'feature_216': Tensor(shape=(None,), dtype=tf.float64),
    'feature_217': Tensor(shape=(None,), dtype=tf.float64),
    'feature_218': Tensor(shape=(None,), dtype=tf.float64),
    'feature_219': Tensor(shape=(None,), dtype=tf.float64),
    'feature_22': Tensor(shape=(None,), dtype=tf.float64),
    'feature_220': Tensor(shape=(None,), dtype=tf.float64),
    'feature_23': Tensor(shape=(None,), dtype=tf.float64),
    'feature_24': Tensor(shape=(None,), dtype=tf.float64),
    'feature_25': Tensor(shape=(None,), dtype=tf.float64),
    'feature_26': Tensor(shape=(None,), dtype=tf.float64),
    'feature_27': Tensor(shape=(None,), dtype=tf.float64),
    'feature_28': Tensor(shape=(None,), dtype=tf.float64),
    'feature_29': Tensor(shape=(None,), dtype=tf.float64),
    'feature_3': Tensor(shape=(None,), dtype=tf.float64),
    'feature_30': Tensor(shape=(None,), dtype=tf.float64),
    'feature_31': Tensor(shape=(None,), dtype=tf.float64),
    'feature_32': Tensor(shape=(None,), dtype=tf.float64),
    'feature_33': Tensor(shape=(None,), dtype=tf.float64),
    'feature_34': Tensor(shape=(None,), dtype=tf.float64),
    'feature_35': Tensor(shape=(None,), dtype=tf.float64),
    'feature_36': Tensor(shape=(None,), dtype=tf.float64),
    'feature_37': Tensor(shape=(None,), dtype=tf.float64),
    'feature_38': Tensor(shape=(None,), dtype=tf.float64),
    'feature_39': Tensor(shape=(None,), dtype=tf.float64),
    'feature_4': Tensor(shape=(None,), dtype=tf.float64),
    'feature_40': Tensor(shape=(None,), dtype=tf.float64),
    'feature_41': Tensor(shape=(None,), dtype=tf.float64),
    'feature_42': Tensor(shape=(None,), dtype=tf.float64),
    'feature_43': Tensor(shape=(None,), dtype=tf.float64),
    'feature_44': Tensor(shape=(None,), dtype=tf.float64),
    'feature_45': Tensor(shape=(None,), dtype=tf.float64),
    'feature_46': Tensor(shape=(None,), dtype=tf.float64),
    'feature_47': Tensor(shape=(None,), dtype=tf.float64),
    'feature_48': Tensor(shape=(None,), dtype=tf.float64),
    'feature_49': Tensor(shape=(None,), dtype=tf.float64),
    'feature_5': Tensor(shape=(None,), dtype=tf.float64),
    'feature_50': Tensor(shape=(None,), dtype=tf.float64),
    'feature_51': Tensor(shape=(None,), dtype=tf.float64),
    'feature_52': Tensor(shape=(None,), dtype=tf.float64),
    'feature_53': Tensor(shape=(None,), dtype=tf.float64),
    'feature_54': Tensor(shape=(None,), dtype=tf.float64),
    'feature_55': Tensor(shape=(None,), dtype=tf.float64),
    'feature_56': Tensor(shape=(None,), dtype=tf.float64),
    'feature_57': Tensor(shape=(None,), dtype=tf.float64),
    'feature_58': Tensor(shape=(None,), dtype=tf.float64),
    'feature_59': Tensor(shape=(None,), dtype=tf.float64),
    'feature_6': Tensor(shape=(None,), dtype=tf.float64),
    'feature_60': Tensor(shape=(None,), dtype=tf.float64),
    'feature_61': Tensor(shape=(None,), dtype=tf.float64),
    'feature_62': Tensor(shape=(None,), dtype=tf.float64),
    'feature_63': Tensor(shape=(None,), dtype=tf.float64),
    'feature_64': Tensor(shape=(None,), dtype=tf.float64),
    'feature_65': Tensor(shape=(None,), dtype=tf.float64),
    'feature_66': Tensor(shape=(None,), dtype=tf.float64),
    'feature_67': Tensor(shape=(None,), dtype=tf.float64),
    'feature_68': Tensor(shape=(None,), dtype=tf.float64),
    'feature_69': Tensor(shape=(None,), dtype=tf.float64),
    'feature_7': Tensor(shape=(None,), dtype=tf.float64),
    'feature_70': Tensor(shape=(None,), dtype=tf.float64),
    'feature_71': Tensor(shape=(None,), dtype=tf.float64),
    'feature_72': Tensor(shape=(None,), dtype=tf.float64),
    'feature_73': Tensor(shape=(None,), dtype=tf.float64),
    'feature_74': Tensor(shape=(None,), dtype=tf.float64),
    'feature_75': Tensor(shape=(None,), dtype=tf.float64),
    'feature_76': Tensor(shape=(None,), dtype=tf.float64),
    'feature_77': Tensor(shape=(None,), dtype=tf.float64),
    'feature_78': Tensor(shape=(None,), dtype=tf.float64),
    'feature_79': Tensor(shape=(None,), dtype=tf.float64),
    'feature_8': Tensor(shape=(None,), dtype=tf.float64),
    'feature_80': Tensor(shape=(None,), dtype=tf.float64),
    'feature_81': Tensor(shape=(None,), dtype=tf.float64),
    'feature_82': Tensor(shape=(None,), dtype=tf.float64),
    'feature_83': Tensor(shape=(None,), dtype=tf.float64),
    'feature_84': Tensor(shape=(None,), dtype=tf.float64),
    'feature_85': Tensor(shape=(None,), dtype=tf.float64),
    'feature_86': Tensor(shape=(None,), dtype=tf.float64),
    'feature_87': Tensor(shape=(None,), dtype=tf.float64),
    'feature_88': Tensor(shape=(None,), dtype=tf.float64),
    'feature_89': Tensor(shape=(None,), dtype=tf.float64),
    'feature_9': Tensor(shape=(None,), dtype=tf.float64),
    'feature_90': Tensor(shape=(None,), dtype=tf.float64),
    'feature_91': Tensor(shape=(None,), dtype=tf.float64),
    'feature_92': Tensor(shape=(None,), dtype=tf.float64),
    'feature_93': Tensor(shape=(None,), dtype=tf.float64),
    'feature_94': Tensor(shape=(None,), dtype=tf.float64),
    'feature_95': Tensor(shape=(None,), dtype=tf.float64),
    'feature_96': Tensor(shape=(None,), dtype=tf.float64),
    'feature_97': Tensor(shape=(None,), dtype=tf.float64),
    'feature_98': Tensor(shape=(None,), dtype=tf.float64),
    'feature_99': Tensor(shape=(None,), dtype=tf.float64),
    'label': Tensor(shape=(None,), dtype=tf.float64),
})
```

*   **Feature documentation**:

Feature     | Class        | Shape   | Dtype      | Description
:---------- | :----------- | :------ | :--------- | :----------
            | FeaturesDict |         |            |
feature_1   | Tensor       | (None,) | tf.float64 |
feature_10  | Tensor       | (None,) | tf.float64 |
feature_100 | Tensor       | (None,) | tf.float64 |
feature_101 | Tensor       | (None,) | tf.float64 |
feature_102 | Tensor       | (None,) | tf.float64 |
feature_103 | Tensor       | (None,) | tf.float64 |
feature_104 | Tensor       | (None,) | tf.float64 |
feature_105 | Tensor       | (None,) | tf.float64 |
feature_106 | Tensor       | (None,) | tf.float64 |
feature_107 | Tensor       | (None,) | tf.float64 |
feature_108 | Tensor       | (None,) | tf.float64 |
feature_109 | Tensor       | (None,) | tf.float64 |
feature_11  | Tensor       | (None,) | tf.float64 |
feature_110 | Tensor       | (None,) | tf.float64 |
feature_111 | Tensor       | (None,) | tf.float64 |
feature_112 | Tensor       | (None,) | tf.float64 |
feature_113 | Tensor       | (None,) | tf.float64 |
feature_114 | Tensor       | (None,) | tf.float64 |
feature_115 | Tensor       | (None,) | tf.float64 |
feature_116 | Tensor       | (None,) | tf.float64 |
feature_117 | Tensor       | (None,) | tf.float64 |
feature_118 | Tensor       | (None,) | tf.float64 |
feature_119 | Tensor       | (None,) | tf.float64 |
feature_12  | Tensor       | (None,) | tf.float64 |
feature_120 | Tensor       | (None,) | tf.float64 |
feature_121 | Tensor       | (None,) | tf.float64 |
feature_122 | Tensor       | (None,) | tf.float64 |
feature_123 | Tensor       | (None,) | tf.float64 |
feature_124 | Tensor       | (None,) | tf.float64 |
feature_125 | Tensor       | (None,) | tf.float64 |
feature_126 | Tensor       | (None,) | tf.float64 |
feature_127 | Tensor       | (None,) | tf.float64 |
feature_128 | Tensor       | (None,) | tf.float64 |
feature_129 | Tensor       | (None,) | tf.float64 |
feature_13  | Tensor       | (None,) | tf.float64 |
feature_130 | Tensor       | (None,) | tf.float64 |
feature_131 | Tensor       | (None,) | tf.float64 |
feature_132 | Tensor       | (None,) | tf.float64 |
feature_133 | Tensor       | (None,) | tf.float64 |
feature_134 | Tensor       | (None,) | tf.float64 |
feature_135 | Tensor       | (None,) | tf.float64 |
feature_136 | Tensor       | (None,) | tf.float64 |
feature_137 | Tensor       | (None,) | tf.float64 |
feature_138 | Tensor       | (None,) | tf.float64 |
feature_139 | Tensor       | (None,) | tf.float64 |
feature_14  | Tensor       | (None,) | tf.float64 |
feature_140 | Tensor       | (None,) | tf.float64 |
feature_141 | Tensor       | (None,) | tf.float64 |
feature_142 | Tensor       | (None,) | tf.float64 |
feature_143 | Tensor       | (None,) | tf.float64 |
feature_144 | Tensor       | (None,) | tf.float64 |
feature_145 | Tensor       | (None,) | tf.float64 |
feature_146 | Tensor       | (None,) | tf.float64 |
feature_147 | Tensor       | (None,) | tf.float64 |
feature_148 | Tensor       | (None,) | tf.float64 |
feature_149 | Tensor       | (None,) | tf.float64 |
feature_15  | Tensor       | (None,) | tf.float64 |
feature_150 | Tensor       | (None,) | tf.float64 |
feature_151 | Tensor       | (None,) | tf.float64 |
feature_152 | Tensor       | (None,) | tf.float64 |
feature_153 | Tensor       | (None,) | tf.float64 |
feature_154 | Tensor       | (None,) | tf.float64 |
feature_155 | Tensor       | (None,) | tf.float64 |
feature_156 | Tensor       | (None,) | tf.float64 |
feature_157 | Tensor       | (None,) | tf.float64 |
feature_158 | Tensor       | (None,) | tf.float64 |
feature_159 | Tensor       | (None,) | tf.float64 |
feature_16  | Tensor       | (None,) | tf.float64 |
feature_160 | Tensor       | (None,) | tf.float64 |
feature_161 | Tensor       | (None,) | tf.float64 |
feature_162 | Tensor       | (None,) | tf.float64 |
feature_163 | Tensor       | (None,) | tf.float64 |
feature_164 | Tensor       | (None,) | tf.float64 |
feature_165 | Tensor       | (None,) | tf.float64 |
feature_166 | Tensor       | (None,) | tf.float64 |
feature_167 | Tensor       | (None,) | tf.float64 |
feature_168 | Tensor       | (None,) | tf.float64 |
feature_169 | Tensor       | (None,) | tf.float64 |
feature_17  | Tensor       | (None,) | tf.float64 |
feature_170 | Tensor       | (None,) | tf.float64 |
feature_171 | Tensor       | (None,) | tf.float64 |
feature_172 | Tensor       | (None,) | tf.float64 |
feature_173 | Tensor       | (None,) | tf.float64 |
feature_174 | Tensor       | (None,) | tf.float64 |
feature_175 | Tensor       | (None,) | tf.float64 |
feature_176 | Tensor       | (None,) | tf.float64 |
feature_177 | Tensor       | (None,) | tf.float64 |
feature_178 | Tensor       | (None,) | tf.float64 |
feature_179 | Tensor       | (None,) | tf.float64 |
feature_18  | Tensor       | (None,) | tf.float64 |
feature_180 | Tensor       | (None,) | tf.float64 |
feature_181 | Tensor       | (None,) | tf.float64 |
feature_182 | Tensor       | (None,) | tf.float64 |
feature_183 | Tensor       | (None,) | tf.float64 |
feature_184 | Tensor       | (None,) | tf.float64 |
feature_185 | Tensor       | (None,) | tf.float64 |
feature_186 | Tensor       | (None,) | tf.float64 |
feature_187 | Tensor       | (None,) | tf.float64 |
feature_188 | Tensor       | (None,) | tf.float64 |
feature_189 | Tensor       | (None,) | tf.float64 |
feature_19  | Tensor       | (None,) | tf.float64 |
feature_190 | Tensor       | (None,) | tf.float64 |
feature_191 | Tensor       | (None,) | tf.float64 |
feature_192 | Tensor       | (None,) | tf.float64 |
feature_193 | Tensor       | (None,) | tf.float64 |
feature_194 | Tensor       | (None,) | tf.float64 |
feature_195 | Tensor       | (None,) | tf.float64 |
feature_196 | Tensor       | (None,) | tf.float64 |
feature_197 | Tensor       | (None,) | tf.float64 |
feature_198 | Tensor       | (None,) | tf.float64 |
feature_199 | Tensor       | (None,) | tf.float64 |
feature_2   | Tensor       | (None,) | tf.float64 |
feature_20  | Tensor       | (None,) | tf.float64 |
feature_200 | Tensor       | (None,) | tf.float64 |
feature_201 | Tensor       | (None,) | tf.float64 |
feature_202 | Tensor       | (None,) | tf.float64 |
feature_203 | Tensor       | (None,) | tf.float64 |
feature_204 | Tensor       | (None,) | tf.float64 |
feature_205 | Tensor       | (None,) | tf.float64 |
feature_206 | Tensor       | (None,) | tf.float64 |
feature_207 | Tensor       | (None,) | tf.float64 |
feature_208 | Tensor       | (None,) | tf.float64 |
feature_209 | Tensor       | (None,) | tf.float64 |
feature_21  | Tensor       | (None,) | tf.float64 |
feature_210 | Tensor       | (None,) | tf.float64 |
feature_211 | Tensor       | (None,) | tf.float64 |
feature_212 | Tensor       | (None,) | tf.float64 |
feature_213 | Tensor       | (None,) | tf.float64 |
feature_214 | Tensor       | (None,) | tf.float64 |
feature_215 | Tensor       | (None,) | tf.float64 |
feature_216 | Tensor       | (None,) | tf.float64 |
feature_217 | Tensor       | (None,) | tf.float64 |
feature_218 | Tensor       | (None,) | tf.float64 |
feature_219 | Tensor       | (None,) | tf.float64 |
feature_22  | Tensor       | (None,) | tf.float64 |
feature_220 | Tensor       | (None,) | tf.float64 |
feature_23  | Tensor       | (None,) | tf.float64 |
feature_24  | Tensor       | (None,) | tf.float64 |
feature_25  | Tensor       | (None,) | tf.float64 |
feature_26  | Tensor       | (None,) | tf.float64 |
feature_27  | Tensor       | (None,) | tf.float64 |
feature_28  | Tensor       | (None,) | tf.float64 |
feature_29  | Tensor       | (None,) | tf.float64 |
feature_3   | Tensor       | (None,) | tf.float64 |
feature_30  | Tensor       | (None,) | tf.float64 |
feature_31  | Tensor       | (None,) | tf.float64 |
feature_32  | Tensor       | (None,) | tf.float64 |
feature_33  | Tensor       | (None,) | tf.float64 |
feature_34  | Tensor       | (None,) | tf.float64 |
feature_35  | Tensor       | (None,) | tf.float64 |
feature_36  | Tensor       | (None,) | tf.float64 |
feature_37  | Tensor       | (None,) | tf.float64 |
feature_38  | Tensor       | (None,) | tf.float64 |
feature_39  | Tensor       | (None,) | tf.float64 |
feature_4   | Tensor       | (None,) | tf.float64 |
feature_40  | Tensor       | (None,) | tf.float64 |
feature_41  | Tensor       | (None,) | tf.float64 |
feature_42  | Tensor       | (None,) | tf.float64 |
feature_43  | Tensor       | (None,) | tf.float64 |
feature_44  | Tensor       | (None,) | tf.float64 |
feature_45  | Tensor       | (None,) | tf.float64 |
feature_46  | Tensor       | (None,) | tf.float64 |
feature_47  | Tensor       | (None,) | tf.float64 |
feature_48  | Tensor       | (None,) | tf.float64 |
feature_49  | Tensor       | (None,) | tf.float64 |
feature_5   | Tensor       | (None,) | tf.float64 |
feature_50  | Tensor       | (None,) | tf.float64 |
feature_51  | Tensor       | (None,) | tf.float64 |
feature_52  | Tensor       | (None,) | tf.float64 |
feature_53  | Tensor       | (None,) | tf.float64 |
feature_54  | Tensor       | (None,) | tf.float64 |
feature_55  | Tensor       | (None,) | tf.float64 |
feature_56  | Tensor       | (None,) | tf.float64 |
feature_57  | Tensor       | (None,) | tf.float64 |
feature_58  | Tensor       | (None,) | tf.float64 |
feature_59  | Tensor       | (None,) | tf.float64 |
feature_6   | Tensor       | (None,) | tf.float64 |
feature_60  | Tensor       | (None,) | tf.float64 |
feature_61  | Tensor       | (None,) | tf.float64 |
feature_62  | Tensor       | (None,) | tf.float64 |
feature_63  | Tensor       | (None,) | tf.float64 |
feature_64  | Tensor       | (None,) | tf.float64 |
feature_65  | Tensor       | (None,) | tf.float64 |
feature_66  | Tensor       | (None,) | tf.float64 |
feature_67  | Tensor       | (None,) | tf.float64 |
feature_68  | Tensor       | (None,) | tf.float64 |
feature_69  | Tensor       | (None,) | tf.float64 |
feature_7   | Tensor       | (None,) | tf.float64 |
feature_70  | Tensor       | (None,) | tf.float64 |
feature_71  | Tensor       | (None,) | tf.float64 |
feature_72  | Tensor       | (None,) | tf.float64 |
feature_73  | Tensor       | (None,) | tf.float64 |
feature_74  | Tensor       | (None,) | tf.float64 |
feature_75  | Tensor       | (None,) | tf.float64 |
feature_76  | Tensor       | (None,) | tf.float64 |
feature_77  | Tensor       | (None,) | tf.float64 |
feature_78  | Tensor       | (None,) | tf.float64 |
feature_79  | Tensor       | (None,) | tf.float64 |
feature_8   | Tensor       | (None,) | tf.float64 |
feature_80  | Tensor       | (None,) | tf.float64 |
feature_81  | Tensor       | (None,) | tf.float64 |
feature_82  | Tensor       | (None,) | tf.float64 |
feature_83  | Tensor       | (None,) | tf.float64 |
feature_84  | Tensor       | (None,) | tf.float64 |
feature_85  | Tensor       | (None,) | tf.float64 |
feature_86  | Tensor       | (None,) | tf.float64 |
feature_87  | Tensor       | (None,) | tf.float64 |
feature_88  | Tensor       | (None,) | tf.float64 |
feature_89  | Tensor       | (None,) | tf.float64 |
feature_9   | Tensor       | (None,) | tf.float64 |
feature_90  | Tensor       | (None,) | tf.float64 |
feature_91  | Tensor       | (None,) | tf.float64 |
feature_92  | Tensor       | (None,) | tf.float64 |
feature_93  | Tensor       | (None,) | tf.float64 |
feature_94  | Tensor       | (None,) | tf.float64 |
feature_95  | Tensor       | (None,) | tf.float64 |
feature_96  | Tensor       | (None,) | tf.float64 |
feature_97  | Tensor       | (None,) | tf.float64 |
feature_98  | Tensor       | (None,) | tf.float64 |
feature_99  | Tensor       | (None,) | tf.float64 |
label       | Tensor       | (None,) | tf.float64 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Citation**:

```
@article{10.1145/2987380,
  author = {Dato, Domenico and Lucchese, Claudio and Nardini, Franco Maria and Orlando, Salvatore and Perego, Raffaele and Tonellotto, Nicola and Venturini, Rossano},
  title = {Fast Ranking with Additive Ensembles of Oblivious and Non-Oblivious Regression Trees},
  year = {2016},
  publisher = {ACM},
  address = {New York, NY, USA},
  volume = {35},
  number = {2},
  issn = {1046-8188},
  url = {https://doi.org/10.1145/2987380},
  doi = {10.1145/2987380},
  journal = {ACM Transactions on Information Systems},
  articleno = {15},
  numpages = {31},
}
```


## istella/main (default config)

*   **Download size**: `1.20 GiB`

*   **Dataset size**: `1.40 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 9,799
`'train'` | 23,219

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/istella-main-1.0.1.html";
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

## istella/s

*   **Download size**: `450.26 MiB`

*   **Dataset size**: `728.40 MiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 6,562
`'train'` | 19,245
`'vali'`  | 7,211

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/istella-s-1.0.1.html";
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

## istella/x

*   **Download size**: `4.42 GiB`

*   **Dataset size**: `2.06 GiB`

*   **Splits**:

Split     | Examples
:-------- | -------:
`'test'`  | 2,000
`'train'` | 6,000
`'vali'`  | 2,000

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/istella-x-1.0.1.html";
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