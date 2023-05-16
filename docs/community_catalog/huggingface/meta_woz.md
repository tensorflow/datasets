# meta_woz

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/meta_woz)
*   [Huggingface](https://huggingface.co/datasets/meta_woz)


## dialogues


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:meta_woz/dialogues')
```

*   **Description**:

```
MetaLWOz: A Dataset of Multi-Domain Dialogues for the Fast Adaptation of Conversation Models. We introduce the Meta-Learning Wizard of Oz (MetaLWOz) dialogue dataset for developing fast adaptation methods for conversation models. This data can be used to train task-oriented dialogue models, specifically to develop methods to quickly simulate user responses with a small amount of data. Such fast-adaptation models fall into the research areas of transfer learning and meta learning. The dataset consists of 37,884 crowdsourced dialogues recorded between two human users in a Wizard of Oz setup, in which one was instructed to behave like a bot, and the other a true human user. The users are assigned a task belonging to a particular domain, for example booking a reservation at a particular restaurant, and work together to complete the task. Our dataset spans 47 domains having 227 tasks total. Dialogues are a minimum of 10 turns long.
```

*   **License**: Microsoft Research Data License Agreement
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2319
`'train'` | 37884

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "user_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "bot_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "task_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "turns": {
        "feature": {
            "dtype": "string",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    }
}
```



## tasks


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:meta_woz/tasks')
```

*   **Description**:

```
MetaLWOz: A Dataset of Multi-Domain Dialogues for the Fast Adaptation of Conversation Models. We introduce the Meta-Learning Wizard of Oz (MetaLWOz) dialogue dataset for developing fast adaptation methods for conversation models. This data can be used to train task-oriented dialogue models, specifically to develop methods to quickly simulate user responses with a small amount of data. Such fast-adaptation models fall into the research areas of transfer learning and meta learning. The dataset consists of 37,884 crowdsourced dialogues recorded between two human users in a Wizard of Oz setup, in which one was instructed to behave like a bot, and the other a true human user. The users are assigned a task belonging to a particular domain, for example booking a reservation at a particular restaurant, and work together to complete the task. Our dataset spans 47 domains having 227 tasks total. Dialogues are a minimum of 10 turns long.
```

*   **License**: Microsoft Research Data License Agreement
*   **Version**: 0.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 14
`'train'` | 227

*   **Features**:

```json
{
    "task_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "domain": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "bot_prompt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "bot_role": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "user_prompt": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "user_role": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


