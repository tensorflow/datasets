# harem

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/harem)
*   [Huggingface](https://huggingface.co/datasets/harem)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:harem')
```

*   **Description**:

```
The HAREM is a Portuguese language corpus commonly used for Named Entity Recognition tasks. It includes about 93k words, from 129 different texts,
from several genres, and language varieties. The split of this dataset version follows the division made by [1], where 7% HAREM
documents are the validation set and the miniHAREM corpus (with about 65k words) is the test set. There are two versions of the dataset set,
a version that has a total of 10 different named entity classes (Person, Organization, Location, Value, Date, Title, Thing, Event,
Abstraction, and Other) and a "selective" version with only 5 classes (Person, Organization, Location, Value, and Date).

It's important to note that the original version of the HAREM dataset has 2 levels of NER details, namely "Category" and "Sub-type".
The dataset version processed here ONLY USE the "Category" level of the original dataset.

[1] Souza, Fábio, Rodrigo Nogueira, and Roberto Lotufo. "BERTimbau: Pretrained BERT Models for Brazilian Portuguese." Brazilian Conference on Intelligent Systems. Springer, Cham, 2020.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 128
`'train'` | 121
`'validation'` | 8

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 21,
            "names": [
                "O",
                "B-PESSOA",
                "I-PESSOA",
                "B-ORGANIZACAO",
                "I-ORGANIZACAO",
                "B-LOCAL",
                "I-LOCAL",
                "B-TEMPO",
                "I-TEMPO",
                "B-VALOR",
                "I-VALOR",
                "B-ABSTRACCAO",
                "I-ABSTRACCAO",
                "B-ACONTECIMENTO",
                "I-ACONTECIMENTO",
                "B-COISA",
                "I-COISA",
                "B-OBRA",
                "I-OBRA",
                "B-OUTRO",
                "I-OUTRO"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## selective


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:harem/selective')
```

*   **Description**:

```
The HAREM is a Portuguese language corpus commonly used for Named Entity Recognition tasks. It includes about 93k words, from 129 different texts,
from several genres, and language varieties. The split of this dataset version follows the division made by [1], where 7% HAREM
documents are the validation set and the miniHAREM corpus (with about 65k words) is the test set. There are two versions of the dataset set,
a version that has a total of 10 different named entity classes (Person, Organization, Location, Value, Date, Title, Thing, Event,
Abstraction, and Other) and a "selective" version with only 5 classes (Person, Organization, Location, Value, and Date).

It's important to note that the original version of the HAREM dataset has 2 levels of NER details, namely "Category" and "Sub-type".
The dataset version processed here ONLY USE the "Category" level of the original dataset.

[1] Souza, Fábio, Rodrigo Nogueira, and Roberto Lotufo. "BERTimbau: Pretrained BERT Models for Brazilian Portuguese." Brazilian Conference on Intelligent Systems. Springer, Cham, 2020.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 128
`'train'` | 121
`'validation'` | 8

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 11,
            "names": [
                "O",
                "B-PESSOA",
                "I-PESSOA",
                "B-ORGANIZACAO",
                "I-ORGANIZACAO",
                "B-LOCAL",
                "I-LOCAL",
                "B-TEMPO",
                "I-TEMPO",
                "B-VALOR",
                "I-VALOR"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


