# wiki_bio

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wiki_bio)
*   [Huggingface](https://huggingface.co/datasets/wiki_bio)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wiki_bio')
```

*   **Description**:

```
This dataset gathers 728,321 biographies from wikipedia. It aims at evaluating text generation
algorithms. For each article, we provide the first paragraph and the infobox (both tokenized).
For each article, we extracted the first paragraph (text), the infobox (structured data). Each
infobox is encoded as a list of (field name, field value) pairs. We used Stanford CoreNLP
(http://stanfordnlp.github.io/CoreNLP/) to preprocess the data, i.e. we broke the text into
sentences and tokenized both the text and the field values. The dataset was randomly split in
three subsets train (80%), valid (10%), test (10%).
```

*   **License**: CC BY-SA 3.0
*   **Version**: 1.2.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 72831
`'train'` | 582659
`'val'` | 72831

*   **Features**:

```json
{
    "input_text": {
        "table": {
            "feature": {
                "column_header": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                },
                "row_number": {
                    "dtype": "int16",
                    "id": null,
                    "_type": "Value"
                },
                "content": {
                    "dtype": "string",
                    "id": null,
                    "_type": "Value"
                }
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "context": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        }
    },
    "target_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


