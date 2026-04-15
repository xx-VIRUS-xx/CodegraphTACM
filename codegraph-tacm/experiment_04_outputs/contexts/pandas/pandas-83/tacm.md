# pandas-83 :: tacm

query: BUG: concat not copying index and columns when copy=True (#31119)

## selected nodes

- rank=1 layer=FILE tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=2 layer=FILE tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=3 layer=FILE tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py
- rank=4 layer=CLASS tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_concat.py::TestConcatenate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_concat.py
- rank=5 layer=CLASS tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_dataframe.py::TestDataFrameConcat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_dataframe.py
- rank=6 layer=CLASS tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_index.py::TestIndexConcat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_index.py
- rank=7 layer=CLASS tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_sort.py::TestConcatSort file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_sort.py
- rank=8 layer=CLASS tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_series.py::TestSeriesConcat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_series.py
- rank=9 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=10 layer=CLASS tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Concat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=11 layer=FUNCTION tokens=241 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_get_concat_axis_dataframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=12 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=13 layer=FUNCTION tokens=262 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::_maybe_reindex_columns_na_proxy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=14 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::concatenate_managers file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=15 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_get_concat_axis_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=16 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_make_concat_multiindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=17 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::concat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=18 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Concat.time_concat_overlapping_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=19 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Concat.time_concat_non_overlapping_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=20 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::_concatenate_join_units file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=21 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py::Styler._copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py
- rank=22 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=23 layer=FUNCTION tokens=299 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py::_from_dataframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=24 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py::ndarray_to_mgr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py
- rank=25 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=26 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=27 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._apply_to_column_groupbys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=28 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py::rec_array_to_mgr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py
- rank=29 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._concat_objects file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=30 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Concat.time_concat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=31 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical.describe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=32 layer=FUNCTION tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py::dict_to_mgr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py
- rank=33 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._concat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=34 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_concat_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=35 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Concat.time_append_overlapping_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=36 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb::highlight_max file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb

## context

```text
file core/reshape/concat.py
imports: __future__, collections, itertools, types, typing, warnings, numpy, pandas
defines: concat, concat, concat, concat, concat, concat, _sanitize_mixed_ndim, _get_result, new_axes, _get_concat_axis_series, _get_concat_axis_dataframe, _clean_keys_and_objs, _get_sample_object, _concat_indexes, validate_unique_levels, _make_concat_multiindex

file core/internals/concat.py
imports: __future__, typing, numpy, pandas, collections
defines: JoinUnit, concatenate_managers, _maybe_reindex_columns_na_proxy, _is_homogeneous_mgr, _concat_homogeneous_fastpath, _get_combined_plan, _get_block_for_concat_plan, _concatenate_join_units, _dtype_to_na_value, _get_empty_dtype, _is_uniform_join_units

file io/sas/sas_constants.py
imports: __future__, typing
defines: SASIndex

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

class TestIndexConcat:  [reshape/concat/test_index.py:17]
methods: test_concat_copy_index_frame
         test_concat_copy_index_series
         test_concat_ignore_index
         test_concat_rename_index
         test_concat_same_index_names, test_default_index
         test_dups_index

class TestConcatSort:  [reshape/concat/test_sort.py:9]
methods: test_concat_aligned_sort
         test_concat_aligned_sort_does_not_raise
         test_concat_frame_with_sort_false
         test_concat_inner_sort
         test_concat_sort_none_raises
         test_concat_sorts_columns, test_concat_sorts_index

class TestSeriesConcat:  [reshape/concat/test_series.py:16]
methods: test_concat_bool_and_numeric
         test_concat_empty_and_non_empty_series_regression
         test_concat_series, test_concat_series_axis1
         test_concat_series_axis1_names_applied
         test_concat_series_axis1_preserves_series_names
         test_concat_series_axis1_same_names_ignore_index
         test_concat_series_axis1_with_reindex
         test_concat_series_length_one_reversed
         test_concat_series_name_npscalar_tuple
         test_concat_series_partial_columns_names

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class Concat:  [asv_bench/benchmarks/categoricals.py:112]
methods: setup, time_append_non_overlapping_index
         time_append_overlapping_index, time_concat
         time_concat_non_overlapping_index
         time_concat_overlapping_index, time_union

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

def concat(
    objs: Iterable[Series | DataFrame] | Mapping[HashableT, Series | DataFrame],
    *,
    axis: Axis = 0,
    join: str = "outer",
    ignore_index: bool = False,
    keys: Iterable[Hashable] | None = None,
    levels=None,
    names: list[HashableT] | None = None,
    verify_integrity: bool = False,
    sort: bool | lib.NoDefault = lib.no_default,
    copy: bool | lib.NoDefault = lib.no_default,
    # ... truncated

    def time_concat_overlapping_index(self):
        pd.concat([self.df_a, self.df_a])

    def time_concat_non_overlapping_index(self):
        pd.concat([self.df_a, self.df_b])

def _concatenate_join_units(join_units: list[JoinUnit], copy: bool) -> ArrayLike:
    """
    Concatenate values from several join units along axis=1.
    """
    empty_dtype = _get_empty_dtype(join_units)

    has_none_blocks = any(unit.block.dtype.kind == "V" for unit in join_units)
    upcasted_na = _dtype_to_na_value(empty_dtype, has_none_blocks)

    to_concat = [
        ju.get_reindexed_values(empty_dtype=empty_dtype, upcasted_na=upcasted_na)
        for ju in join_units
    ]

    if any(is_1d_only_ea_dtype(t.dtype) for t in to_concat):
        # TODO(EA2D): special case not needed if all EAs used HybridBlocks

        # error: No overload variant of "__getitem__" of "ExtensionArray" matches
        # argument type "Tuple[int, slice]"
        to_concat = [
            t if is_1d_only_ea_dtype(t.dtype) else t[0, :]  # type: ignore[call-overload]
            for t in to_concat
        ]
        concat_values = concat_compat(to_concat, axis=0, ea_compat_axis=True)
        concat_values = ensure_block_shape(concat_values, 2)

    else:
        concat_values = concat_compat(to_concat, axis=1)

    return concat_values

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

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

    def _apply_to_column_groupbys(self, func) -> DataFrame:
        from pandas.core.reshape.concat import concat

        obj = self._obj_with_exclusions
        columns = obj.columns
        sgbs = (
            SeriesGroupBy(
                obj.iloc[:, i],
                selection=colname,
                grouper=self._grouper,
                exclusions=self.exclusions,
                observed=self.observed,
            )
            for i, colname in enumerate(obj.columns)
        )
        results = [func(sgb) for sgb in sgbs]

        if not results:
            # concat would raise
            res_df = DataFrame([], columns=columns, index=self._grouper.result_index)
        else:
            res_df = concat(results, keys=columns, axis=1)

        if not self.as_index:
            res_df.index = default_index(len(res_df))
            res_df = self._insert_inaxis_grouper(res_df)
        return res_df

def rec_array_to_mgr(
    data: np.rec.recarray | np.ndarray,
    index,
    columns,
    dtype: DtypeObj | None,
    copy: bool,
) -> Manager:
    """
    Extract from a masked rec array and create the manager.
    """
    # essentially process a record array then fill it
    fdata = ma.getdata(data)
    if index is None:
        index = default_index(len(fdata))
    else:
        index = ensure_index(index)

    if columns is not None:
        columns = ensure_index(columns)
    arrays, arr_columns = to_arrays(fdata, columns)

    # create the manager

    arrays, arr_columns = reorder_arrays(arrays, arr_columns, columns, len(index))
    if columns is None:
        columns = arr_columns

    mgr = arrays_to_mgr(arrays, columns, index, dtype=dtype)

    if copy:
        mgr = mgr.copy(deep=True)
    return mgr

    def _concat_objects(
        self,
        values,
        not_indexed_same: bool = False,
        is_transform: bool = False,
    ):
        from pandas.core.reshape.concat import concat

        if self.group_keys and not is_transform:
            if self.as_index:
                # possible MI return case
                group_keys = self._grouper.result_index
    # ... truncated

    def time_concat(self):
        pd.concat([self.s, self.s])

    def describe(self) -> DataFrame:
        """
        Describes this Categorical

        Returns
        -------
        description: `DataFrame`
            A dataframe with frequency and counts by category.
        """
        counts = self.value_counts(dropna=False)
        freqs = counts / counts.sum()

        from pandas import Index
        from pandas.core.reshape.concat import concat

        result = concat([counts, freqs], ignore_index=True, axis=1)
        result.columns = Index(["counts", "freqs"])
        result.index.name = "categories"

        return result

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

    def _concat(self, to_concat: list[Index], name: Hashable) -> Index:
        """
        Concatenate multiple Index objects.
        """
        to_concat_vals = [x._values for x in to_concat]

        result = concat_compat(to_concat_vals)

        return Index._with_infer(result, name=name, copy=False)

def _concat_indexes(indexes) -> Index:
    return indexes[0].append(indexes[1:])

    def time_append_overlapping_index(self):
        self.idx_a.append(self.idx_a)

  {
   "cell_type": "markdown",
```
