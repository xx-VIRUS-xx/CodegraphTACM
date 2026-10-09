# keras-11 :: tacm-dyn-l4

query: Improve type-check for Sequence (#11468)

## selected nodes

- rank=1 layer=FILE tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/fixes.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/fixes.py
- rank=2 layer=CLASS tokens=379 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes_test.py::DtypesTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes_test.py
- rank=3 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py::_has_fully_masked_sequence file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py
- rank=4 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_has_fully_masked_sequence file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=5 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=6 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::stft file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=7 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::stft file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py
- rank=8 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py::stft file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/math.py
- rank=9 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py::stft file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/math.py
- rank=10 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=11 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::stft file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=12 layer=FILE tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py
- rank=13 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py::_least_upper_bound file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py
- rank=14 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::extract_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=15 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py
- rank=16 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/reversible_embedding.py::ReversibleEmbedding.quantize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/reversible_embedding.py
- rank=17 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense.py::EinsumDense.quantize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/einsum_dense.py
- rank=18 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py::result_type file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py
- rank=19 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::pack_sequence_as file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=20 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense.py::Dense.quantize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/dense.py
- rank=21 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/embedding.py::Embedding.quantize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/embedding.py
- rank=22 layer=CLASS tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/hashed_crossing.py::HashedCrossing file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/hashed_crossing.py
- rank=23 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/hashed_crossing.py::HashedCrossing.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/hashed_crossing.py
- rank=24 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/hashed_crossing.py::HashedCrossing._check_input_shape_and_type file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/hashed_crossing.py
- rank=25 layer=FILE tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py
- rank=26 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py::pack_sequence_as file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py
- rank=27 layer=FUNCTION tokens=169 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py::map_structure file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py
- rank=28 layer=FUNCTION tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/fixes.py::type_of_target file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/fixes.py
- rank=29 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/fixes.py::_raise_or_return file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/fixes.py
- rank=30 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_test.py::_string_dataset file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_test.py
- rank=31 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.quantize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=32 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=33 layer=FILE tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/preprocessing/sequence/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/api/_tf_keras/keras/preprocessing/sequence/__init__.py

## context

```text
file wrappers/fixes.py
imports: sklearn
defines: _validate_data, type_of_target, _raise_or_return, _routing_enabled, _raise_for_params

class DtypesTest(test_case.TestCase):  [backend/common/dtypes_test.py:13]
methods: mock_lattice
         test_cycle_detection_in_make_lattice_upper_bounds
         test_empty_lub_in_least_upper_bound
         test_invalid_dtype_for_keras_promotion
         test_invalid_dtype_in_least_upper_bound
         test_invalid_float8_dtype
         test_least_upper_bound_ensure_order_independence
         test_least_upper_bound_no_element
         test_least_upper_bound_single_element
         test_least_upper_bound_with_no_common_upper_bound
         test_resolve_weak_type_bool
         test_resolve_weak_type_float
         test_resolve_weak_type_for_bfloat16
         test_resolve_weak_type_for_bfloat16_with_precision
         test_resolve_weak_type_for_invalid_dtype
         test_resolve_weak_type_for_invalid_precision
         test_resolve_weak_type_int
         test_resolve_weak_type_uint
         test_respect_weak_type_for_bool
         test_respect_weak_type_for_complex128
         test_respect_weak_type_for_complex64
         test_respect_weak_type_for_float
         test_respect_weak_type_for_int
         test_respect_weak_type_for_invalid_dtype
         test_result_type_empty_list
         test_result_type_with_float64
         test_result_type_with_int64
         test_result_type_with_none
         test_result_type_with_python_scalar_types
         test_result_type_with_tensor
         test_valid_dtype_leading_to_keyerror_and_valueerror
         test_valid_dtype_leading_to_single_lub_element

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

            def key_check_fn(key, objs):
                return all(
                    [
                        issubclass(type(obj), (list, tuple)) and key < len(obj)
                        for obj in objs
                    ]
                )

def stft(
    x, sequence_length, sequence_stride, fft_length, window="hann", center=True
):
    if standardize_dtype(x.dtype) not in {"float32", "float64"}:
        raise TypeError(
            "Invalid input type. Expected `float32` or `float64`. "
            f"Received: input type={x.dtype}"
        )
    if fft_length < sequence_length:
        raise ValueError(
            "`fft_length` must equal or larger than `sequence_length`. "
            f"Received: sequence_length={sequence_length}, "
    # ... truncated

def stft(
    x, sequence_length, sequence_stride, fft_length, window="hann", center=True
):
    if standardize_dtype(x.dtype) not in {"float32", "float64"}:
        raise TypeError(
            "Invalid input type. Expected `float32` or `float64`. "
            f"Received: input type={x.dtype}"
        )
    if fft_length < sequence_length:
        raise ValueError(
            "`fft_length` must equal or larger than `sequence_length`. "
            f"Received: sequence_length={sequence_length}, "
    # ... truncated

def stft(
    x, sequence_length, sequence_stride, fft_length, window="hann", center=True
):
    if standardize_dtype(x.dtype) not in {"float32", "float64"}:
        raise TypeError(
            "Invalid input type. Expected `float32` or `float64`. "
            f"Received: input type={x.dtype}"
        )
    if fft_length < sequence_length:
        raise ValueError(
            "`fft_length` must equal or larger than `sequence_length`. "
            f"Received: sequence_length={sequence_length}, "
    # ... truncated

def stft(
    x, sequence_length, sequence_stride, fft_length, window="hann", center=True
):
    if standardize_dtype(x.dtype) not in {"float32", "float64"}:
        raise TypeError(
            "Invalid input type. Expected `float32` or `float64`. "
            f"Received: input type={x.dtype}"
        )
    if fft_length < sequence_length:
        raise ValueError(
            "`fft_length` must equal or larger than `sequence_length`. "
            f"Received: sequence_length={sequence_length}, "
    # ... truncated

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

def stft(
    x, sequence_length, sequence_stride, fft_length, window="hann", center=True
):
    if standardize_dtype(x.dtype) not in {"float32", "float64"}:
        raise TypeError(
            "Invalid input type. Expected `float32` or `float64`. "
            f"Received: input type={x.dtype}"
        )
    if fft_length < sequence_length:
        raise ValueError(
            "`fft_length` must equal or larger than `sequence_length`. "
            f"Received: sequence_length={sequence_length}, "
    # ... truncated

file backend/common/dtypes.py
imports: functools, keras
defines: _type_promotion_lattice, _make_lattice_upper_bounds, _least_upper_bound, _dtype_and_weaktype, _respect_weak_type, _resolve_weak_type, _lattice_result_type, result_type

def _least_upper_bound(*nodes):
    """Compute the least upper bound of a set of nodes.

    Args:
        nodes: sequence of entries from dtypes + weak_types

    Returns:
        The type representing the least upper bound of the input nodes on the
        promotion lattice.
    """
    # ... truncated

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
    # ... truncated

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

    def quantize(self, mode=None, type_check=True, config=None):
        if type_check and type(self) is not ReversibleEmbedding:
            raise self._not_implemented_error(self.quantize)

        self.quantization_config = config

        embeddings_shape = (self.input_dim, self.output_dim)
        if mode == "int8":
            # Quantize `self._embeddings` to int8 and compute corresponding
            # scale.
            weight_quantizer = QuantizationConfig.weight_quantizer_or_default(
                self.quantization_config, quantizers.AbsMaxQuantizer(axis=-1)
    # ... truncated

    def quantize(self, mode=None, type_check=True, config=None):
        # Prevent quantization of the subclasses
        if type_check and (type(self) is not EinsumDense):
            raise self._not_implemented_error(self.quantize)

        self.quantization_config = config

        kernel_shape = self._kernel.shape
        if mode in ("int8", "int4", "gptq", "awq"):
            self._set_quantization_info()

        if mode == "int8":
    # ... truncated

def result_type(*dtypes):
    """Returns the type from applying the Keras type promotion rules.

    In general, each argument is first parsed by `backend.standardize_dtype`,
    and the resulting dtype is determined by the least upper bound of the type
    promotion lattice.

    Note: This function attempts to match the result of `jnp.result_type`.

    Args:
        dtypes: Input dtypes.

    # ... truncated

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

    # ... truncated

    def quantize(self, mode=None, type_check=True, config=None):
        # Prevent quantization of the subclasses
        if type_check and (type(self) is not Dense):
            raise self._not_implemented_error(self.quantize)

        self.quantization_config = config

        kernel_shape = self._kernel.shape
        if mode == "int8":
            weight_quantizer = QuantizationConfig.weight_quantizer_or_default(
                self.quantization_config, quantizers.AbsMaxQuantizer(axis=0)
            )
    # ... truncated

    def quantize(self, mode=None, type_check=True, config=None):
        # Prevent quantization of the subclasses.
        if type_check and (type(self) is not Embedding):
            raise self._not_implemented_error(self.quantize)

        self.quantization_config = config

        embeddings_shape = (self.input_dim, self.output_dim)
        if mode == "int8":
            # Quantize `self._embeddings` to int8 and compute corresponding
            # scale.
            weight_quantizer = QuantizationConfig.weight_quantizer_or_default(
    # ... truncated

class HashedCrossing(Layer):  [layers/preprocessing/hashed_crossing.py:12]
methods: _check_at_least_two_inputs, _check_input_shape_and_type
         call, compute_output_shape, get_config, __init__

    def call(self, inputs):
        from keras.src.backend import tensorflow as tf_backend

        self._check_at_least_two_inputs(inputs)
        inputs = [tf_utils.ensure_tensor(x) for x in inputs]
        self._check_input_shape_and_type(inputs)

        with tf.device("CPU:0"):
            # Uprank to rank 2 for the cross_hashed op.
            first_shape = tuple(inputs[0].shape)
            rank = len(first_shape)
            if rank < 2:
    # ... truncated

    def _check_input_shape_and_type(self, inputs):
        first_shape = tuple(inputs[0].shape)
        rank = len(first_shape)
        if rank > 2 or (rank == 2 and first_shape[-1] != 1):
            raise ValueError(
                "All `HashedCrossing` inputs should have shape `()`, "
                "`(batch_size)` or `(batch_size, 1)`. "
                f"Received: inputs={inputs}"
            )
        if not all(tuple(x.shape) == first_shape for x in inputs[1:]):
            raise ValueError(
                "All `HashedCrossing` inputs should have equal shape. "
                f"Received: inputs={inputs}"
            )
        if any(
            isinstance(x, (tf.RaggedTensor, tf.SparseTensor)) for x in inputs
        ):
            raise ValueError(
                "All `HashedCrossing` inputs should be dense tensors. "
                f"Received: inputs={inputs}"
            )
        if not all(
            tf.as_dtype(x.dtype).is_integer or x.dtype == tf.string
            for x in inputs
        ):
            raise ValueError(
                "All `HashedCrossing` inputs should have an integer or "
                f"string dtype. Received: inputs={inputs}"
            )

file tree/optree_impl.py
imports: optree, keras, tensorflow
defines: register_tree_node_class, sorted_keys_and_values, is_nested, traverse, traverse_children, flatten, flatten_with_path, map_structure, func_with_check, map_structure_up_to, func_with_check_without_shallow_structure, assert_same_structure, check, assert_same_paths, pack_sequence_as, lists_to_tuples, list_to_tuple, map_shape_structure, is_shape_tuple

def pack_sequence_as(structure, flat_sequence):
    _, treespec = optree.tree_flatten(
        structure, none_is_leaf=True, namespace="keras"
    )
    return optree.tree_unflatten(treespec, flat_sequence)

    def func_with_check(*args):
        if not all(
            optree.tree_is_leaf(s, none_is_leaf=none_is_leaf, namespace="keras")
            for s in args
        ):
            raise ValueError("Structures don't have the same nested structure.")
        return func(*args)

    def _raise_or_return(target_type):
        """Depending on the value of raise_unknown, either raise an error or
        return 'unknown'.
        """
        if raise_unknown and target_type == "unknown":
            input = input_name if input_name else "data"
            raise ValueError(f"Unknown label type for {input}: {y!r}")
        else:
            return target_type

# --- Layer 04: Variable context ---
# call-chain context
  called by: _assert_valid_mask [rnn.py]

# call-chain context
  called by: _assert_valid_mask [rnn.py]

# call-chain context
  called by: _build_nested [compile_utils.py]

# call-chain context
  called by: _spectrogram [mel_spectrogram.py]
  called by: _stft [math_test.py]

# call-chain context
  called by: _spectrogram [mel_spectrogram.py]
  called by: _stft [math_test.py]

# call-chain context
  called by: _spectrogram [mel_spectrogram.py]
  called by: _stft [math_test.py]

# call-chain context
  called by: _spectrogram [mel_spectrogram.py]
  called by: _stft [math_test.py]

# call-chain context
  called by: histogram [numpy.py]

# call-chain context
  called by: _spectrogram [mel_spectrogram.py]
  called by: _stft [math_test.py]

# call-chain context
  called by: _lattice_result_type [dtypes.py]

# call-chain context
  called by: linear_to_mel_weight_matrix [mel_spectrogram.py]

# call-chain context
  called by: create_and_quantize [gptq_test.py]

# call-chain context
  called by: create_and_quantize [gptq_test.py]

# call-chain context
  called by: rgb_to_grayscale [image.py]
  called by: norm [linalg.py]

# call-chain context
  called by: _get_input_tensor [rnn.py]
  called by: rnn [rnn.py]

# call-chain context
  called by: create_and_quantize [gptq_test.py]

# call-chain context
  called by: create_and_quantize [gptq_test.py]

# call-chain context
  called by: call [hashed_crossing.py]

# call-chain context
  called by: _get_input_tensor [rnn.py]
  called by: rnn [rnn.py]

# call-chain context
  called by: type_of_target [fixes.py]

```
