# search_qa

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/search_qa)
*   [Huggingface](https://huggingface.co/datasets/search_qa)


## raw_jeopardy


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:search_qa/raw_jeopardy')
```

*   **Description**:

```
# pylint: disable=line-too-long
We publicly release a new large-scale dataset, called SearchQA, for machine comprehension, or question-answering. Unlike recently released datasets, such as DeepMind 
CNN/DailyMail and SQuAD, the proposed SearchQA was constructed to reflect a full pipeline of general question-answering. That is, we start not from an existing article 
and generate a question-answer pair, but start from an existing question-answer pair, crawled from J! Archive, and augment it with text snippets retrieved by Google. 
Following this approach, we built SearchQA, which consists of more than 140k question-answer pairs with each pair having 49.6 snippets on average. Each question-answer-context
 tuple of the SearchQA comes with additional meta-data such as the snippet's URL, which we believe will be valuable resources for future research. We conduct human evaluation 
 as well as test two baseline methods, one simple word selection and the other deep learning based, on the SearchQA. We show that there is a meaningful gap between the human 
 and machine performances. This suggests that the proposed dataset could well serve as a benchmark for question-answering.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 216757

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
        "dtype": "string",
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
    },
    "search_results": {
        "feature": {
            "urls": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "snippets": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "titles": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "related_links": {
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



## train_test_val


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:search_qa/train_test_val')
```

*   **Description**:

```
# pylint: disable=line-too-long
We publicly release a new large-scale dataset, called SearchQA, for machine comprehension, or question-answering. Unlike recently released datasets, such as DeepMind 
CNN/DailyMail and SQuAD, the proposed SearchQA was constructed to reflect a full pipeline of general question-answering. That is, we start not from an existing article 
and generate a question-answer pair, but start from an existing question-answer pair, crawled from J! Archive, and augment it with text snippets retrieved by Google. 
Following this approach, we built SearchQA, which consists of more than 140k question-answer pairs with each pair having 49.6 snippets on average. Each question-answer-context
 tuple of the SearchQA comes with additional meta-data such as the snippet's URL, which we believe will be valuable resources for future research. We conduct human evaluation 
 as well as test two baseline methods, one simple word selection and the other deep learning based, on the SearchQA. We show that there is a meaningful gap between the human 
 and machine performances. This suggests that the proposed dataset could well serve as a benchmark for question-answering.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 43228
`'train'` | 151295
`'validation'` | 21613

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
        "dtype": "string",
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
    },
    "search_results": {
        "feature": {
            "urls": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "snippets": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "titles": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "related_links": {
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


