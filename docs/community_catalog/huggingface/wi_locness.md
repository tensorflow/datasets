# wi_locness

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wi_locness)
*   [Huggingface](https://huggingface.co/datasets/wi_locness)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wi_locness')
```

*   **Description**:

```
Write & Improve (Yannakoudakis et al., 2018) is an online web platform that assists non-native
English students with their writing. Specifically, students from around the world submit letters,
stories, articles and essays in response to various prompts, and the W&I system provides instant
feedback. Since W&I went live in 2014, W&I annotators have manually annotated some of these
submissions and assigned them a CEFR level.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "userid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "cefr": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edits": {
        "feature": {
            "start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## wi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wi_locness/wi')
```

*   **Description**:

```
Write & Improve (Yannakoudakis et al., 2018) is an online web platform that assists non-native
English students with their writing. Specifically, students from around the world submit letters,
stories, articles and essays in response to various prompts, and the W&I system provides instant
feedback. Since W&I went live in 2014, W&I annotators have manually annotated some of these
submissions and assigned them a CEFR level.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3000
`'validation'` | 300

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "userid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "cefr": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edits": {
        "feature": {
            "start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## locness


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wi_locness/locness')
```

*   **Description**:

```
Write & Improve (Yannakoudakis et al., 2018) is an online web platform that assists non-native
English students with their writing. Specifically, students from around the world submit letters,
stories, articles and essays in response to various prompts, and the W&I system provides instant
feedback. Since W&I went live in 2014, W&I annotators have manually annotated some of these
submissions and assigned them a CEFR level.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 50

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "cefr": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "edits": {
        "feature": {
            "start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "end": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


