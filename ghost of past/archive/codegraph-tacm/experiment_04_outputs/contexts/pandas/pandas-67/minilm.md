# pandas-67 :: minilm

query: BUG: Block.iget not wrapping timedelta64/datetime64 (#31666)

## selected nodes

- rank=1 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::timedelta64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=2 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.inferred_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=3 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_np_timedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py
- rank=4 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::int64ToIsoDuration file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c
- rank=5 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::ensure_wrapped_if_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=6 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::DateInferOps.time_timedelta_plus_datetime file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=7 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaProperties.time_timedelta_microseconds file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py
- rank=8 layer=FUNCTION tokens=292 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::TimedeltaArray.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=9 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_iso_format file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py
- rank=10 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::int64ToIso file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c
- rank=11 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_datetime_timedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py
- rank=12 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.time_add_np_dt64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py
- rank=13 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py
- rank=14 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_validate_td64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=15 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_pd_timedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py
- rank=16 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._get_string_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=17 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._sub_nat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=18 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.inferred_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=19 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py
- rank=20 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::datetime64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=21 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeFromIntsFloats.time_nanosec_uint64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py
- rank=22 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py::TimestampConstruction.time_from_npdatetime64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py
- rank=23 layer=FUNCTION tokens=254 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=24 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/missing.py::_datetimelike_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/missing.py
- rank=25 layer=FUNCTION tokens=849 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::pandas_timedelta_to_timedeltastruct file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::timedelta64_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def timedelta64_dtype(request):
    """
    Parametrized fixture for timedelta64 dtypes.

    * 'timedelta64[ns]'
    * 'm8[ns]'
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.inferred_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py]
    def inferred_type(self) -> str:
        return "timedelta64"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_np_timedelta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py]
    def time_from_np_timedelta(self):
        Timedelta(self.nptimedelta64)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::DateInferOps.time_timedelta_plus_datetime [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_timedelta_plus_datetime(self, df):
        df["timedelta"] + df["datetime64"]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaProperties.time_timedelta_microseconds [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py]
    def time_timedelta_microseconds(self, td):
        td.microseconds

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_iso_format [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py]
    def time_from_iso_format(self):
        Timedelta("P4DT12H30M5S")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::int64ToIso [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c]
char *int64ToIso(int64_t value, NPY_DATETIMEUNIT valueUnit,
                 NPY_DATETIMEUNIT base, size_t *len) {
  npy_datetimestruct dts;
  int ret_code;

  pandas_datetime_to_datetimestruct(value, valueUnit, &dts);

  *len = (size_t)get_datetime_iso_8601_strlen(0, base);
  char *result = PyObject_Malloc(*len);

  if (result == NULL) {
    PyErr_NoMemory();
    return NULL;
  }
  // datetime64 is always naive
  ret_code = make_iso_8601_datetime(&dts, result, *len, 0, base);
  if (ret_code != 0) {
    PyErr_SetString(PyExc_ValueError,
                    "Could not convert datetime value to string");
    PyObject_Free(result);
  }

  // Note that get_datetime_iso_8601_strlen just gives a generic size
  // for ISO string conversion, not the actual size used
  *len = strlen(result);
  return result;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_datetime_timedelta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py]
    def time_from_datetime_timedelta(self):
        Timedelta(self.dttimedelta)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.time_add_np_dt64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py]
    def time_add_np_dt64(self, offset):
        offset + self.dt64

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py]
    def setup(self):
        self.nptimedelta64 = np.timedelta64(3600, "s")
        self.dttimedelta = datetime.timedelta(seconds=3600)
        self.td = Timedelta(3600, unit="s")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_pd_timedelta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py]
    def time_from_pd_timedelta(self):
        Timedelta(self.td)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._get_string_slice [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _get_string_slice(self, key: str) -> slice | npt.NDArray[np.intp]:  # type: ignore[override]
        # overridden by TimedeltaIndex
        parsed, reso = self._parse_with_reso(key)
        try:
            return self._partial_date_slice(reso, parsed)
        except KeyError as err:
            raise KeyError(key) from err

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.inferred_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py]
    def inferred_type(self) -> str:
        # b/c datetime is represented as microseconds since the epoch, make
        # sure we can't have ambiguous indexing
        return "datetime64"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py::TimedeltaConstructor.time_from_int [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timedelta.py]
    def time_from_int(self):
        Timedelta(123456789)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::datetime64_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def datetime64_dtype(request):
    """
    Parametrized fixture for datetime64 dtypes.

    * 'datetime64[ns]'
    * 'M8[ns]'
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeFromIntsFloats.time_nanosec_uint64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py]
    def time_nanosec_uint64(self):
        to_datetime(self.ts_nanosec_uint, unit="ns")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py::TimestampConstruction.time_from_npdatetime64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py]
    def time_from_npdatetime64(self):
        Timestamp(self.npdatetime64)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::pandas_timedelta_to_timedeltastruct [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c]
