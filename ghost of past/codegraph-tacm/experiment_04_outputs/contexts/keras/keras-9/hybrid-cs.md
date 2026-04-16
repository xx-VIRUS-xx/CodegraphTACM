# keras-9 :: hybrid-cs

query: Fix Arguments display in Docs (#12007)

## selected nodes

- rank=1 layer=FUNCTION tokens=993 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::inject_argument_info_in_traceback file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py
- rank=2 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::functional_init_arguments file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py
- rank=3 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::get_arguments_dict file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=4 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py::fix_index file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/openvino/image.py
- rank=5 layer=FUNCTION tokens=485 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_texts file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=6 layer=FUNCTION tokens=259 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::Layer._resolve_and_populate_arg file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py
- rank=7 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py::_resolve_compile_arguments_compat file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/saving/saving_utils.py
- rank=8 layer=FUNCTION tokens=331 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=9 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_do_gru_arguments_support_cudnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=10 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_do_lstm_arguments_support_cudnn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py
- rank=11 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::fix_negative_indices file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=12 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=13 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=14 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::_normalize_einsum_subscripts file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=15 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::KerasFileEditor._edit file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py
- rank=16 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino.py::_check_jax_kwargs file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/export/openvino.py
- rank=17 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/rnn.py::gru file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/rnn.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py::functional_init_arguments [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/model.py]
def functional_init_arguments(args, kwargs):
    return (
        (len(args) == 2)
        or (len(args) == 1 and "outputs" in kwargs)
        or ("inputs" in kwargs and "outputs" in kwargs)
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py::get_arguments_dict [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/layers/layer.py]
def get_arguments_dict(fn, args, kwargs):
    """Return a dict mapping argument names to their values."""
    sig = inspect.signature(fn)
    bound_args = sig.bind(*args, **kwargs)
    arg_dict = {}
    for name, value in bound_args.arguments.items():
        arg_dict[name] = value
    return arg_dict

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_texts [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def fit_on_texts(self, texts):
        for text in texts:
            self.document_count += 1
            if self.char_level or isinstance(text, list):
                if self.lower:
                    if isinstance(text, list):
                        text = [text_elem.lower() for text_elem in text]
                    else:
                        text = text.lower()
                seq = text
            else:
                if self.analyzer is None:
                    seq = text_to_word_sequence(
                        text,
                        filters=self.filters,
                        lower=self.lower,
                        split=self.split,
                    )
                else:
                    seq = self.analyzer(text)
            for w in seq:
                if w in self.word_counts:
                    self.word_counts[w] += 1
                else:
                    self.word_counts[w] = 1
            for w in set(seq):
                # In how many documents each word occurs
                self.word_docs[w] += 1

        wcounts = list(self.word_counts.items())
        wcounts.sort(key=lambda x: x[1], reverse=True)
        # forcing the oov_token to index 1 if it exists
        if self.oov_token is None:
            sorted_voc = []
        else:
            sorted_voc = [self.oov_token]
        sorted_voc.extend(wc[0] for wc in wcounts)

        # note that index 0 is reserved, never assigned to an existing word
        self.word_index = dict(
            zip(sorted_voc, list(range(1, len(sorted_voc) + 1)))
        )

        self.index_word = {c: w for w, c in self.word_index.items()}

        for w, c in list(self.word_docs.items()):
            self.index_docs[self.word_index[w]] = c

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_do_gru_arguments_support_cudnn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py]
def _do_gru_arguments_support_cudnn(
    activation,
    recurrent_activation,
    unroll,
    use_bias,
    reset_after,
):
    from keras.src import activations
    from keras.src import ops

    return (
        activation in (activations.tanh, tf.tanh, ops.tanh)
        and recurrent_activation
        in (activations.sigmoid, tf.sigmoid, ops.sigmoid)
        and not unroll
        and use_bias
        and reset_after
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py::_do_lstm_arguments_support_cudnn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/rnn.py]
def _do_lstm_arguments_support_cudnn(
    activation,
    recurrent_activation,
    unroll,
    use_bias,
):
    from keras.src import activations
    from keras.src import ops

    return (
        activation in (activations.tanh, tf.tanh, ops.tanh)
        and recurrent_activation
        in (activations.sigmoid, tf.sigmoid, ops.sigmoid)
        and not unroll
        and use_bias
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::fix_negative_indices [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
    def fix_negative_indices(i):
        # Correct the indices using "fill" mode which is the same as in jax
        return tf.where(i < 0, i + tf.cast(tf.shape(x)[axis], i.dtype), i)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def fit_on_sequences(self, sequences):
        self.document_count += len(sequences)
        for seq in sequences:
            seq = set(seq)
            for i in seq:
                self.index_docs[i] += 1

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.get_config [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def get_config(self):
        json_word_counts = json.dumps(self.word_counts)
        json_word_docs = json.dumps(self.word_docs)
        json_index_docs = json.dumps(self.index_docs)
        json_word_index = json.dumps(self.word_index)
        json_index_word = json.dumps(self.index_word)

        return {
            "num_words": self.num_words,
            "filters": self.filters,
            "lower": self.lower,
            "split": self.split,
            "char_level": self.char_level,
            "oov_token": self.oov_token,
            "document_count": self.document_count,
            "word_counts": json_word_counts,
            "word_docs": json_word_docs,
            "index_docs": json_index_docs,
            "index_word": json_index_word,
            "word_index": json_word_index,
        }

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::KerasFileEditor._edit [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py]
            def _edit(d):
                for k in d:
                    if isinstance(d[k], dict):
                        _edit(d[k])
                if source_name in d:
                    edit_fn(d, source_name=source_name, target_name=target_name)

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/rnn.py::gru [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/rnn.py]
def gru(*args, **kwargs):
    raise NotImplementedError
```
