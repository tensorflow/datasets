# lc_quad

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/lc_quad)
*   [Huggingface](https://huggingface.co/datasets/lc_quad)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lc_quad')
```

*   **Description**:

```
LC-QuAD 2.0 is a Large Question Answering dataset with 30,000 pairs of question and its corresponding SPARQL query. The target knowledge base is Wikidata and DBpedia, specifically the 2018 version. Please see our paper for details about the dataset creation process and framework.
```

*   **License**: No known license
*   **Version**: 2.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4781
`'train'` | 19293

*   **Features**:

```json
{
    "NNQT_question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "uid": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "subgraph": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "template_index": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sparql_wikidata": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sparql_dbpedia18": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "template": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "paraphrased_question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


