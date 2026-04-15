# keras-9 :: tacm-full

query: Fix Arguments display in Docs (#12007)

## selected nodes

- rank=1 layer=FUNCTION tokens=259 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::tokenizer_from_json file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=2 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.get_config file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=3 layer=FUNCTION tokens=993 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py::inject_argument_info_in_traceback file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/traceback_utils.py
- rank=4 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=5 layer=FUNCTION tokens=331 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=6 layer=FUNCTION tokens=451 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::KerasFileEditor._weights_summary_interactive file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py
- rank=7 layer=FUNCTION tokens=1287 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::display_weight file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py
- rank=8 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py
- rank=9 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py
- rank=10 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::fix_negative_indices file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=11 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py::Node.input_tensors file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def fit_on_sequences(self, sequences):
        self.document_count += len(sequences)
        for seq in sequences:
            seq = set(seq)
            for i in seq:
                self.index_docs[i] += 1

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

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::KerasFileEditor._weights_summary_interactive [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py]
    def _weights_summary_interactive(self):
        def _generate_html_weights(dictionary, margin_left=0, font_size=1):
            html = ""
            for key, value in dictionary.items():
                if isinstance(value, dict) and value:
                    weights_html = _generate_html_weights(
                        value, margin_left + 20, font_size - 1
                    )
                    html += (
                        f'<details style="margin-left: {margin_left}px;">'
                        '<summary style="'
                        f"font-size: {font_size}em; "
                        "font-weight: bold;"
                        f'">{key}</summary>'
                        f"{weights_html}"
                        "</details>"
                    )
                else:
                    html += (
                        f'<details style="margin-left: {margin_left}px;">'
                        f'<summary style="font-size: {font_size}em;">'
                        f"{key} : shape={value.shape}"
                        f", dtype={value.dtype}</summary>"
                        f"<div style="
                        f'"margin-left: {margin_left}px;'
                        f'"margin-top: {margin_left}px;">'
                        f"{display_weight(value)}"
                        "</div>"
                        "</details>"
                    )
            return html

        output = "Weights structure"

        initialize_id_counter()
        output += _generate_html_weights(self.weights_dict)
        ipython.display.display(ipython.display.HTML(output))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py::display_weight [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/saving/file_editor.py]
def display_weight(weight, axis=-1, threshold=16):
    def _find_factors_closest_to_sqrt(num):
        sqrt_num = int(np.sqrt(num))

        for i in range(sqrt_num, 0, -1):
            if num % i == 0:
                M = i
                N = num // i

                if M > N:
                    return N, M
                return M, N

    def _color_from_rbg(value):
        return f"rgba({value[0]}, {value[1]}, {value[2]}, 1)"

    def _reduce_3d_array_by_mean(arr, n, axis):
        if axis == 2:
            trimmed_arr = arr[:, :, : arr.shape[2] - (arr.shape[2] % n)]
            reshaped = np.reshape(
                trimmed_arr, (arr.shape[0], arr.shape[1], -1, n)
            )
            mean_values = np.mean(reshaped, axis=3)

        elif axis == 1:
            trimmed_arr = arr[:, : arr.shape[1] - (arr.shape[1] % n), :]
            reshaped = np.reshape(
                trimmed_arr, (arr.shape[0], -1, n, arr.shape[2])
            )
            mean_values = np.mean(reshaped, axis=2)

        elif axis == 0:
            trimmed_arr = arr[: arr.shape[0] - (arr.shape[0] % n), :, :]
            reshaped = np.reshape(
                trimmed_arr, (-1, n, arr.shape[1], arr.shape[2])
            )
            mean_values = np.mean(reshaped, axis=1)

        else:
            raise ValueError("Axis must be 0, 1, or 2.")

        return mean_values

    def _create_matrix_html(matrix, subplot_size=840):
        rows, cols, num_slices = matrix.shape

        M, N = _find_factors_closest_to_sqrt(num_slices)

        try:
            from matplotlib import cm
        except ImportError:
            cm = None
        if cm:
            rgb_matrix = cm.jet(matrix)
        else:
            rgb_matrix = (matrix - np.min(matrix)) / (
                np.max(matrix) - np.min(matrix)
            )
            rgb_matrix = np.stack([rgb_matrix, rgb_matrix, rgb_matrix], axis=-1)
        rgb_matrix = (rgb_matrix[..., :3] * 255).astype("uint8")

        subplot_html = ""
        for i in range(num_slices):
            cell_html = ""
            for row in rgb_matrix[..., i, :]:
                for rgb in row:
                    color = _color_from_rbg(rgb)
                    cell_html += (
                        f'<div class="cell" '
                        f'style="background-color: {color};">'
                        f"</div>"
                    )
            subplot_html += f"""
                        <div class="matrix">
                          {cell_html}
                        </div>
                        """

        cell_size = subplot_size // (N * cols)

        increment_id_counter()
        div_id = get_id_counter()

        html_code = f"""
            <div class="unique-container_{div_id}">
                  <style>
                      .unique-container_{div_id} .subplots {{
                      display: inline-grid;
                      grid-template-columns: repeat({N}, 1fr);
                      column-gap: 5px;  /* Minimal horizontal gap */
                      row-gap: 5px;     /* Small vertical gap */
                      margin: 0;
                      padding: 0;
                    }}
                    .unique-container_{div_id} .matrix {{
                      display: inline-grid;
                      grid-template-columns: repeat({cols}, {cell_size}px);
                      grid-template-rows: repeat({rows}, {cell_size}px);
                      gap: 1px;
                      margin: 0;
                      padding: 0;
                    }}
                    .unique-container_{div_id} .cell {{
                      width: {cell_size}px;
                      height: {cell_size}px;
                      display: flex;
                      justify-content: center;
                      align-items: center;
                      font-size: 5px;
                      font-weight: bold;
                      color: white;
                    }}
                     .unique-container_{div_id} {{
                      margin-top: 20px;
                      margin-bottom: 20px;
                    }}
                  </style>
                  <div class="subplots">
                    {subplot_html}
                  </div>
                  </div>
                """

        return html_code

    if weight.ndim == 1:
        weight = weight[..., np.newaxis]

    weight = np.swapaxes(weight, axis, -1)
    weight = weight.reshape(-1, weight.shape[-1])

    M, N = _find_factors_closest_to_sqrt(weight.shape[0])
    weight = weight.reshape(M, N, weight.shape[-1])

    for reduce_axis in [0, 1, 2]:
        if weight.shape[reduce_axis] > threshold:
            weight = _reduce_3d_array_by_mean(
                weight,
                weight.shape[reduce_axis] // threshold,
                axis=reduce_axis,
            )

    weight = (weight - weight.min()) / (weight.max() - weight.min() + 1e-5)

    html_code = _create_matrix_html(weight)
    return html_code

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py::Operation.output [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/operation.py]
    def output(self):
        """Retrieves the output tensor(s) of a layer.

        Only returns the tensor(s) corresponding to the *first time*
        the operation was called.

        Returns:
            Output tensor or list of output tensors.
        """
        return self._get_node_attribute_at_index(0, "output_tensors", "output")

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py::Functional.output [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/functional.py]
    def output(self):
        return self._outputs_struct

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::fix_negative_indices [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
    def fix_negative_indices(i):
        # Correct the indices using "fill" mode which is the same as in jax
        return tf.where(i < 0, i + tf.cast(tf.shape(x)[axis], i.dtype), i)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py::Node.input_tensors [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/ops/node.py]
    def input_tensors(self):
        return self.arguments.keras_tensors
```
