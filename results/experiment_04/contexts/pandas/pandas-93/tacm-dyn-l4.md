# pandas-93 :: tacm-dyn-l4

query: BUG: DTI/TDI/PI `where` accepting non-matching dtypes (#30791)

## selected nodes

- rank=1 layer=FILE tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py
- rank=2 layer=CLASS tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=3 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=4 layer=CLASS tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=5 layer=FILE tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=6 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_get file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=7 layer=FILE tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=8 layer=CLASS tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py::TestToTimestamp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_to_timestamp.py
- rank=9 layer=CLASS tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py::TestAllowNonNano file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py
- rank=10 layer=FUNCTION tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_set file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=11 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=12 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.select_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=13 layer=FILE tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py
- rank=14 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=15 layer=FILE tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=16 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=17 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=18 layer=FILE tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/__init__.py
- rank=19 layer=FILE tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/api.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/api.py
- rank=20 layer=CLASS tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=21 layer=CLASS tokens=394 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::TestPeriodIndexArithmetic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py
- rank=22 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.combiner file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=23 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py::TestWhere file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py
- rank=24 layer=CLASS tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::TestTimedelta64ArithmeticUnsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=25 layer=FUNCTION tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_require_matching_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=26 layer=FILE tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=27 layer=CLASS tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_indexing.py::TestWhere file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_indexing.py
- rank=28 layer=CLASS tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::TestPeriodIndexSeriesMethods file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py
- rank=29 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=30 layer=FILE tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=31 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=32 layer=CLASS tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestWhere file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=33 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Where.time_where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=34 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::_assign_where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=35 layer=CLASS tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_indexing.py::TestWhere file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_indexing.py
- rank=36 layer=FILE tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py
- rank=37 layer=FILE tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/generic.py
- rank=38 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtypeType file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=39 layer=CLASS tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py::Dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py
- rank=40 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py::Dtypes.time_pandas_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py

## context

```text
file core/computation/expressions.py
imports: __future__, operator, typing, warnings, numpy, pandas, numexpr
defines: set_use_numexpr, set_numexpr_threads, _evaluate_standard, _can_use_numexpr, _evaluate_numexpr, _where_standard, _where_numexpr, _has_bool_dtype, _bool_arith_fallback, evaluate, where, set_test_mode, _store_test_result, get_test_result

class TestDatetimeIndexArithmetic:  [tests/arithmetic/test_datetime64.py:2021]
methods: test_dta_add_sub_index, test_dti_add_series
         test_dti_add_tdi
         test_dti_addsub_object_arraylike
         test_dti_addsub_offset_arraylike
         test_dti_iadd_tdi, test_dti_isub_tdi
         test_dti_sub_tdi
         test_ops_nat_mixed_datetime64_timedelta64
         test_sub_dti_dti
         test_timedelta64_equal_timedelta_supported_ops
         test_ufunc_coercions, timedelta64

    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

class TestDataFrameIndexingWhere:  [frame/indexing/test_where.py:48]
methods: _check_align, _check_get, _check_set, create
         test_df_where_change_dtype
         test_df_where_with_category, test_where_align
         test_where_alignment, test_where_array_like
         test_where_axis, test_where_axis_multiple_dtypes
         test_where_axis_with_upcast, test_where_bug
         test_where_bug_mixed
         test_where_bug_transposition, test_where_callable
         test_where_categorical_filtering
         test_where_complex
         test_where_dataframe_col_match
         test_where_datetime, test_where_datetimelike_noop
         test_where_ea_other
         test_where_empty_df_and_empty_cond_having_non_bool_dtypes
         test_where_get
         test_where_interval_fullop_downcast
         test_where_interval_noop, test_where_invalid
         test_where_invalid_input_multiple
         test_where_invalid_input_single
         test_where_ndframe_align, test_where_none
         test_where_series_slicing, test_where_set
         test_where_tz_values, test_where_upcasting

file pandas/core/construction.py
imports: __future__, typing, numpy, pandas, collections
defines: array, extract_array, extract_array, extract_array, ensure_wrapped_if_datetimelike, sanitize_masked_array, sanitize_array, range_to_ndarray, _sanitize_non_ordered, _sanitize_ndim, _sanitize_str_dtypes, _maybe_repeat, _try_cast

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

file asv_bench/benchmarks/frame_methods.py
imports: string, warnings, numpy, pandas
defines: AsType, Clip, GetNumericData, Reindex, Rename, Iteration, ToString, ToHTML, ToDict, ToNumpy, ToRecords, Repr, MaskBool, Isnull, Fillna, Dropna, Isna, Count, Apply, Dtypes, Equals, Interpolate, Shift, Nunique, SeriesNuniqueWithNan, Duplicated, XS, SortValues, SortMultiKey, Quantile, Rank, GetDtypeCounts, NSort, Describe, MemoryUsage, Round, Where, FindValidIndex, Update

class TestToTimestamp:  [period/methods/test_to_timestamp.py:18]
methods: test_to_timestamp_1703, test_to_timestamp_freq
         test_to_timestamp_non_contiguous
         test_to_timestamp_pi_combined
         test_to_timestamp_pi_mult
         test_to_timestamp_pi_nat
         test_to_timestamp_preserve_name
         test_to_timestamp_quarterly_bug

class TestAllowNonNano:  [tests/frame/test_constructors.py:3395]
methods: arr, as_td, test_dti_tdi_allow_non_nano
         test_frame_allow_non_nano
         test_frame_from_dict_allow_non_nano
         test_index_allow_non_nano
         test_series_allow_non_nano

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

    def select_dtypes(self, include=None, exclude=None) -> DataFrame:
        """
        Return a subset of the DataFrame's columns based on the column dtypes.

        This method allows for filtering columns based on their data types.
        It is useful when working with heterogeneous DataFrames where operations
        need to be performed on a specific subset of data types.

        Parameters
        ----------
        include, exclude : scalar or list-like
            A selection of dtypes or strings to be included/excluded. At least
    # ... truncated

file asv_bench/benchmarks/dtypes.py
imports: string, numpy, pandas, pandas_vb_common
defines: Dtypes, DtypesInvalid, SelectDtypes, CheckDtypes

    def tdi(self, monotonic):
        tdi = timedelta_range("1 Day", periods=10)
        if monotonic == "decreasing":
            tdi = tdi[::-1]
        elif monotonic is None:
            taker = np.arange(10, dtype=np.intp)
            np.random.default_rng(2).shuffle(taker)
            tdi = tdi.take(taker)
        return tdi

file core/dtypes/dtypes.py
imports: __future__, datetime, decimal, re, typing, warnings, zoneinfo, numpy
defines: PandasExtensionDtype, CategoricalDtypeType, CategoricalDtype, DatetimeTZDtype, PeriodDtype, IntervalDtype, NumpyEADtype, BaseMaskedDtype, SparseDtype, ArrowDtype

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

class Where:  [asv_bench/benchmarks/frame_methods.py:828]
methods: setup, time_where

file core/dtypes/__init__.py
imports: —
defines: —

file core/dtypes/api.py
imports: pandas
defines: —

class TestDatetimeIndexComparisons:  [tests/arithmetic/test_datetime64.py:408]
methods: test_comparators, test_comparison_tzawareness_compat
         test_comparison_tzawareness_compat_scalars
         test_dti_cmp_datetimelike, test_dti_cmp_list
         test_dti_cmp_nat
         test_dti_cmp_nat_behaves_like_float_cmp_nan
         test_dti_cmp_object_dtype, test_dti_cmp_str
         test_dti_cmp_tdi_tzawareness
         test_nat_comparison_tzawareness
         test_scalar_comparison_tzawareness

class TestPeriodIndexArithmetic:  [tests/arithmetic/test_period.py:493]
methods: test_add_iadd_timedeltalike_annual
         test_parr_add_iadd_parr_raises
         test_parr_add_sub_index
         test_parr_add_sub_invalid
         test_parr_add_sub_object_array
         test_parr_add_sub_td64_nat
         test_parr_add_sub_tdt64_nat_array
         test_parr_add_sub_timedeltalike_freq_mismatch_daily
         test_parr_add_timedeltalike_minute_gt1
         test_parr_add_timedeltalike_mismatched_freq_hourly
         test_parr_add_timedeltalike_tick_gt1
         test_parr_sub_pi_mismatched_freq
         test_parr_sub_td64array
         test_period_add_timestamp_raises
         test_pi_add_iadd_int
         test_pi_add_iadd_timedeltalike_M
         test_pi_add_iadd_timedeltalike_daily
         test_pi_add_iadd_timedeltalike_hourly
         test_pi_add_intarray, test_pi_add_offset_array
         test_pi_add_offset_n_gt1
         test_pi_add_offset_n_gt1_not_divisible
         test_pi_add_sub_int_array_freqn_gt1
         test_pi_add_sub_td64_array_non_tick_raises
         test_pi_add_sub_td64_array_tick
         test_pi_add_sub_timedeltalike_freq_mismatch_annual
         test_pi_add_sub_timedeltalike_freq_mismatch_monthly
         test_pi_sub_intarray, test_pi_sub_intlike
         test_pi_sub_isub_int, test_pi_sub_isub_offset
         test_pi_sub_isub_pi
         test_pi_sub_isub_timedeltalike_daily
         test_pi_sub_isub_timedeltalike_hourly
         test_pi_sub_offset_array, test_pi_sub_pi_with_nat
         test_sub_n_gt_1_offsets, test_sub_n_gt_1_ticks

        def combiner(x: Series, y: Series):
            # GH#60128 The combiner is supposed to preserve EA Dtypes.
            return y if y.name not in self.columns else y.where(x.isna(), x)

class TestWhere:  [indexes/period/test_indexing.py:534]
methods: test_where, test_where_invalid_dtypes
         test_where_mismatched_nat, test_where_other

class TestTimedelta64ArithmeticUnsorted:  [tests/arithmetic/test_timedelta64.py:273]
methods: _check, test_addition_ops, test_dti_tdi_numeric_ops
         test_subtraction_ops
         test_subtraction_ops_with_tz
         test_td64_op_with_list
         test_tda_add_dt64_object_array
         test_tda_add_sub_index
         test_tdi_iadd_timedeltalike
         test_tdi_isub_timedeltalike
         test_tdi_ops_attributes, test_timedelta
         test_timedelta_tick_arithmetic
         test_ufunc_coercions

    def _maybe_require_matching_dtypes(
        self, left_join_keys: list[ArrayLike], right_join_keys: list[ArrayLike]
    ) -> None:
        # Overridden by AsOfMerge
        pass

file core/computation/pytables.py
imports: __future__, ast, decimal, functools, typing, numpy, pandas
defines: PyTablesScope, Term, Constant, BinOp, FilterBinOp, JointFilterBinOp, ConditionBinOp, JointConditionBinOp, UnaryOp, PyTablesExprVisitor, PyTablesExpr, TermValue, _validate_where, maybe_expression

class TestWhere:  [indexes/datetimes/test_indexing.py:121]
methods: test_where_doesnt_retain_freq
         test_where_freq_invalidation
         test_where_invalid_dtypes
         test_where_mismatched_nat, test_where_other
         test_where_tz

class TestPeriodIndexSeriesMethods:  [tests/arithmetic/test_period.py:1300]
methods: _check, test_parr_ops_errors, test_pi_offset_errors
         test_pi_ops, test_pi_ops_array_int
         test_pi_ops_nat, test_pi_ops_offset
         test_pi_sub_pdnat, test_pi_sub_period
         test_pi_sub_period_nat

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

    def time_where(self, inplace, dtype):
        self.df.where(self.mask, other=0.0, inplace=inplace)

def dtype():
    return JSONDtype()

# --- Layer 04: Variable context ---
# call-chain context
  called by: _partial_date_slice [datetimelike.py]
  called by: get_loc [datetimes.py]

# call-chain context
  called by: time_select_dtype_int_include [dtypes.py]
  called by: time_select_dtype_int_exclude [dtypes.py]

# call-chain context
  called by: setup [algorithms.py]
  called by: setup [algorithms.py]

# call-chain context
  called by: __init__ [merge.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: setup [dtypes.py]
  called by: diff [algorithms.py]

```
