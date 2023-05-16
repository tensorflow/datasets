# nlu_evaluation_data

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/nlu_evaluation_data)
*   [Huggingface](https://huggingface.co/datasets/nlu_evaluation_data)



Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:nlu_evaluation_data')
```

*   **Description**:

```
Raw part of NLU Evaluation Data. It contains 25 715 non-empty examples (original dataset has 25716 examples) from 68 unique intents belonging to 18 scenarios.
```

*   **License**: Creative Commons Attribution 4.0 International License (CC BY 4.0)
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 25715

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "scenario": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 68,
        "names": [
            "alarm_query",
            "alarm_remove",
            "alarm_set",
            "audio_volume_down",
            "audio_volume_mute",
            "audio_volume_other",
            "audio_volume_up",
            "calendar_query",
            "calendar_remove",
            "calendar_set",
            "cooking_query",
            "cooking_recipe",
            "datetime_convert",
            "datetime_query",
            "email_addcontact",
            "email_query",
            "email_querycontact",
            "email_sendemail",
            "general_affirm",
            "general_commandstop",
            "general_confirm",
            "general_dontcare",
            "general_explain",
            "general_greet",
            "general_joke",
            "general_negate",
            "general_praise",
            "general_quirky",
            "general_repeat",
            "iot_cleaning",
            "iot_coffee",
            "iot_hue_lightchange",
            "iot_hue_lightdim",
            "iot_hue_lightoff",
            "iot_hue_lighton",
            "iot_hue_lightup",
            "iot_wemo_off",
            "iot_wemo_on",
            "lists_createoradd",
            "lists_query",
            "lists_remove",
            "music_dislikeness",
            "music_likeness",
            "music_query",
            "music_settings",
            "news_query",
            "play_audiobook",
            "play_game",
            "play_music",
            "play_podcasts",
            "play_radio",
            "qa_currency",
            "qa_definition",
            "qa_factoid",
            "qa_maths",
            "qa_stock",
            "recommendation_events",
            "recommendation_locations",
            "recommendation_movies",
            "social_post",
            "social_query",
            "takeaway_order",
            "takeaway_query",
            "transport_query",
            "transport_taxi",
            "transport_ticket",
            "transport_traffic",
            "weather_query"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


