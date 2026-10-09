# pandas-80 :: tacm

query: BUG: Series/Frame invert dtypes (#31183)

## selected nodes

- rank=1 layer=FILE tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py
- rank=2 layer=FILE tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py
- rank=3 layer=FILE tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=4 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FILE tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/__init__.py
- rank=6 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=7 layer=CLASS tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/computation/test_eval.py::TestEval file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/computation/test_eval.py
- rank=8 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=9 layer=CLASS tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py::IOArgs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py
- rank=10 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes.time_frame_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=11 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=12 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=13 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=14 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=15 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=16 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::check_iris_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=17 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=18 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=19 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._constructor_expanddim file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=20 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.to_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=21 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::FilterBinOp.invert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=22 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::ConditionBinOp.invert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=23 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArrayNaResult.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=24 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_get file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=25 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py
- rank=26 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=27 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=28 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=29 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=30 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::FilterBinOp.generate_filter_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=31 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py
- rank=32 layer=FUNCTION tokens=229 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::_wrap_transform_general_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=33 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=34 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py::TestFromScalar.constructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py
- rank=35 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.case_when file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=36 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::GetDtypeCounts.time_frame_get_dtype_counts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=37 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=38 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocWithEllipsis.obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=39 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::stack_v3 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=40 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::SparseSeriesToFrame.time_series_to_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py
- rank=41 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=42 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py::_BaseInfo.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py
- rank=43 layer=FUNCTION tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_set file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=44 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Ops2.time_frame_series_dot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=45 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_quantile.py::TestQuantileExtensionDtype.obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_quantile.py
- rank=46 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py::_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py

## context

```text
file pandas/plotting/_core.py
imports: __future__, importlib, typing, pandas, collections, types, matplotlib, numpy
defines: PlotAccessor, holds_integer, hist_series, hist_frame, boxplot, boxplot_frame, boxplot_frame_groupby, _load_backend, _get_plot_backend

file plotting/_matplotlib/hist.py
imports: __future__, typing, numpy, pandas, matplotlib
defines: HistPlot, KdePlot, _grouped_plot, _grouped_hist, plot_group, hist_series, hist_frame

file pandas/core/series.py
imports: __future__, collections, functools, operator, sys, typing, warnings, numpy
defines: Series

file pandas/core/frame.py
imports: __future__, collections, functools, io, itertools, operator, sys, typing
defines: DataFrame, _from_nested_dict, _reindex_for_setitem

file core/dtypes/__init__.py
imports: —
defines: —

class Series(base.IndexOpsMixin, NDFrame):  # type: ignore[misc]  [pandas/core/series.py:211]
methods: _align_for_op, _append_internal, _arith_method, _binop
         _can_hold_na, _cmp_method, _construct_result
         _construct_result, _construct_result
         _constructor, _constructor_expanddim
         _constructor_expanddim_from_mgr
         _constructor_from_mgr, _flex_method
         _get_rows_with_mask, _get_value
         _get_values_tuple, _get_with, _gotitem
         _init_dict, _ixs, _logical_method
         _needs_reindex_multi, _reduce, _references
         _reindex_indexer, _set_labels, _set_name
         _set_value, _set_values, _set_with
         _set_with_engine, _slice, _values, add, aggregate
         all, any, apply, argsort, array, autocorr, axes
         between, case_when, combine, combine_first
         compare, corr, count, cov, cummax, cummin
         cumprod, cumsum, diff, divmod, dot, drop, drop
         drop, drop, drop_duplicates, drop_duplicates
         drop_duplicates, drop_duplicates, dropna, dropna
         dropna, dtype, dtypes, duplicated, eq, explode
         floordiv, from_arrow, ge, groupby, gt, idxmax
         idxmin, info, isin, isna, isnull, items, keys
         kurt, le, lt, map, max, mean, median
         memory_usage, min, mod, mode, mul, name, name, ne
         nlargest, notna, notnull, nsmallest, pop, pow
         prod, quantile, quantile, quantile, quantile
         radd, rdivmod, reindex, rename, rename, rename
         rename_axis, rename_axis, rename_axis
         rename_axis, reorder_levels, repeat, reset_index
         reset_index, reset_index, reset_index, rfloordiv
         rmod, rmul, round, rpow, rsub, rtruediv
         searchsorted, sem, set_axis, skew, sort_index
         sort_index, sort_index, sort_index, sort_values
         sort_values, sort_values, sort_values, std, sub
         sum, swaplevel, to_dict, to_dict, to_dict
         to_frame, to_markdown, to_markdown, to_markdown
         to_markdown, to_period, to_string, to_string
         to_string, to_timestamp, transform, truediv
         unique, unstack, update, values, var, __array__
         __arrow_c_stream__, __getitem__, __init__
         __len__, __matmul__, __repr__, __rmatmul__
         __setitem__

class TestEval:  [tests/computation/test_eval.py:143]
methods: test_and_logic_string_match, test_binary_arith_ops
         test_chained_cmp_op, test_check_single_invert_op
         test_complex_cmp_ops, test_compound_invert_op
         test_disallow_python_keywords
         test_disallow_scalar_bool_ops
         test_eval_keep_name, test_eval_unmatching_names
         test_float_comparison_bin_op
         test_float_truncation, test_floor_division
         test_frame_invert, test_frame_negate
         test_frame_pos, test_identical
         test_line_continuation, test_modulus, test_pow
         test_scalar_unary, test_series_invert
         test_series_negate, test_series_pos
         test_simple_cmp_ops, test_true_false_logic
         test_unary_in_array, test_unary_in_function

class Dtypes:  [asv_bench/benchmarks/frame_methods.py:545]
methods: setup, time_frame_dtypes

class IOArgs:  [pandas/io/common.py:92]
methods: —

    def time_frame_dtypes(self):
        self.df.dtypes

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

    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

    # ... truncated

    def array(self) -> ExtensionArray:
        """
        The ExtensionArray of the data backing this Series or Index.

        This property provides direct access to the underlying array data of a
        Series or Index without requiring conversion to a NumPy array. It
        returns an ExtensionArray, which is the native storage format for
        pandas extension dtypes.

        Returns
        -------
        ExtensionArray
    # ... truncated

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
    # ... truncated

def check_iris_frame(frame: DataFrame):
    pytype = frame.dtypes.iloc[0].type
    row = frame.iloc[0]
    assert issubclass(pytype, np.floating)
    tm.assert_series_equal(
        row, Series([5.1, 3.5, 1.4, 0.2, "Iris-setosa"], index=frame.columns, name=0)
    )
    assert frame.shape in ((150, 5), (8, 5))

    def __invert__(self) -> SparseArray:
        return self._unary_method(operator.invert)

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

    def _constructor_expanddim(self) -> Callable[..., DataFrame]:
        """
        Used when a manipulation result has one higher dimension as the
        original, such as Series.to_frame()
        """
        from pandas.core.frame import DataFrame

        return DataFrame

    def to_frame(self, name: Hashable = lib.no_default) -> DataFrame:
        """
        Convert Series to DataFrame.

        The resulting DataFrame contains a single column. The name of the
        column can be set using the ``name`` parameter; otherwise it
        defaults to the Series' name.

        Parameters
        ----------
        name : object, optional
            The passed name should substitute for the series name (if it has
    # ... truncated

    def invert(self) -> Self:
        """invert the filter"""
        if self.filter is not None:
            self.filter = (
                self.filter[0],
                self.generate_filter_op(invert=True),
                self.filter[2],
            )
        return self

    def invert(self):
        """invert the condition"""
        # if self.condition is not None:
        #    self.condition = "~(%s)" % self.condition
        # return self
        raise NotImplementedError(
            "cannot use an invert condition when passing to numexpr"
        )

    def __invert__(self) -> Self:
        raise AbstractMethodError(self)

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

    def __invert__(self) -> NumpyExtensionArray:
        return type(self)(~self._ndarray)

    def __invert__(self) -> Self:
        if not self.size:
            # inv fails with 0 len
            return self.copy(deep=False)

        new_data = self._mgr.apply(operator.invert)
        res = self._constructor_from_mgr(new_data, axes=new_data.axes)
        return res.__finalize__(self, method="__invert__")

    def __invert__(self) -> Index:
        # GH#8875
        return self._unary_method(operator.inv)

def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

    def __invert__(self) -> Self:
        return self._simple_new(~self._data, self._mask.copy())

    def generate_filter_op(self, invert: bool = False):
        if (self.op == "!=" and not invert) or (self.op == "==" and invert):
            return lambda axis, vals: ~axis.isin(vals)
        else:
            return lambda axis, vals: axis.isin(vals)

    def __invert__(self) -> Expression:
        return Expression(
            lambda df: ~self._eval_expression(df),
            f"~{self._repr_str}",
            needs_parenthese=True,
        )

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

    def case_when(
        self,
        caselist: list[
            tuple[
                ArrayLike | Callable[[Series], Series | np.ndarray | Sequence[bool]],
                ArrayLike | Scalar | Callable[[Series], Series | np.ndarray],
            ],
        ],
    ) -> Series:
        """
    # ... truncated

    def time_frame_get_dtype_counts(self):
        with warnings.catch_warnings(record=True):
            self.df.dtypes.value_counts()

    def __invert__(self) -> Self:
        if len(self) == 0:
            return self.copy()
        rng = range(~self.start, ~self.stop, -self.step)
        return self._simple_new(rng, name=self.name)

    def obj(self, series_with_simple_index, frame_or_series):
        obj = series_with_simple_index
        if frame_or_series is not Series:
            obj = obj.to_frame()
        return obj

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
    # ... truncated

    def time_series_to_frame(self):
        pd.DataFrame(self.series)

    def __setitem__(self, key, value) -> None:
        if not CHAINED_WARNING_DISABLED:
            if sys.getrefcount(self) <= REF_COUNT and not com.is_local_in_caller_frame(
                self
            ):
                warnings.warn(
                    _chained_assignment_msg, ChainedAssignmentError, stacklevel=2
                )

        check_dict_or_set_indexers(key)
        key = com.apply_if_callable(key, self)

    # ... truncated

    def dtypes(self) -> Iterable[Dtype]:
        """
        Dtypes.

        Returns
        -------
        dtypes : sequence
            Dtype of each of the DataFrame's columns (or one series column).
        """

        def _check_set(df, cond, check_dtypes=True):
            dfi = df.copy()
            econd = cond.reindex_like(df).fillna(True).infer_objects()
            expected = dfi.mask(~econd)

            result = dfi.where(cond, np.nan, inplace=True)
            assert result is dfi
            tm.assert_frame_equal(dfi, expected)

            # dtypes (and confirm upcasts)x
            if check_dtypes:
                for k, v in df.dtypes.items():
                    if issubclass(v.type, np.integer) and not cond[k].all():
                        v = np.dtype("float64")
                    assert dfi[k].dtype == v

    def time_frame_series_dot(self):
        self.df.dot(self.s)

    def obj(self, index, frame_or_series):
        # bc index is not always an Index (yet), we need to re-patch .name
        obj = frame_or_series(index).copy()

        if frame_or_series is Series:
            obj.name = "A"
        else:
            obj.columns = ["A"]
        return obj

def _array(_frame):
    return _frame["A"].to_numpy()
```
