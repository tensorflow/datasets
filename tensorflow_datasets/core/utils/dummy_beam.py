# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3


_MSG = ("Failed importing {name}. Please install {name}."
                  " Using pip install {name}")


class DoFn(object):
   def __call__(self, *args, **kwargs):
       return None
  
class Pipeline(object):
  def __call__(self, *args, **kwargs):
       return None


class DummyBeam(object):

    def __init__(self):
      self.module_name = "apache_beam"
      
    def __getattr__(self, _):
      err_msg = _MSG.format(name=self.module_name)
      raise ImportError(err_msg)
