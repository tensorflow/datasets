# mbpp

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/mbpp)
*   [Huggingface](https://huggingface.co/datasets/mbpp)


## full


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mbpp/full')
```

*   **Description**:

```
The MBPP (Mostly Basic Python Problems) dataset consists of around 1,000 crowd-sourced Python
programming problems, designed to be solvable by entry level programmers, covering programming
fundamentals, standard library functionality, and so on. Each problem consists of a task
description, code solution and 3 automated test cases.
```

*   **License**: CC-BY-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 974

*   **Features**:

```json
{
    "task_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "code": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_list": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_setup_code": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "challenge_test_list": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## sanitized


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:mbpp/sanitized')
```

*   **Description**:

```
The MBPP (Mostly Basic Python Problems) dataset consists of around 1,000 crowd-sourced Python
programming problems, designed to be solvable by entry level programmers, covering programming
fundamentals, standard library functionality, and so on. Each problem consists of a task
description, code solution and 3 automated test cases.
```

*   **License**: CC-BY-4.0
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 427

*   **Features**:

```json
{
    "source_file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "task_id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "prompt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "code": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "test_imports": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "test_list": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


