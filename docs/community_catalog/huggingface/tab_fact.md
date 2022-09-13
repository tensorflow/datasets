# tab_fact

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tab_fact)
*   [Huggingface](https://huggingface.co/datasets/tab_fact)


## tab_fact


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tab_fact/tab_fact')
```

*   **Description**:

```
The problem of verifying whether a textual hypothesis holds the truth based on the given evidence, also known as fact verification, plays an important role in the study of natural language understanding and semantic representation. However, existing studies are restricted to dealing with unstructured textual evidence (e.g., sentences and passages, a pool of passages), while verification using structured forms of evidence, such as tables, graphs, and databases, remains unexplored. TABFACT is large scale dataset with 16k Wikipedia tables as evidence for 118k human annotated statements designed for fact verification with semi-structured evidence. The statements are labeled as either ENTAILED or REFUTED. TABFACT is challenging since it involves both soft linguistic reasoning and hard symbolic reasoning.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 12779
`'train'` | 92283
`'validation'` | 12792

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "table_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_caption": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "statement": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "refuted",
            "entailed"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## blind_test


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tab_fact/blind_test')
```

*   **Description**:

```
The problem of verifying whether a textual hypothesis holds the truth based on the given evidence, also known as fact verification, plays an important role in the study of natural language understanding and semantic representation. However, existing studies are restricted to dealing with unstructured textual evidence (e.g., sentences and passages, a pool of passages), while verification using structured forms of evidence, such as tables, graphs, and databases, remains unexplored. TABFACT is large scale dataset with 16k Wikipedia tables as evidence for 118k human annotated statements designed for fact verification with semi-structured evidence. The statements are labeled as either ENTAILED or REFUTED. TABFACT is challenging since it involves both soft linguistic reasoning and hard symbolic reasoning.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9750

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "table_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "table_caption": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "statement": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


