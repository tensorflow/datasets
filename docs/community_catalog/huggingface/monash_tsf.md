# monash_tsf

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/monash_tsf)
*   [Huggingface](https://huggingface.co/datasets/monash_tsf)


## weather


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/weather')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3010
`'train'` | 3010
`'validation'` | 3010

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tourism_yearly


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/tourism_yearly')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 518
`'train'` | 518
`'validation'` | 518

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tourism_quarterly


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/tourism_quarterly')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 427
`'train'` | 427
`'validation'` | 427

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tourism_monthly


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/tourism_monthly')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 366
`'train'` | 366
`'validation'` | 366

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## cif_2016


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/cif_2016')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 72
`'train'` | 72
`'validation'` | 72

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## london_smart_meters


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/london_smart_meters')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5560
`'train'` | 5560
`'validation'` | 5560

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## australian_electricity_demand


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/australian_electricity_demand')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 5
`'train'` | 5
`'validation'` | 5

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wind_farms_minutely


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/wind_farms_minutely')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 339
`'train'` | 339
`'validation'` | 339

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## bitcoin


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/bitcoin')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 18
`'train'` | 18
`'validation'` | 18

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## pedestrian_counts


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/pedestrian_counts')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 66
`'train'` | 66
`'validation'` | 66

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## vehicle_trips


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/vehicle_trips')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 329
`'train'` | 329
`'validation'` | 329

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## kdd_cup_2018


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/kdd_cup_2018')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 270
`'train'` | 270
`'validation'` | 270

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## nn5_daily


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/nn5_daily')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 111
`'train'` | 111
`'validation'` | 111

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## nn5_weekly


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/nn5_weekly')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 111
`'train'` | 111
`'validation'` | 111

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## kaggle_web_traffic


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/kaggle_web_traffic')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 145063
`'train'` | 145063
`'validation'` | 145063

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## kaggle_web_traffic_weekly


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/kaggle_web_traffic_weekly')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 145063
`'train'` | 145063
`'validation'` | 145063

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## solar_10_minutes


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/solar_10_minutes')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 137
`'train'` | 137
`'validation'` | 137

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## solar_weekly


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/solar_weekly')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 137
`'train'` | 137
`'validation'` | 137

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## car_parts


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/car_parts')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2674
`'train'` | 2674
`'validation'` | 2674

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## fred_md


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/fred_md')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 107
`'train'` | 107
`'validation'` | 107

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## traffic_hourly


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/traffic_hourly')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 862
`'train'` | 862
`'validation'` | 862

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## traffic_weekly


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/traffic_weekly')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 862
`'train'` | 862
`'validation'` | 862

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## hospital


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/hospital')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 767
`'train'` | 767
`'validation'` | 767

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## covid_deaths


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/covid_deaths')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 266
`'train'` | 266
`'validation'` | 266

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## sunspot


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/sunspot')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
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
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## saugeenday


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/saugeenday')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
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
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## us_births


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/us_births')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
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
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## solar_4_seconds


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/solar_4_seconds')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
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
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## wind_4_seconds


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/wind_4_seconds')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
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
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## rideshare


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/rideshare')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 156
`'train'` | 156
`'validation'` | 156

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## oikolab_weather


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/oikolab_weather')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 8
`'train'` | 8
`'validation'` | 8

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "dtype": "float32",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## temperature_rain


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:monash_tsf/temperature_rain')
```

*   **Description**:

```
The first repository containing datasets of related time series for global forecasting.
```

*   **License**: The Creative Commons Attribution 4.0 International License. https://creativecommons.org/licenses/by/4.0/
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 422
`'train'` | 422
`'validation'` | 422

*   **Features**:

```json
{
    "start": {
        "dtype": "timestamp[s]",
        "id": null,
        "_type": "Value"
    },
    "target": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_static_cat": {
        "feature": {
            "dtype": "uint64",
            "id": null,
            "_type": "Value"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "feat_dynamic_real": {
        "feature": {
            "feature": {
                "dtype": "float32",
                "id": null,
                "_type": "Value"
            },
            "length": -1,
            "id": null,
            "_type": "Sequence"
        },
        "length": -1,
        "id": null,
        "_type": "Sequence"
    },
    "item_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


