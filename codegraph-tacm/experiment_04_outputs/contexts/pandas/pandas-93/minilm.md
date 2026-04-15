# pandas-93 :: minilm

query: BUG: DTI/TDI/PI `where` accepting non-matching dtypes (#30791)

## selected nodes

- rank=1 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py
- rank=2 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsIn.time_isin_mismatched_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py
- rank=3 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py::any_dtype_for_small_pos_integer_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py
- rank=4 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::maybe_downcast_to_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=5 layer=FUNCTION tokens=756 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.coerce_to_target_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=6 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::TimedeltaArray._validate_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=7 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::validate_dtype_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=8 layer=FUNCTION tokens=348 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_FrequencyInferer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py
- rank=9 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::complex_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=10 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::ensure_dtype_can_hold_na file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=11 layer=FUNCTION tokens=138 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::interleaved_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=12 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_require_matching_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=13 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_ensure_dtype_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=14 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py::is_1d_only_ea_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py
- rank=15 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_na_ok_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py
- rank=16 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::NumpyEADtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=17 layer=FUNCTION tokens=157 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::any_numeric_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=18 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._is_comparable_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=19 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::any_int_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=20 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_dtype_can_hold_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=21 layer=FUNCTION tokens=237 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.dtype_predicate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=22 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Table.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py]
def _is_dt_or_td(dtype: DtypeObj) -> bool:
    # Note: the dtype here comes from an Index.dtype, so we know that any
    #  dt64/td64 dtype is of a supported unit.
    return isinstance(dtype, DatetimeTZDtype) or lib.is_np_dtype(dtype, "mM")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsIn.time_isin_mismatched_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py]
    def time_isin_mismatched_dtype(self, dtype):
        self.series.isin(self.mismatched)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py::any_dtype_for_small_pos_integer_indexes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py]
def any_dtype_for_small_pos_integer_indexes(request):
    """
    Dtypes that can be given to an Index with small positive integers.

    This means that for any dtype `x` in the params list, `Index([1, 2, 3], dtype=x)` is
    valid and gives the correct Index (sub-)class.
    """
    return request.param

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.coerce_to_target_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def coerce_to_target_dtype(self, other, raise_on_upcast: bool) -> Block:
        """
        coerce the current block to a dtype compat for other
        we will return a block, possibly object, and not raise

        we can also safely try to coerce to the same dtype
        and will receive the same block
        """
        new_dtype = find_result_type(self.values.dtype, other)
        if new_dtype == self.dtype:
            if lib.is_np_dtype(new_dtype, "mM"):
                # GH#61671 e.g. datetime64[ns] column and a replacement value
                # outside ns range. find_common_type picked the highest
                # resolution which can't represent the value.
                raise OutOfBoundsDatetime(
                    f"Incompatible (high-resolution) value for "
                    f"dtype='{self.dtype}'. "
                    "Explicitly cast before operating."
                )
            # GH#52927 avoid RecursionError
            raise AssertionError(
                "Something has gone wrong, please report a bug at "
                "https://github.com/pandas-dev/pandas/issues"
            )

        # In a future version of pandas, the default will be that
        # setting `nan` into an integer series won't raise.
        if (
            is_scalar(other)
            and is_integer_dtype(self.values.dtype)
            and isna(other)
            and other is not NaT
            and not (
                isinstance(other, (np.datetime64, np.timedelta64)) and np.isnat(other)
            )
        ):
            raise_on_upcast = False
        elif (
            isinstance(other, np.ndarray)
            and other.ndim == 1
            and is_integer_dtype(self.values.dtype)
            and is_float_dtype(other.dtype)
            and lib.has_only_ints_or_nan(other)
        ):
            raise_on_upcast = False

        if raise_on_upcast:
            raise TypeError(f"Invalid value '{other}' for dtype '{self.values.dtype}'")
        if self.values.dtype == new_dtype:
            raise AssertionError(
                f"Did not expect new dtype {new_dtype} to equal self.dtype "
                f"{self.values.dtype}. Please report a bug at "
                "https://github.com/pandas-dev/pandas/issues."
            )
        try:
            return self.astype(new_dtype)
        except OutOfBoundsDatetime as err:
            # e.g. GH#56419 if self.dtype is a low-resolution dt64 and we try to
            #  upcast to a higher-resolution dt64, we may have entries that are
            #  out of bounds for the higher resolution.
            #  Re-raise with a more informative message.
            raise OutOfBoundsDatetime(
                f"Incompatible (high-resolution) value for dtype='{self.dtype}'. "
                "Explicitly cast before operating."
            ) from err

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::TimedeltaArray._validate_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py]
    def _validate_dtype(cls, values, dtype):
        # used in TimeLikeOps.__init__
        dtype = _validate_td64_dtype(dtype)
        _validate_td64_dtype(values.dtype)
        if dtype != values.dtype:
            raise ValueError("Values resolution does not match dtype.")
        return dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::validate_dtype_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
