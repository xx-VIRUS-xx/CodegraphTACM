# pandas-86 :: hybrid

query: BUG: correct wrong error message in df.pivot when columns=None (#30925)

## selected nodes

- rank=1 layer=FUNCTION tokens=1825 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::pivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=2 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=3 layer=FUNCTION tokens=1995 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pivot_table [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def pivot_table(
        self,
        values=None,
        index=None,
        columns=None,
        aggfunc: AggFuncType = "mean",
        fill_value=None,
        margins: bool = False,
        dropna: bool = True,
        margins_name: Level = "All",
        observed: bool = True,
        sort: bool = True,
        **kwargs,
    ) -> DataFrame:
        """
        Create a spreadsheet-style pivot table as a DataFrame.

        The levels in the pivot table will be stored in MultiIndex objects
        (hierarchical indexes) on the index and columns of the result DataFrame.

        Parameters
        ----------
        values : list-like or scalar, optional
            Column or columns to aggregate.
        index : column, Grouper, array, or sequence of the previous
            Keys to group by on the pivot table index. If a list is passed,
            it can contain any of the other types (except list). If an array is
            passed, it must be the same length as the data and will be used in
            the same manner as column values.
        columns : column, Grouper, array, or sequence of the previous
            Keys to group by on the pivot table column. If a list is passed,
            it can contain any of the other types (except list). If an array is
            passed, it must be the same length as the data and will be used in
            the same manner as column values.
        aggfunc : function, list of functions, dict, default "mean"
            If a list of functions is passed, the resulting pivot table will have
            hierarchical columns whose top level are the function names
            (inferred from the function objects themselves).
            If a dict is passed, the key is column to aggregate and the value is
            function or list of functions. If ``margin=True``, aggfunc will be
            used to calculate the partial aggregates.
        fill_value : scalar, default None
            Value to replace missing values with (in the resulting pivot table,
            after aggregation).
        margins : bool, default False
            If ``margins=True``, special ``All`` columns and rows
            will be added with partial group aggregates across the categories
            on the rows and columns.
        dropna : bool, default True
            Do not include columns whose entries are all NaN. If True,

            * rows with an NA value in any column will be omitted before computing
              margins,
            * index/column keys containing NA values will be dropped (see ``dropna``
              parameter in :meth:`DataFrame.groupby`).

        margins_name : str, default 'All'
            Name of the row / column that will contain the totals
            when margins is True.
        observed : bool, default False
            This only applies if any of the groupers are Categoricals.
            If True: only show observed values for categorical groupers.
            If False: show all values for categorical groupers.

            .. versionchanged:: 3.0.0

                The default value is now ``True``.

        sort : bool, default True
            Specifies if the result should be sorted.

        **kwargs : dict
            Optional keyword arguments to pass to ``aggfunc``.

        Returns
        -------
        DataFrame
            An Excel style pivot table.

        See Also
        --------
        DataFrame.pivot : Pivot without aggregation that can handle
            non-numeric data.
        DataFrame.melt: Unpivot a DataFrame from wide to long format,
            optionally leaving identifiers set.
        wide_to_long : Wide panel to long format. Less flexible but more
            user-friendly than melt.

        Notes
        -----
        Reference :ref:`the user guide <reshaping.pivot>` for more examples.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "A": [
        ...             "foo",
        ...             "foo",
        ...             "foo",
        ...             "foo",
        ...             "foo",
        ...             "bar",
        ...             "bar",
        ...             "bar",
        ...             "bar",
        ...         ],
        ...         "B": [
        ...             "one",
        ...             "one",
        ...             "one",
        ...             "two",
        ...             "two",
        ...             "one",
        ...             "one",
        ...             "two",
        ...             "two",
        ...         ],
        ...         "C": [
        ...             "small",
        ...             "large",
        ...             "large",
        ...             "small",
        ...             "small",
        ...             "large",
        ...             "small",
        ...             "small",
        ...             "large",
        ...         ],
        ...         "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
        ...         "E": [2, 4, 5, 5, 6, 6, 8, 9, 9],
        ...     }
        ... )
        >>> df
             A    B      C  D  E
        0  foo  one  small  1  2
        1  foo  one  large  2  4
        2  foo  one  large  2  5
        3  foo  two  small  3  5
        4  foo  two  small  3  6
        5  bar  one  large  4  6
        6  bar  one  small  5  8
        7  bar  two  small  6  9
        8  bar  two  large  7  9

        This first example aggregates values by taking the sum.

        >>> table = pd.pivot_table(
        ...     df, values="D", index=["A", "B"], columns=["C"], aggfunc="sum"
        ... )
        >>> table
        C        large  small
        A   B
        bar one    4.0    5.0
            two    7.0    6.0
        foo one    4.0    1.0
            two    NaN    6.0

        We can also fill missing values using the `fill_value` parameter.

        >>> table = pd.pivot_table(
        ...     df,
        ...     values="D",
        ...     index=["A", "B"],
        ...     columns=["C"],
        ...     aggfunc="sum",
        ...     fill_value=0,
        ... )
        >>> table
        C        large  small
        A   B
        bar one      4      5
            two      7      6
        foo one      4      1
            two      0      6

        The next example aggregates by taking the mean across multiple columns.

        >>> table = pd.pivot_table(
        ...     df,
        ...     values=["D", "E"],
        ...     index=["A", "C"],
        ...     aggfunc={"D": "mean", "E": "mean"},
        ... )
        >>> table
                        D         E
        A   C
        bar large  5.500000  7.500000
            small  5.500000  8.500000
        foo large  2.000000  4.500000
            small  2.333333  4.333333

        We can also calculate multiple types of aggregations for any given
        value column.

        >>> table = pd.pivot_table(
        ...     df,
        ...     values=["D", "E"],
        ...     index=["A", "C"],
        ...     aggfunc={"D": "mean", "E": ["min", "max", "mean"]},
        ... )
        >>> table
                          D   E
                       mean max      mean  min
        A   C
        bar large  5.500000   9  7.500000    6
            small  5.500000   9  8.500000    8
        foo large  2.000000   5  4.500000    4
            small  2.333333   6  4.333333    2
        """
        from pandas.core.reshape.pivot import pivot_table

        return pivot_table(
            self,
            values=values,
            index=index,
            columns=columns,
            aggfunc=aggfunc,
            fill_value=fill_value,
            margins=margins,
            dropna=dropna,
            margins_name=margins_name,
            observed=observed,
            sort=sort,
            **kwargs,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_margins(self):
        self.df.pivot_table(index="key1", columns=["key2", "key3"], margins=True)
```
