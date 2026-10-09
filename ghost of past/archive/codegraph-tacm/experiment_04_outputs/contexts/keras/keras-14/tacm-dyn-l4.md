# keras-14 :: tacm-dyn-l4

query: Fix bug in sparse_top_k_categorical_accuracy (#11196)

## selected nodes

- rank=1 layer=FILE tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=2 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::InTopKTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=3 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::sparse_top_k_categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=4 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseTopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=5 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::TopKTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=6 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::TopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=7 layer=CLASS tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::MathOpsDynamicShapeTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=8 layer=CLASS tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/confusion_metrics_test.py::PrecisionTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/confusion_metrics_test.py
- rank=9 layer=CLASS tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/confusion_metrics_test.py::RecallTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/confusion_metrics_test.py
- rank=10 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py::get_compiled_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py
- rank=11 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=12 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::top_k_categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=13 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=14 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=15 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py::_filter_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py
- rank=16 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=17 layer=CLASS tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::OpenVINOKerasTensor file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py
- rank=18 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=19 layer=FUNCTION tokens=288 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_metric file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=20 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py::update_confusion_matrix_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/metrics_utils.py
- rank=21 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=22 layer=FUNCTION tokens=224 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=23 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::OpenVINOKerasTensor.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py
- rank=24 layer=CLASS tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils_test.py::TestNumericalUtils file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils_test.py
- rank=25 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=26 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=27 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py
- rank=28 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=29 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::constant file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=30 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py::encode_categorical_inputs file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py
- rank=31 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_loss file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=32 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py::create_keras_tensors file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py
- rank=33 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::InTopK.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=34 layer=CLASS tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::MathOpsCorrectnessTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=35 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/numerical_test.py::compile_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/numerical_test.py
- rank=36 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=37 layer=FUNCTION tokens=276 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::in_top_k file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=38 layer=FUNCTION tokens=11 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::tril file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py

## context

```text
file metrics/accuracy_metrics.py
imports: keras
defines: Accuracy, BinaryAccuracy, CategoricalAccuracy, SparseCategoricalAccuracy, TopKCategoricalAccuracy, SparseTopKCategoricalAccuracy, accuracy, binary_accuracy, categorical_accuracy, sparse_categorical_accuracy, top_k_categorical_accuracy, sparse_top_k_categorical_accuracy

class InTopKTest(testing.TestCase):  [ops/math_test.py:1150]
methods: test_in_top_k_call

def sparse_top_k_categorical_accuracy(
    y_true, y_pred, k=5, from_sorted_ids=False
):
    """Computes how often integer targets are in the top `K` predictions.

    Args:
        y_true: A tensor of shape `(batch_size)` representing indices or IDs of
            true categories.
        y_pred: If `from_sorted_ids=False`, a tensor of shape
            `(batch_size, num_categories)` containing the scores for each sample
            for all possible categories. If `from_sorted_ids=True`, a tensor of
            shape `(batch_size, N)` containing indices or IDs of the top `N`
    # ... truncated

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

class TopKTest(testing.TestCase):  [ops/math_test.py:1130]
methods: test_top_k_call_indices, test_top_k_call_values

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

class MathOpsDynamicShapeTest(testing.TestCase):  [ops/math_test.py:145]
methods: test_extract_sequences, test_fft, test_fft2, test_ifft2
         test_in_top_k, test_irfft, test_istft
         test_istft_with_length, test_logdet
         test_logsumexp, test_rfft, test_rsqrt
         test_segment_reduce, test_stft, test_top_k

class PrecisionTest(testing.TestCase):  [metrics/confusion_metrics_test.py:377]
methods: test_config, test_div_by_zero, test_multiple_updates
         test_unweighted, test_unweighted_all_incorrect
         test_unweighted_class_id_multiclass
         test_unweighted_class_id_should_throw_error_1d
         test_unweighted_top_k
         test_unweighted_top_k_and_threshold
         test_unweighted_with_threshold, test_weighted
         test_weighted_top_k, test_weighted_with_threshold

class RecallTest(testing.TestCase):  [metrics/confusion_metrics_test.py:543]
methods: test_config, test_div_by_zero, test_multiple_updates
         test_unweighted, test_unweighted_all_incorrect
         test_unweighted_class_id_multiclass
         test_unweighted_class_id_should_throw_error_1d
         test_unweighted_top_k
         test_unweighted_top_k_and_threshold
         test_unweighted_with_threshold, test_weighted
         test_weighted_top_k, test_weighted_with_threshold

def get_compiled_model():
    model = get_uncompiled_model()
    model.compile(
        optimizer="rmsprop",
        loss="sparse_categorical_crossentropy",
        metrics=["sparse_categorical_accuracy"],
    )
    return model

    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

def top_k_categorical_accuracy(y_true, y_pred, k=5):
    reshape_matches = False
    y_pred = ops.convert_to_tensor(y_pred)
    y_true = ops.convert_to_tensor(y_true, dtype=y_pred.dtype)
    y_true = ops.argmax(y_true, axis=-1)
    y_true_rank = len(y_true.shape)
    y_pred_rank = len(y_pred.shape)
    y_true_org_shape = ops.shape(y_true)

    # Flatten y_pred to (batch_size, num_samples) and y_true to (num_samples,)
    if (y_true_rank is not None) and (y_pred_rank is not None):
        if y_pred_rank > 2:
            y_pred = ops.reshape(y_pred, [-1, y_pred.shape[-1]])
        if y_true_rank > 1:
            reshape_matches = True
            y_true = ops.reshape(y_true, [-1])

    matches = ops.cast(
        ops.in_top_k(ops.cast(y_true, "int32"), y_pred, k=k),
        dtype=backend.floatx(),
    )

    # returned matches is expected to have same shape as y_true input
    if reshape_matches:
        matches = ops.reshape(matches, y_true_org_shape)

    return matches

    def output(self):
        return self._outputs_struct

def in_top_k(targets, predictions, k):
    return tf.math.in_top_k(targets, predictions, k)

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

def in_top_k(predictions, targets, k):
    """DEPRECATED."""
    return tf.compat.v1.math.in_top_k(predictions, targets, k)

class OpenVINOKerasTensor:  [backend/openvino/core.py:157]
methods: count_unsqueeze_before, numpy, reshape, squeeze, __abs__
         __add__, __and__, __array__, __bool__, __div__
         __eq__, __float__, __floordiv__, __ge__
         __getitem__, __gt__, __init__, __int__
         __invert__, __iter__, __le__, __len__, __lt__
         __matmul__, __mod__, __mul__, __ne__, __neg__
         __or__, __pow__, __radd__, __rand__, __rdiv__
         __repr__, __rfloordiv__, __rmatmul__, __rmod__
         __rmul__, __ror__, __round__, __rpow__, __rsub__
         __rtruediv__, __rxor__, __sub__, __truediv__
         __xor__

    def __init__(self, name="sparse_categorical_accuracy", dtype=None):
        super().__init__(fn=sparse_categorical_accuracy, name=name, dtype=dtype)
        # Metric should be maximized during optimization.
        self._direction = "up"

def get_metric(identifier, y_true, y_pred):
    if identifier is None:
        raise ValueError("Expected metric, received `None`")

    # Convenience feature for selecting b/t binary, categorical,
    # and sparse categorical.
    if str(identifier).lower() not in ["accuracy", "acc"]:
        metric_obj = metrics_module.get(identifier)
    else:
        is_binary, is_sparse_categorical = is_binary_or_sparse_categorical(
            y_true, y_pred
        )
        if is_binary:
            metric_obj = metrics_module.BinaryAccuracy(name=str(identifier))
        elif is_sparse_categorical:
            metric_obj = metrics_module.SparseCategoricalAccuracy(
                name=str(identifier)
            )
        else:
            metric_obj = metrics_module.CategoricalAccuracy(
                name=str(identifier)
            )

    if isinstance(identifier, str):
        metric_name = identifier
    else:
        metric_name = get_object_name(metric_obj)

    if not isinstance(metric_obj, metrics_module.Metric):
        metric_obj = metrics_module.MeanMetricWrapper(metric_obj)

    metric_obj.name = metric_name
    return metric_obj

def update_confusion_matrix_variables(
    variables_to_update,
    y_true,
    y_pred,
    thresholds,
    top_k=None,
    class_id=None,
    sample_weight=None,
    multi_label=False,
    label_weights=None,
    thresholds_distributed_evenly=False,
):
    # ... truncated

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

    def __getitem__(self, indices):
        data = self.output
        rank = len(data.get_partial_shape())
        axes, gather_indices_nodes = [], []
        slice_axes, slice_starts, slice_ends, slice_steps = [], [], [], []
        unsqueeze_axes = []

        if not isinstance(indices, tuple):
            indices = (indices,)

        if any(i is Ellipsis for i in indices):
            ellipsis_pos = indices.index(Ellipsis)
    # ... truncated

class TestNumericalUtils(testing.TestCase):  [utils/numerical_utils_test.py:11]
methods: test_build_pos_neg_masks, test_normalize
         test_to_categorical
         test_to_categorical_with_backend_tensor
         test_to_categorical_without_num_classes

def in_top_k(targets, predictions, k):
    targets = targets[:, None]
    topk_values = top_k(predictions, k)[0]
    targets_values = np.take_along_axis(predictions, targets, axis=-1)
    mask = targets_values >= topk_values
    return np.any(mask, axis=-1)

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

def top_k(x, k, sorted=True):
    # Jax does not supported `sorted`, but in the case where `sorted=False`,
    # order is not guaranteed, so OK to return sorted output.
    return jax.lax.top_k(x, k)

def top_k(x, k, sorted=True):
    return tf.math.top_k(x, k, sorted=sorted)

def constant(value, dtype=None, shape=None, name=None):
    """DEPRECATED."""
    if dtype is None:
        dtype = backend.floatx()

    return tf.constant(value, dtype=dtype, shape=shape, name=name)

def encode_categorical_inputs(
    inputs,
    output_mode,
    depth,
    dtype,
    sparse=False,
    count_weights=None,
    backend_module=None,
):
    """Encodes categorical inputs according to output_mode.

    Args:
    # ... truncated

def get_loss(identifier, y_true, y_pred):
    if identifier is None:
        return None  # Ok to have no loss for an output.

    # Convenience feature for selecting b/t binary, categorical,
    # and sparse categorical.
    if str(identifier).lower() not in ["crossentropy", "ce"]:
        loss_obj = losses_module.get(identifier)
    else:
        is_binary, is_sparse_categorical = is_binary_or_sparse_categorical(
            y_true, y_pred
        )
        if is_binary:
            loss_obj = losses_module.binary_crossentropy
        elif is_sparse_categorical:
            loss_obj = losses_module.sparse_categorical_crossentropy
        else:
            loss_obj = losses_module.categorical_crossentropy

    if not isinstance(loss_obj, losses_module.Loss):
        if isinstance(identifier, str):
            loss_name = identifier
        else:
            loss_name = get_object_name(loss_obj)
        loss_obj = losses_module.LossFunctionWrapper(loss_obj, name=loss_name)
    return loss_obj

def create_keras_tensors(input_shape, dtype, sparse, ragged):
    if isinstance(input_shape, dict):
        return {
            utils.removesuffix(k, "_shape"): KerasTensor(
                v, dtype=dtype[k], sparse=sparse, ragged=ragged
            )
            for k, v in input_shape.items()
        }
    return map_shape_dtype_structure(
        lambda shape, dt: KerasTensor(
            shape, dtype=dt, sparse=sparse, ragged=ragged
        ),
        input_shape,
        dtype,
    )

    def call(self, targets, predictions):
        return backend.math.in_top_k(targets, predictions, self.k)

class MathOpsCorrectnessTest(testing.TestCase):  [ops/math_test.py:482]
methods: run_segment_reduce_test, test_erf_operation_basic
         test_erf_operation_dtype
         test_erf_operation_edge_cases
         test_erfinv_operation_basic
         test_erfinv_operation_dtype
         test_erfinv_operation_edge_cases
         test_extract_sequences, test_fft, test_fft2
         test_ifft2, test_in_top_k, test_irfft, test_istft
         test_logdet, test_logsumexp, test_rfft
         test_rsqrt, test_segment_reduce
         test_segment_reduce_explicit_num_segments
         test_stft, test_top_k

class Accuracy(reduction_metrics.MeanMetricWrapper):  [metrics/accuracy_metrics.py:16]
methods: get_config, __init__

# --- Layer 04: Variable context ---
# call-chain context
  called by: make_or_restore_model [training_with_built_in_methods.py]

# call-chain context
  called by: align_operand_types [core.py]
  called by: get_ov_output [core.py]

# call-chain context
  called by: align_operand_types [core.py]
  called by: get_ov_output [core.py]

# call-chain context
  called by: top_k_categorical_accuracy [accuracy_metrics.py]
  called by: sparse_top_k_categorical_accuracy [accuracy_metrics.py]

# call-chain context
  called by: update_confusion_matrix_variables [metrics_utils.py]

# call-chain context
  called by: top_k_categorical_accuracy [accuracy_metrics.py]
  called by: sparse_top_k_categorical_accuracy [accuracy_metrics.py]

# call-chain context
  called by: get_metrics_list [compile_utils.py]

# call-chain context
  called by: update_state [confusion_metrics.py]
  called by: update_state [confusion_metrics.py]

# call-chain context
  called by: in_top_k [math.py]
  called by: argpartition [numpy.py]

# call-chain context
  called by: argpartition [numpy.py]
  called by: _filter_top_k [metrics_utils.py]

# call-chain context
  called by: __getitem__ [core.py]

# call-chain context
  called by: top_k_categorical_accuracy [accuracy_metrics.py]
  called by: sparse_top_k_categorical_accuracy [accuracy_metrics.py]

# call-chain context
  called by: top_k_categorical_accuracy [accuracy_metrics.py]
  called by: sparse_top_k_categorical_accuracy [accuracy_metrics.py]

# call-chain context
  called by: argpartition [numpy.py]
  called by: _filter_top_k [metrics_utils.py]

# call-chain context
  called by: _build_nested [compile_utils.py]

```
