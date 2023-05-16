# disfl_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/disfl_qa)
*   [Huggingface](https://huggingface.co/datasets/disfl_qa)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:disfl_qa')
```

*   **Description**:

```
Disfl-QA is a targeted dataset for contextual disfluencies in an information seeking setting,
namely question answering over Wikipedia passages. Disfl-QA builds upon the SQuAD-v2 (Rajpurkar et al., 2018)
dataset, where each question in the dev set is annotated to add a contextual disfluency using the paragraph as
a source of distractors.

The final dataset consists of ~12k (disfluent question, answer) pairs. Over 90% of the disfluencies are
corrections or restarts, making it a much harder test set for disfluency correction. Disfl-QA aims to fill a
major gap between speech and NLP research community. We hope the dataset can serve as a benchmark dataset for
testing robustness of models against disfluent inputs.

Our expriments reveal that the state-of-the-art models are brittle when subjected to disfluent inputs from
Disfl-QA. Detailed experiments and analyses can be found in our paper.
```

*   **License**: Disfl-QA dataset is licensed under CC BY 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3643
`'train'` | 7182
`'validation'` | 1000

*   **Features**:

```json
{
    "squad_v2_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "original question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "disfluent question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answers": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "answer_start": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


