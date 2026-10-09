# pandas-73 :: tacm-dyn

query: BUG: DataFrame.floordiv(ser, axis=0) not matching column-wise bheavior (#31271)

## selected nodes

- rank=1 layer=FILE tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=2 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=3 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FUNCTION tokens=287 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.nunique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=6 layer=CLASS tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::TestDivisionByZero file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py
- rank=7 layer=FUNCTION tokens=228 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._replace_columnwise file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=8 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=9 layer=FILE tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=10 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=11 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.transform file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=12 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.get_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=13 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.ne file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=14 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser._convert_axes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py
- rank=15 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.column_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=16 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=17 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__add__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=18 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.swaplevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=19 layer=FUNCTION tokens=299 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py::_from_dataframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=20 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_sanitize_mixed_ndim file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=21 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::StructAccessor.explode file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=22 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=23 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.reorder_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=24 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=25 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py::string_column_to_ndarray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=26 layer=FUNCTION tokens=11 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/aggregate/test_aggregate.py::aggfun_1 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/aggregate/test_aggregate.py

## context

```text
file core/interchange/from_dataframe.py
imports: __future__, ctypes, re, typing, warnings, numpy, pandas
defines: from_dataframe, _from_dataframe, protocol_df_chunk_to_pandas, primitive_column_to_ndarray, categorical_column_to_series, string_column_to_ndarray, parse_datetime_format_str, datetime_column_to_ndarray, buffer_to_ndarray, set_nulls, set_nulls, set_nulls, set_nulls

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

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

    def floordiv(
        self, other, axis: Axis = "columns", level=None, fill_value=None
    ) -> DataFrame:
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

file core/interchange/dataframe_protocol.py
imports: __future__, abc, enum, typing, pandas, collections
defines: DlpackDeviceType, DtypeKind, ColumnNullType, ColumnBuffers, CategoricalDescription, Buffer, Column, DataFrame

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

    def transform(
        self, func: AggFuncType, axis: Axis = 0, *args, **kwargs
    ) -> DataFrame | Series:
        """
    # ... truncated

    def get_column(self, i: int) -> Column:
        """
        Return the column at the indicated position.
        """

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

    def _convert_axes(self, obj: DataFrame | Series) -> DataFrame | Series:
        """
        Try to convert axes.
        """
        for axis_name in obj._AXIS_ORDERS:
            ax = obj._get_axis(axis_name)
            ser = Series(ax, dtype=ax.dtype, copy=False)
            new_ser, result = self._try_convert_data(
                name=axis_name,
                data=ser,
                use_dtypes=False,
                convert_dates=True,
                is_axis=True,
            )
            if result:
                new_axis = Index(new_ser, dtype=new_ser.dtype, copy=False)
                setattr(obj, axis_name, new_axis)
        return obj

    def column_names(self) -> Iterable[str]:
        """
        Return an iterator yielding the column names.
        """

    def aggregate(
        self, func=None, axis: Axis = 0, *args, **kwargs
    ) -> DataFrame | Series:
        """
    # ... truncated

    def __add__(self, other):
        """
        Get Addition of DataFrame and other, column-wise.

        Equivalent to ``DataFrame.add(other)``.

        Parameters
        ----------
        other : scalar, sequence, Series, dict or DataFrame
            Object to be added to the DataFrame.

        Returns
    # ... truncated

    def swaplevel(self, i: Axis = -2, j: Axis = -1, axis: Axis = 0) -> DataFrame:
        """
        Swap levels i and j in a :class:`MultiIndex`.

        Default is to swap the two innermost levels of the index.

        Parameters
        ----------
        i, j : int or str
            Levels of the indices to be swapped. Can pass level name as string.
        axis : {0 or 'index', 1 or 'columns'}, default 0
                    The axis to swap levels on. 0 or 'index' for row-wise, 1 or
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

def _sanitize_mixed_ndim(
    objs: list[Series | DataFrame],
    sample: Series | DataFrame,
    ignore_index: bool,
    axis: AxisInt,
) -> list[Series | DataFrame]:
    # if we have mixed ndims, then convert to highest ndim
    # creating column numbers as needed

    new_objs = []

    current_column = 0
    # ... truncated

    def explode(self) -> DataFrame:
        """
        Extract all child fields of a struct as a DataFrame.

        Each child field of the struct becomes a column in the resulting
        DataFrame, with column names matching the struct field names.

        Returns
        -------
        pandas.DataFrame
            The data corresponding to all child fields.

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

    def reorder_levels(self, order: Sequence[int | str], axis: Axis = 0) -> DataFrame:
        """
        Rearrange index or column levels using input ``order``.

        May not drop or duplicate levels.

        Parameters
        ----------
        order : list of int or list of str
            List representing new level order. Reference level by number
            (position) or by key (label).
        axis : {0 or 'index', 1 or 'columns'}, default 0
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

def string_column_to_ndarray(col: Column) -> tuple[np.ndarray, Any]:
    """
    Convert a column holding string data to a NumPy array.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of np.ndarray holding the data and the memory owner object
    # ... truncated

    def aggfun_1(ser):
        return ser.size
```
