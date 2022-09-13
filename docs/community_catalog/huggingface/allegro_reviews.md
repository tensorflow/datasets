# allegro_reviews

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/allegro_reviews)
*   [Huggingface](https://huggingface.co/datasets/allegro_reviews)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:allegro_reviews')
```

*   **Description**:

```
Allegro Reviews is a sentiment analysis dataset, consisting of 11,588 product reviews written in Polish and extracted 
from Allegro.pl - a popular e-commerce marketplace. Each review contains at least 50 words and has a rating on a scale 
from one (negative review) to five (positive review).

We recommend using the provided train/dev/test split. The ratings for the test set reviews are kept hidden. 
You can evaluate your model using the online evaluation tool available on klejbenchmark.com.
```

*   **License**: CC BY-SA 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1006
`'train'` | 9577
`'validation'` | 1002

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "rating": {
        "dtype": "float32",
        "id": null,
        "_type": "Value"
    }
}
```


