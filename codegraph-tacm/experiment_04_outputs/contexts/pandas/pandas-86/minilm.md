# pandas-86 :: minilm

query: BUG: correct wrong error message in df.pivot when columns=None (#30925)

## selected nodes

- rank=1 layer=FUNCTION tokens=1106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::__internal_pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=2 layer=FUNCTION tokens=1825 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::pivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=3 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=4 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=5 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical_observed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=6 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins_only_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=7 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=8 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_agg file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=9 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Pivot.time_reshape_pivot_time_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=10 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py::HTMLFormatter.row_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py
- rank=11 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py
- rank=12 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::df_col file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py
- rank=13 layer=FUNCTION tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::__internal_pivot_table [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py]
def __internal_pivot_table(
    data: DataFrame,
    values,
    index,
    columns,
    aggfunc: AggFuncTypeBase | AggFuncTypeDict,
    fill_value,
    margins: bool,
    dropna: bool,
    margins_name: Hashable,
    observed: bool,
    sort: bool,
    kwargs,
) -> DataFrame:
    """
    Helper of :func:`pandas.pivot_table` for any non-list ``aggfunc``.
    """
    keys = index + columns

    values_passed = values is not None
    if values_passed:
        if is_list_like(values):
            values_multi = True
            values = list(values)
        else:
            values_multi = False
            values = [values]

        # GH14938 Make sure value labels are in data
        for i in values:
            if i not in data:
                raise KeyError(i)

        to_filter = []
        for x in keys + values:
            if isinstance(x, Grouper):
                x = x.key
            try:
                if x in data:
                    to_filter.append(x)
            except TypeError:
                pass
        if len(to_filter) < len(data.columns):
            data = data[to_filter]

    else:
        values = data.columns
        for key in keys:
            try:
                values = values.drop(key)
            except (TypeError, ValueError, KeyError):
                pass
        values = list(values)

    grouped: SeriesGroupBy | DataFrameGroupBy = data.groupby(
        keys, observed=observed, sort=sort, dropna=dropna
    )
    if values_passed:
        # GH#57876 and GH#61292
        grouped = grouped[values]
    elif grouped._obj_with_exclusions.columns.empty:
        grouped = Series(np.nan, index=data.index).groupby(
            [data[key] for key in keys], observed=observed, sort=sort, dropna=dropna
        )

    agged = grouped.agg(aggfunc, **kwargs)

    if dropna and isinstance(agged, ABCDataFrame) and len(agged.columns):
        agged = agged.dropna(how="all")

    table = agged

    # GH17038, this check should only happen if index is defined (not None)
    if table.index.nlevels > 1 and index:
        # Related GH #17123
        # If index_names are integers, determine whether the integers refer
        # to the level position or name.
        index_names = agged.index.names[: len(index)]
        to_unstack = []
        for i in range(len(index), len(keys)):
            name = agged.index.names[i]
            if name is None or name in index_names:
                to_unstack.append(i)
            else:
                to_unstack.append(name)
        table = agged.unstack(to_unstack, fill_value=fill_value)

    if not dropna:
        if isinstance(table.index, MultiIndex):
            m = MultiIndex.from_product(table.index.levels, names=table.index.names)
            table = table.reindex(m, axis=0, fill_value=fill_value)

        if isinstance(table.columns, MultiIndex):
            m = MultiIndex.from_product(table.columns.levels, names=table.columns.names)
            table = table.reindex(m, axis=1, fill_value=fill_value)

    if sort is True and isinstance(table, ABCDataFrame):
        table = table.sort_index(axis=1)

    if fill_value is not None:
        table = table.fillna(fill_value)
        if aggfunc is len and not observed and lib.is_integer(fill_value):
            # TODO: can we avoid this?  this used to be handled by
            #  downcast="infer" in fillna
            table = table.astype(np.int64)

    if margins:
        if dropna:
            data = data[data.notna().all(axis=1)]
        table = _add_margins(
            table,
            data,
            values,
            rows=index,
            cols=columns,
            aggfunc=aggfunc,
            kwargs=kwargs,
            observed=dropna,
            margins_name=margins_name,
            fill_value=fill_value,
            dropna=dropna,
        )

    # discard the top level
    if values_passed and not values_multi and table.columns.nlevels > 1:
        table.columns = table.columns.droplevel(0)
    if len(index) == 0 and len(columns) > 0:
        table = table.T

    # GH 15193 Make sure empty columns are removed if dropna=True
    if isinstance(table, ABCDataFrame) and dropna:
        table = table.dropna(how="all", axis=1)

    return cast("DataFrame", table)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::pivot [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py]
def pivot(
    data: DataFrame,
    *,
    columns: IndexLabel,
    index: IndexLabel | lib.NoDefault = lib.no_default,
    values: IndexLabel | lib.NoDefault = lib.no_default,
) -> DataFrame:
    """
    Return reshaped DataFrame organized by given index / column values.

    Reshape data (produce a "pivot" table) based on column values. Uses
    unique values from specified `index` / `columns` to form axes of the
    resulting DataFrame. This function does not support data
    aggregation, multiple values will result in a MultiIndex in the
    columns. See the :ref:`User Guide <reshaping>` for more on reshaping.

    Parameters
    ----------
    data : DataFrame
        Input pandas DataFrame object.
    columns : Hashable or a sequence of the previous
        Column to use to make new frame's columns.
    index : Hashable or a sequence of the previous, optional
        Column to use to make new frame's index. If not given, uses existing index.
    values : Hashable or a sequence of the previous, optional
        Column(s) to use for populating new frame's values. If not
        specified, all remaining columns will be used and the result will
        have hierarchically indexed columns.

    Returns
    -------
    DataFrame
        Returns reshaped DataFrame.

    Raises
    ------
    ValueError:
        When there are any `index`, `columns` combinations with multiple
        values. `DataFrame.pivot_table` when you need to aggregate.

    See Also
    --------
    DataFrame.pivot_table : Generalization of pivot that can handle
        duplicate values for one index/column pair.
    DataFrame.unstack : Pivot based on the index values instead of a
        column.
    wide_to_long : Wide panel to long format. Less flexible but more
        user-friendly than melt.

    Notes
    -----
    For finer-tuned control, see hierarchical indexing documentation along
    with the related stack/unstack methods.

    Reference :ref:`the user guide <reshaping.pivot>` for more examples.

    Examples
    --------
    >>> df = pd.DataFrame(
    ...     {
    ...         "foo": ["one", "one", "one", "two", "two", "two"],
    ...         "bar": ["A", "B", "C", "A", "B", "C"],
    ...         "baz": [1, 2, 3, 4, 5, 6],
    ...         "zoo": ["x", "y", "z", "q", "w", "t"],
    ...     }
    ... )
    >>> df
        foo   bar  baz  zoo
    0   one   A    1    x
    1   one   B    2    y
    2   one   C    3    z
    3   two   A    4    q
    4   two   B    5    w
    5   two   C    6    t

    >>> df.pivot(index="foo", columns="bar", values="baz")
    bar  A   B   C
    foo
    one  1   2   3
    two  4   5   6

    >>> df.pivot(index="foo", columns="bar")["baz"]
    bar  A   B   C
    foo
    one  1   2   3
    two  4   5   6

    >>> df.pivot(index="foo", columns="bar", values=["baz", "zoo"])
          baz       zoo
    bar   A  B  C   A  B  C
    foo
    one   1  2  3   x  y  z
    two   4  5  6   q  w  t

    You could also assign a list of column names or a list of index names.

    >>> df = pd.DataFrame(
    ...     {
    ...         "lev1": [1, 1, 1, 2, 2, 2],
    ...         "lev2": [1, 1, 2, 1, 1, 2],
    ...         "lev3": [1, 2, 1, 2, 1, 2],
    ...         "lev4": [1, 2, 3, 4, 5, 6],
    ...         "values": [0, 1, 2, 3, 4, 5],
    ...     }
    ... )
    >>> df
        lev1 lev2 lev3 lev4 values
    0   1    1    1    1    0
    1   1    1    2    2    1
    2   1    2    1    3    2
    3   2    1    2    4    3
    4   2    1    1    5    4
    5   2    2    2    6    5

    >>> df.pivot(index="lev1", columns=["lev2", "lev3"], values="values")
    lev2    1         2
    lev3    1    2    1    2
    lev1
    1     0.0  1.0  2.0  NaN
    2     4.0  3.0  NaN  5.0

    >>> df.pivot(index=["lev1", "lev2"], columns=["lev3"], values="values")
          lev3    1    2
    lev1  lev2
       1     1  0.0  1.0
             2  2.0  NaN
       2     1  4.0  3.0
             2  NaN  5.0

    A ValueError is raised if there are any duplicates.

    >>> df = pd.DataFrame(
    ...     {
    ...         "foo": ["one", "one", "two", "two"],
    ...         "bar": ["A", "A", "B", "C"],
    ...         "baz": [1, 2, 3, 4],
    ...     }
    ... )
    >>> df
       foo bar  baz
    0  one   A    1
    1  one   A    2
    2  two   B    3
    3  two   C    4

    Notice that the first two rows are the same for our `index`
    and `columns` arguments.

    >>> df.pivot(index="foo", columns="bar", values="baz")
    Traceback (most recent call last):
       ...
    ValueError: Index contains duplicate entries, cannot reshape
    """
    columns_listlike = com.convert_to_list_like(columns)

    # If columns is None we will create a MultiIndex level with None as name
    # which might cause duplicated names because None is the default for
    # level names
    if any(name is None for name in data.index.names):
        data = data.copy(deep=False)
        data.index.names = [
            name if name is not None else lib.no_default for name in data.index.names
        ]

    indexed: DataFrame | Series
    if values is lib.no_default:
        if index is not lib.no_default:
            cols = com.convert_to_list_like(index)
        else:
            cols = []

        append = index is lib.no_default
        # error: Unsupported operand types for + ("List[Any]" and "ExtensionArray")
        # error: Unsupported left operand type for + ("ExtensionArray")
        indexed = data.set_index(
            cols + columns_listlike,  # type: ignore[operator]
            append=append,
        )
    else:
        index_list: list[Index] | list[Series]
        if index is lib.no_default:
            if isinstance(data.index, MultiIndex):
                # GH 23955
                index_list = [
                    data.index.get_level_values(i) for i in range(data.index.nlevels)
                ]
            else:
                index_list = [
                    data._constructor_sliced(data.index, name=data.index.name)
                ]
        else:
            index_list = [data[idx] for idx in com.convert_to_list_like(index)]

        data_columns = [data[col] for col in columns_listlike]
        index_list.extend(data_columns)
        multiindex = MultiIndex.from_arrays(index_list)

        if is_list_like(values) and not isinstance(values, tuple):
            # Exclude tuple because it is seen as a single column name
            indexed = data._constructor(
                data[values]._values,
                index=multiindex,
                columns=cast("SequenceNotStr", values),
            )
        else:
            indexed = data._constructor_sliced(data[values]._values, index=multiindex)
    # error: Argument 1 to "unstack" of "DataFrame" has incompatible type "Union
    # [List[Any], ExtensionArray, ndarray[Any, Any], Index, Series]"; expected
    # "Hashable"
    # unstack with a MultiIndex returns a DataFrame
    result = cast("DataFrame", indexed.unstack(columns_listlike))  # type: ignore[arg-type]
    result.index.names = [
        name if name is not lib.no_default else None for name in result.index.names
    ]

    return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table(self):
        self.df.pivot_table(index="key1", columns=["key2", "key3"])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_categorical(self):
        self.df2.pivot_table(
            index="col1", values="col3", columns="col2", aggfunc="sum", fill_value=0
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical_observed [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_categorical_observed(self):
        self.df2.pivot_table(
            index="col1",
            values="col3",
            columns="col2",
            aggfunc="sum",
            fill_value=0,
            observed=True,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins_only_column [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_margins_only_column(self):
        self.df.pivot_table(columns=["key1", "key2", "key3"], margins=True)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_margins(self):
        self.df.pivot_table(index="key1", columns=["key2", "key3"], margins=True)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_agg [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_agg(self):
        self.df.pivot_table(
            index="key1", columns=["key2", "key3"], aggfunc=["sum", "mean"]
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Pivot.time_reshape_pivot_time_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_reshape_pivot_time_series(self):
        self.df.pivot(index="date", columns="variable", values="value")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py::HTMLFormatter.row_levels [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py]
    def row_levels(self) -> int:
        if self.fmt.index:
            # showing (row) index
            return self.frame.index.nlevels
        elif self.show_col_idx_names:
            # see gh-22579
            # Column misalignment also occurs for
            # a standard index when the columns index is named.
            # If the row index is not displayed a column of
            # blank cells need to be included before the DataFrame values.
            return 1
        # not showing (row) index
        return 0

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py::df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py]
def df(vals, cols):
    return DataFrame(vals, columns=cols)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::df_col [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py]
def df_col(df):
    return df.reset_index()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::func [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py]
    def func(df: DataFrame) -> Series:
        if col_name not in df.columns:
            columns_str = str(df.columns.tolist())
            max_len = 90
            if len(columns_str) > max_len:
                columns_str = columns_str[:max_len] + "...]"

            msg = (
                f"Column '{col_name}' not found in given DataFrame.\n\n"
                f"Hint: did you mean one of {columns_str} instead?"
            )
            raise ValueError(msg)
        return df[col_name]
```
