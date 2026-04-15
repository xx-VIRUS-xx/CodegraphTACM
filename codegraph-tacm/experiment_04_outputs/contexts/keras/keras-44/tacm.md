# keras-44 :: tacm

query: Fix RNN layers dynamic `trainable` attr

## selected nodes

- rank=1 layer=FILE tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py
- rank=2 layer=FILE tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=3 layer=FILE tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py
- rank=4 layer=FILE tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=5 layer=FILE tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=6 layer=FILE tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/__init__.py
- rank=7 layer=FILE tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py
- rank=8 layer=FILE tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=9 layer=FILE tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=10 layer=FILE tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=11 layer=FILE tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm2d.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm2d.py
- rank=12 layer=CLASS tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py::SimpleRNNCell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py
- rank=13 layer=CLASS tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm2d.py::ConvLSTM2D file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm2d.py
- rank=14 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py::StackedRNNCells file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/stacked_rnn_cells.py
- rank=15 layer=CLASS tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=16 layer=CLASS tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py::SimpleRNN file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/simple_rnn.py
- rank=17 layer=CLASS tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py::DropoutRNNCell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell.py
- rank=18 layer=CLASS tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py::GRUCell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py
- rank=19 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn_test.py::TwoStatesRNNCell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn_test.py
- rank=20 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn_test.py::OneStateRNNCell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn_test.py
- rank=21 layer=CLASS tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTM file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=22 layer=CLASS tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py::GRU file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/gru.py
- rank=23 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py::RNNCellWithDropout file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py
- rank=24 layer=CLASS tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py::ConvLSTMCell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/conv_lstm.py
- rank=25 layer=CLASS tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py::LSTMCell file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/lstm.py
- rank=26 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py::DropoutRNNCellTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/dropout_rnn_cell_test.py
- rank=27 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/time_distributed_test.py::TimeDistributedTest.MaskedDense file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/time_distributed_test.py
- rank=28 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::set_tensor_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py
- rank=29 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::get_tensor_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py
- rank=30 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py::_clear_tensor_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/tensor_attributes.py
- rank=31 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN._create_state_variables file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=32 layer=FUNCTION tokens=278 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py::_walk_saveable file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib.py
- rank=33 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=34 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer._stateful_handle_finite_grads file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py
- rank=35 layer=FUNCTION tokens=341 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::Tracker.track file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py
- rank=36 layer=FUNCTION tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=37 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=38 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._not_implemented_error file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=39 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.reset_states file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=40 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.layer_property file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=41 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/global_state.py::get_global_attribute file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/global_state.py
- rank=42 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._initialize_tracker file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=43 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::rnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=44 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.reset_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=45 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=46 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer._stateless_handle_non_finite_grads file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py
- rank=47 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_rewrite_constant_fold file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py
- rank=48 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_get_value_attr file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py
- rank=49 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/layer.py::TFLayer._convert_tracked_collections file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/layer.py
- rank=50 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.from_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=51 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py::SubclassFunctional.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/saving_lib_test.py
- rank=52 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py::RNN.compute_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/rnn.py
- rank=53 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=54 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py::LossScaleOptimizer.upscale file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/optimizers/loss_scale_optimizer.py

## context

