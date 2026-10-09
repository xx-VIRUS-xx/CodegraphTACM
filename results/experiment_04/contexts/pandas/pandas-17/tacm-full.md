# pandas-17 :: tacm-full

query: BUG: DTI/TDI.insert doing invalid casting (#33703)

## selected nodes

- rank=1 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=2 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=3 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_EastAsianTextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=4 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=5 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=6 layer=FUNCTION tokens=2506 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py::to_numeric file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py
- rank=7 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=8 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Term.type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=9 layer=FUNCTION tokens=159 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta_dti file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py]
    def len(self):
        """
        Compute the length of each element in the Series/Index.

        The element may be a sequence (such as a string, tuple or list) or a collection
        (such as a dictionary).

        Returns
        -------
        Series or Index of int
            A Series or Index of integer values indicating the length of each
            element in the Series or Index.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.

        Examples
        --------
        Returns the length (number of characters) in a string. Returns the
        number of entries for dictionaries, lists or tuples.

        >>> s = pd.Series(
        ...     ["dog", "", 5, {"foo": "bar"}, [2, 3, 5, 7], ("one", "two", "three")]
        ... )
        >>> s
        0                  dog
        1
        2                    5
        3       {'foo': 'bar'}
        4         [2, 3, 5, 7]
        5    (one, two, three)
        dtype: object
        >>> s.str.len()
        0    3.0
        1    0.0
        2    NaN
        3    1.0
        4    4.0
        5    3.0
        dtype: float64
        """
        result = self._data.array._str_len()
        return self._wrap_result(result, returns_string=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py]
    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.
        StringMethods.len : Compute the length of each element in the Series/Index.

        Examples
        --------
        >>> import pyarrow as pa
        >>> s = pd.Series(
        ...     [
        ...         [1, 2, 3],
        ...         [3],
        ...     ],
        ...     dtype=pd.ArrowDtype(pa.list_(pa.int64())),
        ... )
        >>> s.list.len()
        0    3
        1    1
        dtype: int32[pyarrow]
        """
        from pandas import Series

        value_lengths = pc.list_value_length(self._pa_array)
        return Series(
            value_lengths,
            dtype=ArrowDtype(value_lengths.type),
            index=self._data.index,
            name=self._data.name,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_EastAsianTextAdjustment.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py]
    def len(self, text: str) -> int:
        """
        Calculate display width considering unicode East Asian Width
        """
        if not isinstance(text, str):
            return len(text)

        return sum(
            self._EAW_MAP.get(east_asian_width(c), self.ambiguous_width) for c in text
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py]
    def len(self, text: str) -> int:
        return len(text)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py]
    def tdi(self, monotonic):
        tdi = timedelta_range("1 Day", periods=10)
        if monotonic == "decreasing":
            tdi = tdi[::-1]
        elif monotonic is None:
            taker = np.arange(10, dtype=np.intp)
            np.random.default_rng(2).shuffle(taker)
            tdi = tdi.take(taker)
        return tdi

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py::to_numeric [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py]
def to_numeric(
    arg,
    errors: DateTimeErrorChoices = "raise",
    downcast: Literal["integer", "signed", "unsigned", "float"] | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,
):
    """
    Convert argument to a numeric type.

    If the input is already of a numeric dtype, the dtype will be preserved.
    For non-numeric inputs, the default return dtype is `float64` or `int64`
    depending on the data supplied. Use the `downcast` parameter
    to obtain other dtypes.

    Please note that precision loss may occur if really large numbers
    are passed in. Due to the internal limitations of `ndarray`, if
    numbers smaller than `-9223372036854775808` (np.iinfo(np.int64).min)
    or larger than `18446744073709551615` (np.iinfo(np.uint64).max) are
    passed in, it is very likely they will be converted to float so that
    they can be stored in an `ndarray`. These warnings apply similarly to
    `Series` since it internally leverages `ndarray`.

    Parameters
    ----------
    arg : scalar, list, tuple, 1-d array, or Series
        Argument to be converted.

    errors : {'raise', 'coerce'}, default 'raise'
        - If 'raise', then invalid parsing will raise an exception.
        - If 'coerce', then invalid parsing will be set as NaN.

    downcast : str, default None
        Can be 'integer', 'signed', 'unsigned', or 'float'.
        If not None, and if the data has been successfully cast to a
        numerical dtype (or if the data was numeric to begin with),
        downcast that resulting data to the smallest numerical dtype
        possible according to the following rules:

        - 'integer' or 'signed': smallest signed int dtype (min.: np.int8)
        - 'unsigned': smallest unsigned int dtype (min.: np.uint8)
        - 'float': smallest float dtype (min.: np.float32)

        As this behaviour is separate from the core conversion to
        numeric values, any errors raised during the downcasting
        will be surfaced regardless of the value of the 'errors' input.

        In addition, downcasting will only occur if the size
        of the resulting data's dtype is strictly larger than
        the dtype it is to be cast to, so if none of the dtypes
        checked satisfy that specification, no downcasting will be
        performed on the data.

    dtype_backend : {'numpy_nullable', 'pyarrow'}
        Back-end data type applied to the resultant :class:`DataFrame`
        (still experimental). If not specified, the default behavior
        is to not use nullable data types. If specified, the behavior
        is as follows:

        * ``"numpy_nullable"``: returns nullable-dtype-backed object
        * ``"pyarrow"``: returns with pyarrow-backed nullable object

        .. versionadded:: 2.0

    Returns
    -------
    ret
        Numeric if parsing succeeded.
        Return type depends on input.  Series if Series, otherwise ndarray.

    Raises
    ------
    ValueError
        If the input contains non-numeric values and `errors='raise'`.
    TypeError
        If the input is not list-like, 1D, or scalar convertible to numeric,
        such as nested lists or unsupported input types (e.g., dict).

    See Also
    --------
    DataFrame.astype : Cast argument to a specified dtype.
    to_datetime : Convert argument to datetime.
    to_timedelta : Convert argument to timedelta.
    numpy.ndarray.astype : Cast a numpy array to a specified type.
    DataFrame.convert_dtypes : Convert dtypes.

    Examples
    --------
    Take separate series and convert to numeric, coercing when told to

    >>> s = pd.Series(["1.0", "2", -3])
    >>> pd.to_numeric(s)
    0    1.0
    1    2.0
    2   -3.0
    dtype: float64
    >>> pd.to_numeric(s, downcast="float")
    0    1.0
    1    2.0
    2   -3.0
    dtype: float32
    >>> pd.to_numeric(s, downcast="signed")
    0    1
    1    2
    2   -3
    dtype: int8
    >>> s = pd.Series(["apple", "1.0", "2", -3])
    >>> pd.to_numeric(s, errors="coerce")
    0    NaN
    1    1.0
    2    2.0
    3   -3.0
    dtype: float64

    Downcasting of nullable integer and floating dtypes is supported:

    >>> s = pd.Series([1, 2, 3], dtype="Int64")
    >>> pd.to_numeric(s, downcast="integer")
    0    1
    1    2
    2    3
    dtype: Int8
    >>> s = pd.Series([1.0, 2.1, 3.0], dtype="Float64")
    >>> pd.to_numeric(s, downcast="float")
    0    1.0
    1    2.1
    2    3.0
    dtype: Float32
    """
    if downcast not in (None, "integer", "signed", "unsigned", "float"):
        raise ValueError("invalid downcasting method provided")

    if errors not in ("raise", "coerce"):
        raise ValueError("invalid error value specified")

    check_dtype_backend(dtype_backend)

    is_series = False
    is_index = False
    is_scalars = False

    if isinstance(arg, ABCSeries):
        is_series = True
        values = arg.values
    elif isinstance(arg, ABCIndex):
        is_index = True
        if needs_i8_conversion(arg.dtype):
            values = arg.view("i8")
        else:
            values = arg.values
    elif isinstance(arg, (list, tuple)):
        values = np.array(arg, dtype="O")
    elif is_scalar(arg):
        if is_decimal(arg):
            return float(arg)
        if is_number(arg):
            return arg
        if isinstance(arg, (Timedelta, Timestamp)):
            return arg._value
        is_scalars = True
        values = np.array([arg], dtype="O")
    elif getattr(arg, "ndim", 1) > 1:
        raise TypeError("arg must be a list, tuple, 1-d array, or Series")
    else:
        values = arg

    # GH33013: for IntegerArray & FloatingArray extract non-null values for casting
    # save mask to reconstruct the full array after casting
    mask: npt.NDArray[np.bool_] | None = None
    if isinstance(values, BaseMaskedArray):
        mask = values._mask
        values = values._data[~mask]

    values_dtype = getattr(values, "dtype", None)
    if isinstance(values_dtype, ArrowDtype):
        mask = values.isna()
        values = values.dropna().to_numpy()
    new_mask: np.ndarray | None = None
    if is_numeric_dtype(values_dtype):
        pass
    elif lib.is_np_dtype(values_dtype, "mM"):
        values = values.view(np.int64)
    else:
        values = ensure_object(values)
        coerce_numeric = errors != "raise"
        values, new_mask = lib.maybe_convert_numeric(  # type: ignore[call-overload]
            values,
            set(),
            coerce_numeric=coerce_numeric,
            convert_to_masked_nullable=dtype_backend is not lib.no_default
            or (
                isinstance(values_dtype, StringDtype)
                and values_dtype.na_value is libmissing.NA
            ),
        )

    if new_mask is not None:
        # Remove unnecessary values, is expected later anyway and enables
        # downcasting
        values = values[~new_mask]
    elif (dtype_backend is not lib.no_default and new_mask is None) or (
        isinstance(values_dtype, StringDtype) and values_dtype.na_value is libmissing.NA
    ):
        new_mask = np.zeros(values.shape, dtype=np.bool_)

    # attempt downcast only if the data has been successfully converted
    # to a numerical dtype and if a downcast method has been specified
    if downcast is not None and is_numeric_dtype(values.dtype):
        typecodes: str | None = None

        if downcast in ("integer", "signed"):
            typecodes = np.typecodes["Integer"]
        elif downcast == "unsigned" and (not len(values) or np.min(values) >= 0):
            typecodes = np.typecodes["UnsignedInteger"]
        elif downcast == "float":
            typecodes = np.typecodes["Float"]

            # pandas support goes only to np.float32,
            # as float dtypes smaller than that are
            # extremely rare and not well supported
            float_32_char = np.dtype(np.float32).char
            float_32_ind = typecodes.index(float_32_char)
            typecodes = typecodes[float_32_ind:]

        if typecodes is not None:
            # from smallest to largest
            for typecode in typecodes:
                dtype = np.dtype(typecode)
                if dtype.itemsize <= values.dtype.itemsize:
                    values = maybe_downcast_numeric(values, dtype)

                    # successful conversion
                    if values.dtype == dtype:
                        break

    # GH33013: for IntegerArray, BooleanArray & FloatingArray need to reconstruct
    # masked array
    if (mask is not None or new_mask is not None) and not is_string_dtype(values.dtype):
        if mask is None or (new_mask is not None and new_mask.shape == mask.shape):
            # GH 52588
            mask = new_mask
        else:
            mask = mask.copy()
        assert isinstance(mask, np.ndarray)
        data = np.zeros(mask.shape, dtype=values.dtype)
        data[~mask] = values

        from pandas.core.arrays import (
            ArrowExtensionArray,
            BooleanArray,
            FloatingArray,
            IntegerArray,
        )

        klass: type[IntegerArray | BooleanArray | FloatingArray]
        if is_integer_dtype(data.dtype):
            klass = IntegerArray
        elif is_bool_dtype(data.dtype):
            klass = BooleanArray
        else:
            klass = FloatingArray
        values = klass(data, mask)

        if dtype_backend == "pyarrow" or isinstance(values_dtype, ArrowDtype):
            values = ArrowExtensionArray(values.__arrow_array__())

    if is_series:
        return arg._constructor(values, index=arg.index, name=arg.name)
    elif is_index:
        # because we want to coerce to numeric if possible,
        # do not use _shallow_copy
        from pandas import Index

        return Index(values, name=arg.name)
    elif is_scalars:
        return values[0]
    else:
        return values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Term.type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py]
    def type(self):
        try:
            # GH#35247 avoid .values which boxes PeriodArray/IntervalArray
            dtype = self._value.dtype
        except AttributeError:
            try:
                return self._value.values.dtype  # DataFrame
            except AttributeError:
                return type(self._value)  # scalar

        # Match .values.dtype behavior for types that external_values boxes
        if isinstance(dtype, (PeriodDtype, IntervalDtype)):
            return np.dtype("object")
        return dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta_dti [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py]
    def dta_dti(self, unit, dtype):
        tz = getattr(dtype, "tz", None)

        dti = pd.date_range("2016-01-01", periods=55, freq="D", tz=tz, unit="ns")
        if tz is None:
            arr = np.asarray(dti).astype(f"M8[{unit}]")
        else:
            arr = np.asarray(dti.tz_convert("UTC").tz_localize(None)).astype(
                f"M8[{unit}]"
            )

        dta = DatetimeArray._simple_new(arr, dtype=dtype)
        return dta, dti
```
