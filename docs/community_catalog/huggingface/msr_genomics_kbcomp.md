# msr_genomics_kbcomp

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/msr_genomics_kbcomp)
*   [Huggingface](https://huggingface.co/datasets/msr_genomics_kbcomp)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:msr_genomics_kbcomp')
```

*   **Description**:

```
The database is derived from the NCI PID Pathway Interaction Database, and the textual mentions are extracted from cooccurring pairs of genes in PubMed abstracts, processed and annotated by Literome (Poon et al. 2014). This dataset was used in the paper “Compositional Learning of Embeddings for Relation Paths in Knowledge Bases and Text” (Toutanova, Lin, Yih, Poon, and Quirk, 2016).
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2784
`'train'` | 12160
`'validation'` | 1315

*   **Features**:

```json
{
    "GENE1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relation": {
        "num_classes": 3,
        "names": [
            "Positive_regulation",
            "Negative_regulation",
            "Family"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "GENE2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


