# covost2

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/covost2)
*   [Huggingface](https://huggingface.co/datasets/covost2)


## en_de


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_de')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_tr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_tr')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_fa


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_fa')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_sv-SE


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_sv-SE')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_mn


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_mn')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_zh-CN


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_zh-CN')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_cy


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_cy')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_ca


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_ca')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_sl


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_sl')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_et


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_et')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_id


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_id')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_ar


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_ar')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_ta


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_ta')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_lv


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_lv')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## en_ja


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/en_ja')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 15531
`'train'` | 289430
`'validation'` | 15531

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## fr_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/fr_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 14760
`'train'` | 207374
`'validation'` | 14760

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## de_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/de_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 13511
`'train'` | 127834
`'validation'` | 13511

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## es_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/es_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 13221
`'train'` | 79015
`'validation'` | 13221

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ca_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/ca_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 12730
`'train'` | 95854
`'validation'` | 12730

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## it_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/it_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 8951
`'train'` | 31698
`'validation'` | 8940

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ru_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/ru_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 6300
`'train'` | 12112
`'validation'` | 6110

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## zh-CN_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/zh-CN_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4898
`'train'` | 7085
`'validation'` | 4843

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## pt_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/pt_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 4023
`'train'` | 9158
`'validation'` | 3318

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## fa_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/fa_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3445
`'train'` | 53949
`'validation'` | 3445

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## et_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/et_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1571
`'train'` | 1782
`'validation'` | 1576

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## mn_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/mn_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1759
`'train'` | 2067
`'validation'` | 1761

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## nl_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/nl_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1699
`'train'` | 7108
`'validation'` | 1699

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## tr_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/tr_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1629
`'train'` | 3966
`'validation'` | 1624

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ar_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/ar_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1695
`'train'` | 2283
`'validation'` | 1758

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## sv-SE_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/sv-SE_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1595
`'train'` | 2160
`'validation'` | 1349

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## lv_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/lv_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 1629
`'train'` | 2337
`'validation'` | 1125

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## sl_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/sl_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 360
`'train'` | 1843
`'validation'` | 509

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ta_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/ta_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 786
`'train'` | 1358
`'validation'` | 384

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## ja_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/ja_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 684
`'train'` | 1119
`'validation'` | 635

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## id_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/id_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 844
`'train'` | 1243
`'validation'` | 792

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```



## cy_en


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:covost2/cy_en')
```

*   **Description**:

```
CoVoST 2, a large-scale multilingual speech translation corpus covering translations from 21 languages into English and from English into 15 languages. The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .mp3 format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import torchaudio

def map_to_array(batch):
    speech_array, _ = torchaudio.load(batch["file"])
    batch["speech"] = speech_array.numpy()
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.0.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 690
`'train'` | 1241
`'validation'` | 690

*   **Features**:

```json
{
    "client_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "sentence": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "translation": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


