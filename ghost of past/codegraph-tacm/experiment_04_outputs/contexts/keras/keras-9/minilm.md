# keras-9 :: minilm

query: Fix Arguments display in Docs (#12007)

## selected nodes

- rank=1 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::get_arguments_dict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=2 layer=FUNCTION tokens=240 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer._validate_signature file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=3 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::functional_init_arguments file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py
- rank=4 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py::raise_unsupported_arg file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py
- rank=5 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/callback.py::Callback.set_params file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/callback.py
- rank=6 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py::func_skipping_none file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py
- rank=7 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::func_skipping_none file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=8 layer=FUNCTION tokens=324 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py::wrapped_parametrize_with_checks file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py
- rank=9 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::CallContext.set_value file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=10 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py::JaxVariable.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py
- rank=11 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer.wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=12 layer=FUNCTION tokens=331 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=13 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer._partial_with_positional file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=14 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py::ModifiedBuildLayer.build file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py
- rank=15 layer=FUNCTION tokens=796 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::error_handler file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py
- rank=16 layer=FUNCTION tokens=259 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._resolve_and_populate_arg file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=17 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_wrapper.py::SKLearnTransformer._more_tags file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_wrapper.py
- rank=18 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py::Config.__repr__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py
- rank=19 layer=FUNCTION tokens=662 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::CallSpec.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::get_arguments_dict [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
def get_arguments_dict(fn, args, kwargs):
    """Return a dict mapping argument names to their values."""
    sig = inspect.signature(fn)
    bound_args = sig.bind(*args, **kwargs)
    arg_dict = {}
    for name, value in bound_args.arguments.items():
        arg_dict[name] = value
    return arg_dict

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer._validate_signature [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py]
    def _validate_signature(self, fn, fn_name, allowed, required):
        fn_parameters = inspect.signature(fn).parameters
        for parameter_name in required:
            if parameter_name not in fn_parameters:
                raise ValueError(
                    f"Missing required argument in `{fn_name}`: "
                    f"`{parameter_name}`"
                )

        parameter_names = []
        for parameter in fn_parameters.values():
            if parameter.name not in allowed:
                raise ValueError(
                    f"Unsupported argument in `{fn_name}`: `{parameter.name}`, "
                    f"supported arguments are `{'`, `'.join(allowed)}`"
                )
            parameter_names.append(parameter.name)

        return parameter_names

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::functional_init_arguments [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py]
def functional_init_arguments(args, kwargs):
    return (
        (len(args) == 2)
        or (len(args) == 1 and "outputs" in kwargs)
        or ("inputs" in kwargs and "outputs" in kwargs)
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py::raise_unsupported_arg [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/data_adapters/__init__.py]
def raise_unsupported_arg(arg_name, arg_description, input_type):
    raise ValueError(
        f"When providing `x` as a {input_type}, `{arg_name}` "
        f"should not be passed. Instead, {arg_description} should "
        f"be included as part of the {input_type}."
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/callback.py::Callback.set_params [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/callbacks/callback.py]
    def set_params(self, params):
        self.params = params

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py::func_skipping_none [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py]
        def func_skipping_none(*args):
            # Check if the reference entry (first one) is None
            if args[0] is None:
                if not all(s is None for s in args):
                    raise ValueError(
                        "Structure mismatch: some arguments are None, others "
                        f"are not. Received arguments: {args}."
                    )
                return None
            return func(*args)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::func_skipping_none [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py]
        def func_skipping_none(*args):
            # Check if the reference entry (first one) is None
            if args[0] is None:
                if not all(s is None for s in args):
                    raise ValueError(
                        "Structure mismatch: some arguments are None, others "
                        f"are not. Received arguments: {args}."
                    )
                return None
            return func(*args)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py::wrapped_parametrize_with_checks [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_test.py]
def wrapped_parametrize_with_checks(
    estimators,
    *,
    legacy=True,
    expected_failed_checks=None,
):
    """Wrapped `parametrize_with_checks` handling backwards compat."""
    sklearn_version = parse_version(
        parse_version(sklearn.__version__).base_version
    )

    if sklearn_version >= parse_version("1.6"):
        return parametrize_with_checks(
            estimators,
            legacy=legacy,
            expected_failed_checks=expected_failed_checks,
        )

    def patched_more_tags(estimator, expected_failed_checks):
        import copy

        original_tags = copy.deepcopy(sklearn.utils._tags._safe_tags(estimator))

        def patched_more_tags(self):
            original_tags.update({"_xfail_checks": expected_failed_checks})
            return original_tags

        estimator.__class__._more_tags = patched_more_tags
        return estimator

    estimators = [
        patched_more_tags(estimator, expected_failed_checks(estimator))
        for estimator in estimators
    ]

    # legacy is not supported and ignored
    return parametrize_with_checks(estimators)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::CallContext.set_value [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def set_value(self, arg_name, value):
        """Set `arg_name` = `value` on this context object."""
        setattr(self, arg_name, value)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py::JaxVariable.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/jax/core.py]
    def __init__(self, *args, layout=None, **kwargs):
        # Intercept layout parameter so that it is available
        # during initialization.
        self._layout = layout
        super().__init__(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer.wrapper [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py]
        def wrapper(*args):
            args = args[0:index] + (value,) + args[index:]
            return fn(*args)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def __init__(
        self,
        num_words=None,
        filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
        lower=True,
        split=" ",
        char_level=False,
        oov_token=None,
        analyzer=None,
        **kwargs,
    ):
        # Legacy support
        if "nb_words" in kwargs:
            warnings.warn(
                "The `nb_words` argument in `Tokenizer` "
                "has been renamed `num_words`."
            )
            num_words = kwargs.pop("nb_words")
        document_count = kwargs.pop("document_count", 0)
        if kwargs:
            raise TypeError(f"Unrecognized keyword arguments: {str(kwargs)}")

        self.word_counts = collections.OrderedDict()
        self.word_docs = collections.defaultdict(int)
        self.filters = filters
        self.split = split
        self.lower = lower
        self.num_words = num_words
        self.document_count = document_count
        self.char_level = char_level
        self.oov_token = oov_token
        self.index_docs = collections.defaultdict(int)
        self.word_index = {}
        self.index_word = {}
        self.analyzer = analyzer

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer._partial_with_positional [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py]
    def _partial_with_positional(self, fn, index, value):
        """Return a new partial with one positional argument set to a value.

        This is needed because `jax2tf` only supports positional arguments and
        `functools.partial` only supports setting positional arguments starting
        from the left. Our use case is the `training` argument which is
        typically the righmost argument.

        Args:
          fn: the function to wrap.
          index: the index of the positional argument to set to `value`.
          value: the value for the positional argument at `index`.
        """

        @functools.wraps(fn)
        def wrapper(*args):
            args = args[0:index] + (value,) + args[index:]
            return fn(*args)

        return wrapper

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py::ModifiedBuildLayer.build [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/testing/test_case.py]
                    def build(self, *args, **kwargs):
                        pass

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::error_handler [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_wrapper.py::SKLearnTransformer._more_tags [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/wrappers/sklearn_wrapper.py]
    def _more_tags(self):
        # required to be compatible with scikit-learn<1.6
        return {
            "preserves_dtype": [],
        }

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py::Config.__repr__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/config.py]
    def __repr__(self):
        return f"<Config {self._config}>"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::CallSpec.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
    def __init__(self, signature, call_context_args, args, kwargs):
        # Strip out user-supplied call-context args that this layer’s `call()`
        # does not accept (otherwise `signature.bind` would raise).
        # This includes built-in args like `training`, and user-defined args.
        call_args = {
            context_arg: kwargs.pop(context_arg)
            for context_arg in call_context_args
            if context_arg in kwargs and context_arg not in signature.parameters
        }

        bound_args = signature.bind(*args, **kwargs)

        # Combine the two dicts.
        self.user_arguments_dict = {**call_args, **bound_args.arguments}

        bound_args.apply_defaults()
        arg_dict = {}
        arg_names = []
        tensor_arg_dict = {}
        tensor_args = []
        tensor_arg_names = []
        nested_tensor_arg_names = []
        for name, value in bound_args.arguments.items():
            arg_dict[name] = value
            arg_names.append(name)
            if is_backend_tensor_or_symbolic(value):
                tensor_args.append(value)
                tensor_arg_names.append(name)
                tensor_arg_dict[name] = value
            elif tree.is_nested(value) and len(value) > 0:
                flat_values = tree.flatten(value)
                if all(
                    is_backend_tensor_or_symbolic(x, allow_none=True)
                    for x in flat_values
                ):
                    tensor_args.append(value)
                    tensor_arg_names.append(name)
                    tensor_arg_dict[name] = value
                    nested_tensor_arg_names.append(name)
                elif any(is_backend_tensor_or_symbolic(x) for x in flat_values):
                    raise ValueError(
                        "In a nested call() argument, "
                        "you cannot mix tensors and non-tensors. "
                        "Received invalid mixed argument: "
                        f"{name}={value}"
                    )
        self.arguments_dict = arg_dict
        self.argument_names = arg_names
        self.tensor_arguments_dict = tensor_arg_dict
        self.tensor_arguments_names = tensor_arg_names
        self.nested_tensor_argument_names = nested_tensor_arg_names
        self.first_arg = arg_dict[arg_names[0]]
        if all(
            backend.is_tensor(x) for x in self.tensor_arguments_dict.values()
        ):
            self.eager = True
        else:
            self.eager = False
```
