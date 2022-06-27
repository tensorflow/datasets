# kor_sae

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kor_sae)
*   [Huggingface](https://huggingface.co/datasets/kor_sae)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kor_sae')
```

*   **Description**:

```
This new dataset is designed to extract intent from non-canonical directives which will help dialog managers
extract intent from user dialog that may have no clear objective or are paraphrased forms of utterances.
```

*   **License**: CC-BY-SA-4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 30837

*   **Features**:

```json
{
    "intent_pair1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "intent_pair2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 6,
        "names": [
            "yes/no",
            "alternative",
            "wh- questions",
            "prohibitions",
            "requirements",
            "strong requirements"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


