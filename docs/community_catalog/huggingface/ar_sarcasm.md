# ar_sarcasm

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ar_sarcasm)
*   [Huggingface](https://huggingface.co/datasets/ar_sarcasm)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ar_sarcasm')
```

*   **Description**:

```
ArSarcasm is a new Arabic sarcasm detection dataset.
The dataset was created using previously available Arabic sentiment analysis datasets (SemEval 2017 and ASTD)
 and adds sarcasm and dialect labels to them. The dataset contains 10,547 tweets, 1,682 (16%) of which are sarcastic.
```

*   **License**: MIT
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2110
`'train'` | 8437

*   **Features**:

```json
{
    "dialect": {
        "num_classes": 5,
        "names": [
            "egypt",
            "gulf",
            "levant",
            "magreb",
            "msa"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "sarcasm": {
        "num_classes": 2,
        "names": [
            "non-sarcastic",
            "sarcastic"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "sentiment": {
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
    "original_sentiment": {
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
    "tweet": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


