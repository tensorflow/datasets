# atomic

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/atomic)
*   [Huggingface](https://huggingface.co/datasets/atomic)


## atomic


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:atomic/atomic')
```

*   **Description**:

```
This dataset provides the template sentences and
relationships defined in the ATOMIC common sense dataset. There are
three splits - train, test, and dev.

From the authors.

Disclaimer/Content warning: the events in atomic have been
automatically extracted from blogs, stories and books written at
various times. The events might depict violent or problematic actions,
which we left in the corpus for the sake of learning the (probably
negative but still important) commonsense implications associated with
the events. We removed a small set of truly out-dated events, but
might have missed some so please email us (msap@cs.washington.edu) if
you have any concerns.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 24856
`'train'` | 202271
`'validation'` | 22620

*   **Features**:

```json
{
    "event": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "oEffect": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "oReact": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "oWant": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "xAttr": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "xEffect": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "xIntent": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "xNeed": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "xReact": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "xWant": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "prefix": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "split": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


