# keras-2 :: hybrid

query: Fix in_top_k tests to include CNTK [Test fails] (#12336)

## selected nodes

- rank=1 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=2 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=3 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=4 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=5 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=6 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=7 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py
- rank=8 layer=FUNCTION tokens=257 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=9 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=10 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py::_filter_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py
- rank=11 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=12 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::TopK.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=13 layer=FUNCTION tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=14 layer=FUNCTION tokens=908 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_utils.py::named_product file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_utils.py
- rank=15 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseTopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=16 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::TopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=17 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::InTopK.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=18 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=19 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_end file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=20 layer=FUNCTION tokens=470 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/conftest.py::pytest_collection_modifyitems file=/Users/xxvirusxx/PY/CodegraphTACM/keras/conftest.py
- rank=21 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_batch_end file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py
- rank=22 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_begin file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py]
def in_top_k(predictions, targets, k):
    """DEPRECATED."""
    return tf.compat.v1.math.in_top_k(predictions, targets, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py]
def in_top_k(targets, predictions, k):
    return tf.math.in_top_k(targets, predictions, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py]
def top_k(x, k, sorted=True):
    return tf.math.top_k(x, k, sorted=sorted)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py]
def top_k(x, k, sorted=True):
    x = convert_to_tensor(x)
    return torch.topk(x, k, sorted=sorted)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py]
def in_top_k(targets, predictions, k):
    targets = targets[:, None]
    topk_values = top_k(predictions, k)[0]
    targets_values = np.take_along_axis(predictions, targets, axis=-1)
    mask = targets_values >= topk_values
    return np.any(mask, axis=-1)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py]
def top_k(x, k, sorted=True):
    if sorted:
        # Take the k largest values.
        sorted_indices = np.argsort(x, axis=-1)[..., ::-1]
        sorted_values = np.take_along_axis(x, sorted_indices, axis=-1)
        top_k_values = sorted_values[..., :k]
        top_k_indices = sorted_indices[..., :k]
    else:
        # Partition the array such that all values larger than the k-th
        # largest value are to the right of it.
        top_k_indices = np.argpartition(x, -k, axis=-1)[..., -k:]
        top_k_values = np.take_along_axis(x, top_k_indices, axis=-1)
    return top_k_values, top_k_indices

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py]
def top_k(x, k, sorted=True):
    # Jax does not supported `sorted`, but in the case where `sorted=False`,
    # order is not guaranteed, so OK to return sorted output.
    return jax.lax.top_k(x, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
def top_k(x, k, sorted=True):
    """Finds the top-k values and their indices in a tensor.

    Args:
        x: Input tensor.
        k: An integer representing the number of top elements to retrieve.
        sorted: A boolean indicating whether to sort the output in
        descending order. Defaults to `True`.

    Returns:
        A tuple containing two tensors. The first tensor contains the
        top-k values, and the second tensor contains the indices of the
        top-k values in the input tensor.

    Example:

    >>> x = keras.ops.convert_to_tensor([5, 2, 7, 1, 9, 3])
    >>> values, indices = top_k(x, k=3)
    >>> print(values)
    array([9 7 5], shape=(3,), dtype=int32)
    >>> print(indices)
    array([4 2 0], shape=(3,), dtype=int32)

    """
    if any_symbolic_tensors((x,)):
        return TopK(k, sorted).symbolic_call(x)
    return backend.math.top_k(x, k, sorted)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py]
def top_k(x, k, sorted=True):
    x = get_ov_output(x)
    k_tensor = ov_opset.constant(k, dtype=Type.i32)
    axis = -1
    sort_type = "value" if sorted else "none"
    topk_node = ov_opset.topk(x, k_tensor, axis, "max", sort_type)
    values = topk_node.output(0)
    indices = topk_node.output(1)
    return OpenVINOKerasTensor(values), OpenVINOKerasTensor(indices)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py::_filter_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py]
def _filter_top_k(x, k):
    """Filters top-k values in the last dim of x and set the rest to NEG_INF.

    Used for computing top-k prediction values in dense labels (which has the
    same shape as predictions) for recall and precision top-k metrics.

    Args:
      x: tensor with any dimensions.
      k: the number of values to keep.

    Returns:
      tensor with same shape and dtype as x.
    """
    _, top_k_idx = ops.top_k(x, k)
    top_k_mask = ops.sum(
        ops.one_hot(top_k_idx, ops.shape(x)[-1], axis=-1), axis=-2
    )
    return x * top_k_mask + NEG_INF * (1 - top_k_mask)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py]
