# keras-37 :: tacm-full

query: Fix __call__ for Bidirectional wrapper (#9248)

## selected nodes

- rank=1 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py::Classifier.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py
- rank=2 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::benchmark_bidirectional file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py
- rank=3 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::vectorize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=4 layer=FUNCTION tokens=1297 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_rewrite_constant_fold file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py
- rank=5 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_activation_call_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=6 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=7 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=8 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::no_automatic_dependency_tracking file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py
- rank=9 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=10 layer=FUNCTION tokens=767 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py
- rank=11 layer=FUNCTION tokens=340 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py::slice_tensorflow_sparse_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py
- rank=12 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer._autoconvert_optionals file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py
- rank=13 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py
- rank=14 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py::custom_gradient file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py
- rank=15 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py::TensorflowSparseSliceable.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py
- rank=16 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py::TensorflowSparseSliceable.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py
- rank=17 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer.wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=18 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py::flax_dropout_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py::Classifier.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py]
    def call(self, x, training=None):
        for wrapper in self.torch_wrappers:
            x = wrapper(x, training=training)
        return self.fc(x)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::benchmark_bidirectional [/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::vectorize [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py]
def vectorize(pyfunc, *, excluded=None, signature=None):
    def wrapper(*args, **kwargs):
        converted_args = tuple(convert_to_tensor(arg) for arg in args)
        return pyfunc(*converted_args, **kwargs)

    return wrapper

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py::patched_rewrite_constant_fold [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/tf2onnx_lib.py]
    def patched_rewrite_constant_fold(g, ops):
        """
        We call tensorflow transform with constant folding but in some cases
        tensorflow does fold all constants. Since there are a bunch of ops in
        onnx that use attributes where tensorflow has dynamic inputs, we badly
        want constant folding to work. For cases where tensorflow missed
        something, make another pass over the graph and fix want we care about.
        """
        func_map = {
            "Add": np.add,
            "GreaterEqual": np.greater_equal,
            "Cast": np.asarray,
            "ConcatV2": np.concatenate,
            "Less": np.less,
            "ListDiff": np.setdiff1d,
            "Mul": np.multiply,
            "Pack": np.stack,
            "Range": np.arange,
            "Sqrt": np.sqrt,
            "Sub": np.subtract,
        }
        ops = list(ops)

        keep_looking = True
        while keep_looking:
            keep_looking = False
            for idx, op in enumerate(ops):
                func = func_map.get(op.type)
                if func is None:
                    continue
                if set(op.output) & set(g.outputs):
                    continue
                try:
                    inputs = []
                    for node in op.inputs:
                        if not node.is_const():
                            break
                        inputs.append(node.get_tensor_value(as_list=False))

                    logger.debug(
                        "op name %s, %s, %s",
                        op.name,
                        len(op.input),
                        len(inputs),
                    )
                    if inputs and len(op.input) == len(inputs):
                        logger.info(
                            "folding node type=%s, name=%s" % (op.type, op.name)
                        )
                        if op.type == "Cast":
                            dst = op.get_attr_int("to")
                            np_type = tf2onnx.utils.map_onnx_to_numpy_type(dst)
                            val = np.asarray(*inputs, dtype=np_type)
                        elif op.type == "ConcatV2":
                            axis = inputs[-1]
                            values = inputs[:-1]
                            val = func(tuple(values), axis)
                        elif op.type == "ListDiff":
                            out_type = op.get_attr_int("out_idx")
                            np_type = tf2onnx.utils.map_onnx_to_numpy_type(
                                out_type
                            )
                            val = func(*inputs)
                            val = val.astype(np_type)
                        elif op.type in ["Pack"]:
                            # handle ops that need input array and axis
                            axis = op.get_attr_int("axis")
                            val = func(inputs, axis=axis)
                        elif op.type == "Range":
                            dtype = op.get_attr_int("Tidx")
                            np_type = tf2onnx.utils.map_onnx_to_numpy_type(
                                dtype
                            )
                            val = func(*inputs, dtype=np_type)
                        else:
                            val = func(*inputs)

                        new_node_name = tf2onnx.utils.make_name(op.name)
                        new_output_name = new_node_name
                        old_output_name = op.output[0]
                        old_node_name = op.name
                        logger.debug(
                            "create const node [%s] replacing [%s]",
                            new_node_name,
                            old_node_name,
                        )
                        ops[idx] = g.make_const(new_node_name, val)

                        logger.debug(
                            "replace old output [%s] with new output [%s]",
                            old_output_name,
                            new_output_name,
                        )
                        # need to re-write the consumers input name to use the
                        # const name
                        consumers = g.find_output_consumers(old_output_name)
                        if consumers:
                            for consumer in consumers:
                                g.replace_input(
                                    consumer, old_output_name, new_output_name
                                )

                        # keep looking until there is nothing we can fold.
                        # We keep the graph in topological order so if we
                        # folded, the result might help a following op.
                        keep_looking = True
                except Exception as ex:
                    tb = traceback.format_exc()
                    logger.info("exception: %s, details: %s", ex, tb)
                    # ignore errors

        return ops

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_activation_call_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
                def rematerialized_activation_call_wrapper(*args, **kwargs):
                    original_activation = self.activation
                    self.activation = remat.remat(original_activation)
                    try:
                        return layer_call(*args, **kwargs)
                    finally:
                        self.activation = original_activation

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py]
    def wrapper(*args, **kwargs):
        converted_args = tuple(convert_to_tensor(arg) for arg in args)
        return pyfunc(*converted_args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py]
    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::no_automatic_dependency_tracking [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py]
