# pandas-39 :: tacm

query: BUG: Fixed strange behaviour of pd.DataFrame.drop() with inplace argu… (#30501)

## selected nodes

- rank=1 layer=FILE tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py
- rank=2 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FILE tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/datetime/pd_datetime.h file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/datetime/pd_datetime.h
- rank=4 layer=FILE tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/parser/pd_parser.h file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/parser/pd_parser.h
- rank=5 layer=FILE tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/pd_parser.c file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/pd_parser.c
- rank=6 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=7 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=8 layer=CLASS tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/pd_parser.c::PyModuleDef file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/pd_parser.c
- rank=9 layer=CLASS tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_reset_index.py::TestResetIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_reset_index.py
- rank=10 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/datetime/pd_datetime.h::PandasDateTime_CAPI file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/datetime/pd_datetime.h
- rank=11 layer=CLASS tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/parser/pd_parser.h::PandasParser_CAPI file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/parser/pd_parser.h
- rank=12 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::PeakMemFixedWindowMinMax file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=13 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.reset_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=14 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.drop_duplicates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=15 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.drop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=16 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.drop_duplicates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=17 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=18 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=19 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.set_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=20 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_string file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=21 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=22 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_bool file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=23 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_na file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=24 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=25 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.drop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=26 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.pop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=27 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.reset_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=28 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=29 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::PeakMemFixedWindowMinMax.peakmem_fixed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=30 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=31 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=32 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=33 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=34 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.reorder_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=35 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py::ReplaceList.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py
- rank=36 layer=FUNCTION tokens=340 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.drop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=37 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.num_chunks file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=38 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=39 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.idxmax file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=40 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.idxmin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=41 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::write_legacy_hdf file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=42 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.num_rows file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=43 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dropna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=44 layer=FUNCTION tokens=229 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.items file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=45 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::list_of_str file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py
- rank=46 layer=FUNCTION tokens=5 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py::m file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py

## context

```text
file asv_bench/benchmarks/ctors.py
imports: numpy, pandas
defines: SeriesConstructors, SeriesDtypesConstructors, MultiIndexConstructor, DatetimeIndexConstructor, no_change, list_of_str, gen_of_str, arr_dict, list_of_tuples, gen_of_tuples, list_of_lists, list_of_tuples_with_none, list_of_lists_with_none

file pandas/core/frame.py
imports: __future__, collections, functools, io, itertools, operator, sys, typing
defines: DataFrame, _from_nested_dict, _reindex_for_setitem

file pandas/datetime/pd_datetime.h
imports: pandas, numpy
defines: PandasDateTime_CAPI

file pandas/parser/pd_parser.h
imports: Python, pandas
defines: PandasParser_CAPI

file parser/pd_parser.c
imports: pandas
defines: PyModuleDef, to_double, floatify, pandas_parser_destructor, pandas_parser_exec, PyInit_pandas_parser

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

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class PyModuleDef  [parser/pd_parser.c:168]
methods: —

class TestResetIndex:  [series/methods/test_reset_index.py:19]
methods: test_reset_index, test_reset_index_drop_errors
         test_reset_index_drop_infer_string
         test_reset_index_dti_round_trip
         test_reset_index_inplace_and_drop_ignore_name
         test_reset_index_level, test_reset_index_name
         test_reset_index_range, test_reset_index_with_drop

class PandasDateTime_CAPI  [pandas/datetime/pd_datetime.h:33]
methods: —

class PandasParser_CAPI  [pandas/parser/pd_parser.h:20]
methods: —

class PeakMemFixedWindowMinMax:  [asv_bench/benchmarks/rolling.py:262]
methods: peakmem_fixed, setup

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

    def drop_duplicates(
        self,
        *,
        keep: DropKeep = "first",
        inplace: bool = False,
        ignore_index: bool = False,
    ) -> Series | None:
        """
    # ... truncated

    def drop(
        self,
        labels: IndexLabel | ListLike = None,
        *,
        axis: Axis = 0,
        index: IndexLabel | ListLike = None,
        columns: IndexLabel | ListLike = None,
        level: Level | None = None,
        inplace: bool = False,
        errors: IgnoreRaise = "raise",
    ) -> Series | None:
        """
    # ... truncated

    def drop_duplicates(
        self,
        subset: Hashable | Iterable[Hashable] | None = None,
        *,
        keep: DropKeep = "first",
        inplace: bool = False,
        ignore_index: bool = False,
    ) -> DataFrame | None:
        """
    # ... truncated

    def time_frame_drop_dups(self, inplace):
        self.df.drop_duplicates(["key1", "key2"], inplace=inplace)

    def time_series_drop_dups_int(self, inplace):
        self.s.drop_duplicates(inplace=inplace)

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

    def time_series_drop_dups_string(self, inplace):
        self.s_str.drop_duplicates(inplace=inplace)

    def time_frame_drop_dups_int(self, inplace):
        self.df_int.drop_duplicates(inplace=inplace)

    def time_frame_drop_dups_bool(self, inplace):
        self.df_bool.drop_duplicates(inplace=inplace)

    def time_frame_drop_dups_na(self, inplace):
        self.df_nan.drop_duplicates(["key1", "key2"], inplace=inplace)

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

    def drop(
        self,
        labels: IndexLabel | ListLike = None,
        *,
        axis: Axis = 0,
        index: IndexLabel | ListLike = None,
        columns: IndexLabel | ListLike = None,
        level: Level | None = None,
        inplace: bool = False,
        errors: IgnoreRaise = "raise",
    ) -> DataFrame | None:
        """
    # ... truncated

    def pop(self, item: Hashable) -> Any:
        """
        Return item and drops from series. Raise KeyError if not found.

        The Series is modified in place, and the value corresponding to the
        given label is removed and returned.

        Parameters
        ----------
        item : label
            Index of the element that needs to be removed.

        Returns
        -------
        scalar
            Value that is popped from series.

        See Also
        --------
        Series.drop: Drop specified values from Series.
        Series.drop_duplicates: Return Series with duplicate values removed.

        Examples
        --------
        >>> ser = pd.Series([1, 2, 3])

        >>> ser.pop(0)
        1

        >>> ser
        1    2
        2    3
        dtype: int64
        """
        return maybe_unbox_numpy_scalar(super().pop(item=item))

    def reset_index(
        self,
        level: IndexLabel | None = None,
        *,
        drop: bool = False,
        inplace: bool = False,
        col_level: Hashable = 0,
        col_fill: Hashable = "",
        allow_duplicates: bool | lib.NoDefault = lib.no_default,
        names: Hashable | Sequence[Hashable] | None = None,
    ) -> DataFrame | None:
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

    def peakmem_fixed(self, operation):
        for x in range(5):
            getattr(self.roll, operation)()

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

    def dtypes(self) -> DtypeObj:
        """
        Return the dtype object of the underlying data.

        Unlike ``DataFrame.dtypes``, which returns a Series of dtypes for each
        column, ``Series.dtypes`` returns a single dtype object representing
        the type of all elements in the Series.

        See Also
        --------
        DataFrame.dtypes :  Return the dtypes in the DataFrame.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> s.dtypes
        dtype('int64')
        """
        # DataFrame compatibility
        return self.dtype

    def _set_with_engine(self, key, value) -> None:
        loc = self.index.get_loc(key)

        # this is equivalent to self._values[key] = value
        self._mgr.setitem_inplace(loc, value)

    def dtype(self) -> DtypeObj:
        """
        Return the dtype object of the underlying data.

        This is the dtype of the array backing the Series (or the single dtype
        for a DataFrame column). For extension types, it returns the
        corresponding extension dtype.

        See Also
        --------
        Series.dtypes : Return the dtype object of the underlying data.
        Series.astype : Cast a pandas object to a specified dtype dtype.
        Series.convert_dtypes : Convert columns to the best possible dtypes using dtypes
            supporting pd.NA.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> s.dtype
        dtype('int64')
        """
        return self._mgr.dtype

    def reorder_levels(self, order: Sequence[Level]) -> Series:
        """
        Rearrange index levels using input order.

        May not drop or duplicate levels.

        Parameters
        ----------
        order : list of int representing new level order
            Reference level by number or key.

        Returns
    # ... truncated

    def setup(self, inplace):
        self.df = pd.DataFrame({"A": 0, "B": 0}, index=range(10**7))

    def drop(
        self,
        labels: IndexLabel | ListLike = None,
        *,
        axis: Axis = 0,
        index: IndexLabel | ListLike = None,
        columns: IndexLabel | ListLike = None,
        level: Level | None = None,
        inplace: bool = False,
        errors: IgnoreRaise = "raise",
    ) -> Self | None:
        inplace = validate_bool_kwarg(inplace, "inplace")

        if labels is not None:
            if index is not None or columns is not None:
                raise ValueError("Cannot specify both 'labels' and 'index'/'columns'")
            axis_name = self._get_axis_name(axis)
            axes = {axis_name: labels}
        elif index is not None or columns is not None:
            if axis == 1:
                raise ValueError("Cannot specify both 'axis' and 'index'/'columns'")
            axes = {"index": index}
            if self.ndim == 2:
                axes["columns"] = columns
        else:
            raise ValueError(
                "Need to specify at least one of 'labels', 'index' or 'columns'"
            )

        obj = self

        for axis, labels in axes.items():
            if labels is not None:
                obj = obj._drop_axis(labels, axis, level=level, errors=errors)

        if inplace:
            self._update_inplace(obj)
            return None
        else:
            return obj

    def num_chunks(self) -> int:
        """
        Return the number of chunks the DataFrame consists of.
        """

    def count(self) -> int:
        """
        Return number of non-NA/null observations in the Series.

        This method counts the number of elements that are not missing
        (i.e., not NaN or None) in the Series.

        Returns
        -------
        int
            Number of non-null values in the Series.

        See Also
        --------
        DataFrame.count : Count non-NA cells for each column or row.

        Examples
        --------
        >>> s = pd.Series([0.0, 1.0, np.nan])
        >>> s.count()
        2
        """
        return maybe_unbox_numpy_scalar(notna(self._values).sum().astype("int64"))

    def idxmax(self, axis: Axis = 0, skipna: bool = True, *args, **kwargs) -> Hashable:
        """
        Return the row label of the maximum value.

        If multiple values equal the maximum, the first row label with that
        value is returned.

        Parameters
        ----------
        axis : {0 or 'index'}
            Unused. Parameter needed for compatibility with DataFrame.
        skipna : bool, default True
    # ... truncated

    def idxmin(self, axis: Axis = 0, skipna: bool = True, *args, **kwargs) -> Hashable:
        """
        Return the row label of the minimum value.

        If multiple values equal the minimum, the first row label with that
        value is returned.

        Parameters
        ----------
        axis : {0 or 'index'}
            Unused. Parameter needed for compatibility with DataFrame.
        skipna : bool, default True
    # ... truncated

def write_legacy_hdf(output_dir, format):
    import tables

    pth = f"{platform_name()}_pytables-{tables.__version__}_{format}.h5"

    df = create_dataframe_all_types()
    if format == "fixed":
        # df = df.drop(columns=["categorical", "categorical_object", "categorical_int"])
        df = df.drop(columns=["categorical_int"])
    complevel = 9 if format == "table" else None
    df.to_hdf(
        os.path.join(output_dir, pth),
        key="df_alltypes",
        format=format,
        complevel=complevel,
    )

    print(f"created hdf file: {pth}")

    def num_rows(self) -> int | None:
        # TODO: not happy with Optional, but need to flag it may be expensive
        #       why include it if it may be None - what do we expect consumers
        #       to do here?
        """
        Return the number of rows in the DataFrame, if available.
        """

    def dropna(
        self,
        *,
        axis: Axis = 0,
        inplace: bool = False,
        how: AnyAll | None = None,
        ignore_index: bool = False,
    ) -> Series | None:
        """
    # ... truncated

    def items(self) -> Iterable[tuple[Hashable, Any]]:
        """
        Lazily iterate over (index, value) tuples.

        This method returns an iterable tuple (index, value). This is
        convenient if you want to create a lazy iterator.

        Returns
        -------
        iterable
            Iterable of tuples containing the (index, value) pairs from a
            Series.

        See Also
        --------
        DataFrame.items : Iterate over (column name, Series) pairs.
        DataFrame.iterrows : Iterate over DataFrame rows as (index, Series) pairs.

        Examples
        --------
        >>> s = pd.Series(["A", "B", "C"])
        >>> for index, value in s.items():
        ...     print(f"Index : {index}, Value : {value}")
        Index : 0, Value : A
        Index : 1, Value : B
        Index : 2, Value : C
        """
        return zip(iter(self.index), iter(self), strict=True)

def list_of_str(arr):
    return list(arr.astype(str))

def m():
    return 5
```
