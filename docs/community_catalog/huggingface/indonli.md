# indonli

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/indonli)
*   [Huggingface](https://huggingface.co/datasets/indonli)


## indonli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:indonli/indonli')
```

*   **Description**:

```
IndoNLI is the first human-elicited Natural Language Inference (NLI) dataset for Indonesian.
  IndoNLI is annotated by both crowd workers and experts. The expert-annotated data is used exclusively as a test set.
  It is designed to provide a challenging test-bed for Indonesian NLI by explicitly incorporating various linguistic phenomena such as numerical reasoning, structural changes, idioms, or temporal and spatial reasoning.
```

*   **License**: 
  CC BY-SA 4.0

  Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

  ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

  No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.


*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test_expert'` | 2984
`'test_lay'` | 2201
`'train'` | 10330
`'validation'` | 2197

*   **Features**:

```json
{
    "premise": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hypothesis": {
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
    }
}
```


