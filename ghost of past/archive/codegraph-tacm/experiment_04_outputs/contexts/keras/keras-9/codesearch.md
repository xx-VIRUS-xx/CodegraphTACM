# keras-9 :: codesearch

query: Fix Arguments display in Docs (#12007)

## selected nodes

- rank=1 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py::raise_unsupported_arg file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py
- rank=2 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/argument_validation.py::validate_string_arg file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/argument_validation.py
- rank=3 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::functional_init_arguments file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py
- rank=4 layer=FUNCTION tokens=219 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::format_argument_value file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py
- rank=5 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::_normalize_einsum_subscripts file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=6 layer=FUNCTION tokens=259 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._resolve_and_populate_arg file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=7 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::KerasFileEditor._edit file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py
- rank=8 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::get_arguments_dict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=9 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino.py::_check_jax_kwargs file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino.py
- rank=10 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py
- rank=11 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._not_implemented_error file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=12 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py::cleanup file=/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py
- rank=13 layer=FUNCTION tokens=583 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::KerasFileEditor._edit_object file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py
- rank=14 layer=FUNCTION tokens=993 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::inject_argument_info_in_traceback file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py
- rank=15 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py::patched_more_tags file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py
- rank=16 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::_adjust_padding file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py
- rank=17 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py::TestCase.assertNotAllClose file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py
- rank=18 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/rnn.py::gru file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/rnn.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py::raise_unsupported_arg [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py]
def raise_unsupported_arg(arg_name, arg_description, input_type):
    raise ValueError(
        f"When providing `x` as a {input_type}, `{arg_name}` "
        f"should not be passed. Instead, {arg_description} should "
        f"be included as part of the {input_type}."
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/argument_validation.py::validate_string_arg [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/argument_validation.py]
def validate_string_arg(
    value,
    allowable_strings,
    caller_name,
    arg_name,
    allow_none=False,
    allow_callables=False,
):
    """Validates the correctness of a string-based arg."""
    if allow_none and value is None:
        return
    elif allow_callables and callable(value):
        return
    elif isinstance(value, str) and value in allowable_strings:
        return
    raise ValueError(
        f"Unknown value for `{arg_name}` argument of {caller_name}. "
        f"Allowed values are: {allowable_strings}. Received: "
        f"{arg_name}={value}"
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::functional_init_arguments [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py]
def functional_init_arguments(args, kwargs):
    return (
        (len(args) == 2)
        or (len(args) == 1 and "outputs" in kwargs)
        or ("inputs" in kwargs and "outputs" in kwargs)
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::format_argument_value [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py]
def format_argument_value(value):
    if backend.is_tensor(value):
        # Simplified representation for eager / graph tensors
        # to keep messages readable
        if backend.backend() == "tensorflow":
            tensor_cls = "tf.Tensor"
        elif backend.backend() == "jax":
            tensor_cls = "jnp.ndarray"
        elif backend.backend() == "torch":
            tensor_cls = "torch.Tensor"
        elif backend.backend() == "numpy":
            tensor_cls = "np.ndarray"
        else:
            tensor_cls = "array"

        return (
            f"{tensor_cls}(shape={value.shape}, "
            f"dtype={backend.standardize_dtype(value.dtype)})"
        )
    return repr(value)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::_normalize_einsum_subscripts [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
def _normalize_einsum_subscripts(subscripts):
    # string.ascii_letters
    mapping = {}
    normalized_subscripts = ""
    for c in subscripts:
        if c in string.ascii_letters:
            if c not in mapping:
                mapping[c] = string.ascii_letters[len(mapping)]
            normalized_subscripts += mapping[c]
        else:
            normalized_subscripts += c
    return normalized_subscripts

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._resolve_and_populate_arg [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def _resolve_and_populate_arg(
        self, arg_name, call_spec, call_context, kwargs
    ):
        # 1) user explicitly passed it?
        if arg_name in call_spec.user_arguments_dict:
            value = call_spec.user_arguments_dict[arg_name]
        # 2) else: inherited from outer layer call?
        elif call_context.get_value(arg_name) is not None:
            value = call_context.get_value(arg_name)
        # 3) else: default from the call() signature
        else:
            value = call_spec.arguments_dict.get(arg_name, None)

        # stash it for downstream layers
        call_context.set_value(arg_name, value)

        # only inject it if this layer actually accepts it and it's not None
        if (
            self._call_has_context_arg.get(arg_name, False)
            and value is not None
        ):
            kwargs[arg_name] = value

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::KerasFileEditor._edit [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py]
            def _edit(d):
                for k in d:
                    if isinstance(d[k], dict):
                        _edit(d[k])
                if source_name in d:
                    edit_fn(d, source_name=source_name, target_name=target_name)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::get_arguments_dict [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
def get_arguments_dict(fn, args, kwargs):
    """Return a dict mapping argument names to their values."""
    sig = inspect.signature(fn)
    bound_args = sig.bind(*args, **kwargs)
    arg_dict = {}
    for name, value in bound_args.arguments.items():
        arg_dict[name] = value
    return arg_dict

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino.py::_check_jax_kwargs [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino.py]
def _check_jax_kwargs(kwargs):
    kwargs = kwargs.copy()
    if "is_static" not in kwargs:
        kwargs["is_static"] = True
    if "jax2tf_kwargs" not in kwargs:
        kwargs["jax2tf_kwargs"] = {
            "enable_xla": False,
            "native_serialization": False,
        }
    if kwargs["is_static"] is not True:
        raise ValueError(
            "`is_static` must be `True` in `kwargs` when using the jax backend."
        )
    if kwargs["jax2tf_kwargs"]["enable_xla"] is not False:
        raise ValueError(
            "`enable_xla` must be `False` in `kwargs['jax2tf_kwargs']` "
            "when using the jax backend."
        )
    if kwargs["jax2tf_kwargs"]["native_serialization"] is not False:
        raise ValueError(
            "`native_serialization` must be `False` in "
            "`kwargs['jax2tf_kwargs']` when using the jax backend."
        )
    return kwargs

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py]
    def fix_index(index, size_node):
        if fill_mode in ("constant", "nearest"):
            zero = ov_opset.constant(0, dtype=Type.i32).output(0)
            size_m1 = ov_opset.subtract(
                size_node, ov_opset.constant(1, dtype=Type.i32)
            ).output(0)
            return ov_opset.minimum(
                ov_opset.maximum(index, zero), size_m1
            ).output(0)
        elif fill_mode == "wrap":
            return ov_opset.floor_mod(index, size_node).output(0)
        elif fill_mode == "mirror":
            return _mirror_index_fixer(index, size_node)
        else:  # reflect
            return _reflect_index_fixer(index, size_node)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._not_implemented_error [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py::cleanup [/Users/xxvirusxx/PY/CodegraphTACM/keras/integration_tests/import_test.py]
def cleanup():
    cleanup_script = [
        # Exits virtual environment, deletes files, and any
        # miscellaneous install logs
        "exit",
        "rm -rf test_env",
        "rm -rf tmp_build_dir",
        "rm -f *+cpu",
    ]
    run_commands_local(cleanup_script)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::KerasFileEditor._edit_object [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py]
    def _edit_object(self, edit_fn, source_name, target_name=None):
        if target_name is not None and "/" in target_name:
            raise ValueError(
                "Argument `target_name` should be a leaf name, "
                "not a full path name. "
                f"Received: target_name='{target_name}'"
            )
        if "/" in source_name:
            # It's a path
            elements = source_name.split("/")
            weights_dict = self.weights_dict
            for e in elements[:-1]:
                if e not in weights_dict:
                    raise ValueError(
                        f"Path '{source_name}' not found in model."
                    )
                weights_dict = weights_dict[e]
            if elements[-1] not in weights_dict:
                raise ValueError(f"Path '{source_name}' not found in model.")
            edit_fn(
                weights_dict, source_name=elements[-1], target_name=target_name
            )
        else:
            # Ensure unicity
            def count_occurences(d, name, count=0):
                for k in d:
                    if isinstance(d[k], dict):
                        count += count_occurences(d[k], name, count)
                if name in d:
                    count += 1
                return count

            occurrences = count_occurences(self.weights_dict, source_name)
            if occurrences > 1:
                raise ValueError(
                    f"Name '{source_name}' occurs more than once in the model; "
                    "try passing a complete path"
                )
            if occurrences == 0:
                raise ValueError(
                    f"Source name '{source_name}' does not appear in the "
                    "model. Use `editor.weights_summary()` "
                    "to list all objects."
                )

            def _edit(d):
                for k in d:
                    if isinstance(d[k], dict):
                        _edit(d[k])
                if source_name in d:
                    edit_fn(d, source_name=source_name, target_name=target_name)

            _edit(self.weights_dict)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::inject_argument_info_in_traceback [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py]
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
        A wrapped version of `fn`.
    """
    if backend.backend() == "tensorflow":
        from tensorflow import errors as tf_errors
    else:
        tf_errors = None

    @wraps(fn)
    def error_handler(*args, **kwargs):
        if not is_traceback_filtering_enabled():
            return fn(*args, **kwargs)

        signature = None
        bound_signature = None
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            if hasattr(e, "_keras_call_info_injected"):
                # Only inject info for the innermost failing call
                raise e
            signature = inspect.signature(fn)
            try:
                # The first argument is `self`, so filter it out
                bound_signature = signature.bind(*args, **kwargs)
            except TypeError:
                # Likely unbindable arguments
                raise e

            # Add argument context
            arguments_context = []
            for arg in list(signature.parameters.values()):
                if arg.name in bound_signature.arguments:
                    value = tree.map_structure(
                        format_argument_value,
                        bound_signature.arguments[arg.name],
                    )
                else:
                    value = arg.default
                arguments_context.append(f"  • {arg.name}={value}")
            if arguments_context:
                arguments_context = "\n".join(arguments_context)
                # Get original error message and append information to it.
                if tf_errors is not None and isinstance(e, tf_errors.OpError):
                    message = e.message
                elif e.args:
                    # Canonically, the 1st argument in an exception is the error
                    # message. This works for all built-in Python exceptions.
                    message = e.args[0]
                else:
                    message = ""
                display_name = f"{object_name if object_name else fn.__name__}"
                message = (
                    f"Exception encountered when calling {display_name}.\n\n"
                    f"\x1b[1m{message}\x1b[0m\n\n"
                    f"Arguments received by {display_name}:\n"
                    f"{arguments_context}"
                )

                # Reraise exception, with added context
                if tf_errors is not None and isinstance(e, tf_errors.OpError):
                    new_e = e.__class__(e.node_def, e.op, message, e.error_code)
                else:
                    try:
                        # For standard exceptions such as ValueError, TypeError,
                        # etc.
                        new_e = e.__class__(message)
                    except TypeError:
                        # For any custom error that doesn't have a standard
                        # signature.
                        new_e = RuntimeError(message)
                new_e._keras_call_info_injected = True
            else:
                new_e = e
            raise new_e.with_traceback(e.__traceback__) from None
        finally:
            del signature
            del bound_signature

    return error_handler

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py::patched_more_tags [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py]
        def patched_more_tags(self):
            original_tags.update({"_xfail_checks": expected_failed_checks})
            return original_tags

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py::_adjust_padding [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/nn.py]
def _adjust_padding(
    padding,
):
    padding = padding.lower() if isinstance(padding, str) else padding
    if padding == "same":
        return "SAME_UPPER", [], []
    elif padding == "same_lower":
        return "SAME_LOWER", [], []
    elif padding == "valid":
        return "VALID", [], []
    pads_begin = []
    pads_end = []
    for padding_pair in padding:
        pads_begin.append(padding_pair[0])
        pads_end.append(padding_pair[1])
    return "EXPLICIT", pads_begin, pads_end

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py::TestCase.assertNotAllClose [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py]
    def assertNotAllClose(self, x1, x2, atol=1e-6, rtol=1e-6, msg=None):
        try:
            self.assertAllClose(x1, x2, atol=atol, rtol=rtol, msg=msg)
        except AssertionError:
            return
        msg = msg or ""
        raise AssertionError(
            f"The two values are close at all elements. \n{msg}.\nValues: {x1}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/rnn.py::gru [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/rnn.py]
def gru(*args, **kwargs):
    raise NotImplementedError
```
