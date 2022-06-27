# quartz

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/quartz)
*   [Huggingface](https://huggingface.co/datasets/quartz)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:quartz')
```

*   **Description**:

```
QuaRTz is a crowdsourced dataset of 3864 multiple-choice questions about open domain qualitative relationships. Each 
question is paired with one of 405 different background sentences (sometimes short paragraphs).
The QuaRTz dataset V1 contains 3864 questions about open domain qualitative relationships. Each question is paired with 
one of 405 different background sentences (sometimes short paragraphs).

The dataset is split into train (2696), dev (384) and test (784). A background sentence will only appear in a single split.
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 784
`'train'` | 2696
`'validation'` | 384

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "choices": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "label": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "answerKey": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "para": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "para_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "para_anno": {
        "effect_prop": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "cause_dir_str": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "effect_dir_str": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "cause_dir_sign": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "effect_dir_sign": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "cause_prop": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "question_anno": {
        "more_effect_dir": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "less_effect_dir": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "less_cause_prop": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "more_effect_prop": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "less_effect_prop": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "less_cause_dir": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    }
}
```


