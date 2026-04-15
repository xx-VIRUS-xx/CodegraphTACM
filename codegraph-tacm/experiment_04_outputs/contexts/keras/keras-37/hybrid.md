# keras-37 :: hybrid

query: Fix __call__ for Bidirectional wrapper (#9248)

## selected nodes

- rank=1 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_activation_call_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=2 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py::Classifier.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py
- rank=3 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.build_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=4 layer=FUNCTION tokens=430 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=5 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer.wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=6 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=7 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py
- rank=8 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=9 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py::MyWrapper.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py
- rank=10 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._int4_call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=11 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/saved_model_test.py::CustomSignatureModel.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/saved_model_test.py
- rank=12 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::Relu6.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=13 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py::Cond.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py
- rank=14 layer=FUNCTION tokens=542 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=15 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._int8_call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=16 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._float8_call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=17 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/input_layer.py::InputLayer.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/input_layer.py
- rank=18 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::Relu.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py
- rank=19 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::no_automatic_dependency_tracking file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py
- rank=20 layer=FUNCTION tokens=385 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py::_wrap_clone_function file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py
- rank=21 layer=FUNCTION tokens=549 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=22 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.quantize_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=23 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::vectorize file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py
- rank=24 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py::benchmark_bidirectional file=/Users/xxvirusxx/PY/CodegraphTACM/keras/benchmarks/layer_benchmark/rnn_benchmark.py
- rank=25 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::operation_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_activation_call_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
                def rematerialized_activation_call_wrapper(*args, **kwargs):
                    original_activation = self.activation
                    self.activation = remat.remat(original_activation)
                    try:
                        return layer_call(*args, **kwargs)
                    finally:
                        self.activation = original_activation

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py::Classifier.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py]
    def call(self, x, training=None):
        for wrapper in self.torch_wrappers:
            x = wrapper(x, training=training)
        return self.fc(x)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.build_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.__new__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
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
            signature = inspect.signature(original_build_method)
            obj._build_shapes_dict = signature.bind(*args, **kwargs).arguments
            # Set built, post build actions, and lock state.
            obj.built = True
            obj._post_build()
            obj._lock_state()

        obj.build = build_wrapper

        # Wrap the user-provided `quantize` method in the `quantize_wrapper`
        # to add tracker support.
        original_quantize_method = obj.quantize

        @wraps(original_quantize_method)
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

        obj.quantize = quantize_wrapper

        return obj

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer.wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py]
        def wrapper(*args):
            args = args[0:index] + (value,) + args[index:]
            return fn(*args)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py]
    def wrapper(*args, **kwargs):
        converted_args = tuple(convert_to_tensor(arg) for arg in args)
        return pyfunc(*converted_args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py]
    def wrapper(*args, **kwargs):
        with DotNotTrackScope():
            return fn(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def call(self, *args, **kwargs):
        raise self._not_implemented_error(self.call)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py::MyWrapper.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/serialization_lib_test.py]
    def call(self, inputs):
        return self._wrapped(inputs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._int4_call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _int4_call(self, *args, **kwargs):
        raise self._not_implemented_error(self._int4_call)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/saved_model_test.py::CustomSignatureModel.__call__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/saved_model_test.py]
    def __call__(self, x):
        return x * self.v

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::Relu6.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py]
    def call(self, x):
        return backend.nn.relu6(x)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py::Cond.__call__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py]
    def __call__(self, *args, **kwargs):
        def call_fn(*args, **kwargs):
            if any_symbolic_tensors(args, kwargs):
                return self.symbolic_call(*args, **kwargs)
            else:
                return self.call(*args, **kwargs)

        if traceback_utils.is_traceback_filtering_enabled():
            # Wrap self.call to provide helpful info in case of exception
            call_fn = traceback_utils.inject_argument_info_in_traceback(
                call_fn,
                object_name=(f"{self.__class__.__name__}.call()"),
            )
            return call_fn(*args, **kwargs)

        # Plain flow.
        return call_fn(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.__call__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py]
    def __call__(self, *args, **kwargs):
        if traceback_utils.is_traceback_filtering_enabled():
            # Wrap self.call to provide helpful info in case of exception
            if any_symbolic_tensors(args, kwargs):
                call_fn = self.symbolic_call
            else:
                if getattr(self, "_remat_mode", None) is not None:
                    if getattr(self, "quantization_mode", None) is not None:
                        call_fn = self.rematerialized_call(
                            self.quantized_call,
                            *args,
                            **kwargs,
                        )
                    else:
                        call_fn = self.rematerialized_call(
                            self.call, *args, **kwargs
                        )
                else:
                    if getattr(self, "quantization_mode", None) is not None:
                        call_fn = self.quantized_call
                    else:
                        call_fn = self.call
            call_fn = traceback_utils.inject_argument_info_in_traceback(
                call_fn,
                object_name=(f"{self.__class__.__name__}.call()"),
            )
            return call_fn(*args, **kwargs)

        # Plain flow.
        if any_symbolic_tensors(args, kwargs):
            return self.symbolic_call(*args, **kwargs)
        elif getattr(self, "_remat_mode", None) is not None:
            if getattr(self, "quantization_mode", None) is not None:
                return self.rematerialized_call(
                    self.quantized_call, *args, **kwargs
                )(*args, **kwargs)
            else:
                return self.rematerialized_call(self.call, *args, **kwargs)(
                    *args, **kwargs
                )
        else:
            if getattr(self, "quantization_mode", None) is not None:
                return self.quantized_call(*args, **kwargs)
            else:
                return self.call(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._int8_call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _int8_call(self, *args, **kwargs):
        raise self._not_implemented_error(self._int8_call)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._float8_call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _float8_call(self, *args, **kwargs):
        raise self._not_implemented_error(self._float8_call)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/input_layer.py::InputLayer.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/core/input_layer.py]
    def call(self):
        return

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py::Relu.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/nn.py]
    def call(self, x):
        return backend.nn.relu(x)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::no_automatic_dependency_tracking [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py]
