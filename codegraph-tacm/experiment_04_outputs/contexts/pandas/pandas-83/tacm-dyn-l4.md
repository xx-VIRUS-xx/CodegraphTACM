# pandas-83 :: tacm-dyn-l4

query: BUG: concat not copying index and columns when copy=True (#31119)

## selected nodes

- rank=1 layer=FILE tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=2 layer=CLASS tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_concat.py::TestConcatenate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_concat.py
- rank=3 layer=FUNCTION tokens=241 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_get_concat_axis_dataframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=4 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=5 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_get_concat_axis_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=6 layer=CLASS tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_dataframe.py::TestDataFrameConcat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_dataframe.py
- rank=7 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=8 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=9 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py::Styler._copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py
- rank=10 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=11 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=12 layer=CLASS tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_index.py::TestIndexConcat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_index.py
- rank=13 layer=FILE tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=14 layer=FUNCTION tokens=262 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::_maybe_reindex_columns_na_proxy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=15 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::concatenate_managers file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=16 layer=FUNCTION tokens=299 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py::_from_dataframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=17 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py::ndarray_to_mgr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py
- rank=18 layer=CLASS tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_sort.py::TestConcatSort file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_sort.py
- rank=19 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=20 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_make_concat_multiindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=21 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=22 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._apply_to_column_groupbys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=23 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py::rec_array_to_mgr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py
- rank=24 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Concat.time_concat_overlapping_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=25 layer=FUNCTION tokens=6 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::at file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
file core/reshape/concat.py
imports: __future__, collections, itertools, types, typing, warnings, numpy, pandas
defines: concat, concat, concat, concat, concat, concat, _sanitize_mixed_ndim, _get_result, new_axes, _get_concat_axis_series, _get_concat_axis_dataframe, _clean_keys_and_objs, _get_sample_object, _concat_indexes, validate_unique_levels, _make_concat_multiindex

class TestConcatenate:  [reshape/concat/test_concat.py:34]
methods: test_append_concat, test_concat_bug_1719
         test_concat_bug_2972, test_concat_bug_3602
         test_concat_copy
         test_concat_different_extension_dtypes_upcasts
         test_concat_duplicate_indices_raise
         test_concat_exclude_none, test_concat_iterables
         test_concat_keys_and_levels
         test_concat_keys_levels_no_overlap
         test_concat_keys_specific_levels
         test_concat_keys_with_none, test_concat_mapping
         test_concat_mixed_objs_columns
         test_concat_mixed_objs_index
         test_concat_mixed_objs_index_names
         test_concat_no_items_raises, test_concat_order
         test_concat_ordered_dict
         test_concat_preserves_rangeindex
         test_concat_single_with_key
         test_concat_with_group_keys
         test_crossed_dtypes_weird_corner
         test_dtype_coercion, test_with_mixed_tuples

def _get_concat_axis_dataframe(
    objs: list[Series | DataFrame],
    axis: AxisInt,
    ignore_index: bool,
    keys: Iterable[Hashable] | None,
    names: list[HashableT] | None,
    levels,
    verify_integrity: bool,
) -> Index:
    """Return result concat axis when concatenating DataFrame objects."""
    indexes_gen = (x.axes[axis] for x in objs)

    if ignore_index:
        return default_index(sum(len(i) for i in indexes_gen))
    else:
        indexes = list(indexes_gen)

    if keys is None:
        if levels is not None:
            raise ValueError("levels supported only when keys is not None")
        concat_axis = _concat_indexes(indexes)
    else:
        concat_axis = _make_concat_multiindex(indexes, keys, levels, names)

    if verify_integrity and not concat_axis.is_unique:
        overlap = concat_axis[concat_axis.duplicated()].unique()
        raise ValueError(f"Indexes have overlapping values: {overlap}")

    return concat_axis

    def copy(self, deep: bool = True) -> Self:
        """
        Make a copy of this object's indices and data.

        When ``deep=True`` (default), a new object will be created with a
        copy of the calling object's data and indices. Modifications to
        the data or indices of the copy will not be reflected in the
        original object (see notes below).

        When ``deep=False``, a new object will be created without copying
        the calling object's data or index (only references to the data
        and index are copied). With Copy-on-Write, changes to the original
    # ... truncated

def _get_concat_axis_series(
    objs: list[Series | DataFrame],
    ignore_index: bool,
    bm_axis: AxisInt,
    keys: Iterable[Hashable] | None,
    levels,
    verify_integrity: bool,
    names: list[HashableT] | None,
) -> Index:
    """Return result concat axis when concatenating Series objects."""
    if ignore_index:
        return default_index(len(objs))
    # ... truncated

class TestDataFrameConcat:  [reshape/concat/test_dataframe.py:14]
methods: test_concat_astype_dup_col, test_concat_axis_parameter
         test_concat_bool_with_int
         test_concat_dataframe_keys_bug
         test_concat_duplicates_in_index_with_keys
         test_concat_multiindex_level_bool_and_numeric
         test_concat_multiple_frames_dtypes
         test_concat_named_keys
         test_concat_numerical_names
         test_concat_tuple_keys, test_inner_sort_columns
         test_outer_sort_columns, test_sort_columns_one_df

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

    def __init__(
        self,
        data=None,
        index: Axes | None = None,
        columns: Axes | None = None,
        dtype: Dtype | None = None,
        copy: bool | None = None,
    ) -> None:
        allow_mgr = False
        if dtype is not None:
            dtype = self._validate_dtype(dtype)

    # ... truncated

    def _copy(self, deepcopy: bool = False) -> Styler:
        """
        Copies a Styler, allowing for deepcopy or shallow copy

        Copying a Styler aims to recreate a new Styler object which contains the same
        data and styles as the original.

        Data dependent attributes [copied and NOT exported]:
          - formatting (._display_funcs)
          - hidden index values or column values (.hidden_rows, .hidden_columns)
          - tooltips
          - cell_context (cell css classes)
    # ... truncated

    def astype(self, dtype: Dtype, copy: bool = True) -> Index:
        """
        Create an Index with values cast to dtypes.

        The class of a new Index is determined by dtype. When conversion is
        impossible, a TypeError exception is raised.

        Parameters
        ----------
        dtype : numpy dtype or pandas type
            Dtype for the result Index.
        copy : bool, default True
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

class TestIndexConcat:  [reshape/concat/test_index.py:17]
methods: test_concat_copy_index_frame
         test_concat_copy_index_series
         test_concat_ignore_index
         test_concat_rename_index
         test_concat_same_index_names, test_default_index
         test_dups_index

file core/internals/concat.py
imports: __future__, typing, numpy, pandas, collections
defines: JoinUnit, concatenate_managers, _maybe_reindex_columns_na_proxy, _is_homogeneous_mgr, _concat_homogeneous_fastpath, _get_combined_plan, _get_block_for_concat_plan, _concatenate_join_units, _dtype_to_na_value, _get_empty_dtype, _is_uniform_join_units

def _maybe_reindex_columns_na_proxy(
    axes: list[Index],
    mgrs_indexers: list[tuple[BlockManager, dict[int, np.ndarray]]],
    needs_copy: bool,
) -> list[BlockManager]:
    """
    Reindex along columns so that all of the BlockManagers being concatenated
    have matching columns.

    Columns added in this reindexing have dtype=np.void, indicating they
    should be ignored when choosing a column's final dtype.
    """
    new_mgrs = []

    for mgr, indexers in mgrs_indexers:
        # For axis=0 (i.e. columns) we use_na_proxy and only_slice, so this
        #  is a cheap reindexing.
        for i, indexer in indexers.items():
            mgr = mgr.reindex_indexer(
                axes[i],
                indexer,
                axis=i,
                only_slice=True,  # only relevant for i==0
                allow_dups=True,
                use_na_proxy=True,  # only relevant for i==0
            )
        if needs_copy and not indexers:
            mgr = mgr.copy(deep=True)

        new_mgrs.append(mgr)
    return new_mgrs

def concatenate_managers(
    mgrs_indexers, axes: list[Index], concat_axis: AxisInt, copy: bool
) -> BlockManager:
    """
    # ... truncated

def _from_dataframe(df: DataFrameXchg, allow_copy: bool = True) -> pd.DataFrame:
    """
    Build a ``pd.DataFrame`` from the DataFrame interchange object.

    Parameters
    ----------
    df : DataFrameXchg
        Object supporting the interchange protocol, i.e. `__dataframe__` method.
    allow_copy : bool, default: True
        Whether to allow copying the memory to perform the conversion
        (if false then zero-copy approach is requested).

    Returns
    -------
    pd.DataFrame
    """
    pandas_dfs = []
    for chunk in df.get_chunks():
        pandas_df = protocol_df_chunk_to_pandas(chunk)
        pandas_dfs.append(pandas_df)

    if not allow_copy and len(pandas_dfs) > 1:
        raise RuntimeError(
            "To join chunks a copy is required which is forbidden by allow_copy=False"
        )
    if not pandas_dfs:
        pandas_df = protocol_df_chunk_to_pandas(df)
    elif len(pandas_dfs) == 1:
        pandas_df = pandas_dfs[0]
    else:
        pandas_df = pd.concat(pandas_dfs, axis=0, ignore_index=True, copy=False)

    index_obj = df.metadata.get("pandas.index", None)
    if index_obj is not None:
        pandas_df.index = index_obj

    return pandas_df

def ndarray_to_mgr(
    values, index, columns, dtype: DtypeObj | None, copy: bool
) -> Manager:
    # used in DataFrame.__init__
    # input must be an ndarray, list, Series, Index, ExtensionArray
    infer_object = not isinstance(values, (ABCSeries, Index, ExtensionArray))

    if isinstance(values, ABCSeries):
        if columns is None:
            if values.name is not None:
                columns = Index([values.name])
        if index is None:
    # ... truncated

class TestConcatSort:  [reshape/concat/test_sort.py:9]
methods: test_concat_aligned_sort
         test_concat_aligned_sort_does_not_raise
         test_concat_frame_with_sort_false
         test_concat_inner_sort
         test_concat_sort_none_raises
         test_concat_sorts_columns, test_concat_sorts_index

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

def _make_concat_multiindex(indexes, keys, levels=None, names=None) -> MultiIndex:
    if (levels is None and isinstance(keys[0], tuple)) or (
        levels is not None and len(levels) > 1
    ):
        zipped = list(zip(*keys, strict=True))
        if names is None:
            names = [None] * len(zipped)

        if levels is None:
            _, levels = factorize_from_iterables(zipped)
        else:
            levels = [ensure_index(x) for x in levels]
    # ... truncated

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

def dict_to_mgr(
    data: dict,
    index,
    columns,
    *,
    dtype: DtypeObj | None = None,
    copy: bool = True,
) -> Manager:
    """
    # ... truncated

    def time_concat_overlapping_index(self):
        pd.concat([self.df_a, self.df_a])

# --- Layer 04: Variable context ---
# call-chain context
  called by: new_axes [concat.py]

# call-chain context
  called by: setup [categoricals.py]
  called by: setup [frame_methods.py]

# call-chain context
  called by: _get_result [concat.py]

# call-chain context
  called by: to_latex [style.py]
  called by: to_typst [style.py]

# call-chain context
  called by: setup_cache [algorithms.py]
  called by: setup [algorithms.py]

# call-chain context
  called by: check_indexing_smoketest_or_raises [common.py]

# call-chain context
  called by: concatenate_managers [concat.py]

# call-chain context
  called by: _get_result [concat.py]

# call-chain context
  called by: from_dataframe [from_dataframe.py]

# call-chain context
  called by: __init__ [frame.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: _get_concat_axis_series [concat.py]
  called by: _get_concat_axis_dataframe [concat.py]

# call-chain context
  called by: setup [algorithms.py]
  called by: setup [algorithms.py]

# call-chain context
  called by: __init__ [frame.py]

```
