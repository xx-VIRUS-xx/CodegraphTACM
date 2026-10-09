# pandas-17 :: minilm

query: BUG: DTI/TDI.insert doing invalid casting (#33703)

## selected nodes

- rank=1 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py::IntegerDtype._safe_cast file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py
- rank=2 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=3 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::maybe_downcast_to_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=4 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericDtype._safe_cast file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py
- rank=5 layer=FUNCTION tokens=1375 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::_cast_to_stata_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=6 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=7 layer=FUNCTION tokens=1108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::maybe_cast_to_integer_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=8 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/floating.py::FloatingDtype._safe_cast file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/floating.py
- rank=9 layer=FUNCTION tokens=223 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._add_timedeltalike_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=10 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestInsertIndexCoercion._assert_insert_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py
- rank=11 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::TestMaskedArrays._cast_pointwise_result file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py
- rank=12 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py::IntegerDtype._safe_cast [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py]
    def _safe_cast(cls, values: np.ndarray, dtype: np.dtype, copy: bool) -> np.ndarray:
        """
        Safely cast the values to the given dtype.

        "safe" in this context means the casting is lossless. e.g. if 'values'
        has a floating dtype, each value must be an integer.
        """
        try:
            return values.astype(dtype, casting="safe", copy=copy)
        except TypeError as err:
            casted = values.astype(dtype, copy=copy)
            if (casted == values).all():
                return casted

            raise TypeError(
                f"cannot safely cast non-equivalent {values.dtype} to {np.dtype(dtype)}"
            ) from err

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_add_dti_offset(self, offset):
        with warnings.catch_warnings(record=True):
            self.rng + offset

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::maybe_downcast_to_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def maybe_downcast_to_dtype(result: ArrayLike, dtype: np.dtype) -> ArrayLike:
    """
    try to cast to the specified dtype (e.g. convert back to bool/int
    or could be an astype of float64->float32
    """
    if isinstance(result, ABCSeries):
        result = result._values
    do_round = False

    if not isinstance(dtype, np.dtype):
        # enforce our signature annotation
        raise TypeError(dtype)  # pragma: no cover

    converted = maybe_downcast_numeric(result, dtype, do_round)
    if converted is not result:
        return converted

    # a datetimelike
    # GH12821, iNaT is cast to float
    if dtype.kind in "mM" and result.dtype.kind in "if":
        result = result.astype(dtype)

    elif dtype.kind == "m" and result.dtype == _dtype_obj:
        # test_where_downcast_to_td64
        result = cast("np.ndarray", result)
        result = array_to_timedelta64(result)

    elif dtype == np.dtype("M8[ns]") and result.dtype == _dtype_obj:
        result = cast("np.ndarray", result)
        return np.asarray(maybe_cast_to_datetime(result, dtype=dtype))

    return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericDtype._safe_cast [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py]
    def _safe_cast(cls, values: np.ndarray, dtype: np.dtype, copy: bool) -> np.ndarray:
        """
        Safely cast the values to the given dtype.

        "safe" in this context means the casting is lossless.
        """
        raise AbstractMethodError(cls)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::_cast_to_stata_types [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py]
def _cast_to_stata_types(data: DataFrame) -> DataFrame:
    """
    Checks the dtypes of the columns of a pandas DataFrame for
    compatibility with the data types and ranges supported by Stata, and
    converts if necessary.

    Parameters
    ----------
    data : DataFrame
        The DataFrame to check and convert

    Notes
    -----
    Numeric columns in Stata must be one of int8, int16, int32, float32 or
    float64, with some additional value restrictions.  int8 and int16 columns
    are checked for violations of the value restrictions and upcast if needed.
    int64 data is not usable in Stata, and so it is downcast to int32 whenever
    the value are in the int32 range, and sidecast to float64 when larger than
    this range.  If the int64 values are outside of the range of those
    perfectly representable as float64 values, a warning is raised.

    bool columns are cast to int8.  uint columns are converted to int of the
    same size if there is no loss in precision, otherwise are upcast to a
    larger type.  uint64 is currently not supported since it is concerted to
    object in a DataFrame.
    """
    ws = ""
    # original, if small, if large
    conversion_data: tuple[
        tuple[type, type, type],
        tuple[type, type, type],
        tuple[type, type, type],
        tuple[type, type, type],
        tuple[type, type, type],
    ] = (
        (np.bool_, np.int8, np.int8),
        (np.uint8, np.int8, np.int16),
        (np.uint16, np.int16, np.int32),
        (np.uint32, np.int32, np.int64),
        (np.uint64, np.int64, np.float64),
    )

    float32_max = struct.unpack("<f", b"\xff\xff\xff\x7e")[0]
    float64_max = struct.unpack("<d", b"\xff\xff\xff\xff\xff\xff\xdf\x7f")[0]

    for col in data:
        # Cast from unsupported types to supported types
        is_nullable_int = (
            isinstance(data[col].dtype, ExtensionDtype)
            and data[col].dtype.kind in "iub"
        )
        # We need to find orig_missing before altering data below
        orig_missing = data[col].isna()
        if is_nullable_int:
            fv = 0 if data[col].dtype.kind in "iu" else False
            # Replace with NumPy-compatible column
            data[col] = data[col].fillna(fv).astype(data[col].dtype.numpy_dtype)
        elif isinstance(data[col].dtype, ExtensionDtype):
            if getattr(data[col].dtype, "numpy_dtype", None) is not None:
                data[col] = data[col].astype(data[col].dtype.numpy_dtype)
            elif is_string_dtype(data[col].dtype):
                # TODO could avoid converting string dtype to object here,
                # but handle string dtype in _encode_strings
                data[col] = data[col].astype("object")
                # generate_table checks for None values
                data.loc[data[col].isna(), col] = None

        dtype = data[col].dtype
        empty_df = data.shape[0] == 0
        for c_data in conversion_data:
            if dtype == c_data[0]:
                if empty_df or data[col].max() <= np.iinfo(c_data[1]).max:
                    dtype = c_data[1]
                else:
                    dtype = c_data[2]
                if c_data[2] == np.int64:  # Warn if necessary
                    if data[col].max() >= 2**53:
                        ws = precision_loss_doc.format("uint64", "float64")

                data[col] = data[col].astype(dtype)

        # Check values and upcast if necessary

        if dtype == np.int8 and not empty_df:
            if data[col].max() > 100 or data[col].min() < -127:
                data[col] = data[col].astype(np.int16)
        elif dtype == np.int16 and not empty_df:
            if data[col].max() > 32740 or data[col].min() < -32767:
                data[col] = data[col].astype(np.int32)
        elif dtype == np.int64:
            if empty_df or (
                data[col].max() <= 2147483620 and data[col].min() >= -2147483647
            ):
                data[col] = data[col].astype(np.int32)
            else:
                data[col] = data[col].astype(np.float64)
                if data[col].max() >= 2**53 or data[col].min() <= -(2**53):
                    ws = precision_loss_doc.format("int64", "float64")
        elif dtype in (np.float32, np.float64):
            if np.isinf(data[col]).any():
                raise ValueError(
                    f"Column {col} contains infinity or -infinity"
                    "which is outside the range supported by Stata."
                )
            value = data[col].max()
            if dtype == np.float32 and value > float32_max:
                data[col] = data[col].astype(np.float64)
            elif dtype == np.float64:
                if value > float64_max:
                    raise ValueError(
                        f"Column {col} has a maximum value ({value}) outside the range "
                        f"supported by Stata ({float64_max})"
                    )
        if is_nullable_int:
            if orig_missing.any():
                # Replace missing by Stata sentinel value
                sentinel = StataMissingValue.BASE_MISSING_VALUES[data[col].dtype.name]
                data.loc[orig_missing, col] = sentinel
    if ws:
        warnings.warn(
            ws,
            PossiblePrecisionLoss,
            stacklevel=find_stack_level(),
        )

    return data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py]
    def dta(self, dta_dti):
        dta, dti = dta_dti
        return dta

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::maybe_cast_to_integer_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def maybe_cast_to_integer_array(arr: list | np.ndarray, dtype: np.dtype) -> np.ndarray:
    """
    Takes any dtype and returns the casted version, raising for when data is
    incompatible with integer/unsigned integer dtypes.

    Parameters
    ----------
    arr : np.ndarray or list
        The array to cast.
    dtype : np.dtype
        The integer dtype to cast the array to.

    Returns
    -------
    ndarray
        Array of integer or unsigned integer dtype.

    Raises
    ------
    OverflowError : the dtype is incompatible with the data
    ValueError : loss of precision has occurred during casting

    Examples
    --------
    If you try to coerce negative values to unsigned integers, it raises:

    >>> pd.Series([-1], dtype="uint64")
    Traceback (most recent call last):
        ...
    OverflowError: Trying to coerce negative values to unsigned integers

    Also, if you try to coerce float values to integers, it raises:

    >>> maybe_cast_to_integer_array([1, 2, 3.5], dtype=np.dtype("int64"))
    Traceback (most recent call last):
        ...
    ValueError: Trying to coerce float values to integers
    """
    assert dtype.kind in "iu"

    try:
        if not isinstance(arr, np.ndarray):
            with warnings.catch_warnings():
                # We already disallow dtype=uint w/ negative numbers
                # (test_constructor_coercion_signed_to_unsigned) so safe to ignore.
                warnings.filterwarnings(
                    "ignore",
                    "NumPy will stop allowing conversion of out-of-bound Python int",
                    DeprecationWarning,
                )
                casted = np.asarray(arr, dtype=dtype)
        else:
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=RuntimeWarning)
                casted = arr.astype(dtype, copy=False)
    except OverflowError as err:
        raise OverflowError(
            "The elements provided in the data cannot all be "
            f"casted to the dtype {dtype}"
        ) from err

    if isinstance(arr, np.ndarray) and arr.dtype == dtype:
        # avoid expensive array_equal check
        return casted

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        warnings.filterwarnings(
            "ignore", "elementwise comparison failed", FutureWarning
        )
        if np.array_equal(arr, casted):
            return casted

    # We do this casting to allow for proper
    # data and dtype checking.
    #
    # We didn't do this earlier because NumPy
    # doesn't handle `uint64` correctly.
    arr = np.asarray(arr)

    if np.issubdtype(arr.dtype, str):
        # TODO(numpy-2.0 min): This case will raise an OverflowError above
        if (casted.astype(str) == arr).all():
            return casted
        raise ValueError(f"string values cannot be losslessly cast to {dtype}")

    if dtype.kind == "u" and (arr < 0).any():
        # TODO: can this be hit anymore after numpy 2.0?
        raise OverflowError("Trying to coerce negative values to unsigned integers")

    if arr.dtype.kind == "f":
        if not np.isfinite(arr).all():
            raise IntCastingNaNError(
                "Cannot convert non-finite values (NA or inf) to integer"
            )
        raise ValueError("Trying to coerce float values to integers")
    if arr.dtype == object:
        raise ValueError("Trying to coerce object values to integers")

    if casted.dtype < arr.dtype:
        # TODO: Can this path be hit anymore with numpy > 2
        # GH#41734 e.g. [1, 200, 923442] and dtype="int8" -> overflows
        raise ValueError(
            f"Values are too large to be losslessly converted to {dtype}. "
            f"To cast anyway, use pd.Series(values).astype({dtype})"
        )

    if arr.dtype.kind in "mM":
        # test_constructor_maskedarray_nonfloat
        raise TypeError(
            f"Constructing a Series or DataFrame from {arr.dtype} values and "
            f"dtype={dtype} is not supported. Use values.view({dtype}) instead."
        )

    # No known cases that get here, but raising explicitly to cover our bases.
    raise ValueError(f"values cannot be losslessly cast to {dtype}")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/floating.py::FloatingDtype._safe_cast [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/floating.py]
    def _safe_cast(cls, values: np.ndarray, dtype: np.dtype, copy: bool) -> np.ndarray:
        """
        Safely cast the values to the given dtype.

        "safe" in this context means the casting is lossless.
        """
        # This is really only here for compatibility with IntegerDtype
        # Here for compat with IntegerDtype
        return values.astype(dtype, copy=copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._add_timedeltalike_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _add_timedeltalike_scalar(self, other):
        """
        Add a delta of a timedeltalike

        Returns
        -------
        Same type as self
        """
        if isna(other):
            # i.e np.timedelta64("NaT")
            new_values = np.empty(self.shape, dtype="i8").view(self._ndarray.dtype)
            new_values.fill(iNaT)
            return type(self)._simple_new(new_values, dtype=self.dtype)

        # PeriodArray overrides, so we only get here with DTA/TDA
        self = cast("DatetimeArray | TimedeltaArray", self)
        other = Timedelta(other)
        self, other = self._ensure_matching_resos(other)
        return self._add_timedeltalike(other)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestInsertIndexCoercion._assert_insert_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py]
    def _assert_insert_conversion(self, original, value, expected, expected_dtype):
        """test coercion triggered by insert"""
        target = original.copy()
        res = target.insert(1, value)
        tm.assert_index_equal(res, expected)
        assert res.dtype == expected_dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::TestMaskedArrays._cast_pointwise_result [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py]
    def _cast_pointwise_result(self, op_name: str, obj, other, pointwise_result):
        sdtype = tm.get_dtype(obj)
        expected = pointwise_result

        if sdtype.kind == "b":
            if op_name in (
                "__mod__",
                "__rmod__",
            ):
                # combine keeps boolean type
                expected = expected.astype("Int8")

        return expected

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py]
    def insert(self, loc: int, item) -> Self:
        if not is_valid_na_for_dtype(item, self.dtype):
            self._validate_setitem_value(item)
        return super().insert(loc, item)
```
