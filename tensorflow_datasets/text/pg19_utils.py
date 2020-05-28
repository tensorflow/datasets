"""Utilities for accessing TFDS GCS buckets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import concurrent.futures
import posixpath
from typing import Optional
from xml.etree import ElementTree

import requests
import tensorflow.compat.v2 as tf


GCS_URL = 'https://storage.googleapis.com'
BUCKET = posixpath.join(GCS_URL, 'deepmind-gutenberg')

def download_gcs_file(url, prefix_filter=None, marker=None):
    """Download a file from GCS, optionally to a file."""
    if prefix_filter:
        url += '?prefix={}'.format(prefix_filter)
    if marker:
        url += '&marker={}'.format(marker)
    resp = requests.get(url)
    if not resp.ok:
        raise ValueError('GCS bucket inaccessible')
    return resp.content


def get_all_files_name(prefix_filter=None):
    """Get all files from GCS"""
    top_level_xml_str = download_gcs_file(BUCKET, prefix_filter=prefix_filter)
    xml_root = ElementTree.fromstring(top_level_xml_str)
    filenames = [el[0].text for el in xml_root if el.tag.endswith('Contents')]
    next_marker = xml_root[3]

    while next_marker.text != 'false':
        top_level_xml_str = download_gcs_file(BUCKET,
                                            prefix_filter=prefix_filter,
                                            marker=xml_root[3].text
                                            )
        xml_root = ElementTree.fromstring(top_level_xml_str)
        filenames.extend([
                el[0].text
                for el in xml_root
                if el.tag.endswith('Contents')
                ])
        next_marker = xml_root[3]
    return filenames[:-1]


def get_urls(filenames):
    """Build URL from filenames from GCS"""
    return [posixpath.join(BUCKET, filename) for filename in filenames]
