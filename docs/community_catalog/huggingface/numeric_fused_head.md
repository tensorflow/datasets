# numeric_fused_head

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/numeric_fused_head)
*   [Huggingface](https://huggingface.co/datasets/numeric_fused_head)


## identification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:numeric_fused_head/identification')
```

*   **Description**:

```
Fused Head constructions are noun phrases in which the head noun is missing and is said to be "fused" with its dependent modifier. This missing information is implicit and is important for sentence understanding.The missing heads are easily filled in by humans,  but pose a challenge for computational models.

For example, in the sentence: "I bought 5 apples but got only 4.", 4 is a Fused-Head, and the missing head is apples, which appear earlier in the sentence.

This is a crowd-sourced dataset of 10k numerical fused head examples (1M tokens).
```

*   **License**: MIT
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 500
`'train'` | 165606
`'validation'` | 18401

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "start_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "end_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## resolution


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:numeric_fused_head/resolution')
```

*   **Description**:

```
Fused Head constructions are noun phrases in which the head noun is missing and is said to be "fused" with its dependent modifier. This missing information is implicit and is important for sentence understanding.The missing heads are easily filled in by humans,  but pose a challenge for computational models.

For example, in the sentence: "I bought 5 apples but got only 4.", 4 is a Fused-Head, and the missing head is apples, which appear earlier in the sentence.

This is a crowd-sourced dataset of 10k numerical fused head examples (1M tokens).
```

*   **License**: MIT
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1000
`'train'` | 7412
`'validation'` | 1000

*   **Features**:

```json
{
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "line_indices": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "head": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "speakers": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "anchors_indices": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


