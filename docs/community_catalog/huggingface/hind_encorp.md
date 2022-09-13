# hind_encorp

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hind_encorp)
*   [Huggingface](https://huggingface.co/datasets/hind_encorp)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hind_encorp')
```

*   **Description**:

```
HindEnCorp parallel texts (sentence-aligned) come from the following sources:
Tides, which contains 50K sentence pairs taken mainly from news articles. This dataset was originally col- lected for the DARPA-TIDES surprise-language con- test in 2002, later refined at IIIT Hyderabad and provided for the NLP Tools Contest at ICON 2008 (Venkatapathy, 2008).

Commentaries by Daniel Pipes contain 322 articles in English written by a journalist Daniel Pipes and translated into Hindi.

EMILLE. This corpus (Baker et al., 2002) consists of three components: monolingual, parallel and annotated corpora. There are fourteen monolingual sub- corpora, including both written and (for some lan- guages) spoken data for fourteen South Asian lan- guages. The EMILLE monolingual corpora contain in total 92,799,000 words (including 2,627,000 words of transcribed spoken data for Bengali, Gujarati, Hindi, Punjabi and Urdu). The parallel corpus consists of 200,000 words of text in English and its accompanying translations into Hindi and other languages.

Smaller datasets as collected by Bojar et al. (2010) include the corpus used at ACL 2005 (a subcorpus of EMILLE), a corpus of named entities from Wikipedia (crawled in 2009), and Agriculture domain parallel corpus.
￼
For the current release, we are extending the parallel corpus using these sources:
Intercorp (Čermák and Rosen,2012) is a large multilingual parallel corpus of 32 languages including Hindi. The central language used for alignment is Czech. Intercorp’s core texts amount to 202 million words. These core texts are most suitable for us because their sentence alignment is manually checked and therefore very reliable. They cover predominately short sto- ries and novels. There are seven Hindi texts in Inter- corp. Unfortunately, only for three of them the English translation is available; the other four are aligned only with Czech texts. The Hindi subcorpus of Intercorp contains 118,000 words in Hindi.

TED talks 3 held in various languages, primarily English, are equipped with transcripts and these are translated into 102 languages. There are 179 talks for which Hindi translation is available.

The Indic multi-parallel corpus (Birch et al., 2011; Post et al., 2012) is a corpus of texts from Wikipedia translated from the respective Indian language into English by non-expert translators hired over Mechanical Turk. The quality is thus somewhat mixed in many respects starting from typesetting and punctuation over capi- talization, spelling, word choice to sentence structure. A little bit of control could be in principle obtained from the fact that every input sentence was translated 4 times. We used the 2012 release of the corpus.

Launchpad.net is a software collaboration platform that hosts many open-source projects and facilitates also collaborative localization of the tools. We downloaded all revisions of all the hosted projects and extracted the localization (.po) files.

Other smaller datasets. This time, we added Wikipedia entities as crawled in 2013 (including any morphological variants of the named entitity that appears on the Hindi variant of the Wikipedia page) and words, word examples and quotes from the Shabdkosh online dictionary.
```

*   **License**: CC BY-NC-SA 3.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 273885

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "alignment_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "alignment_quality": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "hi"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


