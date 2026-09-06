# pandas-80 :: tacm-dyn-l4

query: BUG: Series/Frame invert dtypes (#31183)

## selected nodes

- rank=1 layer=FILE tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py
- rank=2 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=CLASS tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/computation/test_eval.py::TestEval file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/computation/test_eval.py
- rank=4 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes.time_frame_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=5 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=6 layer=CLASS tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::TestAdditionSubtraction file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py
- rank=7 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=8 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::check_iris_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=9 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=10 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=11 layer=CLASS tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_unary.py::TestDataFrameUnaryOperators file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_unary.py
- rank=12 layer=CLASS tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_fillna.py::TestFillnaPad file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_fillna.py
- rank=13 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::FilterBinOp.invert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=14 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::ConditionBinOp.invert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=15 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArrayNaResult.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=16 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_get file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=17 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py
- rank=18 layer=FILE tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py
- rank=19 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=20 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.to_records file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=21 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.combiner file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=22 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=23 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=24 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=25 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::FilterBinOp.generate_filter_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=26 layer=FILE tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=27 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=28 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=29 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=30 layer=CLASS tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_dtypes.py::TestDataFrameDataTypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_dtypes.py
- rank=31 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py
- rank=32 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=33 layer=FUNCTION tokens=229 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::_wrap_transform_general_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=34 layer=CLASS tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_unary.py::TestSeriesUnaryOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_unary.py
- rank=35 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::GetDtypeCounts.time_frame_get_dtype_counts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=36 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex.__invert__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py

## context

```text
file pandas/plotting/_core.py
imports: __future__, importlib, typing, pandas, collections, types, matplotlib, numpy
defines: PlotAccessor, holds_integer, hist_series, hist_frame, boxplot, boxplot_frame, boxplot_frame_groupby, _load_backend, _get_plot_backend

class DataFrame(NDFrame, OpsMixin):  [pandas/core/frame.py:269]
methods: T, _align_for_op, _append_internal, _arith_method
         _arith_method_with_reindex, _arith_op
         _box_col_values, _can_fast_transpose, _cmp_method
         _combine_frame, _construct_result, _constructor
         _constructor_from_mgr
         _constructor_sliced_from_mgr, _dict_round
         _dispatch_frame_op, _ensure_valid_index
         _flex_arith_method, _flex_cmp_method
         _from_arrays, _get_agg_axis, _get_column_array
         _get_data, _get_item, _get_value
         _get_values_for_csv, _getitem_bool_array
         _getitem_multilevel, _gotitem, _info_repr
         _is_homogeneous_type, _iset_item, _iset_item_mgr
         _iset_not_inplace, _iter_column_arrays, _ixs
         _maybe_align_series_as_frame, _reduce
         _reduce_axis1, _reindex_multi
         _replace_columnwise, _repr_fits_horizontal_
         _repr_fits_vertical_, _repr_html_
         _sanitize_column, _series, _series_round
         _set_item, _set_item_frame_value, _set_item_mgr
         _set_value, _setitem_array, _setitem_frame
         _setitem_slice, _should_reindex_frame_op
         _to_dict_of_blocks, _values, add, aggregate, all
         all, all, all, any, any, any, any, apply, assign
         axes, blk_func, c, check_int_infer_dtype, combine
         combine_first, combiner, compare, corr, corrwith
         count, cov, create_index, cummax, cummin, cumprod
         cumsum, diff, dot, dot, dot, drop, drop, drop
         drop, drop_duplicates, drop_duplicates
         drop_duplicates, drop_duplicates, dropna, dropna
         dropna, dtype_predicate, duplicated, eq, eval
         eval, eval, explode, f, f, floordiv, from_arrow
         from_dict, from_records, func, ge, groupby, gt
         idxmax, idxmin, igetitem, infer, info, insert
         isetitem, isin, isin_, isna, isnull, items
         iterrows, itertuples, join, kurt, kurt, kurt
         kurt, le, lt, map, max, max, max, max
         maybe_reorder, mean, mean, mean, mean, median
         median, median, median, melt, memory_usage, merge
         min, min, min, min, mod, mode, mul, ne, nlargest
         notna, notnull, nsmallest, nunique, pivot
         pivot_table, pop, pow, predicate, prod, quantile
         quantile, quantile, quantile, query, query, query
         query, radd, reindex, rename, rename, rename
         rename, reorder_levels, reset_index, reset_index
         reset_index, reset_index, rfloordiv, rmod, rmul
         round, rpow, rsub, rtruediv, select_dtypes, sem
         sem, sem, sem, set_axis, set_index, set_index
         set_index, shape, shift, skew, skew, skew, skew
         sort_index, sort_index, sort_index, sort_index
         sort_values, sort_values, sort_values, stack, std
         std, std, std, style, sub, sum, swaplevel
         to_dict, to_dict, to_dict, to_dict, to_dict
         to_feather, to_html, to_html, to_html, to_iceberg
         to_markdown, to_markdown, to_markdown
         to_markdown, to_numpy, to_orc, to_orc, to_orc
         to_orc, to_parquet, to_parquet, to_parquet
         to_period, to_records, to_series, to_stata
         to_string, to_string, to_string, to_timestamp
         to_xml, to_xml, to_xml, transform, transpose
         truediv, unstack, update, value_counts, values
         var, var, var, var, __arrow_c_stream__
         __dataframe__, __divmod__, __getitem__, __init__
         __len__, __matmul__, __matmul__, __matmul__
         __rdivmod__, __repr__, __rmatmul__, __setitem__

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

    def time_frame_dtypes(self):
        self.df.dtypes

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

class TestAdditionSubtraction:  [tests/arithmetic/test_numeric.py:903]
methods: test_add_frames, test_add_series
         test_datetime64_with_index, test_divmod
         test_frame_operators
         test_frame_operators_col_align
         test_frame_operators_empty_like
         test_frame_operators_none_to_nan
         test_series_divmod_zero
         test_series_frame_radd_bug
         test_series_operators_arithmetic
         test_series_operators_compare

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

class TestDataFrameUnaryOperators:  [tests/frame/test_unary.py:10]
methods: test_invert, test_invert_empty_not_input
         test_invert_mixed, test_neg_numeric
         test_neg_object, test_neg_raises
         test_pos_numeric, test_pos_object
         test_pos_object_raises, test_pos_raises
         test_unary_nullable

class TestFillnaPad:  [series/methods/test_fillna.py:853]
methods: test_datetime64tz_fillna_round_issue
         test_ffill_mixed_dtypes_without_missing_data
         test_fillna_bug, test_fillna_int
         test_fillna_parr, test_pad_nan
         test_series_fillna_limit
         test_series_pad_backfill_limit

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

file plotting/_matplotlib/hist.py
imports: __future__, typing, numpy, pandas, matplotlib
defines: HistPlot, KdePlot, _grouped_plot, _grouped_hist, plot_group, hist_series, hist_frame

    def __invert__(self) -> Self:
        if not self.size:
            # inv fails with 0 len
            return self.copy(deep=False)

        new_data = self._mgr.apply(operator.invert)
        res = self._constructor_from_mgr(new_data, axes=new_data.axes)
        return res.__finalize__(self, method="__invert__")

    def to_records(
        self, index: bool = True, column_dtypes=None, index_dtypes=None
    ) -> np.rec.recarray:
        """
    # ... truncated

        def combiner(x: Series, y: Series):
            # GH#60128 The combiner is supposed to preserve EA Dtypes.
            return y if y.name not in self.columns else y.where(x.isna(), x)

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

file pandas/core/series.py
imports: __future__, collections, functools, operator, sys, typing, warnings, numpy
defines: Series

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

class TestDataFrameDataTypes:  [frame/methods/test_dtypes.py:17]
methods: test_datetime_with_tz_dtypes
         test_dtypes_are_correct_after_column_slice
         test_dtypes_are_correct_after_groupby_last
         test_dtypes_gh8722, test_dtypes_timedeltas
         test_empty_frame_dtypes
         test_frame_apply_np_array_return_type

class Dtypes:  [asv_bench/benchmarks/frame_methods.py:545]
methods: setup, time_frame_dtypes

# --- Layer 04: Variable context ---
# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: _str_get [_arrow_string_mixins.py]
  called by: __invert__ [array.py]

# call-chain context
  called by: _str_get [_arrow_string_mixins.py]
  called by: __invert__ [array.py]

# call-chain context
  called by: time_to_records [frame_methods.py]
  called by: time_to_records_multiindex [frame_methods.py]

# call-chain context
  called by: invert [pytables.py]
  called by: evaluate [pytables.py]

# call-chain context
  called by: setup [dtypes.py]
  called by: diff [algorithms.py]

```
