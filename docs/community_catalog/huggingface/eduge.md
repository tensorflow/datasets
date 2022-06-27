# eduge

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/eduge)
*   [Huggingface](https://huggingface.co/datasets/eduge)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:eduge')
```

*   **Description**:

```
Eduge news classification dataset is provided by Bolorsoft LLC. It is used for training the Eduge.mn production news classifier
75K news articles in 9 categories: урлаг соёл, эдийн засаг, эрүүл мэнд, хууль, улс төр, спорт, технологи, боловсрол and байгал орчин
```

*   **License**: No known license
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15133
`'train'` | 60528

*   **Features**:

```json
{
    "news": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 9,
        "names": [
            "\u0443\u0440\u043b\u0430\u0433 \u0441\u043e\u0451\u043b",
            "\u044d\u0434\u0438\u0439\u043d \u0437\u0430\u0441\u0430\u0433",
            "\u044d\u0440\u04af\u04af\u043b \u043c\u044d\u043d\u0434",
            "\u0445\u0443\u0443\u043b\u044c",
            "\u0443\u043b\u0441 \u0442\u04e9\u0440",
            "\u0441\u043f\u043e\u0440\u0442",
            "\u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438",
            "\u0431\u043e\u043b\u043e\u0432\u0441\u0440\u043e\u043b",
            "\u0431\u0430\u0439\u0433\u0430\u043b \u043e\u0440\u0447\u0438\u043d"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