```text
file backend/common/tensor_attributes.py
imports: weakref, keras
defines: _clear_tensor_attr, set_tensor_attr, get_tensor_attr

file layers/rnn/rnn.py
imports: keras
defines: RNN

file layers/rnn/simple_rnn.py
imports: keras
defines: SimpleRNNCell, SimpleRNN

file layers/rnn/stacked_rnn_cells.py
imports: keras
defines: StackedRNNCells

file layers/rnn/dropout_rnn_cell.py
imports: keras
defines: DropoutRNNCell

file layers/rnn/__init__.py
imports: —
defines: —

file layers/rnn/gru.py
imports: keras
defines: GRUCell, GRU

file layers/rnn/lstm.py
imports: keras
defines: LSTMCell, LSTM

file layers/rnn/bidirectional.py
imports: copy, keras
defines: Bidirectional

file layers/rnn/conv_lstm.py
imports: keras
defines: ConvLSTMCell, ConvLSTM

file layers/rnn/conv_lstm2d.py
imports: keras
defines: ConvLSTM2D

class SimpleRNNCell(Layer, DropoutRNNCell):  [layers/rnn/simple_rnn.py:15]
methods: build, call, get_config, get_initial_state, __init__

class ConvLSTM2D(ConvLSTM):  [layers/rnn/conv_lstm2d.py:6]
methods: __init__

class StackedRNNCells(Layer):  [layers/rnn/stacked_rnn_cells.py:9]
methods: build, call, from_config, get_config, get_initial_state
         output_size, state_size, __init__

class RNN(Layer):  [layers/rnn/rnn.py:13]
methods: _create_state_variables, _maybe_config_dropout_masks
         _maybe_reset_dropout_masks, build, call
         compute_mask, compute_output_shape, from_config
         get_config, get_initial_state, inner_loop
         reset_state, reset_states, step, __init__

class SimpleRNN(RNN):  [layers/rnn/simple_rnn.py:212]
methods: activation, bias_constraint, bias_initializer
         bias_regularizer, call, dropout, from_config
         get_config, kernel_constraint, kernel_initializer
         kernel_regularizer, recurrent_constraint
         recurrent_dropout, recurrent_initializer
         recurrent_regularizer, units, use_bias, __init__

class DropoutRNNCell:  [layers/rnn/dropout_rnn_cell.py:5]
methods: _create_dropout_mask, get_dropout_mask
         get_recurrent_dropout_mask, reset_dropout_mask
         reset_recurrent_dropout_mask

class GRUCell(Layer, DropoutRNNCell):  [layers/rnn/gru.py:16]
methods: build, call, get_config, get_initial_state, __init__

class TwoStatesRNNCell(layers.Layer):  [layers/rnn/rnn_test.py:33]
methods: build, call, __init__

class OneStateRNNCell(layers.Layer):  [layers/rnn/rnn_test.py:8]
methods: build, call, __init__

class LSTM(RNN):  [layers/rnn/lstm.py:332]
methods: activation, bias_constraint, bias_initializer
         bias_regularizer, call, dropout, from_config
         get_config, inner_loop, kernel_constraint
         kernel_initializer, kernel_regularizer
         recurrent_activation, recurrent_constraint
         recurrent_dropout, recurrent_initializer
         recurrent_regularizer, unit_forget_bias, units
         use_bias, __init__

class GRU(RNN):  [layers/rnn/gru.py:342]
methods: activation, bias_constraint, bias_initializer
         bias_regularizer, call, dropout, from_config
         get_config, inner_loop, kernel_constraint
         kernel_initializer, kernel_regularizer
         recurrent_activation, recurrent_constraint
         recurrent_dropout, recurrent_initializer
         recurrent_regularizer, reset_after, units
         use_bias, __init__

class RNNCellWithDropout(layers.Layer, DropoutRNNCell):  [layers/rnn/dropout_rnn_cell_test.py:8]
methods: build, call, __init__

class ConvLSTMCell(Layer, DropoutRNNCell):  [layers/rnn/conv_lstm.py:16]
methods: bias_initializer, build, call, compute_output_shape
         get_config, get_initial_state, input_conv
         recurrent_conv, __init__

class LSTMCell(Layer, DropoutRNNCell):  [layers/rnn/lstm.py:16]
methods: _compute_carry_and_output, _compute_carry_and_output_fused
         bias_initializer, build, call, get_config
         get_initial_state, __init__

class DropoutRNNCellTest(testing.TestCase):  [layers/rnn/dropout_rnn_cell_test.py:45]
methods: test_basics, test_seed_tracking

class MaskedDense(layers.Wrapper):  [layers/rnn/time_distributed_test.py:53]
methods: —

def set_tensor_attr(tensor, attr, value):
    try:
        setattr(tensor, attr, value)
    except AttributeError:
        attr_dict = global_state.get_global_attribute(f"{attr}_dict")
        if attr_dict is None:
            if value is None:
                return
            attr_dict = {}
            global_state.set_global_attribute(f"{attr}_dict", attr_dict)
        if value is not None:
            attr_dict[id(tensor)] = value
            weakref.finalize(tensor, _clear_tensor_attr, id(tensor), attr)
        elif id(tensor) in attr_dict:
            del attr_dict[id(tensor)]

def get_tensor_attr(tensor, attr):
    if not hasattr(tensor, attr):
        attr_dict = global_state.get_global_attribute(f"{attr}_dict")
        if attr_dict is not None:
            return attr_dict.get(id(tensor), None)
        else:
            return None
    return getattr(tensor, attr, None)

def _clear_tensor_attr(tensor_id, attr):
    attr_dict = global_state.get_global_attribute(f"{attr}_dict")
    if attr_dict is not None and tensor_id in attr_dict:
        del attr_dict[tensor_id]

    def _create_state_variables(self, batch_size):
        with backend.name_scope(self.name, caller=self):
            self.states = tree.map_structure(
                lambda value: backend.Variable(
                    value,
                    trainable=False,
                    dtype=self.variable_dtype,
                    name="rnn_state",
                ),
                self.get_initial_state(batch_size),
            )

def _walk_saveable(saveable):
    from keras.src.saving.keras_saveable import KerasSaveable

    if not isinstance(saveable, KerasSaveable):
        raise ValueError(
            "Expected object to be an "
            "instance of `KerasSaveable`, but "
            f"got {saveable} of type {type(saveable)}"
        )

    obj_type = saveable._obj_type()
    attr_skipset = get_attr_skipset(obj_type)

    # Save all layers directly tracked by Sequential and Functional first.
    # This helps avoid ordering concerns for subclassed Sequential or Functional
    # models with extra attributes--the internal Keras state take precedence.
    if obj_type in ("Sequential", "Functional"):
        yield "layers", saveable.layers

    for child_attr in sorted(dir(saveable), key=lambda x: _name_key(x)):
        if child_attr.startswith("__") or child_attr in attr_skipset:
            continue
        try:
            child_obj = getattr(saveable, child_attr)
        except Exception:
            # Avoid raising the exception when visiting the attributes.
            continue
        yield child_attr, child_obj

    def call(
        self,
        sequences,
        initial_state=None,
        mask=None,
        training=False,
    ):
        timesteps = sequences.shape[1]
        if self.unroll and timesteps is None:
            raise ValueError(
                "Cannot unroll a RNN if the "
                "time dimension is undefined. \n"
    # ... truncated

    def _stateful_handle_finite_grads(self, grads, trainable_variables):
        scale = self.dynamic_scale
        # Unscale gradients.
        tvs = trainable_variables or self._trainable_variables
        unscaled_grads = [
            g
            if g is None or self._overwrite_variable_with_gradient(v)
            else ops.divide(g, scale)
            for g, v in zip(grads, tvs)
        ]
        self.inner_optimizer.apply(
            unscaled_grads, trainable_variables=trainable_variables
        )

        def upscale():
            self.step_counter.assign(0)
            self.dynamic_scale.assign(ops.multiply(self.dynamic_scale, 2.0))

        def increment():
            self.step_counter.assign_add(1)

        # Potentially upscale loss and reset counter.
        ops.cond(
            ops.equal(self.step_counter, self.dynamic_growth_steps - 1),
            upscale,
            increment,
        )

    def track(self, attr):
        if not is_tracking_enabled():
            return attr

        for store_name, (is_attr_type, _) in self.config.items():
            if is_attr_type(attr):
                if store_name in self.exclusions:
                    for excl in self.exclusions[store_name]:
                        if self.is_in_store(excl, attr):
                            return attr
                if not self.is_in_store(store_name, attr):
                    self.add_to_store(store_name, attr)
                return attr
        if isinstance(attr, tuple) and hasattr(attr, "_fields"):
            # Named tuple case.
            wrapped_attr = {}
            for name, e in attr._asdict().items():
                wrapped_attr[name] = self.track(e)
            return attr.__class__(**wrapped_attr)
        if isinstance(attr, tuple):
            wrapped_attr = []
            for e in attr:
                wrapped_attr.append(self.track(e))
            return attr.__class__(wrapped_attr)
        elif isinstance(attr, list):
            return TrackedList(attr, self)
        elif isinstance(attr, OrderedDict):
            return TrackedOrderedDict(attr, self)
        elif isinstance(attr, dict):
            return TrackedDict(attr, self)
        elif isinstance(attr, set):
            return TrackedSet(attr, self)
        return attr

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

    def __init__(self, layers=None, trainable=True, name=None):
        super().__init__(trainable=trainable, name=name)
        self._functional = None
        self._layers = []
        if layers:
            for layer in layers:
                self.add(layer, rebuild=False)
            self._maybe_rebuild()

    def _not_implemented_error(self, attr, msg=None):
        if callable(attr):
            attr_name = attr.__name__
            attr_type = "method"
        else:
            attr_name = str(attr)
            attr_type = "attribute"
        msg = f" {msg}" if msg is not None else ""
        return NotImplementedError(
            f"Layer {self.__class__.__name__} does not have a `{attr_name}` "
            f"{attr_type} implemented.{msg}"
        )

    def reset_states(self):
        # Compatibility alias.
        self.reset_state()

    def layer_property(self):
        # Properties for layers in the functional graph should not affect saving
        return self.layer_attr

def get_global_attribute(name, default=None, set_to_default=False):
    attr = getattr(GLOBAL_STATE_TRACKER, name, None)
    if attr is None and default is not None:
        attr = default
        if set_to_default:
            set_global_attribute(name, attr)
    return attr

    def _initialize_tracker(self):
        if hasattr(self, "_tracker"):
            return

        trainable_variables = []
        non_trainable_variables = []
        layers = []
        metrics = []
        seed_generators = []
        self._tracker = tracking.Tracker(
            {
                "trainable_variables": (
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

    def reset_state(self):
        if self.states is not None:
            for v in self.states:
                v.assign(ops.zeros_like(v.value))

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

    def _stateless_handle_non_finite_grads(
        self, optimizer_variables, trainable_variables
    ):
        mapping = list(zip(self.variables, optimizer_variables))
        with backend.StatelessScope(state_mapping=mapping) as scope:
            self.step_counter.assign(0)
            self.dynamic_scale.assign(ops.multiply(self.dynamic_scale, 0.5))
        new_optimizer_variables = []
        for v in self.variables:
            new_optimizer_variables.append(scope.get_current_value(v))
        return trainable_variables, new_optimizer_variables

    def patched_rewrite_constant_fold(g, ops):
        """
        We call tensorflow transform with constant folding but in some cases
        tensorflow does fold all constants. Since there are a bunch of ops in
        onnx that use attributes where tensorflow has dynamic inputs, we badly
        want constant folding to work. For cases where tensorflow missed
        something, make another pass over the graph and fix want we care about.
        """
    # ... truncated

    def patched_get_value_attr(self, external_tensor_storage=None):
        """
        Return onnx attr for value property of node.
        Attr is modified to point to external tensor data stored in
        external_tensor_storage, if included.
        """
    # ... truncated

    def _convert_tracked_collections(self, children):
        """Convert TrackedList/Dict/Set to plain Python structures."""
        for tracked_attr in self._tracked:
            tracked_item = getattr(self, tracked_attr)
            if isinstance(tracked_item, tracking.TrackedList):
                children[tracked_attr] = list(tracked_item)
            elif isinstance(tracked_item, tracking.TrackedOrderedDict):
                children[tracked_attr] = collections.OrderedDict(tracked_item)
            elif isinstance(tracked_item, tracking.TrackedDict):
                children[tracked_attr] = dict(tracked_item)
            elif isinstance(tracked_item, tracking.TrackedSet):
                children[tracked_attr] = list(tracked_item)

    def from_config(cls, config, custom_objects=None):
        cell = serialization_lib.deserialize_keras_object(
            config.pop("cell"), custom_objects=custom_objects
        )
        layer = cls(cell, **config)
        return layer

    def __init__(self, **kwargs):
        inputs = keras.Input(shape=(4,), batch_size=2)
        dense = keras.layers.Dense(1, name="first_dense")
        x = dense(inputs)
        outputs = keras.layers.Dense(1, name="second_dense")(x)
        super().__init__(inputs=inputs, outputs=outputs, **kwargs)
        # Attrs for layers in the functional graph should not affect saving
        self.layer_attr = dense

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

    def output(self):
        return self._outputs_struct

        def upscale():
            self.step_counter.assign(0)
            self.dynamic_scale.assign(ops.multiply(self.dynamic_scale, 2.0))
```
