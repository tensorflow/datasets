# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

-   Loggers are also called on `tfds.as_numpy(...)`, base `Logger` class has a
    new corresponding method.

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [4.7.0] - 2022-10-04

### Added

-   [API] Added
    [TfDataBuilder](https://www.tensorflow.org/datasets/format_specific_dataset_builders#datasets_based_on_tfdatadataset)
    that is handy for storing experimental ad hoc TFDS datasets in notebook-like
    environments such that they can be versioned, described, and easily shared
    with teammates.
-   [API] Added options to create format-specific dataset builders. The new API
    now includes a number of NLP-specific builders, such as:
    -   [CoNNL](https://www.tensorflow.org/datasets/format_specific_dataset_builders#conll)
    -   [CoNNL-U](https://www.tensorflow.org/datasets/format_specific_dataset_builders#conllu)
-   [API] Added `tfds.beam.inc_counter` to reduce `beam.metrics.Metrics.counter`
    boilerplate
-   [API] Added options to group together existing TFDS datasets into
    [dataset collections](https://www.tensorflow.org/datasets/dataset_collections)
    and to perform simple operations over them.
-   [Documentation] update, specifically:
    -   [New guide](https://www.tensorflow.org/datasets/format_specific_dataset_builders)
        on format-specific dataset builders;
    -   [New guide](https://www.tensorflow.org/datasets/add_dataset_collection)
        on adding new dataset collections to TFDS;
    -   Updated [TFDS CLI](https://www.tensorflow.org/datasets/cli)
        documentation.
-   [TFDS CLI] Supports custom config through Json (e.g. `tfds build my_dataset
    --config='{"name": "my_custom_config", "description": "Abc"}'`)
-   New datasets:
    -   [conll2003](https://www.tensorflow.org/datasets/catalog/conll2003)
    -   [universal_dependency 2.10](https://www.tensorflow.org/datasets/catalog/universal_dependency)
    -   [bucc](https://www.tensorflow.org/datasets/catalog/bucc)
    -   [i_naturalist2021](https://www.tensorflow.org/datasets/catalog/i_naturalist2021)
    -   [mtnt](https://www.tensorflow.org/datasets/catalog/mtnt) Machine
        Translation of Noisy Text.
    -   [placesfull](https://www.tensorflow.org/datasets/catalog/placesfull)
    -   [tatoeba](https://www.tensorflow.org/datasets/catalog/tatoeba)
    -   [user_libri_audio](https://www.tensorflow.org/datasets/catalog/user_libri_audio)
    -   [user_libri_text](https://www.tensorflow.org/datasets/catalog/user_libri_text)
    -   [xtreme_pos](https://www.tensorflow.org/datasets/catalog/xtreme_pos)
    -   [yahoo_ltrc](https://www.tensorflow.org/datasets/catalog/yahoo_ltrc)
-   Updated datasets:
    -   [C4](https://www.tensorflow.org/datasets/catalog/c4) was updated to
        version 3.1.
    -   [common_voice](https://www.tensorflow.org/datasets/catalog/common_voice)
        was updated to a more recent snapshot.
    -   [wikipedia](https://www.tensorflow.org/datasets/catalog/wikipedia) was
        updated with the `20220620` snapshot.
-   New dataset collections, such as
    [xtreme](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/dataset_collections/xtreme/xtreme.py)
    and
    [LongT5](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/dataset_collections/longt5/longt5.py)

### Changed

-   The base `Logger` class expects more information to be passed to the
    `as_dataset` method. This should only be relevant to people who have
    implemented and registered custom `Logger` class(es).
-   You can set `DEFAULT_BUILDER_CONFIG_NAME` in a `DatasetBuilder` to change
    the default config if it shouldn't be the first builder config defined in
    `BUILDER_CONFIGS`.

### Deprecated

### Removed

### Fixed

-   Various datasets
-   In Linux, when loading a dataset from a directory that is not your home
    (`~`) directory, a new `~` directory is not created in the current
    directory (fixes [#4117](https://github.com/tensorflow/datasets/issues/4117)).

### Security

## [4.6.0] - 2022-06-01

### Added

-   Support for community datasets on GCS.
-   [API] `tfds.builder_from_directory` and `tfds.builder_from_directories`, see
    https://www.tensorflow.org/datasets/external_tfrecord#directly_from_folder.
-   [API] Dash ("-") support in split names.
-   [API] `file_format` argument to `download_and_prepare` method, allowing user
    to specify an alternative file format to store prepared data (e.g.
    "riegeli").
-   [API] `file_format` to `DatasetInfo` string representation.
-   [API] Expose the return value of Beam pipelines. This allows for users to
    read the Beam metrics.
-   [API] Expose Feature `tf_example_spec` to public.
-   [API] `doc` kwarg on `Feature`s, to describe a feature.
-   [Documentation] Features description is shown on
    [TFDS Catalog](https://www.tensorflow.org/datasets/catalog/overview).
-   [Documentation] More metadata about HuggingFace datasets in TFDS catalog.
-   [Performance] Parallel load of metadata files.
-   [Testing] TFDS tests are now run using GitHub actions - misc improvements
    such as caching and sharding.
-   [Testing] Improvements to MockFs.
-   New datasets.

### Changed

-   [API] `num_shards` is now optional in the shard name.

### Removed

-   TFDS pathlib API, migrated to a self-contained `etils.epath` (see
    https://github.com/google/etils).

### Fixed

-   Various datasets.
-   Dataset builders that are defined adhoc (e.g. in Colab).
-   Better `DatasetNotFoundError` messages.
-   Don't set `deterministic` on a global level but locally in interleave, so it
    only apply to interleave and not all transformations.
-   Google drive downloader.

## [4.5.2] - 2022-01-31

### Added

-   [API] `split=tfds.split_for_jax_process('train')` (alias of
    `tfds.even_splits('train', n=jax.process_count())[jax.process_index()]`).
-   [Documentation] update.

### Fixed

-   Import bug on Windows (#3709).

## [4.5.0] - 2022-01-25

### Added

-   [API] Better split API:
    -   Splits can be selected using shards: `split='train[3shard]'`.
    -   Underscore supported in numbers for better readability:
        `split='train[:500_000]'`.
    -   Select the union of all splits with `split='all'`.
    -   [`tfds.even_splits`](https://www.tensorflow.org/datasets/splits#tfdseven_splits_multi-host_training)
        is more precise and flexible:
    -   Return splits exactly of the same size when passed
        `tfds.even_splits('train', n=3, drop_remainder=True)`.
    -   Works on subsplits `tfds.even_splits('train[:75%]', n=3)` or even
        nested.
    -   Can be composed with other splits: `tfds.even_splits('train', n=3)[0] +
        'test'`.
-   [API] `serialize_example` / `deserialize_example` methods on features to
    encode/decode example to proto: `example_bytes =
    features.serialize_example(example_data)`.
-   [API] `Audio` feature now supports `encoding='zlib'` for better compression.
-   [API] Features specs are exposed in proto for better compatibility with
    other languages.
-   [API] Create beam pipeline using TFDS as input with
    [tfds.beam.ReadFromTFDS](https://www.tensorflow.org/datasets/api_docs/python/tfds/beam/ReadFromTFDS).
-   [API] Support setting the file formats in `tfds build
    --file_format=tfrecord`.
-   [API] Typing annotations exposed in `tfds.typing`.
-   [API] `tfds.ReadConfig` has a new `assert_cardinality=False` argument to
    disable cardinality.
-   [API] `tfds.display_progress_bar(True)` for functional control.
-   [API] DatasetInfo exposes `.release_notes`.
-   Support for huge number of shards (>99999).
-   [Performance] Faster dataset generation (using tfrecords).
-   [Testing] Mock dataset now supports nested datasets
-   [Testing] Customize the number of sub examples
-   [Documentation] Community datasets:
    https://www.tensorflow.org/datasets/community_catalog/overview.
-   [Documentation]
    [Guide on TFDS and determinism](https://www.tensorflow.org/datasets/determinism).
-   [[RLDS](https://github.com/google-research/rlds)] Support for nested
    datasets features.
-   [[RLDS](https://github.com/google-research/rlds)] New datasets: Robomimic,
    D4RL Ant Maze, RLU Real World RL, and RLU Atari with ordered episodes.
-   New datasets.

### Deprecated

-   Python 3.6 support: this is the last version of TFDS supporting Python 3.6.
    Future versions will use Python 3.7.

### Fixed

-   Misc bugs.

## [4.4.0] - 2021-07-28

### Added

-   [API]
    [`PartialDecoding` support](https://www.tensorflow.org/datasets/decode#only_decode_a_sub-set_of_the_features),
    to decode only a subset of the features (for performances).
-   [API] `tfds.features.LabeledImage` for semantic segmentation (like image but
    with additional `info.features['image_label'].name` label metadata).
-   [API] float32 support for `tfds.features.Image` (e.g. for depth map).
-   [API] Loading datasets from files now supports custom
    `tfds.features.FeatureConnector`.
-   [API] All FeatureConnector can now have a `None` dimension anywhere
    (previously restricted to the first position).
-   [API] `tfds.features.Tensor()` can have arbitrary number of dynamic
    dimension (`Tensor(..., shape=(None, None, 3, None)`)).
-   [API] `tfds.features.Tensor` can now be serialised as bytes, instead of
    float/int values (to allow better compression): `Tensor(...,
    encoding='zlib')`.
-   [API] Support for datasets with `None` in `tfds.as_numpy`.
-   Script to add TFDS metadata files to existing TF-record (see
    [doc](https://www.tensorflow.org/datasets/external_tfrecord)).
-   [TESTING] `tfds.testing.mock_data` now supports:
    -   non-scalar tensors with dtype `tf.string`;
    -   `builder_from_files` and path-based community datasets.
-   [Documentation] Catalog now exposes links to
    [KnowYourData visualisations](https://knowyourdata-tfds.withgoogle.com/).
-   [Documentation] Guide on
    [common implementation gotchas](https://www.tensorflow.org/datasets/common_gotchas).
-   Many new reinforcement learning datasets. ### Changed
-   [API] Dataset generated with `disable_shuffling=True` are now read in
    generation order.

### Fixed

-   File format automatically restored (for datasets generated with
    `tfds.builder(..., file_format=)`).
-   Dynamically set number of worker threads during extraction.
-   Update progress bar during download even if downloads are cached.
-   Misc bug fixes.

## [4.3.0] - 2021-05-06

### Added

-   [API] `dataset.info.splits['train'].num_shards` to expose the number of
    shards to the user.
-   [API] `tfds.features.Dataset` to have a field containing sub-datasets (e.g.
    used in RL datasets).
-   [API] dtype and `tf.uint16` support in `tfds.features.Video`.
-   [API] `DatasetInfo.license` field to add redistributing information.
-   [API] `.copy`, `.format` methods to GPath objects.
-   [Performances] `tfds.benchmark(ds)` (compatible with any iterator, not just
    `tf.data`, better colab representation).
-   [Performances] Faster `tfds.as_numpy()` (avoid extra `tf.Tensor` <>
    `np.array` copy).
-   [Testing] Support for custom `BuilderConfig` in `DatasetBuilderTest`.
-   [Testing] `DatasetBuilderTest` now has a `dummy_data` class property which
    can be used in `setUpClass`.
-   [Testing] `add_tfds_id` and cardinality support to `tfds.testing.mock_data`.
-   [Documentation] Better `tfds.as_dataframe` visualisation (Sequence, ragged
    tensor, semantic masks with `use_colormap`).
-   [Experimental] Community datasets support. To allow dynamically import
    datasets defined outside the TFDS repository.
-   [Experimental] Hugging-face compatibility wrapper to use Hugging-face
    datasets directly in TFDS.
-   [Experimental] Riegeli format support.
-   [Experimental] `DatasetInfo.disable_shuffling` to force examples to be read
    in generation order.
-   New datasets.

### Fixed

-   Many bugs.

## [4.2.0] - 2021-01-06

### Added

-   [CLI] `tfds build` to the CLI. See
    [documentation](https://www.tensorflow.org/datasets/cli#tfds_build_download_and_prepare_a_dataset).
-   [API] `tfds.features.Dataset` to represent nested datasets.
-   [API] `tfds.ReadConfig(add_tfds_id=True)` to add a unique id to the example
    `ex['tfds_id']` (e.g. `b'train.tfrecord-00012-of-01024__123'`).
-   [API] `num_parallel_calls` option to `tfds.ReadConfig` to overwrite to
    default `AUTOTUNE` option.
-   [API] `tfds.ImageFolder` support for `tfds.decode.SkipDecoder`.
-   [API] Multichannel audio support to `tfds.features.Audio`.
-   [API] `try_gcs` to `tfds.builder(..., try_gcs=True)`
-   Better `tfds.as_dataframe` visualization (ffmpeg video if installed,
    bounding boxes,...).
-   [TESTING] Allow `max_examples_per_splits=0` in `tfds build
    --max_examples_per_splits=0` to test `_split_generators` only (without
    `_generate_examples`).
-   New datasets.

### Changed

-   [API] DownloadManager now returns
    [Pathlib-like](https://docs.python.org/3/library/pathlib.html#basic-use)
    objects.
-   [API] Simpler `BuilderConfig` definition: class `VERSION` and
    `RELEASE_NOTES` are applied to all `BuilderConfig`. Config description is
    now optional.
-   [API] To guarantee better deterministic, new validations are performed on
    the keys when creating a dataset (to avoid filenames as keys
    (non-deterministic) and restrict key to `str`, `bytes` and `int`). New
    errors likely indicates an issue in the dataset implementation.
-   [API] `tfds.core.benchmark` now returns a `pd.DataFrame` (instead of a
    `dict`).
-   [API] `tfds.units` is not visible anymore from the public API.
-   Datasets updates.

### Deprecated

### Removed

-   Configs for all text datasets. Only plain text version is kept. For example:
    `multi_nli/plain_text` -> `multi_nli`.

### Fixed

-   [API] Datasets returned by `tfds.as_numpy` are compatible with `len(ds)`.
-   Support 0-len sequence with images of dynamic shape (Fix #2616).
-   Progression bar correctly updated when copying files.
-   Better debugging and error message (e.g. human readable size,...).
-   Many bug fixes (GPath consistency with pathlib, s3 compatibility, TQDM
    visual artifacts, GCS crash on windows, re-download when checksums updated,
    ...).

## [4.1.0] - 2020-11-04

### Added

-   It is now easier to create datasets outside TFDS repository (see our updated
    [dataset creation guide](https://www.tensorflow.org/datasets/add_dataset)).
-   When generating a dataset, if download fails for any reason, it is now
    possible to manually download the data. See
    [doc](https://www.tensorflow.org/datasets/overview#manual_download_if_download_fails).
-   `tfds.core.as_path` to create pathlib.Path-like objects compatible with GCS
    (e.g. `tfds.core.as_path('gs://my-bucket/labels.csv').read_text()`).
-   `verify_ssl=` option to `tfds.download.DownloadConfig` to disable SSH
    certificate during download.
-   New datasets. ### Changed
-   All dataset inherit from `tfds.core.GeneratorBasedBuilder`. Converting a
    dataset to beam now only require changing `_generate_examples` (see
    [example and doc](https://www.tensorflow.org/datasets/beam_datasets#instructions)).
-   `_split_generators` should now returns `{'split_name':
    self._generate_examples(), ...}` (but current datasets are backward
    compatible).
-   Better `pathlib.Path`, `os.PathLike` compatibility: `dl_manager.manual_dir`
    now returns a pathlib-Like object. Example: `python text =
    (dl_manager.manual_dir / 'downloaded-text.txt').read_text()` Note: Other
    `dl_manager.download`, `.extract`,... will return pathlib-like objects in
    future versions. `FeatureConnector`,... and most functions should accept
    `PathLike` objects. Let us know if some functions you need are missing.
-   `--record_checksums` now assume the new dataset-as-folder model.

### Deprecated

-   `tfds.core.SplitGenerator`, `tfds.core.BeamBasedBuilder` are deprecated and
    will be removed in a future version.

### Fixed

-   `BuilderConfig` are now compatible with Beam datasets #2348
-   `tfds.features.Images` can accept encoded `bytes` images directly (useful
    when used with `img_name, img_bytes =
    dl_manager.iter_archive('images.zip')`).
-   Doc API now show deprecated methods, abstract methods to overwrite are now
    documented.
-   You can generate `imagenet2012` with only a single split (e.g. only the
    validation data). Other split will be skipped if not present.

## [4.0.1] - 2020-10-09

### Fixed

-   `tfds.load` when generation code isn't present.
-   GCS compatibility.

## [4.0.0] - 2020-10-06

### Added

-   Dataset-as-folder: Dataset can now be self-contained module in a folder with
    checksums, dummy data,... This simplify implementing datasets outside the
    TFDS repository.
-   `tfds.load` can now load dataset without using the generation class. So
    `tfds.load('my_dataset:1.0.0')` can work even if `MyDataset.VERSION ==
    '2.0.0'` (See #2493).
-   TFDS CLI (see https://www.tensorflow.org/datasets/cli for detail).
-   `tfds.testing.mock_data` does not require metadata files anymore!
-   `tfds.as_dataframe(ds, ds_info)` with custom visualisation
    ([example](https://www.tensorflow.org/datasets/overview#tfdsas_dataframe)).
-   `tfds.even_splits` to generate subsplits (e.g. `tfds.even_splits('train',
    n=3) == ['train[0%:33%]', 'train[33%:67%]', ...]`.
-   `DatasetBuilder.RELEASE_NOTES` property.
-   `tfds.features.Image` now supports PNG with 4-channels.
-   `tfds.ImageFolder` now supports custom shape, dtype.
-   Downloaded URLs are available through `MyDataset.url_infos`.
-   `skip_prefetch` option to `tfds.ReadConfig`.
-   `as_supervised=True` support for `tfds.show_examples`, `tfds.as_dataframe`.
-   tfds.features can now be saved/loaded, you may have to overwrite
    [FeatureConnector.from_json_content](https://www.tensorflow.org/datasets/api_docs/python/tfds/features/FeatureConnector?version=nightly#from_json_content)
    and `FeatureConnector.to_json_content` to support this feature.
-   Script to detect dead-urls.
-   New datasets.

### Changed

-   `tfds.as_numpy()` now returns an iterable which can be iterated multiple
    times. To migrate: `next(ds)` -> `next(iter(ds))`.
-   Rename `tfds.features.text.Xyz` -> `tfds.deprecated.text.Xyz`.

### Removed

-   `DatasetBuilder.IN_DEVELOPMENT` property.
-   `tfds.core.disallow_positional_args` (should use Py3 `*,` instead).
-   Testing against TF 1.15. Requires Python 3.6.8+.

### Fixed

-   Better archive extension detection for `dl_manager.download_and_extract`.
-   Fix `tfds.__version__` in TFDS nightly to be PEP440 compliant
-   Fix crash when GCS not available.
-   Improved open-source workflow, contributor guide, documentation.
-   Many other internal cleanups, bugs, dead code removal, py2->py3 cleanup,
    pytype annotations,...
-   Datasets updates.

## [3.2.1] - 2020-08-12

### Fixed

-   Issue with GCS on Windows.

## [3.2.0] - 2020-07-10

### Added

-   [API] `tfds.ImageFolder` and `tfds.TranslateFolder` to easily create custom
    datasets with your custom data.
-   [API] `tfds.ReadConfig(input_context=)` to shard dataset, for better
    multi-worker compatibility (#1426).
-   [API] The default `data_dir` can be controlled by the `TFDS_DATA_DIR`
    environment variable.
-   [API] Better usability when developing datasets outside TFDS: downloads are
    always cached, checksums are optional.
-   Scripts to help deployment/documentation (Generate catalog documentation,
    export all metadata files, ...).
-   [Documentation] Catalog display images
    ([example](https://www.tensorflow.org/datasets/catalog/sun397#sun397standard-part2-120k)).
-   [Documentation] Catalog shows which dataset have been recently added and are
    only available in `tfds-nightly`
    <span class="material-icons">nights_stay</span>.
-   [API] `tfds.show_statistics(ds_info)` to display
    [FACETS OVERVIEW](https://pair-code.github.io/facets/). Note: This require
    the dataset to have been generated with the statistics.

### Deprecated

-   `tfds.features.text` encoding API. Please use
    [tensorflow_text](https://www.tensorflow.org/tutorials/tensorflow_text/intro)
    instead.

### Removed

-   `tfds.load('image_label_folder')` in favor of the more user-friendly
    `tfds.ImageFolder`.

### Fixed

-   Fix deterministic example order on Windows when path was used as key (this
    only impacts a few datasets). Now example order should be the same on all
    platforms.
-   Misc performances improvements for both generation and reading (e.g. use
    `__slot__`, fix parallelisation bug in `tf.data.TFRecordReader`, ...).
-   Misc fixes (typo, types annotations, better error messages, fixing dead
    links, better windows compatibility, ...).

## [3.1.0] - 2020-04-29

### Added

-   [API] `tfds.builder_cls(name)` to access a DatasetBuilder class by name
-   [API] `info.split['train'].filenames` for access to the tf-record files.
-   [API] `tfds.core.add_data_dir` to register an additional data dir.
-   [Testing] Support for custom decoders in `tfds.testing.mock_data`.
-   [Documentation] Shows which datasets are only present in `tfds-nightly`.
-   [Documentation] Display images for supported datasets.

### Changed

-   Rename `tfds.core.NamedSplit`, `tfds.core.SplitBase` -> `tfds.Split`. Now
    `tfds.Split.TRAIN`,... are instance of `tfds.Split`.
-   Rename `interleave_parallel_reads` -> `interleave_cycle_length` for
    `tfds.ReadConfig`.
-   Invert ds, ds_info argument orders for `tfds.show_examples`.

### Deprecated

-   `tfds.features.text` encoding API. Please use `tensorflow_text` instead.

### Removed

-   `num_shards` argument from `tfds.core.SplitGenerator`. This argument was
    ignored as shards are automatically computed.
-   Most `ds.with_options` which where applied by TFDS. Now use `tf.data`
    default.

### Fixed

-   Better error messages.
-   Windows compatibility.

## [3.0.0] - 2020-04-16

### Added

-   `DownloadManager` is now pickable (can be used inside Beam pipelines).
-   `tfds.features.Audio`:
    -   Support float as returned value.
    -   Expose sample_rate through `info.features['audio'].sample_rate`.
    -   Support for encoding audio features from file objects.
-   More datasets.

### Changed

-   New `image_classification` section. Some datasets have been move there from
    `images`.
-   `DownloadConfig` does not append the dataset name anymore (manual data
    should be in `<manual_dir>/` instead of `<manual_dir>/<dataset_name>/`).
-   Tests now check that all `dl_manager.download` urls has registered
    checksums. To opt-out, add `SKIP_CHECKSUMS = True` to your
    `DatasetBuilderTestCase`.
-   `tfds.load` now always returns `tf.compat.v2.Dataset`. If you're using still
    using `tf.compat.v1`:
    -   Use `tf.compat.v1.data.make_one_shot_iterator(ds)` rather than
        `ds.make_one_shot_iterator()`.
    -   Use `isinstance(ds, tf.compat.v2.Dataset)` instead of `isinstance(ds,
        tf.data.Dataset)`.

### Deprecated

-   The `tfds.features.text` encoding API is deprecated. Please use
    [tensorflow_text](https://www.tensorflow.org/tutorials/tensorflow_text/intro)
    instead.
-   `num_shards` argument of `tfds.core.SplitGenerator` is currently ignored and
    will be removed in the next version.

### Removed

-   Legacy mode `tfds.experiment.S3` has been removed
-   `in_memory` argument has been removed from `as_dataset`/`tfds.load` (small
    datasets are now auto-cached).
-   `tfds.Split.ALL`.

### Fixed

-   Various bugs, better error messages, documentation improvements.

## [2.1.0] - 2020-02-25

### Added

-   Datasets expose `info.dataset_size` and `info.download_size`.
-   [Auto-caching small datasets](https://www.tensorflow.org/datasets/performances#auto-caching).
-   Datasets expose their cardinality `num_examples =
    tf.data.experimental.cardinality(ds)` (Requires tf-nightly or TF >= 2.2.0)
-   Get the number of example in a sub-splits with:
    `info.splits['train[70%:]'].num_examples`

### Changes

-   All datasets generated with 2.1.0 cannot be loaded with previous version
    (previous datasets can be read with `2.1.0` however).

### Deprecated

-   `in_memory` argument is deprecated and will be removed in a future version.

## [2.0.0] - 2020-01-24

### Added

-   Several new datasets. Thanks to all the
    [contributors](https://github.com/tensorflow/datasets/graphs/contributors)!
-   Support for nested `tfds.features.Sequence` and `tf.RaggedTensor`
-   Custom `FeatureConnector`s can override the `decode_batch_example` method
    for efficient decoding when wrapped inside a
    `tfds.features.Sequence(my_connector)`.
-   Beam datasets can use a `tfds.core.BeamMetadataDict` to store additional
    metadata computed as part of the Beam pipeline.
-   Beam datasets' `_split_generators` accepts an additional `pipeline` kwargs
    to define a pipeline shared between all splits.

### Changed

-   The default versions of all datasets are now using the S3 slicing API. See
    the [guide](https://www.tensorflow.org/datasets/splits) for details.
-   `shuffle_files` defaults to False so that dataset iteration is deterministic
    by default. You can customize the reading pipeline, including shuffling and
    interleaving, through the new `read_config` parameter in
    [`tfds.load`](https://www.tensorflow.org/datasets/api_docs/python/tfds/load).
-   `urls` kwargs renamed `homepage` in `DatasetInfo`

### Deprecated

-   Python2 support: this is the last version of TFDS that will support
    Python 2. Going forward, we'll only support and test against Python 3.
-   The previous split API is still available, but is deprecated. If you wrote
    `DatasetBuilder`s outside the TFDS repository, please make sure they do not
    use `experiments={tfds.core.Experiment.S3: False}`. This will be removed in
    the next version, as well as the `num_shards` kwargs from `SplitGenerator`.

### Fixed

-   Various other bug fixes and performance improvements. Thank you for all the
    reports and fixes!

## [1.3.0] - 2019-10-21

### Fixed

-   Misc bugs and performance improvements.

## [1.2.0] - 2019-08-19

### Added

#### Features

-   Add `shuffle_files` argument to `tfds.load` function. The semantic is the
    same as in `builder.as_dataset` function, which for now means that by
    default, files will be shuffled for `TRAIN` split, and not for other splits.
    Default behaviour will change to always be False at next major release.
-   Most datasets now support the new S3 API
    ([documentation](https://github.com/tensorflow/datasets/blob/master/docs/splits.md#two-apis-s3-and-legacy)).
-   Support for uint16 PNG images.

#### Datasets

-   AFLW2000-3D
-   Amazon_US_Reviews
-   binarized_mnist
-   BinaryAlphaDigits
-   Caltech Birds 2010
-   Coil100
-   DeepWeeds
-   Food101
-   MIT Scene Parse 150
-   RockYou leaked password
-   Stanford Dogs
-   Stanford Online Products
-   Visual Domain Decathlon

### Fixed

-   Crash while shuffling on Windows
-   Various documentation improvements

## [1.1.0] - 2019-07-23

### Added

#### Features

-   `in_memory` option to cache small dataset in RAM.
-   Better sharding, shuffling and sub-split.
-   It is now possible to add arbitrary metadata to `tfds.core.DatasetInfo`
    which will be stored/restored with the dataset. See `tfds.core.Metadata`.
-   Better proxy support, possibility to add certificate.
-   `decoders` kwargs to override the default feature decoding
    ([guide](https://github.com/tensorflow/datasets/tree/master/docs/decode.md)).

#### Datasets

-   [downsampled_imagenet](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md#downsampled_imagenet).
-   [patch_camelyon](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md#patch_camelyon).
-   [coco](https://github.com/tensorflow/datasets/tree/master/docs/datasets.md#coco)
    2017 (with and without panoptic annotations).
-   uc_merced.
-   trivia_qa.
-   super_glue.
-   so2sat.
-   snli.
-   resisc45.
-   pet_finder.
-   mnist_corrupted.
-   kitti.
-   eurosat.
-   definite_pronoun_resolution.
-   curated_breast_imaging_ddsm.
-   clevr.
-   bigearthnet.

## [1.0.2] - 2019-05-01

### Added

-   [Apache Beam support](https://www.tensorflow.org/datasets/beam_datasets).
-   Direct GCS access for MNIST (with `tfds.load('mnist', try_gcs=True)`).
-   More datasets.
-   Option to turn off tqdm bar (`tfds.disable_progress_bar()`).

### Fixed

-   Subsplit do not depends on the number of shard anymore
    (https://github.com/tensorflow/datasets/issues/292).
-   Various bugs.

## [1.0.1] - 2019-02-15

### Added

-   Dataset
    [`celeb_a_hq`](https://github.com/tensorflow/datasets/blob/master/docs/datasets.md#celeb_a_hq).

### Fixed

-   Bug #52 that was putting the process in Eager mode by default.

## [1.0.0] - 2019-02-14

### Added

-   25 datasets.
-   Ready to be used `tensorflow-datasets`.
