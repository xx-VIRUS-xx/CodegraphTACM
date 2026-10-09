# pandas-67 :: codesearch

query: BUG: Block.iget not wrapping timedelta64/datetime64 (#31666)

## selected nodes

- rank=1 layer=FUNCTION tokens=365 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::get_datetime_iso_8601_strlen file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=2 layer=FUNCTION tokens=1641 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::make_iso_8601_datetime file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=3 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::make_iso_8601_timedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=4 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyDateTimeToIsoCallback file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=5 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py::TimestampConstruction.time_from_npdatetime64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py
- rank=6 layer=FUNCTION tokens=137 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyTimeDeltaToIsoCallback file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=7 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeFromIntsFloats.time_sec_uint64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py
- rank=8 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::int64ToIso file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c
- rank=9 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py::_format_datetime64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py
- rank=10 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::apply_tzinfo_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c
- rank=11 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::int64ToIsoDuration file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c
- rank=12 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeISO8601.time_iso8601_infer_zero_tz_fromat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py
- rank=13 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeFromIntsFloats.time_nanosec_uint64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py
- rank=14 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strftime.py::PeriodStrftime.time_frame_period_formatting_iso8601_strftime_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strftime.py
- rank=15 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyDateTimeToIsoCallback [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *NpyDateTimeToIsoCallback(JSOBJ Py_UNUSED(unused),
                                            JSONTypeContext *tc, size_t *len) {
  NPY_DATETIMEUNIT base = ((PyObjectEncoder *)tc->encoder)->datetimeUnit;
  NPY_DATETIMEUNIT valueUnit = ((PyObjectEncoder *)tc->encoder)->valueUnit;
  GET_TC(tc)->cStr = int64ToIso(GET_TC(tc)->longValue, valueUnit, base, len);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py::TimestampConstruction.time_from_npdatetime64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py]
    def time_from_npdatetime64(self):
        Timestamp(self.npdatetime64)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyTimeDeltaToIsoCallback [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *NpyTimeDeltaToIsoCallback(JSOBJ Py_UNUSED(unused),
                                             JSONTypeContext *tc, size_t *len) {
  NPY_DATETIMEUNIT valueUnit = ((PyObjectEncoder *)tc->encoder)->valueUnit;
  GET_TC(tc)->cStr = int64ToIsoDuration(GET_TC(tc)->longValue, valueUnit, len);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeFromIntsFloats.time_sec_uint64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py]
    def time_sec_uint64(self):
        to_datetime(self.ts_sec_uint, unit="s")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py::_format_datetime64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py]
def _format_datetime64(x: NaTType | Timestamp, nat_rep: str = "NaT") -> str:
    if x is NaT:
        return nat_rep

    # Timestamp.__str__ falls back to datetime.datetime.__str__ = isoformat(sep=' ')
    # so it already uses string formatting rather than strftime (faster).
    return str(x)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeISO8601.time_iso8601_infer_zero_tz_fromat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py]
    def time_iso8601_infer_zero_tz_fromat(self):
        # GH 41047
        to_datetime(self.strings_zero_tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py::ToDatetimeFromIntsFloats.time_nanosec_uint64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/inference.py]
    def time_nanosec_uint64(self):
        to_datetime(self.ts_nanosec_uint, unit="ns")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strftime.py::PeriodStrftime.time_frame_period_formatting_iso8601_strftime_offset [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strftime.py]
    def time_frame_period_formatting_iso8601_strftime_offset(self, nobs, freq):
        """Not optimized yet as %z is not supported by `convert_strftime_format`"""
        self.data["p"].dt.strftime(date_format="%Y-%m-%dT%H:%M:%S%z")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py]
    def ts(self, dt64):
        return Timestamp._from_dt64(dt64)
```
