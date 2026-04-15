# pandas-36 :: hybrid-cs

query: BUG: isna_old with td64, dt64tz, period (#33158)

## selected nodes

- rank=1 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_validate_td64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=2 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::TestSetitemNADatetimeLikeDtype.is_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=3 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py::_f4 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py
- rank=4 layer=FUNCTION tokens=515 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::get_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=5 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::_make_2d_ea_df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py
- rank=6 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::make_iso_8601_timedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=7 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::TimedeltaArray._validate_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=8 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=9 layer=FUNCTION tokens=682 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=10 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.any file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=11 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::dt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
- rank=12 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_day.py::dt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_day.py
- rank=13 layer=FUNCTION tokens=365 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::get_datetime_iso_8601_strlen file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=14 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.all file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=15 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::TimedeltaArray._simple_new file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=16 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::apply_tzinfo_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c
- rank=17 layer=FUNCTION tokens=216 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_with_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=18 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py::dt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
- rank=19 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py::TimeTZConvert.time_tz_convert_from_utc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py
- rank=20 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_hour.py::dt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_hour.py
- rank=21 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::at file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::TestSetitemNADatetimeLikeDtype.is_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py]
    def is_inplace(self, val, obj):
        # td64   -> cast to object iff val is datetime64("NaT")
        # dt64   -> cast to object iff val is timedelta64("NaT")
        # dt64tz -> cast to object with anything _but_ NaT
        return val is NaT or val is None or val is np.nan or obj.dtype == val.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py::_f4 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py]
def _f4(old=True, unchanged=True):
    return old, unchanged

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::_make_2d_ea_df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py]
def _make_2d_ea_df(col_arrays, col_names):
    """
    Construct a DataFrame with a single 2D ExtensionArray block.

    Used for dt64tz and period types which support 2D blocks but don't
    consolidate automatically.
    """
    ea_type = type(col_arrays[0])
    ea_2d = ea_type._simple_new(
        np.stack([arr._ndarray for arr in col_arrays]),
        dtype=col_arrays[0].dtype,
    )
    return DataFrame(ea_2d.T, columns=col_names)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::make_iso_8601_timedelta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c]
