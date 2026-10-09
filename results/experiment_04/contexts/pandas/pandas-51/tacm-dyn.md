# pandas-51 :: tacm-dyn

query: BUG: fix in categorical merges (#32079)

## selected nodes

- rank=1 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/console.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/console.py
- rank=2 layer=CLASS tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py::TestLocILocDataFrameCategorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py
- rank=3 layer=FUNCTION tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/sphinxext/announce.py::get_pull_requests file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/sphinxext/announce.py
- rank=4 layer=CLASS tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_algos.py::TestIsin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_algos.py
- rank=5 layer=CLASS tokens=228 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocWithMultiIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=6 layer=FILE tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=7 layer=CLASS tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py::TestTimedeltaIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py
- rank=8 layer=FILE tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/grouper.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/grouper.py
- rank=9 layer=FILE tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=10 layer=CLASS tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/libs/test_hashtable.py::TestPyObjectHashTableWithNans file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/libs/test_hashtable.py
- rank=11 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tools/test_to_datetime.py::TestDaysInMonth file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tools/test_to_datetime.py
- rank=12 layer=CLASS tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_cumulative.py::TestSeriesCumulativeOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_cumulative.py
- rank=13 layer=CLASS tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_arithmetic.py::TestFrameComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_arithmetic.py
- rank=14 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py
- rank=15 layer=CLASS tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_algos.py::TestUnique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_algos.py
- rank=16 layer=CLASS tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_getitem.py::TestGetitemBooleanMask file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_getitem.py
- rank=17 layer=CLASS tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_dropna.py::TestDataFrameMissingData file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_dropna.py
- rank=18 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=19 layer=CLASS tokens=260 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_repr.py::TestCategoricalRepr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_repr.py
- rank=20 layer=CLASS tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_categorical.py::TestCategoricalConcat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_categorical.py
- rank=21 layer=CLASS tokens=375 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py::TestStackUnstackMultiLevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py
- rank=22 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py::recode_for_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py
- rank=23 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_coerce_merge_keys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=24 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=25 layer=CLASS tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::CategoricalAccessor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=26 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=27 layer=FUNCTION tokens=6 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::at file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
file io/formats/console.py
imports: __future__, shutil, pandas, __main__
defines: get_console_size, in_interactive_session, check_main, in_ipython_frontend

class TestLocILocDataFrameCategorical:  [frame/indexing/test_indexing.py:1607]
methods: exp_parts_cats_col, exp_single_cats_value, orig
         test_getitem_preserve_object_index_with_dates
         test_loc_iloc_at_iat_setitem_single_value_in_categories
         test_loc_iloc_setitem_full_row_non_categorical_rhs
         test_loc_iloc_setitem_list_of_lists
         test_loc_iloc_setitem_mask_single_value_in_categories
         test_loc_iloc_setitem_non_categorical_rhs
         test_loc_iloc_setitem_partial_col_categorical_rhs
         test_loc_on_multiindex_one_level

def get_pull_requests(repo, revision_range):
    prnums = []

    # From regular merges
    merges = this_repo.git.log("--oneline", "--merges", revision_range)
    issues = re.findall("Merge pull request \\#(\\d*)", merges)
    prnums.extend(int(s) for s in issues)

    # From Homu merges (Auto merges)
    issues = re.findall("Auto merge of \\#(\\d*)", merges)
    prnums.extend(int(s) for s in issues)

    # From fast forward squash-merges
    commits = this_repo.git.log(
        "--oneline", "--no-merges", "--first-parent", revision_range
    )
    issues = re.findall("^.*\\(\\#(\\d+)\\)$", commits, re.M)
    prnums.extend(int(s) for s in issues)

    # get PR data from GitHub repo
    prnums.sort()
    prs = [repo.get_pull(n) for n in prnums]
    return prs

class TestIsin:  [pandas/tests/test_algos.py:903]
methods: test_basic, test_categorical_from_codes
         test_categorical_isin, test_different_nan_objects
         test_different_nans
         test_different_nans_as_float64, test_empty
         test_i8, test_invalid
         test_isin_datetimelike_all_nat
         test_isin_datetimelike_strings_returns_false
         test_isin_datetimelike_values_numeric_comps
         test_isin_dt64tz_with_nat
         test_isin_float_df_string_search
         test_isin_int_df_string_search
         test_isin_nan_df_string_search
         test_isin_unsigned_dtype, test_large
         test_no_cast, test_same_nan_is_in
         test_same_nan_is_in_large
         test_same_nan_is_in_large_series
         test_same_object_is_in

class TestLocWithMultiIndex:  [tests/indexing/test_loc.py:1764]
methods: test_additional_categorical_element_loc
         test_additional_element_to_categorical_series_loc
         test_loc_consistency_series_enlarge_set_into
         test_loc_drops_level
         test_loc_getitem_access_none_value_in_multiindex
         test_loc_getitem_datetime_string_with_datetimeindex
         test_loc_getitem_multiindex_nonunique_len_zero
         test_loc_getitem_multilevel_index_order
         test_loc_getitem_preserves_index_level_category_dtype
         test_loc_getitem_slice_datetime_objs_with_datetimeindex
         test_loc_getitem_sorted_index_level_with_duplicates
         test_loc_multiindex_levels_contain_values_not_in_index_anymore
         test_loc_multiindex_null_slice_na_level
         test_loc_preserve_names
         test_loc_set_nan_in_categorical_series
         test_loc_setitem_multiindex_slice

file core/computation/ops.py
imports: __future__, datetime, functools, operator, typing, numpy, pandas, collections
defines: Term, Constant, Op, BinOp, UnaryOp, MathCall, FuncNode, _in, _not_in, is_term

class TestTimedeltaIndex:  [indexes/timedeltas/test_setops.py:17]
methods: test_intersection, test_intersection_bug_1708
         test_intersection_equal
         test_intersection_non_monotonic
         test_intersection_zero_length, test_union
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_freq_infer, test_union_sort_false
         test_zero_length_input_index

file core/groupby/grouper.py
imports: __future__, itertools, typing, warnings, numpy, pandas, collections
defines: Grouper, Grouping, get_grouper, is_in_axis, is_in_obj, _is_label_like, _convert_grouper

file core/arrays/categorical.py
imports: __future__, csv, functools, itertools, operator, shutil, typing, warnings
defines: Categorical, CategoricalAccessor, _cat_compare_op, func, contains, _get_codes_for_values, recode_for_categories, factorize_from_iterable, factorize_from_iterables

class TestPyObjectHashTableWithNans:  [tests/libs/test_hashtable.py:385]
methods: test_nan_complex_both, test_nan_complex_imag
         test_nan_complex_real, test_nan_float
         test_nan_in_namedtuple
         test_nan_in_nested_namedtuple
         test_nan_in_nested_tuple, test_nan_in_tuple

class TestDaysInMonth:  [tests/tools/test_to_datetime.py:2945]
methods: test_day_not_in_month_coerce, test_day_not_in_month_raise
         test_day_not_in_month_raise_value

class TestSeriesCumulativeOps:  [tests/series/test_cumulative.py:25]
methods: test_cum_methods_ea_strings
         test_cummax_cummin_on_ordered_categorical
         test_cummax_cummin_ordered_categorical_nan
         test_cummethods_bool
         test_cummethods_bool_in_object_dtype
         test_cummin_cummax
         test_cummin_cummax_datetimelike
         test_cummin_cummax_period
         test_cumprod_pyarrow_strings
         test_cumprod_timedelta, test_cumsum_datetimelike
         test_datetime_series

class TestFrameComparisons:  [tests/frame/test_arithmetic.py:86]
methods: test_comparison_invalid
         test_comparison_with_categorical_dtype
         test_df_boolean_comparison_error
         test_df_float_none_comparison
         test_df_string_comparison, test_frame_in_list
         test_mixed_comparison, test_timestamp_compare

file core/groupby/categorical.py
imports: __future__, numpy, pandas
defines: recode_for_groupby

class TestUnique:  [pandas/tests/test_algos.py:552]
methods: test_categorical, test_datetime64_dtype_array_returned
         test_datetime64tz_aware, test_datetime_non_ns
         test_different_nans, test_do_not_mangle_na_values
         test_dtype_preservation
         test_factorize_multiindex_empty
         test_first_nan_kept, test_index_returned
         test_ints, test_nan_in_object_array
         test_obj_none_preservation
         test_object_refcount_bug, test_objects
         test_order_of_appearance
         test_order_of_appearance_dt64
         test_order_of_appearance_dt64tz, test_signed_zero
         test_timedelta64_dtype_array_returned
         test_timedelta_non_ns, test_tuple_with_strings
         test_uint64_overflow
         test_unique_NumpyExtensionArray, test_unique_masked

class TestGetitemBooleanMask:  [frame/indexing/test_getitem.py:338]
methods: df_dup_cols, test_getitem_bool_mask_categorical_index
         test_getitem_bool_mask_duplicate_columns_mixed_dtypes
         test_getitem_boolean_frame_unaligned_with_duplicate_columns
         test_getitem_boolean_frame_with_duplicate_columns
         test_getitem_boolean_series_with_duplicate_columns
         test_getitem_empty_frame_with_boolean
         test_getitem_frozenset_unique_in_column
         test_getitem_returns_view_when_column_is_unique_in_df

class TestDataFrameMissingData:  [frame/methods/test_dropna.py:15]
methods: test_dropEmptyRows, test_dropIncompleteRows
         test_drop_and_dropna_caching, test_dropna
         test_dropna_categorical_interval_index
         test_dropna_corner, test_dropna_ignore_index
         test_dropna_multiple_axes
         test_dropna_tz_aware_datetime
         test_dropna_with_duplicate_columns
         test_how_thresh_param_incompatible
         test_no_nans_in_frame
         test_set_single_column_subset
         test_single_column_not_present_in_axis
         test_subset_is_nparray

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

class TestCategoricalRepr:  [arrays/categorical/test_repr.py:29]
methods: test_big_print, test_categorical_index_repr
         test_categorical_index_repr_datetime
         test_categorical_index_repr_datetime_ordered
         test_categorical_index_repr_ordered
         test_categorical_index_repr_period
         test_categorical_index_repr_period_ordered
         test_categorical_index_repr_timedelta
         test_categorical_index_repr_timedelta_ordered
         test_categorical_repr
         test_categorical_repr_datetime
         test_categorical_repr_datetime_ordered
         test_categorical_repr_int_with_nan
         test_categorical_repr_ordered
         test_categorical_repr_period
         test_categorical_repr_period_ordered
         test_categorical_repr_timedelta
         test_categorical_repr_timedelta_ordered
         test_categorical_str_repr
         test_categorical_with_string_dtype
         test_empty_print, test_print_none_width
         test_unicode_print
         test_values_repr_respects_display_width

class TestCategoricalConcat:  [reshape/concat/test_categorical.py:18]
methods: test_categorical_concat, test_categorical_concat_dtypes
         test_categorical_concat_gh7864
         test_categorical_concat_preserve
         test_categorical_index_preserver
         test_categorical_index_upcast
         test_categorical_missing_from_one_frame
         test_concat_categorical_datetime
         test_concat_categorical_same_categories_different_order
         test_concat_categorical_tz
         test_concat_categorical_unchanged
         test_concat_categoricalindex

class TestStackUnstackMultiLevel:  [tests/frame/test_stack_unstack.py:1690]
methods: test_multi_level_stack_categorical, test_stack
         test_stack_dropna, test_stack_duplicate_index
         test_stack_level_name, test_stack_mixed_dtype
         test_stack_multiple_bug
         test_stack_multiple_out_of_bounds
         test_stack_names_and_numbers
         test_stack_nan_in_multiindex_columns
         test_stack_nan_level, test_stack_nullable_dtype
         test_stack_order_with_unsorted_levels
         test_stack_order_with_unsorted_levels_multi_row
         test_stack_order_with_unsorted_levels_multi_row_2
         test_stack_unsorted, test_stack_unstack_multiple
         test_stack_unstack_preserve_names
         test_stack_unstack_unordered_multiindex
         test_stack_unstack_wrong_level_name, test_unstack
         test_unstack_bug
         test_unstack_categorical_columns
         test_unstack_group_index_overflow
         test_unstack_level_name
         test_unstack_mixed_level_names
         test_unstack_multiple_hierarchical
         test_unstack_multiple_no_empty_columns
         test_unstack_number_of_levels_larger_than_int32_warns
         test_unstack_odd_failure, test_unstack_partial
         test_unstack_period_frame
         test_unstack_period_series
         test_unstack_preserve_types
         test_unstack_sparse_keyspace
         test_unstack_unobserved_keys
         test_unstack_with_level_has_nan
         test_unstack_with_missing_int_cast_to_float

def recode_for_groupby(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    # ... truncated

    def _maybe_coerce_merge_keys(self) -> None:
        # we have valid merges but we may have to further
        # coerce these if they are originally incompatible types
        #
        # for example if these are categorical, but are not dtype_equal
        # or if we have object and integer dtypes

        for lk, rk, name in zip(
            self.left_join_keys, self.right_join_keys, self.join_names, strict=True
        ):
            if (len(lk) and not len(rk)) or (not len(lk) and len(rk)):
                continue
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

class CategoricalAccessor(PandasDelegate, PandasObject, NoNewAttributesMixin):  [core/arrays/categorical.py:2909]
methods: _delegate_method, _delegate_property_get
         _delegate_property_set, _validate, codes, __init__

    def time_categorical_contains(self):
        self.key in self.c

def at(x):
    return x.at
```
