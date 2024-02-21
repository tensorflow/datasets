# superb

References:

*   [Code](https://github.com/huggingface/datasets/blob/master/datasets/superb)
*   [Huggingface](https://huggingface.co/datasets/superb)


## asr


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:superb/asr')
```

*   **Description**:

```
Self-supervised learning (SSL) has proven vital for advancing research in
natural language processing (NLP) and computer vision (CV). The paradigm
pretrains a shared model on large volumes of unlabeled data and achieves
state-of-the-art (SOTA) for various tasks with minimal adaptation. However, the
speech processing community lacks a similar setup to systematically explore the
paradigm. To bridge this gap, we introduce Speech processing Universal
PERformance Benchmark (SUPERB). SUPERB is a leaderboard to benchmark the
performance of a shared model across a wide range of speech processing tasks
with minimal architecture changes and labeled data. Among multiple usages of the
shared model, we especially focus on extracting the representation learned from
SSL due to its preferable re-usability. We present a simple framework to solve
SUPERB tasks by learning task-specialized lightweight prediction heads on top of
the frozen shared model. Our results demonstrate that the framework is promising
as SSL representations show competitive generalizability and accessibility
across SUPERB tasks. We release SUPERB as a challenge with a leaderboard and a
benchmark toolkit to fuel the research in representation learning and general
speech processing.

Note that in order to limit the required storage for preparing this dataset, the
audio is stored in the .wav format and is not converted to a float32 array. To
convert the audio file to a float32 array, please make use of the `.map()`
function as follows:


python
import soundfile as sf

def map_to_array(batch):
    speech_array, _ = sf.read(batch["file"])
    batch["speech"] = speech_array
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.9.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 2620
`'train'` | 28539
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



## sd


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:superb/sd')
```

*   **Description**:

```
Self-supervised learning (SSL) has proven vital for advancing research in
natural language processing (NLP) and computer vision (CV). The paradigm
pretrains a shared model on large volumes of unlabeled data and achieves
state-of-the-art (SOTA) for various tasks with minimal adaptation. However, the
speech processing community lacks a similar setup to systematically explore the
paradigm. To bridge this gap, we introduce Speech processing Universal
PERformance Benchmark (SUPERB). SUPERB is a leaderboard to benchmark the
performance of a shared model across a wide range of speech processing tasks
with minimal architecture changes and labeled data. Among multiple usages of the
shared model, we especially focus on extracting the representation learned from
SSL due to its preferable re-usability. We present a simple framework to solve
SUPERB tasks by learning task-specialized lightweight prediction heads on top of
the frozen shared model. Our results demonstrate that the framework is promising
as SSL representations show competitive generalizability and accessibility
across SUPERB tasks. We release SUPERB as a challenge with a leaderboard and a
benchmark toolkit to fuel the research in representation learning and general
speech processing.

Note that in order to limit the required storage for preparing this dataset, the
audio is stored in the .flac format and is not converted to a float32 array. To
convert, the audio file to a float32 array, please make use of the `.map()`
function as follows:


python
import soundfile as sf

def map_to_array(batch):
    speech_array, _ = sf.read(batch["file"])
    batch["speech"] = speech_array
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.9.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'dev'` | 3014
`'test'` | 3002
`'train'` | 13901

*   **Features**:

```json
{
    "record_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "start": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "end": {
        "dtype": "int64",
        "id": null,
        "_type": "Value"
    },
    "speakers": [
        {
            "speaker_id": {
                "dtype": "string",
                "id": null,
                "_type": "Value"
            },
            "start": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            },
            "end": {
                "dtype": "int64",
                "id": null,
                "_type": "Value"
            }
        }
    ]
}
```



## ks


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:superb/ks')
```

*   **Description**:

