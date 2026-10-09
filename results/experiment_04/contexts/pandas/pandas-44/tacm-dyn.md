# pandas-44 :: tacm-dyn

query: BUG: DTI/TDI/PI get_indexer_non_unique with incompatible dtype (#32650)

## selected nodes

- rank=1 layer=FILE tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=2 layer=CLASS tokens=1045 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=3 layer=FUNCTION tokens=368 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=4 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=5 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_strict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=6 layer=CLASS tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_indexing.py::TestGetIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_indexing.py
- rank=7 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._setitem_with_indexer_frame_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=8 layer=CLASS tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py::TestGetIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py
- rank=9 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex.get_indexer_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=10 layer=CLASS tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/base_class/test_indexing.py::TestGetIndexerNonUnique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/base_class/test_indexing.py
- rank=11 layer=FUNCTION tokens=258 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_for file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=12 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=13 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=14 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=15 layer=CLASS tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=16 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=17 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/object/test_indexing.py::TestGetIndexerNonUnique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/object/test_indexing.py
- rank=18 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique_sorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=19 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/string/test_indexing.py::TestGetIndexerNonUnique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/string/test_indexing.py
- rank=20 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb::highlight_max file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb

## context

```text
file core/reshape/merge.py
imports: __future__, datetime, functools, types, typing, warnings, numpy, pandas
defines: _MergeOperation, _CrossMergeOperation, _OrderedMerge, _AsOfMerge, merge, _cross_merge, _groupby_and_merge, merge_ordered, _merger, merge_asof, _maybe_promote_to_rangeindex, get_join_indexers, get_join_indexers_non_unique, restore_dropped_levels_multijoin, _convert_to_multiindex, _asof_by_function, _get_multiindex_indexer, _get_empty_indexer, _get_no_sort_one_missing_indexer, _left_join_on_index, _factorize_keys, _convert_arrays_and_get_rizer_klass, _sort_labels, _get_join_keys, _should_fill, _any, _validate_operand, _items_overlap_with_suffix, renamer

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

    def _get_indexer_non_comparable(
        self, target: Index, method: str_t | None, unique: bool = True
    ) -> npt.NDArray[np.intp] | tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
        Called from get_indexer or get_indexer_non_unique when the target
        is of a non-comparable dtype.

        For get_indexer lookups with method=None, get_indexer is an _equality_
        check, so non-comparable dtypes mean we will always have no matches.

        For get_indexer lookups with a method, get_indexer is an _inequality_
        check, so non-comparable dtypes mean we will always raise TypeError.

        Parameters
        ----------
        target : Index
        method : str or None
        unique : bool, default True
            * True if called from get_indexer.
            * False if called from get_indexer_non_unique.

        Raises
        ------
        TypeError
            If doing an inequality check, i.e. method is not None.
        """
        if method is not None:
            other_dtype = _unpack_nested_dtype(target)
            raise TypeError(f"Cannot compare dtypes {self.dtype} and {other_dtype}")

        no_matches = -1 * np.ones(target.shape, dtype=np.intp)
        if unique:
            # This is for get_indexer
            return no_matches
        else:
            # This is for get_indexer_non_unique
            missing = np.arange(len(target), dtype=np.intp)
            return no_matches, missing

    def get_indexer_non_unique(
        self, target: Axes
    ) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
    # ... truncated

    def _get_indexer_strict(
        self, key: Axes, axis_name: str_t
    ) -> tuple[Index, np.ndarray]:
        """
        Analogue to get_indexer that raises if any elements are missing.
        """
        keyarr = key
        if not isinstance(keyarr, Index):
            keyarr = com.asarray_tuplesafe(keyarr)

        if self._index_as_unique:
            indexer = self.get_indexer_for(keyarr)  # pyright: ignore[reportArgumentType]
            keyarr = self.reindex(keyarr)[0]  # pyright: ignore[reportArgumentType]
        else:
            keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

        self._raise_if_missing(keyarr, indexer, axis_name)

        keyarr = self.take(indexer)
        if isinstance(key, Index):
            # GH 42790 - Preserve name from an Index
            keyarr.name = key.name
        if lib.is_np_dtype(keyarr.dtype, "mM") or isinstance(
            keyarr.dtype, DatetimeTZDtype
        ):
            # DTI/TDI.take can infer a freq in some cases when we dont want one
            if isinstance(key, list) or (
                isinstance(key, type(self))
                # "Index" has no attribute "freq"
                and key.freq is None  # type: ignore[attr-defined]
            ):
                # error: "Index" has no attribute "_with_freq"; maybe "_with_infer"?
                keyarr = keyarr._with_freq(None)  # type: ignore[attr-defined]

        return keyarr, indexer

class TestGetIndexer:  [indexes/interval/test_indexing.py:255]
methods: test_get_index_non_unique_non_monotonic
         test_get_indexer_categorical
         test_get_indexer_categorical_with_nans
         test_get_indexer_datetime
         test_get_indexer_errors
         test_get_indexer_interval_index
         test_get_indexer_length_one
         test_get_indexer_length_one_interval
         test_get_indexer_multiindex_with_intervals
         test_get_indexer_non_monotonic
         test_get_indexer_non_unique_right
         test_get_indexer_non_unique_with_int_and_float
         test_get_indexer_read_only
         test_get_indexer_with_int_and_float
         test_get_indexer_with_interval
         test_get_indexer_with_nans

    def _setitem_with_indexer_frame_value(
        self, indexer, value: DataFrame, name: str
    ) -> None:
        ilocs = self._ensure_iterable_column_indexer(indexer[1])

        sub_indexer = list(indexer)
        pi = indexer[0]

        multiindex_indexer = isinstance(self.obj.columns, MultiIndex)

        unique_cols = value.columns.is_unique

    # ... truncated

class TestGetIndexer:  [indexes/period/test_indexing.py:362]
methods: test_get_indexer, test_get_indexer2
         test_get_indexer_mismatched_dtype
         test_get_indexer_mismatched_dtype_different_length
         test_get_indexer_mismatched_dtype_with_method
         test_get_indexer_non_unique

    def get_indexer_non_unique(
        self, target: Axes
    ) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
    # ... truncated

class TestGetIndexerNonUnique:  [indexes/base_class/test_indexing.py:36]
methods: test_get_indexer_non_unique_dtype_mismatch
         test_get_indexer_non_unique_int_index

    def get_indexer_for(self, target: Axes) -> npt.NDArray[np.intp]:
        """
        Guaranteed return of an indexer even when non-unique.

        This dispatches to get_indexer or get_indexer_non_unique
        as appropriate.

        Parameters
        ----------
        target : Index
            An iterable containing the values to be used for computing indexer.

        Returns
        -------
        np.ndarray[np.intp]
            List of indices.

        See Also
        --------
        Index.get_indexer : Computes indexer and mask for new index given
            the current index.
        Index.get_non_unique : Returns indexer and masks for new index given
            the current index.

        Examples
        --------
        >>> idx = pd.Index([np.nan, "var1", np.nan])
        >>> idx.get_indexer_for([np.nan])
        array([0, 2])
        """
        if self._index_as_unique:
            return self.get_indexer(target)
        indexer, _ = self.get_indexer_non_unique(target)
        return indexer

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

    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

    def time_get_indexer_mismatched_tz(self):
        # reached via e.g.
        #  ser = Series(range(len(dti)), index=dti)
        #  ser[dti2]
        self.dti.get_indexer(self.dti2)

class IntervalIndex(ExtensionIndex):  [core/indexes/interval.py:163]
methods: _convert_slice_indexer, _engine, _from_join_target
         _get_engine_target, _get_indexer
         _get_indexer_monotonic, _get_indexer_pointwise
         _get_indexer_unique_sides, _getitem_slice
         _index_as_unique, _intersection
         _intersection_non_unique, _intersection_unique
         _is_comparable_dtype, _maybe_cast_slice_bound
         _maybe_convert_i8, _multiindex
         _needs_i8_conversion, _searchsorted_monotonic
         _should_fallback_to_positional, from_arrays
         from_breaks, from_tuples, get_indexer_non_unique
         get_loc, inferred_type, is_monotonic_decreasing
         is_overlapping, is_unique, left, length
         memory_usage, mid, right, __contains__, __new__
         __reduce__

    def time_get_loc_non_unique(self, dtype):
        self.non_unique.get_loc(self.key)

class TestGetIndexerNonUnique:  [indexes/object/test_indexing.py:76]
methods: test_get_indexer_non_unique_nas
         test_get_indexer_non_unique_np_nats

    def time_get_loc_non_unique_sorted(self, dtype):
        self.non_unique_sorted.get_loc(self.key)

class TestGetIndexerNonUnique:  [indexes/string/test_indexing.py:108]
methods: test_get_indexer_non_unique_nas

  {
   "cell_type": "markdown",
```
