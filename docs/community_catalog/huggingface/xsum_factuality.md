# xsum_factuality

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/xsum_factuality)
*   [Huggingface](https://huggingface.co/datasets/xsum_factuality)


## xsum_factuality


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xsum_factuality/xsum_factuality')
```

*   **Description**:

```
Neural abstractive summarization models are highly prone to hallucinate content that is unfaithful to the input
document. The popular metric such as ROUGE fails to show the severity of the problem. The dataset consists of
faithfulness and factuality annotations of abstractive summaries for the XSum dataset. We have crowdsourced 3 judgements
 for each of 500 x 5 document-system pairs. This will be a valuable resource to the abstractive summarization community.
```

*   **License**: https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 5597

*   **Features**:

```json
{
    "bbcid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "system": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "is_factual": {
        "num_classes": 2,
        "names": [
            "no",
            "yes"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "worker_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## xsum_faithfulness


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:xsum_factuality/xsum_faithfulness')
```

*   **Description**:

```
Neural abstractive summarization models are highly prone to hallucinate content that is unfaithful to the input
document. The popular metric such as ROUGE fails to show the severity of the problem. The dataset consists of
faithfulness and factuality annotations of abstractive summaries for the XSum dataset. We have crowdsourced 3 judgements
 for each of 500 x 5 document-system pairs. This will be a valuable resource to the abstractive summarization community.
```

*   **License**: https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 11185

*   **Features**:

```json
{
    "bbcid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "system": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "summary": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hallucination_type": {
        "num_classes": 2,
        "names": [
            "intrinsic",
            "extrinsic"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "hallucinated_span_start": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "hallucinated_span_end": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "worker_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


