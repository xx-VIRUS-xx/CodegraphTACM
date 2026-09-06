# pandas-67 :: hybrid-cs

query: BUG: Block.iget not wrapping timedelta64/datetime64 (#31666)

## selected nodes

- rank=1 layer=FUNCTION tokens=461 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=2 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic.timedelta64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=3 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_maybe_unbox_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=4 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::int64ToIso file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c
- rank=5 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=6 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py::_format_datetime64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py
- rank=7 layer=FUNCTION tokens=365 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::get_datetime_iso_8601_strlen file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=8 layer=FUNCTION tokens=482 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unwrap_setitem_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=9 layer=FUNCTION tokens=346 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py::_make_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py
- rank=10 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray._unbox_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=11 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=12 layer=FUNCTION tokens=493 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py::is_valid_na_for_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py
- rank=13 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c::make_iso_8601_timedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime_strings.c
- rank=14 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyDateTimeToIsoCallback file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=15 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py::TimestampConstruction.time_from_npdatetime64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/timestamp.py
- rank=16 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic.timedelta64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py]
        def timedelta64(*args):
            # see casting notes in NumPy gh-12927
            return np.sum(list(map(np.timedelta64, args, intervals)))

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def iget(self, i: int, track_ref: bool = True) -> SingleBlockManager:
        """
        Return the data as a SingleBlockManager.
        """
        block = self.blocks[self.blknos[i]]
        values = block.iget(self.blklocs[i])

        # shortcut for select a single-dim from a 2-dim BM
        bp = BlockPlacement(slice(0, len(values)))
        nb = type(block)(
            values, placement=bp, ndim=1, refs=block.refs if track_ref else None
        )
        return SingleBlockManager(nb, self.axes[1].view())

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py::_format_datetime64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py]
def _format_datetime64(x: NaTType | Timestamp, nat_rep: str = "NaT") -> str:
    if x is NaT:
        return nat_rep

    # Timestamp.__str__ falls back to datetime.datetime.__str__ = isoformat(sep=' ')
    # so it already uses string formatting rather than strftime (faster).
    return str(x)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unwrap_setitem_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def _unwrap_setitem_indexer(self, indexer):
        """
        Adapt a 2D-indexer to our 1D values.

        This is intended for 'setitem', not 'iget' or '_slice'.
        """
        # TODO: ATM this doesn't work for iget/_slice, can we change that?

        if isinstance(indexer, tuple) and len(indexer) == 2:
            # TODO(EA2D): not needed with 2D EAs
            #  Should never have length > 2.  Caller is responsible for checking.
            #  Length 1 is reached vis setitem_single_block and setitem_single_column
            #  each of which pass indexer=(pi,)
            if all(isinstance(x, np.ndarray) and x.ndim == 2 for x in indexer):
                # GH#44703 went through indexing.maybe_convert_ix
                first, second = indexer
                if not (
                    second.size == 1 and (second == 0).all() and first.shape[1] == 1
                ):
                    raise NotImplementedError(
                        "This should not be reached. Please report a bug at "
                        "github.com/pandas-dev/pandas/"
                    )
                indexer = first[:, 0]

            elif lib.is_integer(indexer[1]) and indexer[1] == 0:
                # reached via setitem_single_block passing the whole indexer
                indexer = indexer[0]

            elif com.is_null_slice(indexer[1]):
                indexer = indexer[0]

            elif is_list_like(indexer[1]) and indexer[1][0] == 0:
                indexer = indexer[0]

            else:
                raise NotImplementedError(
                    "This should not be reached. Please report a bug at "
                    "github.com/pandas-dev/pandas/"
                )
        return indexer

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray._unbox_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py]
    def _unbox_scalar(self, value) -> np.datetime64:
        if not isinstance(value, self._scalar_type) and value is not NaT:
            raise ValueError("'value' should be a Timestamp.")
        self._check_compatible_with(value)
        if value is NaT:
            return np.datetime64(value._value, self.unit)
        else:
            return value.as_unit(self.unit, round_ok=False).asm8

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget_values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def iget_values(self, i: int) -> ArrayLike:
        """
        Return the data for column i as the values (ndarray or ExtensionArray).

        Warning! The returned array is a view but doesn't handle Copy-on-Write,
        so this should be used with caution.
        """
        # TODO(CoW) making the arrays read-only might make this safer to use?
        block = self.blocks[self.blknos[i]]
        values = block.iget(self.blklocs[i])
        return values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py::is_valid_na_for_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py]
def is_valid_na_for_dtype(obj, dtype: DtypeObj) -> bool:
    """
    isna check that excludes incompatible dtypes

    Parameters
    ----------
    obj : object
    dtype : np.datetime64, np.timedelta64, DatetimeTZDtype, or PeriodDtype

    Returns
    -------
    bool
    """
    if not lib.is_scalar(obj) or not isna(obj):
        return False
    elif dtype.kind == "M":
        if isinstance(dtype, np.dtype):
            # i.e. not tzaware
            return not isinstance(obj, (np.timedelta64, Decimal))
        # we have to rule out tznaive dt64("NaT")
        return not isinstance(obj, (np.timedelta64, np.datetime64, Decimal))
    elif dtype.kind == "m":
        return not isinstance(obj, (np.datetime64, Decimal))
    elif dtype.kind in "iufc":
        # Numeric
        return obj is not NaT and not isinstance(obj, (np.datetime64, np.timedelta64))
    elif dtype.kind == "b":
        # We allow pd.NA, None, np.nan in BooleanArray (same as IntervalDtype)
        return lib.is_float(obj) or obj is None or obj is libmissing.NA

    elif dtype == _dtype_str:
        # numpy string dtypes to avoid float np.nan
        return not isinstance(obj, (np.datetime64, np.timedelta64, Decimal, float))

    elif dtype == _dtype_object:
        # This is needed for Categorical, but is kind of weird
        return True

    elif isinstance(dtype, PeriodDtype):
        return not isinstance(obj, (np.datetime64, np.timedelta64, Decimal))

    elif isinstance(dtype, IntervalDtype):
        return lib.is_float(obj) or obj is None or obj is libmissing.NA

    elif isinstance(dtype, CategoricalDtype):
        return is_valid_na_for_dtype(obj, dtype.categories.dtype)

    # fallback, default to allowing NaN, None, NA, NaT
    return not isinstance(obj, (np.datetime64, np.timedelta64, Decimal))

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py]
    def setup(self, offset):
        self.date = datetime(2011, 1, 1)
        self.dt64 = np.datetime64("2011-01-01 09:00Z")
```
