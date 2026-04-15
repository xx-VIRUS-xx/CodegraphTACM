# pandas-39 :: hybrid-cs

query: BUG: Fixed strange behaviour of pd.DataFrame.drop() with inplace argu… (#30501)

## selected nodes

- rank=1 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_bool file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=2 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=3 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_na file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=4 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=5 layer=FUNCTION tokens=891 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.drop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=6 layer=FUNCTION tokens=1452 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.drop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=7 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.drop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=8 layer=FUNCTION tokens=433 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pop file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=9 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=10 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_string file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=11 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterEnd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=12 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyArr_iterNextNone file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=13 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c::parser_del file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c
- rank=14 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=15 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_bool [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups_bool(self, inplace):
        self.df_bool.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_int [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups_int(self, inplace):
        self.df_int.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_na [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups_na(self, inplace):
        self.df_nan.drop_duplicates(["key1", "key2"], inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups(self, inplace):
        self.df.drop_duplicates(["key1", "key2"], inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.drop [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
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
        Return Series with specified index labels removed.

        Remove elements of a Series based on specifying the index labels.
        When using a multi-index, labels on different levels can be removed
        by specifying the level.

        Parameters
        ----------
        labels : single label or list-like
            Index labels to drop.
        axis : {0 or 'index'}
            Unused. Parameter needed for compatibility with DataFrame.
        index : single label or list-like
            Redundant for application on Series, but 'index' can be used instead
            of 'labels'.
        columns : single label or list-like
            No change is made to the Series; use 'index' or 'labels' instead.
        level : int or level name, optional
            For MultiIndex, level for which the labels will be removed.
        inplace : bool, default False
            If True, do operation inplace and return None.
        errors : {'ignore', 'raise'}, default 'raise'
            If 'ignore', suppress error and only existing labels are dropped.

        Returns
        -------
        Series or None
            Series with specified index labels removed or None if ``inplace=True``.

        Raises
        ------
        KeyError
            If none of the labels are found in the index.

        See Also
        --------
        Series.reindex : Return only specified index labels of Series.
        Series.dropna : Return series without null values.
        Series.drop_duplicates : Return Series with duplicate values removed.
        DataFrame.drop : Drop specified labels from rows or columns.

        Examples
        --------
        >>> s = pd.Series(data=np.arange(3), index=["A", "B", "C"])
        >>> s
        A  0
        B  1
        C  2
        dtype: int64

        Drop labels B and C

        >>> s.drop(labels=["B", "C"])
        A  0
        dtype: int64

        Drop 2nd level label in MultiIndex Series

        >>> midx = pd.MultiIndex(
        ...     levels=[["llama", "cow", "falcon"], ["speed", "weight", "length"]],
        ...     codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2]],
        ... )
        >>> s = pd.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)
        >>> s
        llama   speed      45.0
                weight    200.0
                length      1.2
        cow     speed      30.0
                weight    250.0
                length      1.5
        falcon  speed     320.0
                weight      1.0
                length      0.3
        dtype: float64

        >>> s.drop(labels="weight", level=1)
        llama   speed      45.0
                length      1.2
        cow     speed      30.0
                length      1.5
        falcon  speed     320.0
                length      0.3
        dtype: float64
        """
        return super().drop(
            labels=labels,
            axis=axis,
            index=index,
            columns=columns,
            level=level,
            inplace=inplace,
            errors=errors,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.drop [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
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
        Drop specified labels from rows or columns.

        Remove rows or columns by specifying label names and corresponding
        axis, or by directly specifying index or column names. When using a
        multi-index, labels on different levels can be removed by specifying
        the level. See the :ref:`user guide <advanced.shown_levels>`
        for more information about the now unused levels.

        Parameters
        ----------
        labels : single label or iterable of labels
            Index or column labels to drop. A tuple will be used as a single
            label and not treated as an iterable.
        axis : {0 or 'index', 1 or 'columns'}, default 0
            Whether to drop labels from the index (0 or 'index') or
            columns (1 or 'columns').
        index : single label or iterable of labels
            Alternative to specifying axis (``labels, axis=0``
            is equivalent to ``index=labels``).
        columns : single label or iterable of labels
            Alternative to specifying axis (``labels, axis=1``
            is equivalent to ``columns=labels``).
        level : int or level name, optional
            For MultiIndex, level from which the labels will be removed.
        inplace : bool, default False
            If False, return a copy. Otherwise, do operation
            in place and return None.
        errors : {'ignore', 'raise'}, default 'raise'
            If 'ignore', suppress error and only existing labels are
            dropped.

        Returns
        -------
        DataFrame or None
            Returns DataFrame or None DataFrame with the specified
            index or column labels removed or None if inplace=True.

        Raises
        ------
        KeyError
            If any of the labels is not found in the selected axis.

        See Also
        --------
        DataFrame.loc : Label-location based indexer for selection by label.
        DataFrame.dropna : Return DataFrame with labels on given axis omitted
            where (all or any) data are missing.
        DataFrame.drop_duplicates : Return DataFrame with duplicate rows
            removed, optionally only considering certain columns.
        Series.drop : Return Series with specified index labels removed.

        Examples
        --------
        >>> df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=["A", "B", "C", "D"])
        >>> df
           A  B   C   D
        0  0  1   2   3
        1  4  5   6   7
        2  8  9  10  11

        Drop columns

        >>> df.drop(["B", "C"], axis=1)
           A   D
        0  0   3
        1  4   7
        2  8  11

        >>> df.drop(columns=["B", "C"])
           A   D
        0  0   3
        1  4   7
        2  8  11

        Drop a row by index

        >>> df.drop([0, 1])
           A  B   C   D
        2  8  9  10  11

        Drop columns and/or rows of MultiIndex DataFrame

        >>> midx = pd.MultiIndex(
        ...     levels=[["llama", "cow", "falcon"], ["speed", "weight", "length"]],
        ...     codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2]],
        ... )
        >>> df = pd.DataFrame(
        ...     index=midx,
        ...     columns=["big", "small"],
        ...     data=[
        ...         [45, 30],
        ...         [200, 100],
        ...         [1.5, 1],
        ...         [30, 20],
        ...         [250, 150],
        ...         [1.5, 0.8],
        ...         [320, 250],
        ...         [1, 0.8],
        ...         [0.3, 0.2],
        ...     ],
        ... )
        >>> df
                        big     small
        llama   speed   45.0    30.0
                weight  200.0   100.0
                length  1.5     1.0
        cow     speed   30.0    20.0
                weight  250.0   150.0
                length  1.5     0.8
        falcon  speed   320.0   250.0
                weight  1.0     0.8
                length  0.3     0.2

        Drop a specific index combination from the MultiIndex
        DataFrame, i.e., drop the combination ``'falcon'`` and
        ``'weight'``, which deletes only the corresponding row

        >>> df.drop(index=("falcon", "weight"))
                        big     small
        llama   speed   45.0    30.0
                weight  200.0   100.0
                length  1.5     1.0
        cow     speed   30.0    20.0
                weight  250.0   150.0
                length  1.5     0.8
        falcon  speed   320.0   250.0
                length  0.3     0.2

        >>> df.drop(index="cow", columns="small")
                        big
        llama   speed   45.0
                weight  200.0
                length  1.5
        falcon  speed   320.0
                weight  1.0
                length  0.3

        >>> df.drop(index="length", level=1)
                        big     small
        llama   speed   45.0    30.0
                weight  200.0   100.0
        cow     speed   30.0    20.0
                weight  250.0   150.0
        falcon  speed   320.0   250.0
                weight  1.0     0.8
        """
        return super().drop(
            labels=labels,
            axis=axis,
            index=index,
            columns=columns,
            level=level,
            inplace=inplace,
            errors=errors,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.drop [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pop [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def pop(self, item: Hashable) -> Series:
        """
        Return item and drop it from DataFrame. Raise KeyError if not found.

        The column is removed from the DataFrame and returned as a Series;
        the original DataFrame is modified in place unless it was a view.

        Parameters
        ----------
        item : label
            Label of column to be popped.

        Returns
        -------
        Series
            Series representing the item that is dropped.

        See Also
        --------
        DataFrame.drop: Drop specified labels from rows or columns.
        DataFrame.drop_duplicates: Return DataFrame with duplicate rows removed.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     [
        ...         ("falcon", "bird", 389.0),
        ...         ("parrot", "bird", 24.0),
        ...         ("lion", "mammal", 80.5),
        ...         ("monkey", "mammal", np.nan),
        ...     ],
        ...     columns=("name", "class", "max_speed"),
        ... )
        >>> df
             name   class  max_speed
        0  falcon    bird      389.0
        1  parrot    bird       24.0
        2    lion  mammal       80.5
        3  monkey  mammal        NaN

        >>> df.pop("class")
        0      bird
        1      bird
        2    mammal
        3    mammal
        Name: class, dtype: str

        >>> df
             name  max_speed
        0  falcon      389.0
        1  parrot       24.0
        2    lion       80.5
        3  monkey        NaN
        """
        return super().pop(item=item)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_int [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_series_drop_dups_int(self, inplace):
        self.s.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_string [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_series_drop_dups_string(self, inplace):
        self.s_str.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterEnd [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void DataFrame_iterEnd(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  PyObjectEncoder *enc = (PyObjectEncoder *)tc->encoder;
  enc->outputFormat = enc->originalOutputFormat;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyArr_iterNextNone [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static int NpyArr_iterNextNone(JSOBJ Py_UNUSED(_obj),
                               JSONTypeContext *Py_UNUSED(tc)) {
  return 0;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c::parser_del [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c]
void parser_del(parser_t *self) { free(self); }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endArray [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_endArray(void *Py_UNUSED(prv), JSOBJ obj) { return obj; }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newNull(void *Py_UNUSED(prv)) { Py_RETURN_NONE; }
```
