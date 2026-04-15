# pandas-36 :: codesearch

query: BUG: isna_old with td64, dt64tz, period (#33158)

## selected nodes

- rank=1 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::make_iso_8601_timedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=2 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::dt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
- rank=3 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_day.py::dt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_day.py
- rank=4 layer=FUNCTION tokens=365 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::get_datetime_iso_8601_strlen file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=5 layer=FUNCTION tokens=1641 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::make_iso_8601_datetime file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=6 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::apply_tzinfo_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c
- rank=7 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py::dt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
- rank=8 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_hour.py::dt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_hour.py
- rank=9 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_offsets.py::dt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_offsets.py
- rank=10 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimeDT64ArrToPeriodArr.time_dt64arr_to_periodarr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=11 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
- rank=12 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.dt64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
- rank=13 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::time2num file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py
- rank=14 layer=FUNCTION tokens=313 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::get_long_attr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=15 layer=FUNCTION tokens=137 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyTimeDeltaToIsoCallback file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=16 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeISO8601.time_iso8601_infer_zero_tz_fromat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py
- rank=17 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::total_seconds file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=18 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::TestCustomBusinessMonthBegin.testRollback2 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::make_iso_8601_datetime [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c]
int make_iso_8601_datetime(npy_datetimestruct *dts, char *outstr, size_t outlen,
                           int utc, NPY_DATETIMEUNIT base) {
  char *substr = outstr;
  size_t sublen = outlen;
  int tmplen;

  /*
   * Print weeks with the same precision as days.
   *
   * TODO: Could print weeks with YYYY-Www format if the week
   *       epoch is a Monday.
   */
  if (base == NPY_FR_W) {
    base = NPY_FR_D;
  }

/* YEAR */
/*
 * Can't use PyOS_snprintf, because it always produces a '\0'
 * character at the end, and NumPy string types are permitted
 * to have data all the way to the end of the buffer.
 */
#ifdef _WIN32
  tmplen = _snprintf(substr, sublen, "%04" NPY_INT64_FMT, dts->year);
#else
  tmplen = snprintf(substr, sublen, "%04" NPY_INT64_FMT, dts->year);
#endif // _WIN32
  /* If it ran out of space or there isn't space for the NULL terminator */
  if (tmplen < 0 || (size_t)tmplen > sublen) {
    goto string_too_short;
  }
  substr += tmplen;
  sublen -= tmplen;

  /* Stop if the unit is years */
  if (base == NPY_FR_Y) {
    if (sublen > 0) {
      *substr = '\0';
    }
    return 0;
  }

  /* MONTH */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = '-';
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->month / 10) + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)((dts->month % 10) + '0');
  substr += 3;
  sublen -= 3;

  /* Stop if the unit is months */
  if (base == NPY_FR_M) {
    if (sublen > 0) {
      *substr = '\0';
    }
    return 0;
  }

  /* DAY */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = '-';
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->day / 10) + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)((dts->day % 10) + '0');
  substr += 3;
  sublen -= 3;

  /* Stop if the unit is days */
  if (base == NPY_FR_D) {
    if (sublen > 0) {
      *substr = '\0';
    }
    return 0;
  }

  /* HOUR */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = 'T';
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->hour / 10) + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)((dts->hour % 10) + '0');
  substr += 3;
  sublen -= 3;

  /* Stop if the unit is hours */
  if (base == NPY_FR_h) {
    goto add_time_zone;
  }

  /* MINUTE */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = ':';
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->min / 10) + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)((dts->min % 10) + '0');
  substr += 3;
  sublen -= 3;

  /* Stop if the unit is minutes */
  if (base == NPY_FR_m) {
    goto add_time_zone;
  }

  /* SECOND */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = ':';
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->sec / 10) + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)((dts->sec % 10) + '0');
  substr += 3;
  sublen -= 3;

  /* Stop if the unit is seconds */
  if (base == NPY_FR_s) {
    goto add_time_zone;
  }

  /* MILLISECOND */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = '.';
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->us / 100000) % 10 + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)((dts->us / 10000) % 10 + '0');
  if (sublen < 4) {
    goto string_too_short;
  }
  substr[3] = (char)((dts->us / 1000) % 10 + '0');
  substr += 4;
  sublen -= 4;

  /* Stop if the unit is milliseconds */
  if (base == NPY_FR_ms) {
    goto add_time_zone;
  }

  /* MICROSECOND */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = (char)((dts->us / 100) % 10 + '0');
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->us / 10) % 10 + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)(dts->us % 10 + '0');
  substr += 3;
  sublen -= 3;

  /* Stop if the unit is microseconds */
  if (base == NPY_FR_us) {
    goto add_time_zone;
  }

  /* NANOSECOND */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = (char)((dts->ps / 100000) % 10 + '0');
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->ps / 10000) % 10 + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)((dts->ps / 1000) % 10 + '0');
  substr += 3;
  sublen -= 3;

  /* Stop if the unit is nanoseconds */
  if (base == NPY_FR_ns) {
    goto add_time_zone;
  }

  /* PICOSECOND */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = (char)((dts->ps / 100) % 10 + '0');
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->ps / 10) % 10 + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)(dts->ps % 10 + '0');
  substr += 3;
  sublen -= 3;

  /* Stop if the unit is picoseconds */
  if (base == NPY_FR_ps) {
    goto add_time_zone;
  }

  /* FEMTOSECOND */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = (char)((dts->as / 100000) % 10 + '0');
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->as / 10000) % 10 + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)((dts->as / 1000) % 10 + '0');
  substr += 3;
  sublen -= 3;

  /* Stop if the unit is femtoseconds */
  if (base == NPY_FR_fs) {
    goto add_time_zone;
  }

  /* ATTOSECOND */
  if (sublen < 1) {
    goto string_too_short;
  }
  substr[0] = (char)((dts->as / 100) % 10 + '0');
  if (sublen < 2) {
    goto string_too_short;
  }
  substr[1] = (char)((dts->as / 10) % 10 + '0');
  if (sublen < 3) {
    goto string_too_short;
  }
  substr[2] = (char)(dts->as % 10 + '0');
  substr += 3;
  sublen -= 3;

