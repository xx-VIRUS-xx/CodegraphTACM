# keras-19 :: tacm-dyn

query: Update the RNN cell API to be explicit about output_size. (#11021)

## selected nodes

- rank=1 layer=FILE tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=2 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py::RNNCellWithDropout file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py
- rank=3 layer=CLASS tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=4 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=5 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=6 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.get_initial_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=7 layer=FUNCTION tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=8 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py::DropoutRNNCellTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py
- rank=9 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=10 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=11 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=12 layer=CLASS tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells_test.py::StackedRNNTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells_test.py
- rank=13 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=14 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=15 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=16 layer=CLASS tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/tree_api.py::MAP_TO_NONE file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/tree_api.py
- rank=17 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.get_initial_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=18 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=19 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/progbar.py::Progbar.update file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/progbar.py
- rank=20 layer=FUNCTION tokens=211 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_assert_valid_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=21 layer=CLASS tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=22 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._ensure_vocab_size_unchanged file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=23 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._ensure_known_vocab_size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=24 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py::rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/torch/rnn.py
- rank=25 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/iou_metrics.py::_IoUBase.update_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/metrics/iou_metrics.py
- rank=26 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/python_utils.py::ensure_value_to_cell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/python_utils.py
- rank=27 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::unique file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py
- rank=28 layer=FUNCTION tokens=386 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/api_gen.py::build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/api_gen.py
- rank=29 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/image_utils.py::smart_resize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/image_utils.py
- rank=30 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation_utils.py::compute_pooling_output_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation_utils.py
- rank=31 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::inject_argument_info_in_traceback file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py
- rank=32 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib.py::serialize_keras_object file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib.py
- rank=33 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_utils.py::named_product file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_utils.py
- rank=34 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/rnn.py::rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/rnn.py
- rank=35 layer=FUNCTION tokens=8 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/numpy.py::size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/numpy.py

## context

```text
file layers/rnn/dropout_rnn_cell.py
imports: keras
defines: DropoutRNNCell

class RNNCellWithDropout(layers.Layer, DropoutRNNCell):  [layers/rnn/dropout_rnn_cell_test.py:8]
methods: build, call, __init__

class DropoutRNNCell:  [layers/rnn/dropout_rnn_cell.py:5]
methods: _create_dropout_mask, get_dropout_mask
         get_recurrent_dropout_mask, reset_dropout_mask
         reset_recurrent_dropout_mask

    def reset_dropout_mask(self):
        """Reset the cached dropout mask if any.

        The RNN layer invokes this in the `call()` method
        so that the cached mask is cleared after calling `cell.call()`. The
        mask should be cached across all timestep within the same batch, but
        shouldn't be cached between batches.
        """
        self._dropout_mask = None

    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

    def get_initial_state(self, batch_size):
        get_initial_state_fn = getattr(self.cell, "get_initial_state", None)
        if get_initial_state_fn:
            init_state = get_initial_state_fn(batch_size=batch_size)
        else:
            return [
                ops.zeros((batch_size, d), dtype=self.cell.compute_dtype)
                for d in self.state_size
            ]

        # RNN expect the states in a list, even if single state.
        if not tree.is_nested(init_state):
            init_state = [init_state]
        # Force the state to be a list in case it is a namedtuple eg
        # LSTMStateTuple.
        return list(init_state)

    def build(self, sequences_shape, initial_state_shape=None):
        # Build cell (if layer).
        step_input_shape = (sequences_shape[0],) + tuple(sequences_shape[2:])
        if isinstance(self.cell, Layer) and not self.cell.built:
            self.cell.build(step_input_shape)
            self.cell.built = True
        if self.stateful:
            if self.states is not None:
                self.reset_state()
            else:
                if sequences_shape[0] is None:
                    raise ValueError(
                        "When using `stateful=True` in a RNN, the "
                        "batch size must be static. Found dynamic "
                        f"batch size: sequence.shape={sequences_shape}"
                    )
                self._create_state_variables(sequences_shape[0])
                self._expected_batch_size = ops.shape(
                    tree.flatten(self.states)[0]
                )[0]

class DropoutRNNCellTest(testing.TestCase):  [layers/rnn/dropout_rnn_cell_test.py:45]
methods: test_basics, test_seed_tracking

    def build(self, input_shape):
        for cell in self.cells:
            if isinstance(cell, Layer) and not cell.built:
                cell.build(input_shape)
                cell.built = True
            if getattr(cell, "output_size", None) is not None:
                output_dim = cell.output_size
            elif isinstance(cell.state_size, (list, tuple)):
                output_dim = cell.state_size[0]
            else:
                output_dim = cell.state_size
            batch_size = tree.flatten(input_shape)[0]
            input_shape = (batch_size, output_dim)

class StackedRNNCells(Layer):  [layers/rnn/stacked_rnn_cells.py:9]
methods: build, call, from_config, get_config, get_initial_state
         output_size, state_size, __init__

    def __init__(self, cells, **kwargs):
        super().__init__(**kwargs)
        for cell in cells:
            if "call" not in dir(cell):
                raise ValueError(
                    "All cells must have a `call` method. "
                    f"Received cell without a `call` method: {cell}"
                )
            if "state_size" not in dir(cell):
                raise ValueError(
                    "All cells must have a `state_size` attribute. "
                    f"Received cell without a `state_size`: {cell}"
                )
        self.cells = cells

class StackedRNNTest(testing.TestCase):  [layers/rnn/stacked_rnn_cells_test.py:9]
methods: test_basics, test_correctness_single_state_stack
         test_correctness_two_states_stack
         test_return_state_stacked_lstm_cell
         test_stacked_lstm_cell_mask
         test_statefullness_single_state_stack
         test_statefullness_two_states_stack

    def output(self):
        return self._outputs_struct

    def compute_mask(self, _, mask):
        # Time step masks must be the same for each input.
        # This is because the mask for an RNN is of size [batch, time_steps, 1],
        # and specifies which time steps should be skipped, and a time step
        # must be skipped for all inputs.
        mask = tree.flatten(mask)[0]
        output_mask = mask if self.return_sequences else None
        if self.return_state:
            state_mask = [None for _ in self.state_size]
            return [output_mask] + state_mask
        else:
            return output_mask

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,
    # ... truncated

class MAP_TO_NONE:  [tree/tree_api.py:28]
methods: —

    def get_initial_state(self, batch_size=None):
        initial_states = []
        for cell in self.cells:
            get_initial_state_fn = getattr(cell, "get_initial_state", None)
            if get_initial_state_fn:
                initial_states.append(
                    get_initial_state_fn(batch_size=batch_size)
                )
            else:
                if isinstance(cell.state_size, int):
                    initial_states.append(
                        ops.zeros(
                            (batch_size, cell.state_size),
                            dtype=self.compute_dtype,
                        )
                    )
                else:
                    initial_states.append(
                        [
                            ops.zeros((batch_size, d), dtype=self.compute_dtype)
                            for d in cell.state_size
                        ]
                    )
        return initial_states

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,
    # ... truncated

    def update(self, current, values=None, finalize=None):
        """Updates the progress bar.

        Args:
            current: Index of current step.
            values: List of tuples: `(name, value_for_last_step)`. If `name` is
                in `stateful_metrics`, `value_for_last_step` will be displayed
                as-is. Else, an average of the metric over time will be
                displayed.
            finalize: Whether this is the last update for the progress bar. If
                `None`, defaults to `current >= self.target`.
        """
    # ... truncated

def _assert_valid_mask(mask):
    valid = tf.logical_and(
        tf.logical_not(_has_fully_masked_sequence(mask)),
        _is_sequence_right_padded(mask),
    )
    tf.Assert(
        valid,
        [
            (
                "You are passing a RNN mask that does not correspond to "
                "right-padded sequences, while using cuDNN, which is not "
                "supported. With cuDNN, RNN masks can only be used for "
                "right-padding, e.g. `[[True, True, False, False]]` would "
                "be a valid mask, but any mask that isn't just contiguous "
                "`True`'s on the left and contiguous `False`'s on the right "
                "would be invalid. You can pass `use_cudnn=False` to your "
                "RNN layer to stop using cuDNN (this may be slower)."
            )
        ],
    )

class IndexLookup(Layer):  [layers/preprocessing/index_lookup.py:14]
methods: _convert_to_ndarray, _ensure_known_vocab_size
         _ensure_vocab_size_unchanged, _expand_dims
         _find_repeated_tokens
         _inverse_document_frequency, _lookup_dense
         _lookup_table_from_file
         _lookup_table_from_tokens, _num_tokens
         _oov_start_index, _record_vocabulary_size
         _tensor_vocab_to_numpy, _token_start_index
         _uninitialized_lookup_table, adapt
         build_from_config, call, compute_dtype
         compute_output_shape, compute_output_spec
         finalize_state, get_build_config, get_config
         get_vocabulary, load_assets, load_own_variables
         reset_state, save_assets, save_own_variables
         set_vocabulary, update_state, variable_dtype
         vocabulary_size, __init__

    def _ensure_vocab_size_unchanged(self):
        if self.output_mode == "int" or self.pad_to_max_tokens:
            return

        with tf.init_scope():
            new_vocab_size = self.vocabulary_size()

        if (
            self._frozen_vocab_size is not None
            and new_vocab_size != self._frozen_vocab_size
        ):
            raise RuntimeError(
                f"When using `output_mode={self.output_mode}` "
                "and `pad_to_max_tokens=False`, "
                "the vocabulary size cannot be changed after the layer is "
                f"called. Old vocab size is {self._frozen_vocab_size}, "
                f"new vocab size is {new_vocab_size}"
            )

    def _ensure_known_vocab_size(self):
        if self.output_mode == "int" or self.pad_to_max_tokens:
            return
        if self._frozen_vocab_size is None:
            raise RuntimeError(
                f"When using `output_mode={self.output_mode}` "
                "and `pad_to_max_tokens=False`, "
                "you must set the layer's vocabulary before calling it. Either "
                "pass a `vocabulary` argument to the layer, or call `adapt` "
                "with some sample data."
            )

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,
    # ... truncated

    def update_state(self, y_true, y_pred, sample_weight=None):
        """Accumulates the confusion matrix statistics.

        Args:
            y_true: The ground truth values.
            y_pred: The predicted values.
            sample_weight: Optional weighting of each example. Can
                be a `Tensor` whose rank is either 0, or the same as `y_true`,
                and must be broadcastable to `y_true`. Defaults to `1`.

        Returns:
            Update op.
    # ... truncated

    def ensure_value_to_cell(value):
        """Ensures that a value is converted to a python cell object.

        Args:
            value: Any value that needs to be casted to the cell type

        Returns:
            A value wrapped as a cell object (see function "func_load")
        """

        def dummy_fn():
            value  # just access it so it gets captured in .__closure__

        cell_value = dummy_fn.__closure__[0]
        if not isinstance(value, type(cell_value)):
            return cell_value
        return value

def unique(
    x,
    sorted=True,
    return_inverse=False,
    return_counts=False,
    axis=None,
    size=None,
    fill_value=None,
):
    # Note: np.unique always sorts the output in versions < 2.3.0.
    # We accept the 'sorted' argument for API consistency across backends
    # but do not pass it to np.unique to avoid TypeError in older versions.
    # ... truncated

def build():
    root_path = os.path.dirname(os.path.abspath(__file__))
    code_api_dir = os.path.join(root_path, PACKAGE, "api")
    # Create temp build dir
    build_dir = copy_source_to_build_directory(root_path)
    build_api_dir = os.path.join(build_dir, PACKAGE)
    build_src_dir = os.path.join(build_api_dir, "src")
    build_api_init_fname = os.path.join(build_api_dir, "__init__.py")
    try:
        os.chdir(build_dir)
        open(build_api_init_fname, "w").close()
        namex.generate_api_files(
            "keras",
            code_directory="src",
            exclude_directories=[
                os.path.join("src", "backend", "jax"),
                os.path.join("src", "backend", "openvino"),
                os.path.join("src", "backend", "tensorflow"),
                os.path.join("src", "backend", "torch"),
            ],
        )
        # Add __version__ to `api/`.
        export_version_string(build_api_init_fname)
        # Creates `_tf_keras` with full keras API
        create_legacy_directory(package_dir=os.path.join(build_dir, PACKAGE))
        # Copy back the keras/api and keras/__init__.py from build directory
        if os.path.exists(build_src_dir):
            shutil.rmtree(build_src_dir)
        if os.path.exists(code_api_dir):
            shutil.rmtree(code_api_dir)
        shutil.copytree(
            build_api_dir, code_api_dir, ignore=shutil.ignore_patterns("src/")
        )
    finally:
        # Clean up: remove the build directory (no longer needed)
        shutil.rmtree(build_dir)

def smart_resize(
    x,
    size,
    interpolation="bilinear",
    data_format="channels_last",
    **kwargs,
):
    """Resize images to a target size without aspect ratio distortion.

    Image datasets typically yield images that have each a different
    size. However, these images need to be batched before they can be
    processed by Keras layers. To be batched, images need to share the same
    # ... truncated

def compute_pooling_output_shape(
    input_shape,
    pool_size,
    strides,
    padding="valid",
    data_format="channels_last",
):
    """Computes the output shape of pooling operations.

    Args:
        input_shape: Input shape. Must be a tuple of integers.
        pool_size: Size of the pooling operation. Must be a tuple of integers.
    # ... truncated

def inject_argument_info_in_traceback(fn, object_name=None):
    """Add information about call argument values to an error message.

    Arguments:
        fn: Function to wrap. Exceptions raised by the this function will be
            re-raised with additional information added to the error message,
            displaying the values of the different arguments that the function
            was called with.
        object_name: String, display name of the class/function being called,
            e.g. `'layer "layer_name" (LayerClass)'`.

    Returns:
    # ... truncated

def serialize_keras_object(obj):
    """Retrieve the config dict by serializing the Keras object.

    `serialize_keras_object()` serializes a Keras object to a python dictionary
    that represents the object, and is a reciprocal function of
    `deserialize_keras_object()`. See `deserialize_keras_object()` for more
    information about the config format.

    Args:
        obj: the Keras object to serialize.

    Returns:
    # ... truncated

def named_product(*args, **kwargs):
    """Utility to generate the cartesian product of parameters values and
    generate a test case names for each combination.

    The result of this function is to be used with the
    `@parameterized.named_parameters` decorator. It is a replacement for
    `@parameterized.product` which adds explicit test case names.

    For example, this code:
    ```
    class NamedExample(parameterized.TestCase):
        @parameterized.named_parameters(
    # ... truncated

def rnn(
    step_function,
    inputs,
    initial_states,
    go_backwards=False,
    mask=None,
    constants=None,
    unroll=False,
    input_length=None,
    time_major=False,
    zero_output_for_mask=False,
    return_all_outputs=True,
    # ... truncated

def size(x):
    return jnp.size(x)
```
