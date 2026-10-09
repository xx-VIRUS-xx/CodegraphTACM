# keras-37 :: tacm

query: Fix __call__ for Bidirectional wrapper (#9248)

## selected nodes

- rank=1 layer=FILE tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=2 layer=CLASS tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=3 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py::ExampleWrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py
- rank=4 layer=CLASS tokens=446 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=5 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py::WrapperTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py
- rank=6 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py::Wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=7 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py::WrapperLayer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py
- rank=8 layer=CLASS tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py::OpenVINOKerasTensor file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/core.py
- rank=9 layer=CLASS tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_wrapper.py::TransformerMixin file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_wrapper.py
- rank=10 layer=CLASS tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_wrapper.py::BaseEstimator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_wrapper.py
- rank=11 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_activation_call_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=12 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=13 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=14 layer=FUNCTION tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py::Classifier.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py
- rank=15 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.force_zero_output_for_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=16 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.reset_states file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=17 layer=FUNCTION tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.from_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=18 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.reset_state file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=19 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.states file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=20 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py::Wrapper.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=21 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.quantize_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=22 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=23 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.build_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=24 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=25 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py::Wrapper.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=26 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=27 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=28 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py::Wrapper.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=29 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py::Wrapper.from_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=30 layer=FUNCTION tokens=159 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.compute_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=31 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::vectorize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=32 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional._verify_layer_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=33 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::wrap_densifying_unary file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=34 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::benchmark_bidirectional file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py
- rank=35 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_rewrite_constant_fold file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py
- rank=36 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::sparse_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=37 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::wrap_elementwise_binary_union file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=38 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=39 layer=FUNCTION tokens=8 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/input_layer.py::InputLayer.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/input_layer.py

## context

```text
file backend/tensorflow/sparse.py
imports: functools, tensorflow
defines: sparse_to_dense, sparse_with_values, broadcast_scalar_to_sparse_shape, sparse_subtract, sparse_union_indices_and_values, indexed_slices_union_indices_and_values, values_for_union, sparse_intersection_indices_and_values, empty_intersection, non_empty_intersection, indexed_slices_intersection_indices_and_values, empty_intersection, non_empty_intersection, values_for_intersection, densifying_unary, wrap_densifying_unary, sparse_wrapper, elementwise_unary, sparse_wrapper, elementwise_binary_union, wrap_elementwise_binary_union, sparse_wrapper, elementwise_binary_intersection, sparse_wrapper, elementwise_division, sparse_wrapper, func_for_x1_indices, func_for_union_indices, func_for_x1_indices, func_for_union_indices

class Bidirectional(Layer):  [layers/rnn/bidirectional.py:11]
methods: _verify_layer_config, build, call, compute_mask
         compute_output_shape, force_zero_output_for_mask
         from_config, get_config, reset_state
         reset_states, states, __init__

class ExampleWrapper(layers.Wrapper):  [layers/core/wrapper_test.py:6]
methods: call

class Layer(BackendLayer, Operation):  [layers/layer.py:72]
methods: _assert_input_compatibility, _awq_call, _build_at_init
         _build_by_run_for_kwargs
         _build_by_run_for_single_pos_arg
         _check_load_own_variables, _check_quantize_args
         _check_super_called, _clear_losses
         _flatten_layers, _float8_call, _get_call_context
         _get_own_losses, _get_regularization_losses
         _gptq_call, _initialize_tracker, _int4_call
         _int8_call, _lock_state, _maybe_build
         _maybe_reset_call_context, _not_implemented_error
         _obj_type, _open_name_scope
         _quantization_mode_error
         _register_call_context_args
         _resolve_and_populate_arg, _set_mask_metadata
         _track_variable, _untrack_variable, add_loss
         add_metric, add_variable, add_weight, build
         build_from_config, build_wrapper, call
         compute_dtype, compute_mask, compute_output_shape
         compute_output_spec, compute_size, count_params
         dtype, dtype_policy, dtype_policy
         get_build_config, get_config, get_weights
         input_dtype, input_spec, input_spec
         load_own_variables, losses, maybe_convert
         metrics, metrics_variables
         non_trainable_variables, non_trainable_weights
         path, quantization_mode, quantize
         quantize_wrapper, quantized_build, quantized_call
         rematerialized_activation_call_wrapper
         rematerialized_call, save_own_variables
         set_weights, stateless_call, supports_masking
         supports_masking, symbolic_call, trainable
         trainable, trainable_variables, trainable_weights
         variable_dtype, variables, weights, __call__
         __delattr__, __init__, __new__, __repr__
         __setattr__, __str__

class WrapperTest(testing.TestCase):  [layers/core/wrapper_test.py:13]
methods: test_wrapper_basics, test_wrapper_invalid_layer

class Wrapper(Layer):  [layers/core/wrapper.py:7]
methods: build, from_config, get_config, __init__

class WrapperLayer(keras.layers.Wrapper):  [saving/serialization_lib_test.py:53]
methods: call

class OpenVINOKerasTensor:  [backend/openvino/core.py:157]
methods: count_unsqueeze_before, numpy, reshape, squeeze, __abs__
         __add__, __and__, __array__, __bool__, __div__
         __eq__, __float__, __floordiv__, __ge__
         __getitem__, __gt__, __init__, __int__
         __invert__, __iter__, __le__, __len__, __lt__
         __matmul__, __mod__, __mul__, __ne__, __neg__
         __or__, __pow__, __radd__, __rand__, __rdiv__
         __repr__, __rfloordiv__, __rmatmul__, __rmod__
         __rmul__, __ror__, __round__, __rpow__, __rsub__
         __rtruediv__, __rxor__, __sub__, __truediv__
         __xor__

class TransformerMixin:  [wrappers/sklearn_wrapper.py:33]
methods: —

class BaseEstimator:  [wrappers/sklearn_wrapper.py:24]
methods: —

                def rematerialized_activation_call_wrapper(*args, **kwargs):
                    original_activation = self.activation
                    self.activation = remat.remat(original_activation)
                    try:
                        return layer_call(*args, **kwargs)
                    finally:
                        self.activation = original_activation

    def call(
        self,
        sequences,
        initial_state=None,
        mask=None,
        training=None,
    ):
        kwargs = {}
        if self.forward_layer._call_has_training_arg:
            kwargs["training"] = training
        if self.forward_layer._call_has_mask_arg:
            kwargs["mask"] = mask
    # ... truncated

    def __init__(
        self,
        layer,
        merge_mode="concat",
        weights=None,
        backward_layer=None,
        **kwargs,
    ):
        if not isinstance(layer, Layer):
            raise ValueError(
                "Please initialize `Bidirectional` layer with a "
                f"`keras.layers.Layer` instance. Received: {layer}"
    # ... truncated

    def call(self, x, training=None):
        for wrapper in self.torch_wrappers:
            x = wrapper(x, training=training)
        return self.fc(x)

        def force_zero_output_for_mask(layer):
            # Force the zero_output_for_mask to be True if returning sequences.
            if getattr(layer, "zero_output_for_mask", None) is not None:
                layer.zero_output_for_mask = layer.return_sequences

    def reset_states(self):
        # Compatibility alias.
        self.reset_state()

    def from_config(cls, config, custom_objects=None):
        # Instead of updating the input, create a copy and use that.
        config = copy.deepcopy(config)

        config["layer"] = serialization_lib.deserialize_keras_object(
            config["layer"], custom_objects=custom_objects
        )
        # Handle (optional) backward layer instantiation.
        backward_layer_config = config.pop("backward_layer", None)
        if backward_layer_config is not None:
            backward_layer = serialization_lib.deserialize_keras_object(
                backward_layer_config, custom_objects=custom_objects
            )
            config["backward_layer"] = backward_layer
        # Instantiate the wrapper, adjust it and return it.
        layer = cls(**config)
        return layer

    def reset_state(self):
        if not self.stateful:
            raise AttributeError("Layer must be stateful.")
        self.forward_layer.reset_state()
        self.backward_layer.reset_state()

    def states(self):
        if self.forward_layer.states and self.backward_layer.states:
            return tuple(self.forward_layer.states + self.backward_layer.states)
        return None

    def __init__(self, layer, **kwargs):
        if not isinstance(layer, Layer):
            raise ValueError(
                f"Layer {layer} supplied to Wrapper isn't "
                "a supported layer type. Please "
                "ensure wrapped layer is a valid Keras layer."
            )
        super().__init__(**kwargs)
        self.layer = layer

        def quantize_wrapper(mode=None, config=None, **kwargs):
            config = validate_and_resolve_config(mode, config)
            mode = config.mode
            obj._check_quantize_args(mode, obj.compute_dtype)
            obj._tracker.unlock()
            try:
                original_quantize_method(mode=mode, config=config, **kwargs)
            except Exception:
                raise
            finally:
                obj._tracker.lock()

    def build(self, sequences_shape, initial_state_shape=None):
        if not self.forward_layer.built:
            self.forward_layer.build(sequences_shape)
        if not self.backward_layer.built:
            self.backward_layer.build(sequences_shape)

        def build_wrapper(*args, **kwargs):
            with obj._open_name_scope():
                obj._path = current_path()
                original_build_method(*args, **kwargs)
            # Record build config.
            signature = inspect.signature(original_build_method)
            obj._build_shapes_dict = signature.bind(*args, **kwargs).arguments
            # Set built, post build actions, and lock state.
            obj.built = True
            obj._post_build()
            obj._lock_state()

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        # Wrap the user-provided `build` method in the `build_wrapper`
        # to add name scope support and serialization support.
        original_build_method = obj.build

        @wraps(original_build_method)
        def build_wrapper(*args, **kwargs):
            with obj._open_name_scope():
                obj._path = current_path()
                original_build_method(*args, **kwargs)
            # Record build config.
    # ... truncated

    def build(self, input_shape=None):
        if not self.layer.built:
            self.layer.build(input_shape)
            self.layer.built = True

    def rematerialized_call(self, layer_call, *args, **kwargs):
        """Enable rematerialization dynamically for layer's call method.

        Args:
            layer_call: The original `call` method of a layer.

        Returns:
            Rematerialized layer's `call` method.
        """
    # ... truncated

    def get_config(self):
        config = {"merge_mode": self.merge_mode}
        config["layer"] = serialization_lib.serialize_keras_object(
            self.forward_layer
        )
        config["backward_layer"] = serialization_lib.serialize_keras_object(
            self.backward_layer
        )
        base_config = super().get_config()
        return {**base_config, **config}

    def get_config(self):
        config = {"layer": serialization_lib.serialize_keras_object(self.layer)}
        base_config = super().get_config()
        return {**base_config, **config}

    def from_config(cls, config, custom_objects=None):
        layer = serialization_lib.deserialize_keras_object(
            config.pop("layer"),
            custom_objects=custom_objects,
        )
        return cls(layer, **config)

    def compute_mask(self, _, mask):
        if isinstance(mask, list):
            mask = mask[0]
        if self.return_sequences:
            if not self.merge_mode:
                output_mask = (mask, mask)
            else:
                output_mask = mask
        else:
            output_mask = (None, None) if not self.merge_mode else None

        if self.return_state and self.states is not None:
            state_mask = (None for _ in self.states)
            if isinstance(output_mask, list):
                return output_mask + state_mask * 2
            return (output_mask,) + state_mask * 2
        return output_mask

def vectorize(pyfunc, *, excluded=None, signature=None):
    def wrapper(*args, **kwargs):
        converted_args = tuple(convert_to_tensor(arg) for arg in args)
        return pyfunc(*converted_args, **kwargs)

    return wrapper

    def _verify_layer_config(self):
        """Ensure the forward and backward layers have valid common property."""
        if self.forward_layer.go_backwards == self.backward_layer.go_backwards:
            raise ValueError(
                "Forward layer and backward layer should have different "
                "`go_backwards` value. Received: "
                "forward_layer.go_backwards "
                f"{self.forward_layer.go_backwards}, "
                "backward_layer.go_backwards="
                f"{self.backward_layer.go_backwards}"
            )

        common_attributes = ("stateful", "return_sequences", "return_state")
        for a in common_attributes:
            forward_value = getattr(self.forward_layer, a)
            backward_value = getattr(self.backward_layer, a)
            if forward_value != backward_value:
                raise ValueError(
                    "Forward layer and backward layer are expected to have "
                    f'the same value for attribute "{a}", got '
                    f'"{forward_value}" for forward layer and '
                    f'"{backward_value}" for backward layer'
                )

    def wrap_densifying_unary(func):
        @functools.wraps(func)
        def sparse_wrapper(x, *args, **kwargs):
            if isinstance(x, tf.SparseTensor):
                sparse_output = sparse_with_values(
                    x, func(x.values, *args, **kwargs)
                )
                return sparse_to_dense(
                    sparse_output,
                    tf.cast(default_value, sparse_output.values.dtype),
                )
            elif isinstance(x, tf.IndexedSlices):
                sparse_output_values = func(x.values, *args, **kwargs)
                output = tf.fill(
                    x.dense_shape,
                    tf.cast(default_value, sparse_output_values.dtype),
                )
                return tf.tensor_scatter_nd_update(
                    output, tf.expand_dims(x.indices, 1), sparse_output_values
                )
            return func(x, *args, **kwargs)

        return sparse_wrapper

def benchmark_bidirectional(
    num_samples,
    batch_size,
    jit_compile=True,
):
    layer_name = "Bidirectional"
    init_args = {}
    keras_layer = keras.layers.Bidirectional(keras.layers.LSTM(32))
    tf_keras_layer = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32))
    benchmark = LayerBenchmark(
        layer_name,
        init_args,
        input_shape=[256, 256],
        jit_compile=jit_compile,
        keras_layer=keras_layer,
        tf_keras_layer=tf_keras_layer,
    )

    benchmark.benchmark_predict(
        num_samples=num_samples,
        batch_size=batch_size,
    )

    benchmark.benchmark_train(
        num_samples=num_samples,
        batch_size=batch_size,
    )

    def patched_rewrite_constant_fold(g, ops):
        """
        We call tensorflow transform with constant folding but in some cases
        tensorflow does fold all constants. Since there are a bunch of ops in
        onnx that use attributes where tensorflow has dynamic inputs, we badly
        want constant folding to work. For cases where tensorflow missed
        something, make another pass over the graph and fix want we care about.
        """
    # ... truncated

    def sparse_wrapper(x1, x2):
        if isinstance(x1, tf.SparseTensor):
            if isinstance(x2, tf.SparseTensor):
                # x1 is a SparseTensor and x2 is a SparseTensor.
                # Divisor is sparse, meaning we're doing divisions by zero
                # outside of x2.indices, so the result is dense. Densify both.
                x1 = sparse_to_dense(x1)
                x2 = sparse_to_dense(x2)
            else:
                # x1 is a SparseTensor.
                if not hasattr(x2, "shape") or len(x2.shape) == 0:
                    # x2 is a scalar, apply func element-wise.
    # ... truncated

    def wrap_elementwise_binary_union(func):
        @functools.wraps(func)
        def sparse_wrapper(x1, x2):
            if isinstance(x1, tf.SparseTensor):
                if isinstance(x2, tf.SparseTensor):
                    # x1 is a SparseTensor and x2 is a SparseTensor.
                    if x1.indices is x2.indices:
                        return sparse_with_values(
                            x1, func(x1.values, x2.values)
                        )
                    else:
                        output = sparse_op(x1, x2)
    # ... truncated

    def __call__(self, *args, **kwargs):
        self._check_super_called()
        self._called = True

        original_args = args
        original_kwargs = kwargs

        #############################################################
        # 1. Convert any array arguments to tensors of correct dtype.
        def maybe_convert(x):
            # Prevent _keras_mask from disappearing
            mask = backend.get_keras_mask(x)
    # ... truncated

    def call(self):
        return
```
