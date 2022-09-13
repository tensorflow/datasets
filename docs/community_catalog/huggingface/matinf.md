# matinf

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/matinf)
*   [Huggingface](https://huggingface.co/datasets/matinf)


## age_classification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:matinf/age_classification')
```

*   **Description**:

```
MATINF is the first jointly labeled large-scale dataset for classification, question answering and summarization.
MATINF contains 1.07 million question-answer pairs with human-labeled categories and user-generated question 
descriptions. Based on such rich information, MATINF is applicable for three major NLP tasks, including classification, 
question answering, and summarization. We benchmark existing methods and a novel multi-task baseline over MATINF to 
inspire further research. Our comprehensive comparison and experiments over MATINF and other datasets demonstrate the 
merits held by MATINF.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 38318
`'train'` | 134852
`'validation'` | 19323

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 3,
        "names": [
            "0-1\u5c81",
            "1-2\u5c81",
            "2-3\u5c81"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## topic_classification


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:matinf/topic_classification')
```

*   **Description**:

```
MATINF is the first jointly labeled large-scale dataset for classification, question answering and summarization.
MATINF contains 1.07 million question-answer pairs with human-labeled categories and user-generated question 
descriptions. Based on such rich information, MATINF is applicable for three major NLP tasks, including classification, 
question answering, and summarization. We benchmark existing methods and a novel multi-task baseline over MATINF to 
inspire further research. Our comprehensive comparison and experiments over MATINF and other datasets demonstrate the 
merits held by MATINF.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 175363
`'train'` | 613036
`'validation'` | 87519

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 18,
        "names": [
            "\u4ea7\u8925\u671f\u4fdd\u5065",
            "\u513f\u7ae5\u8fc7\u654f",
            "\u52a8\u4f5c\u53d1\u80b2",
            "\u5a74\u5e7c\u4fdd\u5065",
            "\u5a74\u5e7c\u5fc3\u7406",
            "\u5a74\u5e7c\u65e9\u6559",
            "\u5a74\u5e7c\u671f\u5582\u517b",
            "\u5a74\u5e7c\u8425\u517b",
            "\u5b55\u671f\u4fdd\u5065",
            "\u5bb6\u5ead\u6559\u80b2",
            "\u5e7c\u513f\u56ed",
            "\u672a\u51c6\u7236\u6bcd",
            "\u6d41\u4ea7\u548c\u4e0d\u5b55",
            "\u75ab\u82d7\u63a5\u79cd",
            "\u76ae\u80a4\u62a4\u7406",
            "\u5b9d\u5b9d\u4e0a\u706b",
            "\u8179\u6cfb",
            "\u5a74\u5e7c\u5e38\u89c1\u75c5"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## summarization


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:matinf/summarization')
```

*   **Description**:

```
MATINF is the first jointly labeled large-scale dataset for classification, question answering and summarization.
MATINF contains 1.07 million question-answer pairs with human-labeled categories and user-generated question 
descriptions. Based on such rich information, MATINF is applicable for three major NLP tasks, including classification, 
question answering, and summarization. We benchmark existing methods and a novel multi-task baseline over MATINF to 
inspire further research. Our comprehensive comparison and experiments over MATINF and other datasets demonstrate the 
merits held by MATINF.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 213681
`'train'` | 747888
`'validation'` | 106842

*   **Features**:

```json
{
    "description": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```



## qa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:matinf/qa')
```

*   **Description**:

```
MATINF is the first jointly labeled large-scale dataset for classification, question answering and summarization.
MATINF contains 1.07 million question-answer pairs with human-labeled categories and user-generated question 
descriptions. Based on such rich information, MATINF is applicable for three major NLP tasks, including classification, 
question answering, and summarization. We benchmark existing methods and a novel multi-task baseline over MATINF to 
inspire further research. Our comprehensive comparison and experiments over MATINF and other datasets demonstrate the 
merits held by MATINF.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 213681
`'train'` | 747888
`'validation'` | 106842

*   **Features**:

```json
{
    "question": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "answer": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    }
}
```


