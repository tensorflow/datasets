# asnq

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/asnq)
*   [Huggingface](https://huggingface.co/datasets/asnq)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:asnq')
```

*   **Description**:

```
ASNQ is a dataset for answer sentence selection derived from
Google's Natural Questions (NQ) dataset (Kwiatkowski et al. 2019).

Each example contains a question, candidate sentence, label indicating whether or not
the sentence answers the question, and two additional features -- 
sentence_in_long_answer and short_answer_in_sentence indicating whether ot not the 
candidate sentence is contained in the long_answer and if the short_answer is in the candidate sentence.

For more details please see 
https://arxiv.org/pdf/1911.04118.pdf

and 

https://research.google/pubs/pub47761/
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 20377568
`'validation'` | 930062

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "neg",
            "pos"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "sentence_in_long_answer": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    },
    "short_answer_in_sentence": {
        "dtype": "bool",
        "id": null,
        "_type": "Value"
    }
}
```


