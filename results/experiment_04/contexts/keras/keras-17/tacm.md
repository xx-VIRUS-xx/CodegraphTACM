# keras-17 :: tacm

query: fix sparse categorical acc (#11100)

## selected nodes

- rank=1 layer=FILE tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=2 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py
- rank=3 layer=FILE tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=4 layer=FILE tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py
- rank=5 layer=CLASS tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::OpenVINOKerasTensor file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py
- rank=6 layer=CLASS tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense.py::Dense file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense.py
- rank=7 layer=CLASS tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils_test.py::TestNumericalUtils file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils_test.py
- rank=8 layer=CLASS tokens=373 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn_test.py::NNOpsCorrectnessTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn_test.py
- rank=9 layer=CLASS tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.WeightedLoss file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=10 layer=CLASS tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py::KerasHistory file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py
- rank=11 layer=FUNCTION tokens=288 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_metric file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=12 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_loss file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=13 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py::encode_categorical_inputs file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py
- rank=14 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py::tf_encode_categorical_inputs file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py
- rank=15 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::is_binary_or_sparse_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=16 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py::get_compiled_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py
- rank=17 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py::BaseOptimizer._backend_increment_gradient_accumulators file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py
- rank=18 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=19 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py::BaseOptimizer._backend_reset_gradient_accumulators file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py
- rank=20 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=21 layer=FUNCTION tokens=222 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py::one_hot file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py
- rank=22 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/optimizers/torch_parallel_optimizer.py::TorchParallelOptimizer._backend_increment_gradient_accumulators file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/optimizers/torch_parallel_optimizer.py
- rank=23 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::sparse_top_k_categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=24 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py::to_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py
- rank=25 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::SparseCategoricalCrossentropy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py
- rank=26 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseTopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=27 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py::SparseCategoricalCrossentropy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py
- rank=28 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py::expand_dims file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py
- rank=29 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/model_checkpoint_test.py::ModelCheckpointTest.get_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/model_checkpoint_test.py
- rank=30 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::SparseCategoricalCrossentropy.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=31 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py
- rank=32 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/optimizer.py::TFOptimizer._backend_increment_gradient_accumulators file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/optimizer.py
- rank=33 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=34 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/optimizer.py::TFOptimizer._distributed_tf_increment_grad_acc file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/optimizer.py
- rank=35 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=36 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py::sparse_bincount file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py
- rank=37 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py::TensorflowSparseSliceable.shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py

## context

```text
file metrics/accuracy_metrics.py
imports: keras
defines: Accuracy, BinaryAccuracy, CategoricalAccuracy, SparseCategoricalAccuracy, TopKCategoricalAccuracy, SparseTopKCategoricalAccuracy, accuracy, binary_accuracy, categorical_accuracy, sparse_categorical_accuracy, top_k_categorical_accuracy, sparse_top_k_categorical_accuracy

file utils/tf_utils.py
imports: keras
defines: ensure_tensor, is_ragged_tensor, sparse_bincount, dense_bincount, expand_dims, tf_encode_categorical_inputs

file trainers/compile_utils.py
imports: collections, keras
defines: MetricsList, CompileMetrics, CompileLoss, WeightedLoss, is_binary_or_sparse_categorical, get_metric, get_metrics_list, get_loss

file utils/numerical_utils.py
imports: numpy, keras
defines: normalize, to_categorical, encode_categorical_inputs, build_pos_neg_masks

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

class Dense(Layer):  [layers/core/dense.py:21]
methods: _awq_build, _awq_call, _float8_build, _float8_call
         _get_kernel_with_merged_lora, _gptq_build
         _gptq_call, _int4_build, _int4_call, _int8_build
         _int8_call, build, call, compute_output_shape
         enable_lora, from_config, get_config, grad, grad
         grad_fn, grad_fn, grad_fn, idx_initializer
         kernel, load_own_variables
         matmul_per_channel_with_inputs_gradient
         matmul_sub_channel_with_inputs_gradient
         matmul_with_inputs_gradient, quantize
         quantized_build, quantized_dequantize_inputs
         quantized_dequantize_outputs, save_own_variables
         variable_serialization_spec, __init__

class TestNumericalUtils(testing.TestCase):  [utils/numerical_utils_test.py:11]
methods: test_build_pos_neg_masks, test_normalize
         test_to_categorical
         test_to_categorical_with_backend_tensor
         test_to_categorical_without_num_classes

class NNOpsCorrectnessTest(testing.TestCase):  [ops/nn_test.py:1326]
methods: attention_scan_body, conv, test_average_pool_same_padding
         test_average_pool_valid_padding
         test_batch_normalization
         test_binary_crossentropy
         test_categorical_crossentropy, test_celu
         test_conv_1d, test_conv_2d, test_conv_2d_group_2
         test_conv_3d, test_conv_transpose_1d
         test_conv_transpose_2d, test_ctc_decode
         test_ctc_loss, test_depthwise_conv_2d
         test_dot_product_attention
         test_dot_product_attention_inside_scan, test_elu
         test_gelu, test_glu, test_hard_shrink
         test_hard_sigmoid, test_hard_silu, test_hard_tanh
         test_layer_normalization, test_leaky_relu
         test_log_sigmoid, test_log_softmax
         test_log_softmax_correctness_with_axis_tuple
         test_max_pool, test_moments, test_moments_sync
         test_moments_sync_with_distribution_strategy
         test_multi_hot, test_normalize, test_on_moments
         test_one_hot, test_polar_corectness, test_psnr
         test_relu, test_relu6, test_rms_normalization
         test_selu, test_separable_conv_2d, test_sigmoid
         test_silu, test_soft_shrink, test_softmax
         test_softmax_correctness_with_axis_tuple
         test_softplus, test_softsign
         test_sparse_categorical_crossentropy
         test_sparse_plus, test_sparse_sigmoid
         test_sparsemax, test_squareplus, test_tanh_shrink
         test_threshold

class WeightedLoss:  [trainers/compile_utils.py:562]
methods: —

class KerasHistory(  [ops/node.py:111]
methods: —

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

def tf_encode_categorical_inputs(
    inputs,
    output_mode,
    depth,
    dtype="float32",
    sparse=False,
    count_weights=None,
    idf_weights=None,
):
    """Encodes categorical inputs according to output_mode.

    Faster method that relies on bincount.
    # ... truncated

def is_binary_or_sparse_categorical(y_true, y_pred):
    y_t_rank = len(y_true.shape)
    y_p_rank = len(y_pred.shape)
    y_t_last_dim = y_true.shape[-1]
    y_p_last_dim = y_pred.shape[-1]

    is_binary = y_p_last_dim == 1
    is_sparse_categorical = (
        y_t_rank < y_p_rank or y_t_last_dim == 1 and y_p_last_dim > 1
    )
    return is_binary, is_sparse_categorical

def get_compiled_model():
    model = get_uncompiled_model()
    model.compile(
        optimizer="rmsprop",
        loss="sparse_categorical_crossentropy",
        metrics=["sparse_categorical_accuracy"],
    )
    return model

    def _backend_increment_gradient_accumulators(self, grads, acc_grads):
        new_g_accs = [(g + acc_g) for g, acc_g in zip(grads, acc_grads)]
        for n_g_acc, g_acc in zip(new_g_accs, acc_grads):
            g_acc.assign(n_g_acc)

    def __init__(self, name="sparse_categorical_accuracy", dtype=None):
        super().__init__(fn=sparse_categorical_accuracy, name=name, dtype=dtype)
        # Metric should be maximized during optimization.
        self._direction = "up"

    def _backend_reset_gradient_accumulators(self):
        for g_acc in self._accumulated_gradients:
            if g_acc is not None:
                g_acc.assign(ops.zeros(g_acc.shape, dtype=g_acc.dtype))

def sparse_categorical_crossentropy(target, output, from_logits=False, axis=-1):
    """Computes sparse categorical cross-entropy loss.

    The sparse categorical cross-entropy loss is similar to categorical
    cross-entropy, but it is used when the target tensor contains integer
    class labels instead of one-hot encoded vectors. It measures the
    dissimilarity between the target and output probabilities or logits.

    Args:
        target: The target tensor representing the true class labels as
            integers. Its shape should match the shape of the `output`
            tensor except for the last dimension.
    # ... truncated

def one_hot(x, num_classes, axis=-1, dtype=None, sparse=False):
    if sparse:
        raise ValueError("Unsupported value `sparse=True` with numpy backend")
    if dtype is None:
        dtype = "float32"
    x = convert_to_tensor(x)
    input_shape = x.shape

    x = x.reshape(-1)
    if not num_classes:
        num_classes = np.max(x) + 1

    batch_size = x.shape[0]
    categorical = np.zeros((batch_size, num_classes), dtype=dtype)
    valid_indices = x >= 0
    categorical[np.arange(batch_size)[valid_indices], x[valid_indices]] = 1

    # First, reshape the array with the extra dimension at the end
    output_shape = input_shape + (num_classes,)
    categorical = np.reshape(categorical, output_shape)

    # Then, move this new dimension to the right place (according to axis)
    if axis != -1:
        categorical = np.moveaxis(categorical, -1, axis)

    return categorical

    def _backend_increment_gradient_accumulators(self, grads, acc_grads):
        acc_list = [v.value for v in acc_grads]
        torch._foreach_add_(acc_list, grads, alpha=1.0)

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

def to_categorical(x, num_classes=None):
    """Converts a class vector (integers) to binary class matrix.

    E.g. for use with `categorical_crossentropy`.

    Args:
        x: Array-like with class values to be converted into a matrix
            (integers from 0 to `num_classes - 1`).
        num_classes: Total number of classes. If `None`, this would be inferred
            as `max(x) + 1`. Defaults to `None`.

    Returns:
    # ... truncated

    def __init__(
        self,
        from_logits=False,
        ignore_class=None,
        reduction="sum_over_batch_size",
        axis=-1,
        name="sparse_categorical_crossentropy",
        dtype=None,
    ):
        super().__init__(
            sparse_categorical_crossentropy,
            name=name,
            reduction=reduction,
            dtype=dtype,
            from_logits=from_logits,
            ignore_class=ignore_class,
            axis=axis,
        )
        self.from_logits = from_logits
        self.ignore_class = ignore_class

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

    def __init__(
        self,
        name="sparse_categorical_crossentropy",
        dtype=None,
        from_logits=False,
        ignore_class=None,
        axis=-1,
    ):
        super().__init__(
            sparse_categorical_crossentropy,
            name=name,
            dtype=dtype,
            from_logits=from_logits,
            ignore_class=ignore_class,
            axis=axis,
        )
        self.from_logits = from_logits
        self.ignore_class = ignore_class
        self.axis = axis
        # Metric should be minimized during optimization.
        self._direction = "down"

def expand_dims(inputs, axis):
    """Expand dims on sparse, ragged, or dense tensors."""
    if isinstance(inputs, tf.SparseTensor):
        return tf.sparse.expand_dims(inputs, axis)
    return tf.expand_dims(inputs, axis)

        def get_model():
            inputs = layers.Input(shape=(INPUT_DIM,), batch_size=5)
            x = layers.Dense(NUM_HIDDEN, activation="relu")(inputs)
            outputs = layers.Dense(NUM_CLASSES, activation="softmax")(x)
            functional_model = models.Model(inputs, outputs)
            functional_model.compile(
                loss="categorical_crossentropy",
                optimizer="sgd",
                metrics=[metrics.Accuracy("acc")],
            )
            return functional_model

    def call(self, target, output):
        return backend.nn.sparse_categorical_crossentropy(
            target, output, from_logits=self.from_logits, axis=self.axis
        )

def sparse_categorical_crossentropy(
    y_true, y_pred, from_logits=False, ignore_class=None, axis=-1
):
    """Computes the sparse categorical crossentropy loss.

    Args:
        y_true: Ground truth values.
        y_pred: The predicted values.
        from_logits: Whether `y_pred` is expected to be a logits tensor. By
            default, we assume that `y_pred` encodes a probability distribution.
        ignore_class: Optional integer. The ID of a class to be ignored during
            loss computation. This is useful, for example, in segmentation
    # ... truncated

    def _backend_increment_gradient_accumulators(self, grads, acc_grads):
        def update_accumulator(var, grad):
            var.assign(var + grad)

        accumulators = [v.value for v in acc_grads]

        def _distributed_tf_increment_grad_acc(
            distribution, grads, accumulators
        ):
            for grad, var in zip(grads, accumulators):
                distribution.extended.update(
                    var, update_accumulator, args=(grad,), group=False
                )

        tf.__internal__.distribute.interim.maybe_merge_call(
            _distributed_tf_increment_grad_acc,
            self._distribution_strategy,
            grads,
            accumulators,
        )

    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

        def _distributed_tf_increment_grad_acc(
            distribution, grads, accumulators
        ):
            for grad, var in zip(grads, accumulators):
                distribution.extended.update(
                    var, update_accumulator, args=(grad,), group=False
                )

    def output(self):
        return self._outputs_struct

def sparse_bincount(inputs, depth, binary_output, dtype, count_weights=None):
    """Apply binary or count encoding to an input and return a sparse tensor."""
    result = tf.sparse.bincount(
        inputs,
        weights=count_weights,
        minlength=depth,
        maxlength=depth,
        axis=-1,
        binary_output=binary_output,
    )
    result = tf.cast(result, dtype)
    if inputs.shape.rank == 1:
        output_shape = (depth,)
    else:
        batch_size = tf.shape(result)[0]
        output_shape = (batch_size, depth)
    result = tf.SparseTensor(
        indices=result.indices, values=result.values, dense_shape=output_shape
    )
    return result

    def shape(self):
        return self.array.sparse.shape
```
