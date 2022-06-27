# bing_coronavirus_query_set

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/bing_coronavirus_query_set)
*   [Huggingface](https://huggingface.co/datasets/bing_coronavirus_query_set)


## country_2020-09-01_2020-09-30


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:bing_coronavirus_query_set/country_2020-09-01_2020-09-30')
```

*   **Description**:

```
This dataset was curated from the Bing search logs (desktop users only) over the period of Jan 1st, 2020 – (Current Month - 1). Only searches that were issued many times by multiple users were included. The dataset includes queries from all over the world that had an intent related to the Coronavirus or Covid-19. In some cases this intent is explicit in the query itself (e.g., “Coronavirus updates Seattle”), in other cases it is implicit , e.g. “Shelter in place”. The implicit intent of search queries (e.g., “Toilet paper”) was extracted using random walks on the click graph as outlined in this paper by Microsoft Research. All personal data were removed.
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 317856

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "Date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Query": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "IsImplicitIntent": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Country": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "PopularityScore": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


