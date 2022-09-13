# squad_kor_v2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/squad_kor_v2)
*   [Huggingface](https://huggingface.co/datasets/squad_kor_v2)


## squad_kor_v2


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:squad_kor_v2/squad_kor_v2')
```

*   **Description**:

```
KorQuAD 2.0 is a Korean question and answering dataset consisting of a total of 100,000+ pairs. There are three major differences from KorQuAD 1.0, which is the standard Korean Q & A data. The first is that a given document is a whole Wikipedia page, not just one or two paragraphs. Second, because the document also contains tables and lists, it is necessary to understand the document structured with HTML tags. Finally, the answer can be a long text covering not only word or phrase units, but paragraphs, tables, and lists. As a baseline model, BERT Multilingual is used, released by Google as an open source. It shows 46.0% F1 score, a very low score compared to 85.7% of the human F1 score. It indicates that this data is a challenging task. Additionally, we increased the performance by no-answer data augmentation. Through the distribution of this data, we intend to extend the limit of MRC that was limited to plain text to real world tasks of various lengths and formats.
```

*   **License**: CC BY-ND 2.0 KR
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 83486
`'validation'` | 10165

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "context": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "text": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "answer_start": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        },
        "html_answer_start": {
            "dtype": "int32",
            "id": null,
            "_type": "Value"
        }
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "raw_html": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