def validate_dtype_freq(
    dtype: DtypeObj | None, dtype2: DtypeObj | None
) -> PeriodDtype | None:
    """
    If a dtype is specified both directly and indirectly via a `freq` (dtype2),
    ensure they match. If only the latter is available, return the indirect dtype.

    Parameters
    ----------
    dtype : dtype
    dtype2 : PeriodDtype or None
        Dtype derived from a `freq` passed to the caller.

    Returns
    -------
    PeriodDtype or None

    Raises
    ------
    ValueError : non-period dtype
    IncompatibleFrequency : mismatch between dtype and freq
    """
    if dtype is not None:
        if not isinstance(dtype, PeriodDtype):
            raise ValueError("dtype must be PeriodDtype")
        if dtype2 is not None and dtype != dtype2:
            raise IncompatibleFrequency("specified freq and dtype are different")

    elif dtype2 is not None:
        if not isinstance(dtype2, PeriodDtype):
            raise ValueError("dtype must be PeriodDtype")
        dtype = dtype2

    return dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_FrequencyInferer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py]
    def __init__(self, index) -> None:
        self.index = index
        self.i8values = index.asi8

        # For get_unit_from_dtype we need the dtype to the underlying ndarray,
        #  which for tz-aware is not the same as index.dtype
        if isinstance(index, ABCIndex):
            # error: Item "ndarray[Any, Any]" of "Union[ExtensionArray,
            # ndarray[Any, Any]]" has no attribute "_ndarray"
            self._creso = get_unit_from_dtype(
                index._data._ndarray.dtype  # type: ignore[union-attr]
            )
        else:
            # otherwise we have DTA/TDA
            self._creso = get_unit_from_dtype(index._ndarray.dtype)

        # This moves the values, which are implicitly in UTC, to the
        # the timezone so they are in local time
        if hasattr(index, "tz"):
            if index.tz is not None:
                self.i8values = tz_convert_from_utc(
                    self.i8values, index.tz, reso=self._creso
                )

        if len(index) < 3:
            raise ValueError("Need at least 3 dates to infer frequency")

        self.is_monotonic = (
            self.index._is_monotonic_increasing or self.index._is_monotonic_decreasing
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::complex_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def complex_dtype(request):
    """
    Parameterized fixture for complex dtypes.

    * complex
    * 'complex64'
    * 'complex128'
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::ensure_dtype_can_hold_na [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def ensure_dtype_can_hold_na(dtype: DtypeObj) -> DtypeObj:
    """
    If we have a dtype that cannot hold NA values, find the best match that can.
    """
    if isinstance(dtype, ExtensionDtype):
        if dtype._can_hold_na:
            return dtype
        elif isinstance(dtype, IntervalDtype):
            # TODO(GH#45349): don't special-case IntervalDtype, allow
            #  overriding instead of returning object below.
            return IntervalDtype(np.float64, closed=dtype.closed)
        return _dtype_obj
    elif dtype.kind == "b":
        return _dtype_obj
    elif dtype.kind in "iu":
        return np.dtype(np.float64)
    return dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::interleaved_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
def interleaved_dtype(dtypes: list[DtypeObj]) -> DtypeObj | None:
    """
    Find the common dtype for `blocks`.

    Parameters
    ----------
    blocks : List[DtypeObj]

    Returns
    -------
    dtype : np.dtype, ExtensionDtype, or None
        None is returned when `blocks` is empty.
    """
    if not len(dtypes):
        return None

    return find_common_type(dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_require_matching_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _maybe_require_matching_dtypes(
        self, left_join_keys: list[ArrayLike], right_join_keys: list[ArrayLike]
    ) -> None:
        # Overridden by AsOfMerge
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_ensure_dtype_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def _ensure_dtype_type(value: Any, dtype: np.dtype) -> Any:
    """
    Ensure that the given value is an instance of the given dtype.

    e.g. if out dtype is np.complex64_, we should have an instance of that
    as opposed to a python complex object.

    Parameters
    ----------
    value : object
    dtype : np.dtype

    Returns
    -------
    object
    """
    # Start with exceptions in which we do _not_ cast to numpy types

    if dtype == _dtype_obj:
        return value

    # Note: before we get here we have already excluded isna(value)
    return dtype.type(value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py::is_1d_only_ea_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py]
def is_1d_only_ea_dtype(dtype: DtypeObj | None) -> bool:
    """
    Analogue to is_extension_array_dtype but excluding DatetimeTZDtype.
    """
    return isinstance(dtype, ExtensionDtype) and not dtype._supports_2d

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_na_ok_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py]
def _na_ok_dtype(dtype: DtypeObj) -> bool:
    if needs_i8_conversion(dtype):
        return False
    return not issubclass(dtype.type, np.integer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::NumpyEADtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        from pandas.core.dtypes.cast import find_common_type

        dtypes = [x.numpy_dtype if isinstance(x, NumpyEADtype) else x for x in dtypes]
        if not all(isinstance(x, np.dtype) for x in dtypes):
            return None

        common_dtype = find_common_type(dtypes)
        # error: Argument 1 to "NumpyEADtype" has incompatible type
        return NumpyEADtype(common_dtype)  # type: ignore[arg-type]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::any_numeric_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def any_numeric_dtype(request):
    """
    Parameterized fixture for all numeric dtypes.

    * int
    * 'int8'
    * 'uint8'
    * 'int16'
    * 'uint16'
    * 'int32'
    * 'uint32'
    * 'int64'
    * 'uint64'
    * float
    * 'float32'
    * 'float64'
    * complex
    * 'complex64'
    * 'complex128'
    * 'UInt8'
    * 'Int8'
    * 'UInt16'
    * 'Int16'
    * 'UInt32'
    * 'Int32'
    * 'UInt64'
    * 'Int64'
    * 'Float32'
    * 'Float64'
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._is_comparable_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
    def _is_comparable_dtype(self, dtype: DtypeObj) -> bool:
        if not isinstance(dtype, IntervalDtype):
            return False
        common_subtype = find_common_type([self.dtype, dtype])
        return not is_object_dtype(common_subtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::any_int_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def any_int_dtype(request):
    """
    Parameterized fixture for any nullable integer dtype.

    * int
    * 'int8'
    * 'uint8'
    * 'int16'
    * 'uint16'
    * 'int32'
    * 'uint32'
    * 'int64'
    * 'uint64'
    * 'UInt8'
    * 'Int8'
    * 'UInt16'
    * 'Int16'
    * 'UInt32'
    * 'Int32'
    * 'UInt64'
    * 'Int64'
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_dtype_can_hold_range [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def _dtype_can_hold_range(rng: range, dtype: np.dtype) -> bool:
    """
    _maybe_infer_dtype_type infers to int64 (and float64 for very large endpoints),
    but in many cases a range can be held by a smaller integer dtype.
    Check if this is one of those cases.
    """
    if not len(rng):
        return True
    return np_can_cast_scalar(rng.start, dtype) and np_can_cast_scalar(rng.stop, dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.dtype_predicate [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
        def dtype_predicate(dtype: DtypeObj, dtypes_set) -> bool:
            # GH 46870: BooleanDtype._is_numeric == True but should be excluded
            dtype = dtype if not isinstance(dtype, ArrowDtype) else dtype.numpy_dtype
            return (
                issubclass(dtype.type, tuple(dtypes_set))
                or (
                    np.number in dtypes_set
                    and getattr(dtype, "_is_numeric", False)
                    and not is_bool_dtype(dtype)
                )
                # backwards compat for the default `str` dtype being selected by object
                or (
                    isinstance(dtype, StringDtype)
                    and dtype.na_value is np.nan
                    and np.object_ in dtypes_set
                )
            )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Table.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def dtype(self):
        return self.table.dtype
```
