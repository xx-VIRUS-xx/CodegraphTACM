# pandas-47 :: tacm-dyn

query: BUG: assignment to multiple columns when some column do not exist (#29334)

## selected nodes

- rank=1 layer=FILE tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=2 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=4 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FUNCTION tokens=343 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._do_select_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=6 layer=FUNCTION tokens=410 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::stack_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=7 layer=CLASS tokens=396 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/computation/test_eval.py::TestOperations file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/computation/test_eval.py
- rank=8 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=9 layer=CLASS tokens=261 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_chaining_and_caching.py::TestChaining file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_chaining_and_caching.py
- rank=10 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=11 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._ensure_listlike_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=12 layer=CLASS tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_describe.py::TestDataFrameDescribe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_describe.py
- rank=13 layer=FUNCTION tokens=243 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._set_item file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=14 layer=CLASS tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=15 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.column_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py
- rank=16 layer=FUNCTION tokens=10 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase.close file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py

## context

```text
file core/reshape/reshape.py
imports: __future__, itertools, typing, warnings, numpy, pandas
defines: _Unstacker, _unstack_multiple, unstack, unstack, unstack, _unstack_frame, _unstack_extension_series, stack, stack_factorize, stack_multiple, _stack_multi_column_index, _stack_multi_columns, _convert_level_number, _reorder_for_extension_array_stack, stack_v3, stack_reshape

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

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

    def __setitem__(self, key, value) -> None:
        """
        Set item(s) in DataFrame by key.

        This method allows you to set the values of one or more columns in the
        DataFrame using a key. If the key does not exist, a new
        column will be created.

        Parameters
        ----------
        key : The object(s) in the index which are to be assigned to
            Column label(s) to set. Can be a single column name, list of column names,
    # ... truncated

    def _do_select_columns(self, data: DataFrame, columns: Sequence[str]) -> DataFrame:
        if not self._column_selector_set:
            column_set = set(columns)
            if len(column_set) != len(columns):
                raise ValueError("columns contains duplicate entries")
            unmatched = column_set.difference(data.columns)
            if unmatched:
                joined = ", ".join(list(unmatched))
                raise ValueError(
                    "The following columns were not "
                    f"found in the Stata data set: {joined}"
                )
            # Copy information for retained columns for later processing
            dtyplist = []
            typlist = []
            fmtlist = []
            lbllist = []
            for col in columns:
                i = data.columns.get_loc(col)
                dtyplist.append(self._dtyplist[i])
                typlist.append(self._typlist[i])
                fmtlist.append(self._fmtlist[i])
                lbllist.append(self._lbllist[i])

            self._dtyplist = dtyplist  # type: ignore[assignment]
            self._typlist = typlist  # type: ignore[assignment]
            self._fmtlist = fmtlist  # type: ignore[assignment]
            self._lbllist = lbllist  # type: ignore[assignment]
            self._column_selector_set = True

        return data[columns]

def stack_multiple(frame: DataFrame, level, dropna: bool = True, sort: bool = True):
    # If all passed levels match up to column names, no
    # ambiguity about what to do
    if all(lev in frame.columns.names for lev in level):
        result = frame
        for lev in level:
            # error: Incompatible types in assignment (expression has type
            # "Series | DataFrame", variable has type "DataFrame")
            result = stack(result, lev, dropna=dropna, sort=sort)  # type: ignore[assignment]

    # Otherwise, level numbers may change as each successive level is stacked
    elif all(isinstance(lev, int) for lev in level):
        # As each stack is done, the level numbers decrease, so we need
        #  to account for that when level is a sequence of ints
        result = frame
        # _get_level_number() checks level numbers are in range and converts
        # negative numbers to positive
        level = [frame.columns._get_level_number(lev) for lev in level]

        while level:
            lev = level.pop(0)
            # error: Incompatible types in assignment (expression has type
            # "Series | DataFrame", variable has type "DataFrame")
            result = stack(result, lev, dropna=dropna, sort=sort)  # type: ignore[assignment]
            # Decrement all level numbers greater than current, as these
            # have now shifted down by one
            level = [v if v <= lev else v - 1 for v in level]

    else:
        raise ValueError(
            "level should contain all level names or all level "
            "numbers, not a mixture of the two."
        )

    return result

class TestOperations:  [tests/computation/test_eval.py:1081]
methods: eval, local_func, local_func, test_4d_ndarray_fails
         test_assignment_column_invalid_assign
         test_assignment_column_invalid_assign_function_call
         test_assignment_column_multiple_raise
         test_assignment_explicit, test_assignment_fails
         test_assignment_in_query
         test_assignment_multiple_raises
         test_assignment_not_inplace
         test_assignment_single_assign_existing
         test_assignment_single_assign_local_overlap
         test_assignment_single_assign_name
         test_assignment_single_assign_new
         test_attr_expression
         test_basic_period_index_boolean_expression
         test_basic_period_index_subscript_expression
         test_bool_ops_with_constants
         test_cannot_copy_item, test_cannot_item_assign
         test_check_many_exprs, test_column_in
         test_constant, test_date_boolean
         test_failing_subscript_with_name_error
         test_fails_ampersand_pipe, test_fails_and_or_not
         test_inplace_no_assignment
         test_lhs_expression_subscript
         test_multi_line_expression
         test_multi_line_expression_callable_local_variable
         test_multi_line_expression_callable_local_variable_with_kwargs
         test_multi_line_expression_local_variable
         test_multi_line_expression_not_inplace
         test_nested_period_index_subscript_expression
         test_query_inplace, test_simple_arith_ops
         test_simple_bool_ops, test_simple_in_ops
         test_single_variable

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

class TestChaining:  [tests/indexing/test_chaining_and_caching.py:74]
methods: test_cache_updating, test_cache_updating2
         test_chained_getitem_with_lists
         test_detect_chained_assignment
         test_detect_chained_assignment_changing_dtype
         test_detect_chained_assignment_doc_example
         test_detect_chained_assignment_fails
         test_detect_chained_assignment_false_positives
         test_detect_chained_assignment_is_copy_pickle
         test_detect_chained_assignment_object_dtype
         test_detect_chained_assignment_raises
         test_detect_chained_assignment_sorting
         test_detect_chained_assignment_str
         test_detect_chained_assignment_undefined_column
         test_detect_chained_assignment_warning_stacklevel
         test_detect_chained_assignment_warnings_errors
         test_getitem_loc_assignment_slice_state
         test_iloc_setitem_chained_assignment
         test_setitem_chained_setfault
         test_setting_with_copy_bug
         test_setting_with_copy_bug_no_warning

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

    def _ensure_listlike_indexer(self, key, axis=None) -> None:
        """
        Ensure that a list-like of column labels are all present by adding them if
        they do not already exist.

        Parameters
        ----------
        key : list-like of column labels
            Target labels.
        axis : key axis if known
        """
    # ... truncated

class TestDataFrameDescribe:  [frame/methods/test_describe.py:15]
methods: test_datetime_is_numeric_includes_datetime
         test_describe_bool_frame
         test_describe_bool_in_mixed_frame
         test_describe_categorical
         test_describe_categorical_columns
         test_describe_datetime_columns
         test_describe_does_not_raise_error_for_dictlike_elements
         test_describe_empty_categorical_column
         test_describe_empty_object
         test_describe_exclude_pa_dtype
         test_describe_percentiles_integer_idx
         test_describe_timedelta_values
         test_describe_tz_values, test_describe_tz_values2
         test_describe_when_include_all_exclude_not_allowed
         test_describe_when_included_dtypes_not_present
         test_describe_with_duplicate_columns
         test_ea_with_na, test_refine_percentiles

    def _set_item(self, key, value) -> None:
        """
        Add series to DataFrame in specified column.

        If series is a numpy-array (not a Series/TimeSeries), it must be the
        same length as the DataFrames index or an error will be thrown.

        Series/TimeSeries will be conformed to the DataFrames index to
        ensure homogeneity.
        """
        value, refs = self._sanitize_column(value)

        if (
            key in self.columns
            and value.ndim == 1
            and not isinstance(value.dtype, ExtensionDtype)
        ):
            # broadcast across multiple columns if necessary
            if not self.columns.is_unique or isinstance(self.columns, MultiIndex):
                existing_piece = self[key]
                if isinstance(existing_piece, DataFrame):
                    value = np.tile(value, (len(existing_piece.columns), 1)).T
                    refs = None

        self._set_item_mgr(key, value, refs)

class ParserBase:  [io/parsers/base_parser.py:86]
methods: _agg_index, _check_data_length, _clean_index_names
         _clean_mapping, _do_date_conversions
         _do_date_conversions, _do_date_conversions
         _extract_multi_indexer_columns, _get_empty_meta
         _infer_types, _make_index
         _maybe_make_multi_index_columns, _set
         _set_noconvert_dtype_columns, _should_parse_dates
         _validate_usecols_names, close, extract, __init__

    def column_names(self) -> Index:
        return self._df.columns

    def close(self) -> None:
        pass
```
