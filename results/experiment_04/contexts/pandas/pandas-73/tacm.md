# pandas-73 :: tacm

query: BUG: DataFrame.floordiv(ser, axis=0) not matching column-wise bheavior (#31271)

## selected nodes

- rank=1 layer=FILE tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=2 layer=FILE tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=3 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=5 layer=CLASS tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::TestDivisionByZero file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py
- rank=6 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=7 layer=CLASS tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas7bdat.py::_Column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas7bdat.py
- rank=8 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=9 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=10 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.transform file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=11 layer=FUNCTION tokens=287 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.nunique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=12 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=13 layer=FUNCTION tokens=228 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._replace_columnwise file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=14 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.ne file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=15 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.add file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=16 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.truediv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=17 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.get_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=18 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.rmul file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=19 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.rmod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=20 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.mod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=21 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.pow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=22 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.rfloordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=23 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.rtruediv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=24 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.rpow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=25 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.divmod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=26 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.column_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=27 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.rdivmod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=28 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.le file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=29 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.ge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=30 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.get_column_by_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=31 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.any file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=32 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._flex_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=33 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.all file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=34 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.ne file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=35 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.max file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=36 layer=FUNCTION tokens=6 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::at file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
file core/interchange/from_dataframe.py
imports: __future__, ctypes, re, typing, warnings, numpy, pandas
defines: from_dataframe, _from_dataframe, protocol_df_chunk_to_pandas, primitive_column_to_ndarray, categorical_column_to_series, string_column_to_ndarray, parse_datetime_format_str, datetime_column_to_ndarray, buffer_to_ndarray, set_nulls, set_nulls, set_nulls, set_nulls

file core/interchange/dataframe_protocol.py
imports: __future__, abc, enum, typing, pandas, collections
defines: DlpackDeviceType, DtypeKind, ColumnNullType, ColumnBuffers, CategoricalDescription, Buffer, Column, DataFrame

file pandas/core/frame.py
imports: __future__, collections, functools, io, itertools, operator, sys, typing
defines: DataFrame, _from_nested_dict, _reindex_for_setitem

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class TestDivisionByZero:  [tests/arithmetic/test_numeric.py:382]
methods: test_df_div_zero_array, test_df_div_zero_df
         test_df_div_zero_int
         test_df_div_zero_series_does_not_commute
         test_df_mod_zero_array, test_df_mod_zero_df
         test_df_mod_zero_int
         test_df_mod_zero_series_does_not_commute
         test_div_negative_zero, test_div_zero
         test_div_zero_inf_signs, test_divmod_zero
         test_floordiv_div, test_floordiv_zero
         test_mod_zero, test_rdiv_zero
         test_rdiv_zero_compat, test_ser_div_ser
         test_ser_divmod_inf, test_ser_divmod_zero

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

class _Column:  [io/sas/sas7bdat.py:121]
methods: __init__

    def floordiv(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Integer division of series and other, \
        element-wise (binary operator `floordiv`).

        Equivalent to ``series // other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def floordiv(
        self, other, axis: Axis = "columns", level=None, fill_value=None
    ) -> DataFrame:
        """
    # ... truncated

    def transform(
        self, func: AggFuncType, axis: Axis = 0, *args, **kwargs
    ) -> DataFrame | Series:
        """
    # ... truncated

    def nunique(self, axis: Axis = 0, dropna: bool = True) -> Series:
        """
        Count number of distinct elements in specified axis.

        Return Series with number of distinct elements. Can ignore NaN
        values.

        Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns'}, default 0
            The axis to use. 0 or 'index' for row-wise, 1 or 'columns' for
            column-wise.
        dropna : bool, default True
            Don't include NaN in the counts.

        Returns
        -------
        Series
            Series with counts of unique values per row or column, depending on `axis`.

        See Also
        --------
        Series.nunique: Method nunique for Series.
        DataFrame.count: Count non-NA cells for each column or row.

        Examples
        --------
        >>> df = pd.DataFrame({"A": [4, 5, 6], "B": [4, 1, 1]})
        >>> df.nunique()
        A    3
        B    2
        dtype: int64

        >>> df.nunique(axis=1)
        0    1
        1    2
        2    2
        dtype: int64
        """
        return self.apply(Series.nunique, axis=axis, dropna=dropna)

    def aggregate(
        self, func=None, axis: Axis = 0, *args, **kwargs
    ) -> DataFrame | Series:
        """
    # ... truncated

    def _replace_columnwise(
        self, mapping: dict[Hashable, tuple[Any, Any]], inplace: bool, regex
    ) -> Self:
        """
        Dispatch to Series.replace column-wise.

        Parameters
        ----------
        mapping : dict
            of the form {col: (target, value)}
        inplace : bool
        regex : bool or same types as `to_replace` in DataFrame.replace

        Returns
        -------
        DataFrame
        """
        # Operate column-wise
        res = self if inplace else self.copy(deep=False)
        ax = self.columns

        for i, ax_value in enumerate(ax):
            if ax_value in mapping:
                ser = self.iloc[:, i]

                target, value = mapping[ax_value]
                newobj = ser.replace(target, value, regex=regex)

                res._iset_item(i, newobj, inplace=inplace)

        return res if inplace else res.__finalize__(self)

    def ne(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Not equal to of series and other, element-wise (binary operator `ne`).

        Equivalent to ``series != other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
            will behave the same as ``!=`` but with possibly different results due
    # ... truncated

    def add(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Addition of series and other, element-wise (binary operator `add`).

        Equivalent to ``series + other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : Series or scalar value
            With which to compute the addition.
        level : int or name
    # ... truncated

    def truediv(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Floating division of series and other, \
        element-wise (binary operator `truediv`).

        Equivalent to ``series / other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : Series or scalar value
            Series with which to compute division.
    # ... truncated

    def get_column(self, i: int) -> Column:
        """
        Return the column at the indicated position.
        """

    def rmul(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Multiplication of series and other, \
        element-wise (binary operator `rmul`).

        Equivalent to ``other * series``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def rmod(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Modulo of series and other, \
        element-wise (binary operator `rmod`).

        Equivalent to ``other % series``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def mod(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Modulo of series and other, element-wise (binary operator `mod`).

        Equivalent to ``series % other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : Series or scalar value
            Series with which to compute modulo.
        level : int or name
    # ... truncated

    def pow(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Exponential power of series and other, \
        element-wise (binary operator `pow`).

        Equivalent to ``series ** other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def rfloordiv(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Integer division of series and other, \
        element-wise (binary operator `rfloordiv`).

        Equivalent to ``other // series``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def rtruediv(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Floating division of series and other, \
        element-wise (binary operator `rtruediv`).

        Equivalent to ``other / series``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def rpow(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Exponential power of series and other, \
        element-wise (binary operator `rpow`).

        Equivalent to ``other ** series``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def divmod(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Integer division and modulo of series and other, \
        element-wise (binary operator `divmod`).

        Equivalent to ``divmod(series, other)``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def column_names(self) -> Iterable[str]:
        """
        Return an iterator yielding the column names.
        """

    def rdivmod(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Integer division and modulo of series and other, \
        element-wise (binary operator `rdivmod`).

        Equivalent to ``other divmod series``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def le(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Less than or equal to of series and other, \
        element-wise (binary operator `le`).

        Equivalent to ``series <= other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def ge(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Greater than or equal to of series and other, \
        element-wise (binary operator `ge`).

        Equivalent to ``series >= other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
    # ... truncated

    def get_column_by_name(self, name: str) -> Column:
        """
        Return the column whose name is the indicated name.
        """

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

    def _flex_method(
        self, other, op, *, level=None, fill_value=None, axis: Axis = 0
    ) -> Series:
        if axis is not None:
            self._get_axis_number(axis)

        res_name = ops.get_op_result_name(self, other)

        if isinstance(other, Series):
            return self._binop(other, op, level=level, fill_value=fill_value)
        elif (isinstance(other, np.ndarray) and other.ndim > 0) or isinstance(
            other, (list, tuple, ExtensionArray)
    # ... truncated

    def all(
        self,
        axis: Axis = 0,
        bool_only: bool = False,
        skipna: bool = True,
        **kwargs,
    ) -> bool:
        """
    # ... truncated

    def ne(self, other, axis: Axis = "columns", level=None) -> DataFrame:
        """
        Get Not equal to of dataframe and other, element-wise (binary operator `ne`).

        Among flexible wrappers (`eq`, `ne`, `le`, `lt`, `ge`, `gt`) to comparison
        operators.

        Equivalent to `==`, `!=`, `<=`, `<`, `>=`, `>` with support to choose axis
        (rows or columns) and level for comparison.

        Parameters
        ----------
    # ... truncated

    def max(
        self,
        axis: Axis | None = 0,
        skipna: bool = True,
        numeric_only: bool = False,
        **kwargs,
    ):
        """
    # ... truncated

def at(x):
    return x.at
```
