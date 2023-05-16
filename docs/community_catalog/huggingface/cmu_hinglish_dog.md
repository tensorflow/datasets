# cmu_hinglish_dog

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cmu_hinglish_dog)
*   [Huggingface](https://huggingface.co/datasets/cmu_hinglish_dog)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cmu_hinglish_dog')
```

*   **Description**:

```
This is a collection of text conversations in Hinglish (code mixing between Hindi-English) and their corresponding English only versions. Can be used for Translating between the two.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 960
`'train'` | 8060
`'validation'` | 942

*   **Features**:

```json
{
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "docIdx": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "languages": [
            "en",
            "hi_en"
        ],
        "id": null,
        "_type": "Translation"
    },
    "uid": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utcTimestamp": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rating": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "status": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "uid1LogInTime": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "uid1LogOutTime": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "uid1response": {
        "response": {
            "feature": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "uid2response": {
        "response": {
            "feature": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "type": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "user2_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "whoSawDoc": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "wikiDocumentIdx": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    }
}
```


