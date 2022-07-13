# tiny_shakespeare

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/tiny_shakespeare)
*   [Huggingface](https://huggingface.co/datasets/tiny_shakespeare)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:tiny_shakespeare')
```

*   **Description**:

```
40,000 lines of Shakespeare from a variety of Shakespeare's plays. Featured in Andrej Karpathy's blog post 'The Unreasonable Effectiveness of Recurrent Neural Networks': http://karpathy.github.io/2015/05/21/rnn-effectiveness/.

To use for e.g. character modelling:


d = datasets.load_dataset(name='tiny_shakespeare')['train']
d = d.map(lambda x: datasets.Value('strings').unicode_split(x['text'], 'UTF-8'))
# train split includes vocabulary for other splits
vocabulary = sorted(set(next(iter(d)).numpy()))
d = d.map(lambda x: {'cur_char': x[:-1], 'next_char': x[1:]})
d = d.unbatch()
seq_len = 100
batch_size = 2
d = d.batch(seq_len)
d = d.batch(batch_size)
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1
`'train'` | 1
`'validation'` | 1

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


