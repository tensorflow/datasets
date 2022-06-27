# common_gen

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/common_gen)
*   [Huggingface](https://huggingface.co/datasets/common_gen)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:common_gen')
```

*   **Description**:

```
CommonGen is a constrained text generation task, associated with a benchmark dataset, 
to explicitly test machines for the ability of generative commonsense reasoning. Given 
a set of common concepts; the task is to generate a coherent sentence describing an 
everyday scenario using these concepts.

CommonGen is challenging because it inherently requires 1) relational reasoning using 
background commonsense knowledge, and 2) compositional generalization ability to work 
on unseen concept combinations. Our dataset, constructed through a combination of 
crowd-sourcing from AMT and existing caption corpora, consists of 30k concept-sets and 
50k sentences in total.
```

*   **License**: No known license
*   **Version**: 2020.5.30
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1497
`'train'` | 67389
`'validation'` | 4018

*   **Features**:

```json
{
    "concept_set_idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "concepts": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "target": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


