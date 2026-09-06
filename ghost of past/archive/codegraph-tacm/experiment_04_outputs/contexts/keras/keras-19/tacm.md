# keras-19 :: tacm

query: Update the RNN cell API to be explicit about output_size. (#11021)

## selected nodes

- rank=1 layer=FILE tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=2 layer=FILE tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py
- rank=3 layer=FILE tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/nasnet.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/nasnet.py
- rank=4 layer=CLASS tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=5 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py::RNNCellWithDropout file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py
- rank=6 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py::DropoutRNNCellTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py
- rank=7 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=8 layer=CLASS tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells_test.py::StackedRNNTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells_test.py
- rank=9 layer=CLASS tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/tree_api.py::MAP_TO_NONE file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/tree_api.py
- rank=10 layer=CLASS tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=11 layer=CLASS tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SavingAPITest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=12 layer=CLASS tokens=189 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn_test.py::NNOpsBehaviorTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn_test.py
- rank=13 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py::Variable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py
- rank=14 layer=CLASS tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_api_test.py::LoadModelTests.CustomLayer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_api_test.py
- rank=15 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/api_export.py::keras_export file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/api_export.py
- rank=16 layer=CLASS tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn_test.py::NNOpsDynamicShapeTest.Model file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn_test.py
- rank=17 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=18 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell.reset_dropout_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=19 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=20 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.get_initial_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=21 layer=FUNCTION tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=22 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/nasnet.py::_adjust_block file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/nasnet.py
- rank=23 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=24 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._ensure_vocab_size_unchanged file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=25 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.get_initial_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=26 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/nasnet.py::_reduction_a_cell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/nasnet.py
- rank=27 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=28 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/nasnet.py::_normal_a_cell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/applications/nasnet.py
- rank=29 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=30 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_output_shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=31 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=32 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py::IndexLookup._ensure_known_vocab_size file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/preprocessing/index_lookup.py
- rank=33 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=34 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=35 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN._maybe_reset_dropout_masks file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=36 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.from_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=37 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN._maybe_config_dropout_masks file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=38 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py::rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/backend.py
- rank=39 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=40 layer=FUNCTION tokens=8 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py::shape file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/core.py

## context

```text
file layers/rnn/dropout_rnn_cell.py
imports: keras
defines: DropoutRNNCell

file backend/numpy/core.py
imports: builtins, contextlib, functools, warnings, numpy, keras
defines: Variable, custom_gradient, convert_to_tensor, convert_to_numpy, is_tensor, shape, cast, cond, vectorized_map, has_none_shape, convert_keras_tensor_to_numpy, convert_numpy_to_keras_tensor, map, g, scan, pack_input, pack_output, associative_scan, _combine, _interleave, _scan, scatter, scatter_update, slice, slice_update, switch, while_loop, fori_loop, stop_gradient, unstack, random_seed_dtype, device_scope, remat

file applications/nasnet.py
imports: warnings, keras
defines: NASNet, NASNetMobile, NASNetLarge, _separable_conv_block, _adjust_block, _normal_a_cell, _reduction_a_cell, preprocess_input, decode_predictions

class DropoutRNNCell:  [layers/rnn/dropout_rnn_cell.py:5]
methods: _create_dropout_mask, get_dropout_mask
         get_recurrent_dropout_mask, reset_dropout_mask
         reset_recurrent_dropout_mask

class RNNCellWithDropout(layers.Layer, DropoutRNNCell):  [layers/rnn/dropout_rnn_cell_test.py:8]
methods: build, call, __init__

class DropoutRNNCellTest(testing.TestCase):  [layers/rnn/dropout_rnn_cell_test.py:45]
methods: test_basics, test_seed_tracking

class StackedRNNCells(Layer):  [layers/rnn/stacked_rnn_cells.py:9]
methods: build, call, from_config, get_config, get_initial_state
         output_size, state_size, __init__

class StackedRNNTest(testing.TestCase):  [layers/rnn/stacked_rnn_cells_test.py:9]
methods: test_basics, test_correctness_single_state_stack
         test_correctness_two_states_stack
         test_return_state_stacked_lstm_cell
         test_stacked_lstm_cell_mask
         test_statefullness_single_state_stack
         test_statefullness_two_states_stack

class MAP_TO_NONE:  [tree/tree_api.py:28]
methods: —

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

class SavingAPITest(testing.TestCase):  [saving/saving_lib_test.py:810]
methods: test_model_api_endpoint, test_model_api_endpoint_h5
         test_model_api_errors, test_normalization_kpl
         test_safe_mode, test_saving_api_errors

class NNOpsBehaviorTest(testing.TestCase):  [ops/nn_test.py:3212]
methods: test_check_shape_first_dim_mismatch, test_depth_to_space
         test_depth_to_space_block_size_validation
         test_depth_to_space_space_to_depth_roundtrip
         test_fold, test_fold_batch_and_channels
         test_fold_divisibility_validation
         test_fold_no_padding, test_fold_non_square_output
         test_fold_tuple_params
         test_invalid_strategy_ctc_decode
         test_layer_normalization_rms_scaling_warning
         test_logit_recovery_binary_crossentropy
         test_normalize_order_validation
         test_softmax_on_axis_with_size_one_warns
         test_space_to_depth
         test_space_to_depth_block_size_validation
         test_unfold

class Variable(KerasVariable):  [backend/numpy/core.py:22]
methods: _convert_to_tensor, _direct_assign, _initialize, __array__

class CustomLayer(layers.Layer):  [saving/saving_api_test.py:170]
methods: —

class keras_export:  [api_export.py:43]
methods: __call__, __call__, __init__, __init__

class Model(keras.Model):  [ops/nn_test.py:194]
methods: —

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

def _adjust_block(p, ip, filters, block_id=None):
    """Adjusts the input `previous path` to match the shape of the `input`.

    Used in situations where the output number of filters needs to be changed.

    Args:
        p: Input tensor which needs to be modified
        ip: Input tensor whose shape needs to be matched
        filters: Number of output filters to be matched
        block_id: String block_id

    Returns:
    # ... truncated

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

def _reduction_a_cell(ip, p, filters, block_id=None):
    """Adds a Reduction cell for NASNet-A (Fig. 4 in the paper).

    Args:
      ip: Input tensor `x`
      p: Input tensor `p`
      filters: Number of output filters
      block_id: String block_id

    Returns:
      A Keras tensor
    """
    # ... truncated

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

def _normal_a_cell(ip, p, filters, block_id=None):
    """Adds a Normal cell for NASNet-A (Fig. 4 in the paper).

    Args:
        ip: Input tensor `x`
        p: Input tensor `p`
        filters: Number of output filters
        block_id: String block_id

    Returns:
        A Keras tensor
    """
    # ... truncated

    def __init__(
        self,
        cell,
        return_sequences=False,
        return_state=False,
        go_backwards=False,
        stateful=False,
        unroll=False,
        zero_output_for_mask=False,
        **kwargs,
    ):
        if isinstance(cell, (list, tuple)):
    # ... truncated

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

    def output(self):
        return self._outputs_struct

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

    def call(self, inputs, states, training=False, **kwargs):
        # Call the cells in order and store the returned states.
        new_states = []
        for cell, states in zip(self.cells, states):
            state_is_list = tree.is_nested(states)
            states = list(states) if tree.is_nested(states) else [states]
            if isinstance(cell, Layer) and cell._call_has_training_arg:
                kwargs["training"] = training
            else:
                kwargs.pop("training", None)
            cell_call_fn = cell.__call__ if callable(cell) else cell.call
            inputs, states = cell_call_fn(inputs, states, **kwargs)
            if len(states) == 1 and not state_is_list:
                states = states[0]
            new_states.append(states)

        if len(new_states) == 1:
            new_states = new_states[0]
        return inputs, new_states

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

    def _maybe_reset_dropout_masks(self, cell):
        if isinstance(cell, DropoutRNNCell):
            cell.reset_dropout_mask()
            cell.reset_recurrent_dropout_mask()
        if isinstance(cell, StackedRNNCells):
            for c in cell.cells:
                self._maybe_reset_dropout_masks(c)

    def from_config(cls, config, custom_objects=None):
        cell = serialization_lib.deserialize_keras_object(
            config.pop("cell"), custom_objects=custom_objects
        )
        layer = cls(cell, **config)
        return layer

    def _maybe_config_dropout_masks(self, cell, input_sequence, input_state):
        state = (
            input_state[0]
            if isinstance(input_state, (list, tuple))
            else input_state
        )
        if isinstance(cell, DropoutRNNCell):
            cell.get_dropout_mask(input_sequence)
            cell.get_recurrent_dropout_mask(state)
        if isinstance(cell, StackedRNNCells):
            for c, s in zip(cell.cells, input_state):
                self._maybe_config_dropout_masks(c, input_sequence, s)
                # Replicate the behavior of `StackedRNNCells.call` to compute
                # the inputs for the next cell.
                s = list(s) if tree.is_nested(s) else [s]
                cell_call_fn = c.__call__ if callable(c) else c.call
                input_sequence, _ = cell_call_fn(input_sequence, s)

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

    def get_config(self):
        config = {
            "return_sequences": self.return_sequences,
            "return_state": self.return_state,
            "go_backwards": self.go_backwards,
            "stateful": self.stateful,
            "unroll": self.unroll,
            "zero_output_for_mask": self.zero_output_for_mask,
        }
        config["cell"] = serialization_lib.serialize_keras_object(self.cell)
        base_config = super().get_config()
        return {**base_config, **config}

def shape(x):
    return x.shape
```
