# pandas-70 :: hybrid-cs

query: BUG: regression when applying groupby aggregation on categorical columns (#31359)

## selected nodes

- rank=1 layer=FUNCTION tokens=477 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._groupby_and_aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=2 layer=FUNCTION tokens=367 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py::assert_categorical_single_grouper file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py
- rank=3 layer=FUNCTION tokens=2207 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=4 layer=FUNCTION tokens=638 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::get_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=5 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical.tests_merge_categorical_unordered_equal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=6 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::GroupStrings.time_multi_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._groupby_and_aggregate [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _groupby_and_aggregate(self, how, *args, **kwargs):
        """
        Re-evaluate the obj with a groupby aggregation.
        """
        grouper = self._grouper

        # Excludes `on` column when provided
        obj = self._obj_with_exclusions

        grouped = get_groupby(obj, by=None, grouper=grouper, group_keys=self.group_keys)

        try:
            if callable(how):
                # TODO: test_resample_apply_with_additional_args fails if we go
                #  through the non-lambda path, not clear that it should.
                func = lambda x: how(x, *args, **kwargs)
                result = grouped.aggregate(func)
            else:
                result = grouped.aggregate(how, *args, **kwargs)
        except (AttributeError, KeyError):
            # we have a non-reducing function; try to evaluate
            # alternatively we want to evaluate only a column of the input

            # test_apply_to_one_column_of_df the function being applied references
            #  a DataFrame column, but aggregate_item_by_item operates column-wise
            #  on Series, raising AttributeError or KeyError
            #  (depending on whether the column lookup uses getattr/__getitem__)
            result = grouped.apply(how, *args, **kwargs)

        except ValueError as err:
            if "Must produce aggregated value" in str(err):
                # raised in _aggregate_named
                # see test_apply_without_aggregation, test_apply_with_mutated_index
                pass
            else:
                raise

            # we have a non-reducing function
            # try to evaluate
            result = grouped.apply(how, *args, **kwargs)

        return self._wrap_result(result)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py::assert_categorical_single_grouper [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py]
def assert_categorical_single_grouper(
    education_df, as_index, observed, expected_index, normalize, name, expected_data
):
    # Test single categorical grouper when non-groupers are also categorical
    education_df = education_df.copy().astype("category")

    # Add non-observed grouping categories
    education_df["country"] = education_df["country"].cat.add_categories(["ASIA"])

    gp = education_df.groupby("country", as_index=as_index, observed=observed)
    result = gp.value_counts(normalize=normalize)

    expected_series = Series(
        data=expected_data,
        index=MultiIndex.from_tuples(
            expected_index,
            names=["country", "gender", "education"],
        ),
        name=name,
    )
    for i in range(3):
        index_level = CategoricalIndex(expected_series.index.levels[i])
        if i == 0:
            index_level = index_level.set_categories(
                education_df["country"].cat.categories
            )
        expected_series.index = expected_series.index.set_levels(index_level, level=i)

    if as_index:
        tm.assert_series_equal(result, expected_series)
    else:
        expected = expected_series.reset_index(name=name)
        tm.assert_frame_equal(result, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.aggregate [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
    def aggregate(
        self, func=None, *args, engine=None, engine_kwargs=None, **kwargs
    ) -> DataFrame:
        """
        Aggregate using one or more operations.

        The ``aggregate`` function allows the application of one or more aggregation
        operations on groups of data within a DataFrameGroupBy object. It supports
        various aggregation methods, including user-defined functions and predefined
        functions such as 'sum', 'mean', etc.

        Parameters
        ----------
        func : function, str, list, dict or None
            Function to use for aggregating the data. If a function, must either
            work when passed a DataFrame or when passed to DataFrame.apply.

            Accepted combinations are:

            - function
            - string function name
            - list of functions and/or function names, e.g. ``[np.sum, 'mean']``
            - dict of index labels -> functions, function names or list of such.
            - None, in which case ``**kwargs`` are used with Named Aggregation. Here the
              output has one column for each element in ``**kwargs``. The name of the
              column is keyword, whereas the value determines the aggregation used to
              compute the values in the column.

              Can also accept a Numba JIT function with
              ``engine='numba'`` specified. Only passing a single function is supported
              with this engine.

              If the ``'numba'`` engine is chosen, the function must be
              a user defined function with ``values`` and ``index`` as the
              first and second arguments respectively in the function signature.
              Each group's index will be passed to the user defined function
              and optionally available for use.

        *args
            Positional arguments to pass to func.
        engine : str, default None
            * ``'cython'`` : Runs the function through C-extensions from cython.
            * ``'numba'`` : Runs the function through JIT compiled code from numba.
            * ``None`` : Defaults to ``'cython'`` or globally setting
                ``compute.use_numba``

        engine_kwargs : dict, default None
            * For ``'cython'`` engine, there are no accepted ``engine_kwargs``
            * For ``'numba'`` engine, the engine can accept  ``nogil``
              and ``parallel`` dictionary keys. The values must either be ``True`` or
              ``False``. The default ``engine_kwargs`` for the ``'numba'`` engine is
              ``{'nogil': False, 'parallel': False}`` and will be
              applied to the function

        **kwargs
            * If ``func`` is None, ``**kwargs`` are used to define the output names and
              aggregations via Named Aggregation. See ``func`` entry.
            * Otherwise, keyword arguments to be passed into func.

        Returns
        -------
        DataFrame
            Aggregated DataFrame based on the grouping and the applied aggregation
            functions.

        See Also
        --------
        DataFrame.groupby.apply : Apply function func group-wise
            and combine the results together.
        DataFrame.groupby.transform : Transforms the Series on each group
            based on the given function.
        DataFrame.aggregate : Aggregate using one or more operations.

        Notes
        -----
        See :ref:`groupby.aggregate` in the User Guide for more details
        and examples.

        When using ``engine='numba'``, there will be no "fall back" behavior internally.
        The group data and group index will be passed as numpy arrays to the JITed
        user defined function, and no alternative execution attempts will be tried.

        Functions that mutate the passed object can produce unexpected
        behavior or errors and are not supported. See :ref:`gotchas.udf-mutation`
        for more details.

        The resulting dtype will reflect the return value of the passed ``func``,
        see the examples below.

        Examples
        --------
        >>> data = {
        ...     "A": [1, 1, 2, 2],
        ...     "B": [1, 2, 3, 4],
        ...     "C": [0.362838, 0.227877, 1.267767, -0.562860],
        ... }
        >>> df = pd.DataFrame(data)
        >>> df
           A  B         C
        0  1  1  0.362838
        1  1  2  0.227877
        2  2  3  1.267767
        3  2  4 -0.562860

        The aggregation is for each column.

        >>> df.groupby("A").agg("min")
           B         C
        A
        1  1  0.227877
        2  3 -0.562860

        Multiple aggregations

        >>> df.groupby("A").agg(["min", "max"])
            B             C
          min max       min       max
        A
        1   1   2  0.227877  0.362838
        2   3   4 -0.562860  1.267767

        Select a column for aggregation

        >>> df.groupby("A").B.agg(["min", "max"])
           min  max
        A
        1    1    2
        2    3    4

        User-defined function for aggregation

        >>> df.groupby("A").agg(lambda x: sum(x) + 2)
            B          C
        A
        1       5       2.590715
        2       9       2.704907

        Different aggregations per column

        >>> df.groupby("A").agg({"B": ["min", "max"], "C": "sum"})
            B             C
          min max       sum
        A
        1   1   2  0.590715
        2   3   4  0.704907

        To control the output names with different aggregations per column,
        pandas supports "named aggregation"

        >>> df.groupby("A").agg(
        ...     b_min=pd.NamedAgg(column="B", aggfunc="min"),
        ...     c_sum=pd.NamedAgg(column="C", aggfunc="sum"),
        ... )
           b_min     c_sum
        A
        1      1  0.590715
        2      3  0.704907

        - The keywords are the *output* column names
        - The values are tuples whose first element is the column to select
          and the second element is the aggregation to apply to that column.
          Pandas provides the ``pandas.NamedAgg`` namedtuple with the fields
          ``['column', 'aggfunc']`` to make it clearer what the arguments are.
          As usual, the aggregation can be a callable or a string alias.

        See :ref:`groupby.aggregate.named` for more.

        The resulting dtype will reflect the return value of the aggregating
        function.

        >>> df.groupby("A")[["B"]].agg(lambda x: x.astype(float).min())
              B
        A
        1   1.0
        2   3.0
        """
        relabeling, func, columns, order = reconstruct_func(func, **kwargs)
        func = maybe_mangle_lambdas(func)

        if maybe_use_numba(engine):
            # Not all agg functions support numba, only propagate numba kwargs
            # if user asks for numba
            kwargs["engine"] = engine
            kwargs["engine_kwargs"] = engine_kwargs

        op = GroupByApply(self, func, args=args, kwargs=kwargs)
        result = op.agg()
        if not is_dict_like(func) and result is not None:
            # GH #52849
            if not self.as_index and is_list_like(func):
                return result.reset_index()
            else:
                return cast("DataFrame", result)
        elif relabeling:
            # this should be the only (non-raising) case with relabeling
            # used reordered index of columns
            result = cast("DataFrame", result)
            result = result.iloc[:, order]
            result = cast("DataFrame", result)
            # error: Incompatible types in assignment (expression has type
            # "Optional[List[str]]", variable has type
            # "Union[Union[Union[ExtensionArray, ndarray[Any, Any]],
            # Index, Series], Sequence[Any]]")
            result.columns = columns  # type: ignore[assignment]

        if result is None:
            # Remove the kwargs we inserted
            # (already stored in engine, engine_kwargs arguments)
            if "engine" in kwargs:
                del kwargs["engine"]
                del kwargs["engine_kwargs"]
            # at this point func is not a str, list-like, dict-like,
            # or a known callable(e.g. sum)
            if maybe_use_numba(engine):
                return self._aggregate_with_numba(
                    func, *args, engine_kwargs=engine_kwargs, **kwargs
                )
            result = self._python_agg_general(func, *args, **kwargs)

        if not self.as_index:
            result = self._insert_inaxis_grouper(result)
            result.index = default_index(len(result))

        return cast("DataFrame", result)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical.tests_merge_categorical_unordered_equal [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py]
    def tests_merge_categorical_unordered_equal(self):
        # GH-19551
        df1 = DataFrame(
            {
                "Foo": Categorical(["A", "B", "C"], categories=["A", "B", "C"]),
                "Left": ["A0", "B0", "C0"],
            }
        )

        df2 = DataFrame(
            {
                "Foo": Categorical(["C", "B", "A"], categories=["C", "B", "A"]),
                "Right": ["C1", "B1", "A1"],
            }
        )
        result = merge(df1, df2, on=["Foo"])
        expected = DataFrame(
            {
                "Foo": Categorical(["A", "B", "C"]),
                "Left": ["A0", "B0", "C0"],
                "Right": ["A1", "B1", "C1"],
            }
        )
        tm.assert_frame_equal(result, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::GroupStrings.time_multi_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py]
    def time_multi_columns(self):
        self.df.groupby(list("abcd")).max()
```