void pandas_timedelta_to_timedeltastruct(npy_timedelta td,
                                         NPY_DATETIMEUNIT base,
                                         pandas_timedeltastruct *out) {
  /* Initialize the output to all zeros */
  memset(out, 0, sizeof(pandas_timedeltastruct));

  const npy_int64 sec_per_hour = 3600;
  const npy_int64 sec_per_min = 60;

  switch (base) {
  case NPY_FR_W:
    out->days = 7 * td;
    break;
  case NPY_FR_D:
    out->days = td;
    break;
  case NPY_FR_h:
    out->days = td / 24LL;
    td -= out->days * 24LL;
    out->hrs = (npy_int32)td;
    break;
  case NPY_FR_m:
    out->days = td / 1440LL;
    td -= out->days * 1440LL;
    out->hrs = (npy_int32)(td / 60LL);
    td -= out->hrs * 60LL;
    out->min = (npy_int32)td;
    break;
  case NPY_FR_s:
  case NPY_FR_ms:
  case NPY_FR_us:
  case NPY_FR_ns: {
    const npy_int64 sec_per_day = 86400;
    npy_int64 per_sec;
    if (base == NPY_FR_s) {
      per_sec = 1;
    } else if (base == NPY_FR_ms) {
      per_sec = 1000;
    } else if (base == NPY_FR_us) {
      per_sec = 1000000;
    } else {
      per_sec = 1000000000;
    }

    const npy_int64 per_day = sec_per_day * per_sec;
    npy_int64 frac;
    // put frac in seconds
    if (td < 0 && td % per_sec != 0)
      frac = td / per_sec - 1;
    else
      frac = td / per_sec;

    const int sign = frac < 0 ? -1 : 1;
    if (frac < 0) {
      // even fraction
      if ((-frac % sec_per_day) != 0) {
        out->days = -frac / sec_per_day + 1;
        frac += sec_per_day * out->days;
      } else {
        frac = -frac;
      }
    }

    if (frac >= sec_per_day) {
      out->days += frac / sec_per_day;
      frac -= out->days * sec_per_day;
    }

    if (frac >= sec_per_hour) {
      out->hrs = (npy_int32)(frac / sec_per_hour);
      frac -= out->hrs * sec_per_hour;
    }

    if (frac >= sec_per_min) {
      out->min = (npy_int32)(frac / sec_per_min);
      frac -= out->min * sec_per_min;
    }

    if (frac >= 0) {
      out->sec = (npy_int32)frac;
      frac -= out->sec;
    }

    if (sign < 0)
      out->days = -out->days;

    if (base > NPY_FR_s) {
      const npy_int64 sfrac =
          (out->hrs * sec_per_hour + out->min * sec_per_min + out->sec) *
          per_sec;

      npy_int64 ifrac = td - (out->days * per_day + sfrac);

      if (base == NPY_FR_ms) {
        out->ms = (npy_int32)ifrac;
      } else if (base == NPY_FR_us) {
        out->ms = (npy_int32)(ifrac / 1000LL);
        ifrac = ifrac % 1000LL;
        out->us = (npy_int32)ifrac;
      } else if (base == NPY_FR_ns) {
        out->ms = (npy_int32)(ifrac / (1000LL * 1000LL));
        ifrac = ifrac % (1000LL * 1000LL);
        out->us = (npy_int32)(ifrac / 1000LL);
        ifrac = ifrac % 1000LL;
        out->ns = (npy_int32)ifrac;
      }
    }

  } break;
  default:
    PyErr_SetString(PyExc_RuntimeError,
                    "NumPy timedelta metadata is corrupted with "
                    "invalid base unit");
    break;
  }

  out->seconds =
      (npy_int32)(out->hrs * sec_per_hour + out->min * sec_per_min + out->sec);
  out->microseconds = out->ms * 1000 + out->us;
  out->nanoseconds = out->ns;
}
```
