# pandas-17 :: tacm

query: BUG: DTI/TDI.insert doing invalid casting (#33703)

## selected nodes

- rank=1 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=2 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FILE tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=4 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=5 layer=FILE tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=6 layer=FILE tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/api.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/api.py
- rank=7 layer=CLASS tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=8 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=9 layer=CLASS tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_insert.py::TestDataFrameInsert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_insert.py
- rank=10 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_insert.py::TestInsert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_insert.py
- rank=11 layer=CLASS tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::BaseEngine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=12 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=13 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=14 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_EastAsianTextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=15 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=16 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=17 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic.timedelta64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=18 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::make_invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=19 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=20 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=21 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=22 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::BaseEngine.insert_records file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=23 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=24 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.any file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=25 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.case_when file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=26 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=27 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=28 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/readers.py::read_csv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/readers.py
- rank=29 layer=FUNCTION tokens=260 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::_insert_quantile_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=30 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::_reindex_for_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=31 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.all file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=32 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py::to_numeric file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py
- rank=33 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.sort_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=34 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLTable.insert_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=35 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py::Styler.to_latex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py
- rank=36 layer=FUNCTION tokens=226 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::invalid_comparison file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=37 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/readers.py::read_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/readers.py
- rank=38 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.reset_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=39 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.combine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=40 layer=FUNCTION tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=41 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.map file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=42 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader.read file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=43 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=44 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py

## context

```text
file core/ops/invalid.py
imports: __future__, operator, typing, numpy, collections, pandas
defines: invalid_comparison, make_invalid_op, invalid_op

file pandas/core/frame.py
imports: __future__, collections, functools, io, itertools, operator, sys, typing
defines: DataFrame, _from_nested_dict, _reindex_for_setitem

file core/groupby/groupby.py
imports: __future__, collections, datetime, functools, typing, warnings, numpy, pandas
defines: GroupByPlot, BaseGroupBy, GroupBy, get_groupby, _insert_quantile_level

file pandas/core/generic.py
imports: __future__, collections, copy, datetime, functools, json, operator, pickle
defines: NDFrame

file pandas/core/series.py
imports: __future__, collections, functools, operator, sys, typing, warnings, numpy
defines: Series

file pandas/core/api.py
imports: pandas
defines: —

class TestDatetimeIndexArithmetic:  [tests/arithmetic/test_datetime64.py:2021]
methods: test_dta_add_sub_index, test_dti_add_series
         test_dti_add_tdi
         test_dti_addsub_object_arraylike
         test_dti_addsub_offset_arraylike
         test_dti_iadd_tdi, test_dti_isub_tdi
         test_dti_sub_tdi
         test_ops_nat_mixed_datetime64_timedelta64
         test_sub_dti_dti
         test_timedelta64_equal_timedelta_supported_ops
         test_ufunc_coercions, timedelta64

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

class TestDataFrameInsert:  [frame/indexing/test_insert.py:20]
methods: test_insert, test_insert_EA_no_warning
         test_insert_column_bug_4032
         test_insert_delete_mixed_multiindex_columns
         test_insert_frame, test_insert_int64_loc
         test_insert_with_columns_dups

class TestInsert:  [period/methods/test_insert.py:12]
methods: test_insert

class BaseEngine:  [pandas/io/sql.py:1532]
methods: insert_records

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

    def len(self, text: str) -> int:
        """
        Calculate display width considering unicode East Asian Width
        """
        if not isinstance(text, str):
            return len(text)

        return sum(
            self._EAW_MAP.get(east_asian_width(c), self.ambiguous_width) for c in text
        )

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

    def len(self, text: str) -> int:
        return len(text)

        def timedelta64(*args):
            # see casting notes in NumPy gh-12927
            return np.sum(list(map(np.timedelta64, args, intervals)))

def make_invalid_op(name: str) -> Callable[..., NoReturn]:
    """
    Return a binary method that always raises a TypeError.

    Parameters
    ----------
    name : str

    Returns
    -------
    invalid_op : function
    """

    def invalid_op(self: object, other: object = None) -> NoReturn:
        typ = type(self).__name__
        raise TypeError(f"cannot perform {name} with this index type: {typ}")

    invalid_op.__name__ = name
    return invalid_op

    def __init__(
        self,
        data=None,
        index=None,
        dtype: Dtype | None = None,
        name=None,
        copy: bool | None = None,
    ) -> None:
        allow_mgr = False
        if (
            isinstance(data, SingleBlockManager)
            and index is None
    # ... truncated

    def array(self) -> ExtensionArray:
        """
        The ExtensionArray of the data backing this Series or Index.

        This property provides direct access to the underlying array data of a
        Series or Index without requiring conversion to a NumPy array. It
        returns an ExtensionArray, which is the native storage format for
        pandas extension dtypes.

        Returns
        -------
        ExtensionArray
    # ... truncated

    def tdi(self, monotonic):
        tdi = timedelta_range("1 Day", periods=10)
        if monotonic == "decreasing":
            tdi = tdi[::-1]
        elif monotonic is None:
            taker = np.arange(10, dtype=np.intp)
            np.random.default_rng(2).shuffle(taker)
            tdi = tdi.take(taker)
        return tdi

    def insert_records(
        self,
        table: SQLTable,
        con,
        frame,
        name: str,
        index: bool | str | list[str] | None = True,
        schema=None,
        chunksize: int | None = None,
        method=None,
        **engine_kwargs,
    ) -> int | None:
        """
        Inserts data into already-prepared table
        """
        raise AbstractMethodError(self)

    def groupby(
        self,
        by=None,
        level: IndexLabel | None = None,
        as_index: bool = True,
        sort: bool = True,
        group_keys: bool = True,
        observed: bool = True,
        dropna: bool = True,
    ) -> SeriesGroupBy:
        """
    # ... truncated

    def any(  # type: ignore[override]
        self,
        *,
        axis: Axis = 0,
        bool_only: bool = False,
        skipna: bool = True,
        **kwargs,
    ) -> bool:
        """
    # ... truncated

    def case_when(
        self,
        caselist: list[
            tuple[
                ArrayLike | Callable[[Series], Series | np.ndarray | Sequence[bool]],
                ArrayLike | Scalar | Callable[[Series], Series | np.ndarray],
            ],
        ],
    ) -> Series:
        """
    # ... truncated

    def invalid_op(self: object, other: object = None) -> NoReturn:
        typ = type(self).__name__
        raise TypeError(f"cannot perform {name} with this index type: {typ}")

    def reindex(  # type: ignore[override]
        self,
        index=None,
        *,
        axis: Axis | None = None,
        method: ReindexMethod | None = None,
        copy: bool | lib.NoDefault = lib.no_default,
        level: Level | None = None,
        fill_value: Scalar | None = None,
        limit: int | None = None,
        tolerance=None,
    ) -> Series:
    # ... truncated

def read_csv(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None | lib.NoDefault = lib.no_default,
    delimiter: str | None | lib.NoDefault = None,
    # Column and Index Locations and Names
    header: int | Sequence[int] | None | Literal["infer"] = "infer",
    names: Sequence[Hashable] | None | lib.NoDefault = lib.no_default,
    index_col: IndexLabel | Literal[False] | None = None,
    usecols: UsecolsArgType = None,
    # General Parsing Configuration
    dtype: DtypeArg | None = None,
    # ... truncated

def _insert_quantile_level(idx: Index, qs: npt.NDArray[np.float64]) -> MultiIndex:
    """
    Insert the sequence 'qs' of quantiles as the inner-most level of a MultiIndex.

    The quantile level in the MultiIndex is a repeated copy of 'qs'.

    Parameters
    ----------
    idx : Index
    qs : np.ndarray[float64]

    Returns
    -------
    MultiIndex
    """
    nqs = len(qs)
    lev_codes, lev = Index(qs, copy=False).factorize()
    lev_codes = coerce_indexer_dtype(lev_codes, lev)

    if idx._is_multi:
        idx = cast("MultiIndex", idx)
        levels = [*idx.levels, lev]
        codes = [np.repeat(x, nqs) for x in idx.codes] + [np.tile(lev_codes, len(idx))]
        mi = MultiIndex(levels=levels, codes=codes, names=[*idx.names, None])
    else:
        nidx = len(idx)
        idx_codes = coerce_indexer_dtype(np.arange(nidx), idx)
        levels = [idx, lev]
        codes = [np.repeat(idx_codes, nqs), np.tile(lev_codes, nidx)]
        mi = MultiIndex(levels=levels, codes=codes, names=[idx.name, None])

    return mi

def _reindex_for_setitem(
    value: DataFrame | Series, index: Index
) -> tuple[ArrayLike, BlockValuesRefs | None]:
    # reindex if necessary

    if value.index.equals(index) or not len(index):
        if isinstance(value, Series):
            return value._values, value._references
        return value._values.copy(), None

    # GH#4107
    try:
        reindexed_value = value.reindex(index)._values
    except ValueError as err:
        # raised in MultiIndex.from_tuples, see test_insert_error_msmgs
        if not value.index.is_unique:
            # duplicate axis
            raise err

        raise TypeError(
            "incompatible index of inserted column with frame index"
        ) from err
    return reindexed_value, None

    def all(
        self,
        axis: Axis = 0,
        bool_only: bool = False,
        skipna: bool = True,
        **kwargs,
    ) -> bool:
        """
    # ... truncated

def to_numeric(
    arg,
    errors: DateTimeErrorChoices = "raise",
    downcast: Literal["integer", "signed", "unsigned", "float"] | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,
):
    """
    # ... truncated

    def sort_values(
        self,
        *,
        axis: Axis = 0,
        ascending: bool | Sequence[bool] = True,
        inplace: bool = False,
        kind: SortKind = "quicksort",
        na_position: NaPosition = "last",
        ignore_index: bool = False,
        key: ValueKeyFunc | None = None,
    ) -> Series | None:
        """
    # ... truncated

    def insert_data(self) -> tuple[list[str], list[np.ndarray]]:
        if self.index is not None:
            temp = self.frame.copy(deep=False)
            temp.index.names = self.index
            try:
                temp.reset_index(inplace=True)
            except ValueError as err:
                raise ValueError(f"duplicate name in index/columns: {err}") from err
        else:
            temp = self.frame

        column_names = list(map(str, temp.columns))
    # ... truncated

    def to_latex(
        self,
        buf: FilePath | WriteBuffer[str] | None = None,
        *,
        column_format: str | None = None,
        position: str | None = None,
        position_float: str | None = None,
        hrules: bool | None = None,
        clines: str | None = None,
        label: str | None = None,
        caption: str | tuple | None = None,
        sparse_index: bool | None = None,
    # ... truncated

def invalid_comparison(
    left: ArrayLike,
    right: ArrayLike | list | range | Scalar,
    op: Callable[[Any, Any], bool],
) -> npt.NDArray[np.bool_]:
    """
    If a comparison has mismatched types and is not necessarily meaningful,
    follow python3 conventions by:

        - returning all-False for equality
        - returning all-True for inequality
        - raising TypeError otherwise

    Parameters
    ----------
    left : array-like
    right : scalar, array-like
    op : operator.{eq, ne, lt, le, gt}

    Raises
    ------
    TypeError : on inequality comparisons
    """
    if op is operator.eq:
        res_values = np.zeros(left.shape, dtype=bool)
    elif op is operator.ne:
        res_values = np.ones(left.shape, dtype=bool)
    else:
        typ = type(right).__name__
        raise TypeError(f"Invalid comparison between dtype={left.dtype} and {typ}")
    return res_values

def read_table(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None | lib.NoDefault = lib.no_default,
    delimiter: str | None | lib.NoDefault = None,
    # Column and Index Locations and Names
    header: int | Sequence[int] | None | Literal["infer"] = "infer",
    names: Sequence[Hashable] | None | lib.NoDefault = lib.no_default,
    index_col: IndexLabel | Literal[False] | None = None,
    usecols: UsecolsArgType = None,
    # General Parsing Configuration
    dtype: DtypeArg | None = None,
    # ... truncated

    def reset_index(
        self,
        level: IndexLabel | None = None,
        *,
        drop: bool = False,
        name: Level = lib.no_default,
        inplace: bool = False,
        allow_duplicates: bool = False,
    ) -> DataFrame | Series | None:
        """
    # ... truncated

    def combine(
        self,
        other: Series | Hashable,
        func: Callable[[Hashable, Hashable], Hashable],
        fill_value: Hashable | None = None,
    ) -> Series:
        """
    # ... truncated

    def astype(
        self,
        dtype,
        copy: bool | lib.NoDefault = lib.no_default,
        errors: IgnoreRaise = "raise",
    ) -> Self:
        """
    # ... truncated

    def map(
        self,
        func: Callable | Mapping | Series | None = None,
        na_action: Literal["ignore"] | None = None,
        engine: Callable | None = None,
        **kwargs,
    ) -> Series:
        """
    # ... truncated

    def read(
        self,
        nrows: int | None = None,
        convert_dates: bool | None = None,
        convert_categoricals: bool | None = None,
        index_col: str | None = None,
        convert_missing: bool | None = None,
        preserve_dtypes: bool | None = None,
        columns: Sequence[str] | None = None,
        order_categoricals: bool | None = None,
    ) -> DataFrame:
        """
    # ... truncated

    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

    def dta(self, dta_dti):
        dta, dti = dta_dti
        return dta
```
