# pandas-17 :: tacm-dyn

query: BUG: DTI/TDI.insert doing invalid casting (#33703)

## selected nodes

- rank=1 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=2 layer=CLASS tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=3 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=4 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=5 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=6 layer=CLASS tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_insert.py::TestDataFrameInsert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_insert.py
- rank=7 layer=CLASS tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py::TestVectorizedTimedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py
- rank=8 layer=CLASS tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=9 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_EastAsianTextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=10 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=11 layer=CLASS tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::TestTimedelta64ArithmeticUnsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=12 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/methods/test_insert.py::TestTimedeltaIndexInsert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/methods/test_insert.py
- rank=13 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=14 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=15 layer=CLASS tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py::TestInsert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
- rank=16 layer=CLASS tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_tz_convert.py::TestTZConvert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_tz_convert.py
- rank=17 layer=CLASS tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=18 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=19 layer=CLASS tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py::TestTimedeltaIndexShift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py
- rank=20 layer=CLASS tokens=224 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_tz_localize.py::TestTZLocalize file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_tz_localize.py
- rank=21 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.sort_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=22 layer=CLASS tokens=249 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py::TestDatetimeIndexSetOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py
- rank=23 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic.timedelta64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=24 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::make_invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=25 layer=CLASS tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py::TestAllowNonNano file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_constructors.py
- rank=26 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=27 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=28 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=29 layer=CLASS tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_formats.py::TestDatetimeIndexRendering file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_formats.py
- rank=30 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=31 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringDtype.type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py

## context

```text
file core/ops/invalid.py
imports: __future__, operator, typing, numpy, collections, pandas
defines: invalid_comparison, make_invalid_op, invalid_op

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

class TestDataFrameInsert:  [frame/indexing/test_insert.py:20]
methods: test_insert, test_insert_EA_no_warning
         test_insert_column_bug_4032
         test_insert_delete_mixed_multiindex_columns
         test_insert_frame, test_insert_int64_loc
         test_insert_with_columns_dups

class TestVectorizedTimedelta:  [indexes/timedeltas/test_scalar_compat.py:21]
methods: test_components, test_round, test_tdi_round
         test_tdi_round_invalid, test_tdi_total_seconds
         test_tdi_total_seconds_all_nat

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

    def len(self, text: str) -> int:
        """
        Calculate display width considering unicode East Asian Width
        """
        if not isinstance(text, str):
            return len(text)

        return sum(
            self._EAW_MAP.get(east_asian_width(c), self.ambiguous_width) for c in text
        )

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

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

class TestTimedeltaIndexInsert:  [timedeltas/methods/test_insert.py:18]
methods: test_insert, test_insert_castable_str, test_insert_empty
         test_insert_invalid_na
         test_insert_mismatched_types_raises
         test_insert_nat, test_insert_non_castable_str

    def len(self, text: str) -> int:
        return len(text)

    def insert(
        self,
        loc: int,
        column: Hashable,
        value: object,
        allow_duplicates: bool | lib.NoDefault = lib.no_default,
    ) -> None:
        """
    # ... truncated

class TestInsert:  [datetimes/methods/test_insert.py:18]
methods: test_insert, test_insert2, test_insert3, test_insert4
         test_insert4_no_freq, test_insert_castable_str
         test_insert_empty_preserves_freq
         test_insert_invalid_na
         test_insert_mismatched_types_raises
         test_insert_mismatched_tz
         test_insert_mismatched_tzawareness
         test_insert_nat, test_insert_non_castable_str

class TestTZConvert:  [datetimes/methods/test_tz_convert.py:21]
methods: test_dti_tz_convert_compat_timestamp
         test_dti_tz_convert_day_freq_not_preserved
         test_dti_tz_convert_dst
         test_dti_tz_convert_hour_overflow_dst
         test_dti_tz_convert_hour_overflow_dst_timestamps
         test_dti_tz_convert_trans_pos_plus_1__bug
         test_dti_tz_convert_tzlocal
         test_dti_tz_convert_utc_to_local_no_modify
         test_tz_convert_nat, test_tz_convert_roundtrip
         test_tz_convert_unsorted

class TestMaybeCastSliceBound:  [indexes/timedeltas/test_indexing.py:288]
methods: monotonic, tdi, test_maybe_cast_slice_bound_invalid_str
         test_slice_invalid_str_with_timedeltaindex

    def tdi(self, monotonic):
        tdi = timedelta_range("1 Day", periods=10)
        if monotonic == "decreasing":
            tdi = tdi[::-1]
        elif monotonic is None:
            taker = np.arange(10, dtype=np.intp)
            np.random.default_rng(2).shuffle(taker)
            tdi = tdi.take(taker)
        return tdi

class TestTimedeltaIndexShift:  [timedeltas/methods/test_shift.py:10]
methods: test_shift_no_freq, test_tdi_shift_empty
         test_tdi_shift_hours, test_tdi_shift_int
         test_tdi_shift_minutes
         test_tdi_shift_nonstandard_freq

class TestTZLocalize:  [datetimes/methods/test_tz_localize.py:32]
methods: test_dti_tz_localize, test_dti_tz_localize_ambiguous_flags
         test_dti_tz_localize_ambiguous_flags2
         test_dti_tz_localize_ambiguous_infer
         test_dti_tz_localize_ambiguous_infer2
         test_dti_tz_localize_ambiguous_infer3
         test_dti_tz_localize_ambiguous_nat
         test_dti_tz_localize_ambiguous_times
         test_dti_tz_localize_bdate_range
         test_dti_tz_localize_naive
         test_dti_tz_localize_nonexistent_raise_coerce
         test_dti_tz_localize_nonexistent_shift
         test_dti_tz_localize_nonexistent_shift_invalid
         test_dti_tz_localize_pass_dates_to_utc
         test_dti_tz_localize_roundtrip
         test_dti_tz_localize_tzlocal
         test_dti_tz_localize_utc_conversion
         test_tz_localize_invalidates_freq
         test_tz_localize_utc_copies

    def sort_values(
        self,
        by: IndexLabel,
        *,
        axis: Axis = 0,
        ascending: bool | list[bool] | tuple[bool, ...] = True,
        inplace: bool = False,
        kind: SortKind = "quicksort",
        na_position: str = "last",
        ignore_index: bool = False,
        key: ValueKeyFunc | None = None,
    ) -> DataFrame | None:
    # ... truncated

class TestDatetimeIndexSetOps:  [indexes/datetimes/test_setops.py:33]
methods: test_datetimeindex_diff, test_difference
         test_difference_freq, test_dti_intersection
         test_dti_setop_aware, test_dti_union_mixed
         test_intersection, test_intersection2
         test_intersection_bug_1708
         test_intersection_empty
         test_intersection_non_tick_no_fastpath
         test_intersection_same_timezone_different_units
         test_setops_preserve_freq
         test_symmetric_difference_same_timezone_different_units
         test_union, test_union2, test_union3
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_dataframe_index
         test_union_different_dates_same_timezone_different_units
         test_union_freq_both_none, test_union_freq_infer
         test_union_same_nonzero_timezone_different_units
         test_union_same_timezone_different_units
         test_union_with_DatetimeIndex

        def timedelta64(*args):
            # see casting notes in NumPy gh-12927
            return np.sum(list(map(np.timedelta64, args, intervals)))

def make_invalid_op(name: str) -> Callable[..., NoReturn]:
    """
    Return a binary method that always raises a TypeError.

    Parameters
    ----------
    name : str

    Returns
    -------
    invalid_op : function
    """

    def invalid_op(self: object, other: object = None) -> NoReturn:
        typ = type(self).__name__
        raise TypeError(f"cannot perform {name} with this index type: {typ}")

    invalid_op.__name__ = name
    return invalid_op

class TestAllowNonNano:  [tests/frame/test_constructors.py:3395]
methods: arr, as_td, test_dti_tdi_allow_non_nano
         test_frame_allow_non_nano
         test_frame_from_dict_allow_non_nano
         test_index_allow_non_nano
         test_series_allow_non_nano

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

    def __init__(
        self,
        data=None,
        index=None,
        dtype: Dtype | None = None,
        name=None,
        copy: bool | None = None,
    ) -> None:
        allow_mgr = False
        if (
            isinstance(data, SingleBlockManager)
            and index is None
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

class TestDatetimeIndexRendering:  [indexes/datetimes/test_formats.py:63]
methods: test_dti_business_repr_etc_smoke, test_dti_repr_dates
         test_dti_repr_mixed, test_dti_repr_short
         test_dti_repr_time_midnight
         test_dti_repr_wraps_at_display_width
         test_dti_representation
         test_dti_representation_to_series
         test_dti_summary, test_dti_with_timezone_repr

    def invalid_op(self: object, other: object = None) -> NoReturn:
        typ = type(self).__name__
        raise TypeError(f"cannot perform {name} with this index type: {typ}")

    def type(self) -> type[str]:
        return str
```
