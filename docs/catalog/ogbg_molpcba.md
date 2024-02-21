<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="ogbg_molpcba" />
  <meta itemprop="description" content="&#x27;ogbg-molpcba&#x27; is a molecular dataset sampled from PubChem BioAssay. It is a&#10;graph prediction dataset from the Open Graph Benchmark (OGB).&#10;&#10;This dataset is experimental, and the API is subject to change in future&#10;releases.&#10;&#10;The below description of the dataset is adapted from the OGB paper:&#10;&#10;### Input Format&#10;&#10;All the molecules are pre-processed using RDKit ([1]).&#10;&#10;*   Each graph represents a molecule, where nodes are atoms, and edges are&#10;    chemical bonds.&#10;*   Input node features are 9-dimensional, containing atomic number and&#10;    chirality, as well as other additional atom features such as formal charge&#10;    and whether the atom is in the ring.&#10;*   Input edge features are 3-dimensional, containing bond type, bond&#10;    stereochemistry, as well as an additional bond feature indicating whether&#10;    the bond is conjugated.&#10;&#10;The exact description of all features is available at&#10;https://github.com/snap-stanford/ogb/blob/master/ogb/utils/features.py.&#10;&#10;### Prediction&#10;&#10;The task is to predict 128 different biological activities (inactive/active).&#10;See [2] and [3] for more description about these targets. Not all targets apply&#10;to each molecule: missing targets are indicated by NaNs.&#10;&#10;### References&#10;&#10;[1]: Greg Landrum, et al. &#x27;RDKit: Open-source cheminformatics&#x27;. URL:&#10;https://github.com/rdkit/rdkit&#10;&#10;[2]: Bharath Ramsundar, Steven Kearnes, Patrick Riley, Dale Webster, David&#10;Konerding and Vijay Pande. &#x27;Massively Multitask Networks for Drug Discovery&#x27;.&#10;URL: https://arxiv.org/pdf/1502.02072.pdf&#10;&#10;[3]: Zhenqin Wu, Bharath Ramsundar, Evan N Feinberg, Joseph Gomes, Caleb&#10;Geniesse, Aneesh S. Pappu, Karl Leswing, and Vijay Pande. MoleculeNet: a&#10;benchmark for molecular machine learning. Chemical Science, 9(2):513-530, 2018.&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;ogbg_molpcba&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;&lt;img src=&quot;https://storage.googleapis.com/tfds-data/visualization/fig/ogbg_molpcba-0.1.3.png&quot; alt=&quot;Visualization&quot; width=&quot;500px&quot;&gt;&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/ogbg_molpcba" />
  <meta itemprop="sameAs" content="https://ogb.stanford.edu/docs/graphprop" />
  <meta itemprop="citation" content="@inproceedings{DBLP:conf/nips/HuFZDRLCL20,&#10;  author    = {Weihua Hu and&#10;               Matthias Fey and&#10;               Marinka Zitnik and&#10;               Yuxiao Dong and&#10;               Hongyu Ren and&#10;               Bowen Liu and&#10;               Michele Catasta and&#10;               Jure Leskovec},&#10;  editor    = {Hugo Larochelle and&#10;               Marc Aurelio Ranzato and&#10;               Raia Hadsell and&#10;               Maria{-}Florina Balcan and&#10;               Hsuan{-}Tien Lin},&#10;  title     = {Open Graph Benchmark: Datasets for Machine Learning on Graphs},&#10;  booktitle = {Advances in Neural Information Processing Systems 33: Annual Conference&#10;               on Neural Information Processing Systems 2020, NeurIPS 2020, December&#10;               6-12, 2020, virtual},&#10;  year      = {2020},&#10;  url       = {https://proceedings.neurips.cc/paper/2020/hash/fb60d411a5c5b72b2e7d3527cfc84fd0-Abstract.html},&#10;  timestamp = {Tue, 19 Jan 2021 15:57:06 +0100},&#10;  biburl    = {https://dblp.org/rec/conf/nips/HuFZDRLCL20.bib},&#10;  bibsource = {dblp computer science bibliography, https://dblp.org}&#10;}" />
</div>

# `ogbg_molpcba`


*   **Description**:

'ogbg-molpcba' is a molecular dataset sampled from PubChem BioAssay. It is a
graph prediction dataset from the Open Graph Benchmark (OGB).

This dataset is experimental, and the API is subject to change in future
releases.

The below description of the dataset is adapted from the OGB paper:

### Input Format

All the molecules are pre-processed using RDKit ([1]).

*   Each graph represents a molecule, where nodes are atoms, and edges are
    chemical bonds.
*   Input node features are 9-dimensional, containing atomic number and
    chirality, as well as other additional atom features such as formal charge
    and whether the atom is in the ring.
