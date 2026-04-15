# keras-17 :: minilm

query: fix sparse categorical acc (#11100)

## selected nodes

- rank=1 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=2 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py::FeatureSpace.integer_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py
- rank=3 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseTopKCategoricalAccuracy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=4 layer=FUNCTION tokens=330 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_metric file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=5 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py::SparseCategoricalCrossentropy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/losses/losses.py
- rank=6 layer=FUNCTION tokens=628 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=7 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py::SparseCategoricalCrossentropy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/probabilistic_metrics.py
- rank=8 layer=FUNCTION tokens=616 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::sparse_top_k_categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=9 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py::FeatureSpace.string_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py
- rank=10 layer=FUNCTION tokens=562 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=11 layer=FUNCTION tokens=624 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py
- rank=12 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::is_binary_or_sparse_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=13 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py::sparse_plus file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::SparseCategoricalAccuracy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
    def __init__(self, name="sparse_categorical_accuracy", dtype=None):
        super().__init__(fn=sparse_categorical_accuracy, name=name, dtype=dtype)
        # Metric should be maximized during optimization.
        self._direction = "up"

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::sparse_categorical_crossentropy [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py]
def sparse_categorical_crossentropy(
    target, output, from_logits=False, axis=-1, ignore_class=None
):
    """DEPRECATED."""
    target = tf.convert_to_tensor(target)
    output = tf.convert_to_tensor(output)

    target = cast(target, "int64")

    if not from_logits:
        epsilon_ = tf.convert_to_tensor(backend.epsilon(), output.dtype)
        output = tf.clip_by_value(output, epsilon_, 1 - epsilon_)
        output = tf.math.log(output)

    # Permute output so that the last axis contains the logits/probabilities.
    if isinstance(output.shape, (tuple, list)):
        output_rank = len(output.shape)
    else:
        output_rank = output.shape.ndims
    if output_rank is not None:
        axis %= output_rank
        if axis != output_rank - 1:
            permutation = list(
                itertools.chain(
                    range(axis), range(axis + 1, output_rank), [axis]
                )
            )
            output = tf.transpose(output, perm=permutation)
    elif axis != -1:
        raise ValueError(
            "Cannot compute sparse categorical crossentropy with `axis={}` "
            "on an output tensor with unknown rank".format(axis)
        )

    # Try to adjust the shape so that rank of labels = rank of logits - 1.
    output_shape = tf.shape(output)
    target_rank = target.shape.ndims

    update_shape = (
        target_rank is not None
        and output_rank is not None
        and target_rank != output_rank - 1
    )
    if update_shape:
        target = flatten(target)
        output = tf.reshape(output, [-1, output_shape[-1]])

    if ignore_class is not None:
        valid_mask = tf.not_equal(target, cast(ignore_class, target.dtype))
        target = target[valid_mask]
        output = output[valid_mask]

    res = tf.nn.sparse_softmax_cross_entropy_with_logits(
        labels=target, logits=output
    )

    if ignore_class is not None:
        res_shape = cast(output_shape[:-1], "int64")
        valid_mask = tf.reshape(valid_mask, res_shape)
        res = tf.scatter_nd(tf.where(valid_mask), res, res_shape)
        res._keras_mask = valid_mask

        return res

    if update_shape and output_rank >= 3:
        # If our output includes timesteps or
        # spatial dimensions we need to reshape
        res = tf.reshape(res, output_shape[:-1])

    return res

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py::FeatureSpace.string_categorical [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/feature_space.py]
    def string_categorical(
        cls,
        max_tokens=None,
        num_oov_indices=1,
        output_mode="one_hot",
        name=None,
    ):
        name = name or auto_name("string_categorical")
        preprocessor = layers.StringLookup(
            name=f"{name}_preprocessor",
            max_tokens=max_tokens,
            num_oov_indices=num_oov_indices,
        )
        return Feature(
            dtype="string", preprocessor=preprocessor, output_mode=output_mode
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py::sparse_plus [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py]
def sparse_plus(x):
    x = convert_to_tensor(x)
    return jnn.sparse_plus(x)
```
