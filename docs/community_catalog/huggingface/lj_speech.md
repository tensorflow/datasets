# lj_speech

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/lj_speech)
*   [Huggingface](https://huggingface.co/datasets/lj_speech)


## main


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:lj_speech/main')
```

*   **Description**:

```
This is a public domain speech dataset consisting of 13,100 short audio clips of a single speaker reading 
passages from 7 non-fiction books in English. A transcription is provided for each clip. Clips vary in length 
from 1 to 10 seconds and have a total length of approximately 24 hours.

Note that in order to limit the required storage for preparing this dataset, the audio
is stored in the .wav format and is not converted to a float32 array. To convert the audio
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
*   **Version**: 1.1.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'train'` | 13100

*   **Features**:

```json
{
    "id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "audio": {
        "sampling_rate": 22050,
        "mono": true,
        "decode": true,
        "id": null,
        "_type": "Audio"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "normalized_text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    }
}
```


