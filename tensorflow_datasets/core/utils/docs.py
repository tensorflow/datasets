# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Documentation utils for the website.

Note: To be detected, doc decorators should be applied between descriptors
and other decorators.

```py
class A:

  @staticmethod
  @tfds.core.utils.docs.deprecated
  @other_decorator
  def f():
    pass
```

The functions exposed below are dummy decorators. This allows not having to load
TensorFlow. The functions are monkey patched when needed in
scripts/documentation/build_api_docs.py with actual TensorFlow documentation
decorators.
"""

from typing import Any, TypeVar

_T = TypeVar('_T')


# Some TensorFlow documentation decorators used to obfuscate typing: b/262340871
def _no_op_decorator_without_type(obj) -> Any:
  return obj


def _no_op_decorator(obj: _T) -> _T:
  return obj


deprecated = _no_op_decorator_without_type
doc_private = _no_op_decorator
do_not_doc = _no_op_decorator
do_not_doc_inheritable = _no_op_decorator
do_not_doc_in_subclasses = _no_op_decorator_without_type
