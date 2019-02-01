"""Parsing functions for Binvox files.

https://www.patrickmin.com/binvox/binvox.html
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import collections
Binvox = collections.namedtuple('Binvox', ['rle', 'dims', 'translate', 'scale'])


def parse_binvox_header(fp):
  """Read the header from a binvox file.

  Spec at https://www.patrickmin.com/binvox/binvox.html

  Args:
    fp: object providing a `readline` method (e.g. an open file)

  Returns:
    (dims, translate, scale) according to binvox spec

  Raises:
    `IOError` if invalid binvox file.
  """

  line = fp.readline().strip()
  if not line.startswith(b'#binvox'):
    raise IOError('Not a binvox file')
  dims = tuple(int(s) for s in fp.readline().strip().split(b' ')[1:])
  translate = tuple(float(s) for s in fp.readline().strip().split(b' ')[1:])
  scale = float(fp.readline().strip().split(b' ')[1])
  fp.readline()
  return dims, translate, scale


def parse_binvox(fp):
  """Read a binvox file.

  Spec at https://www.patrickmin.com/binvox/binvox.html

  Args:
    fp: object providing a `readline` method (e.g. an open file)

  Returns:
    `Binvox` object (namedtuple with ['rle', 'dims', 'translate', 'scale'])
    `rle` is the run length encoding of the values.

  Raises:
    `IOError` if invalid binvox file.
  """
  dims, translate, scale = parse_binvox_header(fp)
  rle = np.frombuffer(fp.read(), dtype=np.uint8)
  return Binvox(rle, dims, translate, scale)
