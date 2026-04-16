# keras-11 :: hybrid-cs

query: Improve type-check for Sequence (#11468)

## selected nodes

- rank=1 layer=FUNCTION tokens=453 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::pack_sequence_as file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=2 layer=FUNCTION tokens=217 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py::_has_fully_masked_sequence file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py
- rank=3 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_has_fully_masked_sequence file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=4 layer=FUNCTION tokens=639 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::extract_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=5 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=6 layer=FUNCTION tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=7 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::ExtractSequences.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=8 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py
- rank=9 layer=FUNCTION tokens=348 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=10 layer=FUNCTION tokens=638 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::_overlap_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=11 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::ExtractSequencesOpTest.calculate_expected_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=12 layer=FUNCTION tokens=628 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::scan file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py
- rank=13 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::extract_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=14 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/numpy.py::vstack file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/numpy.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::pack_sequence_as [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py]
def pack_sequence_as(structure, flat_sequence):
    # This is not just an optimization for the case when structure is a leaf.
    # This is required to avoid Torch Dynamo failures.
    if not is_nested(structure):
        if len(flat_sequence) == 1:
            return flat_sequence[0]
        else:
            raise ValueError(
                "Incorrect number of leaves provided by `flat_sequence` for "
                f"`structure`; expected: 1, got {len(flat_sequence)}."
            )

    flat_sequence_it = enumerate(flat_sequence)

    def unflatten_func(s):
        registration = REGISTERED_CLASSES.get(type(s), None)
        if registration is not None:
            flat_meta_s = registration.flatten(s)
            flat_s = dmtree.traverse(
                unflatten_func, list(flat_meta_s[0]), top_down=True
            )
            return registration.unflatten(flat_meta_s[1], flat_s)
        elif not dmtree.is_nested(s):
            try:
                _, value = next(flat_sequence_it)
                return dmtree.MAP_TO_NONE if value is None else value
            except StopIteration:
                raise ValueError(
                    "Too few leaves provided by `flat_sequence` for "
                    f"`structure`. Got {len(flat_sequence)}."
                )
        return None

    ret = dmtree.traverse(unflatten_func, structure, top_down=True)
    try:
        index, _ = next(flat_sequence_it)
        raise ValueError(
            "Too many leaves provided by `flat_sequence` for `structure`; "
            f"expected: {index}, got {len(flat_sequence)}."
        )
    except StopIteration:
        return ret

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py::_has_fully_masked_sequence [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py]
def _has_fully_masked_sequence(mask):
    """Check if input sequence contains any fully masked data.

    cuDNN kernel will error out if the input sequence contains any fully masked
    data. We work around this issue by rerouting the computation to the
    standard kernel until the issue on the cuDNN side has been fixed. For a
    fully masked sequence, it will contain all `False` values. To make it easy
    to check, we invert the boolean and check if any of the sequences has all
    `True` values.

    Args:
        mask: The mask tensor.

    Returns:
        A boolean tensor, `True` if the mask contains a fully masked sequence.
    """
    return torch.any(torch.all(~mask, dim=1))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_has_fully_masked_sequence [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py]
def _has_fully_masked_sequence(mask):
    """Check if input sequence contains any fully masked data.

    cuDNN kernel will error out if the input sequence contains any fully masked
    data. We work around this issue by rerouting the computation to the
    standard kernel until the issue on the cuDNN side has been fixed. For a
    fully masked sequence, it will contain all `False` values. To make it easy
    to check, we invert the boolean and check if any of the sequences has all
    `True` values.

    Args:
        mask: The mask tensor.

    Returns:
        A boolean tensor, `True` if the mask contains a fully masked sequence.
    """
    return tf.reduce_any(
        tf.reduce_all(tf.logical_not(tf.cast(mask, dtype="bool")), axis=1)
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::extract_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py]
def extract_sequences(x, sequence_length, sequence_stride):
    x = get_ov_output(x)
    x_shape = x.partial_shape
    ndim = len(x_shape)

    # Define common constants for reuse
    zero_const_1d = ov_opset.constant([0], Type.i32)
    shape_tensor = ov_opset.shape_of(x, output_type=Type.i32).output(0)

    last_idx = ov_opset.constant([ndim - 1], Type.i32)
    axis0 = ov_opset.constant(0, Type.i32)
    signal_len_1d = ov_opset.gather(shape_tensor, last_idx, axis0).output(0)
    signal_len_scalar = ov_opset.squeeze(signal_len_1d, zero_const_1d).output(0)

    minus_one = ov_opset.constant([-1], Type.i32).output(0)
    shape_2d = ov_opset.concat([minus_one, signal_len_1d], axis=0).output(0)
    x_2d = ov_opset.reshape(x, shape_2d, False).output(0)

    seq_len_c = ov_opset.constant(sequence_length, Type.i32).output(0)
    stride_c = ov_opset.constant(sequence_stride, Type.i32).output(0)
    diff = ov_opset.subtract(signal_len_scalar, seq_len_c).output(0)
    num_seq_scalar = ov_opset.add(
        ov_opset.divide(diff, stride_c).output(0),
        ov_opset.constant(1, Type.i32).output(0),
    ).output(0)

    row_stop = ov_opset.multiply(num_seq_scalar, stride_c).output(0)
    row_idx = ov_opset.range(
        ov_opset.constant(0, Type.i32).output(0),
        row_stop,
        stride_c,
        output_type=Type.i32,
    ).output(0)
    row_idx_2d = ov_opset.unsqueeze(
        row_idx, ov_opset.constant([1], Type.i32)
    ).output(0)

    col_idx = ov_opset.constant(
        np.arange(sequence_length, dtype=np.int32)
    ).output(0)
    col_idx_2d = ov_opset.unsqueeze(col_idx, zero_const_1d).output(0)

    indices = ov_opset.add(row_idx_2d, col_idx_2d).output(0)

    gathered = ov_opset.gather(
        x_2d, indices, ov_opset.constant(1, Type.i32)
    ).output(0)

    batch_shape = ov_opset.slice(
        shape_tensor,
        start=zero_const_1d,
        stop=ov_opset.constant([ndim - 1], Type.i32),
        step=ov_opset.constant([1], Type.i32),
        axes=zero_const_1d,
    ).output(0)
    num_seq_1d = ov_opset.unsqueeze(num_seq_scalar, zero_const_1d).output(0)
    seq_len_1d = ov_opset.constant([sequence_length], Type.i32).output(0)
    out_shape = ov_opset.concat(
        [batch_shape, num_seq_1d, seq_len_1d], axis=0
    ).output(0)
    result = ov_opset.reshape(gathered, out_shape, False).output(0)

    return OpenVINOKerasTensor(result)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py]
            def key_check_fn(key, objs):
                return all(
                    [
                        issubclass(type(obj), (list, tuple)) and key < len(obj)
                        for obj in objs
                    ]
                )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
