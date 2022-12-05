<div itemscope itemtype="http://schema.org/Dataset">
  <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
    <meta itemprop="name" content="TensorFlow Datasets" />
  </div>
  <meta itemprop="name" content="cardiotox" />
  <meta itemprop="description" content="Drug Cardiotoxicity dataset [1-2] is a molecule classification task to detect&#10;cardiotoxicity caused by binding hERG target, a protein associated with heart&#10;beat rhythm. The data covers over 9000 molecules with hERG activity.&#10;&#10;Note:&#10;&#10;1. The data is split into four splits: train, test-iid, test-ood1, test-ood2.&#10;&#10;2. Each molecule in the dataset has 2D graph annotations which is designed to&#10;facilitate graph neural network modeling. Nodes are the atoms of the molecule&#10;and edges are the bonds. Each atom is represented as a vector encoding basic&#10;atom information such as atom type. Similar logic applies to bonds.&#10;&#10;3. We include Tanimoto fingerprint distance (to training data) for each molecule&#10;in the test sets to facilitate research on distributional shift in graph domain.&#10;&#10;For each example, the features include:&#10;  atoms: a 2D tensor with shape (60, 27) storing node features. Molecules with&#10;    less than 60 atoms are padded with zeros. Each atom has 27 atom features.&#10;  pairs: a 3D tensor with shape (60, 60, 12) storing edge features. Each edge&#10;    has 12 edge features.&#10;  atom_mask: a 1D tensor with shape (60, ) storing node masks. 1 indicates the&#10;    corresponding atom is real, othewise a padded one.&#10;  pair_mask: a 2D tensor with shape (60, 60) storing edge masks. 1 indicates the&#10;    corresponding edge is real, othewise a padded one.&#10;  active: a one-hot vector indicating if the molecule is toxic or not. [0, 1]&#10;    indicates it&#x27;s toxic, otherwise [1, 0] non-toxic.&#10;&#10;&#10;## References&#10;[1]: V. B. Siramshetty et al. Critical Assessment of Artificial Intelligence&#10;Methods for Prediction of hERG Channel Inhibition in the Big Data Era.&#10;    JCIM, 2020. https://pubs.acs.org/doi/10.1021/acs.jcim.0c00884&#10;&#10;[2]: K. Han et al. Reliable Graph Neural Networks for Drug Discovery Under&#10;Distributional Shift.&#10;    NeurIPS DistShift Workshop 2021. https://arxiv.org/abs/2111.12951&#10;&#10;To use this dataset:&#10;&#10;```python&#10;import tensorflow_datasets as tfds&#10;&#10;ds = tfds.load(&#x27;cardiotox&#x27;, split=&#x27;train&#x27;)&#10;for ex in ds.take(4):&#10;  print(ex)&#10;```&#10;&#10;See [the guide](https://www.tensorflow.org/datasets/overview) for more&#10;informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).&#10;&#10;" />
  <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/cardiotox" />
  <meta itemprop="sameAs" content="https://github.com/google/uncertainty-baselines/tree/main/baselines/drug_cardiotoxicity" />
  <meta itemprop="citation" content="@ARTICLE{Han2021-tu,&#10;  title         = &quot;Reliable Graph Neural Networks for Drug Discovery Under&#10;                   Distributional Shift&quot;,&#10;  author        = &quot;Han, Kehang and Lakshminarayanan, Balaji and Liu, Jeremiah&quot;,&#10;  month         =  nov,&#10;  year          =  2021,&#10;  archivePrefix = &quot;arXiv&quot;,&#10;  primaryClass  = &quot;cs.LG&quot;,&#10;  eprint        = &quot;2111.12951&quot;&#10;}" />
</div>

# `cardiotox`


*   **Description**:

Drug Cardiotoxicity dataset [1-2] is a molecule classification task to detect
cardiotoxicity caused by binding hERG target, a protein associated with heart
beat rhythm. The data covers over 9000 molecules with hERG activity.

Note:

1.  The data is split into four splits: train, test-iid, test-ood1, test-ood2.

