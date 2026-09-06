# keras-14 :: minilm

query: Fix bug in sparse_top_k_categorical_accuracy (#11196)

## selected nodes

- rank=1 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseTopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=2 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=3 layer=FUNCTION tokens=616 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::sparse_top_k_categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=4 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::TopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=5 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py::SparseCategoricalCrossentropy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py
- rank=6 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::SparseCategoricalCrossentropy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py
- rank=7 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::CategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=8 layer=FUNCTION tokens=535 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py
- rank=9 layer=FUNCTION tokens=330 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_metric file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=10 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::sparse_to_dense file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=11 layer=FUNCTION tokens=562 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=12 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::wrap_densifying_unary file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=13 layer=FUNCTION tokens=338 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::sparse_categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=14 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py::FeatureSpace.integer_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py
- rank=15 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py::KerasTensor.sparse file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
    def __init__(self, name="sparse_categorical_accuracy", dtype=None):
        super().__init__(fn=sparse_categorical_accuracy, name=name, dtype=dtype)
        # Metric should be maximized during optimization.
        self._direction = "up"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::sparse_top_k_categorical_accuracy [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
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
            categories in order from highest score to lowest score.
        k: (Optional) Number of top elements to look at for computing accuracy.
            Defaults to `5`.
        from_sorted_ids: (Optional) Whether `y_pred` is sorted category IDs or
            scores for all categories (the default).

    Returns:
        A tensor with the same shape as `y_true` containing ones where `y_true`
        is in the top `k` and zeros elsewhere.
    """
    reshape_matches = False
    y_pred = ops.convert_to_tensor(y_pred)
    y_true_dtype = y_pred.dtype if from_sorted_ids else "int32"
    y_true = ops.convert_to_tensor(y_true, dtype=y_true_dtype)
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

    if from_sorted_ids:
        # By slicing the first k items, we assume they are sorted by score.
        # Reduce with `any` to count multiple matches only once.
        matches = ops.any(
            ops.equal(ops.expand_dims(y_true, axis=1), y_pred[:, :k]), axis=1
        )
    else:
        matches = ops.in_top_k(y_true, y_pred, k=k)

    matches = ops.cast(matches, dtype=backend.floatx())

    # returned matches is expected to have same shape as y_true input
    if reshape_matches:
        matches = ops.reshape(matches, y_true_org_shape)

    return matches

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::CategoricalAccuracy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
    def __init__(self, name="categorical_accuracy", dtype=None):
        super().__init__(fn=categorical_accuracy, name=name, dtype=dtype)
        # Metric should be maximized during optimization.
        self._direction = "up"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::sparse_categorical_crossentropy [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py]
def sparse_categorical_crossentropy(target, output, from_logits=False, axis=-1):
    target = get_ov_output(target)
    # one_hot requires integer indices
    # cast unconditionally, matching JAX/TF/Torch
    target = ov_opset.convert(target, Type.i64).output(0)
    output = get_ov_output(output)

    if len(target.shape) == len(output.shape) and target.shape[-1] == 1:
        target = ov_opset.squeeze(target, -1).output(0)

    if len(output.shape) < 1:
        raise ValueError(
            "Argument `output` must be at least rank 1. "
            "Received: "
            f"output.shape={output.shape}"
        )

    output_shape_without_class_dim = list(output.shape)
    del output_shape_without_class_dim[axis]

    if list(target.shape) != output_shape_without_class_dim:
        raise ValueError(
            "Arguments `target` and `output` must have the same shape "
            "up until the last dimension: "
            f"target.shape={target.shape}, output.shape={output.shape}"
        )

    if from_logits:
        log_prob = ov_opset.log_softmax(output, axis).output(0)
    else:
        sum = ov_opset.reduce_sum(output, axis, keep_dims=True).output(0)
        output = ov_opset.divide(output, sum).output(0)
        output = ov_opset.clamp(
            output, min_value=backend.epsilon(), max_value=1 - backend.epsilon()
        ).output(0)
        log_prob = ov_opset.log(output).output(0)

    output_type = output.get_element_type()
    on_val = ov_opset.constant(1, output_type).output(0)
    off_val = ov_opset.constant(0, output_type).output(0)
    one_hot_target = ov_opset.one_hot(
        target,
        depth=output.shape[axis],
        on_value=on_val,
        off_value=off_val,
        axis=axis,
    ).output(0)
    result = ov_opset.multiply(one_hot_target, log_prob).output(0)
    loss = ov_opset.reduce_sum(result, axis).output(0)
    loss = ov_opset.negative(loss).output(0)
    return OpenVINOKerasTensor(loss)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::sparse_to_dense [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py]
def sparse_to_dense(x, default_value=None):
    x_shape = x.shape
    if x_shape.rank == 0:
        # Workaround for bug on GPU when sparse tensor represents a scalar.
        if x.values.shape[0] == 0:
            return tf.constant(default_value, dtype=x.dtype)
        else:
            return tf.reshape(x.values, ())
    x = tf.sparse.to_dense(x, default_value=default_value)
    x.set_shape(x_shape)
    return x

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::wrap_densifying_unary [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py]
    def wrap_densifying_unary(func):
        @functools.wraps(func)
        def sparse_wrapper(x, *args, **kwargs):
            if isinstance(x, tf.SparseTensor):
                sparse_output = sparse_with_values(
                    x, func(x.values, *args, **kwargs)
                )
                return sparse_to_dense(
                    sparse_output,
                    tf.cast(default_value, sparse_output.values.dtype),
                )
            elif isinstance(x, tf.IndexedSlices):
                sparse_output_values = func(x.values, *args, **kwargs)
                output = tf.fill(
                    x.dense_shape,
                    tf.cast(default_value, sparse_output_values.dtype),
                )
                return tf.tensor_scatter_nd_update(
                    output, tf.expand_dims(x.indices, 1), sparse_output_values
                )
            return func(x, *args, **kwargs)

        return sparse_wrapper

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::sparse_categorical_accuracy [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
def sparse_categorical_accuracy(y_true, y_pred):
    reshape_matches = False
    y_pred = ops.convert_to_tensor(y_pred)
    y_true = ops.convert_to_tensor(y_true, dtype=y_pred.dtype)
    y_true_org_shape = ops.shape(y_true)
    y_pred_rank = len(y_pred.shape)
    y_true_rank = len(y_true.shape)

    # If the shape of y_true is (num_samples, 1), squeeze to (num_samples,)
    if (
        (y_true_rank is not None)
        and (y_pred_rank is not None)
        and (len(y_true.shape) == len(y_pred.shape))
        and ops.shape(y_true)[-1] == 1
    ):
        y_true = ops.squeeze(y_true, -1)
        reshape_matches = True
    y_pred = ops.argmax(y_pred, axis=-1)

    # If the predicted output and actual output types don't match, force cast
    # them to match.
    if y_pred.dtype is not y_true.dtype:
        y_pred = ops.cast(y_pred, y_true.dtype)
    matches = ops.cast(ops.equal(y_true, y_pred), backend.floatx())
    if reshape_matches:
        matches = ops.reshape(matches, y_true_org_shape)
    # if shape is (num_samples, 1) squeeze
    if len(matches.shape) > 1 and matches.shape[-1] == 1:
        matches = ops.squeeze(matches, -1)
    return matches

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py::KerasTensor.sparse [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/keras_tensor.py]
    def sparse(self, value):
        raise AttributeError(
            "The `sparse` attribute of KerasTensor is immutable. One should "
            "create a new instance of KerasTensor for this."
        )
```
