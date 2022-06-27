# winogrande

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/winogrande)
*   [Huggingface](https://huggingface.co/datasets/winogrande)


## winogrande_xs


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:winogrande/winogrande_xs')
```

*   **Description**:

```
WinoGrande is a new collection of 44k problems, inspired by Winograd Schema Challenge (Levesque, Davis, and Morgenstern
 2011), but adjusted to improve the scale and robustness against the dataset-specific bias. Formulated as a
fill-in-a-blank task with binary options, the goal is to choose the right option for a given sentence which requires
commonsense reasoning.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1767
`'train'` | 160
`'validation'` | 1267

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## winogrande_s


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:winogrande/winogrande_s')
```

*   **Description**:

```
WinoGrande is a new collection of 44k problems, inspired by Winograd Schema Challenge (Levesque, Davis, and Morgenstern
 2011), but adjusted to improve the scale and robustness against the dataset-specific bias. Formulated as a
fill-in-a-blank task with binary options, the goal is to choose the right option for a given sentence which requires
commonsense reasoning.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1767
`'train'` | 640
`'validation'` | 1267

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## winogrande_m


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:winogrande/winogrande_m')
```

*   **Description**:

```
WinoGrande is a new collection of 44k problems, inspired by Winograd Schema Challenge (Levesque, Davis, and Morgenstern
 2011), but adjusted to improve the scale and robustness against the dataset-specific bias. Formulated as a
fill-in-a-blank task with binary options, the goal is to choose the right option for a given sentence which requires
commonsense reasoning.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1767
`'train'` | 2558
`'validation'` | 1267

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## winogrande_l


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:winogrande/winogrande_l')
```

*   **Description**:

```
WinoGrande is a new collection of 44k problems, inspired by Winograd Schema Challenge (Levesque, Davis, and Morgenstern
 2011), but adjusted to improve the scale and robustness against the dataset-specific bias. Formulated as a
fill-in-a-blank task with binary options, the goal is to choose the right option for a given sentence which requires
commonsense reasoning.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1767
`'train'` | 10234
`'validation'` | 1267

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## winogrande_xl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:winogrande/winogrande_xl')
```

*   **Description**:

```
WinoGrande is a new collection of 44k problems, inspired by Winograd Schema Challenge (Levesque, Davis, and Morgenstern
 2011), but adjusted to improve the scale and robustness against the dataset-specific bias. Formulated as a
fill-in-a-blank task with binary options, the goal is to choose the right option for a given sentence which requires
commonsense reasoning.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1767
`'train'` | 40398
`'validation'` | 1267

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## winogrande_debiased


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:winogrande/winogrande_debiased')
```

*   **Description**:

```
WinoGrande is a new collection of 44k problems, inspired by Winograd Schema Challenge (Levesque, Davis, and Morgenstern
 2011), but adjusted to improve the scale and robustness against the dataset-specific bias. Formulated as a
fill-in-a-blank task with binary options, the goal is to choose the right option for a given sentence which requires
commonsense reasoning.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1767
`'train'` | 9248
`'validation'` | 1267

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "option2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


