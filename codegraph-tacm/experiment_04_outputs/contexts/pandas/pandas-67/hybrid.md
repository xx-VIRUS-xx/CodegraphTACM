# pandas-67 :: hybrid

query: BUG: Block.iget not wrapping timedelta64/datetime64 (#31666)

## selected nodes

- rank=1 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._sub_nat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=2 layer=FUNCTION tokens=756 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.coerce_to_target_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=3 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::timedelta64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=4 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::ensure_wrapped_if_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=5 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_validate_td64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=6 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_maybe_unbox_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=7 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.inferred_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=8 layer=FUNCTION tokens=292 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::TimedeltaArray.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=9 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/missing.py::_datetimelike_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/missing.py
- rank=10 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::DateInferOps.time_timedelta_plus_datetime file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=11 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::datetime64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=12 layer=FUNCTION tokens=461 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=13 layer=FUNCTION tokens=346 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py::_make_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py
- rank=14 layer=FUNCTION tokens=254 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=15 layer=FUNCTION tokens=419 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_ensure_nanosecond_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._sub_nat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _sub_nat(self) -> np.ndarray:
        """
        Subtract pd.NaT from self
        """
        # GH#19124 Timedelta - datetime is not in general well-defined.
        # We make an exception for pd.NaT, which in this case quacks
        # like a timedelta.
        # For datetime64 dtypes by convention we treat NaT as a datetime, so
        # this subtraction returns a timedelta64 dtype.
        # For period dtype, timedelta64 is a close-enough return dtype.
        result = np.empty(self.shape, dtype=np.int64)
        result.fill(iNaT)
        if self.dtype.kind in "mM":
            # We can retain unit in dtype
            self = cast("DatetimeArray| TimedeltaArray", self)
            return result.view(f"timedelta64[{self.unit}]")
        else:
            return result.view("timedelta64[ns]")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::timedelta64_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def timedelta64_dtype(request):
    """
    Parametrized fixture for timedelta64 dtypes.

    * 'timedelta64[ns]'
    * 'm8[ns]'
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::ensure_wrapped_if_datetimelike [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py]
def ensure_wrapped_if_datetimelike(arr):
    """
    Wrap datetime64 and timedelta64 ndarrays in DatetimeArray/TimedeltaArray.
    """
    if isinstance(arr, np.ndarray):
        if arr.dtype.kind == "M":
            from pandas.core.arrays import DatetimeArray

            dtype = get_supported_dtype(arr.dtype)
            return DatetimeArray._from_sequence(arr, dtype=dtype)

        elif arr.dtype.kind == "m":
            from pandas.core.arrays import TimedeltaArray

            dtype = get_supported_dtype(arr.dtype)
            return TimedeltaArray._from_sequence(arr, dtype=dtype)

    return arr

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_validate_td64_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py]
def _validate_td64_dtype(dtype) -> DtypeObj:
    dtype = pandas_dtype(dtype)
    if dtype == np.dtype("m8"):
        # no precision disallowed GH#24806
        msg = (
            "Passing in 'timedelta' dtype with no precision is not allowed. "
            "Please pass in 'timedelta64[ns]' instead."
        )
        raise ValueError(msg)

    if not lib.is_np_dtype(dtype, "m"):
        raise ValueError(f"dtype '{dtype}' is invalid, should be np.timedelta64 dtype")
    elif not is_supported_dtype(dtype):
        raise ValueError("Supported timedelta64 resolutions are 's', 'ms', 'us', 'ns'")

    return dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_maybe_unbox_datetimelike [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def _maybe_unbox_datetimelike(value: Scalar, dtype: DtypeObj) -> Scalar:
    """
    Convert a Timedelta or Timestamp to timedelta64 or datetime64 for setting
    into a numpy array.  Failing to unbox would risk dropping nanoseconds.

    Notes
    -----
    Caller is responsible for checking dtype.kind in "mM"
    """
    if is_valid_na_for_dtype(value, dtype):
        # GH#36541: can't fill array directly with pd.NaT
        # > np.empty(10, dtype="datetime64[ns]").fill(pd.NaT)
        # ValueError: cannot convert float NaN to integer
        value = dtype.type("NaT", "ns")
    elif isinstance(value, Timestamp):
        if value.tz is None:
            value = value.to_datetime64()
        elif not isinstance(dtype, DatetimeTZDtype):
            raise TypeError("Cannot unbox tzaware Timestamp to tznaive dtype")
    elif isinstance(value, Timedelta):
        value = value.to_timedelta64()

    _disallow_mismatched_datetimelike(value, dtype)
    return value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.inferred_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py]
    def inferred_type(self) -> str:
        return "timedelta64"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::TimedeltaArray.astype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py]
    def astype(self, dtype, copy: bool = True):
        # We handle
        #   --> timedelta64[ns]
        #   --> timedelta64
        # DatetimeLikeArrayMixin super call handles other cases
        dtype = pandas_dtype(dtype)

        if lib.is_np_dtype(dtype, "m"):
            if dtype == self.dtype:
                if copy:
                    return self.copy()
                return self

            if is_supported_dtype(dtype):
                # unit conversion e.g. timedelta64[s]
                res_values = astype_overflowsafe(self._ndarray, dtype, copy=False)
                return type(self)._simple_new(
                    res_values, dtype=res_values.dtype, freq=self.freq
                )
            else:
                raise ValueError(
                    f"Cannot convert from {self.dtype} to {dtype}. "
                    "Supported resolutions are 's', 'ms', 'us', 'ns'"
                )

        return dtl.DatetimeLikeArrayMixin.astype(self, dtype, copy=copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/missing.py::_datetimelike_compat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/missing.py]
def _datetimelike_compat(func: F) -> F:
    """
    Wrapper to handle datetime64 and timedelta64 dtypes.
    """

    @wraps(func)
    def new_func(
        values,
        limit: int | None = None,
        limit_area: Literal["inside", "outside"] | None = None,
        mask=None,
    ):
        if needs_i8_conversion(values.dtype):
            if mask is None:
                # This needs to occur before casting to int64
                mask = isna(values)

            result, mask = func(
                values.view("i8"), limit=limit, limit_area=limit_area, mask=mask
            )
            return result.view(values.dtype), mask

        return func(values, limit=limit, limit_area=limit_area, mask=mask)

    return cast("F", new_func)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::DateInferOps.time_timedelta_plus_datetime [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_timedelta_plus_datetime(self, df):
        df["timedelta"] + df["datetime64"]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::datetime64_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def datetime64_dtype(request):
    """
    Parametrized fixture for datetime64 dtypes.

    * 'datetime64[ns]'
    * 'M8[ns]'
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _values(self):
        """
        Return the internal repr of this data (defined by Block.interval_values).
        This are the values as stored in the Block (ndarray or ExtensionArray
        depending on the Block class), with datetime64[ns] and timedelta64[ns]
        wrapped in ExtensionArrays to match Index._values behavior.

        Differs from the public ``.values`` for certain data types, because of
        historical backwards compatibility of the public attribute (e.g. period
        returns object ndarray and datetimetz a datetime64[ns] ndarray for
        ``.values`` while it returns an ExtensionArray for ``._values`` in those
        cases).

        Differs from ``.array`` in that this still returns the numpy array if
        the Block is backed by a numpy array (except for datetime64 and
        timedelta64 dtypes), while ``.array`` ensures to always return an
        ExtensionArray.

        Overview:

        dtype       | values        | _values       | array                 |
        ----------- | ------------- | ------------- | --------------------- |
        Numeric     | ndarray       | ndarray       | NumpyExtensionArray   |
        Category    | Categorical   | Categorical   | Categorical           |
        dt64[ns]    | ndarray[M8ns] | DatetimeArray | DatetimeArray         |
        dt64[ns tz] | ndarray[M8ns] | DatetimeArray | DatetimeArray         |
        td64[ns]    | ndarray[m8ns] | TimedeltaArray| TimedeltaArray        |
        Period      | ndarray[obj]  | PeriodArray   | PeriodArray           |
        Nullable    | EA            | EA            | EA                    |

        """
        return self._mgr.internal_values()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py::_make_block [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py]
def _make_block(values: ArrayLike, placement: np.ndarray) -> Block:
    """
    This is an analogue to blocks.new_block(_2d) that ensures:
    1) correct dimension for EAs that support 2D (`ensure_block_shape`), and
    2) correct EA class for datetime64/timedelta64 (`maybe_coerce_values`).

    The input `values` is assumed to be either numpy array or ExtensionArray:
    - In case of a numpy array, it is assumed to already be in the expected
      shape for Blocks (2D, (cols, rows)).
    - In case of an ExtensionArray the input can be 1D, also for EAs that are
      internally stored as 2D.

    For the rest no preprocessing or validation is done, except for those dtypes
    that are internally stored as EAs but have an exact numpy equivalent (and at
    the moment use that numpy dtype), i.e. datetime64/timedelta64.
    """
    dtype = values.dtype
    klass = get_block_type(dtype)
    placement_obj = BlockPlacement(placement)

    if (isinstance(dtype, ExtensionDtype) and dtype._supports_2d) or isinstance(
        values, (DatetimeArray, TimedeltaArray)
    ):
        values = ensure_block_shape(values, ndim=2)

    values = maybe_coerce_values(values)
    return klass(values, ndim=2, placement=placement_obj)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def __init__(
        self,
        blocks: Sequence[Block],
        axes: Sequence[Index],
        verify_integrity: bool = True,
    ) -> None:
        if verify_integrity:
            # Assertion disabled for performance
            # assert all(isinstance(x, Index) for x in axes)

            for block in blocks:
                if self.ndim != block.ndim:
                    raise AssertionError(
                        f"Number of Block dimensions ({block.ndim}) must equal "
                        f"number of axes ({self.ndim})"
                    )
                # As of 2.0, the caller is responsible for ensuring that
                #  DatetimeTZBlock with block.ndim == 2 has block.values.ndim ==2;
                #  previously there was a special check for fastparquet compat.

            self._verify_integrity()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_ensure_nanosecond_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def _ensure_nanosecond_dtype(dtype: DtypeObj) -> None:
    """
    Convert dtypes with granularity less than nanosecond to nanosecond

    >>> _ensure_nanosecond_dtype(np.dtype("M8[us]"))

    >>> _ensure_nanosecond_dtype(np.dtype("M8[D]"))
    Traceback (most recent call last):
        ...
    TypeError: dtype=datetime64[D] is not supported. Supported resolutions are 's', 'ms', 'us', and 'ns'

    >>> _ensure_nanosecond_dtype(np.dtype("m8[ps]"))
    Traceback (most recent call last):
        ...
    TypeError: dtype=timedelta64[ps] is not supported. Supported resolutions are 's', 'ms', 'us', and 'ns'
    """  # noqa: E501
    msg = (
        f"The '{dtype.name}' dtype has no unit. "
        f"Please pass in '{dtype.name}[ns]' instead."
    )

    # unpack e.g. SparseDtype
    dtype = getattr(dtype, "subtype", dtype)

    if not isinstance(dtype, np.dtype):
        # i.e. datetime64tz
        pass

    elif dtype.kind in "mM":
        if not is_supported_dtype(dtype):
            # pre-2.0 we would silently swap in nanos for lower-resolutions,
            #  raise for above-nano resolutions
            if dtype.name in ["datetime64", "timedelta64"]:
                raise ValueError(msg)
            # TODO: ValueError or TypeError? existing test
            #  test_constructor_generic_timestamp_bad_frequency expects TypeError
            raise TypeError(
                f"dtype={dtype} is not supported. Supported resolutions are 's', "
                "'ms', 'us', and 'ns'"
            )
```
