# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Convert QM9 dataset to tensorflow_datasets (tfds) format.

This module converts the QM9 dataset (Ramakrishnan et al, "Quantum chemistry
structures and properties of 134 kilo molecules", Scientific Data, 2014) to
tensorflow_datasets (tfds).

To build the dataset, run the following from directory containing this file:
$ tfds build.
"""
import re

from typing import Any, Dict, Iterable, Tuple
import numpy as np
import tensorflow_datasets.public_api as tfds

pd = tfds.core.lazy_imports.pandas

_HOMEPAGE = 'https://doi.org/10.6084/m9.figshare.c.978904.v5'

_ATOMREF_URL = 'https://figshare.com/ndownloader/files/3195395'
_UNCHARACTERIZED_URL = 'https://springernature.figshare.com/ndownloader/files/3195404'
_MOLECULES_URL = 'https://springernature.figshare.com/ndownloader/files/3195389'

_SIZE = 133_885
_CHARACTERIZED_SIZE = 130_831

_MAX_ATOMS = 29
_CHARGES = {'H': 1, 'C': 6, 'N': 7, 'O': 8, 'F': 9}
_LABELS = ['tag', 'index', 'A', 'B', 'C', 'mu', 'alpha', 'homo', 'lumo', 'gap',
           'r2', 'zpve', 'U0', 'U', 'H', 'G', 'Cv']
# For each of these targets, we will add a second target with an
# _atomization suffix that has the thermo term subtracted.
_ATOMIZATION_TARGETS = ['U0', 'U', 'H', 'G']


def _process_molecule(atomref, fname):
  """Read molecule data from file."""
  with open(fname, 'r') as f:
    lines = f.readlines()
  num_atoms = int(lines[0].rstrip())
  frequencies = re.split(r'\s+', lines[num_atoms + 2].rstrip())
  smiles = re.split(r'\s+', lines[num_atoms + 3].rstrip())
  inchi = re.split(r'\s+', lines[num_atoms + 4].rstrip())

  labels = pd.read_table(fname,
                         skiprows=1,
                         nrows=1,
                         sep=r'\s+',
                         names=_LABELS)

  atoms = pd.read_table(fname,
                        skiprows=2,
                        nrows=num_atoms,
                        sep=r'\s+',
                        names=['Z', 'x', 'y', 'z', 'Mulliken_charge'])

  # Correct exponential notation (6.8*^-6 -> 6.8e-6).
  for key in ['x', 'y', 'z', 'Mulliken_charge']:
    if atoms[key].values.dtype == 'object':
      # there are unrecognized numbers.
      atoms[key].values[:] = np.array([
          float(x.replace('*^', 'e'))
          for i, x in enumerate(atoms[key].values)])

  charges = np.pad([_CHARGES[v] for v in atoms['Z'].values],
                   (0, _MAX_ATOMS - num_atoms))
  positions = np.stack([atoms['x'].values,
                        atoms['y'].values,
                        atoms['z'].values], axis=-1).astype(np.float32)
  positions = np.pad(positions, ((0, _MAX_ATOMS - num_atoms), (0, 0)))

  mulliken_charges = atoms['Mulliken_charge'].values.astype(np.float32)
  mulliken_charges = np.pad(mulliken_charges, ((0, _MAX_ATOMS - num_atoms)))

  example = {'num_atoms': num_atoms,
             'charges': charges,
             'Mulliken_charges': mulliken_charges,
             'positions': positions.astype(np.float32),
             'frequencies': frequencies,
             'SMILES': smiles[0],
             'SMILES_relaxed': smiles[1],
             'InChI': inchi[0],
             'InChI_relaxed': inchi[1],
             **{k: labels[k].values[0] for k in _LABELS}}

  # Create atomization targets by subtracting thermochemical energy of
  # each atom.
  for k in _ATOMIZATION_TARGETS:
    v = atomref[k]
    thermo = 0
    for z in atoms['Z'].values:
      thermo += v[z]
    example[f'{k}_atomization'] = example[k] - thermo

  return example


def _get_valid_ids(uncharacterized):
  """Get valid ids."""
  # Original data files are  1-indexed.
  characterized_ids = np.array(sorted(set(range(1, _SIZE + 1)) -
                                      set(uncharacterized)))
  assert len(characterized_ids) == _CHARACTERIZED_SIZE
  return characterized_ids


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for QM9 dataset. See superclass for details."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        disable_shuffling=True,
        features=tfds.features.FeaturesDict({
            'num_atoms': tfds.features.Tensor(shape=(), dtype=np.int64),
            'charges': tfds.features.Tensor(shape=(29,), dtype=np.int64),
            'Mulliken_charges': tfds.features.Tensor(
                shape=(29,), dtype=np.float32
            ),
            'positions': tfds.features.Tensor(shape=(29, 3), dtype=np.float32),
            'index': tfds.features.Tensor(shape=(), dtype=np.int64),
            'A': tfds.features.Tensor(shape=(), dtype=np.float32),
            'B': tfds.features.Tensor(shape=(), dtype=np.float32),
            'C': tfds.features.Tensor(shape=(), dtype=np.float32),
            'mu': tfds.features.Tensor(shape=(), dtype=np.float32),
            'alpha': tfds.features.Tensor(shape=(), dtype=np.float32),
            'homo': tfds.features.Tensor(shape=(), dtype=np.float32),
            'lumo': tfds.features.Tensor(shape=(), dtype=np.float32),
            'gap': tfds.features.Tensor(shape=(), dtype=np.float32),
            'r2': tfds.features.Tensor(shape=(), dtype=np.float32),
            'zpve': tfds.features.Tensor(shape=(), dtype=np.float32),
            'U0': tfds.features.Tensor(shape=(), dtype=np.float32),
            'U': tfds.features.Tensor(shape=(), dtype=np.float32),
            'H': tfds.features.Tensor(shape=(), dtype=np.float32),
            'G': tfds.features.Tensor(shape=(), dtype=np.float32),
            'Cv': tfds.features.Tensor(shape=(), dtype=np.float32),
            'U0_atomization': tfds.features.Tensor(shape=(), dtype=np.float32),
            'U_atomization': tfds.features.Tensor(shape=(), dtype=np.float32),
            'H_atomization': tfds.features.Tensor(shape=(), dtype=np.float32),
            'G_atomization': tfds.features.Tensor(shape=(), dtype=np.float32),
            'tag': tfds.features.Tensor(shape=(), dtype=np.str_),
            'SMILES': tfds.features.Tensor(shape=(), dtype=np.str_),
            'SMILES_relaxed': tfds.features.Tensor(shape=(), dtype=np.str_),
            'InChI': tfds.features.Tensor(shape=(), dtype=np.str_),
            'InChI_relaxed': tfds.features.Tensor(shape=(), dtype=np.str_),
            'frequencies': tfds.features.Tensor(
                shape=(None,), dtype=np.float32
            ),
        }),
        # These are returned if `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=None,
        homepage=_HOMEPAGE,
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager) -> Dict[str, Any]:
    """Returns SplitGenerators. See superclass method for details."""
    atomref = pd.read_table(
        dl_manager.download({'atomref': _ATOMREF_URL})['atomref'],
        skiprows=5,
        index_col='Z',
        skipfooter=1,
        sep=r'\s+',
        names=['Z', 'zpve', 'U0', 'U', 'H', 'G', 'Cv']).to_dict()

    uncharacterized = pd.read_table(
        dl_manager.download(
            {'uncharacterized': _UNCHARACTERIZED_URL})['uncharacterized'],
        skiprows=9,
        skipfooter=1,
        sep=r'\s+',
        usecols=[0],
        names=['index']).values[:, 0]

    molecules_dir = dl_manager.download_and_extract(
        {'dsgdb9nsd': _MOLECULES_URL})['dsgdb9nsd']

    valid_ids = _get_valid_ids(uncharacterized)

    return {'train': self._generate_examples(valid_ids, atomref, molecules_dir)}

  def _generate_examples(
      self,
      split: np.ndarray,
      atomref: Dict[str, Any],
      molecules_dir: Any) -> Iterable[Tuple[int, Dict[str, Any]]]:
    """Dataset generator. See superclass method for details."""

    for i in split:
      entry = _process_molecule(
          atomref, molecules_dir / f'dsgdb9nsd_{i:06d}.xyz')
      yield int(i), entry
