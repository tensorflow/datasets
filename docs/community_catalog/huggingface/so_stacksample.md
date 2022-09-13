# so_stacksample

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/so_stacksample)
*   [Huggingface](https://huggingface.co/datasets/so_stacksample)


## Answers


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:so_stacksample/Answers')
```

*   **Description**:

```
Dataset with the text of 10% of questions and answers from the Stack Overflow programming Q&A website.

This is organized as three tables:

Questions contains the title, body, creation date, closed date (if applicable), score, and owner ID for all non-deleted Stack Overflow questions whose Id is a multiple of 10.
Answers contains the body, creation date, score, and owner ID for each of the answers to these questions. The ParentId column links back to the Questions table.
Tags contains the tags on each of these questions
```

*   **License**: All Stack Overflow user contributions are licensed under CC-BY-SA 3.0 with attribution required.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'Answers'` | 2014516

*   **Features**:

```json
{
    "Id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "OwnerUserId": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "CreationDate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ParentId": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "Score": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "Body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## Questions


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:so_stacksample/Questions')
```

*   **Description**:

```
Dataset with the text of 10% of questions and answers from the Stack Overflow programming Q&A website.

This is organized as three tables:

Questions contains the title, body, creation date, closed date (if applicable), score, and owner ID for all non-deleted Stack Overflow questions whose Id is a multiple of 10.
Answers contains the body, creation date, score, and owner ID for each of the answers to these questions. The ParentId column links back to the Questions table.
Tags contains the tags on each of these questions
```

*   **License**: All Stack Overflow user contributions are licensed under CC-BY-SA 3.0 with attribution required.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'Questions'` | 1264216

*   **Features**:

```json
{
    "Id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "OwnerUserId": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "CreationDate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "ClosedDate": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Score": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "Title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "Body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## Tags


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:so_stacksample/Tags')
```

*   **Description**:

```
Dataset with the text of 10% of questions and answers from the Stack Overflow programming Q&A website.

This is organized as three tables:

Questions contains the title, body, creation date, closed date (if applicable), score, and owner ID for all non-deleted Stack Overflow questions whose Id is a multiple of 10.
Answers contains the body, creation date, score, and owner ID for each of the answers to these questions. The ParentId column links back to the Questions table.
Tags contains the tags on each of these questions
```

*   **License**: All Stack Overflow user contributions are licensed under CC-BY-SA 3.0 with attribution required.
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'Tags'` | 3750994

*   **Features**:

```json
{
    "Id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "Tag": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