int make_iso_8601_timedelta(pandas_timedeltastruct *tds, char *outstr,
                            size_t *outlen) {
  *outlen = 0;
  *outlen += snprintf(outstr, 60, // NOLINT
                      "P%" NPY_INT64_FMT "DT%" NPY_INT32_FMT "H%" NPY_INT32_FMT
                      "M%" NPY_INT32_FMT,
                      tds->days, tds->hrs, tds->min, tds->sec);
  outstr += *outlen;

  if (tds->ns != 0) {
    *outlen += snprintf(outstr, 12, // NOLINT
                        ".%03" NPY_INT32_FMT "%03" NPY_INT32_FMT
                        "%03" NPY_INT32_FMT "S",
                        tds->ms, tds->us, tds->ns);
  } else if (tds->us != 0) {
    *outlen += snprintf(outstr, 9, // NOLINT
                        ".%03" NPY_INT32_FMT "%03" NPY_INT32_FMT "S", tds->ms,
                        tds->us);
  } else if (tds->ms != 0) {
    *outlen += snprintf(outstr, 6, // NOLINT
                        ".%03" NPY_INT32_FMT "S", tds->ms);
  } else {
    *outlen += snprintf(outstr, 2, // NOLINT
                        "%s", "S");
  }

  return 0;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::TimedeltaArray._validate_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py]
    def _validate_dtype(cls, values, dtype):
        # used in TimeLikeOps.__init__
        dtype = _validate_td64_dtype(dtype)
        _validate_td64_dtype(values.dtype)
        if dtype != values.dtype:
            raise ValueError("Values resolution does not match dtype.")
        return dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def _create_mi_with_dt64tz_level():
    """
    MultiIndex with a level that is a tzaware DatetimeIndex.
    """
    # GH#8367 round trip with pickle
    return MultiIndex.from_product(
        [[1, 2], ["a", "b"], date_range("20130101", periods=3, tz="US/Eastern")],
        names=["one", "two", "three"],
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.to_period [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def to_period(
        self,
        freq: Frequency | None = None,
        axis: Axis = 0,
        copy: bool | lib.NoDefault = lib.no_default,
    ) -> DataFrame:
        """
        Convert DataFrame from DatetimeIndex to PeriodIndex.

        Convert DataFrame from DatetimeIndex to PeriodIndex with desired
        frequency (inferred from index if not passed). Either index of columns can be
        converted, depending on `axis` argument.

        Parameters
        ----------
        freq : str, default
            Frequency of the PeriodIndex.
        axis : {0 or 'index', 1 or 'columns'}, default 0
            The axis to convert (the index by default).
        copy : bool, default False
            This keyword is now ignored; changing its value will have no
            impact on the method.

            .. deprecated:: 3.0.0

                This keyword is ignored and will be removed in pandas 4.0. Since
                pandas 3.0, this method always returns a new object using a lazy
                copy mechanism that defers copies until necessary
                (Copy-on-Write). See the `user guide on Copy-on-Write
                <https://pandas.pydata.org/docs/dev/user_guide/copy_on_write.html>`__
                for more details.

        Returns
        -------
        DataFrame
            The DataFrame with the converted PeriodIndex.

        See Also
        --------
        Series.to_period: Equivalent method for Series.
        Series.dt.to_period: Convert DateTime column values.

        Examples
        --------
        >>> idx = pd.to_datetime(
        ...     [
        ...         "2001-03-31 00:00:00",
        ...         "2002-05-31 00:00:00",
        ...         "2003-08-31 00:00:00",
        ...     ]
        ... )

        >>> idx
        DatetimeIndex(['2001-03-31', '2002-05-31', '2003-08-31'],
                      dtype='datetime64[us]', freq=None)

        >>> idx.to_period("M")
        PeriodIndex(['2001-03', '2002-05', '2003-08'], dtype='period[M]')

        For the yearly frequency

        >>> idx.to_period("Y")
        PeriodIndex(['2001', '2002', '2003'], dtype='period[Y-DEC]')
        """
        self._check_copy_deprecation(copy)
        new_obj = self.copy(deep=False)

        axis_name = self._get_axis_name(axis)
        old_ax = getattr(self, axis_name)
        if not isinstance(old_ax, DatetimeIndex):
            raise TypeError(f"unsupported Type {type(old_ax).__name__}")

        new_ax = old_ax.to_period(freq=freq)

        setattr(new_obj, axis_name, new_ax)
        return new_obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.any [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def any(self, *, axis: AxisInt | None = None, skipna: bool = True) -> bool:
        # GH#34479 the nanops call will raise a TypeError for non-td64 dtype
        return nanops.nanany(self._ndarray, axis=axis, skipna=skipna, mask=self.isna())

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::dt [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py]
def dt():
    return datetime(2008, 1, 1)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_day.py::dt [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_day.py]
def dt():
    return datetime(2008, 1, 1)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::get_datetime_iso_8601_strlen [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c]
int get_datetime_iso_8601_strlen(int local, NPY_DATETIMEUNIT base) {
  int len = 0;

  switch (base) {
  /* Generic units can only be used to represent NaT */
  /*    return 4;*/
  case NPY_FR_as:
    len += 3; /* "###" */
    PD_FALLTHROUGH;
  case NPY_FR_fs:
    len += 3; /* "###" */
    PD_FALLTHROUGH;
  case NPY_FR_ps:
    len += 3; /* "###" */
    PD_FALLTHROUGH;
  case NPY_FR_ns:
    len += 3; /* "###" */
    PD_FALLTHROUGH;
  case NPY_FR_us:
    len += 3; /* "###" */
    PD_FALLTHROUGH;
  case NPY_FR_ms:
    len += 4; /* ".###" */
    PD_FALLTHROUGH;
  case NPY_FR_s:
    len += 3; /* ":##" */
    PD_FALLTHROUGH;
  case NPY_FR_m:
    len += 3; /* ":##" */
    PD_FALLTHROUGH;
  case NPY_FR_h:
    len += 3; /* "T##" */
    PD_FALLTHROUGH;
  case NPY_FR_D:
  case NPY_FR_W:
    len += 3; /* "-##" */
    PD_FALLTHROUGH;
  case NPY_FR_M:
    len += 3; /* "-##" */
    PD_FALLTHROUGH;
  case NPY_FR_Y:
    len += 21; /* 64-bit year */
    break;
  default:
    len += 3; /* handle the now defunct NPY_FR_B */
    break;
  }

  if (base >= NPY_FR_h) {
    if (local) {
      len += 5; /* "+####" or "-####" */
    } else {
      len += 1; /* "Z" */
    }
  }

  len += 1; /* NULL terminator */

  return len;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.all [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def all(self, *, axis: AxisInt | None = None, skipna: bool = True) -> bool:
        # GH#34479 the nanops call will raise a TypeError for non-td64 dtype

        return nanops.nanall(self._ndarray, axis=axis, skipna=skipna, mask=self.isna())

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::TimedeltaArray._simple_new [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py]
    def _simple_new(  # type: ignore[override]
        cls,
        values: npt.NDArray[np.timedelta64],
        freq: Tick | Day | None = None,
        dtype: np.dtype[np.timedelta64] = TD64NS_DTYPE,
    ) -> Self:
        # Require td64 dtype, not unit-less, matching values.dtype
        assert lib.is_np_dtype(dtype, "m")
        assert not tslibs.is_unitless(dtype)
        assert isinstance(values, np.ndarray), type(values)
        assert dtype == values.dtype
        assert freq is None or isinstance(freq, (Tick, Day))

        result = super()._simple_new(values=values, dtype=dtype)
        result._freq = freq
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::apply_tzinfo_offset [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c]
static int apply_tzinfo_offset(PyObject *obj, npy_datetimestruct *out) {
  PyObject *offset = extract_utc_offset(obj);
  /* Apply the time zone offset if datetime obj is tz-aware */
  if (offset != NULL) {
    if (offset == Py_None) {
      Py_DECREF(offset);
      return 0;
    }
    /*
     * The timedelta should have a function "total_seconds"
     * which contains the value we want.
     */
    PyObject *tmp = PyObject_CallMethod(offset, "total_seconds", NULL);
    Py_DECREF(offset);
    if (tmp == NULL) {
      return -1;
    }
    PyObject *tmp_int = PyNumber_Long(tmp);
    if (tmp_int == NULL) {
      Py_DECREF(tmp);
      return -1;
    }
    int seconds_offset = PyLong_AsLong(tmp_int);
    if (seconds_offset == -1 && PyErr_Occurred()) {
      Py_DECREF(tmp_int);
      Py_DECREF(tmp);
      return -1;
    }
    Py_DECREF(tmp_int);
    Py_DECREF(tmp);

    /* Convert to a minutes offset and apply it */
    add_minutes_to_datetimestruct(out, -(seconds_offset / 60));
  }

  return 0;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_with_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def index_with_missing(request):
    """
    Fixture for indices with missing values.

    Integer-dtype and empty cases are excluded because they cannot hold missing
    values.

    MultiIndex is excluded because isna() is not defined for MultiIndex.
    """
    ind = indices_dict[request.param]
    if request.param in ["tuples", "mi-with-dt64tz-level", "multi"]:
        # For setting missing values in the top level of MultiIndex
        vals = ind.tolist()
        vals[0] = (None, *vals[0][1:])
        vals[-1] = (None, *vals[-1][1:])
        return MultiIndex.from_tuples(vals)
    else:
        vals = ind.values.copy()
        vals[0] = None
        vals[-1] = None
        return type(ind)(vals, copy=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py::dt [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py]
def dt():
    return datetime(2014, 7, 1, 10, 00)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py::TimeTZConvert.time_tz_convert_from_utc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py]
    def time_tz_convert_from_utc(self, size, tz):
        # effectively:
        #  dti = DatetimeIndex(self.i8data, tz=tz)
        #  dti.tz_localize(None)
        if old_sig:
            tz_convert_from_utc(self.i8data, timezone.utc, tz)
        else:
            tz_convert_from_utc(self.i8data, tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_hour.py::dt [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_hour.py]
def dt():
    return datetime(2014, 7, 1, 10, 00)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::at [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def at(x):
    return x.at
```
