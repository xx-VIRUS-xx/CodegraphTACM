# keras-9 :: hybrid

query: Fix Arguments display in Docs (#12007)

## selected nodes

- rank=1 layer=FUNCTION tokens=796 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::error_handler file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py
- rank=2 layer=FUNCTION tokens=331 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=3 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::get_arguments_dict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=4 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::functional_init_arguments file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py
- rank=5 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py::func_skipping_none file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/torchtree_impl.py
- rank=6 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::func_skipping_none file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=7 layer=FUNCTION tokens=240 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py::JaxLayer._validate_signature file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/jax_layer.py
- rank=8 layer=FUNCTION tokens=259 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::tokenizer_from_json file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=9 layer=FUNCTION tokens=662 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::CallSpec.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=10 layer=FUNCTION tokens=993 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::inject_argument_info_in_traceback file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py
- rank=11 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::_resolve_compile_arguments_compat file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::get_arguments_dict [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
def get_arguments_dict(fn, args, kwargs):
    """Return a dict mapping argument names to their values."""
    sig = inspect.signature(fn)
    bound_args = sig.bind(*args, **kwargs)
    arg_dict = {}
    for name, value in bound_args.arguments.items():
        arg_dict[name] = value
    return arg_dict

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::functional_init_arguments [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py]
def functional_init_arguments(args, kwargs):
    return (
        (len(args) == 2)
        or (len(args) == 1 and "outputs" in kwargs)
        or ("inputs" in kwargs and "outputs" in kwargs)
    )

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::tokenizer_from_json [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
def tokenizer_from_json(json_string):
    """DEPRECATED."""
    tokenizer_config = json.loads(json_string)
    config = tokenizer_config.get("config")

    word_counts = json.loads(config.pop("word_counts"))
    word_docs = json.loads(config.pop("word_docs"))
    index_docs = json.loads(config.pop("index_docs"))
    # Integer indexing gets converted to strings with json.dumps()
    index_docs = {int(k): v for k, v in index_docs.items()}
    index_word = json.loads(config.pop("index_word"))
    index_word = {int(k): v for k, v in index_word.items()}
    word_index = json.loads(config.pop("word_index"))

    tokenizer = Tokenizer(**config)
    tokenizer.word_counts = word_counts
    tokenizer.word_docs = word_docs
    tokenizer.index_docs = index_docs
    tokenizer.word_index = word_index
    tokenizer.index_word = index_word
    return tokenizer

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::_resolve_compile_arguments_compat [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py]
def _resolve_compile_arguments_compat(obj, obj_config, module):
    """Resolves backwards compatibility issues with training config arguments.

    This helper function accepts built-in Keras modules such as optimizers,
    losses, and metrics to ensure an object being deserialized is compatible
    with Keras 3 built-ins. For legacy H5 files saved within Keras 3,
    this does nothing.
    """
    if isinstance(obj, str) and obj not in module.ALL_OBJECTS_DICT:
        obj = module.get(obj_config["config"]["name"])
    return obj
```
