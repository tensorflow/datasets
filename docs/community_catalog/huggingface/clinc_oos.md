# clinc_oos

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/clinc_oos)
*   [Huggingface](https://huggingface.co/datasets/clinc_oos)


## small


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clinc_oos/small')
```

*   **Description**:

```
This dataset is for evaluating the performance of intent classification systems in the
    presence of "out-of-scope" queries. By "out-of-scope", we mean queries that do not fall
    into any of the system-supported intent classes. Most datasets include only data that is
    "in-scope". Our dataset includes both in-scope and out-of-scope data. You might also know
    the term "out-of-scope" by other terms, including "out-of-domain" or "out-of-distribution".

Small, in which there are only 50 training queries per each in-scope intent
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5500
`'train'` | 7600
`'validation'` | 3100

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "intent": {
        "num_classes": 151,
        "names": [
            "restaurant_reviews",
            "nutrition_info",
            "account_blocked",
            "oil_change_how",
            "time",
            "weather",
            "redeem_rewards",
            "interest_rate",
            "gas_type",
            "accept_reservations",
            "smart_home",
            "user_name",
            "report_lost_card",
            "repeat",
            "whisper_mode",
            "what_are_your_hobbies",
            "order",
            "jump_start",
            "schedule_meeting",
            "meeting_schedule",
            "freeze_account",
            "what_song",
            "meaning_of_life",
            "restaurant_reservation",
            "traffic",
            "make_call",
            "text",
            "bill_balance",
            "improve_credit_score",
            "change_language",
            "no",
            "measurement_conversion",
            "timer",
            "flip_coin",
            "do_you_have_pets",
            "balance",
            "tell_joke",
            "last_maintenance",
            "exchange_rate",
            "uber",
            "car_rental",
            "credit_limit",
            "oos",
            "shopping_list",
            "expiration_date",
            "routing",
            "meal_suggestion",
            "tire_change",
            "todo_list",
            "card_declined",
            "rewards_balance",
            "change_accent",
            "vaccines",
            "reminder_update",
            "food_last",
            "change_ai_name",
            "bill_due",
            "who_do_you_work_for",
            "share_location",
            "international_visa",
            "calendar",
            "translate",
            "carry_on",
            "book_flight",
            "insurance_change",
            "todo_list_update",
            "timezone",
            "cancel_reservation",
            "transactions",
            "credit_score",
            "report_fraud",
            "spending_history",
            "directions",
            "spelling",
            "insurance",
            "what_is_your_name",
            "reminder",
            "where_are_you_from",
            "distance",
            "payday",
            "flight_status",
            "find_phone",
            "greeting",
            "alarm",
            "order_status",
            "confirm_reservation",
            "cook_time",
            "damaged_card",
            "reset_settings",
            "pin_change",
            "replacement_card_duration",
            "new_card",
            "roll_dice",
            "income",
            "taxes",
            "date",
            "who_made_you",
            "pto_request",
            "tire_pressure",
            "how_old_are_you",
            "rollover_401k",
            "pto_request_status",
            "how_busy",
            "application_status",
            "recipe",
            "calendar_update",
            "play_music",
            "yes",
            "direct_deposit",
            "credit_limit_change",
            "gas",
            "pay_bill",
            "ingredients_list",
            "lost_luggage",
            "goodbye",
            "what_can_i_ask_you",
            "book_hotel",
            "are_you_a_bot",
            "next_song",
            "change_speed",
            "plug_type",
            "maybe",
            "w2",
            "oil_change_when",
            "thank_you",
            "shopping_list_update",
            "pto_balance",
            "order_checks",
            "travel_alert",
            "fun_fact",
            "sync_device",
            "schedule_maintenance",
            "apr",
            "transfer",
            "ingredient_substitution",
            "calories",
            "current_location",
            "international_fees",
            "calculator",
            "definition",
            "next_holiday",
            "update_playlist",
            "mpg",
            "min_payment",
            "change_user_name",
            "restaurant_suggestion",
            "travel_notification",
            "cancel",
            "pto_used",
            "travel_suggestion",
            "change_volume"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## imbalanced


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clinc_oos/imbalanced')
```

*   **Description**:

```
This dataset is for evaluating the performance of intent classification systems in the
    presence of "out-of-scope" queries. By "out-of-scope", we mean queries that do not fall
    into any of the system-supported intent classes. Most datasets include only data that is
    "in-scope". Our dataset includes both in-scope and out-of-scope data. You might also know
    the term "out-of-scope" by other terms, including "out-of-domain" or "out-of-distribution".

Imbalanced, in which intents have either 25, 50, 75, or 100 training queries.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5500
`'train'` | 10625
`'validation'` | 3100

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "intent": {
        "num_classes": 151,
        "names": [
            "restaurant_reviews",
            "nutrition_info",
            "account_blocked",
            "oil_change_how",
            "time",
            "weather",
            "redeem_rewards",
            "interest_rate",
            "gas_type",
            "accept_reservations",
            "smart_home",
            "user_name",
            "report_lost_card",
            "repeat",
            "whisper_mode",
            "what_are_your_hobbies",
            "order",
            "jump_start",
            "schedule_meeting",
            "meeting_schedule",
            "freeze_account",
            "what_song",
            "meaning_of_life",
            "restaurant_reservation",
            "traffic",
            "make_call",
            "text",
            "bill_balance",
            "improve_credit_score",
            "change_language",
            "no",
            "measurement_conversion",
            "timer",
            "flip_coin",
            "do_you_have_pets",
            "balance",
            "tell_joke",
            "last_maintenance",
            "exchange_rate",
            "uber",
            "car_rental",
            "credit_limit",
            "oos",
            "shopping_list",
            "expiration_date",
            "routing",
            "meal_suggestion",
            "tire_change",
            "todo_list",
            "card_declined",
            "rewards_balance",
            "change_accent",
            "vaccines",
            "reminder_update",
            "food_last",
            "change_ai_name",
            "bill_due",
            "who_do_you_work_for",
            "share_location",
            "international_visa",
            "calendar",
            "translate",
            "carry_on",
            "book_flight",
            "insurance_change",
            "todo_list_update",
            "timezone",
            "cancel_reservation",
            "transactions",
            "credit_score",
            "report_fraud",
            "spending_history",
            "directions",
            "spelling",
            "insurance",
            "what_is_your_name",
            "reminder",
            "where_are_you_from",
            "distance",
            "payday",
            "flight_status",
            "find_phone",
            "greeting",
            "alarm",
            "order_status",
            "confirm_reservation",
            "cook_time",
            "damaged_card",
            "reset_settings",
            "pin_change",
            "replacement_card_duration",
            "new_card",
            "roll_dice",
            "income",
            "taxes",
            "date",
            "who_made_you",
            "pto_request",
            "tire_pressure",
            "how_old_are_you",
            "rollover_401k",
            "pto_request_status",
            "how_busy",
            "application_status",
            "recipe",
            "calendar_update",
            "play_music",
            "yes",
            "direct_deposit",
            "credit_limit_change",
            "gas",
            "pay_bill",
            "ingredients_list",
            "lost_luggage",
            "goodbye",
            "what_can_i_ask_you",
            "book_hotel",
            "are_you_a_bot",
            "next_song",
            "change_speed",
            "plug_type",
            "maybe",
            "w2",
            "oil_change_when",
            "thank_you",
            "shopping_list_update",
            "pto_balance",
            "order_checks",
            "travel_alert",
            "fun_fact",
            "sync_device",
            "schedule_maintenance",
            "apr",
            "transfer",
            "ingredient_substitution",
            "calories",
            "current_location",
            "international_fees",
            "calculator",
            "definition",
            "next_holiday",
            "update_playlist",
            "mpg",
            "min_payment",
            "change_user_name",
            "restaurant_suggestion",
            "travel_notification",
            "cancel",
            "pto_used",
            "travel_suggestion",
            "change_volume"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## plus


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:clinc_oos/plus')
```

*   **Description**:

```
This dataset is for evaluating the performance of intent classification systems in the
    presence of "out-of-scope" queries. By "out-of-scope", we mean queries that do not fall
    into any of the system-supported intent classes. Most datasets include only data that is
    "in-scope". Our dataset includes both in-scope and out-of-scope data. You might also know
    the term "out-of-scope" by other terms, including "out-of-domain" or "out-of-distribution".

OOS+, in which there are 250 out-of-scope training examples, rather than 100.
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5500
`'train'` | 15250
`'validation'` | 3100

*   **Features**:

```json
{
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "intent": {
        "num_classes": 151,
        "names": [
            "restaurant_reviews",
            "nutrition_info",
            "account_blocked",
            "oil_change_how",
            "time",
            "weather",
            "redeem_rewards",
            "interest_rate",
            "gas_type",
            "accept_reservations",
            "smart_home",
            "user_name",
            "report_lost_card",
            "repeat",
            "whisper_mode",
            "what_are_your_hobbies",
            "order",
            "jump_start",
            "schedule_meeting",
            "meeting_schedule",
            "freeze_account",
            "what_song",
            "meaning_of_life",
            "restaurant_reservation",
            "traffic",
            "make_call",
            "text",
            "bill_balance",
            "improve_credit_score",
            "change_language",
            "no",
            "measurement_conversion",
            "timer",
            "flip_coin",
            "do_you_have_pets",
            "balance",
            "tell_joke",
            "last_maintenance",
            "exchange_rate",
            "uber",
            "car_rental",
            "credit_limit",
            "oos",
            "shopping_list",
            "expiration_date",
            "routing",
            "meal_suggestion",
            "tire_change",
            "todo_list",
            "card_declined",
            "rewards_balance",
            "change_accent",
            "vaccines",
            "reminder_update",
            "food_last",
            "change_ai_name",
            "bill_due",
            "who_do_you_work_for",
            "share_location",
            "international_visa",
            "calendar",
            "translate",
            "carry_on",
            "book_flight",
            "insurance_change",
            "todo_list_update",
            "timezone",
            "cancel_reservation",
            "transactions",
            "credit_score",
            "report_fraud",
            "spending_history",
            "directions",
            "spelling",
            "insurance",
            "what_is_your_name",
            "reminder",
            "where_are_you_from",
            "distance",
            "payday",
            "flight_status",
            "find_phone",
            "greeting",
            "alarm",
            "order_status",
            "confirm_reservation",
            "cook_time",
            "damaged_card",
            "reset_settings",
            "pin_change",
            "replacement_card_duration",
            "new_card",
            "roll_dice",
            "income",
            "taxes",
            "date",
            "who_made_you",
            "pto_request",
            "tire_pressure",
            "how_old_are_you",
            "rollover_401k",
            "pto_request_status",
            "how_busy",
            "application_status",
            "recipe",
            "calendar_update",
            "play_music",
            "yes",
            "direct_deposit",
            "credit_limit_change",
            "gas",
            "pay_bill",
            "ingredients_list",
            "lost_luggage",
            "goodbye",
            "what_can_i_ask_you",
            "book_hotel",
            "are_you_a_bot",
            "next_song",
            "change_speed",
            "plug_type",
            "maybe",
            "w2",
            "oil_change_when",
            "thank_you",
            "shopping_list_update",
            "pto_balance",
            "order_checks",
            "travel_alert",
            "fun_fact",
            "sync_device",
            "schedule_maintenance",
            "apr",
            "transfer",
            "ingredient_substitution",
            "calories",
            "current_location",
            "international_fees",
            "calculator",
            "definition",
            "next_holiday",
            "update_playlist",
            "mpg",
            "min_payment",
            "change_user_name",
            "restaurant_suggestion",
            "travel_notification",
            "cancel",
            "pto_used",
            "travel_suggestion",
            "change_volume"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


