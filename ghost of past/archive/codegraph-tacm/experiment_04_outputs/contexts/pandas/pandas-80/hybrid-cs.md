# pandas-80 :: hybrid-cs

query: BUG: Series/Frame invert dtypes (#31183)

## selected nodes

- rank=1 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=2 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::_wrap_transform_general_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=3 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py::TestGeneric.f file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py
- rank=4 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=5 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes.time_frame_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=6 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py::series_via_frame_from_dict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py
- rank=7 layer=FUNCTION tokens=222 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=8 layer=FUNCTION tokens=1501 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.convert_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=9 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::check_iris_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=10 layer=FUNCTION tokens=348 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=11 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=12 layer=FUNCTION tokens=243 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_nlargest.py::df_main_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_nlargest.py
- rank=13 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::dtype_backend_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=14 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterBegin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=15 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_get file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=16 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py::series_via_frame_from_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py
- rank=17 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py::_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py::TestGeneric.f [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py]
        def f(dtype):
            return construct(frame_or_series, shape=3, value=1, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def dtypes(self) -> DtypeObj:
        """
        Return the dtype object of the underlying data.

        Unlike ``DataFrame.dtypes``, which returns a Series of dtypes for each
        column, ``Series.dtypes`` returns a single dtype object representing
        the type of all elements in the Series.

        See Also
        --------
        DataFrame.dtypes :  Return the dtypes in the DataFrame.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> s.dtypes
        dtype('int64')
        """
        # DataFrame compatibility
        return self.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes.time_frame_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_frame_dtypes(self):
        self.df.dtypes

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py::series_via_frame_from_dict [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py]
def series_via_frame_from_dict(x, **kwargs):
    return DataFrame({"a": x}, **kwargs)["a"]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def dtype(self) -> DtypeObj:
        """
        Return the dtype object of the underlying data.

        This is the dtype of the array backing the Series (or the single dtype
        for a DataFrame column). For extension types, it returns the
        corresponding extension dtype.

        See Also
        --------
        Series.dtypes : Return the dtype object of the underlying data.
        Series.astype : Cast a pandas object to a specified dtype dtype.
        Series.convert_dtypes : Convert columns to the best possible dtypes using dtypes
            supporting pd.NA.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> s.dtype
        dtype('int64')
        """
        return self._mgr.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.convert_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def convert_dtypes(
        self,
        infer_objects: bool = True,
        convert_string: bool = True,
        convert_integer: bool = True,
        convert_boolean: bool = True,
        convert_floating: bool = True,
        dtype_backend: DtypeBackend = "numpy_nullable",
    ) -> Self:
        """
        Convert columns from numpy dtypes to the best dtypes that support ``pd.NA``.

        This finds the smallest dtype that can hold all values, or uses
        extension dtypes (e.g. nullable integer, string, boolean) so that
        missing values are represented by ``pd.NA`` instead of ``np.nan``.

        Parameters
        ----------
        infer_objects : bool, default True
            Whether object dtypes should be converted to the best possible types.
        convert_string : bool, default True
            Whether object dtypes should be converted to ``StringDtype()``.
        convert_integer : bool, default True
            Whether, if possible, conversion can be done to integer extension types.
        convert_boolean : bool, defaults True
            Whether object dtypes should be converted to ``BooleanDtypes()``.
        convert_floating : bool, defaults True
            Whether, if possible, conversion can be done to floating extension types.
            If `convert_integer` is also True, preference will be give to integer
            dtypes if the floats can be faithfully casted to integers.
        dtype_backend : {'numpy_nullable', 'pyarrow'}, default 'numpy_nullable'
            Back-end data type applied to the resultant :class:`DataFrame` or
            :class:`Series` (still experimental). Behaviour is as follows:

            * ``"numpy_nullable"``: returns nullable-dtype-backed
              :class:`DataFrame` or :class:`Series`.
            * ``"pyarrow"``: returns pyarrow-backed nullable :class:`ArrowDtype`
              :class:`DataFrame` or :class:`Series`.

            .. versionadded:: 2.0

        Returns
        -------
        Series or DataFrame
            Copy of input object with new dtype.

        See Also
        --------
        infer_objects : Infer dtypes of objects.
        to_datetime : Convert argument to datetime.
        to_timedelta : Convert argument to timedelta.
        to_numeric : Convert argument to a numeric type.

        Notes
        -----
        By default, ``convert_dtypes`` will attempt to convert a Series (or each
        Series in a DataFrame) to dtypes that support ``pd.NA``. By using the options
        ``convert_string``, ``convert_integer``, ``convert_boolean`` and
        ``convert_floating``, it is possible to turn off individual conversions
        to ``StringDtype``, the integer extension types, ``BooleanDtype``
        or floating extension types, respectively.

        For object-dtyped columns, if ``infer_objects`` is ``True``, use the inference
        rules as during normal Series/DataFrame construction.  Then, if possible,
        convert to ``StringDtype``, ``BooleanDtype`` or an appropriate integer
        or floating extension type, otherwise leave as ``object``.

        If the dtype is integer, convert to an appropriate integer extension type.

        If the dtype is numeric, and consists of all integers, convert to an
        appropriate integer extension type. Otherwise, convert to an
        appropriate floating extension type.

        In the future, as new dtypes are added that support ``pd.NA``, the results
        of this method will change to support those new dtypes.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "a": pd.Series([1, 2, 3], dtype=np.dtype("int32")),
        ...         "b": pd.Series(["x", "y", "z"], dtype=np.dtype("O")),
        ...         "c": pd.Series([True, False, np.nan], dtype=np.dtype("O")),
        ...         "d": pd.Series(["h", "i", np.nan], dtype=np.dtype("O")),
        ...         "e": pd.Series([10, np.nan, 20], dtype=np.dtype("float")),
        ...         "f": pd.Series([np.nan, 100.5, 200], dtype=np.dtype("float")),
        ...     }
        ... )

        Start with a DataFrame with default dtypes.

        >>> df
           a  b      c    d     e      f
        0  1  x   True    h  10.0    NaN
        1  2  y  False    i   NaN  100.5
        2  3  z    NaN  NaN  20.0  200.0

        >>> df.dtypes
        a      int32
        b     object
        c     object
        d     object
        e    float64
        f    float64
        dtype: object

        Convert the DataFrame to use best possible dtypes.

        >>> dfn = df.convert_dtypes()
        >>> dfn
           a  b      c     d     e      f
        0  1  x   True     h    10   <NA>
        1  2  y  False     i  <NA>  100.5
        2  3  z   <NA>  <NA>    20  200.0

        >>> dfn.dtypes
        a      Int32
        b     string
        c    boolean
        d     string
        e      Int64
        f    Float64
        dtype: object

        Start with a Series of strings and missing data represented by ``np.nan``.

        >>> s = pd.Series(["a", "b", np.nan])
        >>> s
        0      a
        1      b
        2    NaN
        dtype: str

        Obtain a Series with dtype ``StringDtype``.

        >>> s.convert_dtypes()
        0       a
        1       b
        2    <NA>
        dtype: string
        """
        check_dtype_backend(dtype_backend)
        new_mgr = self._mgr.convert_dtypes(
            infer_objects=infer_objects,
            convert_string=convert_string,
            convert_integer=convert_integer,
            convert_boolean=convert_boolean,
            convert_floating=convert_floating,
            dtype_backend=dtype_backend,
        )
        res = self._constructor_from_mgr(new_mgr, axes=new_mgr.axes)
        return res.__finalize__(self, method="convert_dtypes")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::check_iris_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py]
def check_iris_frame(frame: DataFrame):
    pytype = frame.dtypes.iloc[0].type
    row = frame.iloc[0]
    assert issubclass(pytype, np.floating)
    tm.assert_series_equal(
        row, Series([5.1, 3.5, 1.4, 0.2, "Iris-setosa"], index=frame.columns, name=0)
    )
    assert frame.shape in ((150, 5), (8, 5))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def dtypes(self):
        """
        Return the dtypes in the DataFrame.

        This returns a Series with the data type of each column.
        The result's index is the original DataFrame's columns. Columns
        with mixed types are stored with the ``object`` dtype. See
        :ref:`the User Guide <basics.dtypes>` for more.

        Returns
        -------
        pandas.Series
            The data type of each column.

        See Also
        --------
        Series.dtypes : Return the dtype object of the underlying data.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "float": [1.0],
        ...         "int": [1],
        ...         "datetime": [pd.Timestamp("20180310")],
        ...         "string": ["foo"],
        ...     }
        ... )
        >>> df.dtypes
        float              float64
        int                  int64
        datetime    datetime64[us]
        string              str
        dtype: object
        """
        data = self._mgr.get_dtypes()
        # copy=False is safe because get_dtypes() returns a new array
        return self._constructor_sliced(
            data, index=self._info_axis, dtype=np.object_, copy=False
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__invert__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py]
    def __invert__(self) -> Self:
        # This is a bit wise op for integer types
        if pa.types.is_integer(self._pa_array.type):
            return self._from_pyarrow_array(pc.bit_wise_not(self._pa_array))
        elif pa.types.is_string(self._pa_array.type) or pa.types.is_large_string(
            self._pa_array.type
        ):
            # Raise TypeError instead of pa.ArrowNotImplementedError
            raise TypeError("__invert__ is not supported for string dtypes")
        else:
            return self._from_pyarrow_array(pc.invert(self._pa_array))

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_get [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py]
        def _check_get(df, cond, check_dtypes=True):
            other1 = _safe_add(df)
            rs = df.where(cond, other1)
            rs2 = df.where(cond.values, other1)
            for k, v in rs.items():
                exp = Series(np.where(cond[k], df[k], other1[k]), index=v.index, name=k)
                tm.assert_series_equal(v, exp)
            tm.assert_frame_equal(rs, rs2)

            # dtypes
            if check_dtypes:
                assert (rs.dtypes == df.dtypes).all()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py::series_via_frame_from_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py]
def series_via_frame_from_scalar(x, **kwargs):
    return DataFrame(x, **kwargs)[0]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py::_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py]
def _array(_frame):
    return _frame["A"].to_numpy()
```
