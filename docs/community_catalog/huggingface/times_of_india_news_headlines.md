# times_of_india_news_headlines

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/times_of_india_news_headlines)
*   [Huggingface](https://huggingface.co/datasets/times_of_india_news_headlines)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:times_of_india_news_headlines')
```

*   **Description**:

```
This news dataset is a persistent historical archive of noteable events in the Indian subcontinent from start-2001 to mid-2020, recorded in realtime by the journalists of India. It contains approximately 3.3 million events published by Times of India. Times Group as a news agency, reaches out a very wide audience across Asia and drawfs every other agency in the quantity of english articles published per day. Due to the heavy daily volume over multiple years, this data offers a deep insight into Indian society, its priorities, events, issues and talking points and how they have unfolded over time. It is possible to chop this dataset into a smaller piece for a more focused analysis, based on one or more facets.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3297173

*   **Features**:

```json
{
    "publish_date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "headline_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "headline_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


