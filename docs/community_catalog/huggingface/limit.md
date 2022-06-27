# limit

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/limit)
*   [Huggingface](https://huggingface.co/datasets/limit)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:limit')
```

*   **Description**:

```
Motion recognition is one of the basic cognitive capabilities of many life forms, yet identifying motion of physical entities in natural language have not been explored extensively and empirically. Literal-Motion-in-Text (LiMiT) dataset, is a large human-annotated collection of English text sentences describing physical occurrence of motion, with annotated physical entities in motion.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 23559

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "motion": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "motion_entities": [
        {
            "entity": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "start_index": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```


