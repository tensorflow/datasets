<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.core.Experiment" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="DUMMY"/>
<meta itemprop="property" content="S3"/>
</div>

# tfds.core.Experiment

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/utils/version.py">View
source</a>

## Class `Experiment`

Experiments which can be enabled/disabled on a per version basis.

<!-- Placeholder for "Used in" -->

Experiments are designed to gradually apply changes to datasets while
maintaining backward compatibility with previous versions. All experiments
should eventually be deleted, once used by all versions of all datasets.

#### Eg:

class Experiment(enum.Enum): EXP_A = enum.auto() # Short description of
experiment.

class MyBuilder(...): VERSION = tfds.core.Version('1.2.3', experiments={
tfds.core.Experiment.EXP_A: True, })

## Class Members

*   `DUMMY` <a id="DUMMY"></a>
*   `S3` <a id="S3"></a>
