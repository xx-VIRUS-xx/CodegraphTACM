# keras-11 :: minilm

query: Improve type-check for Sequence (#11468)

## selected nodes

- rank=1 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential._obj_type file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py
- rank=2 layer=FUNCTION tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::traverse_bottom_up file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=3 layer=FUNCTION tokens=839 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::assert_same_structure file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py
- rank=4 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=5 layer=FUNCTION tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py
- rank=6 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py
- rank=7 layer=FUNCTION tokens=379 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.texts_to_sequences_generator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=8 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.sequences_to_texts file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=9 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.sequences_to_texts_generator file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py
- rank=10 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py
- rank=11 layer=FUNCTION tokens=1173 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils.py::pad_sequences file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils.py
- rank=12 layer=FUNCTION tokens=394 node=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py::_lattice_result_type file=/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py::Sequential._obj_type [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/models/sequential.py]
    def _obj_type(self):
        return "Sequential"

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::traverse_bottom_up [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py]
    def traverse_bottom_up(s):
        registration = REGISTERED_CLASSES.get(type(s), None)
        if registration is not None:
            flat_meta_s = registration.flatten(s)
            ret = [traverse_bottom_up(x) for x in list(flat_meta_s[0])]
            ret = registration.unflatten(flat_meta_s[1], ret)
        elif not dmtree.is_nested(s):
            ret = s
        elif isinstance(s, collections.abc.Mapping):
            ret = [traverse_bottom_up(s[key]) for key in sorted(s)]
            ret = dmtree._sequence_like(s, ret)
        else:
            ret = [traverse_bottom_up(x) for x in s]
            ret = dmtree._sequence_like(s, ret)
        func_ret = func(ret)
        return ret if func_ret is None else remap_map_to_none(func_ret, None)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py::assert_same_structure [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/tree/dmtree_impl.py]
def assert_same_structure(a, b):
    # Fully reimplemented in Python to handle registered classes.

    # Don't handle OrderedDict as a registered class, use the normal dict path
    # so that OrderedDict is equivalent to dict per optree behavior.
    a_registration = REGISTERED_CLASSES.get(type(a), None)
    if type(a) is collections.OrderedDict:
        a_registration = None

    b_registration = REGISTERED_CLASSES.get(type(b), None)
    if type(b) is collections.OrderedDict:
        b_registration = None

    if a_registration != b_registration:
        raise ValueError(
            f"Custom node type mismatch; "
            f"expected type: {type(a)}, got type: {type(b)} "
            f"while comparing {a} and {b}."
        )
    if a_registration is not None:
        a_flat_meta = a_registration.flatten(a)
        b_flat_meta = b_registration.flatten(b)
        a_flat = list(a_flat_meta[0])
        b_flat = list(b_flat_meta[0])
        if not a_flat_meta[1] == b_flat_meta[1]:
            raise ValueError(
                f"Mismatch custom node data; "
                f"expected: {a_flat_meta[1]}, got: {b_flat_meta[1]} "
                f"while comparing {a} and {b}."
            )
        if len(a_flat) != len(b_flat):
            raise ValueError(
                f"Arity mismatch; expected: {len(a)}, got: {len(b)} "
                f"while comparing {a} and {b}."
            )
        for sub_a, sub_b in zip(a_flat, b_flat):
            assert_same_structure(sub_a, sub_b)
    elif not dmtree.is_nested(a):
        if dmtree.is_nested(b):
            raise ValueError(
                f"Structures don't have the same nested structure: {a}, {b}."
            )
    elif isinstance(
        a, (dict, collections.OrderedDict, collections.defaultdict)
    ):
        if not isinstance(
            b, (dict, collections.OrderedDict, collections.defaultdict)
        ):
            raise ValueError(
                f"Expected an instance of dict, collections.OrderedDict, or "
                f"collections.defaultdict, got {type(b)} "
                f"while comparing {a} and {b}."
            )
        a_keys = sorted(a)
        b_keys = sorted(b)
        if not a_keys == b_keys:
            raise ValueError(
                f"Dictionary key mismatch; "
                f"expected key(s): {a_keys}, got key(s): {b_keys} "
                f"while comparing {a} and {b}."
            )
        for key in a_keys:
            assert_same_structure(a[key], b[key])
    elif isinstance(a, collections.abc.Mapping):
        raise ValueError(
            f"Encountered unregistered collections.abc.Mapping type: {type(a)} "
            f"while comparing {a} and {b}."
        )
    else:
        if type(a) is not type(b):
            raise ValueError(
                f"Expected an instance of {type(a)}, got {type(b)} "
                f"while comparing {a} and {b}."
            )
        if not len(a) == len(b):
            raise ValueError(
                f"Arity mismatch; expected: {len(a)}, got: {len(b)} "
                f"while comparing {a} and {b}."
            )
        for sub_a, sub_b in zip(a, b):
            assert_same_structure(sub_a, sub_b)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.fit_on_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def fit_on_sequences(self, sequences):
        self.document_count += len(sequences)
        for seq in sequences:
            seq = set(seq)
            for i in seq:
                self.index_docs[i] += 1

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py::searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/tensorflow/numpy.py]
def searchsorted(sorted_sequence, values, side="left"):
    if ndim(sorted_sequence) != 1:
        raise ValueError(
            "`searchsorted` only supports 1-D sorted sequences. "
            "You can use `keras.ops.vectorized_map` "
            "to extend it to N-D sequences. Received: "
            f"sorted_sequence.shape={sorted_sequence.shape}"
        )
    sequence_len = sorted_sequence.shape[0]
    out_type = (
        "int32"
        if sequence_len is not None and sequence_len <= np.iinfo(np.int32).max
        else "int64"
    )
    return tf.searchsorted(
        sorted_sequence, values, side=side, out_type=out_type
    )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py::CompileLoss.key_check_fn [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/trainers/compile_utils.py]
            def key_check_fn(key, objs):
                return all(
                    [
                        issubclass(type(obj), (list, tuple)) and key < len(obj)
                        for obj in objs
                    ]
                )

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.texts_to_sequences_generator [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def texts_to_sequences_generator(self, texts):
        num_words = self.num_words
        oov_token_index = self.word_index.get(self.oov_token)
        for text in texts:
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
            vect = []
            for w in seq:
                i = self.word_index.get(w)
                if i is not None:
                    if num_words and i >= num_words:
                        if oov_token_index is not None:
                            vect.append(oov_token_index)
                    else:
                        vect.append(i)
                elif self.oov_token is not None:
                    vect.append(oov_token_index)
            yield vect

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.sequences_to_texts [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def sequences_to_texts(self, sequences):
        return list(self.sequences_to_texts_generator(sequences))

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py::Tokenizer.sequences_to_texts_generator [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/legacy/preprocessing/text.py]
    def sequences_to_texts_generator(self, sequences):
        num_words = self.num_words
        oov_token_index = self.word_index.get(self.oov_token)
        for seq in sequences:
            vect = []
            for num in seq:
                word = self.index_word.get(num)
                if word is not None:
                    if num_words and num >= num_words:
                        if oov_token_index is not None:
                            vect.append(self.index_word[oov_token_index])
                    else:
                        vect.append(word)
                elif self.oov_token is not None:
                    vect.append(self.index_word[oov_token_index])
            vect = " ".join(vect)
            yield vect

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py::searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/numpy/numpy.py]
def searchsorted(sorted_sequence, values, side="left"):
    if ndim(sorted_sequence) != 1:
        raise ValueError(
            "`searchsorted` only supports 1-D sorted sequences. "
            "You can use `keras.ops.vectorized_map` "
            "to extend it to N-D sequences. Received: "
            f"sorted_sequence.shape={sorted_sequence.shape}"
        )
    out_type = (
        "int32"
        if sorted_sequence.shape[0] <= np.iinfo(np.int32).max
        else "int64"
    )
    return np.searchsorted(sorted_sequence, values, side=side).astype(out_type)

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils.py::pad_sequences [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/utils/sequence_utils.py]
def pad_sequences(
    sequences,
    maxlen=None,
    dtype="int32",
    padding="pre",
    truncating="pre",
    value=0.0,
):
    """Pads sequences to the same length.

    This function transforms a list (of length `num_samples`)
    of sequences (lists of integers)
    into a 2D NumPy array of shape `(num_samples, num_timesteps)`.
    `num_timesteps` is either the `maxlen` argument if provided,
    or the length of the longest sequence in the list.

    Sequences that are shorter than `num_timesteps`
    are padded with `value` until they are `num_timesteps` long.

    Sequences longer than `num_timesteps` are truncated
    so that they fit the desired length.

    The position where padding or truncation happens is determined by
    the arguments `padding` and `truncating`, respectively.
    Pre-padding or removing values from the beginning of the sequence is the
    default.

    >>> sequence = [[1], [2, 3], [4, 5, 6]]
    >>> keras.utils.pad_sequences(sequence)
    array([[0, 0, 1],
           [0, 2, 3],
           [4, 5, 6]], dtype=int32)

    >>> keras.utils.pad_sequences(sequence, value=-1)
    array([[-1, -1,  1],
           [-1,  2,  3],
           [ 4,  5,  6]], dtype=int32)

    >>> keras.utils.pad_sequences(sequence, padding='post')
    array([[1, 0, 0],
           [2, 3, 0],
           [4, 5, 6]], dtype=int32)

    >>> keras.utils.pad_sequences(sequence, maxlen=2)
    array([[0, 1],
           [2, 3],
           [5, 6]], dtype=int32)

    Args:
        sequences: List of sequences (each sequence is a list of integers).
        maxlen: Optional Int, maximum length of all sequences. If not provided,
            sequences will be padded to the length of the longest individual
            sequence.
        dtype: (Optional, defaults to `"int32"`). Type of the output sequences.
            To pad sequences with variable length strings, you can use `object`.
        padding: String, "pre" or "post" (optional, defaults to `"pre"`):
            pad either before or after each sequence.
        truncating: String, "pre" or "post" (optional, defaults to `"pre"`):
            remove values from sequences larger than
            `maxlen`, either at the beginning or at the end of the sequences.
        value: Float or String, padding value. (Optional, defaults to `0.`)

    Returns:
        NumPy array with shape `(len(sequences), maxlen)`
    """
    if not hasattr(sequences, "__len__"):
        raise ValueError("`sequences` must be iterable.")
    num_samples = len(sequences)

    lengths = []
    sample_shape = ()
    flag = True

    # take the sample shape from the first non empty sequence
    # checking for consistency in the main loop below.

    for x in sequences:
        try:
            lengths.append(len(x))
            if flag and len(x):
                sample_shape = np.asarray(x).shape[1:]
                flag = False
        except TypeError as e:
            raise ValueError(
                "`sequences` must be a list of iterables. "
                f"Found non-iterable: {str(x)}"
            ) from e

    if maxlen is None:
        maxlen = np.max(lengths)

    is_dtype_str = np.issubdtype(dtype, np.str_) or np.issubdtype(
        dtype, np.str_
    )
    if isinstance(value, str) and dtype is not object and not is_dtype_str:
        raise ValueError(
            f"`dtype` {dtype} is not compatible with `value`'s type: "
            f"{type(value)}\nYou should set `dtype=object` for variable length "
            "strings."
        )

    x = np.full((num_samples, maxlen) + sample_shape, value, dtype=dtype)
    for idx, s in enumerate(sequences):
        if not len(s):
            continue  # empty list/array was found
        if truncating == "pre":
            trunc = s[-maxlen:]
        elif truncating == "post":
            trunc = s[:maxlen]
        else:
            raise ValueError(f'Truncating type "{truncating}" not understood')

        # check `trunc` has expected shape
        trunc = np.asarray(trunc, dtype=dtype)
        if trunc.shape[1:] != sample_shape:
            raise ValueError(
                f"Shape of sample {trunc.shape[1:]} of sequence at "
                f"position {idx} is different from expected shape "
                f"{sample_shape}"
            )

        if padding == "post":
            x[idx, : len(trunc)] = trunc
        elif padding == "pre":
            x[idx, -len(trunc) :] = trunc
        else:
            raise ValueError(f'Padding type "{padding}" not understood')
    return x

# /Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py::_lattice_result_type [/Users/xxvirusxx/PY/CodegraphTACM/keras/keras/src/backend/common/dtypes.py]
def _lattice_result_type(*args):
    dtypes, weak_types = zip(*(_dtype_and_weaktype(arg) for arg in args))
    if len(dtypes) == 1:
        out_dtype = dtypes[0]
        out_weak_type = weak_types[0]
    elif len(set(dtypes)) == 1 and not all(weak_types):
        # Trivial promotion case. This allows extended dtypes through.
        out_dtype = dtypes[0]
        out_weak_type = False
    elif all(weak_types):
        # If all inputs are weakly typed, we compute the bound of the
        # strongly-typed counterparts and apply the weak type at the end. This
        # avoids returning the incorrect result with non-canonical weak types
        # (e.g. weak int16).
        out_dtype = _least_upper_bound(
            *{_respect_weak_type(d, False) for d in dtypes}
        )
        out_weak_type = True
    else:
        out_dtype = _least_upper_bound(
            *{_respect_weak_type(d, w) for d, w in zip(dtypes, weak_types)}
        )
        out_weak_type = any(out_dtype is t for t in WEAK_TYPES)

    out_weak_type = (out_dtype != "bool") and out_weak_type
    precision = config.floatx()[-2:]
    if out_weak_type:
        out_dtype = _resolve_weak_type(out_dtype, precision=precision)

    # Force to be 32-bit dtype when encountering 64-bit dtype. This is to
    # be aligned with JAX's default behavior.
    out_dtype = BIT64_TO_BIT32_DTYPE.get(out_dtype, out_dtype)
    return out_dtype
```
