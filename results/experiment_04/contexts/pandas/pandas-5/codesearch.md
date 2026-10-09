# pandas-5 :: codesearch

query: BUG: DataFrameGroupby std/sem modify grouped column when as_index=False (#33630)

## selected nodes

- rank=1 layer=FUNCTION tokens=278 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._apply_to_column_groupbys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=2 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb::make_pretty file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb
- rank=3 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._maybe_make_multi_index_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=4 layer=FUNCTION tokens=311 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_set_index.py::frame_of_index_cols file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_set_index.py
- rank=5 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.select_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py
- rank=6 layer=FUNCTION tokens=2277 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=7 layer=FUNCTION tokens=382 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._do_select_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=8 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_reset_index.py::multiindex_df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_reset_index.py
- rank=9 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=10 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._apply_to_column_groupbys [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb::make_pretty [/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb]
    "  - Formatting values, the index and columns headers, using [.format()][formatfunc] and [.format_index()][formatfuncindex],\n",
    "  - Renaming the index or column header labels, using [.relabel_index()][relabelfunc]\n",
    "  - Hiding certain columns, the index and/or column headers, or index names, using [.hide()][hidefunc]\n",
    "  - Concatenating similar DataFrames, using [.concat()][concatfunc]\n",
    "  \n",
    "[styler]: ../reference/api/pandas.io.formats.style.Styler.rst\n",

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._maybe_make_multi_index_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py]
    def _maybe_make_multi_index_columns(
        self,
        columns: SequenceT,
        col_names: Sequence[Hashable] | None = None,
    ) -> SequenceT | MultiIndex:
        # possibly create a column mi here
        if is_potential_multi_index(columns):
            columns_mi = cast("Sequence[tuple[Hashable, ...]]", columns)
            return MultiIndex.from_tuples(columns_mi, names=col_names)
        return columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_set_index.py::frame_of_index_cols [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_set_index.py]
def frame_of_index_cols():
    """
    Fixture for DataFrame of columns that can be used for indexing

    Columns are ['A', 'B', 'C', 'D', 'E', ('tuple', 'as', 'label')];
    'A' & 'B' contain duplicates (but are jointly unique), the rest are unique.

         A      B  C         D         E  (tuple, as, label)
    0  foo    one  a  0.608477 -0.012500           -1.664297
    1  foo    two  b -0.633460  0.249614           -0.364411
    2  foo  three  c  0.615256  2.154968           -0.834666
    3  bar    one  d  0.234246  1.085675            0.718445
    4  bar    two  e  0.533841 -0.005702           -3.533912
    """
    df = DataFrame(
        {
            "A": ["foo", "foo", "foo", "bar", "bar"],
            "B": ["one", "two", "three", "one", "two"],
            "C": ["a", "b", "c", "d", "e"],
            "D": np.random.default_rng(2).standard_normal(5),
            "E": np.random.default_rng(2).standard_normal(5),
            ("tuple", "as", "label"): np.random.default_rng(2).standard_normal(5),
        }
    )
    return df

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.select_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py]
    def select_columns(self, indices: Sequence[int]) -> PandasDataFrameXchg:
        if not isinstance(indices, abc.Sequence):
            raise ValueError("`indices` is not a sequence")
        if not isinstance(indices, list):
            indices = list(indices)

        return PandasDataFrameXchg(
            self._df.iloc[:, indices], allow_copy=self._allow_copy
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.groupby [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def groupby(
        self,
        by=None,
        level: IndexLabel | None = None,
        as_index: bool = True,
        sort: bool = True,
        group_keys: bool = True,
        observed: bool = True,
        dropna: bool = True,
    ) -> DataFrameGroupBy:
        """
        Group DataFrame using a mapper or by a Series of columns.

        A groupby operation involves some combination of splitting the
        object, applying a function, and combining the results. This can be
        used to group large amounts of data and compute operations on these
        groups.

        Parameters
        ----------
        by : mapping, function, label, pd.Grouper or list of such
            Used to determine the groups for the groupby.
            If ``by`` is a function, it's called on each value of the object's
            index. If a dict or Series is passed, the Series or dict VALUES
            will be used to determine the groups (the Series' values are first
            aligned; see ``.align()`` method). If a list or ndarray of length
            equal to the number of rows is passed (see the `groupby user guide
            <https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#splitting-an-object-into-groups>`_),
            the values are used as-is to determine the groups. A label or list
            of labels may be passed to group by the columns in ``self``.
            Notice that a tuple is interpreted as a (single) key.
        level : int, level name, or sequence of such, default None
            If the axis is a MultiIndex (hierarchical), group by a particular
            level or levels. Do not specify both ``by`` and ``level``.
        as_index : bool, default True
            Return object with group labels as the
            index. Only relevant for DataFrame input. as_index=False is
            effectively "SQL-style" grouped output. This argument has no effect
            on filtrations (see the `filtrations in the user guide
            <https://pandas.pydata.org/docs/dev/user_guide/groupby.html#filtration>`_),
            such as ``head()``, ``tail()``, ``nth()`` and in transformations
            (see the `transformations in the user guide
            <https://pandas.pydata.org/docs/dev/user_guide/groupby.html#transformation>`_).
        sort : bool, default True
            Sort group keys. Get better performance by turning this off.
            Note this does not influence the order of observations within each
            group. Groupby preserves the order of rows within each group. If False,
            the groups will appear in the same order as they did in the original
            DataFrame.
            This argument has no effect on filtrations (see the `filtrations
            in the user guide
            <https://pandas.pydata.org/docs/dev/user_guide/groupby.html#filtration>`_),
            such as ``head()``, ``tail()``, ``nth()`` and in transformations
            (see the `transformations in the user guide
            <https://pandas.pydata.org/docs/dev/user_guide/groupby.html#transformation>`_).

            .. versionchanged:: 2.0.0

                Specifying ``sort=False`` with an ordered categorical grouper will no
                longer sort the values.

        group_keys : bool, default True
            When calling apply and the ``by`` argument produces a like-indexed
            (i.e. :ref:`a transform <groupby.transform>`) result, add group keys to
            index to identify pieces. By default group keys are not included
            when the result's index (and column) labels match the inputs, and
            are included otherwise.

            .. versionchanged:: 2.0.0

               ``group_keys`` now defaults to ``True``.

        observed : bool, default True
            This only applies if any of the groupers are Categoricals.
            If True: only show observed values for categorical groupers.
            If False: show all values for categorical groupers.

            .. versionchanged:: 3.0.0

                The default value is now ``True``.

        dropna : bool, default True
            If True, and if group keys contain NA values, NA values together
            with row/column will be dropped.
            If False, NA values will also be treated as the key in groups.

        Returns
        -------
        pandas.api.typing.DataFrameGroupBy
            Returns a groupby object that contains information about the groups.

        See Also
        --------
        resample : Convenience method for frequency conversion and resampling
            of time series.

        Notes
        -----
        See the `user guide
        <https://pandas.pydata.org/pandas-docs/stable/groupby.html>`__ for more
        detailed usage and examples, including splitting an object into groups,
        iterating through groups, selecting a group, aggregation, and more.

        The implementation of groupby is hash-based, meaning in particular that
        objects that compare as equal will be considered to be in the same group.
        An exception to this is that pandas has special handling of NA values:
        any NA values will be collapsed to a single group, regardless of how
        they compare. See the user guide linked above for more details.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "Animal": ["Falcon", "Falcon", "Parrot", "Parrot"],
        ...         "Max Speed": [380.0, 370.0, 24.0, 26.0],
        ...     }
        ... )
        >>> df
           Animal  Max Speed
        0  Falcon      380.0
        1  Falcon      370.0
        2  Parrot       24.0
        3  Parrot       26.0
        >>> df.groupby(["Animal"]).mean()
                Max Speed
        Animal
        Falcon      375.0
        Parrot       25.0

        **Hierarchical Indexes**

        We can groupby different levels of a hierarchical index
        using the `level` parameter:

        >>> arrays = [
        ...     ["Falcon", "Falcon", "Parrot", "Parrot"],
        ...     ["Captive", "Wild", "Captive", "Wild"],
        ... ]
        >>> index = pd.MultiIndex.from_arrays(arrays, names=("Animal", "Type"))
        >>> df = pd.DataFrame({"Max Speed": [390.0, 350.0, 30.0, 20.0]}, index=index)
        >>> df
                        Max Speed
        Animal Type
        Falcon Captive      390.0
               Wild         350.0
        Parrot Captive       30.0
               Wild          20.0
        >>> df.groupby(level=0).mean()
                Max Speed
        Animal
        Falcon      370.0
        Parrot       25.0
        >>> df.groupby(level="Type").mean()
                 Max Speed
        Type
        Captive      210.0
        Wild         185.0

        We can also choose to include NA in group keys or not by setting
        `dropna` parameter, the default setting is `True`.

        >>> arr = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
        >>> df = pd.DataFrame(arr, columns=["a", "b", "c"])

        >>> df.groupby(by=["b"]).sum()
            a   c
        b
        1.0 2   3
        2.0 2   5

        >>> df.groupby(by=["b"], dropna=False).sum()
            a   c
        b
        1.0 2   3
        2.0 2   5
        NaN 1   4

        >>> arr = [["a", 12, 12], [None, 12.3, 33.0], ["b", 12.3, 123], ["a", 1, 1]]
        >>> df = pd.DataFrame(arr, columns=["a", "b", "c"])

        >>> df.groupby(by="a").sum()
            b     c
        a
        a   13.0   13.0
        b   12.3  123.0

        >>> df.groupby(by="a", dropna=False).sum()
            b     c
        a
        a   13.0   13.0
        b   12.3  123.0
        NaN 12.3   33.0

        When using ``.apply()``, use ``group_keys`` to include or exclude the
        group keys. The ``group_keys`` argument defaults to ``True`` (include).

        >>> df = pd.DataFrame(
        ...     {
        ...         "Animal": ["Falcon", "Falcon", "Parrot", "Parrot"],
        ...         "Max Speed": [380.0, 370.0, 24.0, 26.0],
        ...     }
        ... )
        >>> df.groupby("Animal", group_keys=True)[["Max Speed"]].apply(lambda x: x)
                  Max Speed
        Animal
        Falcon 0      380.0
               1      370.0
        Parrot 2       24.0
               3       26.0

        >>> df.groupby("Animal", group_keys=False)[["Max Speed"]].apply(lambda x: x)
           Max Speed
        0      380.0
        1      370.0
        2       24.0
        3       26.0
        """
        from pandas.core.groupby.generic import DataFrameGroupBy

        if level is None and by is None:
            raise TypeError("You have to supply one of 'by' and 'level'")

        return DataFrameGroupBy(
            obj=self,
            keys=by,
            level=level,
            as_index=as_index,
            sort=sort,
            group_keys=group_keys,
            observed=observed,
            dropna=dropna,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._do_select_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py]
    def _do_select_columns(self, data: DataFrame, columns: Sequence[str]) -> DataFrame:
        if not self._column_selector_set:
            column_set = set(columns)
            if len(column_set) != len(columns):
                raise ValueError("columns contains duplicate entries")
            unmatched = column_set.difference(data.columns)
            if unmatched:
                joined = ", ".join(list(unmatched))
                raise ValueError(
                    "The following columns were not "
                    f"found in the Stata data set: {joined}"
                )
            # Copy information for retained columns for later processing
            dtyplist = []
            typlist = []
            fmtlist = []
            lbllist = []
            for col in columns:
                i = data.columns.get_loc(col)
                dtyplist.append(self._dtyplist[i])
                typlist.append(self._typlist[i])
                fmtlist.append(self._fmtlist[i])
                lbllist.append(self._lbllist[i])

            self._dtyplist = dtyplist  # type: ignore[assignment]
            self._typlist = typlist  # type: ignore[assignment]
            self._fmtlist = fmtlist  # type: ignore[assignment]
            self._lbllist = lbllist  # type: ignore[assignment]
            self._column_selector_set = True

        return data[columns]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_reset_index.py::multiindex_df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_reset_index.py]
def multiindex_df():
    levels = [["A", ""], ["B", "b"]]
    return DataFrame([[0, 2], [1, 3]], columns=MultiIndex.from_tuples(levels))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.__getitem__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
    def __getitem__(self, key) -> DataFrameGroupBy | SeriesGroupBy:
        # per GH 23566
        if isinstance(key, tuple) and len(key) > 1:
            # if len == 1, then it becomes a SeriesGroupBy and this is actually
            # valid syntax, so don't raise
            raise ValueError(
                "Cannot subset columns with a tuple with more than one element. "
                "Use a list instead."
            )
        return super().__getitem__(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::loc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def loc(x):
    return x.loc
```
