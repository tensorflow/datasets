# financial_phrasebank

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/financial_phrasebank)
*   [Huggingface](https://huggingface.co/datasets/financial_phrasebank)


## sentences_allagree


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:financial_phrasebank/sentences_allagree')
```

*   **Description**:

```
The key arguments for the low utilization of statistical techniques in
financial sentiment analysis have been the difficulty of implementation for
practical applications and the lack of high quality training data for building
such models. Especially in the case of finance and economic texts, annotated
collections are a scarce resource and many are reserved for proprietary use
only. To resolve the missing training data problem, we present a collection of
∼ 5000 sentences to establish human-annotated standards for benchmarking
alternative modeling techniques.

The objective of the phrase level annotation task was to classify each example
sentence into a positive, negative or neutral category by considering only the
information explicitly available in the given sentence. Since the study is
focused only on financial and economic domains, the annotators were asked to
consider the sentences from the view point of an investor only; i.e. whether
the news may have positive, negative or neutral influence on the stock price.
As a result, sentences which have a sentiment that is not relevant from an
economic or financial perspective are considered neutral.

This release of the financial phrase bank covers a collection of 4840
sentences. The selected collection of phrases was annotated by 16 people with
adequate background knowledge on financial markets. Three of the annotators
were researchers and the remaining 13 annotators were master’s students at
Aalto University School of Business with majors primarily in finance,
accounting, and economics.

Given the large number of overlapping annotations (5 to 8 annotations per
sentence), there are several ways to define a majority vote based gold
standard. To provide an objective comparison, we have formed 4 alternative
reference datasets based on the strength of majority agreement: all annotators
agree, >=75% of annotators agree, >=66% of annotators agree and >=50% of
annotators agree.
```

*   **License**: Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 2264

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## sentences_75agree


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:financial_phrasebank/sentences_75agree')
```

*   **Description**:

```
The key arguments for the low utilization of statistical techniques in
financial sentiment analysis have been the difficulty of implementation for
practical applications and the lack of high quality training data for building
such models. Especially in the case of finance and economic texts, annotated
collections are a scarce resource and many are reserved for proprietary use
only. To resolve the missing training data problem, we present a collection of
∼ 5000 sentences to establish human-annotated standards for benchmarking
alternative modeling techniques.

The objective of the phrase level annotation task was to classify each example
sentence into a positive, negative or neutral category by considering only the
information explicitly available in the given sentence. Since the study is
focused only on financial and economic domains, the annotators were asked to
consider the sentences from the view point of an investor only; i.e. whether
the news may have positive, negative or neutral influence on the stock price.
As a result, sentences which have a sentiment that is not relevant from an
economic or financial perspective are considered neutral.

This release of the financial phrase bank covers a collection of 4840
sentences. The selected collection of phrases was annotated by 16 people with
adequate background knowledge on financial markets. Three of the annotators
were researchers and the remaining 13 annotators were master’s students at
Aalto University School of Business with majors primarily in finance,
accounting, and economics.

Given the large number of overlapping annotations (5 to 8 annotations per
sentence), there are several ways to define a majority vote based gold
standard. To provide an objective comparison, we have formed 4 alternative
reference datasets based on the strength of majority agreement: all annotators
agree, >=75% of annotators agree, >=66% of annotators agree and >=50% of
annotators agree.
```

*   **License**: Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3453

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## sentences_66agree


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:financial_phrasebank/sentences_66agree')
```

*   **Description**:

```
The key arguments for the low utilization of statistical techniques in
financial sentiment analysis have been the difficulty of implementation for
practical applications and the lack of high quality training data for building
such models. Especially in the case of finance and economic texts, annotated
collections are a scarce resource and many are reserved for proprietary use
only. To resolve the missing training data problem, we present a collection of
∼ 5000 sentences to establish human-annotated standards for benchmarking
alternative modeling techniques.

The objective of the phrase level annotation task was to classify each example
sentence into a positive, negative or neutral category by considering only the
information explicitly available in the given sentence. Since the study is
focused only on financial and economic domains, the annotators were asked to
consider the sentences from the view point of an investor only; i.e. whether
the news may have positive, negative or neutral influence on the stock price.
As a result, sentences which have a sentiment that is not relevant from an
economic or financial perspective are considered neutral.

This release of the financial phrase bank covers a collection of 4840
sentences. The selected collection of phrases was annotated by 16 people with
adequate background knowledge on financial markets. Three of the annotators
were researchers and the remaining 13 annotators were master’s students at
Aalto University School of Business with majors primarily in finance,
accounting, and economics.

Given the large number of overlapping annotations (5 to 8 annotations per
sentence), there are several ways to define a majority vote based gold
standard. To provide an objective comparison, we have formed 4 alternative
reference datasets based on the strength of majority agreement: all annotators
agree, >=75% of annotators agree, >=66% of annotators agree and >=50% of
annotators agree.
```

*   **License**: Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4217

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## sentences_50agree


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:financial_phrasebank/sentences_50agree')
```

*   **Description**:

```
The key arguments for the low utilization of statistical techniques in
financial sentiment analysis have been the difficulty of implementation for
practical applications and the lack of high quality training data for building
such models. Especially in the case of finance and economic texts, annotated
collections are a scarce resource and many are reserved for proprietary use
only. To resolve the missing training data problem, we present a collection of
∼ 5000 sentences to establish human-annotated standards for benchmarking
alternative modeling techniques.

The objective of the phrase level annotation task was to classify each example
sentence into a positive, negative or neutral category by considering only the
information explicitly available in the given sentence. Since the study is
focused only on financial and economic domains, the annotators were asked to
consider the sentences from the view point of an investor only; i.e. whether
the news may have positive, negative or neutral influence on the stock price.
As a result, sentences which have a sentiment that is not relevant from an
economic or financial perspective are considered neutral.

This release of the financial phrase bank covers a collection of 4840
sentences. The selected collection of phrases was annotated by 16 people with
adequate background knowledge on financial markets. Three of the annotators
were researchers and the remaining 13 annotators were master’s students at
Aalto University School of Business with majors primarily in finance,
accounting, and economics.

Given the large number of overlapping annotations (5 to 8 annotations per
sentence), there are several ways to define a majority vote based gold
standard. To provide an objective comparison, we have formed 4 alternative
reference datasets based on the strength of majority agreement: all annotators
agree, >=75% of annotators agree, >=66% of annotators agree and >=50% of
annotators agree.
```

*   **License**: Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 4846

*   **Features**:

```json
{
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "negative",
            "neutral",
            "positive"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


