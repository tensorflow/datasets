<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="tedlium" />
  <meta itemprop="description" content="The TED-LIUM corpus is English-language TED talks, with transcriptions,&#10;sampled at 16kHz. It contains about 118 hours of speech.&#10;&#10;This is the TED-LIUM corpus release 1,&#10;licensed under Creative Commons BY-NC-ND 3.0&#10;(http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;tedlium&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/tedlium" />
  <meta itemprop="sameAs" content="https://www.openslr.org/7/" />
  <meta itemprop="citation" content="@inproceedings{rousseau2012tedlium,&#10;  title={TED-LIUM: an Automatic Speech Recognition dedicated corpus},&#10;  author={Rousseau, Anthony and Del{\&#x27;e}glise, Paul and Est{\`e}ve, Yannick},&#10;  booktitle={Conference on Language Resources and Evaluation (LREC)},&#10;  pages={125--129},&#10;  year={2012}&#10;}" />
</div>
# `tedlium`

Note: This dataset has been updated since the last stable release. The new
versions and config marked with
<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>
are only available in the `tfds-nightly` package.

*   **Source code**:
    [`tfds.audio.tedlium.Tedlium`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/audio/tedlium.py)
*   **Versions**:
    *   **`1.0.1`** (default): No release notes.
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No
*   **Features**:

```python
FeaturesDict({
    'gender': ClassLabel(shape=(), dtype=tf.int64, num_classes=3),
    'id': tf.string,
    'speaker_id': tf.string,
    'speech': Audio(shape=(None,), dtype=tf.int64),
    'text': Text(shape=(), dtype=tf.string),
})
```

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `('speech', 'text')`
*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:
    Not supported.

## tedlium/release1 (default config)<span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Description**:

The TED-LIUM corpus is English-language TED talks, with transcriptions, sampled
at 16kHz. It contains about 118 hours of speech.

This is the TED-LIUM corpus release 1, licensed under Creative Commons BY-NC-ND
3.0 (http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).

*   **Config description**: The TED-LIUM corpus is English-language TED talks,
    with transcriptions, sampled at 16kHz. It contains about 118 hours of
    speech.

        This is the TED-LIUM corpus release 1,
        licensed under Creative Commons BY-NC-ND 3.0
        (http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).

