# pandas-80 :: tacm-full

query: BUG: Series/Frame invert dtypes (#31183)

## selected nodes

- rank=1 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::check_iris_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=2 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=3 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes.time_frame_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=4 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=5 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_get file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=6 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=7 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::FilterBinOp.invert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=8 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=9 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::ConditionBinOp.invert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=10 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=11 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::FilterBinOp.generate_filter_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=12 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=13 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=14 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::_wrap_transform_general_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=15 layer=FUNCTION tokens=243 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py::TestFromScalar.constructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py
- rank=16 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=17 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocWithEllipsis.obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=18 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArrayNaResult.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=19 layer=FUNCTION tokens=888 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::stack_v3 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=20 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py
- rank=21 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py::_BaseInfo.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py
- rank=22 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py::SeriesInfo.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::check_iris_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py]
def check_iris_frame(frame: DataFrame):
    pytype = frame.dtypes.iloc[0].type
    row = frame.iloc[0]
    assert issubclass(pytype, np.floating)
    tm.assert_series_equal(
        row, Series([5.1, 3.5, 1.4, 0.2, "Iris-setosa"], index=frame.columns, name=0)
    )
    assert frame.shape in ((150, 5), (8, 5))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py]
    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.
        StringMethods.len : Compute the length of each element in the Series/Index.

        Examples
        --------
        >>> import pyarrow as pa
        >>> s = pd.Series(
        ...     [
        ...         [1, 2, 3],
        ...         [3],
        ...     ],
        ...     dtype=pd.ArrowDtype(pa.list_(pa.int64())),
        ... )
        >>> s.list.len()
        0    3
        1    1
        dtype: int32[pyarrow]
        """
        from pandas import Series

        value_lengths = pc.list_value_length(self._pa_array)
        return Series(
            value_lengths,
            dtype=ArrowDtype(value_lengths.type),
            index=self._data.index,
            name=self._data.name,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes.time_frame_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_frame_dtypes(self):
        self.df.dtypes

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py]
    def len(self):
        """
        Compute the length of each element in the Series/Index.

        The element may be a sequence (such as a string, tuple or list) or a collection
        (such as a dictionary).

        Returns
        -------
        Series or Index of int
            A Series or Index of integer values indicating the length of each
            element in the Series or Index.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.

        Examples
        --------
        Returns the length (number of characters) in a string. Returns the
        number of entries for dictionaries, lists or tuples.

        >>> s = pd.Series(
        ...     ["dog", "", 5, {"foo": "bar"}, [2, 3, 5, 7], ("one", "two", "three")]
        ... )
        >>> s
        0                  dog
        1
        2                    5
        3       {'foo': 'bar'}
        4         [2, 3, 5, 7]
        5    (one, two, three)
        dtype: object
        >>> s.str.len()
        0    3.0
        1    0.0
        2    NaN
        3    1.0
        4    4.0
        5    3.0
        dtype: float64
        """
        result = self._data.array._str_len()
        return self._wrap_result(result, returns_string=False)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__invert__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def __invert__(self) -> SparseArray:
        return self._unary_method(operator.invert)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::FilterBinOp.invert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py]
    def invert(self) -> Self:
        """invert the filter"""
        if self.filter is not None:
            self.filter = (
                self.filter[0],
                self.generate_filter_op(invert=True),
                self.filter[2],
            )
        return self

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::ConditionBinOp.invert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py]
    def invert(self):
        """invert the condition"""
        # if self.condition is not None:
        #    self.condition = "~(%s)" % self.condition
        # return self
        raise NotImplementedError(
            "cannot use an invert condition when passing to numexpr"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::FilterBinOp.generate_filter_op [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py]
    def generate_filter_op(self, invert: bool = False):
        if (self.op == "!=" and not invert) or (self.op == "==" and invert):
            return lambda axis, vals: ~axis.isin(vals)
        else:
            return lambda axis, vals: axis.isin(vals)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.__invert__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def __invert__(self) -> Self:
        if not self.size:
            # inv fails with 0 len
            return self.copy(deep=False)

        new_data = self._mgr.apply(operator.invert)
        res = self._constructor_from_mgr(new_data, axes=new_data.axes)
        return res.__finalize__(self, method="__invert__")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py::TestFromScalar.constructor [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py]
    def constructor(self, frame_or_series, box):
        extra = {"index": range(2)}
        if frame_or_series is DataFrame:
            extra["columns"] = ["A"]

        if box is None:
            return functools.partial(frame_or_series, **extra)

        elif box is dict:
            if frame_or_series is Series:
                return lambda x, **kwargs: frame_or_series(
                    {0: x, 1: x}, **extra, **kwargs
                )
            else:
                return lambda x, **kwargs: frame_or_series({"A": x}, **extra, **kwargs)
        elif frame_or_series is Series:
            return lambda x, **kwargs: frame_or_series([x, x], **extra, **kwargs)
        else:
            return lambda x, **kwargs: frame_or_series({"A": [x, x]}, **extra, **kwargs)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocWithEllipsis.obj [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py]
    def obj(self, series_with_simple_index, frame_or_series):
        obj = series_with_simple_index
        if frame_or_series is not Series:
            obj = obj.to_frame()
        return obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArrayNaResult.__invert__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def __invert__(self) -> Self:
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::stack_v3 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
def stack_v3(frame: DataFrame, level: list[int]) -> Series | DataFrame:
    if frame.columns.nunique() != len(frame.columns):
        raise ValueError("Columns with duplicate values are not supported in stack")
    if not len(level):
        return frame
    set_levels = set(level)
    stack_cols = frame.columns._drop_level_numbers(
        [k for k in range(frame.columns.nlevels - 1, -1, -1) if k not in set_levels]
    )

    result: Series | DataFrame
    if not isinstance(frame.columns, MultiIndex):
        # GH#58817 Fast path when we're stacking the columns of a non-MultiIndex.
        # When columns are homogeneous EAs, we pass through object
        # dtype but this is still slightly faster than the normal path.
        if len(frame.columns) > 0 and frame._is_homogeneous_type:
            dtype = frame._mgr.blocks[0].dtype
        else:
            dtype = None
        result = frame._constructor_sliced(
            frame._values.reshape(-1, order="F"), dtype=dtype
        )
    else:
        result = stack_reshape(frame, level, set_levels, stack_cols)

    # Construct the correct MultiIndex by combining the frame's index and
    # stacked columns.
    ratio = 0 if frame.empty else len(result) // len(frame)

    index_levels: list | FrozenList
    if isinstance(frame.index, MultiIndex):
        index_levels = frame.index.levels
        index_codes = list(np.tile(frame.index.codes, (1, ratio)))
    else:
        codes, uniques = factorize(frame.index, use_na_sentinel=False)
        index_levels = [uniques]
        index_codes = list(np.tile(codes, (1, ratio)))

    if len(level) > 1:
        # Arrange columns in the order we want to take them, e.g. level=[2, 0, 1]
        sorter = np.argsort(level)
        assert isinstance(stack_cols, MultiIndex)
        ordered_stack_cols = stack_cols._reorder_ilevels(sorter)
    else:
        ordered_stack_cols = stack_cols  # type: ignore[assignment]
    ordered_stack_cols_unique = ordered_stack_cols.unique()
    if isinstance(ordered_stack_cols, MultiIndex):
        column_levels = ordered_stack_cols.levels
        column_codes = ordered_stack_cols.drop_duplicates().codes
    else:
        column_levels = [ordered_stack_cols_unique]
        column_codes = [factorize(ordered_stack_cols_unique, use_na_sentinel=False)[0]]

    # error: Incompatible types in assignment (expression has type "list[ndarray[Any,
    # dtype[Any]]]", variable has type "FrozenList")
    column_codes = [np.repeat(codes, len(frame)) for codes in column_codes]  # type: ignore[assignment]
    result.index = MultiIndex(
        levels=index_levels + column_levels,
        codes=index_codes + column_codes,
        names=frame.index.names + list(ordered_stack_cols.names),
        verify_integrity=False,
    )

    # sort result, but faster than calling sort_index since we know the order we need
    len_df = len(frame)
    n_uniques = len(ordered_stack_cols_unique)
    indexer = np.arange(n_uniques)
    idxs = np.tile(len_df * indexer, len_df) + np.repeat(np.arange(len_df), n_uniques)
    result = result.take(idxs)

    # Reshape/rename if needed and dropna
    if result.ndim == 2 and frame.columns.nlevels == len(level):
        if len(result.columns) == 0:
            result = Series(index=result.index)
        else:
            result = result.iloc[:, 0]
    if result.ndim == 1:
        result.name = None

    return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.__invert__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py]
    def __invert__(self) -> NumpyExtensionArray:
        return type(self)(~self._ndarray)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py::_BaseInfo.dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py]
    def dtypes(self) -> Iterable[Dtype]:
        """
        Dtypes.

        Returns
        -------
        dtypes : sequence
            Dtype of each of the DataFrame's columns (or one series column).
        """

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py::SeriesInfo.dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py]
    def dtypes(self) -> Iterable[Dtype]:
        return [self.data.dtypes]
```
