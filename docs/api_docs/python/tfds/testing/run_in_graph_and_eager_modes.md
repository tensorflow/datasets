<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.testing.run_in_graph_and_eager_modes" />
<meta itemprop="path" content="Stable" />
</div>

# tfds.testing.run_in_graph_and_eager_modes

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/testing/test_utils.py">View
source</a>

Execute the decorated test in both graph mode and eager mode.

``` python
tfds.testing.run_in_graph_and_eager_modes(
    func=None,
    config=None,
    use_gpu=True
)
```

<!-- Placeholder for "Used in" -->

This function returns a decorator intended to be applied to test methods in
a `test_case.TestCase` class. Doing so will cause the contents of the test
method to be executed twice - once in graph mode, and once with eager
execution enabled. This allows unittests to confirm the equivalence between
eager and graph execution.

NOTE: This decorator can only be used when executing eagerly in the
outer scope.

For example, consider the following unittest:

```python
tf.compat.v1.enable_eager_execution()

class SomeTest(testing.TestCase):

  @testing.run_in_graph_and_eager_modes
  def test_foo(self):
    x = tf.constant([1, 2])
    y = tf.constant([3, 4])
    z = tf.add(x, y)
    self.assertAllEqual([4, 6], self.evaluate(z))

if __name__ == "__main__":
  testing.test_main()
```

This test validates that `tf.add()` has the same behavior when computed with
eager execution enabled as it does when constructing a TensorFlow graph and
executing the `z` tensor with a session.

#### Args:

*   <b>`func`</b>: function to be annotated. If `func` is None, this method
    returns a decorator the can be applied to a function. If `func` is not None
    this returns the decorator applied to `func`.
*   <b>`config`</b>: An optional config_pb2.ConfigProto to use to configure the
    session when executing graphs.
*   <b>`use_gpu`</b>: If True, attempt to run as many operations as possible on
    GPU.

#### Returns:

Returns a decorator that will run the decorated test method twice: once by
constructing and executing a graph in a session and once with eager execution
enabled.
