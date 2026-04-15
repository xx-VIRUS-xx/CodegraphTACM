# keras-17 :: hybrid-cs

query: fix sparse categorical acc (#11100)

## selected nodes

- rank=1 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::fix_negative_indices file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=2 layer=FUNCTION tokens=628 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=3 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py
- rank=4 layer=FUNCTION tokens=338 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::sparse_categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=5 layer=FUNCTION tokens=562 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=6 layer=FUNCTION tokens=532 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::take file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=7 layer=FUNCTION tokens=189 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::sparse_plus file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py
- rank=8 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::ctc_batch_cost file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=9 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py
- rank=10 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=11 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py::sparse_plus file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py
- rank=12 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py::get_compiled_model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py
- rank=13 layer=FUNCTION tokens=330 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::get_metric file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=14 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::is_binary_or_sparse_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::fix_negative_indices [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
    def fix_negative_indices(i):
        # Correct the indices using "fill" mode which is the same as in jax
        return tf.where(i < 0, i + tf.cast(tf.shape(x)[axis], i.dtype), i)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py]
    def fix_index(index, size_node):
        if fill_mode in ("constant", "nearest"):
            zero = ov_opset.constant(0, dtype=Type.i32).output(0)
            size_m1 = ov_opset.subtract(
                size_node, ov_opset.constant(1, dtype=Type.i32)
            ).output(0)
            return ov_opset.minimum(
                ov_opset.maximum(index, zero), size_m1
            ).output(0)
        elif fill_mode == "wrap":
            return ov_opset.floor_mod(index, size_node).output(0)
        elif fill_mode == "mirror":
            return _mirror_index_fixer(index, size_node)
        else:  # reflect
            return _reflect_index_fixer(index, size_node)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::take [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
def take(x, indices, axis=None):
    x = convert_to_tensor(x)
    if axis is None:
        x = tf.reshape(x, (-1,))
        axis = 0

    def fix_negative_indices(i):
        # Correct the indices using "fill" mode which is the same as in jax
        return tf.where(i < 0, i + tf.cast(tf.shape(x)[axis], i.dtype), i)

    if isinstance(indices, tf.SparseTensor):
        if x.dtype not in (tf.float16, tf.float32, tf.float64, tf.bfloat16):
            warnings.warn(
                "`take` with the TensorFlow backend does not support "
                f"`x.dtype={x.dtype}` when `indices` is a sparse tensor; "
                "densifying `indices`."
            )
            indices = convert_to_tensor(indices, sparse=False)
        elif axis != 0:
            warnings.warn(
                "`take` with the TensorFlow backend does not support "
                f"`axis={axis}` when `indices` is a sparse tensor; "
                "densifying `indices`."
            )
            indices = convert_to_tensor(indices, sparse=False)
        else:
            indices = sparse.sparse_with_values(
                indices, fix_negative_indices(indices.values)
            )
            # `expand_dims` on `indices` prevents combiner from being applied.
            output = tf.nn.safe_embedding_lookup_sparse(
                embedding_weights=tf.convert_to_tensor(x),
                sparse_ids=tf.sparse.expand_dims(indices, axis=-1),
                default_id=0,
            )
            output.set_shape(indices.shape + output.shape[len(indices.shape) :])
            return output
    elif isinstance(indices, tf.RaggedTensor):
        indices = indices.with_values(fix_negative_indices(indices.values))
        if axis == 0:
            return tf.nn.embedding_lookup(x, indices)
        else:
            return tf.gather(x, indices, axis=axis)

    indices = fix_negative_indices(convert_to_tensor(indices))
    return tf.gather(x, indices, axis=axis)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::sparse_plus [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py]
def sparse_plus(x):
    x = get_ov_output(x)
    et = x.get_element_type()
    one = get_ov_output(1.0, et)
    neg_one = get_ov_output(-1.0, et)
    zero = get_ov_output(0.0, et)
    quarter = get_ov_output(0.25, et)
    x_plus_1 = ov_opset.add(x, one)
    quad = ov_opset.multiply(quarter, ov_opset.multiply(x_plus_1, x_plus_1))
    leq_than_neg_one = ov_opset.less_equal(x, neg_one)
    less_than_one = ov_opset.less(x, one)
    out = ov_opset.select(
        leq_than_neg_one,
        zero,
        ov_opset.select(less_than_one, quad, x),
    )
    return OpenVINOKerasTensor(out.output(0))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::ctc_batch_cost [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py]
def ctc_batch_cost(y_true, y_pred, input_length, label_length):
    """DEPRECATED."""
    label_length = tf.cast(tf.squeeze(label_length, axis=-1), tf.int32)
    input_length = tf.cast(tf.squeeze(input_length, axis=-1), tf.int32)
    sparse_labels = tf.cast(
        ctc_label_dense_to_sparse(y_true, label_length), tf.int32
    )

    y_pred = tf.math.log(
        tf.transpose(y_pred, perm=[1, 0, 2]) + backend.epsilon()
    )

    return tf.expand_dims(
        tf.compat.v1.nn.ctc_loss(
            inputs=y_pred, labels=sparse_labels, sequence_length=input_length
        ),
        1,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py::sparse_categorical_crossentropy [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py]
def sparse_categorical_crossentropy(target, output, from_logits=False, axis=-1):
    target = jnp.array(target, dtype="int32")
    output = jnp.array(output)
    if len(target.shape) == len(output.shape) and target.shape[-1] == 1:
        target = jnp.squeeze(target, axis=-1)

    if len(output.shape) < 1:
        raise ValueError(
            "Argument `output` must be at least rank 1. "
            "Received: "
            f"output.shape={output.shape}"
        )
    if target.shape != output.shape[:-1]:
        raise ValueError(
            "Arguments `target` and `output` must have the same shape "
            "up until the last dimension: "
            f"target.shape={target.shape}, output.shape={output.shape}"
        )
    if from_logits:
        log_prob = jax.nn.log_softmax(output, axis=axis)
    else:
        output = output / jnp.sum(output, axis, keepdims=True)
        output = jnp.clip(output, backend.epsilon(), 1.0 - backend.epsilon())
        log_prob = jnp.log(output)
    target = jnn.one_hot(target, output.shape[axis], axis=axis)
    return -jnp.sum(target * log_prob, axis=axis)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::categorical_accuracy [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py]
def categorical_accuracy(y_true, y_pred):
    y_true = ops.argmax(y_true, axis=-1)

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
    ):
        y_true = ops.squeeze(y_true, -1)
        reshape_matches = True
    y_pred = ops.argmax(y_pred, axis=-1)

    # If the predicted output and actual output types don't match, force cast
    # them to match.
    if y_pred.dtype is not y_true.dtype:
        y_pred = ops.cast(y_pred, dtype=y_true.dtype)
    matches = ops.cast(ops.equal(y_true, y_pred), backend.floatx())
    if reshape_matches:
        matches = ops.reshape(matches, y_true_org_shape)
    return matches

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py::sparse_plus [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py]
def sparse_plus(x):
    x = convert_to_tensor(x)
    return jnn.sparse_plus(x)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py::get_compiled_model [/Users/xxvirusxx/PY/CodegraphTACM/keras/guides/training_with_built_in_methods.py]
def get_compiled_model():
    model = get_uncompiled_model()
    model.compile(
        optimizer="rmsprop",
        loss="sparse_categorical_crossentropy",
        metrics=["sparse_categorical_accuracy"],
    )
    return model

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
```
