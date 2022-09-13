# nell

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/nell)
*   [Huggingface](https://huggingface.co/datasets/nell)


## nell_belief


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nell/nell_belief')
```

*   **Description**:

```
This dataset provides version 1115 of the belief
extracted by CMU's Never Ending Language Learner (NELL) and version
1110 of the candidate belief extracted by NELL. See
http://rtw.ml.cmu.edu/rtw/overview.  NELL is an open information
extraction system that attempts to read the Clueweb09 of 500 million
web pages (http://boston.lti.cs.cmu.edu/Data/clueweb09/) and general
web searches.

The dataset has 4 configurations: nell_belief, nell_candidate,
nell_belief_sentences, and nell_candidate_sentences. nell_belief is
certainties of belief are lower. The two sentences config extracts the
CPL sentence patterns filled with the applicable 'best' literal string
for the entities filled into the sentence patterns. And also provides
sentences found using web searches containing the entities and
relationships.

There are roughly 21M entries for nell_belief_sentences, and 100M
sentences for nell_candidate_sentences.
```

*   **License**: 

*   **Version**: 1115.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2766079

*   **Features**:

```json
{
    "entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "iteration_of_promotion": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_literal_strings": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value_literal_strings": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "best_entity_literal_string": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "best_value_literal_string": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "categories_for_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "categories_for_value": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## nell_candidate


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nell/nell_candidate')
```

*   **Description**:

```
This dataset provides version 1115 of the belief
extracted by CMU's Never Ending Language Learner (NELL) and version
1110 of the candidate belief extracted by NELL. See
http://rtw.ml.cmu.edu/rtw/overview.  NELL is an open information
extraction system that attempts to read the Clueweb09 of 500 million
web pages (http://boston.lti.cs.cmu.edu/Data/clueweb09/) and general
web searches.

The dataset has 4 configurations: nell_belief, nell_candidate,
nell_belief_sentences, and nell_candidate_sentences. nell_belief is
certainties of belief are lower. The two sentences config extracts the
CPL sentence patterns filled with the applicable 'best' literal string
for the entities filled into the sentence patterns. And also provides
sentences found using web searches containing the entities and
relationships.

There are roughly 21M entries for nell_belief_sentences, and 100M
sentences for nell_candidate_sentences.
```

*   **License**: 

*   **Version**: 1110.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 32687353

*   **Features**:

```json
{
    "entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "iteration_of_promotion": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "entity_literal_strings": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value_literal_strings": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "best_entity_literal_string": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "best_value_literal_string": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "categories_for_entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "categories_for_value": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "candidate_source": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## nell_belief_sentences


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nell/nell_belief_sentences')
```

*   **Description**:

```
This dataset provides version 1115 of the belief
extracted by CMU's Never Ending Language Learner (NELL) and version
1110 of the candidate belief extracted by NELL. See
http://rtw.ml.cmu.edu/rtw/overview.  NELL is an open information
extraction system that attempts to read the Clueweb09 of 500 million
web pages (http://boston.lti.cs.cmu.edu/Data/clueweb09/) and general
web searches.

The dataset has 4 configurations: nell_belief, nell_candidate,
nell_belief_sentences, and nell_candidate_sentences. nell_belief is
certainties of belief are lower. The two sentences config extracts the
CPL sentence patterns filled with the applicable 'best' literal string
for the entities filled into the sentence patterns. And also provides
sentences found using web searches containing the entities and
relationships.

There are roughly 21M entries for nell_belief_sentences, and 100M
sentences for nell_candidate_sentences.
```

*   **License**: 

*   **Version**: 1115.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 21031531

*   **Features**:

```json
{
    "entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "count": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## nell_candidate_sentences


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nell/nell_candidate_sentences')
```

*   **Description**:

```
This dataset provides version 1115 of the belief
extracted by CMU's Never Ending Language Learner (NELL) and version
1110 of the candidate belief extracted by NELL. See
http://rtw.ml.cmu.edu/rtw/overview.  NELL is an open information
extraction system that attempts to read the Clueweb09 of 500 million
web pages (http://boston.lti.cs.cmu.edu/Data/clueweb09/) and general
web searches.

The dataset has 4 configurations: nell_belief, nell_candidate,
nell_belief_sentences, and nell_candidate_sentences. nell_belief is
certainties of belief are lower. The two sentences config extracts the
CPL sentence patterns filled with the applicable 'best' literal string
for the entities filled into the sentence patterns. And also provides
sentences found using web searches containing the entities and
relationships.

There are roughly 21M entries for nell_belief_sentences, and 100M
sentences for nell_candidate_sentences.
```

*   **License**: 

*   **Version**: 1110.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 100866414

*   **Features**:

```json
{
    "entity": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "relation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "value": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "score": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "count": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "url": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence_type": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