def no_automatic_dependency_tracking(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        with DotNotTrackScope():
            return fn(*args, **kwargs)

    return wrapper

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py::_wrap_clone_function [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/cloning.py]
def _wrap_clone_function(
    clone_function, call_function=None, recursive=False, cache=None
):
    """Wrapper to handle recursiveness and layer sharing."""
    if clone_function is None:

        def _clone_layer(layer):
            return layer.__class__.from_config(layer.get_config())

        clone_function = _clone_layer

    if cache is None:
        cache = {}

    def wrapped_clone_function(layer):
        if id(layer) in cache:
            return cache[id(layer)]
        if recursive:
            if isinstance(layer, Sequential):
                # Note: Sequential doesn't support call_function.
                clone = clone_model(
                    layer,
                    clone_function=clone_function,
                    recursive=True,
                    cache=cache,
                )
                cache[id(layer)] = clone
                return clone
            elif isinstance(layer, Functional):
                clone = clone_model(
                    layer,
                    clone_function=clone_function,
                    call_function=call_function,
                    recursive=True,
                    cache=cache,
                )
                cache[id(layer)] = clone
                return clone
        clone = clone_function(layer)
        cache[id(layer)] = clone
        return clone

    return wrapped_clone_function

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def rematerialized_call(self, layer_call, *args, **kwargs):
        """Enable rematerialization dynamically for layer's call method.

        Args:
            layer_call: The original `call` method of a layer.

        Returns:
            Rematerialized layer's `call` method.
        """

        def compute_size(x):
            return (
                math.prod([d or 1 for d in x.shape])
                if isinstance(x, KerasTensor)
                else 0
            )

        # Full rematerialization
        if self._remat_mode.mode == "full":
            return remat.remat(layer_call)

        # Apply rematerialization to specific layers
        elif self._remat_mode.mode == "list_of_layers" and (
            self.name in self._remat_mode.layer_names
        ):
            return remat.remat(layer_call)

        # Apply rematerialization based on output size threshold
        elif self._remat_mode.mode == "larger_than":
            output_spec = self.compute_output_spec(*args, **kwargs)
            output_size = sum(
                tree.flatten(tree.map_structure(compute_size, output_spec))
            )
            if (
                output_size
                and output_size > self._remat_mode.output_size_threshold
            ):
                return remat.remat(layer_call)
        elif self._remat_mode.mode == "activations":
            has_activation = (
                hasattr(self, "activation") and self.activation is not None
            )
            if has_activation:

                @functools.wraps(layer_call)
                def rematerialized_activation_call_wrapper(*args, **kwargs):
                    original_activation = self.activation
                    self.activation = remat.remat(original_activation)
                    try:
                        return layer_call(*args, **kwargs)
                    finally:
                        self.activation = original_activation

                return rematerialized_activation_call_wrapper
        return layer_call

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.quantize_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py::vectorize [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/numpy.py]
def vectorize(pyfunc, *, excluded=None, signature=None):
    def wrapper(*args, **kwargs):
        converted_args = tuple(convert_to_tensor(arg) for arg in args)
        return pyfunc(*converted_args, **kwargs)

    return wrapper

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::operation_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py]
def operation_fn(operation, **call_context_args):
    """Wraps each op to inject the call-context args."""

    def call(*args, **kwargs):
        # Propagate all registered call-context args
        for name, value in call_context_args.items():
            if (
                name in getattr(operation, "_call_context_args", {})
                and value is not None
            ):
                kwargs[name] = value

        return operation(*args, **kwargs)

    return call
```
