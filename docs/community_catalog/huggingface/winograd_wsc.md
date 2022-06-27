# winograd_wsc

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/winograd_wsc)
*   [Huggingface](https://huggingface.co/datasets/winograd_wsc)


## wsc285


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:winograd_wsc/wsc285')
```

*   **Description**:

```
A Winograd schema is a pair of sentences that differ in only one or two words and that contain an ambiguity that is
resolved in opposite ways in the two sentences and requires the use of world knowledge and reasoning for its
resolution. The schema takes its name from a well-known example by Terry Winograd:

> The city councilmen refused the demonstrators a permit because they [feared/advocated] violence.

If the word is ``feared'', then ``they'' presumably refers to the city council; if it is ``advocated'' then ``they''
presumably refers to the demonstrators.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 285

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pronoun": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pronoun_loc": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "quote": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "quote_loc": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wsc273


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:winograd_wsc/wsc273')
```

*   **Description**:

```
A Winograd schema is a pair of sentences that differ in only one or two words and that contain an ambiguity that is
resolved in opposite ways in the two sentences and requires the use of world knowledge and reasoning for its
resolution. The schema takes its name from a well-known example by Terry Winograd:

> The city councilmen refused the demonstrators a permit because they [feared/advocated] violence.

If the word is ``feared'', then ``they'' presumably refers to the city council; if it is ``advocated'' then ``they''
presumably refers to the demonstrators.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 273

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pronoun": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pronoun_loc": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "quote": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "quote_loc": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "options": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "0",
            "1"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


