# snow_simplified_japanese_corpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/snow_simplified_japanese_corpus)
*   [Huggingface](https://huggingface.co/datasets/snow_simplified_japanese_corpus)


## snow_t15


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:snow_simplified_japanese_corpus/snow_t15')
```

*   **Description**:

```
About SNOW T15: The simplified corpus for the Japanese language. The corpus has 50,000 manually simplified and aligned sentences. This corpus contains the original sentences, simplified sentences and English translation of the original sentences. It can be used for automatic text simplification as well as translating simple Japanese into English and vice-versa. The core vocabulary is restricted to 2,000 words where it is selected by accounting for several factors such as meaning preservation, variation, simplicity and the UniDic word segmentation criterion.
For details, refer to the explanation page of Japanese simplification (http://www.jnlp.org/research/Japanese_simplification). The original texts are from "small_parallel_enja: 50k En/Ja Parallel Corpus for Testing SMT Methods", which is a bilingual corpus for machine translation. About SNOW T23: An expansion corpus of 35,000 sentences rewritten in easy Japanese (simple Japanese vocabulary) based on SNOW T15. The original texts are from "Tanaka Corpus" (http://www.edrdg.org/wiki/index.php/Tanaka_Corpus).
```

*   **License**: CC BY 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 50000

*   **Features**:

```json
{
    "ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_ja": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simplified_ja": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_en": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## snow_t23


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:snow_simplified_japanese_corpus/snow_t23')
```

*   **Description**:

```
About SNOW T15: The simplified corpus for the Japanese language. The corpus has 50,000 manually simplified and aligned sentences. This corpus contains the original sentences, simplified sentences and English translation of the original sentences. It can be used for automatic text simplification as well as translating simple Japanese into English and vice-versa. The core vocabulary is restricted to 2,000 words where it is selected by accounting for several factors such as meaning preservation, variation, simplicity and the UniDic word segmentation criterion.
For details, refer to the explanation page of Japanese simplification (http://www.jnlp.org/research/Japanese_simplification). The original texts are from "small_parallel_enja: 50k En/Ja Parallel Corpus for Testing SMT Methods", which is a bilingual corpus for machine translation. About SNOW T23: An expansion corpus of 35,000 sentences rewritten in easy Japanese (simple Japanese vocabulary) based on SNOW T15. The original texts are from "Tanaka Corpus" (http://www.edrdg.org/wiki/index.php/Tanaka_Corpus).
```

*   **License**: CC BY 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 34300

*   **Features**:

```json
{
    "ID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_ja": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simplified_ja": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_en": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "proper_noun": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


