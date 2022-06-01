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

*   **Download size**: `Unknown size`

*   **Dataset size**: `Unknown size`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    Unknown

*   **Splits**:

Split | Examples
:---- | -------:

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

## xtreme_s/fleurs.am_et

## xtreme_s/fleurs.ar_eg

## xtreme_s/fleurs.as_in

## xtreme_s/fleurs.ast_es

## xtreme_s/fleurs.az_az

## xtreme_s/fleurs.be_by

## xtreme_s/fleurs.bg_bg

## xtreme_s/fleurs.bn_in

## xtreme_s/fleurs.bs_ba

## xtreme_s/fleurs.ca_es

## xtreme_s/fleurs.ceb_ph

## xtreme_s/fleurs.ckb_iq

## xtreme_s/fleurs.cmn_hans_cn

## xtreme_s/fleurs.cs_cz

## xtreme_s/fleurs.cy_gb

## xtreme_s/fleurs.da_dk

## xtreme_s/fleurs.de_de

## xtreme_s/fleurs.el_gr

## xtreme_s/fleurs.en_us

## xtreme_s/fleurs.es_419

## xtreme_s/fleurs.et_ee

## xtreme_s/fleurs.fa_ir

## xtreme_s/fleurs.ff_sn

## xtreme_s/fleurs.fi_fi

## xtreme_s/fleurs.fil_ph

## xtreme_s/fleurs.fr_fr

## xtreme_s/fleurs.ga_ie

## xtreme_s/fleurs.gl_es

## xtreme_s/fleurs.gu_in

## xtreme_s/fleurs.ha_ng

## xtreme_s/fleurs.he_il

## xtreme_s/fleurs.hi_in

## xtreme_s/fleurs.hr_hr

## xtreme_s/fleurs.hu_hu

## xtreme_s/fleurs.hy_am

## xtreme_s/fleurs.id_id

## xtreme_s/fleurs.ig_ng

## xtreme_s/fleurs.is_is

## xtreme_s/fleurs.it_it

## xtreme_s/fleurs.ja_jp

## xtreme_s/fleurs.jv_id

## xtreme_s/fleurs.ka_ge

## xtreme_s/fleurs.kam_ke

## xtreme_s/fleurs.kea_cv

## xtreme_s/fleurs.kk_kz

## xtreme_s/fleurs.km_kh

## xtreme_s/fleurs.kn_in

## xtreme_s/fleurs.ko_kr

## xtreme_s/fleurs.ky_kg

## xtreme_s/fleurs.lb_lu

## xtreme_s/fleurs.lg_ug

## xtreme_s/fleurs.ln_cd

## xtreme_s/fleurs.lo_la

## xtreme_s/fleurs.lt_lt

## xtreme_s/fleurs.luo_ke

## xtreme_s/fleurs.lv_lv

## xtreme_s/fleurs.mi_nz

## xtreme_s/fleurs.mk_mk

## xtreme_s/fleurs.ml_in

## xtreme_s/fleurs.mn_mn

## xtreme_s/fleurs.mr_in

## xtreme_s/fleurs.ms_my

## xtreme_s/fleurs.mt_mt

## xtreme_s/fleurs.my_mm

## xtreme_s/fleurs.nb_no

## xtreme_s/fleurs.ne_np

## xtreme_s/fleurs.nl_nl

## xtreme_s/fleurs.nso_za

## xtreme_s/fleurs.ny_mw

## xtreme_s/fleurs.oc_fr

## xtreme_s/fleurs.om_et

## xtreme_s/fleurs.or_in

## xtreme_s/fleurs.pa_in

## xtreme_s/fleurs.pl_pl

## xtreme_s/fleurs.ps_af

## xtreme_s/fleurs.pt_br

## xtreme_s/fleurs.ro_ro

## xtreme_s/fleurs.ru_ru

## xtreme_s/fleurs.sd_in

## xtreme_s/fleurs.sk_sk

## xtreme_s/fleurs.sl_si

## xtreme_s/fleurs.sn_zw

## xtreme_s/fleurs.so_so

## xtreme_s/fleurs.sr_rs

## xtreme_s/fleurs.sv_se

## xtreme_s/fleurs.sw_ke

## xtreme_s/fleurs.ta_in

## xtreme_s/fleurs.te_in

## xtreme_s/fleurs.tg_tj

## xtreme_s/fleurs.th_th

## xtreme_s/fleurs.tr_tr

## xtreme_s/fleurs.uk_ua

## xtreme_s/fleurs.umb_ao

## xtreme_s/fleurs.ur_pk

## xtreme_s/fleurs.uz_uz

## xtreme_s/fleurs.vi_vn

## xtreme_s/fleurs.wo_sn

## xtreme_s/fleurs.xh_za

## xtreme_s/fleurs.yo_ng

## xtreme_s/fleurs.yue_hant_hk

## xtreme_s/fleurs.zu_za

## xtreme_s/fleurs.all
