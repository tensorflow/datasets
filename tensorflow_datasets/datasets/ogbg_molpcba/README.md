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

[1]: Greg Landrum, et al. 'RDKit: Open-source cheminformatics'. URL:
https://github.com/rdkit/rdkit

[2]: Bharath Ramsundar, Steven Kearnes, Patrick Riley, Dale Webster, David
Konerding and Vijay Pande. 'Massively Multitask Networks for Drug Discovery'.
URL: https://arxiv.org/pdf/1502.02072.pdf

[3]: Zhenqin Wu, Bharath Ramsundar, Evan N Feinberg, Joseph Gomes, Caleb
Geniesse, Aneesh S. Pappu, Karl Leswing, and Vijay Pande. MoleculeNet: a
benchmark for molecular machine learning. Chemical Science, 9(2):513-530, 2018.
