<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="common_voice" />
  <meta itemprop="description" content="Mozilla Common Voice Dataset&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;common_voice&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/common_voice" />
  <meta itemprop="sameAs" content="https://voice.mozilla.org/en/datasets" />
  <meta itemprop="citation" content="" />
</div>

# `common_voice`


Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

*   **Description**:

Mozilla Common Voice Dataset

*   **Homepage**:
    [https://voice.mozilla.org/en/datasets](https://voice.mozilla.org/en/datasets)

*   **Source code**:
    [`tfds.audio.CommonVoice`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/commonvoice.py)

*   **Versions**:

    *   `1.0.0`: Initial release.
    *   **`2.0.0`** (default)
        <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>:
        Updated to corpus 6.1 from 2020-12-11.

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
    'accent': Text(shape=(), dtype=tf.string),
    'age': Text(shape=(), dtype=tf.string),
    'client_id': Text(shape=(), dtype=tf.string),
    'downvotes': Scalar(shape=(), dtype=tf.int32),
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'segment': Text(shape=(), dtype=tf.string),
    'sentence': Text(shape=(), dtype=tf.string),
    'upvotes': Scalar(shape=(), dtype=tf.int32),
    'voice': Audio(shape=(None,), dtype=tf.int64),
})
```

*   **Feature documentation**:

Feature   | Class        | Shape   | Dtype     | Description
:-------- | :----------- | :------ | :-------- | :----------
          | FeaturesDict |         |           |
accent    | Text         |         | tf.string | Accent of the speaker, see https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts
age       | Text         |         | tf.string | Age bucket of the speaker (e.g. teens, or fourties), see https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts
client_id | Text         |         | tf.string | Hashed UUID of a given user
downvotes | Scalar       |         | tf.int32  | Number of people who said audio does not match text
gender    | ClassLabel   |         | tf.int64  | Gender of the speaker
segment   | Text         |         | tf.string | If sentence belongs to a custom dataset segment, it will be listed here
sentence  | Text         |         | tf.string | Supposed transcription of the audio
upvotes   | Scalar       |         | tf.int32  | Number of people who said audio matches the text
voice     | Audio        | (None,) | tf.int64  |

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


## common_voice/en (default config)

*   **Config description**: Language Code: en

## common_voice/ab <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: ab

## common_voice/ar <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: ar

## common_voice/as <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: as

## common_voice/br

*   **Config description**: Language Code: br

## common_voice/ca

*   **Config description**: Language Code: ca

## common_voice/cnh

*   **Config description**: Language Code: cnh

## common_voice/cs <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: cs

## common_voice/cv

*   **Config description**: Language Code: cv

## common_voice/cy

*   **Config description**: Language Code: cy

## common_voice/de

*   **Config description**: Language Code: de

## common_voice/dv <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: dv

## common_voice/el <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: el

## common_voice/eo

*   **Config description**: Language Code: eo

## common_voice/es <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: es

## common_voice/et <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: et

## common_voice/eu <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: eu

## common_voice/fa <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: fa

## common_voice/fi <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: fi

## common_voice/fr

*   **Config description**: Language Code: fr

## common_voice/fy-NL <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: fy-NL

## common_voice/ga-IE

*   **Config description**: Language Code: ga-IE

## common_voice/hi <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: hi

## common_voice/hsb <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: hsb

## common_voice/hu <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: hu

## common_voice/ia <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: ia

## common_voice/id <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: id

## common_voice/it

*   **Config description**: Language Code: it

## common_voice/ja <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: ja

## common_voice/ka <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: ka

## common_voice/kab

*   **Config description**: Language Code: kab

## common_voice/ky

*   **Config description**: Language Code: ky

## common_voice/lg <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: lg

## common_voice/lt <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: lt

## common_voice/lv <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: lv

## common_voice/mn <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: mn

## common_voice/mt <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: mt

## common_voice/nl

*   **Config description**: Language Code: nl

## common_voice/or <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: or

## common_voice/pa-IN <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: pa-IN

## common_voice/pl <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: pl

## common_voice/pt <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: pt

## common_voice/rm-sursilv <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: rm-sursilv

## common_voice/rm-vallader <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: rm-vallader

## common_voice/ro <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: ro

## common_voice/ru <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: ru

## common_voice/rw <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: rw

## common_voice/sah <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: sah

## common_voice/sl

*   **Config description**: Language Code: sl

## common_voice/sv-SE <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: sv-SE

## common_voice/ta <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: ta

## common_voice/th <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: th

## common_voice/tr

*   **Config description**: Language Code: tr

## common_voice/tt

*   **Config description**: Language Code: tt

## common_voice/uk <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: uk

## common_voice/vi <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: vi

## common_voice/vot <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: vot

## common_voice/zh-CN <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: zh-CN

## common_voice/zh-HK <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Config description**: Language Code: zh-HK

## common_voice/zh-TW

*   **Config description**: Language Code: zh-TW
