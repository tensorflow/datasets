# amazon_reviews_multi

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/amazon_reviews_multi)
*   [Huggingface](https://huggingface.co/datasets/amazon_reviews_multi)


## all_languages


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:amazon_reviews_multi/all_languages')
```

*   **Description**:

```
We provide an Amazon product reviews dataset for multilingual text classification. The dataset contains reviews in English, Japanese, German, French, Chinese and Spanish, collected between November 1, 2015 and November 1, 2019. Each record in the dataset contains the review text, the review title, the star rating, an anonymized reviewer ID, an anonymized product ID and the coarse-grained product category (e.g. ‘books’, ‘appliances’, etc.) The corpus is balanced across stars, so each star rating constitutes 20% of the reviews in each language.

For each language, there are 200,000, 5,000 and 5,000 reviews in the training, development and test sets respectively. The maximum number of reviews per reviewer is 20 and the maximum number of reviews per product is 20. All reviews are truncated after 2,000 characters, and all reviews are at least 20 characters long.

Note that the language of a review does not necessarily match the language of its marketplace (e.g. reviews from amazon.de are primarily written in German, but could also be written in English, etc.). For this reason, we applied a language detection algorithm based on the work in Bojanowski et al. (2017) to determine the language of the review text and we removed reviews that were not written in the expected language.
```

*   **License**: By accessing the Multilingual Amazon Reviews Corpus ("Reviews Corpus"), you agree that the Reviews Corpus is an Amazon Service subject to the Amazon.com Conditions of Use (https://www.amazon.com/gp/help/customer/display.html/ref=footer_cou?ie=UTF8&nodeId=508088) and you agree to be bound by them, with the following additional conditions:

In addition to the license rights granted under the Conditions of Use, Amazon or its content providers grant you a limited, non-exclusive, non-transferable, non-sublicensable, revocable license to access and use the Reviews Corpus for purposes of academic research. You may not resell, republish, or make any commercial use of the Reviews Corpus or its contents, including use of the Reviews Corpus for commercial research, such as research related to a funding or consultancy contract, internship, or other relationship in which the results are provided for a fee or delivered to a for-profit organization. You may not (a) link or associate content in the Reviews Corpus with any personal information (including Amazon customer accounts), or (b) attempt to determine the identity of the author of any content in the Reviews Corpus. If you violate any of the foregoing conditions, your license to access and use the Reviews Corpus will automatically terminate without prejudice to any of the other rights or remedies Amazon may have.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 30000
`'train'` | 1200000
`'validation'` | 30000

*   **Features**:

```json
{
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "reviewer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "stars": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "review_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:amazon_reviews_multi/de')
```

*   **Description**:

```
We provide an Amazon product reviews dataset for multilingual text classification. The dataset contains reviews in English, Japanese, German, French, Chinese and Spanish, collected between November 1, 2015 and November 1, 2019. Each record in the dataset contains the review text, the review title, the star rating, an anonymized reviewer ID, an anonymized product ID and the coarse-grained product category (e.g. ‘books’, ‘appliances’, etc.) The corpus is balanced across stars, so each star rating constitutes 20% of the reviews in each language.

For each language, there are 200,000, 5,000 and 5,000 reviews in the training, development and test sets respectively. The maximum number of reviews per reviewer is 20 and the maximum number of reviews per product is 20. All reviews are truncated after 2,000 characters, and all reviews are at least 20 characters long.

Note that the language of a review does not necessarily match the language of its marketplace (e.g. reviews from amazon.de are primarily written in German, but could also be written in English, etc.). For this reason, we applied a language detection algorithm based on the work in Bojanowski et al. (2017) to determine the language of the review text and we removed reviews that were not written in the expected language.
```

*   **License**: By accessing the Multilingual Amazon Reviews Corpus ("Reviews Corpus"), you agree that the Reviews Corpus is an Amazon Service subject to the Amazon.com Conditions of Use (https://www.amazon.com/gp/help/customer/display.html/ref=footer_cou?ie=UTF8&nodeId=508088) and you agree to be bound by them, with the following additional conditions:

In addition to the license rights granted under the Conditions of Use, Amazon or its content providers grant you a limited, non-exclusive, non-transferable, non-sublicensable, revocable license to access and use the Reviews Corpus for purposes of academic research. You may not resell, republish, or make any commercial use of the Reviews Corpus or its contents, including use of the Reviews Corpus for commercial research, such as research related to a funding or consultancy contract, internship, or other relationship in which the results are provided for a fee or delivered to a for-profit organization. You may not (a) link or associate content in the Reviews Corpus with any personal information (including Amazon customer accounts), or (b) attempt to determine the identity of the author of any content in the Reviews Corpus. If you violate any of the foregoing conditions, your license to access and use the Reviews Corpus will automatically terminate without prejudice to any of the other rights or remedies Amazon may have.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 200000
`'validation'` | 5000

*   **Features**:

```json
{
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "reviewer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "stars": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "review_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:amazon_reviews_multi/en')
```

*   **Description**:

```
We provide an Amazon product reviews dataset for multilingual text classification. The dataset contains reviews in English, Japanese, German, French, Chinese and Spanish, collected between November 1, 2015 and November 1, 2019. Each record in the dataset contains the review text, the review title, the star rating, an anonymized reviewer ID, an anonymized product ID and the coarse-grained product category (e.g. ‘books’, ‘appliances’, etc.) The corpus is balanced across stars, so each star rating constitutes 20% of the reviews in each language.

For each language, there are 200,000, 5,000 and 5,000 reviews in the training, development and test sets respectively. The maximum number of reviews per reviewer is 20 and the maximum number of reviews per product is 20. All reviews are truncated after 2,000 characters, and all reviews are at least 20 characters long.

Note that the language of a review does not necessarily match the language of its marketplace (e.g. reviews from amazon.de are primarily written in German, but could also be written in English, etc.). For this reason, we applied a language detection algorithm based on the work in Bojanowski et al. (2017) to determine the language of the review text and we removed reviews that were not written in the expected language.
```

*   **License**: By accessing the Multilingual Amazon Reviews Corpus ("Reviews Corpus"), you agree that the Reviews Corpus is an Amazon Service subject to the Amazon.com Conditions of Use (https://www.amazon.com/gp/help/customer/display.html/ref=footer_cou?ie=UTF8&nodeId=508088) and you agree to be bound by them, with the following additional conditions:

In addition to the license rights granted under the Conditions of Use, Amazon or its content providers grant you a limited, non-exclusive, non-transferable, non-sublicensable, revocable license to access and use the Reviews Corpus for purposes of academic research. You may not resell, republish, or make any commercial use of the Reviews Corpus or its contents, including use of the Reviews Corpus for commercial research, such as research related to a funding or consultancy contract, internship, or other relationship in which the results are provided for a fee or delivered to a for-profit organization. You may not (a) link or associate content in the Reviews Corpus with any personal information (including Amazon customer accounts), or (b) attempt to determine the identity of the author of any content in the Reviews Corpus. If you violate any of the foregoing conditions, your license to access and use the Reviews Corpus will automatically terminate without prejudice to any of the other rights or remedies Amazon may have.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 200000
`'validation'` | 5000

*   **Features**:

```json
{
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "reviewer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "stars": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "review_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## es


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:amazon_reviews_multi/es')
```

*   **Description**:

```
We provide an Amazon product reviews dataset for multilingual text classification. The dataset contains reviews in English, Japanese, German, French, Chinese and Spanish, collected between November 1, 2015 and November 1, 2019. Each record in the dataset contains the review text, the review title, the star rating, an anonymized reviewer ID, an anonymized product ID and the coarse-grained product category (e.g. ‘books’, ‘appliances’, etc.) The corpus is balanced across stars, so each star rating constitutes 20% of the reviews in each language.

For each language, there are 200,000, 5,000 and 5,000 reviews in the training, development and test sets respectively. The maximum number of reviews per reviewer is 20 and the maximum number of reviews per product is 20. All reviews are truncated after 2,000 characters, and all reviews are at least 20 characters long.

Note that the language of a review does not necessarily match the language of its marketplace (e.g. reviews from amazon.de are primarily written in German, but could also be written in English, etc.). For this reason, we applied a language detection algorithm based on the work in Bojanowski et al. (2017) to determine the language of the review text and we removed reviews that were not written in the expected language.
```

*   **License**: By accessing the Multilingual Amazon Reviews Corpus ("Reviews Corpus"), you agree that the Reviews Corpus is an Amazon Service subject to the Amazon.com Conditions of Use (https://www.amazon.com/gp/help/customer/display.html/ref=footer_cou?ie=UTF8&nodeId=508088) and you agree to be bound by them, with the following additional conditions:

In addition to the license rights granted under the Conditions of Use, Amazon or its content providers grant you a limited, non-exclusive, non-transferable, non-sublicensable, revocable license to access and use the Reviews Corpus for purposes of academic research. You may not resell, republish, or make any commercial use of the Reviews Corpus or its contents, including use of the Reviews Corpus for commercial research, such as research related to a funding or consultancy contract, internship, or other relationship in which the results are provided for a fee or delivered to a for-profit organization. You may not (a) link or associate content in the Reviews Corpus with any personal information (including Amazon customer accounts), or (b) attempt to determine the identity of the author of any content in the Reviews Corpus. If you violate any of the foregoing conditions, your license to access and use the Reviews Corpus will automatically terminate without prejudice to any of the other rights or remedies Amazon may have.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 200000
`'validation'` | 5000

*   **Features**:

```json
{
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "reviewer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "stars": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "review_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## fr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:amazon_reviews_multi/fr')
```

*   **Description**:

```
We provide an Amazon product reviews dataset for multilingual text classification. The dataset contains reviews in English, Japanese, German, French, Chinese and Spanish, collected between November 1, 2015 and November 1, 2019. Each record in the dataset contains the review text, the review title, the star rating, an anonymized reviewer ID, an anonymized product ID and the coarse-grained product category (e.g. ‘books’, ‘appliances’, etc.) The corpus is balanced across stars, so each star rating constitutes 20% of the reviews in each language.

For each language, there are 200,000, 5,000 and 5,000 reviews in the training, development and test sets respectively. The maximum number of reviews per reviewer is 20 and the maximum number of reviews per product is 20. All reviews are truncated after 2,000 characters, and all reviews are at least 20 characters long.

Note that the language of a review does not necessarily match the language of its marketplace (e.g. reviews from amazon.de are primarily written in German, but could also be written in English, etc.). For this reason, we applied a language detection algorithm based on the work in Bojanowski et al. (2017) to determine the language of the review text and we removed reviews that were not written in the expected language.
```

*   **License**: By accessing the Multilingual Amazon Reviews Corpus ("Reviews Corpus"), you agree that the Reviews Corpus is an Amazon Service subject to the Amazon.com Conditions of Use (https://www.amazon.com/gp/help/customer/display.html/ref=footer_cou?ie=UTF8&nodeId=508088) and you agree to be bound by them, with the following additional conditions:

In addition to the license rights granted under the Conditions of Use, Amazon or its content providers grant you a limited, non-exclusive, non-transferable, non-sublicensable, revocable license to access and use the Reviews Corpus for purposes of academic research. You may not resell, republish, or make any commercial use of the Reviews Corpus or its contents, including use of the Reviews Corpus for commercial research, such as research related to a funding or consultancy contract, internship, or other relationship in which the results are provided for a fee or delivered to a for-profit organization. You may not (a) link or associate content in the Reviews Corpus with any personal information (including Amazon customer accounts), or (b) attempt to determine the identity of the author of any content in the Reviews Corpus. If you violate any of the foregoing conditions, your license to access and use the Reviews Corpus will automatically terminate without prejudice to any of the other rights or remedies Amazon may have.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 200000
`'validation'` | 5000

*   **Features**:

```json
{
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "reviewer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "stars": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "review_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ja


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:amazon_reviews_multi/ja')
```

*   **Description**:

```
We provide an Amazon product reviews dataset for multilingual text classification. The dataset contains reviews in English, Japanese, German, French, Chinese and Spanish, collected between November 1, 2015 and November 1, 2019. Each record in the dataset contains the review text, the review title, the star rating, an anonymized reviewer ID, an anonymized product ID and the coarse-grained product category (e.g. ‘books’, ‘appliances’, etc.) The corpus is balanced across stars, so each star rating constitutes 20% of the reviews in each language.

For each language, there are 200,000, 5,000 and 5,000 reviews in the training, development and test sets respectively. The maximum number of reviews per reviewer is 20 and the maximum number of reviews per product is 20. All reviews are truncated after 2,000 characters, and all reviews are at least 20 characters long.

Note that the language of a review does not necessarily match the language of its marketplace (e.g. reviews from amazon.de are primarily written in German, but could also be written in English, etc.). For this reason, we applied a language detection algorithm based on the work in Bojanowski et al. (2017) to determine the language of the review text and we removed reviews that were not written in the expected language.
```

*   **License**: By accessing the Multilingual Amazon Reviews Corpus ("Reviews Corpus"), you agree that the Reviews Corpus is an Amazon Service subject to the Amazon.com Conditions of Use (https://www.amazon.com/gp/help/customer/display.html/ref=footer_cou?ie=UTF8&nodeId=508088) and you agree to be bound by them, with the following additional conditions:

In addition to the license rights granted under the Conditions of Use, Amazon or its content providers grant you a limited, non-exclusive, non-transferable, non-sublicensable, revocable license to access and use the Reviews Corpus for purposes of academic research. You may not resell, republish, or make any commercial use of the Reviews Corpus or its contents, including use of the Reviews Corpus for commercial research, such as research related to a funding or consultancy contract, internship, or other relationship in which the results are provided for a fee or delivered to a for-profit organization. You may not (a) link or associate content in the Reviews Corpus with any personal information (including Amazon customer accounts), or (b) attempt to determine the identity of the author of any content in the Reviews Corpus. If you violate any of the foregoing conditions, your license to access and use the Reviews Corpus will automatically terminate without prejudice to any of the other rights or remedies Amazon may have.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 200000
`'validation'` | 5000

*   **Features**:

```json
{
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "reviewer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "stars": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "review_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## zh


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:amazon_reviews_multi/zh')
```

*   **Description**:

```
We provide an Amazon product reviews dataset for multilingual text classification. The dataset contains reviews in English, Japanese, German, French, Chinese and Spanish, collected between November 1, 2015 and November 1, 2019. Each record in the dataset contains the review text, the review title, the star rating, an anonymized reviewer ID, an anonymized product ID and the coarse-grained product category (e.g. ‘books’, ‘appliances’, etc.) The corpus is balanced across stars, so each star rating constitutes 20% of the reviews in each language.

For each language, there are 200,000, 5,000 and 5,000 reviews in the training, development and test sets respectively. The maximum number of reviews per reviewer is 20 and the maximum number of reviews per product is 20. All reviews are truncated after 2,000 characters, and all reviews are at least 20 characters long.

Note that the language of a review does not necessarily match the language of its marketplace (e.g. reviews from amazon.de are primarily written in German, but could also be written in English, etc.). For this reason, we applied a language detection algorithm based on the work in Bojanowski et al. (2017) to determine the language of the review text and we removed reviews that were not written in the expected language.
```

*   **License**: By accessing the Multilingual Amazon Reviews Corpus ("Reviews Corpus"), you agree that the Reviews Corpus is an Amazon Service subject to the Amazon.com Conditions of Use (https://www.amazon.com/gp/help/customer/display.html/ref=footer_cou?ie=UTF8&nodeId=508088) and you agree to be bound by them, with the following additional conditions:

In addition to the license rights granted under the Conditions of Use, Amazon or its content providers grant you a limited, non-exclusive, non-transferable, non-sublicensable, revocable license to access and use the Reviews Corpus for purposes of academic research. You may not resell, republish, or make any commercial use of the Reviews Corpus or its contents, including use of the Reviews Corpus for commercial research, such as research related to a funding or consultancy contract, internship, or other relationship in which the results are provided for a fee or delivered to a for-profit organization. You may not (a) link or associate content in the Reviews Corpus with any personal information (including Amazon customer accounts), or (b) attempt to determine the identity of the author of any content in the Reviews Corpus. If you violate any of the foregoing conditions, your license to access and use the Reviews Corpus will automatically terminate without prejudice to any of the other rights or remedies Amazon may have.

*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5000
`'train'` | 200000
`'validation'` | 5000

*   **Features**:

```json
{
    "review_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "reviewer_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "stars": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "review_body": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "review_title": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "language": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "product_category": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


