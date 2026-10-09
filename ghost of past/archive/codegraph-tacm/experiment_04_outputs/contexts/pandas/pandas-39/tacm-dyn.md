# pandas-39 :: tacm-dyn

query: BUG: Fixed strange behaviour of pd.DataFrame.drop() with inplace argu… (#30501)

## selected nodes

- rank=1 layer=FILE tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py
- rank=2 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.drop_duplicates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.set_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.drop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=6 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=7 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.reset_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=8 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.drop_duplicates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=9 layer=CLASS tokens=261 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_drop.py::TestDataFrameDrop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_drop.py
- rank=10 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=11 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=12 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=13 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_string file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=14 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.reset_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=15 layer=CLASS tokens=414 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_get_dummies.py::TestGetDummies file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_get_dummies.py
- rank=16 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.drop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=17 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=18 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=19 layer=CLASS tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_block_internals.py::TestDataFrameBlockInternals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_block_internals.py
- rank=20 layer=CLASS tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_reset_index.py::TestResetIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_reset_index.py
- rank=21 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=22 layer=CLASS tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_setitem.py::TestDataFrameSetitemCopyViewSemantics file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_setitem.py
- rank=23 layer=CLASS tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::DatetimeIndexConstructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py
- rank=24 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py::ReplaceList.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py
- rank=25 layer=FUNCTION tokens=340 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.drop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=26 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.num_chunks file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=27 layer=FUNCTION tokens=11 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Fixed.shape file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py

## context

```text
file asv_bench/benchmarks/ctors.py
imports: numpy, pandas
defines: SeriesConstructors, SeriesDtypesConstructors, MultiIndexConstructor, DatetimeIndexConstructor, no_change, list_of_str, gen_of_str, arr_dict, list_of_tuples, gen_of_tuples, list_of_lists, list_of_tuples_with_none, list_of_lists_with_none

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

    def drop_duplicates(
        self,
        subset: Hashable | Iterable[Hashable] | None = None,
        *,
        keep: DropKeep = "first",
        inplace: bool = False,
        ignore_index: bool = False,
    ) -> DataFrame | None:
        """
    # ... truncated

    def set_index(
        self,
        keys,
        *,
        drop: bool = True,
        append: bool = False,
        inplace: bool = False,
        verify_integrity: bool | lib.NoDefault = lib.no_default,
    ) -> DataFrame | None:
        """
    # ... truncated

    def drop(
        self,
        labels: IndexLabel | ListLike = None,
        *,
        axis: Axis = 0,
        index: IndexLabel | ListLike = None,
        columns: IndexLabel | ListLike = None,
        level: Level | None = None,
        inplace: bool = False,
        errors: IgnoreRaise = "raise",
    ) -> DataFrame | None:
        """
    # ... truncated

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

    def reset_index(
        self,
        level: IndexLabel | None = None,
        *,
        drop: bool = False,
        name: Level = lib.no_default,
        inplace: bool = False,
        allow_duplicates: bool = False,
    ) -> DataFrame | Series | None:
        """
    # ... truncated

    def drop_duplicates(
        self,
        *,
        keep: DropKeep = "first",
        inplace: bool = False,
        ignore_index: bool = False,
    ) -> Series | None:
        """
    # ... truncated

class TestDataFrameDrop:  [frame/methods/test_drop.py:67]
methods: test_drop, test_drop_api_equivalence, test_drop_empty_list
         test_drop_empty_listlike_non_unique_datetime_index
         test_drop_index_ea_dtype
         test_drop_inplace_no_leftover_column_reference
         test_drop_level
         test_drop_level_missing_label_multiindex
         test_drop_level_nonunique_datetime
         test_drop_multiindex_not_lexsorted
         test_drop_multiindex_other_level_nan
         test_drop_names, test_drop_non_empty_list
         test_drop_nonunique
         test_drop_parse_strings_datetime_index
         test_drop_preserve_names
         test_drop_raise_with_both_axis_and_index
         test_drop_tuple_with_non_unique_multiindex
         test_drop_tz_aware_timestamp_across_dst
         test_drop_with_duplicate_columns
         test_drop_with_duplicate_columns2
         test_drop_with_non_unique_multiindex
         test_inplace_drop_and_operation
         test_mixed_depth_drop
         test_raise_on_drop_duplicate_index

    def time_frame_drop_dups(self, inplace):
        self.df.drop_duplicates(["key1", "key2"], inplace=inplace)

    def time_series_drop_dups_int(self, inplace):
        self.s.drop_duplicates(inplace=inplace)

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

    def time_series_drop_dups_string(self, inplace):
        self.s_str.drop_duplicates(inplace=inplace)

    def reset_index(
        self,
        level: IndexLabel | None = None,
        *,
        drop: bool = False,
        inplace: bool = False,
        col_level: Hashable = 0,
        col_fill: Hashable = "",
        allow_duplicates: bool | lib.NoDefault = lib.no_default,
        names: Hashable | Sequence[Hashable] | None = None,
    ) -> DataFrame | None:
        """
    # ... truncated

class TestGetDummies:  [tests/reshape/test_get_dummies.py:33]
methods: df, dtype, effective_dtype, sparse
         test_dataframe_dummies_all_obj
         test_dataframe_dummies_drop_first
         test_dataframe_dummies_drop_first_with_categorical
         test_dataframe_dummies_drop_first_with_na
         test_dataframe_dummies_mix_default
         test_dataframe_dummies_prefix_bad_length
         test_dataframe_dummies_prefix_dict
         test_dataframe_dummies_prefix_list
         test_dataframe_dummies_prefix_sep
         test_dataframe_dummies_prefix_sep_bad_length
         test_dataframe_dummies_prefix_str
         test_dataframe_dummies_preserve_categorical_dtype
         test_dataframe_dummies_string_dtype
         test_dataframe_dummies_subset
         test_dataframe_dummies_unicode
         test_dataframe_dummies_with_categorical
         test_dataframe_dummies_with_na
         test_get_dummies_all_sparse
         test_get_dummies_arrow_dtype
         test_get_dummies_basic
         test_get_dummies_basic_drop_first
         test_get_dummies_basic_drop_first_NA
         test_get_dummies_basic_drop_first_one_level
         test_get_dummies_basic_types
         test_get_dummies_dont_sparsify_all_columns
         test_get_dummies_duplicate_columns
         test_get_dummies_ea_dtype
         test_get_dummies_ea_dtype_dataframe
         test_get_dummies_ea_dtype_series
         test_get_dummies_include_na
         test_get_dummies_int_df, test_get_dummies_int_int
         test_get_dummies_just_na
         test_get_dummies_raises_on_dtype_object
         test_get_dummies_unicode
         test_get_dummies_with_string_values

    def drop(
        self,
        labels: IndexLabel | ListLike = None,
        *,
        axis: Axis = 0,
        index: IndexLabel | ListLike = None,
        columns: IndexLabel | ListLike = None,
        level: Level | None = None,
        inplace: bool = False,
        errors: IgnoreRaise = "raise",
    ) -> Series | None:
        """
    # ... truncated

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

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

class TestDataFrameBlockInternals:  [tests/frame/test_block_internals.py:31]
methods: f, test_add_column_with_pandas_array
         test_boolean_set_uncons, test_cast_internals
         test_consolidate, test_consolidate_datetime64
         test_consolidate_inplace
         test_construction_with_conversions
         test_construction_with_mixed
         test_constructor_compound_dtypes
         test_constructor_no_pandas_array
         test_constructor_with_convert, test_is_mixed_type
         test_modify_values, test_pickle_empty
         test_pickle_empty_tz_frame
         test_pickle_float_string_frame
         test_setitem_invalidates_datetime_index_freq
         test_stale_cached_series_bug_473
         test_strange_column_corruption_issue

class TestResetIndex:  [series/methods/test_reset_index.py:19]
methods: test_reset_index, test_reset_index_drop_errors
         test_reset_index_drop_infer_string
         test_reset_index_dti_round_trip
         test_reset_index_inplace_and_drop_ignore_name
         test_reset_index_level, test_reset_index_name
         test_reset_index_range, test_reset_index_with_drop

    def time_frame_drop_dups_int(self, inplace):
        self.df_int.drop_duplicates(inplace=inplace)

class TestDataFrameSetitemCopyViewSemantics:  [frame/indexing/test_setitem.py:1237]
methods: test_frame_setitem_empty_dataframe
         test_iloc_setitem_view_2dblock
         test_setitem_2dblock_with_ref
         test_setitem_always_copy
         test_setitem_column_frame_as_category
         test_setitem_column_update_inplace
         test_setitem_duplicate_columns_not_inplace
         test_setitem_frame_dup_cols_dtype
         test_setitem_iloc_with_numpy_array
         test_setitem_listlike_key_scalar_value_not_inplace
         test_setitem_not_operating_inplace
         test_setitem_partial_column_inplace
         test_setitem_same_dtype_not_inplace

class DatetimeIndexConstructor:  [asv_bench/benchmarks/ctors.py:122]
methods: setup, time_from_list_of_dates
         time_from_list_of_datetimes
         time_from_list_of_str, time_from_list_of_timestamps

    def setup(self, inplace):
        self.df = pd.DataFrame({"A": 0, "B": 0}, index=range(10**7))

    def drop(
        self,
        labels: IndexLabel | ListLike = None,
        *,
        axis: Axis = 0,
        index: IndexLabel | ListLike = None,
        columns: IndexLabel | ListLike = None,
        level: Level | None = None,
        inplace: bool = False,
        errors: IgnoreRaise = "raise",
    ) -> Self | None:
        inplace = validate_bool_kwarg(inplace, "inplace")

        if labels is not None:
            if index is not None or columns is not None:
                raise ValueError("Cannot specify both 'labels' and 'index'/'columns'")
            axis_name = self._get_axis_name(axis)
            axes = {axis_name: labels}
        elif index is not None or columns is not None:
            if axis == 1:
                raise ValueError("Cannot specify both 'axis' and 'index'/'columns'")
            axes = {"index": index}
            if self.ndim == 2:
                axes["columns"] = columns
        else:
            raise ValueError(
                "Need to specify at least one of 'labels', 'index' or 'columns'"
            )

        obj = self

        for axis, labels in axes.items():
            if labels is not None:
                obj = obj._drop_axis(labels, axis, level=level, errors=errors)

        if inplace:
            self._update_inplace(obj)
            return None
        else:
            return obj

    def num_chunks(self) -> int:
        """
        Return the number of chunks the DataFrame consists of.
        """

    def shape(self):
        return self.nrows
```
