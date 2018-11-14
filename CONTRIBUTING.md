# How to Contribute

# Pull Requests

Please send in fixes, feature additions, and especially new datasets through
Pull Requests.

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
