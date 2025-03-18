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

"""kdd_cup_99 dataset."""

import csv
import gzip

import numpy as np
from tensorflow_datasets.core.utils import bool_utils
import tensorflow_datasets.public_api as tfds

_TRAIN_URL = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz'
_TEST_URL = 'http://kdd.ics.uci.edu/databases/kddcup99/corrected.gz'


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for kdd_cup_99 dataset."""

  VERSION = tfds.core.Version('1.0.1')
  RELEASE_NOTES = {
      '1.0.1': (
          'Fixes parsing of boolean fields `land`, `logged_in`, '
          '`root_shell`, `is_hot_login` and `is_guest_login`.'
      ),
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'duration': np.int32,
            'protocol_type': tfds.features.ClassLabel(
                names=['icmp', 'tcp', 'udp']
            ),
            'service': tfds.features.ClassLabel(
                names=[
                    'aol',
                    'auth',
                    'bgp',
                    'courier',
                    'csnet_ns',
                    'ctf',
                    'daytime',
                    'discard',
                    'domain',
                    'domain_u',
                    'echo',
                    'eco_i',
                    'ecr_i',
                    'efs',
                    'exec',
                    'finger',
                    'ftp',
                    'ftp_data',
                    'gopher',
                    'harvest',
                    'hostnames',
                    'http',
                    'http_2784',
                    'http_443',
                    'http_8001',
                    'icmp',
                    'imap4',
                    'IRC',
                    'iso_tsap',
                    'klogin',
                    'kshell',
                    'ldap',
                    'link',
                    'login',
                    'mtp',
                    'name',
                    'netbios_dgm',
                    'netbios_ns',
                    'netbios_ssn',
                    'netstat',
                    'nnsp',
                    'nntp',
                    'ntp_u',
                    'other',
                    'pm_dump',
                    'pop_2',
                    'pop_3',
                    'printer',
                    'private',
                    'red_i',
                    'remote_job',
                    'rje',
                    'shell',
                    'smtp',
                    'sql_net',
                    'ssh',
                    'sunrpc',
                    'supdup',
                    'systat',
                    'telnet',
                    'tftp_u',
                    'time',
                    'tim_i',
                    'urh_i',
                    'urp_i',
                    'uucp',
                    'uucp_path',
                    'vmnet',
                    'whois',
                    'X11',
                    'Z39_50',
                ]
            ),
            'flag': tfds.features.ClassLabel(
                names=[
                    'OTH',
                    'REJ',
                    'RSTO',
                    'RSTOS0',
                    'RSTR',
                    'S0',
                    'S1',
                    'S2',
                    'S3',
                    'SF',
                    'SH',
                ]
            ),
            'src_bytes': np.int32,
            'dst_bytes': np.int32,
            'land': np.bool_,
            'wrong_fragment': np.int32,
            'urgent': np.int32,
            'hot': np.int32,
            'num_failed_logins': np.int32,
            'logged_in': np.bool_,
            'num_compromised': np.int32,
            'root_shell': np.bool_,
            'su_attempted': np.int32,
            'num_root': np.int32,
            'num_file_creations': np.int32,
            'num_shells': np.int32,
            'num_access_files': np.int32,
            'num_outbound_cmds': np.int32,
            'is_hot_login': np.bool_,
            'is_guest_login': np.bool_,
            'count': np.int32,
            'srv_count': np.int32,
            'serror_rate': np.float32,
            'srv_serror_rate': np.float32,
            'rerror_rate': np.float32,
            'srv_rerror_rate': np.float32,
            'same_srv_rate': np.float32,
            'diff_srv_rate': np.float32,
            'srv_diff_host_rate': np.float32,
            'dst_host_count': np.int32,
            'dst_host_srv_count': np.int32,
            'dst_host_same_srv_rate': np.float32,
            'dst_host_diff_srv_rate': np.float32,
            'dst_host_same_src_port_rate': np.float32,
            'dst_host_srv_diff_host_rate': np.float32,
            'dst_host_serror_rate': np.float32,
            'dst_host_srv_serror_rate': np.float32,
            'dst_host_rerror_rate': np.float32,
            'dst_host_srv_rerror_rate': np.float32,
            'label': tfds.features.ClassLabel(
                names=[
                    'apache2',
                    'back',
                    'buffer_overflow',
                    'ftp_write',
                    'guess_passwd',
                    'httptunnel',
                    'imap',
                    'ipsweep',
                    'land',
                    'loadmodule',
                    'mailbomb',
                    'mscan',
                    'multihop',
                    'named',
                    'neptune',
                    'nmap',
                    'normal',
                    'perl',
                    'phf',
                    'pod',
                    'portsweep',
                    'processtable',
                    'ps',
                    'rootkit',
                    'saint',
                    'satan',
                    'sendmail',
                    'smurf',
                    'snmpgetattack',
                    'snmpguess',
                    'spy',
                    'sqlattack',
                    'teardrop',
                    'udpstorm',
                    'warezclient',
                    'warezmaster',
                    'worm',
                    'xlock',
                    'xsnoop',
                    'xterm',
                ]
            ),
        }),
        supervised_keys=None,  # Set to `None` to disable
        homepage='https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    paths = dl_manager.download({
        'train': _TRAIN_URL,
        'test': _TEST_URL,
    })

    return {
        tfds.Split.TRAIN: self._generate_examples(paths['train']),
        tfds.Split.TEST: self._generate_examples(paths['test']),
    }

  def _generate_examples(self, gz_path):
    """Yields examples."""
    with gz_path.open('rb') as f:
      with gzip.open(f, 'rt', newline='') as gz:
        reader = csv.DictReader(gz, self.info.features)
        for index, row in enumerate(reader):
          row['land'] = bool_utils.parse_bool(row['land'])
          row['logged_in'] = bool_utils.parse_bool(row['logged_in'])
          row['root_shell'] = bool_utils.parse_bool(row['root_shell'])
          row['is_hot_login'] = bool_utils.parse_bool(row['is_hot_login'])
          row['is_guest_login'] = bool_utils.parse_bool(row['is_guest_login'])
          row['label'] = str(row['label']).rstrip('.')
          yield index, row
