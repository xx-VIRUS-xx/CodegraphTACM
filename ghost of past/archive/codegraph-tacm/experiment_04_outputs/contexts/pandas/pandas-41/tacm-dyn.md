# pandas-41 :: tacm-dyn

query: BUG: ExtensionBlock.set not setting values inplace (#32831)

## selected nodes

- rank=1 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=2 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=CLASS tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=4 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=5 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=6 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=7 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._iset_not_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=8 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.set_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=9 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=10 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unwrap_setitem_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=11 layer=CLASS tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_partial.py::TestPartialSetting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_partial.py
- rank=12 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents._check_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=13 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=14 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents.is_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=15 layer=CLASS tokens=800 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=16 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._set_axis_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=17 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.replace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=18 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.sort_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=19 layer=CLASS tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_setitem.py::TestDataFrameSetitemCopyViewSemantics file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_setitem.py
- rank=20 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.fillna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=21 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestCanHoldElement.check_series_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py
- rank=22 layer=FILE tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/putmask.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/putmask.py
- rank=23 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py::FillNa.time_fillna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py

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

class ExtensionBlock(EABackedBlock):  [core/internals/blocks.py:1905]
methods: _maybe_squeeze_arg, _slice, _unstack
         _unwrap_setitem_indexer, fillna, iget, is_numeric
         is_view, set_inplace, shape, slice_block_rows

    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None:
        # When an ndarray, we should have locs.tolist() == [0]
        # When a BlockPlacement we should have list(locs) == [0]
        if copy:
            self.values = self.values.copy()
        self.values[:] = values

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

    def _set_name(self, name, inplace: bool = False) -> Series:
        """
        Set the Series name.

        Parameters
        ----------
        name : str
        inplace : bool
            Whether to modify `self` directly or return a copy.
        """
        inplace = validate_bool_kwarg(inplace, "inplace")
        ser = self if inplace else self.copy(deep=False)
        ser.name = name
        return ser

    def _iset_not_inplace(self, key, value) -> None:
        # GH#39510 when setting with df[key] = obj with a list-like key and
        #  list-like value, we iterate over those listlikes and set columns
        #  one at a time.  This is different from dispatching to
        #  `self.loc[:, key]= value`  because loc.__setitem__ may overwrite
        #  data inplace, whereas this will insert new arrays.

        def igetitem(obj, i: int):
            # Note: we catch DataFrame obj before getting here, but
            #  hypothetically would return obj.iloc[:, i]
            if isinstance(obj, np.ndarray):
                return obj[..., i]
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

    def _set_with_engine(self, key, value) -> None:
        loc = self.index.get_loc(key)

        # this is equivalent to self._values[key] = value
        self._mgr.setitem_inplace(loc, value)

    def _unwrap_setitem_indexer(self, indexer):
        """
        Adapt a 2D-indexer to our 1D values.

        This is intended for 'setitem', not 'iget' or '_slice'.
        """
    # ... truncated

class TestPartialSetting:  [tests/indexing/test_partial.py:239]
methods: test_cannot_expand_with_iloc_iat
         test_loc_with_list_of_strings_representing_datetimes
         test_loc_with_list_of_strings_representing_datetimes_missing_value
         test_loc_with_list_of_strings_representing_datetimes_not_matched_type
         test_partial_set_invalid, test_partial_setting
         test_partial_setting2, test_partial_setting_frame
         test_partial_setting_mixed_dtype
         test_series_partial_set
         test_series_partial_set_with_name
         test_setitem_with_expansion_numeric_into_datetimeindex

    def _check_inplace(self, is_inplace, orig, arr, obj):
        if is_inplace is None:
            # We are not (yet) checking whether setting is inplace or not
            pass
        elif is_inplace:
            if arr.dtype.kind in ["m", "M"]:
                # We may not have the same DTA/TDA, but will have the same
                #  underlying data
                assert arr._ndarray is obj._values._ndarray
            else:
                assert obj._values is arr
        else:
            # otherwise original array should be unchanged
            tm.assert_equal(arr, orig._values)

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

    def is_inplace(self, obj, expected):
        """
        Whether we expect the setting to be in-place or not.
        """
        return expected.dtype == obj.dtype

class NDFrame(PandasObject, indexing.IndexingMixin):  [pandas/core/generic.py:209]
methods: _accum_func, _align_frame, _align_series
         _check_copy_deprecation
         _check_inplace_and_allows_duplicate_labels
         _check_label_or_level_ambiguity
         _clip_with_one_bound, _clip_with_scalar
         _consolidate, _consolidate_inplace
         _construct_axes_dict, _constructor
         _dir_additions, _drop_axis
         _drop_labels_or_levels, _find_valid_index
         _from_mgr, _get_axis, _get_axis_name
         _get_axis_number, _get_axis_resolvers
         _get_block_manager_axis, _get_bool_data
         _get_cleaned_column_resolvers
         _get_index_resolvers, _get_label_or_level_values
         _get_numeric_data, _getitem_slice, _indexed_same
         _info_axis, _init_mgr, _inplace_method
         _is_label_or_level_reference, _is_label_reference
         _is_level_reference, _is_mixed_type
         _logical_func, _min_count_stat_function
         _needs_reindex_multi, _pad_or_backfill
         _reindex_axes, _reindex_multi
         _reindex_with_indexers, _rename, _rename, _rename
         _rename, _repr_data_resource_, _repr_latex_
         _set_axis, _set_axis_name, _set_axis_name
         _set_axis_name, _set_axis_name, _set_axis_nocheck
         _set_axis_nocheck, _set_axis_nocheck
         _set_axis_nocheck, _shift_with_freq, _slice
         _stat_function, _stat_function_ddof
         _to_latex_via_styler, _tz_convert, _tz_localize
         _update_inplace, _validate_dtype, _values, _where
         _wrap, abs, add_prefix, add_suffix, align, all
         any, asfreq, asof, astype, at_time, attrs, attrs
         axes, between_time, bfill, blk_func, blk_func
         block_accum_func, clip, compare, convert_dtypes
         copy, cummax, cummin, cumprod, cumsum, describe
         drop, drop, drop, drop, droplevel, dtypes, empty
         equals, ewm, expanding, f, f, ffill, fillna
         filter, first_valid_index, flags, get, head
         infer_objects, interpolate, isna, isnull, items
         keys, kurt, last_valid_index, mask, max, mean
         median, min, ndim, notna, notnull, pct_change
         pipe, pipe, pipe, pop, prod, rank, ranker
         reindex, reindex_like, rename_axis, rename_axis
         rename_axis, rename_axis, replace, resample
         rolling, sample, sem, set_axis, set_flags, shape
         shift, size, skew, sort_index, sort_index
         sort_index, sort_index, sort_values, sort_values
         sort_values, sort_values, squeeze, std, sum, tail
         take, to_clipboard, to_csv, to_csv, to_csv
         to_excel, to_hdf, to_json, to_latex, to_latex
         to_latex, to_pickle, to_sql, to_xarray, truncate
         tz_convert, tz_localize, values, var, where, xs
         __abs__, __array__, __array_ufunc__, __bool__
         __contains__, __copy__, __deepcopy__, __delitem__
         __finalize__, __getattr__, __getitem__
         __getstate__, __iadd__, __iand__, __ifloordiv__
         __imod__, __imul__, __init__, __invert__, __ior__
         __ipow__, __isub__, __iter__, __itruediv__
         __ixor__, __len__, __neg__, __pos__, __repr__
         __round__, __setattr__, __setstate__

    def _set_axis_name(
        self, name, axis: Axis = 0, *, inplace: bool = False
    ) -> Self | None:
        """
    # ... truncated

    def replace(
        self,
        to_replace=None,
        value=lib.no_default,
        *,
        inplace: bool = False,
        regex: bool = False,
    ) -> Self:
        """
    # ... truncated

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

    def fillna(
        self,
        value,
        limit: int | None = None,
        inplace: bool = False,
    ) -> list[Block]:
        if isinstance(self.dtype, (IntervalDtype, StringDtype)):
            # Block.fillna handles coercion (test_fillna_interval)
            if isinstance(self.dtype, IntervalDtype) and limit is not None:
                raise ValueError("limit must be None")
            return super().fillna(
                value=value,
    # ... truncated

    def check_series_setitem(self, elem, index: Index, inplace: bool):
        arr = index._data.copy()
        ser = Series(arr, copy=False)

        self.check_can_hold_element(ser, elem, inplace)

        if is_scalar(elem):
            ser[0] = elem
        else:
            ser[: len(elem)] = elem

        if inplace:
            assert ser._values is arr  # i.e. setting was done inplace
        else:
            assert ser.dtype == object

file core/array_algos/putmask.py
imports: __future__, typing, numpy, pandas
defines: putmask_inplace, putmask_without_repeat, validate_putmask, extract_bool_array, setitem_datetimelike_compat

    def time_fillna(self, inplace):
        self.ts.fillna(0.0, inplace=inplace)
```
