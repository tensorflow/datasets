# ncbi_disease

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/ncbi_disease)
*   [Huggingface](https://huggingface.co/datasets/ncbi_disease)


## ncbi_disease


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:ncbi_disease/ncbi_disease')
```

*   **Description**:

```
This paper presents the disease name and concept annotations of the NCBI disease corpus, a collection of 793 PubMed
abstracts fully annotated at the mention and concept level to serve as a research resource for the biomedical natural
language processing community. Each PubMed abstract was manually annotated by two annotators with disease mentions
and their corresponding concepts in Medical Subject Headings (MeSH®) or Online Mendelian Inheritance in Man (OMIM®).
Manual curation was performed using PubTator, which allowed the use of pre-annotations as a pre-step to manual annotations.
Fourteen annotators were randomly paired and differing annotations were discussed for reaching a consensus in two
annotation phases. In this setting, a high inter-annotator agreement was observed. Finally, all results were checked
against annotations of the rest of the corpus to assure corpus-wide consistency.

For more details, see: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3951655/

The original dataset can be downloaded from: https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/NCBI_corpus.zip
This dataset has been converted to CoNLL format for NER using the following tool: https://github.com/spyysalo/standoff2conll
Note: there is a duplicate document (PMID 8528200) in the original data, and the duplicate is recreated in the converted data.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 941
`'train'` | 5433
`'validation'` | 924

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
            "num_classes": 3,
            "names": [
                "O",
                "B-Disease",
                "I-Disease"
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


