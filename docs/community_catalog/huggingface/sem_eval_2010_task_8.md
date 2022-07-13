# sem_eval_2010_task_8

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/sem_eval_2010_task_8)
*   [Huggingface](https://huggingface.co/datasets/sem_eval_2010_task_8)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:sem_eval_2010_task_8')
```

*   **Description**:

```
The SemEval-2010 Task 8 focuses on Multi-way classification of semantic relations between pairs of nominals.
The task was designed to compare different approaches to semantic relation classification
and to provide a standard testbed for future research.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2717
`'train'` | 8000

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relation": {
        "num_classes": 19,
        "names": [
            "Cause-Effect(e1,e2)",
            "Cause-Effect(e2,e1)",
            "Component-Whole(e1,e2)",
            "Component-Whole(e2,e1)",
            "Content-Container(e1,e2)",
            "Content-Container(e2,e1)",
            "Entity-Destination(e1,e2)",
            "Entity-Destination(e2,e1)",
            "Entity-Origin(e1,e2)",
            "Entity-Origin(e2,e1)",
            "Instrument-Agency(e1,e2)",
            "Instrument-Agency(e2,e1)",
            "Member-Collection(e1,e2)",
            "Member-Collection(e2,e1)",
            "Message-Topic(e1,e2)",
            "Message-Topic(e2,e1)",
            "Product-Producer(e1,e2)",
            "Product-Producer(e2,e1)",
            "Other"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


