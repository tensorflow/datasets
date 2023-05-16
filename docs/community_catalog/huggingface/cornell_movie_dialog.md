# cornell_movie_dialog

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/cornell_movie_dialog)
*   [Huggingface](https://huggingface.co/datasets/cornell_movie_dialog)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:cornell_movie_dialog')
```

*   **Description**:

```
This corpus contains a large metadata-rich collection of fictional conversations extracted from raw movie scripts:
- 220,579 conversational exchanges between 10,292 pairs of movie characters
- involves 9,035 characters from 617 movies
- in total 304,713 utterances
- movie metadata included:
    - genres
    - release year
    - IMDB rating
    - number of IMDB votes
    - IMDB rating
- character metadata included:
    - gender (for 3,774 characters)
    - position on movie credits (3,321 characters)
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 83097

*   **Features**:

```json
{
    "movieID": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "movieTitle": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "movieYear": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "movieIMDBRating": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "movieNoIMDBVotes": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "movieGenres": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "characterID1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "characterID2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "characterName1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "characterName2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "utterance": {
        "feature": {
            "text": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "LineID": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            }
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```


