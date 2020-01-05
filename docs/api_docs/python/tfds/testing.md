<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.testing" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tfds.testing

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/__init__.py">View
source</a>

Testing utilities.



## Classes

[`class DatasetBuilderTestCase`](../tfds/testing/DatasetBuilderTestCase.md): Inherit this class to test your DatasetBuilder class.

[`class DummyDatasetSharedGenerator`](../tfds/testing/DummyDatasetSharedGenerator.md): Test DatasetBuilder.

[`class DummyMnist`](../tfds/testing/DummyMnist.md): Test DatasetBuilder.

[`class FeatureExpectationItem`](../tfds/testing/FeatureExpectationItem.md): Test item of a FeatureExpectation.

[`class FeatureExpectationsTestCase`](../tfds/testing/FeatureExpectationsTestCase.md): Tests FeatureExpectations with full encode-decode.

[`class RaggedConstant`](../tfds/testing/RaggedConstant.md): Container of
tf.ragged.constant values.

[`class SubTestCase`](../tfds/testing/SubTestCase.md): Adds subTest() context
manager to the TestCase if supported.

[`class TestCase`](../tfds/testing/TestCase.md): Base TestCase to be used for all tests.

## Functions

[`fake_examples_dir(...)`](../tfds/testing/fake_examples_dir.md)

[`make_tmp_dir(...)`](../tfds/testing/make_tmp_dir.md): Make a temporary
directory.

[`mock_data(...)`](../tfds/testing/mock_data.md): Mock tfds to generate random
data.

[`mock_kaggle_api(...)`](../tfds/testing/mock_kaggle_api.md): Mock out the
kaggle CLI.

[`rm_tmp_dir(...)`](../tfds/testing/rm_tmp_dir.md): Rm temporary directory.

[`run_in_graph_and_eager_modes(...)`](../tfds/testing/run_in_graph_and_eager_modes.md): Execute the decorated test in both graph mode and eager mode.

[`test_main(...)`](../tfds/testing/test_main.md): Entrypoint for tests.

[`tmp_dir(...)`](../tfds/testing/tmp_dir.md): Context manager for a temporary directory.
