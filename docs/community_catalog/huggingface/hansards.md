# hansards

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/hansards)
*   [Huggingface](https://huggingface.co/datasets/hansards)


## senate


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hansards/senate')
```

*   **Description**:

```
This release contains 1.3 million pairs of aligned text chunks (sentences or smaller fragments)
from the official records (Hansards) of the 36th Canadian Parliament.

The complete Hansards of the debates in the House and Senate of the 36th Canadian Parliament,
as far as available, were aligned. The corpus was then split into 5 sets of sentence pairs:
training (80% of the sentence pairs), two sets of sentence pairs for testing (5% each), and
two sets of sentence pairs for final evaluation (5% each). The current release consists of the
training and testing sets. The evaluation sets are reserved for future MT evaluation purposes
and currently not available.

Caveats
1. This release contains only sentence pairs. Even though the order of the sentences is the same
as in the original, there may be gaps resulting from many-to-one, many-to-many, or one-to-many
alignments that were filtered out. Therefore, this release may not be suitable for
discourse-related research. 
2. Neither the sentence splitting nor the alignments are perfect. In particular, watch out for
pairs that differ considerably in length. You may want to filter these out before you do
any statistical training.

The alignment of the Hansards was performed as part of the ReWrite project under funding
from the DARPA TIDES program.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 25553
`'train'` | 182135

*   **Features**:

```json
{
    "fr": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "en": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## house


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:hansards/house')
```

*   **Description**:

```
This release contains 1.3 million pairs of aligned text chunks (sentences or smaller fragments)
from the official records (Hansards) of the 36th Canadian Parliament.

The complete Hansards of the debates in the House and Senate of the 36th Canadian Parliament,
as far as available, were aligned. The corpus was then split into 5 sets of sentence pairs:
training (80% of the sentence pairs), two sets of sentence pairs for testing (5% each), and
two sets of sentence pairs for final evaluation (5% each). The current release consists of the
training and testing sets. The evaluation sets are reserved for future MT evaluation purposes
and currently not available.

Caveats
1. This release contains only sentence pairs. Even though the order of the sentences is the same
as in the original, there may be gaps resulting from many-to-one, many-to-many, or one-to-many
alignments that were filtered out. Therefore, this release may not be suitable for
discourse-related research. 
2. Neither the sentence splitting nor the alignments are perfect. In particular, watch out for
pairs that differ considerably in length. You may want to filter these out before you do
any statistical training.

The alignment of the Hansards was performed as part of the ReWrite project under funding
from the DARPA TIDES program.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 122290
`'train'` | 947969

*   **Features**:

```json
{
    "fr": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "en": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


