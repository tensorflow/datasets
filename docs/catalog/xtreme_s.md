<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="xtreme_s" />
  <meta itemprop="description" content="FLEURS is the speech version of the FLORES machine translation benchmark, covering 2000 n-way parallel sentences in n=102 languages.&#10;XTREME-S covers four task families: speech recognition, classification, speech-to-text translation and retrieval. Covering 102&#10;languages from 10+ language families, 3 different domains and 4&#10;task families, XTREME-S aims to simplify multilingual speech&#10;representation evaluation, as well as catalyze research in “universal” speech representation learning.&#10;&#10;In this version, only the FLEURS dataset is provided, which covers speech&#10;recognition and speech-to-text translation.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;xtreme_s&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/xtreme_s" />
  <meta itemprop="sameAs" content="https://arxiv.org/abs/2205.12446" />
  <meta itemprop="citation" content="@article{fleurs2022arxiv,&#10;  title = {FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech},&#10;  author = {Conneau, Alexis and Ma, Min and Khanuja, Simran and Zhang, Yu and Axelrod, Vera and Dalmia, Siddharth and Riesa, Jason and Rivera, Clara and Bapna, Ankur},&#10;  journal={arXiv preprint arXiv:2205.12446},&#10;  url = {https://arxiv.org/abs/2205.12446},&#10;  year = {2022},&#10;}&#10;@article{conneau2022xtreme,&#10;  title={XTREME-S: Evaluating Cross-lingual Speech Representations},&#10;  author={Conneau, Alexis and Bapna, Ankur and Zhang, Yu and Ma, Min and von Platen, Patrick and Lozhkov, Anton and Cherry, Colin and Jia, Ye and Rivera, Clara and Kale, Mihir and others},&#10;  journal={arXiv preprint arXiv:2203.10752},&#10;  year={2022}&#10;}" />
</div>

# `xtreme_s`


*   **Description**:

FLEURS is the speech version of the FLORES machine translation benchmark,
covering 2000 n-way parallel sentences in n=102 languages. XTREME-S covers four
task families: speech recognition, classification, speech-to-text translation
and retrieval. Covering 102 languages from 10+ language families, 3 different
domains and 4 task families, XTREME-S aims to simplify multilingual speech
representation evaluation, as well as catalyze research in “universal” speech
representation learning.

In this version, only the FLEURS dataset is provided, which covers speech
recognition and speech-to-text translation.

*   **Config description**: FLEURS is the speech version of the FLORES machine
    translation benchmark, covering 2000 n-way parallel sentences in n=102
    languages.

