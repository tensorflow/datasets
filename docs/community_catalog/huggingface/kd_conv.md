# kd_conv

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kd_conv)
*   [Huggingface](https://huggingface.co/datasets/kd_conv)


## travel_dialogues


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kd_conv/travel_dialogues')
```

*   **Description**:

```
KdConv is a Chinese multi-domain Knowledge-driven Conversionsation dataset, grounding the topics in multi-turn conversations to knowledge graphs. KdConv contains 4.5K conversations from three domains (film, music, and travel), and 86K utterances with an average turn number of 19.0. These conversations contain in-depth discussions on related topics and natural transition between multiple topics, while the corpus can also used for exploration of transfer learning and domain adaptation.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 150
`'train'` | 1200
`'validation'` | 150

*   **Features**:

```json
{
    "messages": {
        "feature": {
            "message": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "attrs": {
                "feature": {
                    "attrname": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "attrvalue": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "name": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## travel_knowledge_base


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kd_conv/travel_knowledge_base')
```

*   **Description**:

```
KdConv is a Chinese multi-domain Knowledge-driven Conversionsation dataset, grounding the topics in multi-turn conversations to knowledge graphs. KdConv contains 4.5K conversations from three domains (film, music, and travel), and 86K utterances with an average turn number of 19.0. These conversations contain in-depth discussions on related topics and natural transition between multiple topics, while the corpus can also used for exploration of transfer learning and domain adaptation.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1154

*   **Features**:

```json
{
    "head_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "kb_triplets": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## music_dialogues


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kd_conv/music_dialogues')
```

*   **Description**:

```
KdConv is a Chinese multi-domain Knowledge-driven Conversionsation dataset, grounding the topics in multi-turn conversations to knowledge graphs. KdConv contains 4.5K conversations from three domains (film, music, and travel), and 86K utterances with an average turn number of 19.0. These conversations contain in-depth discussions on related topics and natural transition between multiple topics, while the corpus can also used for exploration of transfer learning and domain adaptation.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 150
`'train'` | 1200
`'validation'` | 150

*   **Features**:

```json
{
    "messages": {
        "feature": {
            "message": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "attrs": {
                "feature": {
                    "attrname": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "attrvalue": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "name": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## music_knowledge_base


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kd_conv/music_knowledge_base')
```

*   **Description**:

```
KdConv is a Chinese multi-domain Knowledge-driven Conversionsation dataset, grounding the topics in multi-turn conversations to knowledge graphs. KdConv contains 4.5K conversations from three domains (film, music, and travel), and 86K utterances with an average turn number of 19.0. These conversations contain in-depth discussions on related topics and natural transition between multiple topics, while the corpus can also used for exploration of transfer learning and domain adaptation.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4441

*   **Features**:

```json
{
    "head_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "kb_triplets": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## film_dialogues


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kd_conv/film_dialogues')
```

*   **Description**:

```
KdConv is a Chinese multi-domain Knowledge-driven Conversionsation dataset, grounding the topics in multi-turn conversations to knowledge graphs. KdConv contains 4.5K conversations from three domains (film, music, and travel), and 86K utterances with an average turn number of 19.0. These conversations contain in-depth discussions on related topics and natural transition between multiple topics, while the corpus can also used for exploration of transfer learning and domain adaptation.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 150
`'train'` | 1200
`'validation'` | 150

*   **Features**:

```json
{
    "messages": {
        "feature": {
            "message": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "attrs": {
                "feature": {
                    "attrname": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "attrvalue": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "name": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## film_knowledge_base


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kd_conv/film_knowledge_base')
```

*   **Description**:

```
KdConv is a Chinese multi-domain Knowledge-driven Conversionsation dataset, grounding the topics in multi-turn conversations to knowledge graphs. KdConv contains 4.5K conversations from three domains (film, music, and travel), and 86K utterances with an average turn number of 19.0. These conversations contain in-depth discussions on related topics and natural transition between multiple topics, while the corpus can also used for exploration of transfer learning and domain adaptation.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 8090

*   **Features**:

```json
{
    "head_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "kb_triplets": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## all_dialogues


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kd_conv/all_dialogues')
```

*   **Description**:

```
KdConv is a Chinese multi-domain Knowledge-driven Conversionsation dataset, grounding the topics in multi-turn conversations to knowledge graphs. KdConv contains 4.5K conversations from three domains (film, music, and travel), and 86K utterances with an average turn number of 19.0. These conversations contain in-depth discussions on related topics and natural transition between multiple topics, while the corpus can also used for exploration of transfer learning and domain adaptation.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 450
`'train'` | 3600
`'validation'` | 450

*   **Features**:

```json
{
    "messages": {
        "feature": {
            "message": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "attrs": {
                "feature": {
                    "attrname": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "attrvalue": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    },
                    "name": {
                        "dtype": "string",
                        "id": null,
                        "_type": "Value"
                    }
                },
                "length": -1,
                "id": null,
                "_type": "Sequence"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## all_knowledge_base


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kd_conv/all_knowledge_base')
```

*   **Description**:

```
KdConv is a Chinese multi-domain Knowledge-driven Conversionsation dataset, grounding the topics in multi-turn conversations to knowledge graphs. KdConv contains 4.5K conversations from three domains (film, music, and travel), and 86K utterances with an average turn number of 19.0. These conversations contain in-depth discussions on related topics and natural transition between multiple topics, while the corpus can also used for exploration of transfer learning and domain adaptation.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 13685

*   **Features**:

```json
{
    "head_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "kb_triplets": {
        "feature": {
            "feature": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


