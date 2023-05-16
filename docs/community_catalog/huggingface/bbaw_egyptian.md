# bbaw_egyptian

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/bbaw_egyptian)
*   [Huggingface](https://huggingface.co/datasets/bbaw_egyptian)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bbaw_egyptian')
```

*   **Description**:

```
The project `Strukturen und Transformationen des Wortschatzes der ägyptischen Sprache`
is compiling an extensively annotated digital corpus of Egyptian texts.
This publication comprises an excerpt of the internal database's contents.
```

*   **License**: Creative Commons-Lizenz - CC BY-SA - 4.0 International
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 100736

*   **Features**:

```json
{
    "transcription": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "hieroglyphs": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


