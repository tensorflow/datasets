<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="smart_buildings" />
  <meta itemprop="description" content="# Smart Buildings Dataset&#10;&#10;Dataset accompanying  the paper &quot;Real-World Data and&#10;Calibrated Simulation Suite for Offline Training of&#10;Reinforcement Learning Agents to Optimize Energy and&#10;Emission in Office Buildings&quot; by Judah Goldfeder and&#10;John Sipple, containing 6 years of detailed telemetric&#10;readouts from 3 commercial office buildings.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;smart_buildings&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/smart_buildings" />
  <meta itemprop="sameAs" content="https://github.com/google/sbsim" />
  <meta itemprop="citation" content="// TODO(smart_buildings_dataset): BibTeX citation" />
</div>

# `smart_buildings`


*   **Description**:

# Smart Buildings Dataset

Dataset accompanying the paper "Real-World Data and Calibrated Simulation Suite
for Offline Training of Reinforcement Learning Agents to Optimize Energy and
Emission in Office Buildings" by Judah Goldfeder and John Sipple, containing 6
years of detailed telemetric readouts from 3 commercial office buildings.

*   **Config description**: Building sb1

*   **Homepage**:
    [https://github.com/google/sbsim](https://github.com/google/sbsim)

*   **Source code**:
    [`tfds.datasets.smart_buildings.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/smart_buildings/smart_buildings_dataset_builder.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `10.99 GiB`

*   **Dataset size**: `86.77 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split      | Examples
:--------- | -------:
`'sb1_19'` | 105,120
`'sb1_20'` | 105,408
`'sb1_21'` | 105,120
`'sb1_22'` | 60,480
`'sb1_23'` | 105,120
`'sb1_24'` | 61,344

*   **Feature structure**:

```python
FeaturesDict({
    'action': FeaturesDict({
        'request': FeaturesDict({
            'singleActionRequests': Sequence({
                'continuousValue': Scalar(shape=(), dtype=float32),
                'deviceId': Text(shape=(), dtype=string),
                'setpointName': Text(shape=(), dtype=string),
            }),
            'timestamp': Text(shape=(), dtype=string),
        }),
        'singleActionResponses': Sequence({
            'additionalInfo': Text(shape=(), dtype=string),
            'request': FeaturesDict({
                'continuousValue': Scalar(shape=(), dtype=float32),
                'deviceId': Text(shape=(), dtype=string),
                'setpointName': Text(shape=(), dtype=string),
            }),
            'responseType': Text(shape=(), dtype=string),
        }),
        'timestamp': Text(shape=(), dtype=string),
    }),
    'observation': FeaturesDict({
        'request': FeaturesDict({
            'singleObservationRequests': Sequence({
                'deviceId': Text(shape=(), dtype=string),
                'measurementName': Text(shape=(), dtype=string),
            }),
            'timestamp': Text(shape=(), dtype=string),
        }),
        'singleObservationResponses': Sequence({
            'continuousValue': Scalar(shape=(), dtype=float32),
            'observationValid': Text(shape=(), dtype=string),
            'singleObservationRequest': FeaturesDict({
                'deviceId': Text(shape=(), dtype=string),
                'measurementName': Text(shape=(), dtype=string),
            }),
            'timestamp': Text(shape=(), dtype=string),
        }),
        'timestamp': Text(shape=(), dtype=string),
    }),
    'reward': FeaturesDict({
        'agentRewardValue': Scalar(shape=(), dtype=float32),
        'carbonEmissionWeight': Scalar(shape=(), dtype=float32),
        'carbonEmitted': Scalar(shape=(), dtype=float32),
        'electricityEnergyCost': Scalar(shape=(), dtype=float32),
        'endTimestamp': Text(shape=(), dtype=string),
        'energyCostWeight': Scalar(shape=(), dtype=float32),
        'naturalGasEnergyCost': Scalar(shape=(), dtype=float32),
        'normalizedCarbonEmission': Scalar(shape=(), dtype=float32),
        'normalizedEnergyCost': Scalar(shape=(), dtype=float32),
        'normalizedProductivityRegret': Scalar(shape=(), dtype=float32),
        'personProductivity': Scalar(shape=(), dtype=float32),
        'productivityRegret': Scalar(shape=(), dtype=float32),
        'productivityReward': Scalar(shape=(), dtype=float32),
        'productivityWeight': Scalar(shape=(), dtype=float32),
        'rewardScale': Scalar(shape=(), dtype=float32),
        'startTimestamp': Text(shape=(), dtype=string),
        'totalOccupancy': Scalar(shape=(), dtype=float32),
    }),
})
```

*   **Feature documentation**:

Feature                                                                         | Class        | Shape | Dtype   | Description
:------------------------------------------------------------------------------ | :----------- | :---- | :------ | :----------
                                                                                | FeaturesDict |       |         |
action                                                                          | FeaturesDict |       |         |
action/request                                                                  | FeaturesDict |       |         |
action/request/singleActionRequests                                             | Sequence     |       |         |
action/request/singleActionRequests/continuousValue                             | Scalar       |       | float32 |
action/request/singleActionRequests/deviceId                                    | Text         |       | string  |
action/request/singleActionRequests/setpointName                                | Text         |       | string  |
action/request/timestamp                                                        | Text         |       | string  |
action/singleActionResponses                                                    | Sequence     |       |         |
action/singleActionResponses/additionalInfo                                     | Text         |       | string  |
action/singleActionResponses/request                                            | FeaturesDict |       |         |
action/singleActionResponses/request/continuousValue                            | Scalar       |       | float32 |
action/singleActionResponses/request/deviceId                                   | Text         |       | string  |
action/singleActionResponses/request/setpointName                               | Text         |       | string  |
action/singleActionResponses/responseType                                       | Text         |       | string  |
action/timestamp                                                                | Text         |       | string  |
observation                                                                     | FeaturesDict |       |         |
observation/request                                                             | FeaturesDict |       |         |
observation/request/singleObservationRequests                                   | Sequence     |       |         |
observation/request/singleObservationRequests/deviceId                          | Text         |       | string  |
observation/request/singleObservationRequests/measurementName                   | Text         |       | string  |
observation/request/timestamp                                                   | Text         |       | string  |
observation/singleObservationResponses                                          | Sequence     |       |         |
observation/singleObservationResponses/continuousValue                          | Scalar       |       | float32 |
observation/singleObservationResponses/observationValid                         | Text         |       | string  |
observation/singleObservationResponses/singleObservationRequest                 | FeaturesDict |       |         |
observation/singleObservationResponses/singleObservationRequest/deviceId        | Text         |       | string  |
observation/singleObservationResponses/singleObservationRequest/measurementName | Text         |       | string  |
observation/singleObservationResponses/timestamp                                | Text         |       | string  |
observation/timestamp                                                           | Text         |       | string  |
reward                                                                          | FeaturesDict |       |         |
reward/agentRewardValue                                                         | Scalar       |       | float32 |
reward/carbonEmissionWeight                                                     | Scalar       |       | float32 |
reward/carbonEmitted                                                            | Scalar       |       | float32 |
reward/electricityEnergyCost                                                    | Scalar       |       | float32 |
reward/endTimestamp                                                             | Text         |       | string  |
reward/energyCostWeight                                                         | Scalar       |       | float32 |
reward/naturalGasEnergyCost                                                     | Scalar       |       | float32 |
reward/normalizedCarbonEmission                                                 | Scalar       |       | float32 |
reward/normalizedEnergyCost                                                     | Scalar       |       | float32 |
reward/normalizedProductivityRegret                                             | Scalar       |       | float32 |
reward/personProductivity                                                       | Scalar       |       | float32 |
reward/productivityRegret                                                       | Scalar       |       | float32 |
reward/productivityReward                                                       | Scalar       |       | float32 |
reward/productivityWeight                                                       | Scalar       |       | float32 |
reward/rewardScale                                                              | Scalar       |       | float32 |
reward/startTimestamp                                                           | Text         |       | string  |
reward/totalOccupancy                                                           | Scalar       |       | float32 |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):
    Not supported.

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/smart_buildings-sb1-1.0.0.html";
const dataButton = document.getElementById('displaydataframe');
dataButton.addEventListener('click', async () => {
  // Disable the button after clicking (dataframe loaded only once).
  dataButton.disabled = true;

  const contentPane = document.getElementById('dataframecontent');
  try {
    const response = await fetch(url);
    // Error response codes don't throw an error, so force an error to show
    // the error message.
    if (!response.ok) throw Error(response.statusText);

    const data = await response.text();
    contentPane.innerHTML = data;
  } catch (e) {
    contentPane.innerHTML =
        'Error loading examples. If the error persist, please open '
        + 'a new issue.';
  }
});
</script>

{% endframebox %}

<!-- mdformat on -->

*   **Citation**:

```
// TODO(smart_buildings_dataset): BibTeX citation
```


## smart_buildings/sb1 (default config)