*   Input edge features are 3-dimensional, containing bond type, bond
    stereochemistry, as well as an additional bond feature indicating whether
    the bond is conjugated.

The exact description of all features is available at
https://github.com/snap-stanford/ogb/blob/master/ogb/utils/features.py.

### Prediction

The task is to predict 128 different biological activities (inactive/active).
See [2] and [3] for more description about these targets. Not all targets apply
to each molecule: missing targets are indicated by NaNs.

### References

\[1]: Greg Landrum, et al. 'RDKit: Open-source cheminformatics'. URL:
https://github.com/rdkit/rdkit

\[2]: Bharath Ramsundar, Steven Kearnes, Patrick Riley, Dale Webster, David
Konerding and Vijay Pande. 'Massively Multitask Networks for Drug Discovery'.
URL: https://arxiv.org/pdf/1502.02072.pdf

\[3]: Zhenqin Wu, Bharath Ramsundar, Evan N Feinberg, Joseph Gomes, Caleb
Geniesse, Aneesh S. Pappu, Karl Leswing, and Vijay Pande. MoleculeNet: a
benchmark for molecular machine learning. Chemical Science, 9(2):513-530, 2018.

*   **Homepage**:
    [https://ogb.stanford.edu/docs/graphprop](https://ogb.stanford.edu/docs/graphprop)

*   **Source code**:
    [`tfds.datasets.ogbg_molpcba.Builder`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/ogbg_molpcba/ogbg_molpcba_dataset_builder.py)

*   **Versions**:

    *   `0.1.0`: Initial release of experimental API.
    *   `0.1.1`: Exposes the number of edges in each graph explicitly.
    *   `0.1.2`: Add metadata field for GraphVisualizer.
    *   **`0.1.3`** (default): Add metadata field for names of individual tasks.

*   **Download size**: `37.70 MiB`

*   **Dataset size**: `822.53 MiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 43,793
`'train'`      | 350,343
`'validation'` | 43,793

*   **Feature structure**:

```python
FeaturesDict({
    'edge_feat': Tensor(shape=(None, 3), dtype=float32),
    'edge_index': Tensor(shape=(None, 2), dtype=int64),
    'labels': Tensor(shape=(128,), dtype=float32),
    'node_feat': Tensor(shape=(None, 9), dtype=float32),
    'num_edges': Tensor(shape=(None,), dtype=int64),
    'num_nodes': Tensor(shape=(None,), dtype=int64),
})
```

*   **Feature documentation**:

Feature    | Class        | Shape     | Dtype   | Description
:--------- | :----------- | :-------- | :------ | :----------
           | FeaturesDict |           |         |
edge_feat  | Tensor       | (None, 3) | float32 |
edge_index | Tensor       | (None, 2) | int64   |
labels     | Tensor       | (128,)    | float32 |
node_feat  | Tensor       | (None, 9) | float32 |
num_edges  | Tensor       | (None,)   | int64   |
num_nodes  | Tensor       | (None,)   | int64   |

*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `None`

*   **Figure**
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples)):

<img src="https://storage.googleapis.com/tfds-data/visualization/fig/ogbg_molpcba-0.1.3.png" alt="Visualization" width="500px">

*   **Examples**
    ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe)):

<!-- mdformat off(HTML should not be auto-formatted) -->

{% framebox %}

<button id="displaydataframe">Display examples...</button>
<div id="dataframecontent" style="overflow-x:auto"></div>
<script>
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/ogbg_molpcba-0.1.3.html";
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
@inproceedings{DBLP:conf/nips/HuFZDRLCL20,
  author    = {Weihua Hu and
               Matthias Fey and
               Marinka Zitnik and
               Yuxiao Dong and
               Hongyu Ren and
               Bowen Liu and
               Michele Catasta and
               Jure Leskovec},
  editor    = {Hugo Larochelle and
               Marc Aurelio Ranzato and
               Raia Hadsell and
               Maria{-}Florina Balcan and
               Hsuan{-}Tien Lin},
  title     = {Open Graph Benchmark: Datasets for Machine Learning on Graphs},
  booktitle = {Advances in Neural Information Processing Systems 33: Annual Conference
               on Neural Information Processing Systems 2020, NeurIPS 2020, December
               6-12, 2020, virtual},
  year      = {2020},
  url       = {https://proceedings.neurips.cc/paper/2020/hash/fb60d411a5c5b72b2e7d3527cfc84fd0-Abstract.html},
  timestamp = {Tue, 19 Jan 2021 15:57:06 +0100},
  biburl    = {https://dblp.org/rec/conf/nips/HuFZDRLCL20.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

