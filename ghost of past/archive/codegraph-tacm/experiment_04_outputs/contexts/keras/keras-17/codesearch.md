# keras-17 :: codesearch

query: fix sparse categorical acc (#11100)

## selected nodes

- rank=1 layer=FUNCTION tokens=338 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::sparse_categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=2 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py
- rank=3 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::_reflect_index_fixer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py
- rank=4 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::_mirror_index_fixer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py
- rank=5 layer=FUNCTION tokens=376 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/linalg.py::lstsq file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/linalg.py
- rank=6 layer=FUNCTION tokens=189 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::sparse_plus file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py
- rank=7 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/linalg.py::_assert_1d file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/linalg.py
- rank=8 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py::check_data_cardinality file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py
- rank=9 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py::categorical_accuracy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/accuracy_metrics.py
- rank=10 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py::intersection_sparseness file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py
- rank=11 layer=FUNCTION tokens=628 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=12 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::fix_negative_indices file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=13 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/linalg.py::_assert_2d file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/linalg.py
- rank=14 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::ctc_batch_cost file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=15 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::sparse_sigmoid file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py
- rank=16 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/linalg.py::lstsq file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/linalg.py
- rank=17 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py::sparse_categorical_crossentropy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/nn.py
- rank=18 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py::sparse_sigmoid file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::_reflect_index_fixer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py]
def _reflect_index_fixer(index, size_node):
    """size_node: OV i32 scalar node."""
    # floor_divide(_mirror(2*index + 1, 2*size + 1) - 1, 2)
    two_c = ov_opset.constant(2, dtype=Type.i32).output(0)
    one_c = ov_opset.constant(1, dtype=Type.i32).output(0)
    idx2 = ov_opset.add(ov_opset.multiply(two_c, index), one_c).output(0)
    size2_plus1 = ov_opset.add(
        ov_opset.multiply(two_c, size_node), one_c
    ).output(0)
    mirrored = _mirror_index_fixer(idx2, size2_plus1)
    # integer divide by 2 (result is always >= 0, so truncated == floor)
    return ov_opset.divide(ov_opset.subtract(mirrored, one_c), two_c).output(0)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::_mirror_index_fixer [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py]
def _mirror_index_fixer(index, size_node):
    """size_node: OV i32 scalar node."""
    one_c = ov_opset.constant(1, dtype=Type.i32).output(0)
    two_c = ov_opset.constant(2, dtype=Type.i32).output(0)
    zero_c = ov_opset.constant(0, dtype=Type.i32).output(0)
    s = ov_opset.subtract(size_node, one_c).output(0)  # size - 1
    s2 = ov_opset.multiply(two_c, s).output(0)  # 2 * (size - 1)
    # Guard mod-by-zero when size == 1
    safe_s2 = ov_opset.maximum(s2, one_c).output(0)
    diff = ov_opset.subtract(
        ov_opset.mod(ov_opset.add(index, s), safe_s2), s
    ).output(0)
    # Use max(d, 0-d) instead of abs(d): abs on integers is unreliable
    # under OV's INFERENCE_PRECISION_HINT=f32 for certain graph topologies.
    neg_diff = ov_opset.subtract(zero_c, diff).output(0)
    result = ov_opset.maximum(diff, neg_diff).output(0)
    # When size == 1 all indices map to 0.
    size_is_one = ov_opset.equal(size_node, one_c).output(0)
    return ov_opset.select(size_is_one, zero_c, result).output(0)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/linalg.py::lstsq [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/linalg.py]
