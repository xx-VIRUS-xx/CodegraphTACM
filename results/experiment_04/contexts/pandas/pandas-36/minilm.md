# pandas-36 :: minilm

query: BUG: isna_old with td64, dt64tz, period (#33158)

## selected nodes

- rank=1 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimeDT64ArrToPeriodArr.time_dt64arr_to_periodarr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=2 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimePeriodArrToDT64Arr.time_periodarray_to_dt64arr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=3 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._convert_tolerance file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=4 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._from_datetime64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=5 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.dt64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
- rank=6 layer=FUNCTION tokens=344 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::dt64arr_to_periodarr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=7 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_validate_td64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=8 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::mismatched_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py
- rank=9 layer=FUNCTION tokens=499 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::_validate_dt64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=10 layer=FUNCTION tokens=419 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_ints_to_td64ns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=11 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
- rank=12 layer=FUNCTION tokens=254 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._decode file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=13 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::is_extension_array_dtype_and_needs_i8_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py
- rank=14 layer=FUNCTION tokens=354 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataStrLWriter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=15 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::int64ToIsoDuration file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c
- rank=16 layer=FUNCTION tokens=137 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyTimeDeltaToIsoCallback file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=17 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py
- rank=18 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyDateTimeToIsoCallback file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=19 layer=FUNCTION tokens=326 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=20 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Isna.time_isna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimeDT64ArrToPeriodArr.time_dt64arr_to_periodarr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def time_dt64arr_to_periodarr(self, size, freq, tz):
        dt64arr_to_periodarr(self.i8values, freq, tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimePeriodArrToDT64Arr.time_periodarray_to_dt64arr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def time_periodarray_to_dt64arr(self, size, freq):
        periodarr_to_dt64arr(self.i8values, freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._convert_tolerance [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
    def _convert_tolerance(self, tolerance, target):
        # Returned tolerance must be in dtype/units so that
        #  `|self._get_engine_target() - target._engine_target()| <= tolerance`
        #  is meaningful.  Since PeriodIndex returns int64 for engine_target,
        #  we may need to convert timedelta64 tolerance to int64.
        tolerance = super()._convert_tolerance(tolerance, target)

        if self.dtype == target.dtype:
            # convert tolerance to i8
            tolerance = self._maybe_convert_timedelta(tolerance)

        return tolerance

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._from_datetime64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def _from_datetime64(cls, data, freq, tz=None) -> Self:
        """
        Construct a PeriodArray from a datetime64 array

        Parameters
        ----------
        data : ndarray[datetime64[ns], datetime64[ns, tz]]
        freq : str or Tick
        tz : tzinfo, optional

        Returns
        -------
        PeriodArray[freq]
        """
        if isinstance(freq, BaseOffset):
            freq = PeriodDtype(freq)._freqstr
        data, freq = dt64arr_to_periodarr(data, freq, tz)
        dtype = PeriodDtype(freq)
        return cls(data, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.dt64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py]
    def dt64(self, reso):
        # cases that are in-bounds for nanosecond, so we can compare against
        #  the existing implementation.
        return np.datetime64("2016-01-01", reso)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::dt64arr_to_periodarr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
def dt64arr_to_periodarr(
    data, freq, tz=None
) -> tuple[npt.NDArray[np.int64], BaseOffset]:
    """
    Convert a datetime-like array to values Period ordinals.

    Parameters
    ----------
    data : Union[Series[datetime64[ns]], DatetimeIndex, ndarray[datetime64ns]]
    freq : Optional[Union[str, Tick]]
        Must match the `freq` on the `data` if `data` is a DatetimeIndex
        or Series.
    tz : Optional[tzinfo]

    Returns
    -------
    ordinals : ndarray[int64]
    freq : Tick
        The frequency extracted from the Series or DatetimeIndex if that's
        used.

    """
    if not isinstance(data.dtype, np.dtype) or data.dtype.kind != "M":
        raise ValueError(f"Wrong dtype: {data.dtype}")

    if freq is None:
        if isinstance(data, ABCIndex):
            data, freq = data._values, data.freq
        elif isinstance(data, ABCSeries):
            data, freq = data._values, data.dt.freq

    elif isinstance(data, (ABCIndex, ABCSeries)):
        data = data._values

    reso = get_unit_from_dtype(data.dtype)
    freq = Period._maybe_convert_freq(freq)
    base = freq._period_dtype_code
    return c_dt64arr_to_periodarr(data.view("i8"), base, tz, reso=reso), freq

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::mismatched_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py]
def mismatched_freq(request):
    """
    Several timedelta-like and DateOffset instances that are _not_
    compatible with Monthly or Annual frequencies.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::_validate_dt64_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py]
def _validate_dt64_dtype(dtype):
    """
    Check that a dtype, if passed, represents either a numpy datetime64[ns]
    dtype or a pandas DatetimeTZDtype.

    Parameters
    ----------
    dtype : object

    Returns
    -------
    dtype : None, numpy.dtype, or DatetimeTZDtype

    Raises
    ------
    ValueError : invalid dtype

    Notes
    -----
    Unlike _validate_tz_from_dtype, this does _not_ allow non-existent
    tz errors to go through
    """
    if dtype is not None:
        dtype = pandas_dtype(dtype)
        if dtype == np.dtype("M8"):
            # no precision, disallowed GH#24806
            msg = (
                "Passing in 'datetime64' dtype with no precision is not allowed. "
                "Please pass in 'datetime64[ns]' instead."
            )
            raise ValueError(msg)

        if (
            isinstance(dtype, np.dtype)
            and (dtype.kind != "M" or not is_supported_dtype(dtype))
        ) or not isinstance(dtype, (np.dtype, DatetimeTZDtype)):
            raise ValueError(
                f"Unexpected value for 'dtype': '{dtype}'. "
                "Must be 'datetime64[s]', 'datetime64[ms]', 'datetime64[us]', "
                "'datetime64[ns]' or DatetimeTZDtype'."
            )

        if getattr(dtype, "tz", None):
            # https://github.com/pandas-dev/pandas/issues/18595
            # Ensure that we have a standard timezone for pytz objects.
            # Without this, things like adding an array of timedeltas and
            # a  tz-aware Timestamp (with a tz specific to its datetime) will
            # be incorrect(ish?) for the array as a whole
            dtype = cast("DatetimeTZDtype", dtype)
            dtype = DatetimeTZDtype(
                unit=dtype.unit, tz=timezones.tz_standardize(dtype.tz)
            )

    return dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_ints_to_td64ns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py]
def _ints_to_td64ns(data, unit: str = "ns") -> tuple[np.ndarray, bool]:
    """
    Convert an ndarray with integer-dtype to timedelta64[ns] dtype, treating
    the integers as multiples of the given timedelta unit.

    Parameters
    ----------
    data : numpy.ndarray with integer-dtype
    unit : str, default "ns"
        The timedelta unit to treat integers as multiples of.

    Returns
    -------
    numpy.ndarray : timedelta64[ns] array converted from data
    bool : whether a copy was made
    """
    copy_made = False
    unit = unit if unit is not None else "ns"

    if data.dtype != np.int64:
        # GH#60677 unsigned integers > int64 max overflow silently
        # when cast to int64 (which timedelta64 is backed by)
        if data.dtype == np.dtype("uint64") and (data > np.iinfo(np.int64).max).any():
            raise OutOfBoundsTimedelta(f"Cannot convert input with unit '{unit}'")
        # converting to int64 makes a copy, so we can avoid
        # re-copying later
        data = data.astype(np.int64)
        copy_made = True

    if unit != "ns":
        dtype_str = f"timedelta64[{unit}]"
        data = data.view(dtype_str)

        new_dtype = get_supported_dtype(data.dtype)
        if new_dtype != data.dtype:
            data = astype_overflowsafe(data, dtype=new_dtype)

            # the astype conversion makes a copy, so we can avoid re-copying later
            copy_made = True

    else:
        data = data.view("timedelta64[ns]")

    return data, copy_made

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py]
    def ts(self, dt64):
        return Timestamp._from_dt64(dt64)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._decode [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py]
    def _decode(self, s: bytes) -> str:
        # have bytes not strings, so must decode
        s = s.partition(b"\0")[0]
        try:
            return s.decode(self._encoding)
        except UnicodeDecodeError:
            # GH 25960, fallback to handle incorrect format produced when 117
            # files are converted to 118 files in Stata
            encoding = self._encoding
            msg = f"""
One or more strings in the dta file could not be decoded using {encoding}, and
so the fallback encoding of latin-1 is being used.  This can happen when a file
has been incorrectly encoded by Stata or some other software. You should verify
the string values returned are correct."""
            warnings.warn(
                msg,
                UnicodeWarning,
                stacklevel=find_stack_level(),
            )
            return s.decode("latin-1")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::is_extension_array_dtype_and_needs_i8_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py]
def is_extension_array_dtype_and_needs_i8_conversion(
    left_dtype: DtypeObj, right_dtype: DtypeObj
) -> bool:
    """
    Checks that we have the combination of an ExtensionArraydtype and
    a dtype that should be converted to int64

    Returns
    -------
    bool

    Related to issue #37609
    """
    return isinstance(left_dtype, ExtensionDtype) and needs_i8_conversion(right_dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataStrLWriter.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py]
    def __init__(
        self,
        df: DataFrame,
        columns: Sequence[str],
        version: int = 117,
        byteorder: str | None = None,
    ) -> None:
        if version not in (117, 118, 119):
            raise ValueError("Only dta versions 117, 118 and 119 supported")
        self._dta_ver = version

        self.df = df
        self.columns = columns
        self._gso_table = {"": (0, 0)}
        if byteorder is None:
            byteorder = sys.byteorder
        self._byteorder = _set_endianness(byteorder)
        # Flag whether chosen byteorder matches the system on which we're running
        self._native_byteorder = self._byteorder == _set_endianness(sys.byteorder)

        gso_v_type = "I"  # uint32
        gso_o_type = "Q"  # uint64
        self._encoding = "utf-8"
        if version == 117:
            o_size = 4
            gso_o_type = "I"  # 117 used uint32
            self._encoding = "latin-1"
        elif version == 118:
            o_size = 6
        else:  # version == 119
            o_size = 5
        if self._native_byteorder:
            self._o_offet = 2 ** (8 * (8 - o_size))
        else:
            self._o_offet = 2 ** (8 * o_size)
        self._gso_o_type = gso_o_type
        self._gso_v_type = gso_v_type

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::int64ToIsoDuration [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c]
char *int64ToIsoDuration(int64_t value, NPY_DATETIMEUNIT valueUnit,
                         size_t *len) {
  pandas_timedeltastruct tds;
  int ret_code;

  pandas_timedelta_to_timedeltastruct(value, valueUnit, &tds);

  // Max theoretical length of ISO Duration with 64 bit day
  // as the largest unit is 70 characters + 1 for a null terminator
  char *result = PyObject_Malloc(71);
  if (result == NULL) {
    PyErr_NoMemory();
    return NULL;
  }

  ret_code = make_iso_8601_timedelta(&tds, result, len);
  if (ret_code == -1) {
    PyErr_SetString(PyExc_ValueError,
                    "Could not convert timedelta value to string");
    PyObject_Free(result);
    return NULL;
  }

  return result;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyTimeDeltaToIsoCallback [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *NpyTimeDeltaToIsoCallback(JSOBJ Py_UNUSED(unused),
                                             JSONTypeContext *tc, size_t *len) {
  NPY_DATETIMEUNIT valueUnit = ((PyObjectEncoder *)tc->encoder)->valueUnit;
  GET_TC(tc)->cStr = int64ToIsoDuration(GET_TC(tc)->longValue, valueUnit, len);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py]
def _is_dt_or_td(dtype: DtypeObj) -> bool:
    # Note: the dtype here comes from an Index.dtype, so we know that any
    #  dt64/td64 dtype is of a supported unit.
    return isinstance(dtype, DatetimeTZDtype) or lib.is_np_dtype(dtype, "mM")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyDateTimeToIsoCallback [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *NpyDateTimeToIsoCallback(JSOBJ Py_UNUSED(unused),
                                            JSONTypeContext *tc, size_t *len) {
  NPY_DATETIMEUNIT base = ((PyObjectEncoder *)tc->encoder)->datetimeUnit;
  NPY_DATETIMEUNIT valueUnit = ((PyObjectEncoder *)tc->encoder)->valueUnit;
  GET_TC(tc)->cStr = int64ToIso(GET_TC(tc)->longValue, valueUnit, base, len);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.__new__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def __new__(cls, freq) -> PeriodDtype:  # noqa: PYI034
        """
        Parameters
        ----------
        freq : PeriodDtype, BaseOffset, or string
        """
        if isinstance(freq, PeriodDtype):
            return freq

        elif isinstance(freq, PeriodDtypeBase):
            freq = to_offset(freq, is_period=True)

        if not isinstance(freq, BaseOffset):
            freq = cls._parse_dtype_strict(freq)

        if isinstance(freq, BDay):
            # GH#53446
            # TODO(3.0): enforcing this will close GH#10575
            warnings.warn(
                "PeriodDtype[B] is deprecated and will be removed in a future "
                "version. Use a DatetimeIndex with freq='B' instead",
                FutureWarning,  # pdlint: ignore[warning_class]
                stacklevel=find_stack_level(),
            )

        try:
            dtype_code = cls._cache_dtypes[freq]
        except KeyError:
            dtype_code = freq._period_dtype_code
            cls._cache_dtypes[freq] = dtype_code
        u = PeriodDtypeBase.__new__(cls, dtype_code, freq.n)
        u._freq = freq
        return u

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Isna.time_isna [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_isna(self, dtype):
        self.df.isna()
```
