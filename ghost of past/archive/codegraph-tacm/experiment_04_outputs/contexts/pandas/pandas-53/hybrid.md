# pandas-53 :: hybrid

query: BUG: using loc[int] with object index (#31905)

## selected nodes

- rank=1 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_single_level_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=2 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.get_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=3 layer=FUNCTION tokens=2764 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=4 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_get_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=5 layer=FUNCTION tokens=240 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=6 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._maybe_cast_listlike_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=7 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_loc_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=8 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_loc_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=9 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py::ObjectEngineIndexing.time_get_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_single_level_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def _get_loc_single_level_index(self, level_index: Index, key: Hashable) -> int:
        """
        If key is NA value, location of index unify as -1.

        Parameters
        ----------
        level_index: Index
        key : label

        Returns
        -------
        loc : int
            If key is NA value, loc is -1
            Else, location of key in index.

        See Also
        --------
        Index.get_loc : The get_loc method for (single-level) index.
        """
        if is_scalar(key) and isna(key):
            # TODO: need is_valid_na_for_dtype(key, level_index.dtype)
            return -1
        else:
            return level_index.get_loc(key)  # type: ignore[return-value]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.get_loc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py]
    def get_loc(self, key):
        """
        Get integer location for requested label

        Returns
        -------
        loc : int, slice, or ndarray[int]
        """
        self._check_indexing_error(key)

        try:
            key = self._data._validate_scalar(key, unbox=False)
        except TypeError as err:
            raise KeyError(key) from err

        return Index.get_loc(self, key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.loc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def loc(self) -> _LocIndexer:
        """
        Access a group of rows and columns by label(s) or a boolean array.

        ``.loc[]`` is primarily label based, but may also be used with a
        boolean array.

        Allowed inputs are:

        - A single label, e.g. ``5`` or ``'a'``, (note that ``5`` is
          interpreted as a *label* of the index, and **never** as an
          integer position along the index).
        - A list or array of labels, e.g. ``['a', 'b', 'c']``.
        - A slice object with labels, e.g. ``'a':'f'``.

          .. warning:: Note that contrary to usual python slices, **both** the
              start and the stop are included

        - A boolean array of the same length as the axis being sliced,
          e.g. ``[True, False, True]``.
        - An alignable boolean Series. The index of the key will be aligned before
          masking.
        - An alignable Index. The Index of the returned selection will be the input.
        - A ``callable`` function with one argument (the calling Series or
          DataFrame) and that returns valid output for indexing (one of the above)

        See more at :ref:`Selection by Label <indexing.label>`.

        Raises
        ------
        KeyError
            If any items are not found.
        IndexingError
            If an indexed key is passed and its index is unalignable to the frame index.

        See Also
        --------
        DataFrame.at : Access a single value for a row/column label pair.
        DataFrame.iloc : Access group of rows and columns by integer position(s).
        DataFrame.xs : Returns a cross-section (row(s) or column(s)) from the
                       Series/DataFrame.
        Series.loc : Access group of values using labels.

        Examples
        --------
        **Getting values**

        >>> df = pd.DataFrame(
        ...     [[1, 2], [4, 5], [7, 8]],
        ...     index=["cobra", "viper", "sidewinder"],
        ...     columns=["max_speed", "shield"],
        ... )
        >>> df
                    max_speed  shield
        cobra               1       2
        viper               4       5
        sidewinder          7       8

        Single label. Note this returns the row as a Series.

        >>> df.loc["viper"]
        max_speed    4
        shield       5
        Name: viper, dtype: int64

        List of labels. Note using ``[[]]`` returns a DataFrame.

        >>> df.loc[["viper", "sidewinder"]]
                    max_speed  shield
        viper               4       5
        sidewinder          7       8

        Single label for row and column

        >>> df.loc["cobra", "shield"]
        np.int64(2)

        Slice with labels for row and single label for column. As mentioned
        above, note that both the start and stop of the slice are included.

        >>> df.loc["cobra":"viper", "max_speed"]
        cobra    1
        viper    4
        Name: max_speed, dtype: int64

        Boolean list with the same length as the row axis

        >>> df.loc[[False, False, True]]
                    max_speed  shield
        sidewinder          7       8

        Alignable boolean Series:

        >>> df.loc[
        ...     pd.Series([False, True, False], index=["viper", "sidewinder", "cobra"])
        ... ]
                             max_speed  shield
        sidewinder          7       8

        Index (same behavior as ``df.reindex``)

        >>> df.loc[pd.Index(["cobra", "viper"], name="foo")]
               max_speed  shield
        foo
        cobra          1       2
        viper          4       5

        Conditional that returns a boolean Series

        >>> df.loc[df["shield"] > 6]
                    max_speed  shield
        sidewinder          7       8

        Conditional that returns a boolean Series with column labels specified

        >>> df.loc[df["shield"] > 6, ["max_speed"]]
                    max_speed
        sidewinder          7

        Multiple conditional using ``&`` that returns a boolean Series

        >>> df.loc[(df["max_speed"] > 1) & (df["shield"] < 8)]
                    max_speed  shield
        viper          4       5

        Multiple conditional using ``|`` that returns a boolean Series

        >>> df.loc[(df["max_speed"] > 4) | (df["shield"] < 5)]
                    max_speed  shield
        cobra               1       2
        sidewinder          7       8

        Please ensure that each condition is wrapped in parentheses ``()``.
        See the :ref:`user guide<indexing.boolean>`
        for more details and explanations of Boolean indexing.

        .. note::
            If you find yourself using 3 or more conditionals in ``.loc[]``,
            consider using :ref:`advanced indexing<advanced.advanced_hierarchical>`.

            See below for using ``.loc[]`` on MultiIndex DataFrames.

        Callable that returns a boolean Series

        >>> df.loc[lambda df: df["shield"] == 8]
                    max_speed  shield
        sidewinder          7       8

        **Setting values**

        Set value for all items matching the list of labels

        >>> df.loc[["viper", "sidewinder"], ["shield"]] = 50
        >>> df
                    max_speed  shield
        cobra               1       2
        viper               4      50
        sidewinder          7      50

        Set value for an entire row

        >>> df.loc["cobra"] = 10
        >>> df
                    max_speed  shield
        cobra              10      10
        viper               4      50
        sidewinder          7      50

        Set value for an entire column

        >>> df.loc[:, "max_speed"] = 30
        >>> df
                    max_speed  shield
        cobra              30      10
        viper              30      50
        sidewinder         30      50

        Set value for rows matching callable condition

        >>> df.loc[df["shield"] > 35] = 0
        >>> df
                    max_speed  shield
        cobra              30      10
        viper               0       0
        sidewinder          0       0

        Add value matching location

        >>> df.loc["viper", "shield"] += 5
        >>> df
                    max_speed  shield
        cobra              30      10
        viper               0       5
        sidewinder          0       0

        Setting using a ``Series`` or a ``DataFrame`` sets the values matching the
        index labels, not the index positions.

        >>> shuffled_df = df.loc[["viper", "cobra", "sidewinder"]]
        >>> df.loc[:] += shuffled_df
        >>> df
                    max_speed  shield
        cobra              60      20
        viper               0      10
        sidewinder          0       0

        **Getting values on a DataFrame with an index that has integer labels**

        Another example using integers for the index

        >>> df = pd.DataFrame(
        ...     [[1, 2], [4, 5], [7, 8]],
        ...     index=[7, 8, 9],
        ...     columns=["max_speed", "shield"],
        ... )
        >>> df
           max_speed  shield
        7          1       2
        8          4       5
        9          7       8

        Slice with integer labels for rows. As mentioned above, note that both
        the start and stop of the slice are included.

        >>> df.loc[7:9]
           max_speed  shield
        7          1       2
        8          4       5
        9          7       8

        **Getting values with a MultiIndex**

        A number of examples using a DataFrame with a MultiIndex

        >>> tuples = [
        ...     ("cobra", "mark i"),
        ...     ("cobra", "mark ii"),
        ...     ("sidewinder", "mark i"),
        ...     ("sidewinder", "mark ii"),
        ...     ("viper", "mark ii"),
        ...     ("viper", "mark iii"),
        ... ]
        >>> index = pd.MultiIndex.from_tuples(tuples)
        >>> values = [[12, 2], [0, 4], [10, 20], [1, 4], [7, 1], [16, 36]]
        >>> df = pd.DataFrame(values, columns=["max_speed", "shield"], index=index)
        >>> df
                             max_speed  shield
        cobra      mark i           12       2
                   mark ii           0       4
        sidewinder mark i           10      20
                   mark ii           1       4
        viper      mark ii           7       1
                   mark iii         16      36

        Single label. Note this returns a DataFrame with a single index.

        >>> df.loc["cobra"]
                 max_speed  shield
        mark i          12       2
        mark ii          0       4

        Single index tuple. Note this returns a Series.

        >>> df.loc[("cobra", "mark ii")]
        max_speed    0
        shield       4
        Name: (cobra, mark ii), dtype: int64

        Single label for row and column. Similar to passing in a tuple, this
        returns a Series.

        >>> df.loc["cobra", "mark i"]
        max_speed    12
        shield        2
        Name: (cobra, mark i), dtype: int64

        Single tuple. Note using ``[[]]`` returns a DataFrame.

        >>> df.loc[[("cobra", "mark ii")]]
                       max_speed  shield
        cobra mark ii          0       4

        Single tuple for the index with a single label for the column

        >>> df.loc[("cobra", "mark i"), "shield"]
        np.int64(2)

        Slice from index tuple to single label

        >>> df.loc[("cobra", "mark i") : "viper"]
                             max_speed  shield
        cobra      mark i           12       2
                   mark ii           0       4
        sidewinder mark i           10      20
                   mark ii           1       4
        viper      mark ii           7       1
                   mark iii         16      36

        Slice from index tuple to index tuple

        >>> df.loc[("cobra", "mark i") : ("viper", "mark ii")]
                            max_speed  shield
        cobra      mark i          12       2
                   mark ii          0       4
        sidewinder mark i          10      20
                   mark ii          1       4
        viper      mark ii          7       1

        Please see the :ref:`user guide<advanced.advanced_hierarchical>`
        for more details and explanations of advanced indexing.

        **Assignment with Series**

        When assigning a Series to .loc[row_indexer, col_indexer], pandas aligns
        the Series by index labels, not by order or position.

        Series assignment with .loc and index alignment:

        >>> df = pd.DataFrame({"A": [1, 2, 3]}, index=[0, 1, 2])
        >>> s = pd.Series([10, 20], index=[1, 0])  # Note reversed order
        >>> df.loc[:, "B"] = s  # Aligns by index, not order
        >>> df
           A   B
        0  1  20.0
        1  2  10.0
        2  3 NaN
        """
        return _LocIndexer("loc", self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_get_loc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def index_get_loc(index, item):
    def index_get_loc_impl(index, item):
        # Initialize the hash table if not initialized
        if len(index.hashmap) == 0:
            for i, val in enumerate(index._data):
                index.hashmap[val] = i
        return index.hashmap[item]

    return index_get_loc_impl

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _set_value(self, label, value, takeable: bool = False) -> None:
        """
        Quickly set single value at passed label.

        If label is not contained, a new object is created with the label
        placed at the end of the result index.

        Parameters
        ----------
        label : object
            Partial indexing with MultiIndex not allowed.
        value : object
            Scalar value.
        takeable : interpret the index as indexers, default False
        """
        if not takeable:
            try:
                loc = self.index.get_loc(label)
            except KeyError:
                # set using a non-recursive method
                self.loc[label] = value
                return
        else:
            loc = label

        self._set_values(loc, value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._maybe_cast_listlike_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _maybe_cast_listlike_indexer(self, target: Axes) -> Index:
        """
        Analogue to maybe_cast_indexer for get_indexer instead of get_loc.
        """
        target_index = ensure_index(target)
        if (
            not hasattr(target, "dtype")
            and self.dtype == object
            and target_index.dtype == "string"
        ):
            # If we started with a list-like, avoid inference to string dtype if self
            # is object dtype (coercing to string dtype will alter the missing values)
            target_index = Index(target, dtype=self.dtype)
        elif (
            not hasattr(target, "dtype")
            and isinstance(self.dtype, StringDtype)
            and self.dtype.na_value is np.nan
            and using_string_dtype()
        ):
            # Fill missing values to ensure consistent missing value representation
            target_index = target_index.fillna(np.nan)
        return target_index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_loc_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_loc_array(self, index, index_structure):
        self.data.loc[self.array]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_loc_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_loc_scalar(self, index, index_structure):
        self.data.loc[800000]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py::ObjectEngineIndexing.time_get_loc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py]
    def time_get_loc(self, index_type):
        self.data.get_loc("b")
```
