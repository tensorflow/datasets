# How to Contribute

## Datasets

Adding a public dataset to `tensorflow-datasets` is a great way of making it
more accessible to the TensorFlow community.

See our
[Add a dataset doc](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md)
to learn how to add a dataset.

## Docstrings

Methods and classes should have clear and complete docstrings.
Most methods (and all publicly-facing API methods) should have an `Args:`
section that documents the name, type, and description of each argument.
Argument lines should be formatted as
`` arg_name: (`arg_type`) Description of arg. ``

References to `tfds` methods or classes within a docstring should go in
backticks and use the publicly accessible path to that symbol. For example
`` `tfds.core.DatasetBuilder` ``.
Doing so ensures that the API documentation will insert a link to the
documentation for that symbol.

## Tests

To ensure that `tensorflow-datasets` is nice to use and nice to work on
long-term, all modules should have clear tests for public members. All tests
require:

* Subclassing
[`tfds.testing.TestCase`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/test_case.py)
* Calling `tf.compat.v1.enable_eager_execution()` at the top-level just after
  the imports. This is to enable testing against TF 2.0.
* Using the `@tfds.testing.run_in_graph_and_eager_modes()` decorator for all
  functionality that touches TF ops. To evaluate Tensor values in a way that
  is compatible in both Graph and Eager modes, use `self.evaluate(tensors)`
  or `tfds.as_numpy`.
* End the test file with `if __name__ == "__main__": tfds.testing.test_main()`.

*Note that tests for DatasetBuilders are different and are documented in the*
*[guide to add a dataset](https://github.com/tensorflow/datasets/tree/master/docs/add_dataset.md#testing-mydataset).*

# Pull Requests

All contributions are done through Pull Requests here on GitHub.

## Contributor License Agreement

Contributions to this project must be accompanied by a Contributor License
Agreement. You (or your employer) retain the copyright to your contribution,
this simply gives us permission to use and redistribute your contributions as
part of the project. Head over to <https://cla.developers.google.com/> to see
your current agreements on file or to sign a new one.

You generally only need to submit a CLA once, so if you've already submitted one
(even if it was for a different project), you probably don't need to do it
again.

## Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.
