# id_clickbait

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/id_clickbait)
*   [Huggingface](https://huggingface.co/datasets/id_clickbait)


## annotated


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:id_clickbait/annotated')
```

*   **Description**:

```
The CLICK-ID dataset is a collection of Indonesian news headlines that was collected from 12 local online news
publishers; detikNews, Fimela, Kapanlagi, Kompas, Liputan6, Okezone, Posmetro-Medan, Republika, Sindonews, Tempo,
Tribunnews, and Wowkeren. This dataset is comprised of mainly two parts; (i) 46,119 raw article data, and (ii)
15,000 clickbait annotated sample headlines. Annotation was conducted with 3 annotator examining each headline.
Judgment were based only on the headline. The majority then is considered as the ground truth. In the annotated
sample, our annotation shows 6,290 clickbait and 8,710 non-clickbait.
```

*   **License**: Creative Commons Attribution 4.0 International license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 15000

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
    "label": {
        "num_classes": 2,
        "names": [
            "non-clickbait",
            "clickbait"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## raw


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:id_clickbait/raw')
```

*   **Description**:

```
The CLICK-ID dataset is a collection of Indonesian news headlines that was collected from 12 local online news
publishers; detikNews, Fimela, Kapanlagi, Kompas, Liputan6, Okezone, Posmetro-Medan, Republika, Sindonews, Tempo,
Tribunnews, and Wowkeren. This dataset is comprised of mainly two parts; (i) 46,119 raw article data, and (ii)
15,000 clickbait annotated sample headlines. Annotation was conducted with 3 annotator examining each headline.
Judgment were based only on the headline. The majority then is considered as the ground truth. In the annotated
sample, our annotation shows 6,290 clickbait and 8,710 non-clickbait.
```

*   **License**: Creative Commons Attribution 4.0 International license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 38655

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
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sub-category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "content": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