def searchsorted(sorted_sequence, values, side="left"):
    if ndim(sorted_sequence) != 1:
        raise ValueError(
            "`searchsorted` only supports 1-D sorted sequences. "
            "You can use `keras.ops.vectorized_map` "
            "to extend it to N-D sequences. Received: "
            f"sorted_sequence.shape={sorted_sequence.shape}"
        )
    sequence_len = sorted_sequence.shape[0]
    out_type = (
        "int32"
        if sequence_len is not None and sequence_len <= np.iinfo(np.int32).max
        else "int64"
    )
    return tf.searchsorted(
        sorted_sequence, values, side=side, out_type=out_type
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::ExtractSequences.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
    def __init__(self, sequence_length, sequence_stride, *, name=None):
        super().__init__(name=name)
        self.sequence_length = sequence_length
        self.sequence_stride = sequence_stride

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py]
def searchsorted(sorted_sequence, values, side="left"):
    if ndim(sorted_sequence) != 1:
        raise ValueError(
            "`searchsorted` only supports 1-D sorted sequences. "
            "You can use `keras.ops.vectorized_map` "
            "to extend it to N-D sequences. Received: "
            f"sorted_sequence.shape={sorted_sequence.shape}"
        )
    out_type = (
        "int32"
        if sorted_sequence.shape[0] <= np.iinfo(np.int32).max
        else "int64"
    )
    return np.searchsorted(sorted_sequence, values, side=side).astype(out_type)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py]
def searchsorted(sorted_sequence, values, side="left"):
    if side not in ("left", "right"):
        raise ValueError(
            f"`side` must be either 'left' or 'right'. Received: side={side}"
        )
    sorted_sequence = get_ov_output(sorted_sequence)
    values = get_ov_output(values)

    if sorted_sequence.get_partial_shape().rank.get_length() != 1:
        raise ValueError(
            "`searchsorted` only supports 1-D sorted sequences. "
            "You can use `keras.ops.vectorized_map` "
            "to extend it to N-D sequences. Received: "
            f"sorted_sequence.shape={sorted_sequence.get_partial_shape()}"
        )

    sorted_sequence, values = _align_operand_types(
        sorted_sequence, values, "searchsorted()"
    )

    # Note: OpenVINO's bucketize with_right_bound has opposite semantics
    # with_right_bound=True means search from right (side='left' in numpy)
    # with_right_bound=False means search from left (side='right' in numpy)
    with_right_bound = side == "left"
    result = ov_opset.bucketize(
        values,
        sorted_sequence,
        output_type=Type.i32,
        with_right_bound=with_right_bound,
    ).output(0)

    return OpenVINOKerasTensor(result)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::_overlap_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py]
