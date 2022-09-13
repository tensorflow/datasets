# jeopardy

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/jeopardy)
*   [Huggingface](https://huggingface.co/datasets/jeopardy)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:jeopardy')
```

*   **Description**:

```
Dataset containing 216,930 Jeopardy questions, answers and other data.

The json file is an unordered list of questions where each question has
'category' : the question category, e.g. "HISTORY"
'value' : integer $ value of the question as string, e.g. "200"
Note: This is "None" for Final Jeopardy! and Tiebreaker questions
'question' : text of question
Note: This sometimes contains hyperlinks and other things messy text such as when there's a picture or video question
'answer' : text of answer
'round' : one of "Jeopardy!","Double Jeopardy!","Final Jeopardy!" or "Tiebreaker"
Note: Tiebreaker questions do happen but they're very rare (like once every 20 years)
'show_number' : int of show number, e.g '4680'
'air_date' : string of the show air date in format YYYY-MM-DD
```

*   **License**: No known license
*   **Version**: 0.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 216930

*   **Features**:

```json
{
    "category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "air_date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "round": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "show_number": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


