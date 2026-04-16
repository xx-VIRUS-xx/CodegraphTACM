# pandas-53 :: tacm-dyn

query: BUG: using loc[int] with object index (#31905)

## selected nodes

- rank=1 layer=FILE tokens=588 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=2 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.isetitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=5 layer=CLASS tokens=882 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocBaseIndependent file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=6 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=7 layer=CLASS tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLabelSlicing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=8 layer=CLASS tokens=275 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py::TestSelectDtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py
- rank=9 layer=CLASS tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_logical_ops.py::TestSeriesLogicalOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_logical_ops.py
- rank=10 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=11 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=12 layer=CLASS tokens=373 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocSetitemWithExpansion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=13 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=14 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Float64IndexMethod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=15 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
file pandas/pandas/conftest.py
imports: __future__, collections, datetime, decimal, gc, operator, os, typing
defines: TestSubDict, TestNonDictMapping, pytest_addoption, pytest_sessionstart, _from_module, ignore_doctest_warning, pytest_collection_modifyitems, add_doctest_imports, configure_tests, axis, observed, ordered, dropna, sort, skipna, keep, inclusive_endpoints_fixture, closed, other_closed, compression, compression_only, writable, join_type, nselect_method, na_action, ascending, rank_method, as_index, cache, parallel, nogil, nulls_fixture, unique_nulls_fixture, np_nat_fixture, frame_or_series, index_or_series, index_or_series_or_array, box_with_array, dict_subclass, non_dict_mapping_subclass, multiindex_year_month_day_dataframe_random_data, lexsorted_two_level_string_multiindex, multiindex_dataframe_random_data, _create_multiindex, _create_mi_with_dt64tz_level, index, index_flat, index_with_missing, string_series, object_series, datetime_series, _create_series, series_with_simple_index, index_or_series_obj, index_or_series_memory_obj, int_frame, float_frame, rand_series_with_duplicate_datetimeindex, ea_scalar_and_dtype, all_arithmetic_operators, all_binary_operators, all_arithmetic_functions, all_numeric_reductions, all_boolean_reductions, all_reductions, comparison_op, compare_operators_no_eq_ne, all_logical_operators, all_numeric_accumulations, strict_data_files, datapath, deco, tz_naive_fixture, tz_aware_fixture, utc_fixture, unit, string_dtype, string_dtype_no_object, nullable_string_dtype, pyarrow_string_dtype, string_storage, string_dtype_arguments, dtype_backend, bytes_dtype, object_dtype, any_string_dtype, datetime64_dtype, timedelta64_dtype, fixed_now_ts, float_numpy_dtype, float_ea_dtype, any_float_dtype, complex_dtype, complex_or_float_dtype, any_signed_int_numpy_dtype, any_unsigned_int_numpy_dtype, any_int_numpy_dtype, any_int_ea_dtype, any_int_dtype, any_numeric_ea_dtype, any_numeric_ea_and_arrow_dtype, any_signed_int_ea_dtype, any_real_numpy_dtype, any_real_numeric_dtype, any_numpy_dtype, any_real_nullable_dtype, any_numeric_dtype, any_skipna_inferred_dtype, ip, mpl_cleanup, tick_classes, sort_by_key, names, indexer_sli, indexer_li, indexer_si, indexer_sl, indexer_al, indexer_ial, performance_warning, using_infer_string, using_python_scalars, warsaw, temp_file, monkeysession, using_nan_is_na

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

    def isetitem(self, loc, value) -> None:
        """
        Set the given value in the column with position `loc`.

        This is a positional analogue to ``__setitem__``.

        Parameters
        ----------
        loc : int or sequence of ints
            Index position for the column.
        value : scalar or arraylike
            Value(s) for the column.
    # ... truncated

    def _set_value(self, label, value, takeable: bool = False) -> None:
        """
        Quickly set single value at passed label.

        If label is not contained, a new object is created with the label
        placed at the end of the result index.

        Parameters
        ----------
        label : object
            Partial indexing with MultiIndex not allowed.
        value : object
            Scalar value.
        takeable : interpret the index as indexers, default False
        """
        if not takeable:
            try:
                loc = self.index.get_loc(label)
            except KeyError:
                # set using a non-recursive method
                self.loc[label] = value
                return
        else:
            loc = label

        self._set_values(loc, value)

class TestLocBaseIndependent:  [tests/indexing/test_loc.py:296]
methods: frame_for_consistency
         test_contains_raise_error_if_period_index_is_in_multi_index
         test_getitem_label_list_with_missing
         test_getitem_single_row_sparse_df
         test_identity_slice_returns_new_object
         test_indexing_zerodim_np_array
         test_loc_assign_non_ns_datetime
         test_loc_coercion, test_loc_coercion2
         test_loc_coercion3, test_loc_copy_vs_view
         test_loc_empty_list_indexer_is_ok
         test_loc_general, test_loc_getitem_bool_diff_len
         test_loc_getitem_dups, test_loc_getitem_dups2
         test_loc_getitem_index_namedtuple
         test_loc_getitem_index_single_double_tuples
         test_loc_getitem_int_slice
         test_loc_getitem_interval_index
         test_loc_getitem_interval_index2
         test_loc_getitem_iterable
         test_loc_getitem_list_with_fail
         test_loc_getitem_listlike_all_retains_sparse
         test_loc_getitem_missing_unicode_key
         test_loc_getitem_range_from_spmatrix
         test_loc_getitem_sparse_frame
         test_loc_getitem_sparse_series
         test_loc_getitem_time_object
         test_loc_getitem_timedelta_0seconds
         test_loc_getitem_uint64_scalar, test_loc_index
         test_loc_modify_datetime, test_loc_name
         test_loc_non_unique
         test_loc_non_unique_memory_error, test_loc_npstr
         test_loc_reverse_assignment
         test_loc_setitem_2d_to_1d_raises
         test_loc_setitem_cast2, test_loc_setitem_cast3
         test_loc_setitem_categorical_values_partial_column_slice
         test_loc_setitem_consistency
         test_loc_setitem_consistency_dt64_to_float
         test_loc_setitem_consistency_dt64_to_str
         test_loc_setitem_consistency_empty
         test_loc_setitem_consistency_single_row
         test_loc_setitem_consistency_slice_column_len
         test_loc_setitem_datetime_coercion
         test_loc_setitem_datetimeindex_tz
         test_loc_setitem_dtype, test_loc_setitem_dups
         test_loc_setitem_empty_append_expands_rows
         test_loc_setitem_empty_append_expands_rows_mixed_dtype
         test_loc_setitem_empty_append_raises
         test_loc_setitem_empty_append_single_value
         test_loc_setitem_empty_frame
         test_loc_setitem_frame
         test_loc_setitem_frame_mixed_labels
         test_loc_setitem_frame_multiples
         test_loc_setitem_frame_nan_int_coercion_invalid
         test_loc_setitem_frame_with_inverted_slice
         test_loc_setitem_frame_with_reindex
         test_loc_setitem_frame_with_reindex_mixed
         test_loc_setitem_int_label_with_float_index
         test_loc_setitem_listlike_with_timedelta64index
         test_loc_setitem_missing_columns
         test_loc_setitem_numpy_frame_categorical_value
         test_loc_setitem_range_key
         test_loc_setitem_single_column_mixed
         test_loc_setitem_single_row_categorical
         test_loc_setitem_slice
         test_loc_setitem_str_to_small_float_conversion_type
         test_loc_setitem_td64_non_nano
         test_loc_setitem_time_key
         test_loc_setitem_uint_drop
         test_loc_setitem_unsorted_multiindex_columns
         test_loc_setitem_with_scalar_index
         test_loc_to_fail, test_loc_to_fail2
         test_loc_to_fail3, test_loc_uint64
         test_loc_uint64_disallow_negative
         test_loc_with_nat_in_tzaware_index
         test_series_indexing_zerodim_np_array
         test_setitem_new_key_tz

    def insert(
        self,
        loc: int,
        column: Hashable,
        value: object,
        allow_duplicates: bool | lib.NoDefault = lib.no_default,
    ) -> None:
        """
    # ... truncated

class TestLabelSlicing:  [tests/indexing/test_loc.py:2606]
methods: test_loc_getitem_float_slice_floatindex
         test_loc_getitem_label_slice_across_dst
         test_loc_getitem_label_slice_period_timedelta
         test_loc_getitem_slice_columns_mixed_dtype
         test_loc_getitem_slice_floats_inexact
         test_loc_getitem_slice_label_td64obj
         test_loc_getitem_slice_labels_int_in_object_index
         test_loc_getitem_slice_unordered_dt_index
         test_loc_getitem_slicing_datetimes_frame

class TestSelectDtypes:  [frame/methods/test_select_dtypes.py:57]
methods: test_np_bool_ea_boolean_include_number
         test_select_dtype_object_and_str
         test_select_dtypes_bad_arg_raises
         test_select_dtypes_bad_datetime64
         test_select_dtypes_datetime_with_tz
         test_select_dtypes_duplicate_columns
         test_select_dtypes_empty
         test_select_dtypes_exclude_include_int
         test_select_dtypes_exclude_include_using_list_like
         test_select_dtypes_exclude_using_list_like
         test_select_dtypes_exclude_using_scalars
         test_select_dtypes_float_dtype
         test_select_dtypes_include_exclude_mixed_scalars_lists
         test_select_dtypes_include_exclude_using_scalars
         test_select_dtypes_include_using_list_like
         test_select_dtypes_include_using_scalars
         test_select_dtypes_no_view
         test_select_dtypes_not_an_attr_but_still_valid_dtype
         test_select_dtypes_numeric
         test_select_dtypes_numeric_nullable_string
         test_select_dtypes_str_raises
         test_select_dtypes_typecodes

class TestSeriesLogicalOps:  [tests/series/test_logical_ops.py:17]
methods: test_bool_operators_with_nas
         test_int_dtype_different_index_not_bool
         test_logical_operators_bool_dtype_with_empty
         test_logical_operators_bool_dtype_with_int
         test_logical_operators_int_dtype_with_bool
         test_logical_operators_int_dtype_with_bool_dtype_and_reindex
         test_logical_operators_int_dtype_with_float
         test_logical_operators_int_dtype_with_int_dtype
         test_logical_operators_int_dtype_with_int_scalar
         test_logical_operators_int_dtype_with_object
         test_logical_operators_int_dtype_with_str
         test_logical_ops_bool_dtype_with_ndarray
         test_logical_ops_df_compat
         test_logical_ops_label_based
         test_logical_ops_with_index
         test_reverse_ops_with_index
         test_reversed_logical_op_with_index_returns_series
         test_reversed_xor_with_index_returns_series
         test_scalar_na_logical_ops_corners
         test_scalar_na_logical_ops_corners_aligns

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

def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

class TestLocSetitemWithExpansion:  [tests/indexing/test_loc.py:2011]
methods: test_loc_setitem_categorical_column_retains_dtype
         test_loc_setitem_datetime_keys_cast
         test_loc_setitem_datetimeindex_str_column_name
         test_loc_setitem_ea_not_full_column
         test_loc_setitem_empty_series
         test_loc_setitem_empty_series_float
         test_loc_setitem_empty_series_str_idx
         test_loc_setitem_expansion_both
         test_loc_setitem_incremental_with_dst
         test_loc_setitem_with_expansion_and_existing_dst
         test_loc_setitem_with_expansion_categorical
         test_loc_setitem_with_expansion_dtype_retention
         test_loc_setitem_with_expansion_dtype_retention_empty
         test_loc_setitem_with_expansion_empty_stays_object
         test_loc_setitem_with_expansion_fractional_not_truncated
         test_loc_setitem_with_expansion_inf_upcast_empty
         test_loc_setitem_with_expansion_large_dataframe
         test_loc_setitem_with_expansion_multi_column
         test_loc_setitem_with_expansion_multiindex_retains_dtypes
         test_loc_setitem_with_expansion_new_row_and_new_columns
         test_loc_setitem_with_expansion_nonunique_index
         test_loc_setitem_with_expansion_preserves_ea_dtype
         test_loc_setitem_with_expansion_preserves_nullable_int
         test_loc_setitem_with_expansion_retains_ea_dtype
         test_setitem_with_expansion
         test_setitem_with_expansion_pyarrow_scalar_retains_dtype

    def _get_loc_level(self, key, level: int | list[int] = 0):
        """
        get_loc_level but with `level` known to be positional, not name-based.
        """
    # ... truncated

class Float64IndexMethod:  [asv_bench/benchmarks/index_object.py:202]
methods: setup, time_get_loc

def loc(x):
    return x.loc
```
