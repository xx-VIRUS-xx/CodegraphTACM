# pandas-55 :: tacm-dyn

query: BUG: Fix incorrect _is_scalar_access check in iloc (#32085)

## selected nodes

- rank=1 layer=FILE tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/utils.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/utils.py
- rank=2 layer=CLASS tokens=657 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_iloc.py::TestiLocBaseIndependent file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_iloc.py
- rank=3 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=4 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=5 layer=FILE tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/grouper.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/grouper.py
- rank=6 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/console.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/console.py
- rank=7 layer=CLASS tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_iloc.py::TestILocSetItemDuplicateColumns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_iloc.py
- rank=8 layer=CLASS tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=9 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=10 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=11 layer=CLASS tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py::TestLocILocDataFrameCategorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py
- rank=12 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=13 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=14 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=15 layer=FILE tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=16 layer=CLASS tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=17 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.is_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=18 layer=CLASS tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py::TestIsScalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py
- rank=19 layer=CLASS tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::BinOp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=20 layer=FUNCTION tokens=354 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._setitem_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=21 layer=CLASS tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Term file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=22 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=23 layer=CLASS tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_floats.py::TestFloatIndexers file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_floats.py
- rank=24 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_floats.py::TestFloatIndexers.check file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_floats.py
- rank=25 layer=CLASS tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=26 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=27 layer=CLASS tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py::TestSetitemValidation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py
- rank=28 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
file core/indexers/utils.py
imports: __future__, typing, numpy, pandas
defines: is_valid_positional_slice, is_list_like_indexer, is_scalar_indexer, is_empty_indexer, check_setitem_lengths, validate_indices, maybe_convert_indices, length_of_indexer, disallow_ndim_indexing, unpack_1tuple, check_key_length, unpack_tuple_and_ellipses, getitem_returns_view, check_array_indexer

class TestiLocBaseIndependent:  [tests/indexing/test_iloc.py:66]
methods: test_identity_slice_returns_new_object
         test_iloc_array_not_mutating_negative_indices
         test_iloc_assign_series_to_df_cell
         test_iloc_empty_list_indexer_is_ok
         test_iloc_exceeds_bounds, test_iloc_getitem_array
         test_iloc_getitem_bool
         test_iloc_getitem_bool_diff_len
         test_iloc_getitem_categorical_values
         test_iloc_getitem_doc_issue
         test_iloc_getitem_dups
         test_iloc_getitem_float_duplicates
         test_iloc_getitem_frame
         test_iloc_getitem_int_single_ea_block_view
         test_iloc_getitem_invalid_scalar
         test_iloc_getitem_labelled_frame
         test_iloc_getitem_neg_int_can_reach_first_index
         test_iloc_getitem_read_only_values
         test_iloc_getitem_readonly_key
         test_iloc_getitem_singlerow_slice_categoricaldtype_gives_series
         test_iloc_getitem_slice
         test_iloc_getitem_slice_dups
         test_iloc_getitem_slice_negative_step_ea_block
         test_iloc_getitem_with_duplicates
         test_iloc_getitem_with_duplicates2
         test_iloc_interval, test_iloc_mask
         test_iloc_non_integer_raises
         test_iloc_non_unique_indexing
         test_iloc_series_mask_all_true
         test_iloc_series_mask_alternate_true
         test_iloc_series_mask_with_index_mismatch_raises
         test_iloc_setitem
         test_iloc_setitem_2d_ndarray_into_ea_block
         test_iloc_setitem_axis_argument
         test_iloc_setitem_bool_indexer
         test_iloc_setitem_categorical_updates_inplace
         test_iloc_setitem_custom_object
         test_iloc_setitem_dictionary_value
         test_iloc_setitem_dups
         test_iloc_setitem_ea_inplace
         test_iloc_setitem_empty_frame_raises_with_3d_ndarray
         test_iloc_setitem_frame_duplicate_columns_multiple_blocks
         test_iloc_setitem_fullcol_categorical
         test_iloc_setitem_list
         test_iloc_setitem_list_of_lists
         test_iloc_setitem_multicolumn_to_datetime
         test_iloc_setitem_pandas_object
         test_iloc_setitem_pure_position_based
         test_iloc_setitem_series
         test_iloc_setitem_td64_values_cast_na
         test_iloc_setitem_with_scalar_index
         test_iloc_with_boolean_operation
         test_iloc_with_numpy_bool_array
         test_indexing_zerodim_np_array
         test_is_scalar_access
         test_loc_setitem_boolean_list
         test_series_indexing_zerodim_np_array
         test_setitem_mix_of_nan_and_interval
         test_setitem_ragged_list_of_lists_raises

    def _is_scalar_access(self, key: tuple) -> bool:
        """
        Returns
        -------
        bool
        """
        # this is a shortcut accessor to both .loc and .iloc
        # that provide the equivalent access of .at and .iat
        # a) avoid getting things via sections and (to minimize dtype changes)
        # b) provide a performant path
        if len(key) != self.ndim:
            return False

        return all(is_integer(k) for k in key)

    def _is_scalar_access(self, key: tuple):
        raise NotImplementedError

file core/groupby/grouper.py
imports: __future__, itertools, typing, warnings, numpy, pandas, collections
defines: Grouper, Grouping, get_grouper, is_in_axis, is_in_obj, _is_label_like, _convert_grouper

file io/formats/console.py
imports: __future__, shutil, pandas, __main__
defines: get_console_size, in_interactive_session, check_main, in_ipython_frontend

class TestILocSetItemDuplicateColumns:  [tests/indexing/test_iloc.py:1351]
methods: test_iloc_setitem_dtypes_duplicate_columns
         test_iloc_setitem_list_duplicate_columns
         test_iloc_setitem_scalar_duplicate_columns
         test_iloc_setitem_series_duplicate_columns

class NumericSeriesIndexing:  [asv_bench/benchmarks/indexing.py:27]
methods: setup, time_getitem_array, time_getitem_list_like
         time_getitem_lists, time_getitem_scalar
         time_getitem_slice, time_iloc_array
         time_iloc_list_like, time_iloc_scalar
         time_iloc_slice, time_loc_array
         time_loc_list_like, time_loc_scalar, time_loc_slice

    def time_iloc_scalar(self, index, index_structure):
        self.data.iloc[800000]

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

    def _is_scalar_access(self, key: tuple) -> bool:
        """
        Returns
        -------
        bool
        """
        # this is a shortcut accessor to both .loc and .iloc
        # that provide the equivalent access of .at and .iat
        # a) avoid getting things via sections and (to minimize dtype changes)
        # b) provide a performant path
        if len(key) != self.ndim:
            return False

        for i, k in enumerate(key):
            if not is_scalar(k):
                return False

            ax = self.obj.axes[i]
            if isinstance(ax, MultiIndex):
                return False

            if isinstance(k, str) and ax._supports_partial_string_indexing:
                # partial string indexing, df.loc['2000', 'A']
                # should not be considered scalar
                return False

            if not ax._index_as_unique:
                return False

        return True

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

    def __getitem__(self, key):
        check_dict_or_set_indexers(key)
        key = lib.item_from_zerodim(key)
        key = com.apply_if_callable(key, self)

        if is_hashable(key, allow_slice=False) and not is_iterator(key):
            # is_iterator to exclude generator e.g. test_getitem_listlike
            # As of Python 3.12, slice is hashable which breaks MultiIndex (GH#57500)

            # Shortcut: return single column as Series when key refers to one column.
            # Previously we used "key in self.columns.drop_duplicates(keep=False)",
            # which built a new Index on every access when columns had duplicates.
    # ... truncated

file core/computation/ops.py
imports: __future__, datetime, functools, operator, typing, numpy, pandas, collections
defines: Term, Constant, Op, BinOp, UnaryOp, MathCall, FuncNode, _in, _not_in, is_term

class Op:  [core/computation/ops.py:213]
methods: has_invalid_return_type, is_datetime, is_scalar
         operand_types, return_type, __init__, __iter__
         __repr__

    def is_scalar(self) -> bool:
        return all(operand.is_scalar for operand in self.operands)

class TestIsScalar:  [tests/dtypes/test_inference.py:1973]
methods: test_is_scalar_builtin_nonscalars
         test_is_scalar_builtin_scalars
         test_is_scalar_number
         test_is_scalar_numpy_array_scalars
         test_is_scalar_numpy_arrays
         test_is_scalar_numpy_zerodim_arrays
         test_is_scalar_pandas_containers
         test_is_scalar_pandas_scalars

class BinOp(ops.BinOp):  [core/computation/pytables.py:112]
methods: _disallow_scalar_only_bool_ops, conform, convert_value
         convert_values, generate, is_in_table, is_valid
         kind, meta, metadata, pr, prune, stringify
         __init__

    def _setitem_array(self, key, value) -> None:
        # also raises Exception if object array with NA values
        if com.is_bool_indexer(key):
            # bool indexer is indexing along rows
            if len(key) != len(self.index):
                raise ValueError(
                    f"Item wrong length {len(key)} instead of {len(self.index)}!"
                )
            key = check_bool_indexer(self.index, key)
            indexer = key.nonzero()[0]
            if isinstance(value, DataFrame):
                # GH#39931 reindex since iloc does not align
                value = value.reindex(self.index.take(indexer))
            self.iloc[indexer] = value

        # Note: unlike self.iloc[:, indexer] = value, this will
        #  never try to overwrite values inplace

        elif isinstance(value, DataFrame):
            check_key_length(self.columns, key, value)
            for k1, k2 in zip(key, value.columns, strict=False):
                self[k1] = value[k2]

        elif not is_list_like(value):
            for col in key:
                self[col] = value

        elif isinstance(value, np.ndarray) and value.ndim == 2:
            self._iset_not_inplace(key, value)

        elif np.ndim(value) > 1:
            # list of lists
            value = DataFrame(value).values
            self._setitem_array(key, value)

        else:
            self._iset_not_inplace(key, value)

class Term:  [core/computation/ops.py:80]
methods: _resolve_name, evaluate, is_datetime, is_scalar
         local_name, name, ndim, raw, type, update, value
         value, __call__, __init__, __new__, __repr__

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

class TestFloatIndexers:  [tests/indexing/test_floats.py:28]
methods: check, compare
         test_float_slice_getitem_with_integer_index_raises
         test_floatindex_slicing_bug
         test_floating_index_doc_example
         test_floating_misc
         test_integer_positional_indexing
         test_scalar_float, test_scalar_integer
         test_scalar_integer_contains_float
         test_scalar_non_numeric
         test_scalar_non_numeric_series_fallback
         test_scalar_with_mixed, test_slice_float
         test_slice_integer
         test_slice_integer_frame_getitem
         test_slice_non_numeric

    def check(self, result, original, indexer, getitem):
        """
        comparator for results
        we need to take care if we are indexing on a
        Series or a frame
        """
        if isinstance(original, Series):
            expected = original.iloc[indexer]
        elif getitem:
            expected = original.iloc[:, indexer]
        else:
            expected = original.iloc[indexer]

        tm.assert_almost_equal(result, expected)

class PeriodArray(dtl.DatelikeOps, libperiod.PeriodMixin):  [core/arrays/period.py:123]
methods: _add_offset, _add_timedelta_arraylike
         _add_timedeltalike_scalar
         _addsub_int_array_or_scalar, _box_func
         _check_compatible_with
         _check_timedeltalike_freq_compat
         _format_native_types, _formatter
         _from_datetime64, _from_fields, _from_sequence
         _from_sequence_of_strings, _generate_range
         _pad_or_backfill, _reduce, _scalar_from_string
         _scalar_type, _simple_new, _unbox_scalar, asfreq
         astype, dayofweek, dayofyear, daysinmonth, dtype
         freq, freqstr, is_leap_year, searchsorted
         to_timestamp, weekday, __array__, __arrow_array__
         __init__

    def time_iloc_slice(self, index, index_structure):
        self.data.iloc[:800000]

class TestSetitemValidation:  [series/indexing/test_indexing.py:444]
methods: _check_setitem_invalid, _check_setitem_valid
         test_setitem_validation_scalar_bool
         test_setitem_validation_scalar_float
         test_setitem_validation_scalar_int

def iloc(x):
    return x.iloc
```
