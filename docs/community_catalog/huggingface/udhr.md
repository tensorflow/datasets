# udhr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/udhr)
*   [Huggingface](https://huggingface.co/datasets/udhr)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:udhr')
```

*   **Description**:

```
The Universal Declaration of Human Rights (UDHR) is a milestone document in the history of human rights. Drafted by
representatives with different legal and cultural backgrounds from all regions of the world, it set out, for the
first time, fundamental human rights to be universally protected. The Declaration was adopted by the UN General
Assembly in Paris on 10 December 1948 during its 183rd plenary meeting. The dataset includes translations of the
document in 464 languages and dialects.

© 1996 – 2009 The Office of the High Commissioner for Human Rights

This plain text version prepared by the “UDHR in Unicode” project, https://www.unicode.org/udhr.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 488

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang_key": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "lang_name": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "iso639-3": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "iso15924": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