def _overlap_sequences(x, sequence_stride):
    # Ref: https://github.com/google/jax/blob/main/jax/_src/scipy/signal.py
    x = convert_to_tensor(x)
    *batch_shape, num_sequences, sequence_length = x.shape
    if sequence_stride > sequence_length:
        raise ValueError(
            "`sequence_stride` must equal or less than x.shape[-1]. "
            f"Received: sequence_stride={sequence_stride}, "
            f"x.shape[-1]={sequence_length}"
        )
    if sequence_stride < (sequence_length / num_sequences):
        raise ValueError(
            "`sequence_stride` must equal or greater than "
            "x.shape[-1] / x.shape[-2]. "
            f"Received: sequence_stride={sequence_stride}, "
            f"x.shape[-1]={sequence_length}, x.shape[-2]={num_sequences}"
        )
    flat_batchsize = math.prod(batch_shape)
    x = torch.reshape(x, (flat_batchsize, num_sequences, sequence_length))
    output_size = sequence_stride * (num_sequences - 1) + sequence_length
    nstep_per_segment = 1 + (sequence_length - 1) // sequence_stride
    # Here, we use shorter notation for axes.
    # B: batch_size, N: num_sequences, S: nstep_per_segment,
    # T: sequence_length divided by S
    padded_segment_len = nstep_per_segment * sequence_stride
    x = torch.nn.functional.pad(
        x, (0, padded_segment_len - sequence_length, 0, 0, 0, 0)
    )
    x = torch.reshape(
        x, (flat_batchsize, num_sequences, nstep_per_segment, sequence_stride)
    )
    # For obtaining shifted signals, this routine reinterprets flattened array
    # with a shrinked axis.  With appropriate truncation/ padding, this
    # operation pushes the last padded elements of the previous row to the head
    # of the current row.
    # See implementation of `overlap_and_add` in Tensorflow for details.
    x = torch.permute(x, (0, 2, 1, 3))  # x: (B, S, N, T)
    x = torch.nn.functional.pad(x, (0, 0, 0, num_sequences, 0, 0, 0, 0))
    # x: (B, S, N*2, T)
    shrinked = x.shape[2] - 1
    x = torch.reshape(x, (flat_batchsize, -1))
    x = x[:, : (nstep_per_segment * shrinked * sequence_stride)]
    x = torch.reshape(
        x, (flat_batchsize, nstep_per_segment, shrinked * sequence_stride)
    )
    # Finally, sum shifted segments, and truncate results to the output_size.
    x = torch.sum(x, dim=1)[:, :output_size]
    return torch.reshape(x, tuple(batch_shape) + (-1,))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::ExtractSequencesOpTest.calculate_expected_shape [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py]
    def calculate_expected_shape(
        self, input_shape, sequence_length, sequence_stride
    ):
        num_sequences = (
            (input_shape[1] - sequence_length) // sequence_stride
        ) + 1
        return (input_shape[0], num_sequences, sequence_length)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::scan [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py]
def scan(f, init, xs=None, length=None, reverse=False, unroll=1):
    # Ref: jax.lax.scan
    if not callable(f):
        raise TypeError(f"`f` should be a callable. Received: f={f}")
    if not isinstance(unroll, bool):
        if not isinstance(unroll, int) or unroll < 1:
            raise ValueError(
                "`unroll` must be an positive integer or boolean. "
                f"Received: unroll={unroll}"
            )
    if xs is None and length is None:
        raise ValueError("Got no `xs` to scan over and `length` not provided.")

    input_is_sequence = tree.is_nested(xs)
    output_is_sequence = tree.is_nested(init)

    def pack_input(x):
        return tree.pack_sequence_as(xs, x) if input_is_sequence else x[0]

    def pack_output(x):
        return tree.pack_sequence_as(init, x) if output_is_sequence else x[0]

    if xs is None:
        xs_flat = []
        n = int(length)
    else:
        xs_flat = tree.flatten(xs)
        xs_flat = [convert_to_tensor(elem) for elem in xs_flat]
        n = (
            int(length)
            if length is not None
            else (shape(xs_flat[0])[0] if xs_flat else 0)
        )

    init_flat = tree.flatten(init)
    init_flat = [convert_to_tensor(i) for i in init_flat]
    init = pack_output(init_flat)

    dummy_y = []
    for i in init_flat:
        i_ov = get_ov_output(i)
        zero = ov_opset.constant(0, i_ov.get_element_type()).output(0)
        shape_node = ov_opset.shape_of(i_ov, Type.i32).output(0)
        dummy_y.append(
            OpenVINOKerasTensor(ov_opset.broadcast(zero, shape_node).output(0))
        )

    carry = init
    ys = []
    maybe_reversed = reversed if reverse else lambda x: x
    for i in maybe_reversed(range(n)):
        xs_slice = [x[i] for x in xs_flat]
        packed_xs = pack_input(xs_slice) if len(xs_slice) > 0 else None
        carry, y = f(carry, packed_xs)
        ys.append(y if y is not None else dummy_y)

    def _stack(tensors):
        elems = [get_ov_output(t) for t in tensors]
        const_axis = ov_opset.constant(0, Type.i32).output(0)
        elems = [ov_opset.unsqueeze(e, const_axis).output(0) for e in elems]
        return OpenVINOKerasTensor(ov_opset.concat(elems, 0).output(0))

    stacked_y = tree.map_structure(
        lambda *y: _stack(list(y)), *maybe_reversed(ys)
    )
    return carry, stacked_y

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::extract_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py]
def extract_sequences(x, sequence_length, sequence_stride):
    return tf.signal.frame(
        x,
        frame_length=sequence_length,
        frame_step=sequence_stride,
        axis=-1,
        pad_end=False,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/numpy.py::vstack [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/numpy.py]
def vstack(xs):
    return jnp.vstack(xs)
```
