# indonlu

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/indonlu)
*   [Huggingface](https://huggingface.co/datasets/indonlu)


## emot


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/emot')
```

*   **Description**:

```
An emotion classification dataset collected from the social media
platform Twitter (Saputri et al., 2018). The dataset consists of
around 4000 Indonesian colloquial language tweets, covering five
different emotion labels: sadness, anger, love, fear, and happy.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 440
`'train'` | 3521
`'validation'` | 440

*   **Features**:

```json
{
    "tweet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 5,
        "names": [
            "sadness",
            "anger",
            "love",
            "fear",
            "happy"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## smsa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/smsa')
```

*   **Description**:

```
This sentence-level sentiment analysis dataset (Purwarianti and Crisdayanti, 2019)
is a collection of comments and reviews in Indonesian obtained from multiple online
platforms. The text was crawled and then annotated by several Indonesian linguists
to construct this dataset. There are three possible sentiments on the SmSA
dataset: positive, negative, and neutral.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'train'` | 11000
`'validation'` | 1260

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "positive",
            "neutral",
            "negative"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## casa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/casa')
```

*   **Description**:

```
An aspect-based sentiment analysis dataset consisting of around a thousand car reviews collected
from multiple Indonesian online automobile platforms (Ilmania et al., 2018). The dataset covers
six aspects of car quality. We define the task to be a multi-label classification task, where
each label represents a sentiment for a single aspect with three possible values: positive,
negative, and neutral.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 180
`'train'` | 810
`'validation'` | 90

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fuel": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "machine": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "others": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "part": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "price": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "service": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## hoasa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/hoasa')
```

*   **Description**:

```
An aspect-based sentiment analysis dataset consisting of hotel reviews collected from the hotel
aggregator platform, AiryRooms (Azhar et al., 2019). The dataset covers ten different aspects of
hotel quality. Each review is labeled with a single sentiment label for each aspect. There are
four possible sentiment classes for each sentiment label: positive, negative, neutral, and
positive-negative. The positivenegative label is given to a review that contains multiple sentiments
of the same aspect but for different objects (e.g., cleanliness of bed and toilet).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 286
`'train'` | 2283
`'validation'` | 285

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ac": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "air_panas": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "bau": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "general": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "kebersihan": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "linen": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "service": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "sunrise_meal": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "tv": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "wifi": {
        "num_classes": 4,
        "names": [
            "neg",
            "neut",
            "pos",
            "neg_pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## wrete


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/wrete')
```

*   **Description**:

```
The Wiki Revision Edits Textual Entailment dataset (Setya and Mahendra, 2018) consists of 450 sentence pairs
constructed from Wikipedia revision history. The dataset contains pairs of sentences and binary semantic
relations between the pairs. The data are labeled as entailed when the meaning of the second sentence can be
derived from the first one, and not entailed otherwise.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 100
`'train'` | 300
`'validation'` | 50

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "NotEntail",
            "Entail_or_Paraphrase"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## posp


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/posp')
```

*   **Description**:

```
This Indonesian part-of-speech tagging (POS) dataset (Hoesen and Purwarianti, 2018) is collected from Indonesian
news websites. The dataset consists of around 8000 sentences with 26 POS tags. The POS tag labels follow the
Indonesian Association of Computational Linguistics (INACL) POS Tagging Convention.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 840
`'train'` | 6720
`'validation'` | 840

*   **Features**:

```json
{
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
    "pos_tags": {
        "feature": {
            "num_classes": 26,
            "names": [
                "B-PPO",
                "B-KUA",
                "B-ADV",
                "B-PRN",
                "B-VBI",
                "B-PAR",
                "B-VBP",
                "B-NNP",
                "B-UNS",
                "B-VBT",
                "B-VBL",
                "B-NNO",
                "B-ADJ",
                "B-PRR",
                "B-PRK",
                "B-CCN",
                "B-$$$",
                "B-ADK",
                "B-ART",
                "B-CSN",
                "B-NUM",
                "B-SYM",
                "B-INT",
                "B-NEG",
                "B-PRI",
                "B-VBE"
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



## bapos


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/bapos')
```

*   **Description**:

```
This POS tagging dataset (Dinakaramani et al., 2014) contains about 1000 sentences, collected from the PAN Localization
Project. In this dataset, each word is tagged by one of 23 POS tag classes. Data splitting used in this benchmark follows
the experimental setting used by Kurniawan and Aji (2018)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1029
`'train'` | 8000
`'validation'` | 1000

*   **Features**:

```json
{
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
    "pos_tags": {
        "feature": {
            "num_classes": 41,
            "names": [
                "B-PR",
                "B-CD",
                "I-PR",
                "B-SYM",
                "B-JJ",
                "B-DT",
                "I-UH",
                "I-NND",
                "B-SC",
                "I-WH",
                "I-IN",
                "I-NNP",
                "I-VB",
                "B-IN",
                "B-NND",
                "I-CD",
                "I-JJ",
                "I-X",
                "B-OD",
                "B-RP",
                "B-RB",
                "B-NNP",
                "I-RB",
                "I-Z",
                "B-CC",
                "B-NEG",
                "B-VB",
                "B-NN",
                "B-MD",
                "B-UH",
                "I-NN",
                "B-PRP",
                "I-SC",
                "B-Z",
                "I-PRP",
                "I-OD",
                "I-SYM",
                "B-WH",
                "B-FW",
                "I-CC",
                "B-X"
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



## terma


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/terma')
```

*   **Description**:

```
This span-extraction dataset is collected from the hotel aggregator platform, AiryRooms (Septiandri and Sutiono, 2019;
Fernando et al., 2019). The dataset consists of thousands of hotel reviews, which each contain a span label for aspect
and sentiment words representing the opinion of the reviewer on the corresponding aspect. The labels use
Inside-Outside-Beginning (IOB) tagging representation with two kinds of tags, aspect and sentiment.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 3000
`'validation'` | 1000

*   **Features**:

```json
{
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
    "seq_label": {
        "feature": {
            "num_classes": 5,
            "names": [
                "I-SENTIMENT",
                "O",
                "I-ASPECT",
                "B-SENTIMENT",
                "B-ASPECT"
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



## keps


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/keps')
```

*   **Description**:

```
This keyphrase extraction dataset (Mahfuzh et al., 2019) consists of text from Twitter discussing
banking products and services and is written in the Indonesian language. A phrase containing
important information is considered a keyphrase. Text may contain one or more keyphrases since
important phrases can be located at different positions. The dataset follows the IOB chunking format,
which represents the position of the keyphrase.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 247
`'train'` | 800
`'validation'` | 200

*   **Features**:

```json
{
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
    "seq_label": {
        "feature": {
            "num_classes": 3,
            "names": [
                "O",
                "B",
                "I"
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



## nergrit


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/nergrit')
```

*   **Description**:

```
This NER dataset is taken from the Grit-ID repository, and the labels are spans in IOB chunking representation.
The dataset consists of three kinds of named entity tags, PERSON (name of person), PLACE (name of location), and
ORGANIZATION (name of organization).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 209
`'train'` | 1672
`'validation'` | 209

*   **Features**:

```json
{
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
            "num_classes": 7,
            "names": [
                "I-PERSON",
                "B-ORGANISATION",
                "I-ORGANISATION",
                "B-PLACE",
                "I-PLACE",
                "O",
                "B-PERSON"
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



## nerp


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/nerp')
```

*   **Description**:

```
This NER dataset (Hoesen and Purwarianti, 2018) contains texts collected from several Indonesian news websites.
There are five labels available in this dataset, PER (name of person), LOC (name of location), IND (name of product or brand),
EVT (name of the event), and FNB (name of food and beverage). The NERP dataset uses the IOB chunking format.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 840
`'train'` | 6720
`'validation'` | 840

*   **Features**:

```json
{
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
                "I-PPL",
                "B-EVT",
                "B-PLC",
                "I-IND",
                "B-IND",
                "B-FNB",
                "I-EVT",
                "B-PPL",
                "I-PLC",
                "O",
                "I-FNB"
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



## facqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonlu/facqa')
```

*   **Description**:

```
The goal of the FacQA dataset is to find the answer to a question from a provided short passage from
a news article (Purwarianti et al., 2007). Each row in the FacQA dataset consists of a question,
a short passage, and a label phrase, which can be found inside the corresponding short passage.
There are six categories of questions: date, location, name, organization, person, and quantitative.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 311
`'train'` | 2495
`'validation'` | 311

*   **Features**:

```json
{
    "question": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "passage": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "seq_label": {
        "feature": {
            "num_classes": 3,
            "names": [
                "O",
                "B",
                "I"
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


