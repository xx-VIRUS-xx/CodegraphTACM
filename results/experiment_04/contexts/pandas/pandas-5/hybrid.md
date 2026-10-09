# pandas-5 :: hybrid

query: BUG: DataFrameGroupby std/sem modify grouped column when as_index=False (#33630)

## selected nodes

- rank=1 layer=FUNCTION tokens=427 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=2 layer=FUNCTION tokens=638 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::get_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=3 layer=FUNCTION tokens=801 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=4 layer=FUNCTION tokens=581 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby._apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=5 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::slice_test_grouped file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py
- rank=6 layer=FUNCTION tokens=330 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._wrap_aggregated_output file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=7 layer=FUNCTION tokens=682 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=8 layer=FUNCTION tokens=382 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::GroupByApply.agg_or_apply_dict_like file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=9 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py::trans2 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler.sem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def sem(
        self,
        ddof: int = 1,
        numeric_only: bool = False,
    ):
        """
        Compute standard error of the mean of groups, excluding missing values.

        For multiple groupings, the result index will be a MultiIndex.

        Parameters
        ----------
        ddof : int, default 1
            Degrees of freedom.

        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionchanged:: 2.0.0

                numeric_only now defaults to ``False``.

        Returns
        -------
        Series or DataFrame
            Standard error of the mean of values within each group.

        See Also
        --------
        DataFrame.sem : Return unbiased standard error of the mean over requested axis.
        Series.sem : Return unbiased standard error of the mean over requested axis.

        Examples
        --------

        >>> ser = pd.Series(
        ...     [1, 3, 2, 4, 3, 8],
        ...     index=pd.DatetimeIndex(
        ...         [
        ...             "2023-01-01",
        ...             "2023-01-10",
        ...             "2023-01-15",
        ...             "2023-02-01",
        ...             "2023-02-10",
        ...             "2023-02-15",
        ...         ]
        ...     ),
        ... )
        >>> ser.resample("MS").sem()
        2023-01-01    0.577350
        2023-02-01    1.527525
        Freq: MS, dtype: float64
        """
        return self._downsample("sem", ddof=ddof, numeric_only=numeric_only)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::get_groupby [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py]
def get_groupby(
    obj: NDFrame,
    by: _KeysArgType | None = None,
    grouper: ops.BaseGrouper | None = None,
    group_keys: bool = True,
) -> GroupBy:
    """
    Class for grouping and aggregating relational data.

    See aggregate, transform, and apply functions on this object.

    It's easiest to use obj.groupby(...) to use GroupBy, but you can also do:

    ::

        grouped = groupby(obj, ...)

    Parameters
    ----------
    obj : pandas object
    level : int, default None
        Level of MultiIndex
    groupings : list of Grouping objects
        Most users should ignore this
    exclusions : array-like, optional
        List of columns to exclude
    name : str
        Most users should ignore this

    Returns
    -------
    **Attributes**
    groups : dict
        {group name -> group labels}
    len(grouped) : int
        Number of groups

    Notes
    -----
    After grouping, see aggregate, apply, and transform functions. Here are
    some other brief notes about usage. When grouping by multiple groups, the
    result index will be a MultiIndex (hierarchical) by default.

    Iteration produces (key, group) tuples, i.e. chunking the data by group. So
    you can write code like:

    ::

        grouped = obj.groupby(keys)
        for key, group in grouped:
            # do something with the data

    Function calls on GroupBy, if not specially implemented, "dispatch" to the
    grouped data. So if you group a DataFrame and wish to invoke the std()
    method on each group, you can simply do:

    ::

        df.groupby(mapper).std()

    rather than

    ::

        df.groupby(mapper).aggregate(np.std)

    You can pass arguments to these "wrapped" functions, too.

    See the online documentation for full exposition on these topics and much
    more
    """
    if isinstance(obj, Series):
        from pandas.core.groupby.generic import SeriesGroupBy

        return SeriesGroupBy(
            obj=obj,
            keys=by,
            grouper=grouper,
            group_keys=group_keys,
        )
    elif isinstance(obj, DataFrame):
        from pandas.core.groupby.generic import DataFrameGroupBy

        return DataFrameGroupBy(
            obj=obj,
            keys=by,
            grouper=grouper,
            group_keys=group_keys,
        )
    else:  # pragma: no cover
        raise TypeError(f"invalid type: {obj}")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.sem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py]
    def sem(
        self, ddof: int = 1, numeric_only: bool = False, skipna: bool = True
    ) -> NDFrameT:
        """
        Compute standard error of the mean of groups, excluding missing values.

        For multiple groupings, the result index will be a MultiIndex.

        Parameters
        ----------
        ddof : int, default 1
            Degrees of freedom.

        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionchanged:: 2.0.0

                numeric_only now defaults to ``False``.

        skipna : bool, default True
            Exclude NA/null values. If an entire group is NA, the result will be NA.

            .. versionadded:: 3.0.0

        Returns
        -------
        Series or DataFrame
            Standard error of the mean of values within each group.

        See Also
        --------
        DataFrame.sem : Return unbiased standard error of the mean over requested axis.
        Series.sem : Return unbiased standard error of the mean over requested axis.

        Examples
        --------
        For SeriesGroupBy:

        >>> lst = ["a", "a", "b", "b"]
        >>> ser = pd.Series([5, 10, 8, 14], index=lst)
        >>> ser
        a     5
        a    10
        b     8
        b    14
        dtype: int64
        >>> ser.groupby(level=0).sem()
        a    2.5
        b    3.0
        dtype: float64

        For DataFrameGroupBy:

        >>> data = [[1, 12, 11], [1, 15, 2], [2, 5, 8], [2, 6, 12]]
        >>> df = pd.DataFrame(
        ...     data,
        ...     columns=["a", "b", "c"],
        ...     index=["tuna", "salmon", "catfish", "goldfish"],
        ... )
        >>> df
                   a   b   c
            tuna   1  12  11
          salmon   1  15   2
         catfish   2   5   8
        goldfish   2   6  12
        >>> df.groupby("a").sem()
              b  c
        a
        1    1.5  4.5
        2    0.5  2.0

        For Resampler:

        >>> ser = pd.Series(
        ...     [1, 3, 2, 4, 3, 8],
        ...     index=pd.DatetimeIndex(
        ...         [
        ...             "2023-01-01",
        ...             "2023-01-10",
        ...             "2023-01-15",
        ...             "2023-02-01",
        ...             "2023-02-10",
        ...             "2023-02-15",
        ...         ]
        ...     ),
        ... )
        >>> ser.resample("MS").sem()
        2023-01-01    0.577350
        2023-02-01    1.527525
        Freq: MS, dtype: float64
        """
        if numeric_only and self.obj.ndim == 1 and not is_numeric_dtype(self.obj.dtype):
            raise TypeError(
                f"{type(self).__name__}.sem called with "
                f"numeric_only={numeric_only} and dtype {self.obj.dtype}"
            )
        return self._cython_agg_general(
            "sem",
            alt=lambda x: Series(x, copy=False).sem(ddof=ddof, skipna=skipna),
            numeric_only=numeric_only,
            ddof=ddof,
            skipna=skipna,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby._apply [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def _apply(
        self,
        func: Callable[..., Any],
        name: str,
        numeric_only: bool = False,
        numba_args: tuple[Any, ...] = (),
        **kwargs,
    ) -> DataFrame | Series:
        result = super()._apply(
            func,
            name,
            numeric_only,
            numba_args,
            **kwargs,
        )
        # Reconstruct the resulting MultiIndex
        # 1st set of levels = group by labels
        # 2nd set of levels = original DataFrame/Series index
        grouped_object_index = self.obj.index
        grouped_index_name = [*grouped_object_index.names]
        groupby_keys = copy.copy(self._grouper.names)
        result_index_names = groupby_keys + grouped_index_name

        drop_columns = [
            key
            for key in self._grouper.names
            if key not in self.obj.index.names or key is None
        ]

        if len(drop_columns) != len(groupby_keys):
            # Our result will have still kept the column in the result
            result = result.drop(columns=drop_columns, errors="ignore")

        codes = self._grouper.codes
        levels = copy.copy(self._grouper.levels)

        group_indices = self._grouper.indices.values()
        if group_indices:
            indexer = np.concatenate(list(group_indices))
        else:
            indexer = np.array([], dtype=np.intp)
        codes = [c.take(indexer) for c in codes]

        # if the index of the original dataframe needs to be preserved, append
        # this index (but reordered) to the codes/levels from the groupby
        if grouped_object_index is not None:
            idx = grouped_object_index.take(indexer)
            if not isinstance(idx, MultiIndex):
                idx = MultiIndex.from_arrays([idx])
            codes.extend(list(idx.codes))
            levels.extend(list(idx.levels))

        result_index = MultiIndex(
            levels, codes, names=result_index_names, verify_integrity=False
        )

        result.index = result_index
        if not self._as_index:
            result = result.reset_index(level=list(range(len(groupby_keys))))
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::slice_test_grouped [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py]
def slice_test_grouped(slice_test_df):
    return slice_test_df.groupby("Group", as_index=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._wrap_aggregated_output [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py]
    def _wrap_aggregated_output(
        self,
        result: Series | DataFrame,
        qs: npt.NDArray[np.float64] | None = None,
    ):
        """
        Wraps the output of GroupBy aggregations into the expected result.

        Parameters
        ----------
        result : Series, DataFrame

        Returns
        -------
        Series or DataFrame
        """
        # ATM we do not get here for SeriesGroupBy; when we do, we will
        #  need to require that result.name already match self.obj.name

        if not self.as_index:
            # `not self.as_index` is only relevant for DataFrameGroupBy,
            #   enforced in __init__
            result = self._insert_inaxis_grouper(result, qs=qs)
            result = result._consolidate()
            result.index = default_index(len(result))

        else:
            index = self._grouper.result_index
            if qs is not None:
                # We get here with len(qs) != 1 and not self.as_index
                #  in test_pass_args_kwargs
                index = _insert_quantile_level(index, qs)
            result.index = index

        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.sem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def sem(
        self,
        axis: Axis | None = 0,
        skipna: bool = True,
        ddof: int = 1,
        numeric_only: bool = False,
        **kwargs,
    ) -> Series | Any:
        """
        Return unbiased standard error of the mean over requested axis.

        Normalized by N-1 by default. This can be changed using the ddof argument

        Parameters
        ----------
        axis : {index (0), columns (1)}
            For `Series` this parameter is unused and defaults to 0.

            .. warning::

                The behavior of DataFrame.sem with ``axis=None`` is deprecated,
                in a future version this will reduce over both axes and return a scalar
                To retain the old behavior, pass axis=0 (or do not pass axis).

        skipna : bool, default True
            Exclude NA/null values. If an entire row/column is NA, the result
            will be NA.
        ddof : int, default 1
            Delta Degrees of Freedom. The divisor used in calculations is N - ddof,
            where N represents the number of elements.
        numeric_only : bool, default False
            Include only float, int, boolean columns. Not implemented for Series.
        **kwargs :
            Additional keywords passed.

        Returns
        -------
        Series
            Unbiased standard error of the mean over requested axis.

        See Also
        --------
        DataFrame.var : Return unbiased variance over requested axis.
        DataFrame.std : Returns sample standard deviation over requested axis.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> round(s.sem(), 6)
        0.57735

        With a DataFrame

        >>> df = pd.DataFrame({"a": [1, 2], "b": [2, 3]}, index=["tiger", "zebra"])
        >>> df
               a   b
        tiger  1   2
        zebra  2   3
        >>> df.sem()
        a   0.5
        b   0.5
        dtype: float64

        Using axis=1

        >>> df.sem(axis=1)
        tiger   0.5
        zebra   0.5
        dtype: float64

        In this case, `numeric_only` should be set to `True`
        to avoid getting an error.

        >>> df = pd.DataFrame({"a": [1, 2], "b": ["T", "Z"]}, index=["tiger", "zebra"])
        >>> df.sem(numeric_only=True)
        a   0.5
        dtype: float64
        """
        result = super().sem(
            axis=axis, skipna=skipna, ddof=ddof, numeric_only=numeric_only, **kwargs
        )
        if isinstance(result, Series):
            result = result.__finalize__(self, method="sem")
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::GroupByApply.agg_or_apply_dict_like [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def agg_or_apply_dict_like(
        self, op_name: Literal["agg", "apply"]
    ) -> DataFrame | Series:
        from pandas.core.groupby.generic import (
            DataFrameGroupBy,
            SeriesGroupBy,
        )

        assert op_name in ["agg", "apply"]

        obj = self.obj
        kwargs: dict[str, Any] = {}
        if op_name == "apply":
            by_row = "_compat" if self.by_row else False
            kwargs.update({"by_row": by_row})

        if getattr(obj, "axis", 0) == 1:
            raise NotImplementedError("axis other than 0 is not supported")

        selected_obj = obj._selected_obj
        selection = obj._selection

        is_groupby = isinstance(obj, (DataFrameGroupBy, SeriesGroupBy))

        # Numba Groupby engine/engine-kwargs passthrough
        if is_groupby:
            engine = self.kwargs.get("engine", None)
            engine_kwargs = self.kwargs.get("engine_kwargs", None)
            kwargs.update({"engine": engine, "engine_kwargs": engine_kwargs})

        with com.temp_setattr(
            obj, "as_index", True, condition=hasattr(obj, "as_index")
        ):
            result_index, result_data = self.compute_dict_like(
                op_name, selected_obj, selection, kwargs
            )
        result = self.wrap_results_dict_like(selected_obj, result_index, result_data)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py::trans2 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py]
    def trans2(group):
        grouped = group.groupby(df.reindex(group.index)["B"])
        return grouped.sum().sort_values().iloc[:2]
```
