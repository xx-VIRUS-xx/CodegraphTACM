# pandas-80 :: codesearch

query: BUG: Series/Frame invert dtypes (#31183)

## selected nodes

- rank=1 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::dtype_backend_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=2 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=3 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterBegin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=4 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c::object_is_dataframe_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=5 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::_convert_arrays_to_dataframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=6 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterEnd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=7 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py::TestGeneric.f file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py
- rank=8 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newPosInf file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=9 layer=FUNCTION tokens=759 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::convert_pydatetime_to_datetimestruct file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c
- rank=10 layer=FUNCTION tokens=243 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_nlargest.py::df_main_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_nlargest.py
- rank=11 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::_wrap_transform_general_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=12 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py::make_dataframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py
- rank=13 layer=FUNCTION tokens=675 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/_util.py::_post_convert_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/_util.py
- rank=14 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_block_internals.py::TestDataFrameBlockInternals.f file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_block_internals.py
- rank=15 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_typst.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_typst.py
- rank=16 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_string.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_string.py
- rank=17 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py
- rank=18 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::typeof_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=19 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsondec.c::decodePreciseFloat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsondec.c
- rank=20 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py::get_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::dtype_backend_data [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py]
def dtype_backend_data() -> DataFrame:
    return DataFrame(
        {
            "a": Series([1, pd.NA, 3], dtype="Int64"),
            "b": Series([1, 2, 3], dtype="Int64"),
            "c": Series([1.5, pd.NA, 2.5], dtype="Float64"),
            "d": Series([1.5, 2.0, 2.5], dtype="Float64"),
            "e": [True, False, None],
            "f": [True, False, True],
            "g": ["a", "b", "c"],
            "h": ["a", "b", None],
        }
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py]
def types_data_frame(types_data):
    dtypes = {
        "TextCol": "str",
        "DateCol": "str",
        "IntDateCol": "int64",
        "IntDateOnlyCol": "int64",
        "FloatCol": "float",
        "IntCol": "int64",
        "BoolCol": "int64",
        "IntColWithNull": "float",
        "BoolColWithNull": "float",
    }
    df = DataFrame(types_data)
    return df[dtypes.keys()].astype(dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterBegin [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void DataFrame_iterBegin(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  PyObjectEncoder *enc = (PyObjectEncoder *)tc->encoder;
  GET_TC(tc)->index = 0;
  enc->outputFormat = VALUES; // for contained series & index
  GET_TC(tc)->cStr = PyObject_Malloc(CSTR_SIZE);
  if (!GET_TC(tc)->cStr) {
    PyErr_NoMemory();
  }
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c::object_is_dataframe_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c]
int object_is_dataframe_type(PyObject *obj) {
  PyObject *module = PyImport_ImportModule("pandas");
  if (module == NULL) {
    PyErr_Clear();
    return 0;
  }
  PyObject *type_dataframe = PyObject_GetAttrString(module, "DataFrame");
  if (type_dataframe == NULL) {
    Py_DECREF(module);
    PyErr_Clear();
    return 0;
  }
  int result = PyObject_IsInstance(obj, type_dataframe);
  if (result == -1) {
    Py_DECREF(module);
    Py_DECREF(type_dataframe);
    PyErr_Clear();
    return 0;
  }
  return result;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::_convert_arrays_to_dataframe [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py]
def _convert_arrays_to_dataframe(
    data,
    columns,
    coerce_float: bool = True,
    dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",
) -> DataFrame:
    content = lib.to_object_array_tuples(data)
    idx_len = content.shape[0]
    arrays = convert_object_array(
        list(content.T),
        dtype=None,
        coerce_float=coerce_float,
        dtype_backend=dtype_backend,
    )
    if dtype_backend == "pyarrow":
        pa = import_optional_dependency("pyarrow")

        result_arrays = []
        for arr in arrays:
            pa_array = pa.array(arr, from_pandas=True)
            if arr.dtype == "string":
                # TODO: Arrow still infers strings arrays as regular strings instead
                # of large_string, which is what we preserver everywhere else for
                # dtype_backend="pyarrow". We may want to reconsider this
                pa_array = pa_array.cast(pa.string())
            result_arrays.append(ArrowExtensionArray(pa_array))
        arrays = result_arrays  # type: ignore[assignment]
    if arrays:
        return DataFrame._from_arrays(
            arrays, columns=columns, index=range(idx_len), verify_integrity=False
        )
    else:
        return DataFrame(columns=columns)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterEnd [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void DataFrame_iterEnd(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  PyObjectEncoder *enc = (PyObjectEncoder *)tc->encoder;
  enc->outputFormat = enc->originalOutputFormat;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py::TestGeneric.f [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py]
        def f(dtype):
            return construct(frame_or_series, shape=3, value=1, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newPosInf [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newPosInf(void *Py_UNUSED(prv)) {
  return PyFloat_FromDouble(Py_HUGE_VAL);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::convert_pydatetime_to_datetimestruct [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c]
static int convert_pydatetime_to_datetimestruct(PyObject *dtobj,
                                                npy_datetimestruct *out) {
  // Assumes that obj is a valid datetime object
  PyObject *obj = (PyObject *)dtobj;

  /* Initialize the output to all zeros */
  memset(out, 0, sizeof(npy_datetimestruct));
  out->month = 1;
  out->day = 1;

  /*
   * Fast path: use the PyDateTime C API macros for direct struct access
   * instead of generic PyObject_GetAttrString lookups. PyDateTime_IMPORT
   * is called at module init, so the C API is available here.
   *
   * Use CheckExact to exclude subclasses (e.g. pd.Timestamp) whose
   * C-level struct fields may not match their Python-level attributes.
   */
  if (PyDateTime_CheckExact(obj)) {
    out->year = PyDateTime_GET_YEAR(obj);
    out->month = PyDateTime_GET_MONTH(obj);
    out->day = PyDateTime_GET_DAY(obj);
    out->hour = PyDateTime_DATE_GET_HOUR(obj);
    out->min = PyDateTime_DATE_GET_MINUTE(obj);
    out->sec = PyDateTime_DATE_GET_SECOND(obj);
    out->us = PyDateTime_DATE_GET_MICROSECOND(obj);

    PyObject *tzinfo = PyDateTime_DATE_GET_TZINFO(obj);
    if (tzinfo != Py_None) {
      return apply_tzinfo_offset(obj, out);
    }
    return 0;
  }

  if (PyDate_CheckExact(obj)) {
    out->year = PyDateTime_GET_YEAR(obj);
    out->month = PyDateTime_GET_MONTH(obj);
    out->day = PyDateTime_GET_DAY(obj);
    return 0;
  }

  /* Slow path: fall back to generic attribute lookups for duck-typed objects */
  PyObject *tmp;

  tmp = PyObject_GetAttrString(obj, "year");
  if (tmp == NULL)
    return -1;
  out->year = PyLong_AsLong(tmp);
  Py_DECREF(tmp);

  tmp = PyObject_GetAttrString(obj, "month");
  if (tmp == NULL)
    return -1;
  out->month = PyLong_AsLong(tmp);
  Py_DECREF(tmp);

  tmp = PyObject_GetAttrString(obj, "day");
  if (tmp == NULL)
    return -1;
  out->day = PyLong_AsLong(tmp);
  Py_DECREF(tmp);

  /* Check for time attributes (if not there, return success as a date) */
  if (!PyObject_HasAttrString(obj, "hour") ||
      !PyObject_HasAttrString(obj, "minute") ||
      !PyObject_HasAttrString(obj, "second") ||
      !PyObject_HasAttrString(obj, "microsecond")) {
    return 0;
  }

  tmp = PyObject_GetAttrString(obj, "hour");
  if (tmp == NULL)
    return -1;
  out->hour = PyLong_AsLong(tmp);
  Py_DECREF(tmp);

  tmp = PyObject_GetAttrString(obj, "minute");
  if (tmp == NULL)
    return -1;
  out->min = PyLong_AsLong(tmp);
  Py_DECREF(tmp);

  tmp = PyObject_GetAttrString(obj, "second");
  if (tmp == NULL)
    return -1;
  out->sec = PyLong_AsLong(tmp);
  Py_DECREF(tmp);

  tmp = PyObject_GetAttrString(obj, "microsecond");
  if (tmp == NULL)
    return -1;
  out->us = PyLong_AsLong(tmp);
  Py_DECREF(tmp);

  if (PyObject_HasAttrString(obj, "tzinfo")) {
    return apply_tzinfo_offset(obj, out);
  }

  return 0;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_nlargest.py::df_main_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_nlargest.py]
def df_main_dtypes():
    return pd.DataFrame(
        {
            "group": [1, 1, 2],
            "int": [1, 2, 3],
            "float": [4.0, 5.0, 6.0],
            "string": list("abc"),
            "category_string": pd.Series(list("abc")).astype("category"),
            "category_int": [7, 8, 9],
            "datetime": pd.date_range("20130101", periods=3),
            "datetimetz": pd.date_range("20130101", periods=3, tz="US/Eastern"),
            "timedelta": pd.timedelta_range("1 s", periods=3, freq="s"),
        },
        columns=[
            "group",
            "int",
            "float",
            "string",
            "category_string",
            "category_int",
            "datetime",
            "datetimetz",
            "timedelta",
        ],
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::_wrap_transform_general_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
def _wrap_transform_general_frame(
    obj: DataFrame, group: DataFrame, res: DataFrame | Series
) -> DataFrame:
    from pandas import concat

    if isinstance(res, Series):
        # we need to broadcast across the
        # other dimension; this will preserve dtypes
        # GH14457
        if res.index.is_(obj.index):
            res_frame = concat([res] * len(group.columns), axis=1, ignore_index=True)
            res_frame.columns = group.columns
            res_frame.index = group.index
        else:
            res_frame = obj._constructor(
                np.tile(res.values, (len(group.index), 1)),
                columns=group.columns,
                index=group.index,
            )
        assert isinstance(res_frame, DataFrame)
        return res_frame
    elif isinstance(res, DataFrame) and not res.index.is_(group.index):
        return res._align_frame(group)[0]
    else:
        return res

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py::make_dataframe [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py]
        def make_dataframe(*args, **kwargs):
            df = DataFrame(*args, **kwargs)
            df_nullable = df.convert_dtypes()
            # convert_dtypes will try to cast float to int if there is no loss in
            # precision -> undo that change
            for col in df.columns:
                if is_float_dtype(df[col].dtype) and not is_float_dtype(
                    df_nullable[col].dtype
                ):
                    df_nullable[col] = df_nullable[col].astype("Float64")
            # copy final result to ensure we start with a fully self-owning DataFrame
            return df_nullable.copy()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/_util.py::_post_convert_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/_util.py]
def _post_convert_dtypes(
    df: pd.DataFrame,
    dtype_backend: DtypeBackend | Literal["numpy"] | lib.NoDefault,
    dtype: DtypeArg | None,
    names: Sequence[Hashable] | None,
) -> pd.DataFrame:
    if dtype is not None and (
        dtype_backend is lib.no_default or dtype_backend == "numpy"
    ):
        # GH#56136 apply any user-provided dtype, and convert any IntegerDtype
        #  columns the user didn't explicitly ask for.
        if isinstance(dtype, dict):
            if names is not None:
                df.columns = names

            cmp_dtypes = {
                pd.Int8Dtype(),
                pd.Int16Dtype(),
                pd.Int32Dtype(),
                pd.Int64Dtype(),
            }
            for col in df.columns:
                if col not in dtype and df[col].dtype in cmp_dtypes:
                    # Any key that the user didn't explicitly specify
                    #  that got converted to IntegerDtype now gets converted
                    #  to numpy dtype.
                    dtype[col] = df[col].dtype.numpy_dtype

            # Ignore non-existent columns from dtype mapping
            # like other parsers do
            dtype = {
                key: pandas_dtype(dtype[key]) for key in dtype if key in df.columns
            }

        else:
            dtype = pandas_dtype(dtype)

        try:
            df = df.astype(dtype)
        except TypeError as err:
            # GH#44901 reraise to keep api consistent
            raise ValueError(str(err)) from err

    if (
        not using_string_dtype()
        and dtype != "str"
        and (dtype_backend is lib.no_default or dtype_backend == "numpy")
    ):
        # Convert any StringDtype columns back to object dtype (pyarrow always
        # uses string dtype even when the infer_string option is False)
        for col, dtype in zip(df.columns, df.dtypes, strict=True):
            if isinstance(dtype, pd.StringDtype) and dtype.na_value is np.nan:
                df[col] = df[col].astype("object").fillna(None)
            if isinstance(dtype, pd.CategoricalDtype):
                cat_dtype = dtype.categories.dtype
                if (
                    isinstance(cat_dtype, pd.StringDtype)
                    and cat_dtype.na_value is np.nan
                ):
                    cat_dtype = pd.CategoricalDtype(
                        categories=dtype.categories.astype("object"),
                        ordered=dtype.ordered,
                    )
                    df[col] = df[col].astype(cat_dtype)

    return df

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_block_internals.py::TestDataFrameBlockInternals.f [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_block_internals.py]
        def f(dtype):
            data = list(itertools.repeat((datetime(2001, 1, 1), "aa", 20), 9))
            return DataFrame(data=data, columns=["A", "B", "C"], dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_typst.py::df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_typst.py]
def df():
    return DataFrame(
        {"A": [0, 1], "B": [-0.61, -1.22], "C": Series(["ab", "cd"], dtype=object)}
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_string.py::df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_string.py]
def df():
    return DataFrame(
        {"A": [0, 1], "B": [-0.61, -1.22], "C": Series(["ab", "cd"], dtype=object)}
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py::df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py]
def df():
    return DataFrame(
        {"A": [0, 1], "B": [-0.61, -1.22], "C": Series(["ab", "cd"], dtype=object)}
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::typeof_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def typeof_series(val, c) -> SeriesType:
    index = typeof_impl(val.index, c)
    arrty = typeof_impl(val.values, c)
    namety = typeof_impl(val.name, c)
    assert arrty.ndim == 1
    assert arrty.layout == "C"
    return SeriesType(arrty.dtype, index, namety)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsondec.c::decodePreciseFloat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsondec.c]
JSOBJ FASTCALL_MSVC decodePreciseFloat(struct DecoderState *ds) {
  char *end;
  double value;
  errno = 0;

  value = strtod(ds->start, &end);

  if (errno == ERANGE) {
    return SetError(ds, -1, "Range error when decoding numeric as double");
  }

  ds->start = end;
  return ds->dec->newDouble(ds->prv, value);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py::get_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py]
def get_dtype(obj) -> DtypeObj:
    if isinstance(obj, DataFrame):
        # Note: we are assuming only one column
        return obj.dtypes.iat[0]
    else:
        return obj.dtype
```
