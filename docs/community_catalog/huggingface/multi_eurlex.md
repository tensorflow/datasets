# multi_eurlex

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/multi_eurlex)
*   [Huggingface](https://huggingface.co/datasets/multi_eurlex)


## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/en')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 55000
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## da


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/da')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 55000
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/de')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 55000
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## nl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/nl')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 55000
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## sv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/sv')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 42490
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## bg


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/bg')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 15986
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## cs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/cs')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 23187
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## hr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/hr')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 7944
`'validation'` | 2500

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## pl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/pl')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 23197
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## sk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/sk')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 22971
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## sl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/sl')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 23184
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/es')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 52785
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/fr')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 55000
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## it


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/it')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 55000
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/pt')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 52370
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## ro


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/ro')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 15921
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## et


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/et')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 23126
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## fi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/fi')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 42497
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## hu


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/hu')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 22664
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## lt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/lt')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 23188
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## lv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/lv')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 23208
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## el


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/el')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 55000
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## mt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/mt')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 17521
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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



## all_languages


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:multi_eurlex/all_languages')
```

*   **Description**:

```
MultiEURLEX comprises 65k EU laws in 23 official EU languages (some low-ish resource).
Each EU law has been annotated with EUROVOC concepts (labels) by the Publication Office of EU.
As with the English EURLEX, the goal is to predict the relevant EUROVOC concepts (labels);
this is multi-label classification task (given the text, predict multiple labels).
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 55000
`'validation'` | 5000

*   **Features**:

```json
{
    "celex_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "languages": [
            "en",
            "da",
            "de",
            "nl",
            "sv",
            "bg",
            "cs",
            "hr",
            "pl",
            "sk",
            "sl",
            "es",
            "fr",
            "it",
            "pt",
            "ro",
            "et",
            "fi",
            "hu",
            "lt",
            "lv",
            "el",
            "mt"
        ],
        "id": null,
        "_type": "Translation"
    },
    "labels": {
        "feature": {
            "num_classes": 21,
            "names": [
                "100149",
                "100160",
                "100148",
                "100147",
                "100152",
                "100143",
                "100156",
                "100158",
                "100154",
                "100153",
                "100142",
                "100145",
                "100150",
                "100162",
                "100159",
                "100144",
                "100151",
                "100157",
                "100161",
                "100146",
                "100155"
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


