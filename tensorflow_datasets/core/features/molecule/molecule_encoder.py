"""MoleculeEncoders convert between SMILES representation and SMILES, InChI, or
  graph representations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import abc
import six

from rdkit import Chem


@six.add_metaclass(abc.ABCMeta)
class MoleculeEncoder(object):
  """Abstract base class for converting between SMILES representation
    and other molecule representations such as molecular fingerprint(MF) or 
    graph.
  """
  @abc.abstractmethod
  def encode(self, smiles):
    """Encodes SMILES representation into SMILES, MF, or graph 
      representation."""
    raise NotImplementedError


class MFEncoder(MoleculeEncoder):
  """Encodes SMILES representation to Molecular Fingerprint (MF)."""

  def __init__(self):
    """Construcsts MFEncoder.

    Args:
    """

  def encode(self, smiles):
    """Encodes SMILES representation to MF.

    Args:
      smiles: `str`, SMILES representation of a molecule.

    Returns:
      inchi: `str`, InChI representation for a valid SMILES representation,
        `None`for invalid SMILES representation.
    """