def in_top_k(targets, predictions, k):
    from keras.src.backend.openvino.numpy import take_along_axis

    # Expand targets: (batch,) → (batch, 1) for use with take_along_axis
    targets = ov_opset.unsqueeze(
        get_ov_output(targets), ov_opset.constant(1, Type.i32)
    ).output(0)
    predictions = get_ov_output(predictions)

    # top_k returns (batch, k) sorted descending; last col is the k-th largest
    topk_values = top_k(predictions, k)[0]
    # Grab only the last column (index k-1): threshold value, shape (batch,)
    k_minus_1_idx = ov_opset.constant([k - 1], dtype=Type.i32).output(0)
    topk_values_axis = ov_opset.constant(1, dtype=Type.i32).output(0)
    topk_min = ov_opset.gather(
        topk_values, k_minus_1_idx, topk_values_axis
    ).output(0)

    # Gather the prediction score at each true class index → shape (batch, 1)
    targets_values = take_along_axis(predictions, targets, axis=-1)
    # target score >= k-th largest score means it belongs in the top-k
    mask = ov_opset.greater_equal(targets_values, topk_min).output(0)
    return OpenVINOKerasTensor(mask)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::TopK.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
    def call(self, x):
        return backend.math.top_k(x, self.k, self.sorted)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