def lstsq(a, b, rcond=None):
    a = convert_to_tensor(a)
    b = convert_to_tensor(b)
    if a.shape[0] != b.shape[0]:
        raise ValueError("Leading dimensions of input arrays must match")
    b_orig_ndim = b.ndim
    if b_orig_ndim == 1:
        b = b[:, None]
    if a.ndim != 2:
        raise TypeError(
            f"{a.ndim}-dimensional array given. Array must be two-dimensional"
        )
    if b.ndim != 2:
        raise TypeError(
            f"{b.ndim}-dimensional array given. "
            "Array must be one or two-dimensional"
        )
    m, n = a.shape
    dtype = a.dtype
    eps = tf.experimental.numpy.finfo(dtype).eps
    if a.shape == ():
        s = tf.zeros(0, dtype=a.dtype)
        x = tf.zeros((n, *b.shape[1:]), dtype=a.dtype)
    else:
        if rcond is None:
            rcond = eps * max(n, m)
        else:
            rcond = tf.where(rcond < 0, eps, rcond)
        u, s, vt = svd(a, full_matrices=False)
        mask = s >= tf.convert_to_tensor(rcond, dtype=s.dtype) * s[0]
        safe_s = tf.cast(tf.where(mask, s, 1), dtype=a.dtype)
        s_inv = tf.where(mask, 1 / safe_s, 0)[:, tf.newaxis]
        u_t_b = tf.matmul(tf.transpose(tf.math.conj(u)), b)
        x = tf.matmul(tf.transpose(tf.math.conj(vt)), s_inv * u_t_b)

    if b_orig_ndim == 1:
        x = tf.reshape(x, [-1])
    return x

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/linalg.py::_assert_1d [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/linalg.py]
def _assert_1d(*arrays):
    for a in arrays:
        if a.ndim < 1:
            raise ValueError(
                f"Expected input to have rank >= 1. Received scalar input {a}."
            )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py::check_data_cardinality [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py]
def check_data_cardinality(data):
    num_samples = set(
        int(i.shape[0]) for i in tree.flatten(data) if i is not None
    )
    if len(num_samples) > 1:
        msg = (
            "Data cardinality is ambiguous. "
            "Make sure all arrays contain the same number of samples."
        )
        for label, single_data in zip(["x", "y", "sample_weight"], data):
            sizes = ", ".join(
                str(i.shape[0]) for i in tree.flatten(single_data)
            )
            msg += f"'{label}' sizes: {sizes}\n"
        raise ValueError(msg)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py::intersection_sparseness [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py]
def intersection_sparseness(x1, x2):
    x1_sparseness = sparseness(x1)
    x2_sparseness = sparseness(x2)
    if x1_sparseness == "scalar":
        return x2_sparseness
    if x2_sparseness in ("scalar", "dense"):
        return x1_sparseness
    if x1_sparseness == "dense":
        return x2_sparseness
    if x1_sparseness != x2_sparseness:
        raise ValueError(f"Illegal combination of operands: {x1} {x2}")
    return x1_sparseness

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::fix_negative_indices [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
    def fix_negative_indices(i):
        # Correct the indices using "fill" mode which is the same as in jax
        return tf.where(i < 0, i + tf.cast(tf.shape(x)[axis], i.dtype), i)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/linalg.py::_assert_2d [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/linalg.py]
def _assert_2d(*arrays):
    for a in arrays:
        if a.ndim < 2:
            raise ValueError(
                "Expected input to have rank >= 2. "
                f"Received input with shape {a.shape}."
            )

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::sparse_sigmoid [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py]
def sparse_sigmoid(x):
    x = get_ov_output(x)
    et = x.get_element_type()
    one = get_ov_output(1.0, et)
    neg_one = get_ov_output(-1.0, et)
    half = get_ov_output(0.5, et)
    y = ov_opset.minimum(ov_opset.maximum(x, neg_one), one)
    out = ov_opset.multiply(half, ov_opset.add(y, one))
    return OpenVINOKerasTensor(out.output(0))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/linalg.py::lstsq [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/linalg.py]
def lstsq(a, b, rcond=None):
    a = convert_to_tensor(a)
    b = convert_to_tensor(b)
    return jnp.linalg.lstsq(a, b, rcond=rcond)[0]

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py::sparse_sigmoid [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/nn.py]
def sparse_sigmoid(x):
    x = convert_to_tensor(x)
    return tf.where(
        x <= -1,
        tf.constant(0.0, dtype=x.dtype),
        tf.where(x >= 1, tf.constant(1.0, dtype=x.dtype), 0.5 * (x + 1)),
    )
```
