# pandas-95 :: codesearch

query: BUG: PeriodArray comparisons inconsistent with Period comparisons (#30722)

## selected nodes

- rank=1 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::assert_period_array_equal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py
- rank=2 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._sub_periodlike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=3 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._add_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=4 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::_period_dispatch file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=5 layer=FUNCTION tokens=429 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::period_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=6 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::scaleYearToEpoch file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
- rank=7 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::TestPeriodArray.arr1d file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=8 layer=FUNCTION tokens=515 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::get_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=9 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._cast_partial_indexing_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=10 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=11 layer=FUNCTION tokens=849 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::pandas_timedelta_to_timedeltastruct file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
- rank=12 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::_new_PeriodIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=13 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::scaleYearsToMonths file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
- rank=14 layer=FUNCTION tokens=318 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::days_to_yearsdays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
- rank=15 layer=FUNCTION tokens=241 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._difference_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=16 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyDateTimeToIsoCallback file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=17 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimeDT64ArrToPeriodArr.time_dt64arr_to_periodarr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=18 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::GetItem.time_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::assert_period_array_equal [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py]
def assert_period_array_equal(left, right, obj: str = "PeriodArray") -> None:
    _check_isinstance(left, right, PeriodArray)

    assert_numpy_array_equal(left._ndarray, right._ndarray, obj=f"{obj}._ndarray")
    assert_attr_equal("dtype", left, right, obj=obj)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._sub_periodlike [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _sub_periodlike(self, other: Period | PeriodArray) -> npt.NDArray[np.object_]:
        # If the operation is well-defined, we return an object-dtype ndarray
        # of DateOffsets.  Null entries are filled with pd.NaT
        if not isinstance(self.dtype, PeriodDtype):
            raise TypeError(
                f"cannot subtract {type(other).__name__} from {type(self).__name__}"
            )

        self = cast("PeriodArray", self)
        self._check_compatible_with(other)

        other_i8, o_mask = self._get_i8_values_and_mask(other)
        new_i8_data = add_overflowsafe(self.asi8, np.asarray(-other_i8, dtype="i8"))
        new_data = np.array([self.freq.base * x for x in new_i8_data])

        if o_mask is None:
            # i.e. Period scalar
            mask = self._isnan
        else:
            # i.e. PeriodArray
            mask = self._isnan | o_mask
        new_data[mask] = NaT
        return new_data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._add_period [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _add_period(self, other: Period) -> PeriodArray:
        if not lib.is_np_dtype(self.dtype, "m"):
            raise TypeError(f"cannot add Period to a {type(self).__name__}")

        # We will wrap in a PeriodArray and defer to the reversed operation
        from pandas.core.arrays.period import PeriodArray

        i8vals = np.broadcast_to(other.ordinal, self.shape)
        dtype = PeriodDtype(other.freq)
        parr = PeriodArray(i8vals, dtype=dtype)
        return parr + self

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::_period_dispatch [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
def _period_dispatch(meth: F) -> F:
    """
    For PeriodArray methods, dispatch to DatetimeArray and re-wrap the results
    in PeriodArray.  We cannot use ._ndarray directly for the affected
    methods because the i8 data has different semantics on NaT values.
    """

    @wraps(meth)
    def new_meth(self, *args, **kwargs):
        if not isinstance(self.dtype, PeriodDtype):
            return meth(self, *args, **kwargs)

        arr = self.view("M8[ns]")
        result = meth(arr, *args, **kwargs)
        if result is NaT:
            return NaT
        elif isinstance(result, Timestamp):
            return self._box_func(result._value)

        res_i8 = result.view("i8")
        return self._from_backing_data(res_i8)

    return cast("F", new_meth)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::period_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
def period_array(
    data: Sequence[Period | str | None] | AnyArrayLike,
    dtype: PeriodDtype | None = None,
) -> PeriodArray:
    """
    Construct a new PeriodArray from a sequence of Period scalars.

    Parameters
    ----------
    data : Sequence of Period objects
        A sequence of Period objects. These are required to all have
        the same ``freq.`` Missing values can be indicated by ``None``
        or ``pandas.NaT``.
    dtype : PeriodDtype or None, default None
        The dtype for the array. If not specified, is inferred from the data.

    Returns
    -------
    PeriodArray

    See Also
    --------
    PeriodArray
    pandas.PeriodIndex

    Examples
    --------
    >>> period_array([pd.Period("2017", freq="Y"), pd.Period("2018", freq="Y")])
    <PeriodArray>
    ['2017', '2018']
    Length: 2, dtype: period[Y-DEC]

    >>> period_array([pd.Period("2017", freq="Y"), pd.Period("2018", freq="Y"), pd.NaT])
    <PeriodArray>
    ['2017', '2018', 'NaT']
    Length: 3, dtype: period[Y-DEC]

    Integers that look like years are handled

    >>> period_array([2000, 2001, 2002], dtype=PeriodDtype("D"))
    <PeriodArray>
    ['2000-01-01', '2001-01-01', '2002-01-01']
    Length: 3, dtype: period[D]

    Datetime-like strings may also be passed

    >>> period_array(
    ...     ["2000-Q1", "2000-Q2", "2000-Q3", "2000-Q4"], dtype=PeriodDtype("Q")
    ... )
    <PeriodArray>
    ['2000Q1', '2000Q2', '2000Q3', '2000Q4']
    Length: 4, dtype: period[Q-DEC]
    """
    return PeriodArray._from_sequence(data, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::scaleYearToEpoch [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c]
static inline int scaleYearToEpoch(int64_t year, int64_t *result) {
  return checked_sub(year, 1970, result);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::TestPeriodArray.arr1d [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py]
    def arr1d(self, period_index):
        """
        Fixture returning DatetimeArray from parametrized PeriodIndex objects
        """
        return period_index._data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::get_values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static PyObject *get_values(PyObject *obj) {
  PyObject *values = NULL;

  if (object_is_index_type(obj) || object_is_series_type(obj)) {
    // The special cases to worry about are dt64tz and category[dt64tz].
    //  In both cases we want the UTC-localized datetime64 ndarray,
    //  without going through and object array of Timestamps.
    if (PyObject_HasAttrString(obj, "tz")) {
      PyObject *tz = PyObject_GetAttrString(obj, "tz");
      if (tz != Py_None) {
        // Go through object array if we have dt64tz, since tz info will
        // be lost if values is used directly.
        Py_DECREF(tz);
        values = PyObject_CallMethod(obj, "__array__", NULL);
        return values;
      }
      Py_DECREF(tz);
    }
    values = PyObject_GetAttrString(obj, "values");
    if (values == NULL) {
      // Clear so we can subsequently try another method
      PyErr_Clear();
    } else if (PyObject_HasAttrString(values, "__array__")) {
      // We may have gotten a Categorical or Sparse array so call np.array
      PyObject *array_values = PyObject_CallMethod(values, "__array__", NULL);
      Py_DECREF(values);
      values = array_values;
    } else if (!PyArray_CheckExact(values)) {
      // Didn't get a numpy array, so keep trying
      Py_DECREF(values);
      values = NULL;
    }
  }

  if (values == NULL) {
    PyObject *typeRepr = PyObject_Repr((PyObject *)Py_TYPE(obj));
    PyObject *repr;
    if (PyObject_HasAttrString(obj, "dtype")) {
      PyObject *dtype = PyObject_GetAttrString(obj, "dtype");
      repr = PyObject_Repr(dtype);
      Py_DECREF(dtype);
    } else {
      repr = PyUnicode_FromString("<unknown dtype>");
    }

    PyErr_Format(PyExc_ValueError, "%R or %R are not JSON serializable yet",
                 repr, typeRepr);
    Py_DECREF(repr);
    Py_DECREF(typeRepr);

    return NULL;
  }

  return values;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._cast_partial_indexing_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
    def _cast_partial_indexing_scalar(self, label: datetime) -> Period:
        try:
            period = Period(label, freq=self.freq)
        except ValueError as err:
            # we cannot construct the Period
            raise KeyError(label) from err
        return period

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endArray [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_endArray(void *Py_UNUSED(prv), JSOBJ obj) { return obj; }

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::_new_PeriodIndex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
def _new_PeriodIndex(cls, **d):
    # GH13277 for unpickling
    values = d.pop("data")
    if values.dtype == "int64":
        freq = d.pop("freq", None)
        dtype = PeriodDtype(freq)
        values = PeriodArray(values, dtype=dtype)
        return cls._simple_new(values, **d)
    else:
        return cls(values, **d)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::scaleYearsToMonths [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c]
static inline int scaleYearsToMonths(int64_t years, int64_t *result) {
  return checked_mul(years, 12, result);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::days_to_yearsdays [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c]
static npy_int64 days_to_yearsdays(npy_int64 *days_) {
  const npy_int64 days_per_400years = (400 * 365 + 100 - 4 + 1);
  /* Adjust so it's relative to the year 2000 (divisible by 400) */
  npy_int64 days = (*days_) - (365 * 30 + 7);
  npy_int64 year;

  /* Break down the 400 year cycle to get the year and day within the year */
  if (days >= 0) {
    year = 400 * (days / days_per_400years);
    days = days % days_per_400years;
  } else {
    year = 400 * ((days - (days_per_400years - 1)) / days_per_400years);
    days = days % days_per_400years;
    if (days < 0) {
      days += days_per_400years;
    }
  }

  /* Work out the year/day within the 400 year cycle */
  if (days >= 366) {
    year += 100 * ((days - 1) / (100 * 365 + 25 - 1));
    days = (days - 1) % (100 * 365 + 25 - 1);
    if (days >= 365) {
      year += 4 * ((days + 1) / (4 * 365 + 1));
      days = (days + 1) % (4 * 365 + 1);
      if (days >= 366) {
        year += (days - 1) / 365;
        days = (days - 1) % 365;
      }
    }
  }

  *days_ = days;
  return year + 2000;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._difference_compat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _difference_compat(
        self, target: Index, indexer: npt.NDArray[np.intp]
    ) -> ArrayLike:
        # Compatibility for PeriodArray, for which __sub__ returns an ndarray[object]
        #  of DateOffset objects, which do not support __abs__ (and would be slow
        #  if they did)

        if isinstance(self.dtype, PeriodDtype):
            # Note: we only get here with matching dtypes
            own_values = cast("PeriodArray", self._data)._ndarray
            target_values = cast("PeriodArray", target._data)._ndarray
            diff = own_values[indexer] - target_values
        else:
            # error: Unsupported left operand type for - ("ExtensionArray")
            diff = self._values[indexer] - target._values  # type: ignore[operator]
        return abs(diff)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyDateTimeToIsoCallback [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *NpyDateTimeToIsoCallback(JSOBJ Py_UNUSED(unused),
                                            JSONTypeContext *tc, size_t *len) {
  NPY_DATETIMEUNIT base = ((PyObjectEncoder *)tc->encoder)->datetimeUnit;
  NPY_DATETIMEUNIT valueUnit = ((PyObjectEncoder *)tc->encoder)->valueUnit;
  GET_TC(tc)->cStr = int64ToIso(GET_TC(tc)->longValue, valueUnit, base, len);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimeDT64ArrToPeriodArr.time_dt64arr_to_periodarr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def time_dt64arr_to_periodarr(self, size, freq, tz):
        dt64arr_to_periodarr(self.i8values, freq, tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::GetItem.time_slice [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py]
    def time_slice(self):
        self.sp_arr[1:]
```
