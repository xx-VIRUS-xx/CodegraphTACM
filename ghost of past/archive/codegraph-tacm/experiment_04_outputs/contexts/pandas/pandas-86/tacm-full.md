# pandas-86 :: tacm-full

query: BUG: correct wrong error message in df.pivot when columns=None (#30925)

## selected nodes

- rank=1 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=2 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Pivot.time_reshape_pivot_time_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=3 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=4 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_agg file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=5 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins_only_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=6 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=7 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=8 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=9 layer=FUNCTION tokens=478 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._next_iter_line file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py
- rank=10 layer=FUNCTION tokens=366 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_exceptions.py::rewrite_warning file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_exceptions.py
- rank=11 layer=FUNCTION tokens=1825 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::pivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=12 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical_observed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table(self):
        self.df.pivot_table(index="key1", columns=["key2", "key3"])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Pivot.time_reshape_pivot_time_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_reshape_pivot_time_series(self):
        self.df.pivot(index="date", columns="variable", values="value")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_margins(self):
        self.df.pivot_table(index="key1", columns=["key2", "key3"], margins=True)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_agg [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_agg(self):
        self.df.pivot_table(
            index="key1", columns=["key2", "key3"], aggfunc=["sum", "mean"]
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins_only_column [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_margins_only_column(self):
        self.df.pivot_table(columns=["key1", "key2", "key3"], margins=True)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py]
    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.
        StringMethods.len : Compute the length of each element in the Series/Index.

        Examples
        --------
        >>> import pyarrow as pa
        >>> s = pd.Series(
        ...     [
        ...         [1, 2, 3],
        ...         [3],
        ...     ],
        ...     dtype=pd.ArrowDtype(pa.list_(pa.int64())),
        ... )
        >>> s.list.len()
        0    3
        1    1
        dtype: int32[pyarrow]
        """
        from pandas import Series

        value_lengths = pc.list_value_length(self._pa_array)
        return Series(
            value_lengths,
            dtype=ArrowDtype(value_lengths.type),
            index=self._data.index,
            name=self._data.name,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py]
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

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.

        Examples
        --------
        Returns the length (number of characters) in a string. Returns the
        number of entries for dictionaries, lists or tuples.

        >>> s = pd.Series(
        ...     ["dog", "", 5, {"foo": "bar"}, [2, 3, 5, 7], ("one", "two", "three")]
        ... )
        >>> s
        0                  dog
        1
        2                    5
        3       {'foo': 'bar'}
        4         [2, 3, 5, 7]
        5    (one, two, three)
        dtype: object
        >>> s.str.len()
        0    3.0
        1    0.0
        2    NaN
        3    1.0
        4    4.0
        5    3.0
        dtype: float64
        """
        result = self._data.array._str_len()
        return self._wrap_result(result, returns_string=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_pivot_table_categorical(self):
        self.df2.pivot_table(
            index="col1", values="col3", columns="col2", aggfunc="sum", fill_value=0
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._next_iter_line [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py]
    def _next_iter_line(self, row_num: int) -> list[Scalar] | None:
        """
        Wrapper around iterating through `self.data` (CSV source).

        When a CSV error is raised, we check for specific
        error messages that allow us to customize the
        error message displayed to the user.

        Parameters
        ----------
        row_num: int
            The row number of the line being parsed.
        """
        try:
            assert not isinstance(self.data, list)
            line = next(self.data)
            # lie about list[str] vs list[Scalar] to minimize ignores
            return line  # type: ignore[return-value]
        except csv.Error as e:
            if self.on_bad_lines in (
                self.BadLineHandleMethod.ERROR,
                self.BadLineHandleMethod.WARN,
            ):
                msg = str(e)

                if "NULL byte" in msg or "line contains NUL" in msg:
                    msg = (
                        "NULL byte detected. This byte "
                        "cannot be processed in Python's "
                        "native csv library at the moment, "
                        "so please pass in engine='c' instead"
                    )

                if self.skipfooter > 0:
                    reason = (
                        "Error could possibly be due to "
                        "parsing errors in the skipped footer rows "
                        "(the skipfooter keyword is only applied "
                        "after Python's csv library has parsed "
                        "all rows)."
                    )
                    msg += ". " + reason

                self._alert_malformed(msg, row_num)
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_exceptions.py::rewrite_warning [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_exceptions.py]
def rewrite_warning(
    target_message: str,
    target_category: type[Warning],
    new_message: str,
    new_category: type[Warning] | None = None,
) -> Generator[None]:
    """
    Rewrite the message of a warning.

    Parameters
    ----------
    target_message : str
        Warning message to match.
    target_category : Warning
        Warning type to match.
    new_message : str
        New warning message to emit.
    new_category : Warning or None, default None
        New warning type to emit. When None, will be the same as target_category.
    """
    if new_category is None:
        new_category = target_category
    with warnings.catch_warnings(record=True) as record:
        yield
    if len(record) > 0:
        match = re.compile(target_message)
        for warning in record:
            if warning.category is target_category and re.search(
                match, str(warning.message)
            ):
                category = new_category
                message: Warning | str = new_message
            else:
                category, message = warning.category, warning.message
            warnings.warn_explicit(
                message=message,
                category=category,
                filename=warning.filename,
                lineno=warning.lineno,
            )

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
```