```
Self-supervised learning (SSL) has proven vital for advancing research in
natural language processing (NLP) and computer vision (CV). The paradigm
pretrains a shared model on large volumes of unlabeled data and achieves
state-of-the-art (SOTA) for various tasks with minimal adaptation. However, the
speech processing community lacks a similar setup to systematically explore the
paradigm. To bridge this gap, we introduce Speech processing Universal
PERformance Benchmark (SUPERB). SUPERB is a leaderboard to benchmark the
performance of a shared model across a wide range of speech processing tasks
with minimal architecture changes and labeled data. Among multiple usages of the
shared model, we especially focus on extracting the representation learned from
SSL due to its preferable re-usability. We present a simple framework to solve
SUPERB tasks by learning task-specialized lightweight prediction heads on top of
the frozen shared model. Our results demonstrate that the framework is promising
as SSL representations show competitive generalizability and accessibility
across SUPERB tasks. We release SUPERB as a challenge with a leaderboard and a
benchmark toolkit to fuel the research in representation learning and general
speech processing.

Note that in order to limit the required storage for preparing this dataset, the
audio is stored in the .wav format and is not converted to a float32 array. To
convert the audio file to a float32 array, please make use of the `.map()`
function as follows:


python
import soundfile as sf

def map_to_array(batch):
    speech_array, _ = sf.read(batch["file"])
    batch["speech"] = speech_array
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.9.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3081
`'train'` | 51094
`'validation'` | 6798

*   **Features**:

```json
{
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 12,
        "names": [
            "yes",
            "no",
            "up",
            "down",
            "left",
            "right",
            "on",
            "off",
            "stop",
            "go",
            "_silence_",
            "_unknown_"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## ic


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:superb/ic')
```

*   **Description**:

```
Self-supervised learning (SSL) has proven vital for advancing research in
natural language processing (NLP) and computer vision (CV). The paradigm
pretrains a shared model on large volumes of unlabeled data and achieves
state-of-the-art (SOTA) for various tasks with minimal adaptation. However, the
speech processing community lacks a similar setup to systematically explore the
paradigm. To bridge this gap, we introduce Speech processing Universal
PERformance Benchmark (SUPERB). SUPERB is a leaderboard to benchmark the
performance of a shared model across a wide range of speech processing tasks
with minimal architecture changes and labeled data. Among multiple usages of the
shared model, we especially focus on extracting the representation learned from
SSL due to its preferable re-usability. We present a simple framework to solve
SUPERB tasks by learning task-specialized lightweight prediction heads on top of
the frozen shared model. Our results demonstrate that the framework is promising
as SSL representations show competitive generalizability and accessibility
across SUPERB tasks. We release SUPERB as a challenge with a leaderboard and a
benchmark toolkit to fuel the research in representation learning and general
speech processing.

Note that in order to limit the required storage for preparing this dataset, the
audio is stored in the .flac format and is not converted to a float32 array. To
convert, the audio file to a float32 array, please make use of the `.map()`
function as follows:


python
import soundfile as sf

def map_to_array(batch):
    speech_array, _ = sf.read(batch["file"])
    batch["speech"] = speech_array
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.9.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 3793
`'train'` | 23132
`'validation'` | 3118

*   **Features**:

```json
{
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "speaker_id": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "text": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "action": {
        "num_classes": 6,
        "names": [
            "activate",
            "bring",
            "change language",
            "deactivate",
            "decrease",
            "increase"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "object": {
        "num_classes": 14,
        "names": [
            "Chinese",
            "English",
            "German",
            "Korean",
            "heat",
            "juice",
            "lamp",
            "lights",
            "music",
            "newspaper",
            "none",
            "shoes",
            "socks",
            "volume"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    },
    "location": {
        "num_classes": 4,
        "names": [
            "bedroom",
            "kitchen",
            "none",
            "washroom"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```



## si


Use the following command to load this dataset in TFDS:

```python
ds = tfds.load('huggingface:superb/si')
```

*   **Description**:

```
Self-supervised learning (SSL) has proven vital for advancing research in
natural language processing (NLP) and computer vision (CV). The paradigm
pretrains a shared model on large volumes of unlabeled data and achieves
state-of-the-art (SOTA) for various tasks with minimal adaptation. However, the
speech processing community lacks a similar setup to systematically explore the
paradigm. To bridge this gap, we introduce Speech processing Universal
PERformance Benchmark (SUPERB). SUPERB is a leaderboard to benchmark the
performance of a shared model across a wide range of speech processing tasks
with minimal architecture changes and labeled data. Among multiple usages of the
shared model, we especially focus on extracting the representation learned from
SSL due to its preferable re-usability. We present a simple framework to solve
SUPERB tasks by learning task-specialized lightweight prediction heads on top of
the frozen shared model. Our results demonstrate that the framework is promising
as SSL representations show competitive generalizability and accessibility
across SUPERB tasks. We release SUPERB as a challenge with a leaderboard and a
benchmark toolkit to fuel the research in representation learning and general
speech processing.

Note that in order to limit the required storage for preparing this dataset, the
audio is stored in the .flac format and is not converted to a float32 array. To
convert, the audio file to a float32 array, please make use of the `.map()`
function as follows:


python
import soundfile as sf

def map_to_array(batch):
    speech_array, _ = sf.read(batch["file"])
    batch["speech"] = speech_array
    return batch

dataset = dataset.map(map_to_array, remove_columns=["file"])
```

*   **License**: No known license
*   **Version**: 1.9.0
*   **Splits**:

Split  | Examples
:----- | -------:
`'test'` | 8251
`'train'` | 138361
`'validation'` | 6904

*   **Features**:

```json
{
    "file": {
        "dtype": "string",
        "id": null,
        "_type": "Value"
    },
    "label": {
        "num_classes": 1251,
        "names": [
            "id10001",
            "id10002",
            "id10003",
            "id10004",
            "id10005",
            "id10006",
            "id10007",
            "id10008",
            "id10009",
            "id10010",
            "id10011",
            "id10012",
            "id10013",
            "id10014",
            "id10015",
            "id10016",
            "id10017",
            "id10018",
            "id10019",
            "id10020",
            "id10021",
            "id10022",
            "id10023",
            "id10024",
            "id10025",
            "id10026",
            "id10027",
            "id10028",
            "id10029",
            "id10030",
            "id10031",
            "id10032",
            "id10033",
            "id10034",
            "id10035",
            "id10036",
            "id10037",
            "id10038",
            "id10039",
            "id10040",
            "id10041",
            "id10042",
            "id10043",
            "id10044",
            "id10045",
            "id10046",
            "id10047",
            "id10048",
            "id10049",
            "id10050",
            "id10051",
            "id10052",
            "id10053",
            "id10054",
            "id10055",
            "id10056",
            "id10057",
            "id10058",
            "id10059",
            "id10060",
            "id10061",
            "id10062",
            "id10063",
            "id10064",
            "id10065",
            "id10066",
            "id10067",
            "id10068",
            "id10069",
            "id10070",
            "id10071",
            "id10072",
            "id10073",
            "id10074",
            "id10075",
            "id10076",
            "id10077",
            "id10078",
            "id10079",
            "id10080",
            "id10081",
            "id10082",
            "id10083",
            "id10084",
            "id10085",
            "id10086",
            "id10087",
            "id10088",
            "id10089",
            "id10090",
            "id10091",
            "id10092",
            "id10093",
            "id10094",
            "id10095",
            "id10096",
            "id10097",
            "id10098",
            "id10099",
            "id10100",
            "id10101",
            "id10102",
            "id10103",
            "id10104",
            "id10105",
            "id10106",
            "id10107",
            "id10108",
            "id10109",
            "id10110",
            "id10111",
            "id10112",
            "id10113",
            "id10114",
            "id10115",
            "id10116",
            "id10117",
            "id10118",
            "id10119",
            "id10120",
            "id10121",
            "id10122",
            "id10123",
            "id10124",
            "id10125",
            "id10126",
            "id10127",
            "id10128",
            "id10129",
            "id10130",
            "id10131",
            "id10132",
            "id10133",
            "id10134",
            "id10135",
            "id10136",
            "id10137",
            "id10138",
            "id10139",
            "id10140",
            "id10141",
            "id10142",
            "id10143",
            "id10144",
            "id10145",
            "id10146",
            "id10147",
            "id10148",
            "id10149",
            "id10150",
            "id10151",
            "id10152",
            "id10153",
            "id10154",
            "id10155",
            "id10156",
            "id10157",
            "id10158",
            "id10159",
            "id10160",
            "id10161",
            "id10162",
            "id10163",
            "id10164",
            "id10165",
            "id10166",
            "id10167",
            "id10168",
            "id10169",
            "id10170",
            "id10171",
            "id10172",
            "id10173",
            "id10174",
            "id10175",
            "id10176",
            "id10177",
            "id10178",
            "id10179",
            "id10180",
            "id10181",
            "id10182",
            "id10183",
            "id10184",
            "id10185",
            "id10186",
            "id10187",
            "id10188",
            "id10189",
            "id10190",
            "id10191",
            "id10192",
            "id10193",
            "id10194",
            "id10195",
            "id10196",
            "id10197",
            "id10198",
            "id10199",
            "id10200",
            "id10201",
            "id10202",
            "id10203",
            "id10204",
            "id10205",
            "id10206",
            "id10207",
            "id10208",
            "id10209",
            "id10210",
            "id10211",
            "id10212",
            "id10213",
            "id10214",
            "id10215",
            "id10216",
            "id10217",
            "id10218",
            "id10219",
            "id10220",
            "id10221",
            "id10222",
            "id10223",
            "id10224",
            "id10225",
            "id10226",
            "id10227",
            "id10228",
            "id10229",
            "id10230",
            "id10231",
            "id10232",
            "id10233",
            "id10234",
            "id10235",
            "id10236",
            "id10237",
            "id10238",
            "id10239",
            "id10240",
            "id10241",
            "id10242",
            "id10243",
            "id10244",
            "id10245",
            "id10246",
            "id10247",
            "id10248",
            "id10249",
            "id10250",
            "id10251",
            "id10252",
            "id10253",
            "id10254",
            "id10255",
            "id10256",
            "id10257",
            "id10258",
            "id10259",
            "id10260",
            "id10261",
            "id10262",
            "id10263",
            "id10264",
            "id10265",
            "id10266",
            "id10267",
            "id10268",
            "id10269",
            "id10270",
            "id10271",
            "id10272",
            "id10273",
            "id10274",
            "id10275",
            "id10276",
            "id10277",
            "id10278",
            "id10279",
            "id10280",
            "id10281",
            "id10282",
            "id10283",
            "id10284",
            "id10285",
            "id10286",
            "id10287",
            "id10288",
            "id10289",
            "id10290",
            "id10291",
            "id10292",
            "id10293",
            "id10294",
            "id10295",
            "id10296",
            "id10297",
            "id10298",
            "id10299",
            "id10300",
            "id10301",
            "id10302",
            "id10303",
            "id10304",
            "id10305",
            "id10306",
            "id10307",
            "id10308",
            "id10309",
            "id10310",
            "id10311",
            "id10312",
            "id10313",
            "id10314",
            "id10315",
            "id10316",
            "id10317",
            "id10318",
            "id10319",
            "id10320",
            "id10321",
            "id10322",
            "id10323",
            "id10324",
            "id10325",
            "id10326",
            "id10327",
            "id10328",
            "id10329",
            "id10330",
            "id10331",
            "id10332",
            "id10333",
            "id10334",
            "id10335",
            "id10336",
            "id10337",
            "id10338",
            "id10339",
            "id10340",
            "id10341",
            "id10342",
            "id10343",
            "id10344",
            "id10345",
            "id10346",
            "id10347",
            "id10348",
            "id10349",
            "id10350",
            "id10351",
            "id10352",
            "id10353",
            "id10354",
            "id10355",
            "id10356",
            "id10357",
            "id10358",
            "id10359",
            "id10360",
            "id10361",
            "id10362",
            "id10363",
            "id10364",
            "id10365",
            "id10366",
            "id10367",
            "id10368",
            "id10369",
            "id10370",
            "id10371",
            "id10372",
            "id10373",
            "id10374",
            "id10375",
            "id10376",
            "id10377",
            "id10378",
            "id10379",
            "id10380",
            "id10381",
            "id10382",
            "id10383",
            "id10384",
            "id10385",
            "id10386",
            "id10387",
            "id10388",
            "id10389",
            "id10390",
            "id10391",
            "id10392",
            "id10393",
            "id10394",
            "id10395",
            "id10396",
            "id10397",
            "id10398",
            "id10399",
            "id10400",
            "id10401",
            "id10402",
            "id10403",
            "id10404",
            "id10405",
            "id10406",
            "id10407",
            "id10408",
            "id10409",
            "id10410",
            "id10411",
            "id10412",
            "id10413",
            "id10414",
            "id10415",
            "id10416",
            "id10417",
            "id10418",
            "id10419",
            "id10420",
            "id10421",
            "id10422",
            "id10423",
            "id10424",
            "id10425",
            "id10426",
            "id10427",
            "id10428",
            "id10429",
            "id10430",
            "id10431",
            "id10432",
            "id10433",
            "id10434",
            "id10435",
            "id10436",
            "id10437",
            "id10438",
            "id10439",
            "id10440",
            "id10441",
            "id10442",
            "id10443",
            "id10444",
            "id10445",
            "id10446",
            "id10447",
            "id10448",
            "id10449",
            "id10450",
            "id10451",
            "id10452",
            "id10453",
            "id10454",
            "id10455",
            "id10456",
            "id10457",
            "id10458",
            "id10459",
            "id10460",
            "id10461",
            "id10462",
            "id10463",
            "id10464",
            "id10465",
            "id10466",
            "id10467",
            "id10468",
            "id10469",
            "id10470",
            "id10471",
            "id10472",
            "id10473",
            "id10474",
            "id10475",
            "id10476",
            "id10477",
            "id10478",
            "id10479",
            "id10480",
            "id10481",
            "id10482",
            "id10483",
            "id10484",
            "id10485",
            "id10486",
            "id10487",
            "id10488",
            "id10489",
            "id10490",
            "id10491",
            "id10492",
            "id10493",
            "id10494",
            "id10495",
            "id10496",
            "id10497",
            "id10498",
            "id10499",
            "id10500",
            "id10501",
            "id10502",
            "id10503",
            "id10504",
            "id10505",
            "id10506",
            "id10507",
            "id10508",
            "id10509",
            "id10510",
            "id10511",
            "id10512",
            "id10513",
            "id10514",
            "id10515",
            "id10516",
            "id10517",
            "id10518",
            "id10519",
            "id10520",
            "id10521",
            "id10522",
            "id10523",
            "id10524",
            "id10525",
            "id10526",
            "id10527",
            "id10528",
            "id10529",
            "id10530",
            "id10531",
            "id10532",
            "id10533",
            "id10534",
            "id10535",
            "id10536",
            "id10537",
            "id10538",
            "id10539",
            "id10540",
            "id10541",
            "id10542",
            "id10543",
            "id10544",
            "id10545",
            "id10546",
            "id10547",
            "id10548",
            "id10549",
            "id10550",
            "id10551",
            "id10552",
            "id10553",
            "id10554",
            "id10555",
            "id10556",
            "id10557",
            "id10558",
            "id10559",
            "id10560",
            "id10561",
            "id10562",
            "id10563",
            "id10564",
            "id10565",
            "id10566",
            "id10567",
            "id10568",
            "id10569",
            "id10570",
            "id10571",
            "id10572",
            "id10573",
            "id10574",
            "id10575",
            "id10576",
            "id10577",
            "id10578",
            "id10579",
            "id10580",
            "id10581",
            "id10582",
            "id10583",
            "id10584",
            "id10585",
            "id10586",
            "id10587",
            "id10588",
            "id10589",
            "id10590",
            "id10591",
            "id10592",
            "id10593",
            "id10594",
            "id10595",
            "id10596",
            "id10597",
            "id10598",
            "id10599",
            "id10600",
            "id10601",
            "id10602",
            "id10603",
            "id10604",
            "id10605",
            "id10606",
            "id10607",
            "id10608",
            "id10609",
            "id10610",
            "id10611",
            "id10612",
            "id10613",
            "id10614",
            "id10615",
            "id10616",
            "id10617",
            "id10618",
            "id10619",
            "id10620",
            "id10621",
            "id10622",
            "id10623",
            "id10624",
            "id10625",
            "id10626",
            "id10627",
            "id10628",
            "id10629",
            "id10630",
            "id10631",
            "id10632",
            "id10633",
            "id10634",
            "id10635",
            "id10636",
            "id10637",
            "id10638",
            "id10639",
            "id10640",
            "id10641",
            "id10642",
            "id10643",
            "id10644",
            "id10645",
            "id10646",
            "id10647",
            "id10648",
            "id10649",
            "id10650",
            "id10651",
            "id10652",
            "id10653",
            "id10654",
            "id10655",
            "id10656",
            "id10657",
            "id10658",
            "id10659",
            "id10660",
            "id10661",
            "id10662",
            "id10663",
            "id10664",
            "id10665",
            "id10666",
            "id10667",
            "id10668",
            "id10669",
            "id10670",
            "id10671",
            "id10672",
            "id10673",
            "id10674",
            "id10675",
            "id10676",
            "id10677",
            "id10678",
            "id10679",
            "id10680",
            "id10681",
            "id10682",
            "id10683",
            "id10684",
            "id10685",
            "id10686",
            "id10687",
            "id10688",
            "id10689",
            "id10690",
            "id10691",
            "id10692",
            "id10693",
            "id10694",
            "id10695",
            "id10696",
            "id10697",
            "id10698",
            "id10699",
            "id10700",
            "id10701",
            "id10702",
            "id10703",
            "id10704",
            "id10705",
            "id10706",
            "id10707",
            "id10708",
            "id10709",
            "id10710",
            "id10711",
            "id10712",
            "id10713",
            "id10714",
            "id10715",
            "id10716",
            "id10717",
            "id10718",
            "id10719",
            "id10720",
            "id10721",
            "id10722",
            "id10723",
            "id10724",
            "id10725",
            "id10726",
            "id10727",
            "id10728",
            "id10729",
            "id10730",
            "id10731",
            "id10732",
            "id10733",
            "id10734",
            "id10735",
            "id10736",
            "id10737",
            "id10738",
            "id10739",
            "id10740",
            "id10741",
            "id10742",
            "id10743",
            "id10744",
            "id10745",
            "id10746",
            "id10747",
            "id10748",
            "id10749",
            "id10750",
            "id10751",
            "id10752",
            "id10753",
            "id10754",
            "id10755",
            "id10756",
            "id10757",
            "id10758",
            "id10759",
            "id10760",
            "id10761",
            "id10762",
            "id10763",
            "id10764",
            "id10765",
            "id10766",
            "id10767",
            "id10768",
            "id10769",
            "id10770",
            "id10771",
            "id10772",
            "id10773",
            "id10774",
            "id10775",
            "id10776",
            "id10777",
            "id10778",
            "id10779",
            "id10780",
            "id10781",
            "id10782",
            "id10783",
            "id10784",
            "id10785",
            "id10786",
            "id10787",
            "id10788",
            "id10789",
            "id10790",
            "id10791",
            "id10792",
            "id10793",
            "id10794",
            "id10795",
            "id10796",
            "id10797",
            "id10798",
            "id10799",
            "id10800",
            "id10801",
            "id10802",
            "id10803",
            "id10804",
            "id10805",
            "id10806",
            "id10807",
            "id10808",
            "id10809",
            "id10810",
            "id10811",
            "id10812",
            "id10813",
            "id10814",
            "id10815",
            "id10816",
            "id10817",
            "id10818",
            "id10819",
            "id10820",
            "id10821",
            "id10822",
            "id10823",
            "id10824",
            "id10825",
            "id10826",
            "id10827",
            "id10828",
            "id10829",
            "id10830",
            "id10831",
            "id10832",
            "id10833",
            "id10834",
            "id10835",
            "id10836",
            "id10837",
            "id10838",
            "id10839",
            "id10840",
            "id10841",
            "id10842",
            "id10843",
            "id10844",
            "id10845",
            "id10846",
            "id10847",
            "id10848",
            "id10849",
            "id10850",
            "id10851",
            "id10852",
            "id10853",
            "id10854",
            "id10855",
            "id10856",
            "id10857",
            "id10858",
            "id10859",
            "id10860",
            "id10861",
            "id10862",
            "id10863",
            "id10864",
            "id10865",
            "id10866",
            "id10867",
            "id10868",
            "id10869",
            "id10870",
            "id10871",
            "id10872",
            "id10873",
            "id10874",
            "id10875",
            "id10876",
            "id10877",
            "id10878",
            "id10879",
            "id10880",
            "id10881",
            "id10882",
            "id10883",
            "id10884",
            "id10885",
            "id10886",
            "id10887",
            "id10888",
            "id10889",
            "id10890",
            "id10891",
            "id10892",
            "id10893",
            "id10894",
            "id10895",
            "id10896",
            "id10897",
            "id10898",
            "id10899",
            "id10900",
            "id10901",
            "id10902",
            "id10903",
            "id10904",
            "id10905",
            "id10906",
            "id10907",
            "id10908",
            "id10909",
            "id10910",
            "id10911",
            "id10912",
            "id10913",
            "id10914",
            "id10915",
            "id10916",
            "id10917",
            "id10918",
            "id10919",
            "id10920",
            "id10921",
            "id10922",
            "id10923",
            "id10924",
            "id10925",
            "id10926",
            "id10927",
            "id10928",
            "id10929",
            "id10930",
            "id10931",
            "id10932",
            "id10933",
            "id10934",
            "id10935",
            "id10936",
            "id10937",
            "id10938",
            "id10939",
            "id10940",
            "id10941",
            "id10942",
            "id10943",
            "id10944",
            "id10945",
            "id10946",
            "id10947",
            "id10948",
            "id10949",
            "id10950",
            "id10951",
            "id10952",
            "id10953",
            "id10954",
            "id10955",
            "id10956",
            "id10957",
            "id10958",
            "id10959",
            "id10960",
            "id10961",
            "id10962",
            "id10963",
            "id10964",
            "id10965",
            "id10966",
            "id10967",
            "id10968",
            "id10969",
            "id10970",
            "id10971",
            "id10972",
            "id10973",
            "id10974",
            "id10975",
            "id10976",
            "id10977",
            "id10978",
            "id10979",
            "id10980",
            "id10981",
            "id10982",
            "id10983",
            "id10984",
            "id10985",
            "id10986",
            "id10987",
            "id10988",
            "id10989",
            "id10990",
            "id10991",
            "id10992",
            "id10993",
            "id10994",
            "id10995",
            "id10996",
            "id10997",
            "id10998",
            "id10999",
            "id11000",
            "id11001",
            "id11002",
            "id11003",
            "id11004",
            "id11005",
            "id11006",
            "id11007",
            "id11008",
            "id11009",
            "id11010",
            "id11011",
            "id11012",
            "id11013",
            "id11014",
            "id11015",
            "id11016",
            "id11017",
            "id11018",
            "id11019",
            "id11020",
            "id11021",
            "id11022",
            "id11023",
            "id11024",
            "id11025",
            "id11026",
            "id11027",
            "id11028",
            "id11029",
            "id11030",
            "id11031",
            "id11032",
            "id11033",
            "id11034",
            "id11035",
            "id11036",
            "id11037",
            "id11038",
            "id11039",
            "id11040",
            "id11041",
            "id11042",
            "id11043",
            "id11044",
            "id11045",
            "id11046",
            "id11047",
            "id11048",
            "id11049",
            "id11050",
            "id11051",
            "id11052",
            "id11053",
            "id11054",
            "id11055",
            "id11056",
            "id11057",
            "id11058",
            "id11059",
            "id11060",
            "id11061",
            "id11062",
            "id11063",
            "id11064",
            "id11065",
            "id11066",
            "id11067",
            "id11068",
            "id11069",
            "id11070",
            "id11071",
            "id11072",
            "id11073",
            "id11074",
            "id11075",
            "id11076",
            "id11077",
            "id11078",
            "id11079",
            "id11080",
            "id11081",
            "id11082",
            "id11083",
            "id11084",
            "id11085",
            "id11086",
            "id11087",
            "id11088",
            "id11089",
            "id11090",
            "id11091",
            "id11092",
            "id11093",
            "id11094",
            "id11095",
            "id11096",
            "id11097",
            "id11098",
            "id11099",
            "id11100",
            "id11101",
            "id11102",
            "id11103",
            "id11104",
            "id11105",
            "id11106",
            "id11107",
            "id11108",
            "id11109",
            "id11110",
            "id11111",
            "id11112",
            "id11113",
            "id11114",
            "id11115",
            "id11116",
            "id11117",
            "id11118",
            "id11119",
            "id11120",
            "id11121",
            "id11122",
            "id11123",
            "id11124",
            "id11125",
            "id11126",
            "id11127",
            "id11128",
            "id11129",
            "id11130",
            "id11131",
            "id11132",
            "id11133",
            "id11134",
            "id11135",
            "id11136",
            "id11137",
            "id11138",
            "id11139",
            "id11140",
            "id11141",
            "id11142",
            "id11143",
            "id11144",
            "id11145",
            "id11146",
            "id11147",
            "id11148",
            "id11149",
            "id11150",
            "id11151",
            "id11152",
            "id11153",
            "id11154",
            "id11155",
            "id11156",
            "id11157",
            "id11158",
            "id11159",
            "id11160",
            "id11161",
            "id11162",
            "id11163",
            "id11164",
            "id11165",
            "id11166",
            "id11167",
            "id11168",
            "id11169",
            "id11170",
            "id11171",
            "id11172",
            "id11173",
            "id11174",
            "id11175",
            "id11176",
            "id11177",
            "id11178",
            "id11179",
            "id11180",
            "id11181",
            "id11182",
            "id11183",
            "id11184",
            "id11185",
            "id11186",
            "id11187",
            "id11188",
            "id11189",
            "id11190",
            "id11191",
            "id11192",
            "id11193",
            "id11194",
            "id11195",
            "id11196",
            "id11197",
            "id11198",
            "id11199",
            "id11200",
            "id11201",
            "id11202",
            "id11203",
            "id11204",
            "id11205",
            "id11206",
            "id11207",
            "id11208",
            "id11209",
            "id11210",
            "id11211",
            "id11212",
            "id11213",
            "id11214",
            "id11215",
            "id11216",
            "id11217",
            "id11218",
            "id11219",
            "id11220",
            "id11221",
            "id11222",
            "id11223",
            "id11224",
            "id11225",
            "id11226",
            "id11227",
            "id11228",
            "id11229",
            "id11230",
            "id11231",
            "id11232",
            "id11233",
            "id11234",
            "id11235",
            "id11236",
            "id11237",
            "id11238",
            "id11239",
            "id11240",
            "id11241",
            "id11242",
            "id11243",
            "id11244",
            "id11245",
            "id11246",
            "id11247",
            "id11248",
            "id11249",
            "id11250",
            "id11251"
        ],
        "names_file": null,
        "id": null,
        "_type": "ClassLabel"
    }
}
```


