# keras-17 :: hybrid

query: fix sparse categorical acc (#11100)

## selected nodes

- rank=1 layer=FUNCTION tokens=330 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_metric file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=2 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=3 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseTopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=4 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::SparseCategoricalCrossentropy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py
- rank=5 layer=FUNCTION tokens=562 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=6 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::is_binary_or_sparse_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=7 layer=FUNCTION tokens=260 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py::one_hot file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/nn.py
- rank=8 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py::SparseCategoricalCrossentropy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py
- rank=9 layer=FUNCTION tokens=539 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py
- rank=10 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_loss file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=11 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::SparseCategoricalCrossentropy.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=12 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py::BaseOptimizer._backend_reset_gradient_accumulators file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py
- rank=13 layer=FUNCTION tokens=624 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py
- rank=14 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py::FeatureSpace.integer_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py
- rank=15 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::CategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=16 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/hinge_metrics.py::CategoricalHinge.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/hinge_metrics.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
    def __init__(self, name="sparse_categorical_accuracy", dtype=None):
        super().__init__(fn=sparse_categorical_accuracy, name=name, dtype=dtype)
        # Metric should be maximized during optimization.
        self._direction = "up"

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py::SparseCategoricalCrossentropy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::sparse_categorical_crossentropy [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py]
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
            problems featuring a "void" class (commonly -1 or 255) in
            segmentation maps. By default (`ignore_class=None`), all classes are
            considered.
        axis: Defaults to `-1`. The dimension along which the entropy is
            computed.

    Returns:
        Sparse categorical crossentropy loss value.

    Examples:

    >>> y_true = [1, 2]
    >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
    >>> loss = keras.losses.sparse_categorical_crossentropy(y_true, y_pred)
    >>> assert loss.shape == (2,)
    >>> loss
    array([0.0513, 2.303], dtype=float32)
    """

    if len(y_true.shape) == len(y_pred.shape) and y_true.shape[-1] == 1:
        y_true = ops.squeeze(y_true, axis=-1)

    if ignore_class is not None:
        res_shape = ops.shape(y_pred)[:-1]
        valid_mask = ops.not_equal(y_true, ops.cast(ignore_class, y_pred.dtype))
        y_true = ops.multiply(y_true, ops.cast(valid_mask, y_true.dtype))
        y_pred = ops.multiply(
            y_pred,
            ops.cast(ops.expand_dims(valid_mask, -1), y_pred.dtype),
        )

    res = ops.sparse_categorical_crossentropy(
        y_true,
        y_pred,
        from_logits=from_logits,
        axis=axis,
    )

    if ignore_class is not None:
        valid_mask = ops.reshape(valid_mask, res_shape)
        res = ops.where(valid_mask, res, 0.0)
        backend.set_keras_mask(res, mask=valid_mask)

    return res

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::SparseCategoricalCrossentropy.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py]
    def call(self, target, output):
        return backend.nn.sparse_categorical_crossentropy(
            target, output, from_logits=self.from_logits, axis=self.axis
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py::BaseOptimizer._backend_reset_gradient_accumulators [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/base_optimizer.py]
    def _backend_reset_gradient_accumulators(self):
        for g_acc in self._accumulated_gradients:
            if g_acc is not None:
                g_acc.assign(ops.zeros(g_acc.shape, dtype=g_acc.dtype))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py::sparse_categorical_crossentropy [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py]
def sparse_categorical_crossentropy(target, output, from_logits=False, axis=-1):
    """Categorical crossentropy with integer targets.

    Args:
        target: An integer tensor.
        output: A tensor resulting from a softmax
            (unless `from_logits` is True, in which
            case `output` is expected to be the logits).
        from_logits: Boolean, whether `output` is the
            result of a softmax, or is a tensor of logits.
        axis: Int specifying the channels axis. `axis=-1` corresponds to data
            format `channels_last`, and `axis=1` corresponds to data format
            `channels_first`.

    Returns:
        Output tensor.
    """
    if axis != -1 and axis != len(output.shape) - 1:
        raise ValueError(
            f"Only axis=-1 is currently supported. Received: axis={axis}"
        )
    output, from_logits = _get_logits(
        output, from_logits, "Softmax", "sparse_categorical_crossentropy"
    )

    target = tf.convert_to_tensor(target)
    target = tf.cast(target, dtype="int64")
    output = tf.convert_to_tensor(output)
    if len(target.shape) == len(output.shape) and target.shape[-1] == 1:
        target = tf.squeeze(target, axis=-1)

    if len(output.shape) < 1:
        raise ValueError(
            "Argument `output` must be at least rank 1. "
            "Received: "
            f"output.shape={output.shape}"
        )
    if len(target.shape) != len(output.shape[:-1]):
        raise ValueError(
            "Argument `output` must have rank (ndim) `target.ndim - 1`. "
            "Received: "
            f"target.shape={target.shape}, output.shape={output.shape}"
        )
    for e1, e2 in zip(target.shape, output.shape[:-1]):
        if e1 is not None and e2 is not None and e1 != e2:
            raise ValueError(
                "Arguments `target` and `output` must have the same shape "
                "up until the last dimension: "
                f"target.shape={target.shape}, output.shape={output.shape}"
            )

    if not from_logits:
        output = tf.clip_by_value(
            output, backend.epsilon(), 1 - backend.epsilon()
        )
        output = tf.math.log(output)

    result = tf.nn.sparse_softmax_cross_entropy_with_logits(
        labels=target, logits=output
    )
    return result

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py::FeatureSpace.integer_categorical [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py]
    def integer_categorical(
        cls,
        max_tokens=None,
        num_oov_indices=1,
        output_mode="one_hot",
        name=None,
    ):
        name = name or auto_name("integer_categorical")
        preprocessor = layers.IntegerLookup(
            name=f"{name}_preprocessor",
            max_tokens=max_tokens,
            num_oov_indices=num_oov_indices,
        )
        return Feature(
            dtype="int32", preprocessor=preprocessor, output_mode=output_mode
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::CategoricalAccuracy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
    def __init__(self, name="categorical_accuracy", dtype=None):
        super().__init__(fn=categorical_accuracy, name=name, dtype=dtype)
        # Metric should be maximized during optimization.
        self._direction = "up"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/hinge_metrics.py::CategoricalHinge.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/hinge_metrics.py]
    def __init__(self, name="categorical_hinge", dtype=None):
        super().__init__(fn=categorical_hinge, name=name, dtype=dtype)
        # Metric should be minimized during optimization.
        self._direction = "down"
```