*   **Homepage**: [https://www.openslr.org/7/](https://www.openslr.org/7/)

*   **Download size**: `19.82 GiB`

*   **Dataset size**: `39.23 GiB`

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 1,469
'train'      | 56,803
'validation' | 591

*   **Citation**:

```
@inproceedings{rousseau2012tedlium,
  title={TED-LIUM: an Automatic Speech Recognition dedicated corpus},
  author={Rousseau, Anthony and Del{\'e}glise, Paul and Est{\`e}ve, Yannick},
  booktitle={Conference on Language Resources and Evaluation (LREC)},
  pages={125--129},
  year={2012}
}
```

## tedlium/release2 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Description**:

This is the TED-LIUM corpus release 2, licensed under Creative Commons BY-NC-ND
3.0 (http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).

All talks and text are property of TED Conferences LLC.

The TED-LIUM corpus was made from audio talks and their transcriptions available
on the TED website. We have prepared and filtered these data in order to train
acoustic models to participate to the International Workshop on Spoken Language
Translation 2011 (the LIUM English/French SLT system reached the first rank in
the SLT task).

Contains 1495 talks and transcripts.

*   **Config description**: This is the TED-LIUM corpus release 2, licensed
    under Creative Commons BY-NC-ND 3.0
    (http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en).

        All talks and text are property of TED Conferences LLC.

        The TED-LIUM corpus was made from audio talks and their transcriptions
        available on the TED website. We have prepared and filtered these data
        in order to train acoustic models to participate to the International
        Workshop on Spoken Language Translation 2011 (the LIUM English/French
        SLT system reached the first rank in the SLT task).

        Contains 1495 talks and transcripts.

*   **Homepage**: [https://www.openslr.org/19/](https://www.openslr.org/19/)

*   **Download size**: `34.26 GiB`

*   **Dataset size**: `67.04 GiB`

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 1,469
'train'      | 92,973
'validation' | 591

*   **Citation**:

```
@inproceedings{rousseau2014tedlium2,
  title={Enhancing the {TED-LIUM} Corpus with Selected Data for Language Modeling and More {TED} Talks},
  author={Rousseau, Anthony and Del{\'e}glise, Paul and Est{\`e}ve, Yannick},
  booktitle={Conference on Language Resources and Evaluation (LREC)},
  year={2014}
}
```

## tedlium/release3 <span class="material-icons" title="Available only in the tfds-nightly package">nights_stay</span>

*   **Description**:

This is the TED-LIUM corpus release 3, licensed under Creative Commons BY-NC-ND
3.0.

All talks and text are property of TED Conferences LLC.

This new TED-LIUM release was made through a collaboration between the Ubiqus
company and the LIUM (University of Le Mans, France)

Contents:

-   2351 audio talks in NIST sphere format (SPH), including talks from TED-LIUM
    2: be careful, same talks but not same audio files (only these audio file
    must be used with the TED-LIUM 3 STM files)
-   452 hours of audio
-   2351 aligned automatic transcripts in STM format
-   TEDLIUM 2 dev and test data: 19 TED talks in SPH format with corresponding
    manual transcriptions (cf. 'legacy' distribution below).
-   Dictionary with pronunciations (159848 entries), same file as the one
    included in TED-LIUM 2
-   Selected monolingual data for language modeling from WMT12 publicly
    available corpora: these files come from the TED-LIUM 2 release, but have
    been modified to get a tokenization more relevant for English language

Two corpus distributions: - the legacy one, on which the dev and test datasets
are the same as in TED-LIUM 2 (and TED-LIUM 1). - the 'speaker adaptation' one,
especially designed for experiments on speaker adaptation.

*   **Config description**: This is the TED-LIUM corpus release 3, licensed
    under Creative Commons BY-NC-ND 3.0.

        All talks and text are property of TED Conferences LLC.

        This new TED-LIUM release was made through a collaboration between the
        Ubiqus company and the LIUM (University of Le Mans, France)

        Contents:

        - 2351 audio talks in NIST sphere format (SPH), including talks from
          TED-LIUM 2: be careful, same talks but not same audio files (only
          these audio file must be used with the TED-LIUM 3 STM files)
        - 452 hours of audio
        - 2351 aligned automatic transcripts in STM format
        - TEDLIUM 2 dev and test data: 19 TED talks in SPH format with
          corresponding manual transcriptions (cf. 'legacy' distribution below).
        - Dictionary with pronunciations (159848 entries), same file as the one
          included in TED-LIUM 2
        - Selected monolingual data for language modeling from WMT12 publicly
          available corpora: these files come from the TED-LIUM 2 release, but
          have been modified to get a tokenization more relevant for English
          language

        Two corpus distributions:
        - the legacy one, on which the dev and test datasets are the same as in
          TED-LIUM 2 (and TED-LIUM 1).
        - the 'speaker adaptation' one, especially designed for experiments on
          speaker adaptation.

*   **Homepage**: [https://www.openslr.org/51/](https://www.openslr.org/51/)

*   **Download size**: `50.59 GiB`

*   **Dataset size**: `145.67 GiB`

*   **Splits**:

Split        | Examples
:----------- | -------:
'test'       | 1,469
'train'      | 268,263
'validation' | 591

*   **Citation**:

```
@inproceedings{hernandez2018tedlium3,
  title={TED-LIUM 3: twice as much data and corpus repartition for experiments on speaker adaptation},
  author={Hernandez, Fran{\c{c}}ois and Nguyen, Vincent and Ghannay, Sahar and Tomashenko, Natalia and Est{\`e}ve, Yannick},
  booktitle={International Conference on Speech and Computer},
  pages={198--208},
  year={2018},
  organization={Springer}
}
```
