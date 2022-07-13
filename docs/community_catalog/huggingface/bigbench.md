# bigbench

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/bigbench)
*   [Huggingface](https://huggingface.co/datasets/bigbench)


## abstract_narrative_understanding


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/abstract_narrative_understanding')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 3000
`'train'` | 2400
`'validation'` | 600

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## anachronisms


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/anachronisms')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 230
`'train'` | 184
`'validation'` | 46

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## analogical_similarity


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/analogical_similarity')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 323
`'train'` | 259
`'validation'` | 64

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## analytic_entailment


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/analytic_entailment')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 70
`'train'` | 54
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## arithmetic


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/arithmetic')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 15023
`'train'` | 12019
`'validation'` | 3004

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ascii_word_recognition


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/ascii_word_recognition')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 5000
`'train'` | 4000
`'validation'` | 1000

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## authorship_verification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/authorship_verification')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 880
`'train'` | 704
`'validation'` | 176

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## auto_categorization


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/auto_categorization')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 328
`'train'` | 263
`'validation'` | 65

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## auto_debugging


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/auto_debugging')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 34
`'train'` | 18
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## bbq_lite_json


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/bbq_lite_json')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 16076
`'train'` | 12866
`'validation'` | 3210

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## bridging_anaphora_resolution_barqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/bridging_anaphora_resolution_barqa')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 648
`'train'` | 519
`'validation'` | 129

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## causal_judgment


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/causal_judgment')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 190
`'train'` | 152
`'validation'` | 38

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## cause_and_effect


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/cause_and_effect')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 153
`'train'` | 123
`'validation'` | 30

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## checkmate_in_one


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/checkmate_in_one')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 3498
`'train'` | 2799
`'validation'` | 699

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## chess_state_tracking


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/chess_state_tracking')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 6000
`'train'` | 4800
`'validation'` | 1200

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## chinese_remainder_theorem


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/chinese_remainder_theorem')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 500
`'train'` | 400
`'validation'` | 100

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## cifar10_classification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/cifar10_classification')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 20000
`'train'` | 16000
`'validation'` | 4000

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## code_line_description


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/code_line_description')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 60
`'train'` | 44
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## codenames


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/codenames')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 85
`'train'` | 68
`'validation'` | 17

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## color


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/color')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 4000
`'train'` | 3200
`'validation'` | 800

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## common_morpheme


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/common_morpheme')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 50
`'train'` | 34
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## conceptual_combinations


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/conceptual_combinations')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 103
`'train'` | 84
`'validation'` | 19

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## conlang_translation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/conlang_translation')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 164
`'train'` | 132
`'validation'` | 32

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## contextual_parametric_knowledge_conflicts


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/contextual_parametric_knowledge_conflicts')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 17528
`'train'` | 14023
`'validation'` | 3505

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## crash_blossom


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/crash_blossom')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 38
`'train'` | 22
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## crass_ai


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/crass_ai')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 44
`'train'` | 28
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## cryobiology_spanish


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/cryobiology_spanish')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 146
`'train'` | 117
`'validation'` | 29

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## cryptonite


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/cryptonite')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 26157
`'train'` | 20926
`'validation'` | 5231

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## cs_algorithms


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/cs_algorithms')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1320
`'train'` | 1056
`'validation'` | 264

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## dark_humor_detection


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/dark_humor_detection')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 80
`'train'` | 64
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## date_understanding


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/date_understanding')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 369
`'train'` | 296
`'validation'` | 73

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## disambiguation_qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/disambiguation_qa')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 258
`'train'` | 207
`'validation'` | 51

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## discourse_marker_prediction


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/discourse_marker_prediction')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 857
`'train'` | 686
`'validation'` | 171

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## disfl_qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/disfl_qa')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 8000
`'train'` | 6400
`'validation'` | 1600

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## dyck_languages


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/dyck_languages')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1000
`'train'` | 800
`'validation'` | 200

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## elementary_math_qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/elementary_math_qa')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 38160
`'train'` | 30531
`'validation'` | 7629

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## emoji_movie


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/emoji_movie')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 100
`'train'` | 80
`'validation'` | 20

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## emojis_emotion_prediction


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/emojis_emotion_prediction')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 131
`'train'` | 105
`'validation'` | 26

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## empirical_judgments


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/empirical_judgments')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 99
`'train'` | 80
`'validation'` | 19

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## english_proverbs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/english_proverbs')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 34
`'train'` | 18
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## english_russian_proverbs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/english_russian_proverbs')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 80
`'train'` | 64
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## entailed_polarity


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/entailed_polarity')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 148
`'train'` | 119
`'validation'` | 29

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## entailed_polarity_hindi


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/entailed_polarity_hindi')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 138
`'train'` | 111
`'validation'` | 27

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## epistemic_reasoning


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/epistemic_reasoning')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 2000
`'train'` | 1600
`'validation'` | 400

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## evaluating_information_essentiality


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/evaluating_information_essentiality')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 68
`'train'` | 52
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## fact_checker


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/fact_checker')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 7154
`'train'` | 5724
`'validation'` | 1430

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## fantasy_reasoning


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/fantasy_reasoning')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 201
`'train'` | 161
`'validation'` | 40

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## few_shot_nlg


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/few_shot_nlg')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 153
`'train'` | 123
`'validation'` | 30

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## figure_of_speech_detection


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/figure_of_speech_detection')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 59
`'train'` | 43
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## formal_fallacies_syllogisms_negation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/formal_fallacies_syllogisms_negation')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 14200
`'train'` | 11360
`'validation'` | 2840

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## gem


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/gem')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 14802
`'train'` | 11845
`'validation'` | 2957

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## gender_inclusive_sentences_german


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/gender_inclusive_sentences_german')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 200
`'train'` | 160
`'validation'` | 40

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## general_knowledge


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/general_knowledge')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 70
`'train'` | 54
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## geometric_shapes


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/geometric_shapes')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 359
`'train'` | 288
`'validation'` | 71

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## goal_step_wikihow


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/goal_step_wikihow')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 7053
`'train'` | 5643
`'validation'` | 1410

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## gre_reading_comprehension


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/gre_reading_comprehension')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 31
`'train'` | 15
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hhh_alignment


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/hhh_alignment')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 221
`'train'` | 179
`'validation'` | 42

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hindi_question_answering


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/hindi_question_answering')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 6610
`'train'` | 5288
`'validation'` | 1322

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hindu_knowledge


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/hindu_knowledge')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 175
`'train'` | 140
`'validation'` | 35

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hinglish_toxicity


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/hinglish_toxicity')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 200
`'train'` | 160
`'validation'` | 40

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## human_organs_senses


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/human_organs_senses')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 42
`'train'` | 26
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## hyperbaton


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/hyperbaton')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 50000
`'train'` | 40000
`'validation'` | 10000

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## identify_math_theorems


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/identify_math_theorems')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 53
`'train'` | 37
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## identify_odd_metaphor


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/identify_odd_metaphor')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 47
`'train'` | 31
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## implicatures


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/implicatures')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 492
`'train'` | 394
`'validation'` | 98

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## implicit_relations


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/implicit_relations')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 85
`'train'` | 68
`'validation'` | 17

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## intent_recognition


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/intent_recognition')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 693
`'train'` | 555
`'validation'` | 138

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## international_phonetic_alphabet_nli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/international_phonetic_alphabet_nli')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 126
`'train'` | 101
`'validation'` | 25

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## international_phonetic_alphabet_transliterate


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/international_phonetic_alphabet_transliterate')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1003
`'train'` | 803
`'validation'` | 200

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## intersect_geometry


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/intersect_geometry')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 249999
`'train'` | 200000
`'validation'` | 49999

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## irony_identification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/irony_identification')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 99
`'train'` | 80
`'validation'` | 19

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## kanji_ascii


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/kanji_ascii')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1092
`'train'` | 875
`'validation'` | 217

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## kannada


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/kannada')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 316
`'train'` | 253
`'validation'` | 63

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## key_value_maps


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/key_value_maps')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 101
`'train'` | 80
`'validation'` | 21

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## known_unknowns


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/known_unknowns')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 46
`'train'` | 30
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## language_games


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/language_games')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 2128
`'train'` | 1704
`'validation'` | 424

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## language_identification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/language_identification')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 10000
`'train'` | 8000
`'validation'` | 2000

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## linguistic_mappings


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/linguistic_mappings')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 15527
`'train'` | 12426
`'validation'` | 3101

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## linguistics_puzzles


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/linguistics_puzzles')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 2000
`'train'` | 1600
`'validation'` | 400

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## list_functions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/list_functions')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 10750
`'train'` | 8700
`'validation'` | 2050

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## logic_grid_puzzle


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/logic_grid_puzzle')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1000
`'train'` | 800
`'validation'` | 200

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## logical_args


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/logical_args')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 32
`'train'` | 16
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## logical_deduction


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/logical_deduction')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1500
`'train'` | 1200
`'validation'` | 300

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## logical_fallacy_detection


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/logical_fallacy_detection')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 2800
`'train'` | 2240
`'validation'` | 560

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## logical_sequence


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/logical_sequence')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 39
`'train'` | 23
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## mathematical_induction


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/mathematical_induction')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 69
`'train'` | 53
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## matrixshapes


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/matrixshapes')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 4462
`'train'` | 3570
`'validation'` | 892

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## metaphor_boolean


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/metaphor_boolean')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 680
`'train'` | 544
`'validation'` | 136

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## metaphor_understanding


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/metaphor_understanding')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 234
`'train'` | 188
`'validation'` | 46

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## minute_mysteries_qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/minute_mysteries_qa')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 477
`'train'` | 383
`'validation'` | 94

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## misconceptions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/misconceptions')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 219
`'train'` | 176
`'validation'` | 43

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## misconceptions_russian


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/misconceptions_russian')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 49
`'train'` | 33
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## mnist_ascii


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/mnist_ascii')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 69984
`'train'` | 55988
`'validation'` | 13996

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## modified_arithmetic


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/modified_arithmetic')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 6000
`'train'` | 4800
`'validation'` | 1200

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## moral_permissibility


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/moral_permissibility')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 342
`'train'` | 274
`'validation'` | 68

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## movie_dialog_same_or_different


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/movie_dialog_same_or_different')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 50000
`'train'` | 40000
`'validation'` | 10000

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## movie_recommendation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/movie_recommendation')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 500
`'train'` | 400
`'validation'` | 100

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## mult_data_wrangling


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/mult_data_wrangling')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 7854
`'train'` | 6380
`'validation'` | 1474

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## multiemo


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/multiemo')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1437281
`'train'` | 1149873
`'validation'` | 287408

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## natural_instructions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/natural_instructions')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 193250
`'train'` | 154615
`'validation'` | 38635

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## navigate


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/navigate')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1000
`'train'` | 800
`'validation'` | 200

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## nonsense_words_grammar


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/nonsense_words_grammar')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 50
`'train'` | 34
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## novel_concepts


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/novel_concepts')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 32
`'train'` | 16
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## object_counting


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/object_counting')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1000
`'train'` | 800
`'validation'` | 200

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## odd_one_out


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/odd_one_out')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 86
`'train'` | 69
`'validation'` | 17

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## operators


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/operators')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 210
`'train'` | 168
`'validation'` | 42

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## paragraph_segmentation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/paragraph_segmentation')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 9000
`'train'` | 7200
`'validation'` | 1800

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## parsinlu_qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/parsinlu_qa')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1050
`'train'` | 840
`'validation'` | 210

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## parsinlu_reading_comprehension


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/parsinlu_reading_comprehension')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 518
`'train'` | 415
`'validation'` | 103

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## penguins_in_a_table


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/penguins_in_a_table')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 149
`'train'` | 120
`'validation'` | 29

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## periodic_elements


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/periodic_elements')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 654
`'train'` | 524
`'validation'` | 130

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## persian_idioms


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/persian_idioms')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 66
`'train'` | 50
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## phrase_relatedness


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/phrase_relatedness')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 100
`'train'` | 80
`'validation'` | 20

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## physical_intuition


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/physical_intuition')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 81
`'train'` | 65
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## physics


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/physics')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 229
`'train'` | 184
`'validation'` | 45

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## physics_questions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/physics_questions')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 54
`'train'` | 38
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## play_dialog_same_or_different


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/play_dialog_same_or_different')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 3264
`'train'` | 2612
`'validation'` | 652

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## polish_sequence_labeling


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/polish_sequence_labeling')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 12812
`'train'` | 10250
`'validation'` | 2562

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## presuppositions_as_nli


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/presuppositions_as_nli')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 735
`'train'` | 588
`'validation'` | 147

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## qa_wikidata


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/qa_wikidata')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 20321
`'train'` | 16257
`'validation'` | 4064

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## question_selection


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/question_selection')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1582
`'train'` | 1266
`'validation'` | 316

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## real_or_fake_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/real_or_fake_text')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 15088
`'train'` | 12072
`'validation'` | 3016

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## reasoning_about_colored_objects


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/reasoning_about_colored_objects')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 2000
`'train'` | 1600
`'validation'` | 400

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## repeat_copy_logic


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/repeat_copy_logic')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 32
`'train'` | 16
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## rephrase


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/rephrase')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 78
`'train'` | 62
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## riddle_sense


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/riddle_sense')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 49
`'train'` | 33
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## ruin_names


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/ruin_names')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 448
`'train'` | 359
`'validation'` | 89

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## salient_translation_error_detection


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/salient_translation_error_detection')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 998
`'train'` | 799
`'validation'` | 199

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## scientific_press_release


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/scientific_press_release')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 50
`'train'` | 34
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## semantic_parsing_in_context_sparc


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/semantic_parsing_in_context_sparc')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1155
`'train'` | 924
`'validation'` | 231

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## semantic_parsing_spider


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/semantic_parsing_spider')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1034
`'train'` | 828
`'validation'` | 206

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## sentence_ambiguity


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/sentence_ambiguity')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 60
`'train'` | 44
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## similarities_abstraction


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/similarities_abstraction')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 76
`'train'` | 60
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## simp_turing_concept


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/simp_turing_concept')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 6390
`'train'` | 5112
`'validation'` | 1278

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## simple_arithmetic_json


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/simple_arithmetic_json')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 30
`'train'` | 14
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## simple_arithmetic_json_multiple_choice


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/simple_arithmetic_json_multiple_choice')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 8
`'train'` | 0
`'validation'` | 0

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## simple_arithmetic_json_subtasks


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/simple_arithmetic_json_subtasks')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 30
`'train'` | 15
`'validation'` | 15

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## simple_arithmetic_multiple_targets_json


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/simple_arithmetic_multiple_targets_json')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 10
`'train'` | 0
`'validation'` | 0

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## simple_ethical_questions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/simple_ethical_questions')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 115
`'train'` | 92
`'validation'` | 23

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## simple_text_editing


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/simple_text_editing')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 47
`'train'` | 31
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## snarks


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/snarks')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 181
`'train'` | 145
`'validation'` | 36

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## social_iqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/social_iqa')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1935
`'train'` | 1548
`'validation'` | 387

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## social_support


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/social_support')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 897
`'train'` | 718
`'validation'` | 179

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## sports_understanding


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/sports_understanding')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 986
`'train'` | 789
`'validation'` | 197

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## strange_stories


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/strange_stories')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 174
`'train'` | 140
`'validation'` | 34

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## strategyqa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/strategyqa')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 2289
`'train'` | 1832
`'validation'` | 457

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## sufficient_information


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/sufficient_information')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 39
`'train'` | 23
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## suicide_risk


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/suicide_risk')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 40
`'train'` | 24
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## swahili_english_proverbs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/swahili_english_proverbs')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 153
`'train'` | 123
`'validation'` | 30

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## swedish_to_german_proverbs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/swedish_to_german_proverbs')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 72
`'train'` | 56
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## symbol_interpretation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/symbol_interpretation')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 990
`'train'` | 795
`'validation'` | 195

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## temporal_sequences


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/temporal_sequences')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1000
`'train'` | 800
`'validation'` | 200

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## tense


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/tense')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 286
`'train'` | 229
`'validation'` | 57

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## timedial


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/timedial')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 2550
`'train'` | 2040
`'validation'` | 510

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## topical_chat


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/topical_chat')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 22295
`'train'` | 17836
`'validation'` | 4459

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## tracking_shuffled_objects


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/tracking_shuffled_objects')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 3750
`'train'` | 3000
`'validation'` | 750

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## understanding_fables


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/understanding_fables')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 189
`'train'` | 152
`'validation'` | 37

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## undo_permutation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/undo_permutation')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 300
`'train'` | 240
`'validation'` | 60

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## unit_conversion


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/unit_conversion')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 23936
`'train'` | 19151
`'validation'` | 4785

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## unit_interpretation


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/unit_interpretation')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 100
`'train'` | 80
`'validation'` | 20

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## unnatural_in_context_learning


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/unnatural_in_context_learning')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 73420
`'train'` | 58736
`'validation'` | 14684

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## vitaminc_fact_verification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/vitaminc_fact_verification')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 54668
`'train'` | 43735
`'validation'` | 10933

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## what_is_the_tao


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/what_is_the_tao')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 36
`'train'` | 20
`'validation'` | 16

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## which_wiki_edit


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/which_wiki_edit')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 571
`'train'` | 457
`'validation'` | 114

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## winowhy


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/winowhy')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 2862
`'train'` | 2290
`'validation'` | 572

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## word_sorting


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/word_sorting')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 1900
`'train'` | 1520
`'validation'` | 380

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## word_unscrambling


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bigbench/word_unscrambling')
```

*   **Description**:

```
The Beyond the Imitation Game Benchmark (BIG-bench) is a collaborative benchmark intended to
probe large language models, and extrapolate their future capabilities.
```

*   **License**: Apache License 2.0
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'default'` | 8917
`'train'` | 7134
`'validation'` | 1783

*   **Features**:

```json
{
    "idx": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "inputs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_targets": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "multiple_choice_scores": {
        "feature": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