add_time_zone:
  /* UTC "Zulu" time */
  if (utc) {
    if (sublen < 1) {
      goto string_too_short;
    }
    substr[0] = 'Z';
    substr += 1;
    sublen -= 1;
  }
  /* Add a NULL terminator, and return */
  if (sublen > 0) {
    substr[0] = '\0';
  }

  return 0;

string_too_short:
  PyErr_Format(PyExc_RuntimeError,
               "The string provided for NumPy ISO datetime formatting "
               "was too short, with length %d",
               outlen);
  return -1;
}

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py::dt [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py]
def dt():
    return datetime(2014, 7, 1, 10, 00)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_hour.py::dt [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_hour.py]
def dt():
    return datetime(2014, 7, 1, 10, 00)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_offsets.py::dt [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_offsets.py]
def dt():
    return Timestamp(datetime(2008, 1, 2))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimeDT64ArrToPeriodArr.time_dt64arr_to_periodarr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def time_dt64arr_to_periodarr(self, size, freq, tz):
        dt64arr_to_periodarr(self.i8values, freq, tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py]
    def ts(self, dt64):
        return Timestamp._from_dt64(dt64)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.dt64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py]
    def dt64(self, reso):
        # cases that are in-bounds for nanosecond, so we can compare against
        #  the existing implementation.
        return np.datetime64("2016-01-01", reso)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::time2num [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py]
def time2num(d):
    if isinstance(d, str):
        parsed = Timestamp(d)
        return _to_ordinalf(parsed.time())
    if isinstance(d, pydt.time):
        return _to_ordinalf(d)
    return d

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::get_long_attr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static npy_int64 get_long_attr(PyObject *o, const char *attr) {
  // NB we are implicitly assuming that o is a Timedelta or Timestamp, or NaT

  PyObject *value = PyObject_GetAttrString(o, attr);
  const npy_int64 long_val =
      (PyLong_Check(value) ? PyLong_AsLongLong(value) : PyLong_AsLong(value));

  Py_DECREF(value);

  if (object_is_nat_type(o)) {
    // i.e. o is NaT, long_val will be NPY_MIN_INT64
    return long_val;
  }

  // ensure we are in nanoseconds, similar to Timestamp._as_creso or _as_unit
  PyObject *reso = PyObject_GetAttrString(o, "_creso");
  if (!PyLong_Check(reso)) {
    // https://github.com/pandas-dev/pandas/pull/49034#discussion_r1023165139
    Py_DECREF(reso);
    return -1;
  }

  long cReso = PyLong_AsLong(reso);
  Py_DECREF(reso);
  if (cReso == -1 && PyErr_Occurred()) {
    return -1;
  }

  if (cReso == NPY_FR_us) {
    return long_val * 1000L;
  } else if (cReso == NPY_FR_ms) {
    return long_val * 1000000L;
  } else if (cReso == NPY_FR_s) {
    return long_val * 1000000000L;
  }

  return long_val;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyTimeDeltaToIsoCallback [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *NpyTimeDeltaToIsoCallback(JSOBJ Py_UNUSED(unused),
                                             JSONTypeContext *tc, size_t *len) {
  NPY_DATETIMEUNIT valueUnit = ((PyObjectEncoder *)tc->encoder)->valueUnit;
  GET_TC(tc)->cStr = int64ToIsoDuration(GET_TC(tc)->longValue, valueUnit, len);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeISO8601.time_iso8601_infer_zero_tz_fromat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py]
    def time_iso8601_infer_zero_tz_fromat(self):
        # GH 41047
        to_datetime(self.strings_zero_tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::total_seconds [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static npy_float64 total_seconds(PyObject *td) {
  PyObject *value = PyObject_CallMethod(td, "total_seconds", NULL);
  const npy_float64 double_val = PyFloat_AS_DOUBLE(value);
  Py_DECREF(value);
  return double_val;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::TestCustomBusinessMonthBegin.testRollback2 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py]
    def testRollback2(self, dt):
        assert CBMonthBegin(10).rollback(dt) == datetime(2008, 1, 1)
```
