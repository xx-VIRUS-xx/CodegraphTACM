# keras-37 :: hybrid-cs

query: Fix __call__ for Bidirectional wrapper (#9248)

## selected nodes

- rank=1 layer=FUNCTION tokens=2229 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=2 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py::Classifier.call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py
- rank=3 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=4 layer=FUNCTION tokens=542 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=5 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::no_automatic_dependency_tracking file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py
- rank=6 layer=FUNCTION tokens=549 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.rematerialized_call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=7 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._maybe_reset_call_context file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=8 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._int8_call file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=9 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py::Cond.__call__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/core.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer.__call__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
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
            y = self.dtype_policy.convert_input(
                x, self.autocast, self.input_dtype
            )
            if mask is not None:
                backend.set_keras_mask(y, mask)
            return y

        # Used to avoid expensive `tree` operations in the most common case.
        if (
            kwargs
            or len(args) != 1
            or not is_backend_tensor_or_symbolic(args[0], allow_none=False)
            or backend.standardize_dtype(args[0].dtype) != self.input_dtype
        ) and self._convert_input_args:
            args = tree.map_structure(maybe_convert, args)
            kwargs = tree.map_structure(maybe_convert, kwargs)

        ##########################################################
        # 2. Enforce that only tensors can be passed positionally.
        if not self._allow_non_tensor_positional_args:
            for arg in tree.flatten(args):
                if not is_backend_tensor_or_symbolic(arg, allow_none=True):
                    raise ValueError(
                        "Only input tensors may be passed as "
                        "positional arguments. The following argument value "
                        f"should be passed as a keyword argument: {arg} "
                        f"(of type {type(arg)})"
                    )

        # Caches info about `call()` signature, args, kwargs.
        call_spec = CallSpec(
            self._call_signature, self._call_context_args, args, kwargs
        )

        ############################################
        # 3. Check input spec for 1st positional arg.
        # TODO: consider extending this to all args and kwargs.
        self._assert_input_compatibility(call_spec.first_arg)

        ################
        # 4. Call build
        with self._open_name_scope():
            self._maybe_build(call_spec)

        ##########################
        # 5. Infer training value
        # Training phase for `Layer.call` is set via (in order of priority):
        # (1) The `training` argument passed to this `Layer.call`, if not None
        # (2) The training argument of an outer `Layer.call`.
        # (4) Any non-None default value for `training` in the call signature
        # (5) False (treating the layer as if it's in inference)

        # Maintains info about the `Layer.call` stack
        # across nested calls.
        call_context = self._get_call_context()

        for context_arg in self._call_context_args:
            self._resolve_and_populate_arg(
                context_arg, call_spec, call_context, kwargs
            )

        ##############################
        # 6. Populate mask argument(s)
        if len(call_spec.tensor_arguments_dict) == 1:
            if (
                "mask" in call_spec.argument_names
                and call_spec.arguments_dict["mask"] is None
            ):
                arg_name = list(call_spec.tensor_arguments_dict.keys())[0]
                only_tensor_arg = call_spec.tensor_arguments_dict[arg_name]
                mask = tree.map_structure(
                    backend.get_keras_mask,
                    only_tensor_arg,
                )
                kwargs["mask"] = mask
        elif len(call_spec.tensor_arguments_dict) > 1:
            for k, v in call_spec.tensor_arguments_dict.items():
                expected_mask_arg_name = f"{k}_mask"
                if expected_mask_arg_name in call_spec.argument_names:
                    if call_spec.arguments_dict[expected_mask_arg_name] is None:
                        mask = tree.map_structure(backend.get_keras_mask, v)
                        kwargs[expected_mask_arg_name] = mask

        # We need to cache the `previous_mask` before `__call__` because the
        # mask might be removed during the call, such as `MultiHeadAttention`.
        if "mask" in kwargs and kwargs["mask"] is not None:
            # Case 1: Mask was explicitly passed or auto-populated in step 6.
            previous_mask = kwargs["mask"]
        else:
            # Case 2: Fallback to the mask attached to the first input tensor.
            previous_mask = tree.map_structure(
                backend.get_keras_mask, call_spec.first_arg
            )

        ####################
        # 7. Call the layer.
        try:
            with self._open_name_scope():
                current_scope = backend.get_autocast_scope()
                new_scope = None
                if current_scope is not None:
                    # Clear or update the current scope if necessary.
                    if not self.autocast:
                        new_scope = backend.AutocastScope(None)
                    elif not backend.is_float_dtype(self.compute_dtype):
                        # Some preprocessing layers might have a non-float
                        # dtype, we should not autocast in this case.
                        new_scope = backend.AutocastScope(None)
                    elif current_scope.dtype != self.compute_dtype:
                        new_scope = backend.AutocastScope(self.compute_dtype)
                elif self.compute_dtype != self.variable_dtype:
                    # Enter a new scope if our dtypes are "mixed".
                    new_scope = backend.AutocastScope(self.compute_dtype)
                if new_scope is not None:
                    with new_scope:
                        outputs = super().__call__(*args, **kwargs)
                else:
                    outputs = super().__call__(*args, **kwargs)
                # Change the layout for the layer output if needed.
                # This is useful for relayout intermediate tensor in the model
                # to achieve the optimal performance.
                distribution = distribution_lib.distribution()
                if distribution is not None:
                    current_layer_path = current_path()
                    current_layer_path += "/output"
                    layout = distribution.get_tensor_layout(current_layer_path)
                    if layout:
                        outputs = distribution_lib.distribute_tensor(
                            outputs, layout
                        )

                self.built = True
                # Record activity regularizer loss.
                if self.activity_regularizer is not None:
                    for output in tree.flatten(outputs):
                        if backend.is_tensor(output):
                            loss = self.activity_regularizer(output)
                            if output.ndim > 0:
                                # Normalize by batch size to ensure consistent
                                # regularization strength across batch sizes
                                batch_size = ops.cast(
                                    ops.shape(output)[0], dtype=loss.dtype
                                )
                                loss = ops.divide_no_nan(loss, batch_size)
                            self.add_loss(loss)

            # Set `previous_mask` on outputs if available. It is provided only
            # for the first positional input arg and its mask.
            # TODO: consider extending this to all args and kwargs.
            if self.supports_masking:
                self._set_mask_metadata(
                    call_spec.first_arg, outputs, previous_mask
                )
            elif any(m is not None for m in tree.flatten(previous_mask)):
                warnings.warn(
                    f"Layer '{self.name}' (of type {self.__class__.__name__}) "
                    "was passed an input with a mask attached to it. "
                    "However, this layer does not support masking and will "
                    "therefore destroy the mask information. Downstream "
                    "layers will not see the mask."
                )
        finally:
            # Destroy call context if we created it
            self._maybe_reset_call_context()

        ################################################
        # 8. Add a node in the graph for symbolic calls.
        if any_symbolic_tensors(original_args, original_kwargs):
            Node(
                operation=self,
                call_args=original_args,
                call_kwargs=original_kwargs,
                outputs=outputs,
            )

        return outputs

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py::Classifier.call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/torch_utils_test.py]
    def call(self, x, training=None):
        for wrapper in self.torch_wrappers:
            x = wrapper(x, training=training)
        return self.fc(x)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py]
    def call(*args, **kwargs):
        # Propagate all registered call-context args
        for name, value in call_context_args.items():
            if (
                name in getattr(operation, "_call_context_args", {})
                and value is not None
            ):
                kwargs[name] = value

        return operation(*args, **kwargs)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py::no_automatic_dependency_tracking [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/tracking.py]
def no_automatic_dependency_tracking(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        with DotNotTrackScope():
            return fn(*args, **kwargs)

    return wrapper

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._maybe_reset_call_context [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _maybe_reset_call_context(self):
        layer_call_ctx = global_state.get_global_attribute("current_call_ctx")
        if layer_call_ctx is None or layer_call_ctx.entry_layer == self:
            global_state.set_global_attribute("current_call_ctx", None)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._int8_call [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _int8_call(self, *args, **kwargs):
        raise self._not_implemented_error(self._int8_call)

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
```