def in_top_k(targets, predictions, k):
    """Checks if the targets are in the top-k predictions.

    Args:
        targets: A tensor of true labels.
        predictions: A tensor of predicted labels.
        k: An integer representing the number of predictions to consider.

    Returns:
        A boolean tensor of the same shape as `targets`, where each element
        indicates whether the corresponding target is in the top-k predictions.

    Example:

    >>> targets = keras.ops.convert_to_tensor([2, 5, 3])
    >>> predictions = keras.ops.convert_to_tensor(
    ... [[0.1, 0.4, 0.6, 0.9, 0.5],
    ...  [0.1, 0.7, 0.9, 0.8, 0.3],
    ...  [0.1, 0.6, 0.9, 0.9, 0.5]])
    >>> in_top_k(targets, predictions, k=3)
    array([ True False  True], shape=(3,), dtype=bool)
    """
    if any_symbolic_tensors((targets, predictions)):
        return InTopK(k).symbolic_call(targets, predictions)
    return backend.math.in_top_k(targets, predictions, k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_utils.py::named_product [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_utils.py]
def named_product(*args, **kwargs):
    """Utility to generate the cartesian product of parameters values and
    generate a test case names for each combination.

    The result of this function is to be used with the
    `@parameterized.named_parameters` decorator. It is a replacement for
    `@parameterized.product` which adds explicit test case names.

    For example, this code:
    ```
    class NamedExample(parameterized.TestCase):
        @parameterized.named_parameters(
            named_product(
                [
                    {'testcase_name': 'negative', 'x': -1},
                    {'testcase_name': 'positive', 'x': 1},
                    {'testcase_name': 'zero', 'x': 0},
                ],
                numeral_type=[float, int],
            )
        )
        def test_conversion(self, x, numeral_type):
            self.assertEqual(numeral_type(x), x)
    ```
    produces six tests (note that absl will reorder them by name):
    - `NamedExample::test_conversion_negative_float`
    - `NamedExample::test_conversion_positive_float`
    - `NamedExample::test_conversion_zero_float`
    - `NamedExample::test_conversion_negative_int`
    - `NamedExample::test_conversion_positive_int`
    - `NamedExample::test_conversion_zero_int`

    This function is also useful in the case where there is no product to
    generate test case names for one argument:
    ```
    @parameterized.named_parameters(named_product(numeral_type=[float, int]))
    ```

    Args:
        *args: Each positional parameter is a sequence of keyword arg dicts.
            Every test case generated will include exactly one dict from each
            positional parameter. These will then be merged to form an overall
            list of arguments for the test case. Each dict must contain a
            `"testcase_name"` key whose value is combined with others to
            generate the test case name.
        **kwargs: A mapping of parameter names and their possible values.
            Possible values should given as either a list or a tuple. A string
            representation of each value is used to generate the test case name.

    Returns:
        A list of maps for the test parameters combinations to pass to
        `@parameterized.named_parameters`.
    """

    def value_to_str(value):
        if hasattr(value, "__name__"):
            return value.__name__.lower()
        return str(value).lower()

    # Convert the keyword arguments in the same dict format as the args
    all_test_dicts = args + tuple(
        tuple({"testcase_name": value_to_str(v), key: v} for v in values)
        for key, values in kwargs.items()
    )

    # The current list of tests, start with one empty test
    tests = [{}]
    for test_dicts in all_test_dicts:
        new_tests = []
        for test_dict in test_dicts:
            for test in tests:
                # Augment the testcase name by appending
                testcase_name = test.get("testcase_name", "")
                testcase_name += "_" if testcase_name else ""
                testcase_name += test_dict["testcase_name"]
                new_test = test.copy()
                # Augment the test by adding all the parameters
                new_test.update(test_dict)
                new_test["testcase_name"] = testcase_name
                new_tests.append(new_test)
        # Overwrite the list of tests with the product obtained so far
        tests = new_tests

    return tests

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseTopKCategoricalAccuracy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
    def __init__(
        self,
        k=5,
        name="sparse_top_k_categorical_accuracy",
        dtype=None,
        from_sorted_ids=False,
    ):
        super().__init__(
            fn=sparse_top_k_categorical_accuracy,
            name=name,
            dtype=dtype,
            k=k,
            from_sorted_ids=from_sorted_ids,
        )
        self.k = k
        self.from_sorted_ids = from_sorted_ids
        # Metric should be maximized during optimization.
        self._direction = "up"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::TopKCategoricalAccuracy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
    def __init__(self, k=5, name="top_k_categorical_accuracy", dtype=None):
        super().__init__(
            fn=top_k_categorical_accuracy,
            name=name,
            dtype=dtype,
            k=k,
        )
        self.k = k
        # Metric should be maximized during optimization.
        self._direction = "up"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::InTopK.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
    def call(self, targets, predictions):
        return backend.math.in_top_k(targets, predictions, self.k)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::in_top_k [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py]
def in_top_k(targets, predictions, k):
    targets = convert_to_tensor(targets).type(torch.int64)
    targets = targets[:, None]
    predictions = convert_to_tensor(predictions)
    topk_values = top_k(predictions, k).values
    targets_values = torch.take_along_dim(predictions, targets, dim=-1)
    mask = targets_values >= topk_values
    return torch.any(mask, axis=-1)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_end [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
            def on_test_end(self, logs=None):
                keys = sorted(list(logs.keys()))
                test_obj.assertEqual(keys, ["loss", "mean_absolute_error"])

# /Users/xxvirusxx/PY/CodegraphTACM/keras/conftest.py::pytest_collection_modifyitems [/Users/xxvirusxx/PY/CodegraphTACM/keras/conftest.py]
def pytest_collection_modifyitems(config, items):
    has_multiple_devices = False

    openvino_skipped_tests = []
    if backend() == "openvino":
        with open(
            "keras/src/backend/openvino/excluded_concrete_tests.txt", "r"
        ) as file:
            openvino_skipped_tests = file.readlines()
            # it is necessary to check if stripped line is not empty
            # and exclude such lines
            openvino_skipped_tests = [
                line.strip() for line in openvino_skipped_tests if line.strip()
            ]

    if backend() == "jax":
        import jax

        has_multiple_devices = jax.device_count() > 1

    requires_trainable_backend = pytest.mark.skipif(
        backend() in ["numpy", "openvino"],
        reason="Trainer not implemented for NumPy and OpenVINO backend.",
    )
    requires_multiple_devices = (
        None
        if has_multiple_devices
        else pytest.mark.skip(reason="Requires multiple devices")
    )

    for item in items:
        if "requires_trainable_backend" in item.keywords:
            item.add_marker(requires_trainable_backend)
        if requires_multiple_devices and "multi_device" in item.keywords:
            item.add_marker(requires_multiple_devices)

        # also, skip concrete tests for openvino, listed in the special file
        # this is more granular mechanism to exclude tests rather
        # than using --ignore option
        for skipped_test in openvino_skipped_tests:
            if skipped_test in item.nodeid:
                item.add_marker(
                    skip_if_backend(
                        "openvino",
                        "Not supported operation by openvino backend",
                    )
                )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_batch_end [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
            def on_test_batch_end(self, batch, logs=None):
                keys = sorted(list(logs.keys()))
                test_obj.assertEqual(keys, ["loss", "mean_absolute_error"])

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py::CustomCallback.on_test_begin [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/trainer_test.py]
            def on_test_begin(self, logs=None):
                keys = sorted(list(logs.keys()))
                test_obj.assertEqual(keys, [])
```
