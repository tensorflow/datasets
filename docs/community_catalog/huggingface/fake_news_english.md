# fake_news_english

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/fake_news_english)
*   [Huggingface](https://huggingface.co/datasets/fake_news_english)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:fake_news_english')
```

*   **Description**:

```
Fake news has become a major societal issue and a technical challenge for social media companies to identify. This content is difficult to identify because the term "fake news" covers intentionally false, deceptive stories as well as factual errors, satire, and sometimes, stories that a person just does not like. Addressing the problem requires clear definitions and examples. In this work, we present a dataset of fake news and satire stories that are hand coded, verified, and, in the case of fake news, include rebutting stories. We also include a thematic content analysis of the articles, identifying major themes that include hyperbolic support or condemnation of a gure, conspiracy theories, racist themes, and discrediting of reliable sources. In addition to releasing this dataset for research use, we analyze it and show results based on language that are promising for classification purposes. Overall, our contribution of a dataset and initial analysis are designed to support future work by fake news researchers.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 492

*   **Features**:

```json
{
    "article_number": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "url_of_article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "fake_or_satire": {
        "num_classes": 2,
        "names": [
            "Satire",
            "Fake"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "url_of_rebutting_article": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


