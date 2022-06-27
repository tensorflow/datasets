# wisesight_sentiment

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/wisesight_sentiment)
*   [Huggingface](https://huggingface.co/datasets/wisesight_sentiment)


## wisesight_sentiment


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:wisesight_sentiment/wisesight_sentiment')
```

*   **Description**:

```
Wisesight Sentiment Corpus: Social media messages in Thai language with sentiment category (positive, neutral, negative, question)
* Released to public domain under Creative Commons Zero v1.0 Universal license.
* Category (Labels): {"pos": 0, "neu": 1, "neg": 2, "q": 3}
* Size: 26,737 messages
* Language: Central Thai
* Style: Informal and conversational. With some news headlines and advertisement.
* Time period: Around 2016 to early 2019. With small amount from other period.
* Domains: Mixed. Majority are consumer products and services (restaurants, cosmetics, drinks, car, hotels), with some current affairs.
* Privacy:
    * Only messages that made available to the public on the internet (websites, blogs, social network sites).
    * For Facebook, this means the public comments (everyone can see) that made on a public page.
    * Private/protected messages and messages in groups, chat, and inbox are not included.
* Alternations and modifications:
    * Keep in mind that this corpus does not statistically represent anything in the language register.
    * Large amount of messages are not in their original form. Personal data are removed or masked.
    * Duplicated, leading, and trailing whitespaces are removed. Other punctuations, symbols, and emojis are kept intact.
    (Mis)spellings are kept intact.
    * Messages longer than 2,000 characters are removed.
    * Long non-Thai messages are removed. Duplicated message (exact match) are removed.
* More characteristics of the data can be explore: https://github.com/PyThaiNLP/wisesight-sentiment/blob/master/exploration.ipynb
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2671
`'train'` | 21628
`'validation'` | 2404

*   **Features**:

```json
{
    "texts": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "num_classes": 4,
        "names": [
            "pos",
            "neu",
            "neg",
            "q"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


