# pandas-84 :: tacm

query: BUG: Fix MutliIndexed unstack failures at tuple names (#30943)

## selected nodes

- rank=1 layer=FILE tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=2 layer=FILE tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=3 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/melt.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/melt.py
- rank=4 layer=CLASS tokens=375 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py::TestStackUnstackMultiLevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py
- rank=5 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::ReshapeExtensionDtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=6 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::SparseIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=7 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::SimpleReshape file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=8 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=9 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=10 layer=CLASS tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_at_time.py::TestAtTime file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_at_time.py
- rank=11 layer=CLASS tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_at.py::TestAtErrors file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_at.py
- rank=12 layer=CLASS tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_at.py::TestAtSetItem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_at.py
- rank=13 layer=CLASS tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=14 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::SparseIndex.time_unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=15 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::SimpleReshape.time_unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=16 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::ReshapeExtensionDtype.time_unstack_slow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=17 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::ReshapeExtensionDtype.time_unstack_fast file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=18 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Unstack.time_full_product file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=19 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Unstack.time_without_last_row file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=20 layer=FUNCTION tokens=355 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=21 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=22 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py::TestDataFrameReshape.unstack_and_compare file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py
- rank=23 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::loads file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=24 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_extension_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=25 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::ReshapeExtensionDtype.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=26 layer=FUNCTION tokens=138 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=27 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=28 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=29 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=30 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.at file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=31 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::SimpleReshape.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=32 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=33 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.column_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=34 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::reduction_func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py
- rank=35 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=36 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._getitem_nested_tuple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=37 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::get_unanimous_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=38 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._maybe_match_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=39 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._join_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=40 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.get_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=41 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py::agg_before file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py
- rank=42 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._extract_multi_indexer_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=43 layer=FUNCTION tokens=351 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=44 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py::_func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py

## context

```text
file core/reshape/reshape.py
imports: __future__, itertools, typing, warnings, numpy, pandas
defines: _Unstacker, _unstack_multiple, unstack, unstack, unstack, _unstack_frame, _unstack_extension_series, stack, stack_factorize, stack_multiple, _stack_multi_column_index, _stack_multi_columns, _convert_level_number, _reorder_for_extension_array_stack, stack_v3, stack_reshape

file asv_bench/benchmarks/reshape.py
imports: itertools, string, numpy, pandas
defines: Melt, Pivot, SimpleReshape, ReshapeExtensionDtype, ReshapeMaskedArrayDtype, Unstack, SparseIndex, WideToLong, PivotTable, Crosstab, GetDummies, Cut, Explode

file core/reshape/melt.py
imports: __future__, re, typing, numpy, pandas, collections
defines: ensure_list_vars, melt, lreshape, wide_to_long, get_var_names, melt_stub

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

class ReshapeExtensionDtype:  [asv_bench/benchmarks/reshape.py:61]
methods: setup, time_stack, time_transpose, time_unstack_fast
         time_unstack_slow

class SparseIndex:  [asv_bench/benchmarks/reshape.py:148]
methods: setup, time_unstack

class SimpleReshape:  [asv_bench/benchmarks/reshape.py:47]
methods: setup, time_stack, time_unstack

class Unstack:  [asv_bench/benchmarks/reshape.py:115]
methods: setup, time_full_product, time_without_last_row

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class TestAtTime:  [frame/methods/test_at_time.py:20]
methods: test_at_time, test_at_time_ambiguous_format_deprecation
         test_at_time_axis, test_at_time_datetimeindex
         test_at_time_errors, test_at_time_midnight
         test_at_time_nonexistent, test_at_time_raises
         test_at_time_tz, test_localized_at_time

class TestAtErrors:  [tests/indexing/test_at.py:192]
methods: test_at_applied_for_rows, test_at_categorical_integers
         test_at_frame_multiple_columns
         test_at_frame_raises_key_error
         test_at_frame_raises_key_error2
         test_at_getitem_mixed_index_no_fallback
         test_at_series_raises_key_error
         test_at_series_raises_key_error2

class TestAtSetItem:  [tests/indexing/test_at.py:70]
methods: test_at_datetime_index
         test_at_setitem_categorical_missing
         test_at_setitem_mixed_index_assignment
         test_at_setitem_multiindex

class IndexingMixin:  [pandas/core/indexing.py:165]
methods: at, iat, iloc, loc

    def time_unstack(self):
        self.df.unstack()

    def time_unstack(self):
        self.df.unstack(1)

    def time_unstack_slow(self, dtype):
        # first level -> must make copies
        self.ser.unstack("foo")

    def time_unstack_fast(self, dtype):
        # last level -> doesn't have to make copies
        self.ser.unstack("bar")

    def time_full_product(self, dtype):
        self.df.unstack()

    def time_without_last_row(self, dtype):
        self.df2.unstack()

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

        def unstack_and_compare(df, column_name):
            unstacked1 = df.unstack([column_name])
            unstacked2 = df.unstack(column_name)
            tm.assert_frame_equal(unstacked1, unstacked2)

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

    def setup(self, dtype):
        lev = pd.Index(list("ABCDEFGHIJ"))
        ri = pd.Index(range(1000))
        mi = MultiIndex.from_product([lev, ri], names=["foo", "bar"])

        index = date_range("2016-01-01", periods=10000, freq="s", tz="US/Pacific")
        if dtype == "Period[s]":
            index = index.tz_localize(None).to_period("s")

        ser = pd.Series(index, index=mi)
        df = ser.unstack("bar")
        # roundtrips -> df.stack().equals(ser)

        self.ser = ser
        self.df = df

def _unstack_frame(
    obj: DataFrame, level, fill_value=None, sort: bool = True
) -> DataFrame:
    assert isinstance(obj.index, MultiIndex)  # checked by caller
    unstacker = _Unstacker(
        obj.index, level=level, constructor=obj._constructor, sort=sort
    )

    if not obj._can_fast_transpose:
        mgr = obj._mgr.unstack(unstacker, fill_value=fill_value)
        return obj._constructor_from_mgr(mgr, axes=mgr.axes)
    else:
        return unstacker.get_result(
            obj, value_columns=obj.columns, fill_value=fill_value
        )

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

    def at(self) -> _AtIndexer:
        """
        Access a single value for a row/column label pair.

        Similar to ``loc``, in that both provide label-based lookups. Use
        ``at`` if you only need to get or set a single value in a DataFrame
        or Series.

        Raises
        ------
        KeyError
            If getting a value and 'label' does not exist in a DataFrame or Series.
    # ... truncated

    def setup(self):
        arrays = [np.arange(100).repeat(100), np.roll(np.tile(np.arange(100), 100), 25)]
        index = MultiIndex.from_arrays(arrays)
        self.df = DataFrame(np.random.randn(10000, 4), index=index)
        self.udf = self.df.unstack(1)

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

    def column_names(self) -> Iterable[str]:
        """
        Return an iterator yielding the column names.
        """

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

    def _maybe_match_names(self, other):
        """
        Try to find common names to attach to the result of an operation between
        a and b. Return a consensus list of names if they match at least partly
        or list of None if they have completely different names.
        """
        if len(self.names) != len(other.names):
            return [None] * len(self.names)
        names = []
        for a_name, b_name in zip(self.names, other.names, strict=True):
            if a_name == b_name:
                names.append(a_name)
            else:
                # TODO: what if they both have np.nan for their names?
                names.append(None)
        return names

    def _join_multi(
        self, other: Index, how: JoinHow
    ) -> tuple[Index, npt.NDArray[np.intp] | None, npt.NDArray[np.intp] | None]:
        from pandas.core.indexes.multi import MultiIndex
        from pandas.core.reshape.merge import restore_dropped_levels_multijoin

        # figure out join names
        self_names_list = list(self.names)
        other_names_list = list(other.names)
        self_names_order = self_names_list.index
        other_names_order = other_names_list.index
        self_names = set(self_names_list)
    # ... truncated

    def get_column(self, i: int) -> Column:
        """
        Return the column at the indicated position.
        """

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

    def _extract_multi_indexer_columns(
        self,
        header,
        index_names: Sequence[Hashable] | None,
        passed_names: bool = False,
    ) -> tuple[
        Sequence[Hashable], Sequence[Hashable] | None, Sequence[Hashable] | None, bool
    ]:
        """
    # ... truncated

    def _unstack(
        self,
        unstacker,
        fill_value,
        new_placement: npt.NDArray[np.intp],
        needs_masking: npt.NDArray[np.bool_],
    ):
        # ExtensionArray-safe unstack.
        # We override Block._unstack, which unstacks directly on the
        # values of the array. For EA-backed blocks, this would require
        # converting to a 2-D ndarray of objects.
        # Instead, we unstack an ndarray of integer positions, followed by
        # a `take` on the actual values.

        # Caller is responsible for ensuring self.shape[-1] == len(unstacker.index)
        new_values = unstacker.arange_result

        # needs_masking[i] calculated once in BlockManager.unstack tells
        #  us if there are any -1s in the relevant indices.  When False,
        #  that allows us to go through a faster path in 'take', among
        #  other things avoiding e.g. Categorical._validate_scalar.
        blocks = [
            # TODO: could cast to object depending on fill_value?
            type(self)(
                self.values.take(
                    indices, allow_fill=needs_masking[i], fill_value=fill_value
                ),
                BlockPlacement(place),
                ndim=2,
            )
            for i, (indices, place) in enumerate(
                zip(new_values.T, new_placement, strict=True)
            )
        ]
        return blocks

        def _func(data):
            d = data.loc[data.index.map(lambda x: x.hour < 11)].dropna()
            if fix:
                data[data.index[0]]
            if len(d) == 0:
                return None
            return func(d)
```
