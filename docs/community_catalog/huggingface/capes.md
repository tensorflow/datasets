# capes

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/capes)
*   [Huggingface](https://huggingface.co/datasets/capes)


## en-pt


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:capes/en-pt')
```

*   **Description**:

```
A parallel corpus of theses and dissertations abstracts in English and Portuguese were collected from the CAPES website (Coordenação de Aperfeiçoamento de Pessoal de Nível Superior) - Brazil. The corpus is sentence aligned for all language pairs. Approximately 240,000 documents were collected and aligned using the Hunalign algorithm.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 1157610

*   **Features**:

```json
{
    "translation": {
        "languages": [
            "en",
            "pt"
        ],
        "id": null,
        "_type": "Translation"
    }
}
```


