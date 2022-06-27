# blog_authorship_corpus

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/blog_authorship_corpus)
*   [Huggingface](https://huggingface.co/datasets/blog_authorship_corpus)


## blog_authorship_corpus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:blog_authorship_corpus/blog_authorship_corpus')
```

*   **Description**:

```
The Blog Authorship Corpus consists of the collected posts of 19,320 bloggers gathered from blogger.com in August 2004. The corpus incorporates a total of 681,288 posts and over 140 million words - or approximately 35 posts and 7250 words per person.

Each blog is presented as a separate file, the name of which indicates a blogger id# and the blogger’s self-provided gender, age, industry and astrological sign. (All are labeled for gender and age but for many, industry and/or sign is marked as unknown.)

All bloggers included in the corpus fall into one of three age groups:
- 8240 "10s" blogs (ages 13-17),
- 8086 "20s" blogs (ages 23-27)
- 2994 "30s" blogs (ages 33-47).

For each age group there are an equal number of male and female bloggers.

Each blog in the corpus includes at least 200 occurrences of common English words. All formatting has been stripped with two exceptions. Individual posts within a single blogger are separated by the date of the following post and links within a post are denoted by the label urllink.

The corpus may be freely used for non-commercial research purposes.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 689793
`'validation'` | 37919

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "date": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "gender": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "age": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "horoscope": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "job": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


