# adv_glue

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/adv_glue)
*   [Huggingface](https://huggingface.co/datasets/adv_glue)


## adv_sst2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:adv_glue/adv_sst2')
```

*   **Description**:

```
Adversarial GLUE Benchmark (AdvGLUE) is a comprehensive robustness evaluation benchmark
that focuses on the adversarial robustness evaluation of language models. It covers five
natural language understanding tasks from the famous GLUE tasks and is an adversarial
version of GLUE benchmark.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 148

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## adv_qqp


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:adv_glue/adv_qqp')
```

*   **Description**:

```
Adversarial GLUE Benchmark (AdvGLUE) is a comprehensive robustness evaluation benchmark
that focuses on the adversarial robustness evaluation of language models. It covers five
natural language understanding tasks from the famous GLUE tasks and is an adversarial
version of GLUE benchmark.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 78

*   **Features**:

```json
{
    "question1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## adv_mnli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:adv_glue/adv_mnli')
```

*   **Description**:

```
Adversarial GLUE Benchmark (AdvGLUE) is a comprehensive robustness evaluation benchmark
that focuses on the adversarial robustness evaluation of language models. It covers five
natural language understanding tasks from the famous GLUE tasks and is an adversarial
version of GLUE benchmark.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 121

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
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## adv_mnli_mismatched


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:adv_glue/adv_mnli_mismatched')
```

*   **Description**:

```
Adversarial GLUE Benchmark (AdvGLUE) is a comprehensive robustness evaluation benchmark
that focuses on the adversarial robustness evaluation of language models. It covers five
natural language understanding tasks from the famous GLUE tasks and is an adversarial
version of GLUE benchmark.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 162

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
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## adv_qnli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:adv_glue/adv_qnli')
```

*   **Description**:

```
Adversarial GLUE Benchmark (AdvGLUE) is a comprehensive robustness evaluation benchmark
that focuses on the adversarial robustness evaluation of language models. It covers five
natural language understanding tasks from the famous GLUE tasks and is an adversarial
version of GLUE benchmark.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 148

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## adv_rte


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:adv_glue/adv_rte')
```

*   **Description**:

```
Adversarial GLUE Benchmark (AdvGLUE) is a comprehensive robustness evaluation benchmark
that focuses on the adversarial robustness evaluation of language models. It covers five
natural language understanding tasks from the famous GLUE tasks and is an adversarial
version of GLUE benchmark.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'validation'` | 81

*   **Features**:

```json
{
    "sentence1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