*   **Homepage**:
    [https://arxiv.org/abs/2205.12446](https://arxiv.org/abs/2205.12446)

*   **Source code**:
    [`tfds.audio.xtreme_s.XtremeS`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/xtreme_s/xtreme_s.py)

*   **Versions**:

    *   **`2.0.0`** (default): Initial release on TFDS, FLEURS-only. Named to
        match version 2.0.0 on huggingface which has the same FLEURS data (
        https://huggingface.co/datasets/google/xtreme_s).

*   **Feature structure**:

```python
FeaturesDict({
    'audio': Audio(shape=(None,), dtype=tf.int64),
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'id': Scalar(shape=(), dtype=tf.int32),
    'lang_group_id': ClassLabel(shape=(), dtype=tf.int64, num_classes=7),
    'lang_id': ClassLabel(shape=(), dtype=tf.int64, num_classes=102),
    'language': Text(shape=(), dtype=tf.string),
    'num_samples': Scalar(shape=(), dtype=tf.int32),
    'path': tf.string,
    'raw_transcription': Text(shape=(), dtype=tf.string),
    'transcription': Text(shape=(), dtype=tf.string),
})
```

*   **Feature documentation**:

Feature           | Class        | Shape   | Dtype     | Description
:---------------- | :----------- | :------ | :-------- | :----------
                  | FeaturesDict |         |           |
audio             | Audio        | (None,) | tf.int64  |
gender            | ClassLabel   |         | tf.int64  |
id                | Scalar       |         | tf.int32  | Source text identifier, consistent across all languages to keep n-way parallelism of translations. Since each transcription may be spoken by multiple speakers, within each language multiple examples will also share the same id.
lang_group_id     | ClassLabel   |         | tf.int64  |
lang_id           | ClassLabel   |         | tf.int64  |
language          | Text         |         | tf.string | Language encoded as lowercase, underscore-separatedversion of a BCP-47 tag.
num_samples       | Scalar       |         | tf.int32  | Total number of frames in the audio
path              | Tensor       |         | tf.string |
raw_transcription | Text         |         | tf.string | Raw Transcription from FLoRes.
transcription     | Text         |         | tf.string | Normalized transcription.

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('audio', 'transcription')`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):
    Missing.

*   **Citation**:

```
@article{fleurs2022arxiv,
  title = {FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech},
  author = {Conneau, Alexis and Ma, Min and Khanuja, Simran and Zhang, Yu and Axelrod, Vera and Dalmia, Siddharth and Riesa, Jason and Rivera, Clara and Bapna, Ankur},
  journal={arXiv preprint arXiv:2205.12446},
  url = {https://arxiv.org/abs/2205.12446},
  year = {2022},
}
@article{conneau2022xtreme,
  title={XTREME-S: Evaluating Cross-lingual Speech Representations},
  author={Conneau, Alexis and Bapna, Ankur and Zhang, Yu and Ma, Min and von Platen, Patrick and Lozhkov, Anton and Cherry, Colin and Jia, Ye and Rivera, Clara and Kale, Mihir and others},
  journal={arXiv preprint arXiv:2203.10752},
  year={2022}
}
```


## xtreme_s/fleurs.af_za (default config)

*   **Download size**: `877.09 MiB`

*   **Dataset size**: `1.91 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 264
`'train'`      | 1,032
`'validation'` | 198

## xtreme_s/fleurs.am_et

*   **Download size**: `2.18 GiB`

*   **Dataset size**: `4.92 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 516
`'train'`      | 3,163
`'validation'` | 223

## xtreme_s/fleurs.ar_eg

*   **Download size**: `1.42 GiB`

*   **Dataset size**: `3.06 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 428
`'train'`      | 2,104
`'validation'` | 295

## xtreme_s/fleurs.as_in

*   **Download size**: `2.67 GiB`

*   **Dataset size**: `5.73 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 984
`'train'`      | 2,812
`'validation'` | 418

## xtreme_s/fleurs.ast_es

*   **Download size**: `1.90 GiB`

*   **Dataset size**: `4.03 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 946
`'train'`      | 2,511
`'validation'` | 398

## xtreme_s/fleurs.az_az

*   **Download size**: `2.28 GiB`

*   **Dataset size**: `5.08 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 923
`'train'`      | 2,665
`'validation'` | 400

## xtreme_s/fleurs.be_by

*   **Download size**: `2.45 GiB`

*   **Dataset size**: `5.53 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 967
`'train'`      | 2,433
`'validation'` | 408

## xtreme_s/fleurs.bg_bg

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.bn_in

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.bs_ba

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.ca_es

*   **Download size**: `2.01 GiB`

*   **Dataset size**: `4.32 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 940
`'train'`      | 2,300
`'validation'` | 404

## xtreme_s/fleurs.ceb_ph

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.ckb_iq

*   **Download size**: `2.46 GiB`

*   **Dataset size**: `5.34 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 922
`'train'`      | 3,040
`'validation'` | 386

## xtreme_s/fleurs.cmn_hans_cn

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.cs_cz

*   **Download size**: `1.93 GiB`

*   **Dataset size**: `4.32 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 723
`'train'`      | 2,811
`'validation'` | 305

## xtreme_s/fleurs.cy_gb

*   **Download size**: `2.90 GiB`

*   **Dataset size**: `6.62 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,021
`'train'`      | 3,427
`'validation'` | 447

## xtreme_s/fleurs.da_dk

*   **Download size**: `1.82 GiB`

*   **Dataset size**: `4.17 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 930
`'train'`      | 2,465
`'validation'` | 395

## xtreme_s/fleurs.de_de

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.el_gr

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.en_us

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.es_419

*   **Download size**: `2.14 GiB`

*   **Dataset size**: `4.80 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 908
`'train'`      | 2,796
`'validation'` | 408

## xtreme_s/fleurs.et_ee

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.fa_ir

*   **Download size**: `2.87 GiB`

*   **Dataset size**: `6.34 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 871
`'train'`      | 3,101
`'validation'` | 369

## xtreme_s/fleurs.ff_sn

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.fi_fi

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.fil_ph

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.fr_fr

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.ga_ie

*   **Download size**: `2.78 GiB`

*   **Dataset size**: `6.24 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 842
`'train'`      | 2,845
`'validation'` | 369

## xtreme_s/fleurs.gl_es

*   **Download size**: `1.79 GiB`

*   **Dataset size**: `3.87 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 927
`'train'`      | 2,175
`'validation'` | 395

## xtreme_s/fleurs.gu_in

*   **Download size**: `2.33 GiB`

*   **Dataset size**: `4.97 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,000
`'train'`      | 3,145
`'validation'` | 432

## xtreme_s/fleurs.ha_ng

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.he_il

*   **Download size**: `2.22 GiB`

*   **Dataset size**: `4.60 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 792
`'train'`      | 3,242
`'validation'` | 328

## xtreme_s/fleurs.hi_in

*   **Download size**: `1.53 GiB`

*   **Dataset size**: `3.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 418
`'train'`      | 2,120
`'validation'` | 239

## xtreme_s/fleurs.hr_hr

*   **Download size**: `2.40 GiB`

*   **Dataset size**: `5.54 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 914
`'train'`      | 3,461
`'validation'` | 377

## xtreme_s/fleurs.hu_hu

*   **Download size**: `2.33 GiB`

*   **Dataset size**: `5.07 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 905
`'train'`      | 3,095
`'validation'` | 407

## xtreme_s/fleurs.hy_am

*   **Download size**: `2.30 GiB`

*   **Dataset size**: `5.23 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 932
`'train'`      | 3,053
`'validation'` | 395

## xtreme_s/fleurs.id_id

*   **Download size**: `2.21 GiB`

*   **Dataset size**: `4.69 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 687
`'train'`      | 2,579
`'validation'` | 350

## xtreme_s/fleurs.ig_ng

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.is_is

*   **Download size**: `559.65 MiB`

*   **Dataset size**: `1.16 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 46
`'train'`      | 926
`'validation'` | 36

## xtreme_s/fleurs.it_it

*   **Download size**: `2.41 GiB`

*   **Dataset size**: `5.19 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 865
`'train'`      | 3,030
`'validation'` | 391

## xtreme_s/fleurs.ja_jp

*   **Download size**: `1.83 GiB`

*   **Dataset size**: `3.94 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 650
`'train'`      | 2,292
`'validation'` | 266

## xtreme_s/fleurs.jv_id

*   **Download size**: `2.68 GiB`

*   **Dataset size**: `5.62 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 728
`'train'`      | 3,051
`'validation'` | 295

## xtreme_s/fleurs.ka_ge

*   **Download size**: `1.50 GiB`

*   **Dataset size**: `3.37 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 979
`'train'`      | 1,491
`'validation'` | 409

## xtreme_s/fleurs.kam_ke

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.kea_cv

*   **Download size**: `2.55 GiB`

*   **Dataset size**: `5.57 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 864
`'train'`      | 2,715
`'validation'` | 366

## xtreme_s/fleurs.kk_kz

*   **Download size**: `2.69 GiB`

*   **Dataset size**: `6.24 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 856
`'train'`      | 3,200
`'validation'` | 369

## xtreme_s/fleurs.km_kh

*   **Download size**: `1.88 GiB`

*   **Dataset size**: `4.26 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 771
`'train'`      | 1,675
`'validation'` | 326

## xtreme_s/fleurs.kn_in

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.ko_kr

*   **Download size**: `1.65 GiB`

*   **Dataset size**: `3.67 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 382
`'train'`      | 2,307
`'validation'` | 226

## xtreme_s/fleurs.ky_kg

*   **Download size**: `2.18 GiB`

*   **Dataset size**: `5.13 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 977
`'train'`      | 2,818
`'validation'` | 422

## xtreme_s/fleurs.lb_lu

*   **Download size**: `1.94 GiB`

*   **Dataset size**: `4.39 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 934
`'train'`      | 2,502
`'validation'` | 408

## xtreme_s/fleurs.lg_ug

*   **Download size**: `2.83 GiB`

*   **Dataset size**: `6.43 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 723
`'train'`      | 2,478
`'validation'` | 306

## xtreme_s/fleurs.ln_cd

*   **Download size**: `3.68 GiB`

*   **Dataset size**: `8.13 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 478
`'train'`      | 3,350
`'validation'` | 209

## xtreme_s/fleurs.lo_la

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.lt_lt

*   **Download size**: `2.24 GiB`

*   **Dataset size**: `5.03 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 986
`'train'`      | 2,937
`'validation'` | 416

## xtreme_s/fleurs.luo_ke

*   **Download size**: `1.87 GiB`

*   **Dataset size**: `4.18 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 256
`'train'`      | 2,384
`'validation'` | 102

## xtreme_s/fleurs.lv_lv

*   **Download size**: `1.74 GiB`

*   **Dataset size**: `3.84 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 851
`'train'`      | 2,110
`'validation'` | 356

## xtreme_s/fleurs.mi_nz

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.mk_mk

*   **Download size**: `1.91 GiB`

*   **Dataset size**: `4.23 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 973
`'train'`      | 2,337
`'validation'` | 415

## xtreme_s/fleurs.ml_in

*   **Download size**: `2.68 GiB`

*   **Dataset size**: `5.80 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 958
`'train'`      | 3,043
`'validation'` | 418

## xtreme_s/fleurs.mn_mn

*   **Download size**: `2.21 GiB`

*   **Dataset size**: `5.47 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 949
`'train'`      | 3,074
`'validation'` | 405

## xtreme_s/fleurs.mr_in

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.ms_my

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.mt_mt

*   **Download size**: `2.39 GiB`

*   **Dataset size**: `5.37 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 926
`'train'`      | 2,895
`'validation'` | 404

## xtreme_s/fleurs.my_mm

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.nb_no

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.ne_np

*   **Download size**: `2.47 GiB`

*   **Dataset size**: `5.39 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 726
`'train'`      | 3,332
`'validation'` | 305

## xtreme_s/fleurs.nl_nl

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.nso_za

*   **Download size**: `3.27 GiB`

*   **Dataset size**: `7.11 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 790
`'train'`      | 1,990
`'validation'` | 363

## xtreme_s/fleurs.ny_mw

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.oc_fr

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.om_et

*   **Download size**: `1.18 GiB`

*   **Dataset size**: `2.52 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 41
`'train'`      | 1,701
`'validation'` | 19

## xtreme_s/fleurs.or_in

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.pa_in

*   **Download size**: `1.58 GiB`

*   **Dataset size**: `3.34 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 574
`'train'`      | 1,923
`'validation'` | 251

## xtreme_s/fleurs.pl_pl

*   **Download size**: `1.95 GiB`

*   **Dataset size**: `4.39 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 758
`'train'`      | 2,841
`'validation'` | 338

## xtreme_s/fleurs.ps_af

*   **Download size**: `1.89 GiB`

*   **Dataset size**: `4.20 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 512
`'train'`      | 2,513
`'validation'` | 217

## xtreme_s/fleurs.pt_br

*   **Download size**: `2.50 GiB`

*   **Dataset size**: `5.43 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 919
`'train'`      | 2,793
`'validation'` | 386

## xtreme_s/fleurs.ro_ro

*   **Download size**: `2.39 GiB`

*   **Dataset size**: `5.09 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 883
`'train'`      | 2,891
`'validation'` | 387

## xtreme_s/fleurs.ru_ru

*   **Download size**: `1.92 GiB`

*   **Dataset size**: `4.25 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 775
`'train'`      | 2,562
`'validation'` | 356

## xtreme_s/fleurs.sd_in

*   **Download size**: `3.00 GiB`

*   **Dataset size**: `6.35 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 980
`'train'`      | 3,443
`'validation'` | 426

## xtreme_s/fleurs.sk_sk

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.sl_si

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.sn_zw

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.so_so

*   **Download size**: `3.13 GiB`

*   **Dataset size**: `6.93 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 1,019
`'train'`      | 3,149
`'validation'` | 432

## xtreme_s/fleurs.sr_rs

*   **Download size**: `2.36 GiB`

*   **Dataset size**: `5.04 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 700
`'train'`      | 2,944
`'validation'` | 290

## xtreme_s/fleurs.sv_se

*   **Download size**: `1.95 GiB`

*   **Dataset size**: `4.21 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 759
`'train'`      | 2,385
`'validation'` | 330

## xtreme_s/fleurs.sw_ke

*   **Download size**: `2.70 GiB`

*   **Dataset size**: `5.98 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 487
`'train'`      | 3,070
`'validation'` | 211

## xtreme_s/fleurs.ta_in

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.te_in

*   **Download size**: `1.81 GiB`

*   **Dataset size**: `3.86 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 472
`'train'`      | 2,302
`'validation'` | 311

## xtreme_s/fleurs.tg_tj

*   **Download size**: `1.79 GiB`

*   **Dataset size**: `4.26 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 600
`'train'`      | 2,298
`'validation'` | 240

## xtreme_s/fleurs.th_th

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.tr_tr

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.uk_ua

*   **Download size**: `2.01 GiB`

*   **Dataset size**: `4.44 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 750
`'train'`      | 2,810
`'validation'` | 325

## xtreme_s/fleurs.umb_ao

*   **Download size**: `2.58 GiB`

*   **Dataset size**: `5.55 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 379
`'train'`      | 1,597
`'validation'` | 135

## xtreme_s/fleurs.ur_pk

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.uz_uz

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.vi_vn

*   **Download size**: `2.21 GiB`

*   **Dataset size**: `4.88 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 857
`'train'`      | 2,994
`'validation'` | 361

## xtreme_s/fleurs.wo_sn

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.xh_za

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.yo_ng

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.yue_hant_hk

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

## xtreme_s/fleurs.zu_za

*   **Download size**: `3.15 GiB`

*   **Dataset size**: `7.27 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 854
`'train'`      | 2,858
`'validation'` | 354

## xtreme_s/fleurs.all

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:
