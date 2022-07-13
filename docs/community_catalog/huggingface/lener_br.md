# lener_br

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/lener_br)
*   [Huggingface](https://huggingface.co/datasets/lener_br)


## lener_br


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lener_br/lener_br')
```

*   **Description**:

```
LeNER-Br is a Portuguese language dataset for named entity recognition 
applied to legal documents. LeNER-Br consists entirely of manually annotated 
legislation and legal cases texts and contains tags for persons, locations, 
time entities, organizations, legislation and legal cases.
To compose the dataset, 66 legal documents from several Brazilian Courts were
collected. Courts of superior and state levels were considered, such as Supremo
Tribunal Federal, Superior Tribunal de Justiça, Tribunal de Justiça de Minas
Gerais and Tribunal de Contas da União. In addition, four legislation documents
were collected, such as "Lei Maria da Penha", giving a total of 70 documents
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1390
`'train'` | 7828
`'validation'` | 1177

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "tokens": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "ner_tags": {
        "feature": {
            "num_classes": 13,
            "names": [
                "O",
                "B-ORGANIZACAO",
                "I-ORGANIZACAO",
                "B-PESSOA",
                "I-PESSOA",
                "B-TEMPO",
                "I-TEMPO",
                "B-LOCAL",
                "I-LOCAL",
                "B-LEGISLACAO",
                "I-LEGISLACAO",
                "B-JURISPRUDENCIA",
                "I-JURISPRUDENCIA"
            ],
            "names_file": null,
            "id": null,
            "_type": "ClassLabel"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


