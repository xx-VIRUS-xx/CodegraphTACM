# pandas-35 :: tacm-dyn-l4

query: BUG: create new MI from MultiIndex._get_level_values (#33134)

## selected nodes

- rank=1 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=2 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=CLASS tokens=477 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=4 layer=FUNCTION tokens=368 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_values_for_csv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=5 layer=FUNCTION tokens=313 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.dropna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=6 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.putmask file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=7 layer=FILE tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=8 layer=CLASS tokens=1045 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=9 layer=FUNCTION tokens=272 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_level_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=10 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py::TestDataFrameQueryWithMultiIndex.to_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py
- rank=11 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=12 layer=FILE tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/api/internals.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/api/internals.py

## context

```text
file core/internals/blocks.py
imports: __future__, inspect, re, typing, warnings, numpy, pandas
defines: Block, EABackedBlock, ExtensionBlock, NumpyBlock, NDArrayBackedExtensionBlock, DatetimeLikeBlock, maybe_coerce_values, get_block_type, new_block_2d, new_block, check_ndim, extract_pandas_array, extend_blocks, ensure_block_shape, external_values

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

class MultiIndex(Index):  [core/indexes/multi.py:198]
methods: _check_indexing_error, _constructor, _convert_can_do_setop
         _drop_from_level, _engine, _format_multi
         _formatter_func, _get_codes_for_sorting
         _get_indexer_level_0, _get_indexer_strict
         _get_level_indexer, _get_level_number
         _get_level_values, _get_loc_level
         _get_loc_single_level_index, _get_names
         _get_reconciled_name_object, _get_values_for_csv
         _getitem_slice, _is_comparable_dtype
         _is_lexsorted, _is_memory_usage_qualified
         _lexsort_depth, _maybe_match_names
         _maybe_preserve_names, _maybe_to_slice, _nbytes
         _partial_tup_index, _raise_if_missing
         _recode_for_new_levels, _reorder_ilevels
         _reorder_indexer, _set_codes, _set_levels
         _set_names, _shallow_copy
         _should_fallback_to_positional
         _sort_levels_monotonic, _to_bool_indexer, _union
         _validate_codes, _validate_fill_value, _values
         _verify_integrity, _view, _wrap_difference_result
         _wrap_intersection_result, _wrap_reindex_result
         append, argsort, array, astype, cats, codes
         convert_indexer, copy, delete, drop, dropna
         dtype, dtypes, duplicated, equal_levels, equals
         f, fillna, from_arrays, from_frame, from_product
         from_tuples, get_level_values, get_loc
         get_loc_level, get_locs, get_slice_bound
         inferred_type, insert, is_monotonic_decreasing
         is_monotonic_increasing, isin, levels, levshape
         maybe_mi_droplevels, memory_usage, nbytes
         nlevels, putmask, remove_unused_levels
         reorder_levels, repeat, set_codes, set_levels
         size, slice_locs, sortlevel, swaplevel, take
         to_flat_index, to_frame, truncate, unique, values
         view, __array__, __contains__, __getitem__
         __len__, __new__, __reduce__

    def _get_values_for_csv(
        self, *, na_rep: str = "nan", **kwargs
    ) -> npt.NDArray[np.object_]:
        new_levels = []
        new_codes = []

        # go through the levels and format them
        for level, level_codes in zip(self.levels, self.codes, strict=True):
            level_strs = level._get_values_for_csv(na_rep=na_rep, **kwargs)
            # add nan values, if there are any
            mask = level_codes == -1
            if mask.any():
                nan_index = len(level_strs)
                # numpy 1.21 deprecated implicit string casting
                level_strs = level_strs.astype(str)
                level_strs = np.append(level_strs, na_rep)
                assert not level_codes.flags.writeable  # i.e. copy is needed
                level_codes = level_codes.copy()  # make writeable
                level_codes[mask] = nan_index
            new_levels.append(level_strs)
            new_codes.append(level_codes)

        if len(new_levels) == 1:
            # a single-level multi-index
            return Index(
                new_levels[0].take(new_codes[0]), copy=False
            )._get_values_for_csv()
        else:
            # reconstruct the multi-index
            mi = MultiIndex(
                levels=new_levels,
                codes=new_codes,
                names=self.names,
                sortorder=self.sortorder,
                verify_integrity=False,
            )
            return mi._values

    def dropna(self, how: AnyAll = "any") -> MultiIndex:
        """
        Return MultiIndex without NA/NaN values.

        Parameters
        ----------
        how : {'any', 'all'}, default 'any'
            Drop the value when any or all levels are NaN.

        Returns
        -------
        Index
            Returns a MultiIndex object after removing NA/NaN values.

        See Also
        --------
        Index.fillna : Fill NA/NaN values with the specified value.
        Index.isna : Detect missing values.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays(([np.nan, np.nan, 2.0], [3.0, np.nan, 4.0]))
        >>> mi.dropna()
        MultiIndex([(2.0, 4.0)],
                   )
        >>> mi.dropna(how="all")
        MultiIndex([(nan, 3.0),
                    (2.0, 4.0)],
                   )
        """
        nans = [level_codes == -1 for level_codes in self.codes]
        if how == "any":
            indexer = np.any(nans, axis=0)
        elif how == "all":
            indexer = np.all(nans, axis=0)
        else:
            raise ValueError(f"invalid how option: {how}")

        new_codes = [level_codes[~indexer] for level_codes in self.codes]
        return self.set_codes(codes=new_codes)

    def putmask(self, mask, value: MultiIndex) -> MultiIndex:  # type: ignore[override]
        """
        Return a new MultiIndex of the values set with the mask.

        Parameters
        ----------
        mask : array like
        value : MultiIndex
            Must either be the same length as self or length one

        Returns
        -------
        MultiIndex
        """
        mask, noop = validate_putmask(self, mask)
        if noop:
            return self.copy()

        if len(mask) == len(value):
            subset = value[mask].remove_unused_levels()
        else:
            subset = value.remove_unused_levels()

        new_levels = []
        new_codes = []

        for i, (value_level, level, level_codes) in enumerate(
            zip(subset.levels, self.levels, self.codes, strict=True)
        ):
            new_level = level.union(value_level, sort=False)
            value_codes = new_level.get_indexer_for(subset.get_level_values(i))
            new_code = ensure_int64(level_codes)
            new_code[mask] = value_codes
            new_levels.append(new_level)
            new_codes.append(new_code)

        return MultiIndex(
            levels=new_levels, codes=new_codes, names=self.names, verify_integrity=False
        )

file core/indexes/base.py
imports: __future__, collections, datetime, functools, itertools, operator, typing, warnings
defines: Index, _maybe_return_indexers, join, _new_Index, maybe_sequence_to_range, ensure_index_from_sequences, ensure_index, trim_front, _validate_join_method, maybe_extract_name, get_unanimous_names, _unpack_nested_dtype, _maybe_try_sort, get_values_for_csv

class Index(IndexOpsMixin, PandasObject):  [core/indexes/base.py:318]
methods: _arith_method, _assert_can_do_setop
         _can_hold_identifiers_and_holds_name
         _can_hold_na, _can_hold_strings, _can_use_libjoin
         _check_indexing_error, _check_indexing_method
         _cleanup, _cmp_method, _concat, _construct_result
         _constructor, _convert_can_do_setop
         _convert_slice_indexer, _convert_tolerance
         _difference, _difference_compat
         _dir_additions_for_owner, _drop_level_numbers
         _dti_setop_align_tzs, _dtype_to_subclass, _engine
         _engine_type, _ensure_array
         _filter_indexer_tolerance
         _find_common_type_compat, _format_attrs
         _format_data, _format_duplicate_message
         _format_flat, _format_with_header
         _formatter_func, _from_join_target
         _get_default_index_names, _get_engine_target
         _get_fill_indexer, _get_fill_indexer_searchsorted
         _get_indexer, _get_indexer_non_comparable
         _get_indexer_non_comparable
         _get_indexer_non_comparable
         _get_indexer_non_comparable, _get_indexer_strict
         _get_join_target, _get_leaf_sorter
         _get_level_names, _get_level_number
         _get_level_values, _get_names
         _get_nearest_indexer, _get_reconciled_name_object
         _get_string_slice, _get_values_for_csv
         _getitem_slice, _index_as_unique, _inner_indexer
         _intersection, _intersection_via_get_indexer
         _is_all_dates, _is_comparable_dtype
         _is_memory_usage_qualified, _is_multi
         _is_strictly_monotonic_decreasing
         _is_strictly_monotonic_increasing, _isnan
         _join_empty, _join_level, _join_monotonic
         _join_multi, _join_non_unique
         _join_via_get_indexer, _left_indexer
         _left_indexer_unique, _logical_method
         _maybe_cast_indexer, _maybe_cast_listlike_indexer
         _maybe_cast_slice_bound, _maybe_check_unique
         _maybe_copy_array_input
         _maybe_disable_logical_methods
         _maybe_disallow_fill
         _maybe_downcast_for_indexing
         _maybe_preserve_names, _mpl_repr, _na_value
         _outer_indexer, _raise_if_missing
         _raise_invalid_indexer, _raise_scalar_data_error
         _reindex_non_unique, _rename, _reset_identity
         _searchsorted_monotonic, _set_names
         _shallow_copy, _should_compare
         _should_fallback_to_positional
         _should_partial_index, _simple_new
         _sort_levels_monotonic, _summary
         _transform_index, _unary_method, _union
         _validate_can_reindex, _validate_fill_value
         _validate_index_level, _validate_indexer
         _validate_names, _validate_positional_slice
         _validate_sort_keyword, _values, _view
         _with_infer, _wrap_difference_result
         _wrap_intersection_result, _wrap_join_result
         _wrap_reindex_result, _wrap_setop_result, all
         any, append, argmax, argmin, argsort, array, asof
         asof_locs, astype, copy, delete, diff, difference
         drop, drop_duplicates, droplevel, dropna, dtype
         duplicated, equals, fillna, get_indexer
         get_indexer_for, get_indexer_non_unique, get_loc
         get_slice_bound, groupby, has_duplicates, hasnans
         identical, infer_objects, inferred_type, insert
         intersection, is_, is_monotonic_decreasing
         is_monotonic_increasing, is_unique, isin, isna
         join, join, join, join, map, max, memory_usage
         min, name, name, nlevels, notna, putmask, ravel
         reindex, rename, rename, rename, repeat, round
         set_names, set_names, set_names, set_names, shape
         shift, slice_indexer, slice_locs, sort_values
         sort_values, sort_values, sort_values, sortlevel
         symmetric_difference, take, to_flat_index
         to_frame, to_series, union, unique, values, view
         where, __abs__, __array__, __array_ufunc__
         __array_wrap__, __bool__, __contains__, __copy__
         __deepcopy__, __getitem__, __getitem__
         __getitem__, __iadd__, __invert__, __len__
         __neg__, __new__, __pos__, __reduce__, __repr__
         __setitem__

    def values(self) -> np.ndarray:
        return self._values

# --- Layer 04: Variable context ---
# call-chain context
  called by: _format_with_header [datetimelike.py]
  called by: _initialize_columns [csvs.py]

# call-chain context
  called by: time_dropna [frame_methods.py]
  called by: time_dropna_axis_mixed_dtypes [frame_methods.py]

# call-chain context
  called by: time_putmask [multiindex_object.py]
  called by: time_putmask_all_different [multiindex_object.py]

# call-chain context
  called by: looper_wrapper [executor.py]
  called by: map_array [algorithms.py]

```
