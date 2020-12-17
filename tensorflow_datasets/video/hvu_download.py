import os
import sys
import numpy as np
import pandas as pd
from tqdm import tqdm
from tqdm.notebook import tqdm as tqdm_notebook
import pandas as pd
import numpy as np
import logging

#Checking and installing required packages
try:
    import moviepy
except:
    os.system('pip install moviepy')
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip as trim

try:
    import youtube_dl
except:
    os.system('pip install youtube-dl')
    import youtube_dl

try:
    import joblib
except:
    os.system('pip install joblib')
from joblib import delayed
from joblib import Parallel

import argparse
import glob
import json
import os
import shutil
import subprocess
import uuid
from collections import OrderedDict

def isnotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False

def construct_video_filename(row,output_dir, trim_format='%06d'):
    """Given a dataset row, this function constructs the
       output filename for a given video.
    """
    basename = '%s_.mp4' % (row['video-id'])
    output_filename = os.path.join(output_dir,basename)
    return output_filename

def trim_video(row, output_dir):
    """Trim all the videos present in the dataset if they were downloaded successfully"""
    output_filename = construct_video_filename(row, output_dir, trim_format = '%06d')
    trimmed_filename = output_filename.split('.mp4')[0][:-1] + '.mp4'
    start_time = row['start-time']
    end_time = row['end-time']
    if os.path.exists(output_filename):
        trim(output_filename,start_time,end_time,trimmed_filename)
        os.remove(output_filename)
    else:
        print("video not found!\n")
    return

def download_clip(video_identifier, output_filename,start_time, end_time,
                  num_attempts=5,
                  url_base='https://www.youtube.com/watch?v='):
    """Download a video from youtube if exists and is not blocked.
    arguments:
    ---------
    video_identifier: str
        Unique YouTube video identifier (11 characters)
    output_filename: str
        File path where the video will be stored.
    start_time: float
        Indicates the begining time in seconds from where the video
        will be trimmed.
    end_time: float
        Indicates the ending time in seconds of the trimmed video.
    """
    # Defensive argument checking.
    assert isinstance(video_identifier, str), 'video_identifier must be string'
    assert isinstance(output_filename, str), 'output_filename must be string'
    assert len(video_identifier) == 11, 'video_identifier must have length 11'
    status = False
    # Construct command line for getting the direct video link.
    command = ['youtube-dl',
               '--force-ipv4',
               '--quiet', '--no-warnings',
               '-f', 'mp4',
               '-o', '"%s"' % output_filename,
               '"%s"' % (url_base + video_identifier)]
    command = ' '.join(command)
    attempts = 0
    while True:
        try:
            output = subprocess.check_output(command, shell=True,
                                             stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as err:
            attempts += 1
            if attempts == num_attempts:
                return status, err.output
        else:
            break
    # Check if the video was successfully saved.
    status = os.path.exists(output_filename)
    #os.remove(tmp_filename)
    return status, 'Downloaded'

def download_clip_wrapper(row, output_dir):
    """Wrapper for parallel processing purposes."""
    output_filename = construct_video_filename(row,output_dir)

    clip_id = os.path.basename(output_filename).split('.mp4')[0][:-1]
    if os.path.exists(output_filename):
        status = {'Filename' : clip_id, 'Annotations' : row['Tags']}
        return status

    downloaded, log = download_clip(row['video-id'], output_filename,
                                    row['start-time'], row['end-time'])
    if downloaded:
        status = {'Filename' : clip_id, 'Annotations' : row['Tags']}
        return status

def parse_CSV(input_csv,sample_dataset = False):
    """Returns a parsed DataFrame.
    arguments:
    ---------
    input_csv: str
        Path to CSV file containing the following columns:
          'YouTube Identifier,Start time,End time,Class label'
    returns:
    -------
    dataset: DataFrame
        Pandas with the following columns:
            'video-id', 'start-time', 'end-time'
    """
    if sample_dataset:
        df = pd.read_csv(input_csv)[:100]
    else:
        df = pd.read_csv(input_csv)
    if 'youtube_id' in df.columns:
        columns = OrderedDict([
            ('youtube_id', 'video-id'),
            ('time_start', 'start-time'),
            ('time_end', 'end-time')])
        df.rename(columns=columns, inplace=True)
    return df


def main(input_csv, output_dir,sample_dataset=False,
         trim_format='%06d', num_jobs=-1, tmp_dir='/tmp/HVU',
         drop_duplicates=False):

    #parse the dataset CSV file
    dataset = parse_CSV(input_csv,sample_dataset)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    # Download all clips.
    if num_jobs == 1:
        cleaned_data = []
        for i, row in dataset.iterrows():
            cleaned_data.append(download_clip_wrapper(row, output_dir))
    else:
        if isnotebook():
            cleaned_data = Parallel(n_jobs=num_jobs,require='sharedmem')(delayed(download_clip_wrapper)(
                row, output_dir) for i, row in tqdm_notebook(dataset.iterrows(), total = dataset.shape[0]))
        else:
            cleaned_data = Parallel(n_jobs=num_jobs,require='sharedmem')(delayed(download_clip_wrapper)(
            row, output_dir) for i, row in tqdm(dataset.iterrows(), total = dataset.shape[0]))
    logging.getLogger(moviepy.__name__).setLevel(logging.WARNING)
    # Trim all clips
    if isnotebook():
        Parallel(n_jobs = num_jobs)(delayed(trim_video)(row, output_dir) for i,row in tqdm_notebook(dataset.iterrows(), total = dataset.shape[0]))
    else:
        Parallel(n_jobs = num_jobs)(delayed(trim_video)(row, output_dir) for i,row in tqdm(dataset.iterrows(), total = dataset.shape[0]))

    cleaned_data = [x for x in cleaned_data if x is not None]
    return cleaned_data
