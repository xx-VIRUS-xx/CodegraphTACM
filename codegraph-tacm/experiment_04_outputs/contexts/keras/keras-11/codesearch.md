# keras-11 :: codesearch

query: Improve type-check for Sequence (#11468)

## selected nodes

- rank=1 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/image_dataset_utils_test.py::ImageDatasetFromDirectoryTest.symbolic_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/image_dataset_utils_test.py
- rank=2 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential._obj_type file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=3 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/audio_dataset_utils_test.py::AudioDatasetFromDirectoryTest.symbolic_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/audio_dataset_utils_test.py
- rank=4 layer=FUNCTION tokens=639 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py::extract_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/math.py
- rank=5 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::ExtractSequences.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py
- rank=6 layer=FUNCTION tokens=453 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::pack_sequence_as file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=7 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py::SparseTest.assertSparseness file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py
- rank=8 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_output_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=9 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_has_fully_masked_sequence file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=10 layer=FUNCTION tokens=217 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py::_has_fully_masked_sequence file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py
- rank=11 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::extract_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py
- rank=12 layer=FUNCTION tokens=316 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional._maybe_warn_inputs_struct_mismatch file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=13 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::ExtractSequencesOpTest.calculate_expected_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py
- rank=14 layer=FUNCTION tokens=383 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_test.py::_get_sequence_classifier file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_test.py
- rank=15 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py::pack_sequence_as file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py
- rank=16 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::extract_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py
- rank=17 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py::func_with_check file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py
- rank=18 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=19 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=20 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py::check_data_cardinality file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/data_adapter_utils.py
- rank=21 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py::SparseTest.assertSameSparseness file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/image_dataset_utils_test.py::ImageDatasetFromDirectoryTest.symbolic_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/image_dataset_utils_test.py]
        def symbolic_fn(ds):
            for x, _ in ds.take(1):
                test_obj.assertListEqual(x.shape.as_list(), output_shape)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential._obj_type [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py]
    def _obj_type(self):
        return "Sequential"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/audio_dataset_utils_test.py::AudioDatasetFromDirectoryTest.symbolic_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/audio_dataset_utils_test.py]
        def symbolic_fn(ds):
            for x, _ in ds.take(1):
                test_obj.assertListEqual(x.shape.as_list(), [None, 30, None])

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py::ExtractSequences.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math.py]
    def __init__(self, sequence_length, sequence_stride, *, name=None):
        super().__init__(name=name)
        self.sequence_length = sequence_length
        self.sequence_stride = sequence_stride

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py::SparseTest.assertSparseness [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py]
    def assertSparseness(self, x, expected_sparseness):
        self.assertEqual(sparseness(x), expected_sparseness)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_output_shape [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py]
    def compute_output_shape(self, sequences_shape, initial_state_shape=None):
        batch_size = sequences_shape[0]
        length = sequences_shape[1]
        states_shape = []
        for state_size in self.state_size:
            if isinstance(state_size, int):
                states_shape.append((batch_size, state_size))
            elif isinstance(state_size, (list, tuple)):
                states_shape.append([(batch_size, s) for s in state_size])

        output_size = getattr(self.cell, "output_size", None)
        if output_size is None:
            output_size = self.state_size[0]
        if not isinstance(output_size, int):
            raise ValueError("output_size must be an integer.")
        if self.return_sequences:
            output_shape = (batch_size, length, output_size)
        else:
            output_shape = (batch_size, output_size)
        if self.return_state:
            return output_shape, *states_shape
        return output_shape

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py::extract_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/math.py]
def extract_sequences(x, sequence_length, sequence_stride):
    *batch_shape, signal_length = x.shape
    batch_shape = list(batch_shape)
    x = jnp.reshape(x, (math.prod(batch_shape), signal_length, 1))
    x = jax.lax.conv_general_dilated_patches(
        x,
        (sequence_length,),
        (sequence_stride,),
        "VALID",
        dimension_numbers=("NTC", "OIT", "NTC"),
    )
    return jnp.reshape(x, (*batch_shape, *x.shape[-2:]))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional._maybe_warn_inputs_struct_mismatch [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py]
    def _maybe_warn_inputs_struct_mismatch(self, inputs, raise_exception=False):
        try:
            # We first normalize to tuples before performing the check to
            # suppress warnings when encountering mismatched tuples and lists.
            tree.assert_same_structure(
                tree.lists_to_tuples(inputs),
                tree.lists_to_tuples(self._inputs_struct),
            )
        except:
            model_inputs_struct = tree.map_structure(
                lambda x: "None" if x is None else x.name,
                self._inputs_struct,
            )
            inputs_struct = tree.map_structure(
                lambda x: "None" if x is None else f"Tensor(shape={x.shape})",
                inputs,
            )
            msg = (
                "The structure of `inputs` doesn't match the expected "
                f"structure.\nExpected: {model_inputs_struct}\n"
                f"Received: inputs={inputs_struct}"
            )
            if raise_exception:
                raise ValueError(msg)
            warnings.warn(msg)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py::ExtractSequencesOpTest.calculate_expected_shape [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/math_test.py]
    def calculate_expected_shape(
        self, input_shape, sequence_length, sequence_stride
    ):
        num_sequences = (
            (input_shape[1] - sequence_length) // sequence_stride
        ) + 1
        return (input_shape[0], num_sequences, sequence_length)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_test.py::_get_sequence_classifier [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/awq_test.py]