2.  Each molecule in the dataset has 2D graph annotations which is designed to
    facilitate graph neural network modeling. Nodes are the atoms of the
    molecule and edges are the bonds. Each atom is represented as a vector
    encoding basic atom information such as atom type. Similar logic applies to
    bonds.

3.  We include Tanimoto fingerprint distance (to training data) for each
    molecule in the test sets to facilitate research on distributional shift in
    graph domain.

For each example, the features include: atoms: a 2D tensor with shape (60, 27)
storing node features. Molecules with less than 60 atoms are padded with zeros.
Each atom has 27 atom features. pairs: a 3D tensor with shape (60, 60, 12)
storing edge features. Each edge has 12 edge features. atom_mask: a 1D tensor
with shape (60, ) storing node masks. 1 indicates the corresponding atom is
real, othewise a padded one. pair_mask: a 2D tensor with shape (60, 60) storing
edge masks. 1 indicates the corresponding edge is real, othewise a padded one.
active: a one-hot vector indicating if the molecule is toxic or not. [0, 1]
indicates it's toxic, otherwise [1, 0] non-toxic.

## References

\[1]: V. B. Siramshetty et al. Critical Assessment of Artificial Intelligence
Methods for Prediction of hERG Channel Inhibition in the Big Data Era. JCIM,
2020. https://pubs.acs.org/doi/10.1021/acs.jcim.0c00884

\[2]: K. Han et al. Reliable Graph Neural Networks for Drug Discovery Under
Distributional Shift. NeurIPS DistShift Workshop 2021.
https://arxiv.org/abs/2111.12951

*   **Homepage**:
    [https://github.com/google/uncertainty-baselines/tree/main/baselines/drug_cardiotoxicity](https://github.com/google/uncertainty-baselines/tree/main/baselines/drug_cardiotoxicity)

*   **Source code**:
    [`tfds.graphs.cardiotox.Cardiotox`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/graphs/cardiotox/cardiotox.py)

*   **Versions**:

    *   **`1.0.0`** (default): Initial release.

*   **Download size**: `Unknown size`

*   **Dataset size**: `1.66 GiB`

*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    No

*   **Splits**:

Split          | Examples
:------------- | -------:
`'test'`       | 839
`'test2'`      | 177
`'train'`      | 6,523
`'validation'` | 1,631

*   **Feature structure**:

```python
FeaturesDict({
    'active': Tensor(shape=(2,), dtype=int64),
    'atom_mask': Tensor(shape=(60,), dtype=float32),
    'atoms': Tensor(shape=(60, 27), dtype=float32),
    'dist2topk_nbs': Tensor(shape=(1,), dtype=float32),
    'molecule_id': string,
    'pair_mask': Tensor(shape=(60, 60), dtype=float32),
    'pairs': Tensor(shape=(60, 60, 12), dtype=float32),
})
```

*   **Feature documentation**:

Feature       | Class        | Shape        | Dtype   | Description
:------------ | :----------- | :----------- | :------ | :----------
              | FeaturesDict |              |         |
active        | Tensor       | (2,)         | int64   |
atom_mask     | Tensor       | (60,)        | float32 |
atoms         | Tensor       | (60, 27)     | float32 |
dist2topk_nbs | Tensor       | (1,)         | float32 |
molecule_id   | Tensor       |              | string  |
pair_mask     | Tensor       | (60, 60)     | float32 |
pairs         | Tensor       | (60, 60, 12) | float32 |

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
const url = "https://storage.googleapis.com/tfds-data/visualization/dataframe/cardiotox-1.0.0.html";
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
@ARTICLE{Han2021-tu,
  title         = "Reliable Graph Neural Networks for Drug Discovery Under
                   Distributional Shift",
  author        = "Han, Kehang and Lakshminarayanan, Balaji and Liu, Jeremiah",
  month         =  nov,
  year          =  2021,
  archivePrefix = "arXiv",
  primaryClass  = "cs.LG",
  eprint        = "2111.12951"
}
```

