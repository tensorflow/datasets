# kan_hope

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/kan_hope)
*   [Huggingface](https://huggingface.co/datasets/kan_hope)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:kan_hope')
```

*   **Description**:

```
Numerous methods have been developed to monitor the spread of negativity in modern years by
eliminating vulgar, offensive, and fierce comments from social media platforms. However, there are relatively
lesser amounts of study that converges on embracing positivity, reinforcing supportive and reassuring content in online forums.
Consequently, we propose creating an English Kannada Hope speech dataset, KanHope and comparing several experiments to benchmark the dataset.
The dataset consists of 6,176 user generated comments in code mixed Kannada scraped from YouTube and manually annotated as bearing hope
speech or Not-hope speech.
This dataset was prepared for hope-speech text classification benchmark on code-mixed Kannada, an under-resourced language.
```

*   **License**: Creative Commons Attribution 4.0 International Licence
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 618
`'train'` | 4940

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 2,
        "names": [
            "Not-Hope",
            "Hope"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


