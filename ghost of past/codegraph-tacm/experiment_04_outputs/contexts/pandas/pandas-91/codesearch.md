# pandas-91 :: codesearch

query: BUG: TimedeltaIndex.searchsorted accepting invalid types/dtypes (#30831)

## selected nodes

- rank=1 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=2 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py
- rank=3 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data_missing_for_sorting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py
- rank=4 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py::data_missing_for_sorting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py
- rank=5 layer=FUNCTION tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype._parse_dtype_strict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=6 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py::construct file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py
- rank=7 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py::data_for_sorting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py
- rank=8 layer=FUNCTION tokens=294 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLTable._get_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=9 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=10 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_validate_td64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=11 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data_for_sorting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py
- rank=12 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=13 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::get_datetime_metadata_from_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
- rank=14 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::FindValidIndex.time_first_valid_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=15 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::data_missing_for_sorting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py
- rank=16 layer=FUNCTION tokens=849 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::pandas_timedelta_to_timedeltastruct file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
- rank=17 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::data_for_sorting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py
- rank=18 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::SparseDtype.is_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=19 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::_maybe_try_sort file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=20 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique_sorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=21 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py
- rank=22 layer=FUNCTION tokens=247 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dict_iterNext file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=23 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Methods.time_findall file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py]
    def time_searchsorted(self, dtype):
        key = "2" if dtype == "str" else 2
        self.s.searchsorted(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py]
    def _test_searchsorted_bool_dtypes(self, data_for_sorting, as_series):
        # We call this from test_searchsorted in cases where we have a
        #  boolean-like dtype. The non-bool test assumes we have more than 2
        #  unique values.
        dtype = data_for_sorting.dtype
        data_for_sorting = pd.array([True, False], dtype=dtype)
        b, a = data_for_sorting
        arr = type(data_for_sorting)._from_sequence([a, b], dtype=dtype)

        if as_series:
            arr = pd.Series(arr)
        assert arr.searchsorted(a) == 0
        assert arr.searchsorted(a, side="right") == 1

        assert arr.searchsorted(b) == 1
        assert arr.searchsorted(b, side="right") == 2

        result = arr.searchsorted(arr.take([0, 1]))
        expected = np.array([0, 1], dtype=np.intp)

        tm.assert_numpy_array_equal(result, expected)

        # sorter
        sorter = np.array([1, 0])
        assert data_for_sorting.searchsorted(a, sorter=sorter) == 0

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data_missing_for_sorting [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py]
def data_missing_for_sorting(dtype):
    return PeriodArray([2018, iNaT, 2017], dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py::data_missing_for_sorting [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py]
def data_missing_for_sorting(dtype):
    a = pd.Timestamp("2000-01-01")
    b = pd.Timestamp("2000-01-02")
    return DatetimeArray._from_sequence(
        np.array([b, "NaT", a], dtype="datetime64[ns]"), dtype=dtype
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype._parse_dtype_strict [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _parse_dtype_strict(cls, freq: str_type) -> BaseOffset:
        if isinstance(freq, str):  # note: freq is already of type str!
            if freq.startswith(("Period[", "period[")):
                m = cls._match.search(freq)
                if m is not None:
                    freq = m.group("freq")

            freq_offset = to_offset(freq, is_period=True)
            if freq_offset is not None:
                return freq_offset

        raise TypeError(
            "PeriodDtype argument should be string or BaseOffset, "
            f"got {type(freq).__name__}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py::construct [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py]
    def construct(dtype):
        if dtype is dtlike_dtypes[-1]:
            # PeriodArray will try to cast ints to strings
            return DatetimeIndex(vals).astype(dtype)
        return Index(vals, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py::data_for_sorting [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py]
def data_for_sorting(dtype):
    a = pd.Timestamp("2000-01-01")
    b = pd.Timestamp("2000-01-02")
    c = pd.Timestamp("2000-01-03")
    return DatetimeArray._from_sequence(
        np.array([b, c, a], dtype="datetime64[ns]"), dtype=dtype
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLTable._get_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py]
    def _get_dtype(self, sqltype):
        from sqlalchemy.types import (
            TIMESTAMP,
            Boolean,
            Date,
            DateTime,
            Float,
            Integer,
            String,
        )

        if isinstance(sqltype, Float):
            return float
        elif isinstance(sqltype, Integer):
            # TODO: Refine integer size.
            return np.dtype("int64")
        elif isinstance(sqltype, TIMESTAMP):
            # we have a timezone capable type
            if not sqltype.timezone:
                return datetime
            return DatetimeTZDtype
        elif isinstance(sqltype, DateTime):
            # Caution: np.datetime64 is also a subclass of np.number.
            return datetime
        elif isinstance(sqltype, Date):
            return date
        elif isinstance(sqltype, Boolean):
            return bool
        elif isinstance(sqltype, String):
            if using_string_dtype():
                return StringDtype(na_value=np.nan)

        return object

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        if all(isinstance(t, DatetimeTZDtype) and t.tz == self.tz for t in dtypes):
            np_dtype = np.max(
                [cast("DatetimeTZDtype", t).base for t in [self, *dtypes]]
            )
            unit = np.datetime_data(np_dtype)[0]
            unit = cast("TimeUnit", unit)
            return type(self)(unit=unit, tz=self.tz)
        return super()._get_common_dtype(dtypes)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data_for_sorting [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py]
def data_for_sorting(dtype):
    return PeriodArray([2018, 2019, 2017], dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        if not all(isinstance(x, IntervalDtype) for x in dtypes):
            return None

        closed = cast("IntervalDtype", dtypes[0]).closed
        if not all(cast("IntervalDtype", x).closed == closed for x in dtypes):
            return np.dtype(object)

        from pandas.core.dtypes.cast import find_common_type

        common = find_common_type([cast("IntervalDtype", x).subtype for x in dtypes])
        if common == object:
            return np.dtype(object)
        return IntervalDtype(common, closed=closed)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::get_datetime_metadata_from_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c]
PyArray_DatetimeMetaData
get_datetime_metadata_from_dtype(PyArray_Descr *dtype) {
#if NPY_ABI_VERSION < 0x02000000
#  define PyDataType_C_METADATA(dtype) ((dtype)->c_metadata)
#endif
  return ((PyArray_DatetimeDTypeMetaData *)PyDataType_C_METADATA(dtype))->meta;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::FindValidIndex.time_first_valid_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_first_valid_index(self, dtype):
        self.df.first_valid_index()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::data_missing_for_sorting [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py]
def data_missing_for_sorting(dtype):
    if dtype.kind == "f":
        return pd.array([0.1, pd.NA, 0.0], dtype=dtype)
    elif dtype.kind == "b":
        return pd.array([True, np.nan, False], dtype=dtype)
    return pd.array([1, pd.NA, 0], dtype=dtype)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::data_for_sorting [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py]
def data_for_sorting(dtype):
    if dtype.kind == "f":
        return pd.array([0.1, 0.2, 0.0], dtype=dtype)
    elif dtype.kind == "b":
        return pd.array([True, True, False], dtype=dtype)
    return pd.array([1, 2, 0], dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::SparseDtype.is_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def is_dtype(cls, dtype: object) -> bool:
        dtype = getattr(dtype, "dtype", dtype)
        if isinstance(dtype, str) and dtype.startswith("Sparse"):
            sub_type, _ = cls._parse_subtype(dtype)
            dtype = np.dtype(sub_type)
        elif isinstance(dtype, cls):
            return True
        return isinstance(dtype, np.dtype) or dtype == "Sparse"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::_maybe_try_sort [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
def _maybe_try_sort(result: Index | ArrayLike, sort: bool | None) -> Index | ArrayLike:
    if sort is not False:
        try:
            # error: Incompatible types in assignment (expression has type
            # "Union[ExtensionArray, ndarray[Any, Any], Index, Series,
            # Tuple[Union[Union[ExtensionArray, ndarray[Any, Any]], Index, Series],
            # ndarray[Any, Any]]]", variable has type "Union[Index,
            # Union[ExtensionArray, ndarray[Any, Any]]]")
            result = algos.safe_sort(result)  # type: ignore[assignment]
        except TypeError as err:
            if sort is True:
                raise
            warnings.warn(
                f"{err}, sort order is undefined for incomparable objects.",
                RuntimeWarning,
                stacklevel=find_stack_level(),
            )
    return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique_sorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def time_get_loc_non_unique_sorted(self, dtype):
        self.non_unique_sorted.get_loc(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py]
def _is_dt_or_td(dtype: DtypeObj) -> bool:
    # Note: the dtype here comes from an Index.dtype, so we know that any
    #  dt64/td64 dtype is of a supported unit.
    return isinstance(dtype, DatetimeTZDtype) or lib.is_np_dtype(dtype, "mM")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dict_iterNext [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static int Dict_iterNext(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  if (GET_TC(tc)->itemName) {
    Py_DECREF(GET_TC(tc)->itemName);
    GET_TC(tc)->itemName = NULL;
  }

  if (!PyDict_Next((PyObject *)GET_TC(tc)->dictObj, &GET_TC(tc)->index,
                   &GET_TC(tc)->itemName, &GET_TC(tc)->itemValue)) {
    return 0;
  }

  if (PyUnicode_Check(GET_TC(tc)->itemName)) {
    GET_TC(tc)->itemName = PyUnicode_AsUTF8String(GET_TC(tc)->itemName);
  } else if (!PyBytes_Check(GET_TC(tc)->itemName)) {
    GET_TC(tc)->itemName = PyObject_Str(GET_TC(tc)->itemName);
    PyObject *itemNameTmp = GET_TC(tc)->itemName;
    GET_TC(tc)->itemName = PyUnicode_AsUTF8String(GET_TC(tc)->itemName);
    Py_DECREF(itemNameTmp);
  } else {
    Py_INCREF(GET_TC(tc)->itemName);
  }
  return 1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Methods.time_findall [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py]
    def time_findall(self, dtype):
        self.s.str.findall("[A-Z]+")
```