def _get_sequence_classifier():
    """Create a transformer-based sequence classifier for testing."""
    embed_dim = 32
    num_heads = 4
    ff_dim = 32

    class SimpleTransformerBlock(layers.Layer):
        def __init__(self, embed_dim, num_heads, ff_dim, **kwargs):
            super().__init__(**kwargs)
            self.att = layers.MultiHeadAttention(
                num_heads=num_heads, key_dim=embed_dim // num_heads
            )
            self.ffn = models.Sequential(
                [
                    layers.Dense(ff_dim, activation="relu"),
                    layers.Dense(embed_dim),
                ]
            )
            self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
            self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)

        def call(self, inputs):
            attention_output = self.att(inputs, inputs)
            out1 = self.layernorm1(inputs + attention_output)
            ffn_output = self.ffn(out1)
            return self.layernorm2(out1 + ffn_output)

    inputs = layers.Input(shape=(SEQ_LEN,), dtype="int32")
    x = layers.Embedding(VOCAB_SIZE, embed_dim)(inputs)
    x = SimpleTransformerBlock(embed_dim, num_heads, ff_dim)(x)
    x = layers.GlobalAveragePooling1D(data_format="channels_last")(x)
    outputs = layers.Dense(NUM_CLASSES)(x)
    return models.Model(inputs, outputs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py::pack_sequence_as [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py]
def pack_sequence_as(structure, flat_sequence):
    # We need to first sort dicts to ensure a deterministic order that is
    # consistent with other tree implementations.
    structure = _dict_to_ordered_dict(structure)
    _, treespec = torch_tree.tree_flatten(structure)
    return torch_tree.tree_unflatten(flat_sequence, treespec)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py::extract_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/math.py]
def extract_sequences(x, sequence_length, sequence_stride):
    return tf.signal.frame(
        x,
        frame_length=sequence_length,
        frame_step=sequence_stride,
        axis=-1,
        pad_end=False,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py::func_with_check [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/optree_impl.py]
    def func_with_check(*args):
        if not all(
            optree.tree_is_leaf(s, none_is_leaf=none_is_leaf, namespace="keras")
            for s in args
        ):
            raise ValueError("Structures don't have the same nested structure.")
        return func(*args)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def fit_on_sequences(self, sequences):
        self.document_count += len(sequences)
        for seq in sequences:
            seq = set(seq)
            for i in seq:
                self.index_docs[i] += 1

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py]
            def key_check_fn(key, objs):
                return all(
                    [
                        issubclass(type(obj), (list, tuple)) and key < len(obj)
                        for obj in objs
                    ]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py::SparseTest.assertSameSparseness [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/numpy_test.py]
    def assertSameSparseness(self, x, y):
        self.assertEqual(sparseness(x), sparseness(y))
```
