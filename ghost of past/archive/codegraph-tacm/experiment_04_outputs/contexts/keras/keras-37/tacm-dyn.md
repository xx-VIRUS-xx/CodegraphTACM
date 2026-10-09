# keras-37 :: tacm-dyn

query: Fix __call__ for Bidirectional wrapper (#9248)

## selected nodes

- rank=1 layer=FILE tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=2 layer=CLASS tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=3 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=4 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=5 layer=FUNCTION tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py::Classifier.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py
- rank=6 layer=FILE tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/sparse.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/sparse.py
- rank=7 layer=FILE tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=8 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_activation_call_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=9 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/sparse.py::wrap_elementwise_unary file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/sparse.py
- rank=10 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.force_zero_output_for_mask file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=11 layer=FUNCTION tokens=223 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/sparse.py::densifying_unary file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/sparse.py
- rank=12 layer=FILE tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=13 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py::Wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=14 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py::Wrapper.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=15 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::vectorize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=16 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py::Wrapper.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=17 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::wrap_densifying_unary file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=18 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::benchmark_bidirectional file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py
- rank=19 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_rewrite_constant_fold file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py
- rank=20 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::sparse_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=21 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py::ExampleWrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py
- rank=22 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=23 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer.wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=24 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=25 layer=CLASS tokens=446 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=26 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.quantize_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=27 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.build_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=28 layer=FUNCTION tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=29 layer=FUNCTION tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::no_automatic_dependency_tracking file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py
- rank=30 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py::WrapperTest file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py
- rank=31 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.reset_states file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=32 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py::slice_tensorflow_sparse_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py
- rank=33 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer.wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py
- rank=34 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer._autoconvert_optionals file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py
- rank=35 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/gptq_core.py::stream_hessians file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/quantizers/gptq_core.py
- rank=36 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py::custom_gradient file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py
- rank=37 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py::Wrapper.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper.py
- rank=38 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py
- rank=39 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py::ExampleWrapper.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/wrapper_test.py
- rank=40 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py::WrapperLayer file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py
- rank=41 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py::WrapperLayer.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py
- rank=42 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py::wrap_elementwise_binary_union file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/sparse.py
- rank=43 layer=FUNCTION tokens=6 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::copy file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py

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

file backend/jax/sparse.py
imports: functools, jax, keras, as
defines: axis_shape_dims_for_broadcast_in_dim, bcoo_add_indices, densifying_unary, sparse_wrapper, elementwise_unary, wrap_elementwise_unary, sparse_wrapper, elementwise_binary_union, wrap_elementwise_binary_union, sparse_wrapper, elementwise_division, sparse_wrapper

file layers/rnn/bidirectional.py
imports: copy, keras
defines: Bidirectional

                def rematerialized_activation_call_wrapper(*args, **kwargs):
                    original_activation = self.activation
                    self.activation = remat.remat(original_activation)
                    try:
                        return layer_call(*args, **kwargs)
                    finally:
                        self.activation = original_activation

    def wrap_elementwise_unary(func):
        @functools.wraps(func)
        def sparse_wrapper(x, *args, **kwargs):
            if isinstance(x, jax_sparse.BCOO):
                if not linear and not x.unique_indices:
                    x = jax_sparse.bcoo_sum_duplicates(x)
                return jax_sparse.BCOO(
                    (func(x.data, *args, **kwargs), x.indices), shape=x.shape
                )
            else:
                return func(x, *args, **kwargs)

        return sparse_wrapper

        def force_zero_output_for_mask(layer):
            # Force the zero_output_for_mask to be True if returning sequences.
            if getattr(layer, "zero_output_for_mask", None) is not None:
                layer.zero_output_for_mask = layer.return_sequences

def densifying_unary(func):
    """Decorator to add support for `JAXSparse` tensors (including `BCOO`) to a
    non-zero-preserving element-wise unary operator.

    There are requirements on the operator for this decorator to work correctly:

    - The operator must be element-wise
    - The operator must be unary (one input tensor and one output tensor)
    - The operator must return a tensor of the same shape.

    Additional arguments to the function (besides the input tensor) are
    supported. The returned result is a dense tensor.

    Args:
        func: The unary operator to wrap.
    Returns:
        Wrapped function that supports `JAXSparse` tensors.
    """

    @functools.wraps(func)
    def sparse_wrapper(x, *args, **kwargs):
        if isinstance(x, jax_sparse.JAXSparse):
            x = x.todense()
        return func(x, *args, **kwargs)

    return sparse_wrapper

file layers/core/wrapper.py
imports: keras
defines: Wrapper

class Wrapper(Layer):  [layers/core/wrapper.py:7]
methods: build, from_config, get_config, __init__

    def __init__(self, layer, **kwargs):
        if not isinstance(layer, Layer):
            raise ValueError(
                f"Layer {layer} supplied to Wrapper isn't "
                "a supported layer type. Please "
                "ensure wrapped layer is a valid Keras layer."
            )
        super().__init__(**kwargs)
        self.layer = layer

def vectorize(pyfunc, *, excluded=None, signature=None):
    def wrapper(*args, **kwargs):
        converted_args = tuple(convert_to_tensor(arg) for arg in args)
        return pyfunc(*converted_args, **kwargs)

    return wrapper

    def build(self, input_shape=None):
        if not self.layer.built:
            self.layer.build(input_shape)
            self.layer.built = True

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

class ExampleWrapper(layers.Wrapper):  [layers/core/wrapper_test.py:6]
methods: call

    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

        def wrapper(*args):
            args = args[0:index] + (value,) + args[index:]
            return fn(*args)

    def output(self):
        return self._outputs_struct

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

    def wrapper(*args, **kwargs):
        converted_args = tuple(convert_to_tensor(arg) for arg in args)
        return pyfunc(*converted_args, **kwargs)

def no_automatic_dependency_tracking(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        with DotNotTrackScope():
            return fn(*args, **kwargs)

    return wrapper

class WrapperTest(testing.TestCase):  [layers/core/wrapper_test.py:13]
methods: test_wrapper_basics, test_wrapper_invalid_layer

    def reset_states(self):
        # Compatibility alias.
        self.reset_state()

def slice_tensorflow_sparse_wrapper(sparse_wrapper, indices):
    from keras.src.utils.module_utils import tensorflow as tf

    if isinstance(indices, slice):
        sparse_indices = sparse_wrapper.ragged_indices[indices]
        sparse_values = sparse_wrapper.ragged_values[indices]
        batch_dim = indices.stop - indices.start
    else:
        sparse_indices = tf.gather(sparse_wrapper.ragged_indices, indices)
        sparse_values = tf.gather(sparse_wrapper.ragged_values, indices)
        if isinstance(indices, list):
            batch_dim = len(indices)
        else:
            batch_dim = indices.shape[0]
            if batch_dim is None:
                batch_dim = tf.shape(indices)[0]

    row_ids = sparse_indices.value_rowids()
    sparse_indices = sparse_indices.flat_values[:, 1:]  # remove first value
    sparse_indices = tf.concat(
        [tf.expand_dims(row_ids, -1), sparse_indices], axis=1
    )

    sparse_values = sparse_values.flat_values
    sparse_shape = (batch_dim,) + tuple(
        sparse_wrapper.sparse.shape.as_list()[1:]
    )
    return tf.SparseTensor(sparse_indices, sparse_values, sparse_shape)

        def wrapper(data):
            converted_data = tree.map_structure(
                lambda i: (
                    None if isinstance(i, tf.experimental.Optional) else i
                ),
                data,
            )
            result = step_func(converted_data)
            return result

    def _autoconvert_optionals(self, step_func):
        # Wrapper converting (nested) TF Optional in input data to None
        @functools.wraps(step_func)
        def wrapper(data):
            converted_data = tree.map_structure(
                lambda i: (
                    None if isinstance(i, tf.experimental.Optional) else i
                ),
                data,
            )
            result = step_func(converted_data)
            return result

        return wrapper

def stream_hessians(layers_map, gptq_objects):
    """
    Temporarily monkey-patch each target layer's `call` method so
    that input activations are streamed into the GPTQ instance
    running Hessian estimate at capture time.

    On `__enter__`: For every (name, layer) in `layers_map`, replaces
     `layer.call` with a wrapper that:
     1) extracts the layer input from `*args`/`**kwargs`,
     2) reshapes it to 2D `[-1, rows]` where
      `rows = gptq_objects[name].rows`,
     3) calls `gptq_objects[name].update_hessian_with_batch(x2d)`
    # ... truncated

def custom_gradient(fun):
    fun_with_custom_gradient = jax.custom_gradient(fun=fun)

    # Add a wrapper to unwrap variables, otherwise custom_gradient will fail
    def fun_with_custom_gradient_wrapper(*args, **kwargs):
        args, kwargs = tree.map_shape_structure(
            lambda x: x.value if isinstance(x, KerasVariable) else x,
            (args, kwargs),
        )
        return fun_with_custom_gradient(*args, **kwargs)

    return fun_with_custom_gradient_wrapper

    def get_config(self):
        config = {"layer": serialization_lib.serialize_keras_object(self.layer)}
        base_config = super().get_config()
        return {**base_config, **config}

    def wrapper(*args, **kwargs):
        with DotNotTrackScope():
            return fn(*args, **kwargs)

    def call(self, inputs, **kwargs):
        return ops.cast(self.layer(inputs, **kwargs), self.compute_dtype)

class WrapperLayer(keras.layers.Wrapper):  [saving/serialization_lib_test.py:53]
methods: call

    def call(self, x):
        return self.layer(x)

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

def copy(x):
    return x
```