def no_automatic_dependency_tracking(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        with DotNotTrackScope():
            return fn(*args, **kwargs)

    return wrapper

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py]
    def output(self):
        return self._outputs_struct

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py::Bidirectional.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/rnn/bidirectional.py]
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
            )
        if backward_layer is not None and not isinstance(backward_layer, Layer):
            raise ValueError(
                "`backward_layer` need to be a `keras.layers.Layer` "
                f"instance. Received: {backward_layer}"
            )
        if merge_mode not in ["sum", "mul", "ave", "concat", None]:
            raise ValueError(
                f"Invalid merge mode. Received: {merge_mode}. "
                "Merge mode should be one of "
                '{"sum", "mul", "ave", "concat", None}'
            )
        super().__init__(**kwargs)

        # Recreate the forward layer from the original layer config, so that it
        # will not carry over any state from the layer.
        config = serialization_lib.serialize_keras_object(layer)
        config["config"]["name"] = (
            f"forward_{utils.removeprefix(layer.name, 'forward_')}"
        )
        self.forward_layer = serialization_lib.deserialize_keras_object(config)

        if backward_layer is None:
            config = serialization_lib.serialize_keras_object(layer)
            config["config"]["go_backwards"] = True
            config["config"]["name"] = (
                f"backward_{utils.removeprefix(layer.name, 'backward_')}"
            )
            self.backward_layer = serialization_lib.deserialize_keras_object(
                config
            )
        else:
            self.backward_layer = backward_layer
        # Keep the use_cudnn attribute if defined (not serialized).
        if hasattr(layer, "use_cudnn"):
            self.forward_layer.use_cudnn = layer.use_cudnn
            self.backward_layer.use_cudnn = layer.use_cudnn
        self._verify_layer_config()

        def force_zero_output_for_mask(layer):
            # Force the zero_output_for_mask to be True if returning sequences.
            if getattr(layer, "zero_output_for_mask", None) is not None:
                layer.zero_output_for_mask = layer.return_sequences

        force_zero_output_for_mask(self.forward_layer)
        force_zero_output_for_mask(self.backward_layer)

        self.merge_mode = merge_mode
        if weights:
            nw = len(weights)
            self.forward_layer.initial_weights = weights[: nw // 2]
            self.backward_layer.initial_weights = weights[nw // 2 :]
        self.stateful = layer.stateful
        self.return_sequences = layer.return_sequences
        self.return_state = layer.return_state
        self.supports_masking = True
        self.input_spec = layer.input_spec

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py::slice_tensorflow_sparse_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py::TensorFlowTrainer._autoconvert_optionals [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/trainer.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py]
    def wrapper(*args, **kwargs):
        with DotNotTrackScope():
            return fn(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py::custom_gradient [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py::TensorflowSparseSliceable.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py]
    def __init__(self, array):
        super().__init__(to_tensorflow_sparse_wrapper(array))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py::TensorflowSparseSliceable.__getitem__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/array_slicing.py]
    def __getitem__(self, indices):
        return slice_tensorflow_sparse_wrapper(self.array, indices)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer.wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py]
        def wrapper(*args):
            args = args[0:index] + (value,) + args[index:]
            return fn(*args)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py::flax_dropout_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer_test.py]
    def flax_dropout_wrapper(module, x, training):
        return module.my_apply(x, training)
```
