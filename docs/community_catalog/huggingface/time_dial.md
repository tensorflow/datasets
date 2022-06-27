# time_dial

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/time_dial)
*   [Huggingface](https://huggingface.co/datasets/time_dial)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:time_dial')
```

*   **Description**:

```
TimeDial presents a crowdsourced English challenge set, for temporal commonsense reasoning, formulated
as a multiple choice cloze task with around 1.5k carefully curated dialogs. The dataset is derived from
the DailyDialog (Li et al., 2017), which is a multi-turn dialog corpus.

In order to establish strong baselines and provide information on future model development, we
conducted extensive experiments with state-of-the-art LMs. While humans can easily answer these
questions (97.8%), the best T5 model variant struggles on this challenge set (73%). Moreover, our
qualitative error analyses show that the models often rely on shallow, spurious features (particularly text
matching), instead of truly doing reasoning over the context.
```

*   **License**: TimeDial dataset is licensed under CC BY-NC-SA 4.0
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1446

*   **Features**:

```json
{
    "id": {
        "dtype": "int32",
        "id": null,
        "_type": "Value"
    },
    "conversation": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "correct1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "correct2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "incorrect1": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "incorrect1_rule": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "incorrect2": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "incorrect2_rule": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


