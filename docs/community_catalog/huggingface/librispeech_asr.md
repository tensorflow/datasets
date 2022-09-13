# librispeech_asr

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/librispeech_asr)
*   [Huggingface](https://huggingface.co/datasets/librispeech_asr)


## clean


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:librispeech_asr/clean')
```

*   **Description**:

```
LibriSpeech is a corpus of approximately 1000 hours of read English speech with sampling rate of 16 kHz,
prepared by Vassil Panayotov with the assistance of Daniel Povey. The data is derived from read
audiobooks from the LibriVox project, and has been carefully segmented and aligned.87

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .flac format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import soundfile as sf

def map_to_array(batch):
    speech_array, _ = sf.read(batch["file"])
    batch["speech"] = speech_array
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2620
`'train.100'` | 28539
`'train.360'` | 104014
`'validation'` | 2703

*   **Features**:

```json
{
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 16000,
        "mono": true,
        "decode": true,
        "id": null,
        "_type": "Audio"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "speaker_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "chapter_id": {
        "dtype": "int64",
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



## other


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:librispeech_asr/other')
```

*   **Description**:

```
LibriSpeech is a corpus of approximately 1000 hours of read English speech with sampling rate of 16 kHz,
prepared by Vassil Panayotov with the assistance of Daniel Povey. The data is derived from read
audiobooks from the LibriVox project, and has been carefully segmented and aligned.87

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .flac format and is not converted to a float32 array. To convert, the audio
file to a float32 array, please make use of the `.map()` function as follows:


python
import soundfile as sf

def map_to_array(batch):
    speech_array, _ = sf.read(batch["file"])
    batch["speech"] = speech_array
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2939
`'train.500'` | 148688
`'validation'` | 2864

*   **Features**:

```json
{
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 16000,
        "mono": true,
        "decode": true,
        "id": null,
        "_type": "Audio"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "speaker_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "chapter_id": {
        "dtype": "int64",
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



## all


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:librispeech_asr/all')
```

*   **Description**:

```
LibriSpeech is a corpus of approximately 1000 hours of read English speech with sampling rate of 16 kHz,
prepared by Vassil Panayotov with the assistance of Daniel Povey. The data is derived from read
audiobooks from the LibriVox project, and has been carefully segmented and aligned.87
```

*   **License**: No known license
*   **Version**: 2.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test.clean'` | 2620
`'test.other'` | 2939
`'train.clean.100'` | 28539
`'train.clean.360'` | 104014
`'train.other.500'` | 148688
`'validation.clean'` | 2703
`'validation.other'` | 2864

*   **Features**:

```json
{
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 16000,
        "mono": true,
        "decode": true,
        "id": null,
        "_type": "Audio"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "speaker_id": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "chapter_id": {
        "dtype": "int64",
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


