# keras-11 :: hybrid

query: Improve type-check for Sequence (#11468)

## selected nodes

- rank=1 layer=FUNCTION tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=2 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=3 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py
- rank=4 layer=FUNCTION tokens=1173 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils.py::pad_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils.py
- rank=5 layer=FUNCTION tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::traverse_bottom_up file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=6 layer=FUNCTION tokens=453 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::pack_sequence_as file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=7 layer=FUNCTION tokens=233 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::unflatten_func file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=8 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_has_fully_masked_sequence file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=9 layer=FUNCTION tokens=628 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::scan file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py
- rank=10 layer=FUNCTION tokens=348 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=11 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::ExtractSequences.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=12 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py::pack_input file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py
- rank=13 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential._obj_type file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py]
            def key_check_fn(key, objs):
                return all(
                    [
                        issubclass(type(obj), (list, tuple)) and key < len(obj)
                        for obj in objs
                    ]
                )

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils.py::pad_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils.py]
def pad_sequences(
    sequences,
    maxlen=None,
    dtype="int32",
    padding="pre",
    truncating="pre",
    value=0.0,
):
    """Pads sequences to the same length.

    This function transforms a list (of length `num_samples`)
    of sequences (lists of integers)
    into a 2D NumPy array of shape `(num_samples, num_timesteps)`.
    `num_timesteps` is either the `maxlen` argument if provided,
    or the length of the longest sequence in the list.

    Sequences that are shorter than `num_timesteps`
    are padded with `value` until they are `num_timesteps` long.

    Sequences longer than `num_timesteps` are truncated
    so that they fit the desired length.

    The position where padding or truncation happens is determined by
    the arguments `padding` and `truncating`, respectively.
    Pre-padding or removing values from the beginning of the sequence is the
    default.

    >>> sequence = [[1], [2, 3], [4, 5, 6]]
    >>> keras.utils.pad_sequences(sequence)
    array([[0, 0, 1],
           [0, 2, 3],
           [4, 5, 6]], dtype=int32)

    >>> keras.utils.pad_sequences(sequence, value=-1)
    array([[-1, -1,  1],
           [-1,  2,  3],
           [ 4,  5,  6]], dtype=int32)

    >>> keras.utils.pad_sequences(sequence, padding='post')
    array([[1, 0, 0],
           [2, 3, 0],
           [4, 5, 6]], dtype=int32)

    >>> keras.utils.pad_sequences(sequence, maxlen=2)
    array([[0, 1],
           [2, 3],
           [5, 6]], dtype=int32)

    Args:
        sequences: List of sequences (each sequence is a list of integers).
        maxlen: Optional Int, maximum length of all sequences. If not provided,
            sequences will be padded to the length of the longest individual
            sequence.
        dtype: (Optional, defaults to `"int32"`). Type of the output sequences.
            To pad sequences with variable length strings, you can use `object`.
        padding: String, "pre" or "post" (optional, defaults to `"pre"`):
            pad either before or after each sequence.
        truncating: String, "pre" or "post" (optional, defaults to `"pre"`):
            remove values from sequences larger than
            `maxlen`, either at the beginning or at the end of the sequences.
        value: Float or String, padding value. (Optional, defaults to `0.`)

    Returns:
        NumPy array with shape `(len(sequences), maxlen)`
    """
    if not hasattr(sequences, "__len__"):
        raise ValueError("`sequences` must be iterable.")
    num_samples = len(sequences)

    lengths = []
    sample_shape = ()
    flag = True

    # take the sample shape from the first non empty sequence
    # checking for consistency in the main loop below.

    for x in sequences:
        try:
            lengths.append(len(x))
            if flag and len(x):
                sample_shape = np.asarray(x).shape[1:]
                flag = False
        except TypeError as e:
            raise ValueError(
                "`sequences` must be a list of iterables. "
                f"Found non-iterable: {str(x)}"
            ) from e

    if maxlen is None:
        maxlen = np.max(lengths)

    is_dtype_str = np.issubdtype(dtype, np.str_) or np.issubdtype(
        dtype, np.str_
    )
    if isinstance(value, str) and dtype is not object and not is_dtype_str:
        raise ValueError(
            f"`dtype` {dtype} is not compatible with `value`'s type: "
            f"{type(value)}\nYou should set `dtype=object` for variable length "
            "strings."
        )

    x = np.full((num_samples, maxlen) + sample_shape, value, dtype=dtype)
    for idx, s in enumerate(sequences):
        if not len(s):
            continue  # empty list/array was found
        if truncating == "pre":
            trunc = s[-maxlen:]
        elif truncating == "post":
            trunc = s[:maxlen]
        else:
            raise ValueError(f'Truncating type "{truncating}" not understood')

        # check `trunc` has expected shape
        trunc = np.asarray(trunc, dtype=dtype)
        if trunc.shape[1:] != sample_shape:
            raise ValueError(
                f"Shape of sample {trunc.shape[1:]} of sequence at "
                f"position {idx} is different from expected shape "
                f"{sample_shape}"
            )

        if padding == "post":
            x[idx, : len(trunc)] = trunc
        elif padding == "pre":
            x[idx, -len(trunc) :] = trunc
        else:
            raise ValueError(f'Padding type "{padding}" not understood')
    return x

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::traverse_bottom_up [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py]
    def traverse_bottom_up(s):
        registration = REGISTERED_CLASSES.get(type(s), None)
        if registration is not None:
            flat_meta_s = registration.flatten(s)
            ret = [traverse_bottom_up(x) for x in list(flat_meta_s[0])]
            ret = registration.unflatten(flat_meta_s[1], ret)
        elif not dmtree.is_nested(s):
            ret = s
        elif isinstance(s, collections.abc.Mapping):
            ret = [traverse_bottom_up(s[key]) for key in sorted(s)]
            ret = dmtree._sequence_like(s, ret)
        else:
            ret = [traverse_bottom_up(x) for x in s]
            ret = dmtree._sequence_like(s, ret)
        func_ret = func(ret)
        return ret if func_ret is None else remap_map_to_none(func_ret, None)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::unflatten_func [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::ExtractSequences.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
    def call(self, x):
        return backend.math.extract_sequences(
            x,
            sequence_length=self.sequence_length,
            sequence_stride=self.sequence_stride,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py::pack_input [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py]
    def pack_input(x):
        return tree.pack_sequence_as(xs, x) if input_is_sequence else x[0]

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential._obj_type [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py]
    def _obj_type(self):
        return "Sequential"
```
