# pandas-84 :: tacm-dyn-l4

query: BUG: Fix MutliIndexed unstack failures at tuple names (#30943)

## selected nodes

- rank=1 layer=FILE tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=2 layer=CLASS tokens=375 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py::TestStackUnstackMultiLevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py
- rank=3 layer=FUNCTION tokens=355 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=4 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=5 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::SparseIndex.time_unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=6 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::SimpleReshape.time_unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=7 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py::TestDataFrameReshape.unstack_and_compare file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py
- rank=8 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::ReshapeExtensionDtype.time_unstack_slow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=9 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::loads file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=10 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=11 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=12 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::ReshapeExtensionDtype.time_unstack_fast file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=13 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=14 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=15 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.items file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=16 layer=CLASS tokens=436 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py::TestDataFrameReshape file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py
- rank=17 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=18 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::reduction_func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py
- rank=19 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=20 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._getitem_nested_tuple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=21 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Unstack.time_full_product file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=22 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_extension_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=23 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::get_unanimous_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=24 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._maybe_match_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=25 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._join_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=26 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py::agg_before file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py
- rank=27 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._extract_multi_indexer_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=28 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Unstack.time_without_last_row file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=29 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DataFrameStringIndexing.time_at file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py

## context

```text
file core/reshape/reshape.py
imports: __future__, itertools, typing, warnings, numpy, pandas
defines: _Unstacker, _unstack_multiple, unstack, unstack, unstack, _unstack_frame, _unstack_extension_series, stack, stack_factorize, stack_multiple, _stack_multi_column_index, _stack_multi_columns, _convert_level_number, _reorder_for_extension_array_stack, stack_v3, stack_reshape

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

def unstack(
    obj: Series | DataFrame, level, fill_value=None, sort: bool = True
) -> Series | DataFrame:
    if isinstance(level, (tuple, list)):
        if len(level) != 1:
            # _unstack_multiple only handles MultiIndexes,
            # and isn't needed for a single level
            return _unstack_multiple(obj, level, fill_value=fill_value, sort=sort)
        else:
            level = level[0]

    if not is_integer(level) and not level == "__placeholder__":
        # check if level is valid in case of regular index
        obj.index._get_level_number(level)

    if isinstance(obj, DataFrame):
        if isinstance(obj.index, MultiIndex):
            return _unstack_frame(obj, level, fill_value=fill_value, sort=sort)
        else:
            return obj.T.stack()
    elif not isinstance(obj.index, MultiIndex):
        # GH 36113
        # Give nicer error messages when unstack a Series whose
        # Index is not a MultiIndex.
        raise ValueError(
            f"index must be a MultiIndex to unstack, {type(obj.index)} was passed"
        )
    else:
        if is_1d_only_ea_dtype(obj.dtype):
            return _unstack_extension_series(obj, level, fill_value, sort=sort)
        unstacker = _Unstacker(
            obj.index, level=level, constructor=obj._constructor_expanddim, sort=sort
        )
        return unstacker.get_result(obj, value_columns=None, fill_value=fill_value)

def _unstack_multiple(
    data: Series | DataFrame, clocs, fill_value=None, sort: bool = True
):
    if len(clocs) == 0:
        return data

    # NOTE: This doesn't deal with hierarchical columns yet

    index = data.index
    index = cast("MultiIndex", index)  # caller is responsible for checking

    # GH 19966 Make sure if MultiIndexed index has tuple name, they will be
    # ... truncated

    def time_unstack(self):
        self.df.unstack()

    def time_unstack(self):
        self.df.unstack(1)

        def unstack_and_compare(df, column_name):
            unstacked1 = df.unstack([column_name])
            unstacked2 = df.unstack(column_name)
            tm.assert_frame_equal(unstacked1, unstacked2)

    def time_unstack_slow(self, dtype):
        # first level -> must make copies
        self.ser.unstack("foo")

def loads(
    bytes_object: bytes,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
) -> Any:
    """
    Analogous to pickle._loads.
    """
    fd = io.BytesIO(bytes_object)
    return Unpickler(
        fd, fix_imports=fix_imports, encoding=encoding, errors=errors
    ).load()

    def unstack(
        self, level: IndexLabel = -1, fill_value=None, sort: bool = True
    ) -> DataFrame | Series:
        """
    # ... truncated

    def unstack(
        self,
        level: IndexLabel = -1,
        fill_value: Hashable | None = None,
        sort: bool = True,
    ) -> DataFrame:
        """
    # ... truncated

    def time_unstack_fast(self, dtype):
        # last level -> doesn't have to make copies
        self.ser.unstack("bar")

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

    def items(self) -> Iterable[tuple[Hashable, Series]]:
        r"""
        Iterate over (column name, Series) pairs.

        Iterates over the DataFrame columns, returning a tuple with
        the column name and the content as a Series.

        Yields
        ------
        label : object
            The column names for the DataFrame being iterated over.
        content : Series
    # ... truncated

class TestDataFrameReshape:  [tests/frame/test_stack_unstack.py:30]
methods: cast, cast, test_stack_datetime_column_multiIndex
         test_stack_full_multiIndex
         test_stack_int_level_names, test_stack_ints
         test_stack_mixed_level, test_stack_mixed_levels
         test_stack_multi_columns_mixed_extension_types
         test_stack_multi_columns_non_unique_index
         test_stack_multi_preserve_categorical_dtype
         test_stack_partial_multiIndex
         test_stack_preserve_categorical_dtype
         test_stack_preserve_categorical_dtype_values
         test_stack_unstack, test_unstack_bool
         test_unstack_dtypes
         test_unstack_dtypes_mixed_date, test_unstack_fill
         test_unstack_fill_frame
         test_unstack_fill_frame_categorical
         test_unstack_fill_frame_datetime
         test_unstack_fill_frame_period
         test_unstack_fill_frame_timedelta
         test_unstack_level_binding
         test_unstack_long_index
         test_unstack_mixed_extension_types
         test_unstack_mixed_type_name_in_multiindex
         test_unstack_multi_level_cols
         test_unstack_multi_level_rows_and_cols
         test_unstack_nan_index1, test_unstack_nan_index2
         test_unstack_nan_index3, test_unstack_nan_index4
         test_unstack_nan_index5
         test_unstack_nan_index_repeats
         test_unstack_non_unique_index_names
         test_unstack_not_consolidated
         test_unstack_preserve_dtypes
         test_unstack_swaplevel_sortlevel
         test_unstack_to_series
         test_unstack_tuplename_in_multiindex
         test_unstack_unused_level
         test_unstack_unused_levels
         test_unstack_unused_levels_mixed_with_nan
         unstack_and_compare

    def unstack(self, unstacker, fill_value) -> BlockManager:
        """
        Return a BlockManager with all blocks unstacked.

        Parameters
        ----------
        unstacker : reshape._Unstacker
        fill_value : Any
            fill_value for newly introduced missing values.

        Returns
        -------
    # ... truncated

def reduction_func(request):
    """
    yields the string names of all groupby reduction functions, one at a time.
    """
    return request.param

def names(request) -> tuple[Hashable, Hashable, Hashable]:
    """
    A 3-tuple of names, the first two for operands, the last for a result.
    """
    return request.param

    def _getitem_nested_tuple(self, tup: tuple):
        # we have a nested tuple so have at least 1 multi-index level
        # we should be able to match up the dimensionality here

        for key in tup:
            check_dict_or_set_indexers(key)

        # we have too many indexers for our dim, but have at least 1
        # multi-index dimension, try to see if we have something like
        # a tuple passed to a series with a multi-index
        if len(tup) > self.ndim:
            if self.name != "loc":
    # ... truncated

    def time_full_product(self, dtype):
        self.df.unstack()

def _unstack_extension_series(
    series: Series, level, fill_value, sort: bool
) -> DataFrame:
    """
    Unstack an ExtensionArray-backed Series.

    The ExtensionDtype is preserved.

    Parameters
    ----------
    series : Series
        A Series with an ExtensionArray for values
    level : Any
        The level name or number.
    fill_value : Any
        The user-level (not physical storage) fill value to use for
        missing values introduced by the reshape. Passed to
        ``series.values.take``.
    sort : bool
        Whether to sort the resulting MuliIndex levels

    Returns
    -------
    DataFrame
        Each column of the DataFrame will have the same dtype as
        the input Series.
    """
    # Defer to the logic in ExtensionBlock._unstack
    df = series.to_frame()
    result = df.unstack(level=level, fill_value=fill_value, sort=sort)

    # equiv: result.droplevel(level=0, axis=1)
    #  but this avoids an extra copy
    result.columns = result.columns._drop_level_numbers([0])
    # error: Incompatible return value type (got "DataFrame | Series", expected
    # "DataFrame")
    return result  # type: ignore[return-value]

def get_unanimous_names(*indexes: Index) -> tuple[Hashable, ...]:
    """
    Return common name if all indices agree, otherwise None (level-by-level).

    Parameters
    ----------
    indexes : list of Index objects

    Returns
    -------
    list
        A list representing the unanimous 'names' found.
    """
    name_tups = (tuple(i.names) for i in indexes)
    name_sets = ({*ns} for ns in zip_longest(*name_tups))
    names = tuple(ns.pop() if len(ns) == 1 else None for ns in name_sets)
    return names

    def agg_before(func, fix=False):
        """
        Run an aggregate func on the subset of data.
        """

        def _func(data):
            d = data.loc[data.index.map(lambda x: x.hour < 11)].dropna()
            if fix:
                data[data.index[0]]
            if len(d) == 0:
                return None
            return func(d)

        return _func

    def time_without_last_row(self, dtype):
        self.df2.unstack()

def m():
    return 5

# --- Layer 04: Variable context ---
# call-chain context
  called by: setup [reshape.py]
  called by: time_unstack [reshape.py]

# call-chain context
  called by: unstack [reshape.py]

# call-chain context
  called by: __arrow_ext_deserialize__ [extension_types.py]
  called by: __arrow_ext_deserialize__ [extension_types.py]

# call-chain context
  called by: setup [reshape.py]
  called by: time_unstack [reshape.py]

# call-chain context
  called by: setup [reshape.py]
  called by: time_unstack [reshape.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: setup [categoricals.py]
  called by: time_items [frame_methods.py]

# call-chain context
  called by: setup [reshape.py]
  called by: time_unstack [reshape.py]

# call-chain context
  called by: _getitem_lowerdim [indexing.py]

# call-chain context
  called by: unstack [reshape.py]

# call-chain context
  called by: union_indexes [api.py]
  called by: _convert_can_do_setop [multi.py]

# call-chain context
  called by: _from_derivatives [missing.py]

```
