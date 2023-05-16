# oclar

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/oclar)
*   [Huggingface](https://huggingface.co/datasets/oclar)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:oclar')
```

*   **Description**:

```
The researchers of OCLAR Marwan et al. (2019), they gathered Arabic costumer reviews from Google reviewsa and Zomato website 
(https://www.zomato.com/lebanon) on wide scope of domain, including restaurants, hotels, hospitals, local shops, etc.
The corpus finally contains 3916 reviews in 5-rating scale. For this research purpose, the positive class considers
rating stars from 5 to 3 of 3465 reviews, and the negative class is represented from values of 1 and 2 of about 451 texts.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 3916

*   **Features**:

```json
{
    "pagename": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rating": {
        "dtype": "int8",
        "id": null,
        "_type": "Value"
    }
}
```


