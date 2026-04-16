# keras-17 :: tacm-full

query: fix sparse categorical acc (#11100)

## selected nodes

- rank=1 layer=FUNCTION tokens=330 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_metric file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=2 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py::get_compiled_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py
- rank=3 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py::BaseOptimizer._backend_increment_gradient_accumulators file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py
- rank=4 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_loss file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=5 layer=FUNCTION tokens=878 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py::encode_categorical_inputs file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py
- rank=6 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=7 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py::BaseOptimizer._backend_reset_gradient_accumulators file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py
- rank=8 layer=FUNCTION tokens=562 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=9 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/optimizers/torch_parallel_optimizer.py::TorchParallelOptimizer._backend_increment_gradient_accumulators file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/optimizers/torch_parallel_optimizer.py
- rank=10 layer=FUNCTION tokens=260 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py::one_hot file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py
- rank=11 layer=FUNCTION tokens=536 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py::tf_encode_categorical_inputs file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py
- rank=12 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::is_binary_or_sparse_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=13 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::SparseCategoricalCrossentropy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py
- rank=14 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseTopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=15 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::SparseCategoricalCrossentropy.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_metric [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py::get_compiled_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py]
def get_compiled_model():
    model = get_uncompiled_model()
    model.compile(
        optimizer="rmsprop",
        loss="sparse_categorical_crossentropy",
        metrics=["sparse_categorical_accuracy"],
    )
    return model

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py::BaseOptimizer._backend_increment_gradient_accumulators [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py]
    def _backend_increment_gradient_accumulators(self, grads, acc_grads):
        new_g_accs = [(g + acc_g) for g, acc_g in zip(grads, acc_grads)]
        for n_g_acc, g_acc in zip(new_g_accs, acc_grads):
            g_acc.assign(n_g_acc)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_loss [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py::encode_categorical_inputs [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/numerical_utils.py]
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
        inputs: the inputs to encode.
        output_mode: one of `"int"`, `"one_hot"`, `"multi_hot"`, or `"count"`.
        depth: number of classes, this will be the last dimension of the output.
        dtype: the dtype of the output, unless `count_weights` is not `None`.
        sparse: whether the output should be sparse for backends supporting it.
        count_weights: weights to apply if `output_mode` is `"count"`.
        backend_module: the backend to use instead of the current one.

    Returns: the encoded inputs.
    """
    backend_module = backend_module or backend

    if output_mode == "int":
        return backend_module.cast(inputs, dtype=dtype)

    rank_of_inputs = len(backend_module.shape(inputs))

    # In all cases, we should uprank scalar input to a single sample.
    if rank_of_inputs == 0:
        inputs = backend_module.numpy.expand_dims(inputs, -1)
        rank_of_inputs = 1

    if (
        backend_module.__name__.endswith("tensorflow")
        and rank_of_inputs <= 2
        and output_mode in ("multi_hot", "count")
    ):
        # TF only fastpath. Uses bincount; faster. Doesn't work for rank 3+.
        try:
            return tf_utils.tf_encode_categorical_inputs(
                inputs,
                output_mode,
                depth,
                dtype=dtype,
                sparse=sparse,
                count_weights=count_weights,
            )
        except ValueError:
            pass

    if output_mode == "multi_hot":
        return backend_module.nn.multi_hot(
            inputs, depth, dtype=dtype, sparse=sparse
        )
    elif output_mode == "one_hot":
        input_shape = backend_module.core.shape(inputs)
        # Shrink the last dimension if the shape is (..., 1).
        if (
            input_shape is not None
            and len(input_shape) > 1
            and input_shape[-1] == 1
        ):
            newshape = tuple(input_shape[:-1])
            inputs = backend_module.numpy.reshape(inputs, newshape)
        return backend_module.nn.one_hot(
            inputs, depth, dtype=dtype, sparse=sparse
        )
    elif output_mode == "count":
        # We don't use `ops.bincount` because its output has a dynamic shape
        # (last dimension is the highest value of `inputs`). We implement a
        # narrower use case where `minlength` and `maxlength` (not supported by
        # `ops.bincount`) are the same and static value: `depth`. We also don't
        # need to support indices that are negative or greater than `depth`.
        reduction_axis = 1 if len(inputs.shape) > 1 else 0

        if count_weights is not None:
            dtype = count_weights.dtype
        one_hot_encoding = backend_module.nn.one_hot(
            inputs, depth, dtype=dtype, sparse=sparse
        )
        if count_weights is not None:
            count_weights = backend_module.numpy.expand_dims(count_weights, -1)
            one_hot_encoding = one_hot_encoding * count_weights

        outputs = backend_module.numpy.sum(
            one_hot_encoding,
            axis=reduction_axis,
        )
        return outputs

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
    def __init__(self, name="sparse_categorical_accuracy", dtype=None):
        super().__init__(fn=sparse_categorical_accuracy, name=name, dtype=dtype)
        # Metric should be maximized during optimization.
        self._direction = "up"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py::BaseOptimizer._backend_reset_gradient_accumulators [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py]
    def _backend_reset_gradient_accumulators(self):
        for g_acc in self._accumulated_gradients:
            if g_acc is not None:
                g_acc.assign(ops.zeros(g_acc.shape, dtype=g_acc.dtype))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::sparse_categorical_crossentropy [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py]
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
        output: The output tensor representing the predicted probabilities
            or logits.
            Its shape should match the shape of the `target` tensor except
            for the last dimension.
        from_logits: (optional) Whether `output` is a tensor of logits
            or probabilities.
            Set it to `True` if `output` represents logits; otherwise,
            set it to `False` if `output` represents probabilities.
            Defaults to `False`.
        axis: (optional) The axis along which the sparse categorical
            cross-entropy is computed.
            Defaults to `-1`, which corresponds to the last dimension
            of the tensors.

    Returns:
        Integer tensor: The computed sparse categorical cross-entropy
        loss between `target` and `output`.

    Example:

    >>> target = keras.ops.convert_to_tensor([0, 1, 2], dtype=int32)
    >>> output = keras.ops.convert_to_tensor(
    ... [[0.9, 0.05, 0.05],
    ...  [0.1, 0.8, 0.1],
    ...  [0.2, 0.3, 0.5]])
    >>> sparse_categorical_crossentropy(target, output)
    array([0.10536056 0.22314355 0.6931472 ], shape=(3,), dtype=float32)
    """
    if any_symbolic_tensors((target, output)):
        return SparseCategoricalCrossentropy(
            from_logits=from_logits, axis=axis
        ).symbolic_call(target, output)
    return backend.nn.sparse_categorical_crossentropy(
        target, output, from_logits=from_logits, axis=axis
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/optimizers/torch_parallel_optimizer.py::TorchParallelOptimizer._backend_increment_gradient_accumulators [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/optimizers/torch_parallel_optimizer.py]
    def _backend_increment_gradient_accumulators(self, grads, acc_grads):
        acc_list = [v.value for v in acc_grads]
        torch._foreach_add_(acc_list, grads, alpha=1.0)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py::one_hot [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py::tf_encode_categorical_inputs [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tf_utils.py]
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
    """

    if output_mode == "int":
        return tf.identity(tf.cast(inputs, dtype))

    original_shape = inputs.shape
    # In all cases, we should uprank scalar input to a single sample.
    if inputs.shape.rank == 0:
        inputs = expand_dims(inputs, -1)
    # One hot will uprank only if the final output dimension is not already 1.
    if output_mode == "one_hot":
        if inputs.shape[-1] != 1:
            inputs = expand_dims(inputs, -1)

    if inputs.shape.rank > 2:
        raise ValueError(
            "When output_mode is not `'int'`, maximum supported output rank "
            f"is 2. Received output_mode {output_mode} and input shape "
            f"{original_shape}, "
            f"which would result in output rank {inputs.shape.rank}."
        )

    binary_output = output_mode in ("multi_hot", "one_hot")
    if sparse:
        bincounts = sparse_bincount(
            inputs, depth, binary_output, dtype, count_weights
        )
    else:
        bincounts = dense_bincount(
            inputs, depth, binary_output, dtype, count_weights
        )

    bincounts = tf.cast(bincounts, dtype)
    if output_mode != "tf_idf":
        return bincounts

    if idf_weights is None:
        raise ValueError(
            "When output mode is `'tf_idf'`, idf_weights must be provided. "
            f"Received: output_mode={output_mode} and idf_weights={idf_weights}"
        )

    if sparse:
        value_weights = tf.gather(idf_weights, bincounts.indices[:, -1])
        return tf.SparseTensor(
            bincounts.indices,
            value_weights * bincounts.values,
            bincounts.dense_shape,
        )
    else:
        return tf.multiply(bincounts, idf_weights)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::is_binary_or_sparse_categorical [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::SparseCategoricalCrossentropy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::SparseCategoricalCrossentropy.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py]
    def call(self, target, output):
        return backend.nn.sparse_categorical_crossentropy(
            target, output, from_logits=self.from_logits, axis=self.axis
        )
```
