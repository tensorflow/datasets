# sick

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sick)
*   [Huggingface](https://huggingface.co/datasets/sick)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sick')
```

*   **Description**:

```
Shared and internationally recognized benchmarks are fundamental for the development of any computational system.
We aim to help the research community working on compositional distributional semantic models (CDSMs) by providing SICK (Sentences Involving Compositional Knowldedge), a large size English benchmark tailored for them.
SICK consists of about 10,000 English sentence pairs that include many examples of the lexical, syntactic and semantic phenomena that CDSMs are expected to account for, but do not require dealing with other aspects of existing sentential data sets (idiomatic multiword expressions, named entities, telegraphic language) that are not within the scope of CDSMs.
By means of crowdsourcing techniques, each pair was annotated for two crucial semantic tasks: relatedness in meaning (with a 5-point rating scale as gold score) and entailment relation between the two elements (with three possible gold labels: entailment, contradiction, and neutral).
The SICK data set was used in SemEval-2014 Task 1, and it freely available for research purposes.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4906
`'train'` | 4439
`'validation'` | 495

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_A": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_B": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "entailment",
            "neutral",
            "contradiction"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "relatedness_score": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    },
    "entailment_AB": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entailment_BA": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_A_original": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_B_original": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_A_dataset": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_B_dataset": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


