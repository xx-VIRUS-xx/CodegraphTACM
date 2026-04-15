# pandas-5 :: minilm

query: BUG: DataFrameGroupby std/sem modify grouped column when as_index=False (#33630)

## selected nodes

- rank=1 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=2 layer=FUNCTION tokens=427 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=3 layer=FUNCTION tokens=330 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._wrap_aggregated_output file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=4 layer=FUNCTION tokens=816 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._wrap_applied_output file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=5 layer=FUNCTION tokens=686 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::SeriesGroupBy._wrap_applied_output file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=6 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::as_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=7 layer=FUNCTION tokens=207 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_timegrouper.py::groupby_with_truncated_bingrouper file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_timegrouper.py
- rank=8 layer=FUNCTION tokens=581 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby._apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=9 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::ApplyNonUniqueUnsortedIndex.time_groupby_apply_non_unique_unsorted_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=10 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=11 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::slice_test_grouped file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py
- rank=12 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._numba_prep file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=13 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def __init__(
        self,
        obj: DataFrame | Series,
        *args,
        _grouper: BaseGrouper,
        _as_index: bool = True,
        **kwargs,
    ) -> None:
        from pandas.core.groupby.ops import BaseGrouper

        if not isinstance(_grouper, BaseGrouper):
            raise ValueError("Must pass a BaseGrouper object.")
        self._grouper = _grouper
        self._as_index = _as_index
        # GH 32262: It's convention to keep the grouping column in
        # groupby.<agg_func>, but unexpected to users in
        # groupby.rolling.<agg_func>
        obj = obj.drop(columns=self._grouper.names, errors="ignore")
        # GH 15354
        if kwargs.get("step") is not None:
            raise NotImplementedError("step not implemented for groupby")
        super().__init__(obj, *args, **kwargs)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._wrap_applied_output [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
    def _wrap_applied_output(
        self,
        data: DataFrame,
        values: list,
        not_indexed_same: bool = False,
        is_transform: bool = False,
    ):
        if len(values) == 0:
            if is_transform:
                # GH#47787 see test_group_on_empty_multiindex
                res_index = data.index
            elif not self.group_keys:
                res_index = None
            else:
                res_index = self._grouper.result_index

            result = self.obj._constructor(index=res_index, columns=data.columns)
            result = result.astype(data.dtypes)
            return result

        # GH12824
        # using values[0] here breaks test_groupby_apply_none_first
        first_not_none = next(com.not_none(*values), None)

        if first_not_none is None:
            # GH9684 - All values are None, return an empty frame
            # GH57775 - Ensure that columns and dtypes from original frame are kept.
            result = self.obj._constructor(columns=data.columns)
            result = result.astype(data.dtypes)
            return result
        elif isinstance(first_not_none, DataFrame):
            return self._concat_objects(
                values,
                not_indexed_same=not_indexed_same,
                is_transform=is_transform,
            )

        key_index = self._grouper.result_index if self.as_index else None

        if isinstance(first_not_none, (np.ndarray, Index)):
            # GH#1738: values is list of arrays of unequal lengths
            #  fall through to the outer else clause
            # TODO: sure this is right?  we used to do this
            #  after raising AttributeError above
            # GH 18930
            if not is_hashable(self._selection):
                # error: Need type annotation for "name"
                name = tuple(self._selection)  # type: ignore[var-annotated, arg-type]
            else:
                # error: Incompatible types in assignment
                # (expression has type "Hashable", variable
                # has type "Tuple[Any, ...]")
                name = self._selection  # type: ignore[assignment]
            return self.obj._constructor_sliced(values, index=key_index, name=name)
        elif not isinstance(first_not_none, Series):
            # values are not series or array-like but scalars
            # self._selection not passed through to Series as the
            # result should not take the name of original selection
            # of columns
            if self.as_index:
                return self.obj._constructor_sliced(values, index=key_index)
            else:
                result = self.obj._constructor(values, columns=[self._selection])
                result = self._insert_inaxis_grouper(result)
                return result
        else:
            # values are Series
            return self._wrap_applied_output_series(
                values,
                not_indexed_same,
                first_not_none,
                key_index,
                is_transform,
            )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::SeriesGroupBy._wrap_applied_output [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
    def _wrap_applied_output(
        self,
        data: Series,
        values: list[Any],
        not_indexed_same: bool = False,
        is_transform: bool = False,
    ) -> DataFrame | Series:
        """
        Wrap the output of SeriesGroupBy.apply into the expected result.

        Parameters
        ----------
        data : Series
            Input data for groupby operation.
        values : List[Any]
            Applied output for each group.
        not_indexed_same : bool, default False
            Whether the applied outputs are not indexed the same as the group axes.

        Returns
        -------
        DataFrame or Series
        """
        if len(values) == 0:
            # GH #6265
            if is_transform:
                # GH#47787 see test_group_on_empty_multiindex
                res_index = data.index
            elif not self.group_keys:
                res_index = None
            else:
                res_index = self._grouper.result_index

            return self.obj._constructor(
                [],
                name=self.obj.name,
                index=res_index,
                dtype=data.dtype,
            )
        assert values is not None

        if isinstance(values[0], dict):
            # GH #823 #24880
            index = self._grouper.result_index
            res_df = self.obj._constructor_expanddim(values, index=index)
            # if self.observed is False,
            # keep all-NaN rows created while re-indexing
            res_ser = res_df.stack()
            res_ser.name = self.obj.name
            return res_ser
        elif isinstance(values[0], (Series, DataFrame)):
            result = self._concat_objects(
                values,
                not_indexed_same=not_indexed_same,
                is_transform=is_transform,
            )
            if isinstance(result, Series):
                result.name = self.obj.name
            if not self.as_index and not_indexed_same:
                result = self._insert_inaxis_grouper(result)
                result.index = default_index(len(result))
            return result.__finalize__(self.obj, method="groupby")
        else:
            # GH #6265 #24880
            result = self.obj._constructor(
                data=values, index=self._grouper.result_index, name=self.obj.name
            )
            if not self.as_index:
                result = self._insert_inaxis_grouper(result)
                result.index = default_index(len(result))
            return result.__finalize__(self.obj, method="groupby")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::as_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def as_index(request):
    """
    Fixture for 'as_index' argument in groupby.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_timegrouper.py::groupby_with_truncated_bingrouper [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_timegrouper.py]
def groupby_with_truncated_bingrouper(frame_for_truncated_bingrouper):
    """
    GroupBy object such that gb._grouper is a BinGrouper and
    len(gb._grouper.result_index) < len(gb._grouper.group_keys_seq)

    Aggregations on this groupby should have

        dti = date_range("2013-09-01", "2013-10-01", freq="5D", name="Date")

    As either the index or an index level.
    """
    df = frame_for_truncated_bingrouper

    tdg = Grouper(key="Date", freq="5D")
    gb = df.groupby(tdg)

    # check we're testing the case we're interested in
    assert len(gb._grouper.result_index) != len(gb._grouper.codes)

    return gb

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::ApplyNonUniqueUnsortedIndex.time_groupby_apply_non_unique_unsorted_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py]
    def time_groupby_apply_non_unique_unsorted_index(self):
        self.df.groupby("key", group_keys=False).apply(lambda x: x)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::slice_test_grouped [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py]
def slice_test_grouped(slice_test_df):
    return slice_test_df.groupby("Group", as_index=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._numba_prep [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py]
    def _numba_prep(self, data: DataFrame):
        ngroups = self._grouper.ngroups
        sorted_index = self._grouper.result_ilocs
        sorted_ids = self._grouper._sorted_ids

        sorted_data = data.take(sorted_index, axis=0).to_numpy()
        # GH 46867
        index_data = data.index
        if isinstance(index_data, MultiIndex):
            if len(self._grouper.groupings) > 1:
                raise NotImplementedError(
                    "Grouping with more than 1 grouping labels and "
                    "a MultiIndex is not supported with engine='numba'"
                )
            group_key = self._grouper.groupings[0].name
            index_data = index_data.get_level_values(group_key)
        sorted_index_data = index_data.take(sorted_index).to_numpy()

        starts, ends = lib.generate_slices(sorted_ids, ngroups)
        return (
            starts,
            ends,
            sorted_index_data,
            sorted_data,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def iat(x):
    return x.iat
```
