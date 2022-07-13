# hebrew_this_world

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hebrew_this_world)
*   [Huggingface](https://huggingface.co/datasets/hebrew_this_world)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hebrew_this_world')
```

*   **Description**:

```
HebrewThisWorld is a data set consists of 2028 issues of the newspaper 'This World' edited by Uri Avnery and were published between 1950 and 1989. Released under the AGPLv3 license.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2028

*   **Features**:

```json
{
    "issue_num": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "page_count": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date_he": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "year": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "href": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "pdf": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "coverpage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "backpage": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


