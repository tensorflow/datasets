# mdd

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mdd)
*   [Huggingface](https://huggingface.co/datasets/mdd)


## task1_qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mdd/task1_qa')
```

*   **Description**:

```
The Movie Dialog dataset (MDD) is designed to measure how well
models can perform at goal and non-goal orientated dialog
centered around the topic of movies (question answering,
recommendation and discussion).
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 9952
`'train'` | 96185
`'validation'` | 9968

*   **Features**:

```json
{
    "dialogue_turns": {
        "feature": {
            "speaker": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "utterance": {
                "dtype": "string",
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



## task2_recs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mdd/task2_recs')
```

*   **Description**:

```
The Movie Dialog dataset (MDD) is designed to measure how well
models can perform at goal and non-goal orientated dialog
centered around the topic of movies (question answering,
recommendation and discussion).
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 10000
`'train'` | 1000000
`'validation'` | 10000

*   **Features**:

```json
{
    "dialogue_turns": {
        "feature": {
            "speaker": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "utterance": {
                "dtype": "string",
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



## task3_qarecs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mdd/task3_qarecs')
```

*   **Description**:

```
The Movie Dialog dataset (MDD) is designed to measure how well
models can perform at goal and non-goal orientated dialog
centered around the topic of movies (question answering,
recommendation and discussion).
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4915
`'train'` | 952125
`'validation'` | 5052

*   **Features**:

```json
{
    "dialogue_turns": {
        "feature": {
            "speaker": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "utterance": {
                "dtype": "string",
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



## task4_reddit


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mdd/task4_reddit')
```

*   **Description**:

```
The Movie Dialog dataset (MDD) is designed to measure how well
models can perform at goal and non-goal orientated dialog
centered around the topic of movies (question answering,
recommendation and discussion).
```

*   **License**: Creative Commons Attribution 3.0 License
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'cand_test'` | 10000
`'cand_valid'` | 10000
`'test'` | 10000
`'train'` | 945198
`'validation'` | 10000

*   **Features**:

```json
{
    "dialogue_turns": {
        "feature": {
            "speaker": {
                "dtype": "int32",
                "id": null,
                "_type": "Value"
            },
            "utterance": {
                "dtype": "string",
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


