# Contribute to the TFDS repository

Thank you for your interest to our library ! We are thrilled to have such a
motivated community.

## Get started

*   If you're new with TFDS, the easiest way to get started is to implement one
    of our
    [requested dataset](https://github.com/tensorflow/datasets/issues?q=is%3Aissue+is%3Aopen+label%3A%22dataset+request%22+sort%3Areactions-%2B1-desc),
    focusing on the most requested ones.
    [Follow our guide](https://www.tensorflow.org/datasets/add_dataset) for
    instructions.
*   Issues, feature requests, bugs,... have a much bigger impact than adding new
    datasets, as they benefit the entire TFDS community. See the
    [potential contribution list](https://github.com/tensorflow/datasets/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+-label%3A%22dataset+request%22+).
    Starts with the ones labeled with
    [contribution-welcome](https://github.com/tensorflow/datasets/issues?q=is%3Aissue+is%3Aopen+label%3A%22contributions+welcome%22)
    which are small self-contained easy issues to get started with.
*   Don't hesitate to take over bugs which are already assigned, but haven't
    been updated in a while.
*   No need to get the issue assigned to you. Simply comment on the issue when
    you're starting working on it :)
*   Don't hesitate to ask for help if you're interested by an issue but don't
    know how to get started. And please send draft PR if you want early
    feedback.
*   To avoid unnecessary duplication of work, check the list of
    [pending Pull Requests](https://github.com/tensorflow/datasets/pulls), and
    comment on issues you're working on.

## Setup

### Cloning the repo

To get started, clone or download the
[Tensorflow Datasets](https://github.com/tensorflow/datasets) repository and
install the repo locally.

```sh
git clone https://github.com/tensorflow/datasets.git
cd datasets/
```

Install the development dependencies:

```sh
pip install -e .  # Install minimal deps to use tensorflow_datasets
pip install -e ".[dev]"  # Install all deps required for testing and development
```

Note there is also a `pip install -e ".[tests-all]"` to install all
dataset-specific deps.

### Visual Studio Code

When developing with [Visual Studio Code](https://code.visualstudio.com/), our
repo comes with some
[pre-defined settings](https://github.com/tensorflow/datasets/tree/master/.vscode/settings.json)
to help development (correct indentation, pylint,...).

Note: enabling test discovery in VS Code may fails due to some VS Code bugs
[#13301](https://github.com/microsoft/vscode-python/issues/13301) and
[#6594](https://github.com/microsoft/vscode-python/issues/6594). To solve the
issues, you can look at the test discovery logs:

*   If you are encountering some TensorFlow warning message, try
    [this fix](https://github.com/microsoft/vscode-python/issues/6594#issuecomment-555680813).
*   If discovery fail due to missing import which should have been installed,
    please send a PR to update the `dev` pip install.

## PR checklist

### Sign the CLA

Contributions to this project must be accompanied by a Contributor License
Agreement (CLA). You (or your employer) retain the copyright to your
contribution; this simply gives us permission to use and redistribute your
contributions as part of the project. Head over to
<https://cla.developers.google.com/> to see your current agreements on file or
to sign a new one.

You generally only need to submit a CLA once, so if you've already submitted one
(even if it was for a different project), you probably don't need to do it
again.

### Follow best practices

*   Readability is important. Code should follow best programming practices
    (avoid duplication, factorise into small self-contained functions, explicit
    variables names,...)
*   Simpler is better (e.g. implementation split into multiple smaller
    self-contained PRs which is easier to review).
*   Add tests when required, existing tests should be passing.
*   Add [typing annotations](https://docs.python.org/3/library/typing.html)

### Check your style guide

Our style is based on
[Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md),
which is based on
[PEP 8 Python style guide](https://www.python.org/dev/peps/pep-0008). New code
should try to follow
[Black code style](https://github.com/psf/black/blob/master/docs/the_black_code_style.md)
but with:

*   Line length: 80
*   2 spaces indentation instead of 4.
*   Single quote `'`

**Important:** Make sure to run `pylint` on your code to check your code is
properly formatted:

```sh
pip install pylint --upgrade
pylint tensorflow_datasets/core/some_file.py
```

You can try `yapf` to auto-format a file, but the tool is not perfect, so you'll
likely have to manually apply fixes afterward.

```sh
yapf tensorflow_datasets/core/some_file.py
```

Both `pylint` and `yapf` should have been installed with `pip install -e
".[dev]"` but can also be manually installed with `pip install`. If you're using
VS Code, those tools should be integrated in the UI.

### Docstrings and typing annotations

Classes and functions should be documented with docstrings and typing
annotation. Docstrings should follow the
[Google style](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods).
For example:

```python
def function(x: List[T]) -> T:
  """One line doc should end by a dot.

  * Use `backticks` for code and tripple backticks for multi-line.
  * Use full API name (`tfds.core.DatasetBuilder` instead of `DatasetBuilder`)
  * Use `Args:`, `Returns:`, `Yields:`, `Attributes:`, `Raises:`

  Args:
    x: description

  Returns:
    y: description
  """
```

### Add and run unittests

Make sure new features are tested with unit-tests. You can run tests through the
VS Code interface, or command line. For instance:

```sh
pytest -vv tensorflow_datasets/core/
```

`pytest` vs `unittest`: Historically, we have been using `unittest` module to
write tests. New tests should preferably use `pytest` which is more simple,
flexible, modern and used by most famous libraries (numpy, pandas, sklearn,
matplotlib, scipy, six,...). You can read the
[pytest guide](https://docs.pytest.org/en/stable/getting-started.html#getstarted)
if you're not familiar with pytest.

Tests for DatasetBuilders are special and are documented in the
[guide to add a dataset](https://github.com/tensorflow/datasets/blob/master/docs/add_dataset.md#test-your-dataset).

### Send the PR for reviews!

Congrats! See
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.
