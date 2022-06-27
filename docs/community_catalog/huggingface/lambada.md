# lambada

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/lambada)
*   [Huggingface](https://huggingface.co/datasets/lambada)


## plain_text


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lambada/plain_text')
```

*   **Description**:

```
The LAMBADA evaluates the capabilities of computational models
for text understanding by means of a word prediction task.
LAMBADA is a collection of narrative passages sharing the characteristic
that human subjects are able to guess their last word if
they are exposed to the whole passage, but not if they
only see the last sentence preceding the target word.
To succeed on LAMBADA, computational models cannot
simply rely on local context, but must be able to
keep track of information in the broader discourse.

The LAMBADA dataset is extracted from BookCorpus and
consists of 10'022 passages, divided into 4'869 development
and 5'153 test passages. The training data for language
models to be tested on LAMBADA include the full text
of 2'662 novels (disjoint from those in dev+test),
comprising 203 million words.
```

*   **License**: No known license
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5153
`'train'` | 2662
`'validation'` | 4869

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


