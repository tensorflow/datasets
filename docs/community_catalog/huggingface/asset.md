# asset

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/asset)
*   [Huggingface](https://huggingface.co/datasets/asset)


## simplification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:asset/simplification')
```

*   **Description**:

```
ASSET is a dataset for evaluating Sentence Simplification systems with multiple rewriting transformations,
as described in "ASSET: A Dataset for Tuning and Evaluation of Sentence Simplification Models with Multiple Rewriting Transformations".
The corpus is composed of 2000 validation and 359 test original sentences that were each simplified 10 times by different annotators.
The corpus also contains human judgments of meaning preservation, fluency and simplicity for the outputs of several automatic text simplification systems.
```

*   **License**: Creative Common Attribution-NonCommercial 4.0 International
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 359
`'validation'` | 2000

*   **Features**:

```json
{
    "original": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simplifications": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ratings


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:asset/ratings')
```

*   **Description**:

```
ASSET is a dataset for evaluating Sentence Simplification systems with multiple rewriting transformations,
as described in "ASSET: A Dataset for Tuning and Evaluation of Sentence Simplification Models with Multiple Rewriting Transformations".
The corpus is composed of 2000 validation and 359 test original sentences that were each simplified 10 times by different annotators.
The corpus also contains human judgments of meaning preservation, fluency and simplicity for the outputs of several automatic text simplification systems.
```

*   **License**: Creative Common Attribution-NonCommercial 4.0 International
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'full'` | 4500

*   **Features**:

```json
{
    "original": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "simplification": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original_sentence_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "aspect": {
        "num_classes": 3,
        "names": [
            "meaning",
            "fluency",
            "simplicity"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "worker_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "rating": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


