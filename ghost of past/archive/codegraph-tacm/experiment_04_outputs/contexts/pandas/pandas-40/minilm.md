# pandas-40 :: minilm

query: BUG: 27453 right merge order (#31278)

## selected nodes

- rank=1 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeRangeLikeFastPath.time_right_join_unsorted_right file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=2 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeRangeLikeFastPath.time_left_join_unsorted_left file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=3 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeRangeLikeFastPath.time_left_join_zero_match_unsorted_left file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=4 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeOrdered.time_merge_ordered file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=5 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_2intkey file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=6 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_dataframe_empty_right file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=7 layer=FUNCTION tokens=2416 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=8 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_dataframe_empty_left file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=9 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeRangeLikeFastPath.time_left_join_sorted_baseline file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=10 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_merger file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=11 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::_check_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=12 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=13 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_cat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=14 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_col file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=15 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_cross_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=16 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_object file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=17 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::UniqueMerge.time_unique_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=18 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/roperator.py::rtruediv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/roperator.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeRangeLikeFastPath.time_right_join_unsorted_right [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_right_join_unsorted_right(self, n):
        self.left_sorted.merge(self.right_unsorted, on="k", how="right", sort=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeRangeLikeFastPath.time_left_join_unsorted_left [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_left_join_unsorted_left(self, n):
        self.left_unsorted.merge(self.right_sorted, on="k", how="left", sort=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeRangeLikeFastPath.time_left_join_zero_match_unsorted_left [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_left_join_zero_match_unsorted_left(self, n):
        self.left_miss.merge(self.right_sorted, on="k", how="left", sort=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeOrdered.time_merge_ordered [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_ordered(self):
        merge_ordered(self.left, self.right, on="key", left_by="group")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_2intkey [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_2intkey(self, sort):
        merge(self.left, self.right, sort=sort)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_dataframe_empty_right [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_dataframe_empty_right(self, sort):
        merge(self.left, self.right.iloc[:0], sort=sort)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::merge [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
def merge(
    left: DataFrame | Series,
    right: DataFrame | Series,
    how: MergeHow = "inner",
    on: IndexLabel | AnyArrayLike | None = None,
    left_on: IndexLabel | AnyArrayLike | None = None,
    right_on: IndexLabel | AnyArrayLike | None = None,
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = False,
    suffixes: Suffixes = ("_x", "_y"),
    copy: bool | lib.NoDefault = lib.no_default,
    indicator: str | bool = False,
    validate: str | None = None,
) -> DataFrame:
    """
    Merge DataFrame or named Series objects with a database-style join.

    A named Series object is treated as a DataFrame with a single named column.

    The join is done on columns or indexes. If joining columns on
    columns, the DataFrame indexes *will be ignored*. Otherwise if joining indexes
    on indexes or indexes on a column or columns, the index will be passed on.
    When performing a cross merge, no column specifications to merge on are
    allowed.

    .. warning::

        If both key columns contain rows where the key is a null value, those
        rows will be matched against each other. This is different from usual SQL
        join behaviour and can lead to unexpected results.

    Parameters
    ----------
    left : DataFrame or named Series
        First pandas object to merge.
    right : DataFrame or named Series
        Second pandas object to merge.
    how : {'left', 'right', 'outer', 'inner', 'cross', 'left_anti', 'right_anti},
        default 'inner'
        Type of merge to be performed.

        * left: use only keys from left frame, similar to a SQL left outer join;
          preserve key order.
        * right: use only keys from right frame, similar to a SQL right outer join;
          preserve key order.
        * outer: use union of keys from both frames, similar to a SQL full outer
          join; sort keys lexicographically.
        * inner: use intersection of keys from both frames, similar to a SQL inner
          join; preserve the order of the left keys.
        * cross: creates the cartesian product from both frames, preserves the order
          of the left keys.
        * left_anti: use only keys from left frame that are not in right frame, similar
          to SQL left anti join; preserve key order.
        * right_anti: use only keys from right frame that are not in left frame, similar
          to SQL right anti join; preserve key order.
    on : Hashable or a sequence of the previous
        Column or index level names to join on. These must be found in both
        DataFrames. If `on` is None and not merging on indexes then this defaults
        to the intersection of the columns in both DataFrames.
    left_on : Hashable or a sequence of the previous, or array-like
        Column or index level names to join on in the left DataFrame. Can also
        be an array or list of arrays of the length of the left DataFrame.
        These arrays are treated as if they are columns.
    right_on : Hashable or a sequence of the previous, or array-like
        Column or index level names to join on in the right DataFrame. Can also
        be an array or list of arrays of the length of the right DataFrame.
        These arrays are treated as if they are columns.
    left_index : bool, default False
        Use the index from the left DataFrame as the join key(s). If it is a
        MultiIndex, the number of keys in the other DataFrame (either the index
        or a number of columns) must match the number of levels.
    right_index : bool, default False
        Use the index from the right DataFrame as the join key. Same caveats as
        left_index.
    sort : bool, default False
        Sort the join keys lexicographically in the result DataFrame. If False,
        the order of the join keys depends on the join type (how keyword).
    suffixes : list-like, default is ("_x", "_y")
        A length-2 sequence where each element is optionally a string
        indicating the suffix to add to overlapping column names in
        `left` and `right` respectively. Pass a value of `None` instead
        of a string to indicate that the column name from `left` or
        `right` should be left as-is, with no suffix. At least one of the
        values must not be None.
    copy : bool, default False
        This keyword is now ignored; changing its value will have no
        impact on the method.

        .. deprecated:: 3.0.0

            This keyword is ignored and will be removed in pandas 4.0. Since
            pandas 3.0, this method always returns a new object using a lazy
            copy mechanism that defers copies until necessary
            (Copy-on-Write). See the `user guide on Copy-on-Write
            <https://pandas.pydata.org/docs/dev/user_guide/copy_on_write.html>`__
            for more details.

    indicator : bool or str, default False
        If True, adds a column to the output DataFrame called "_merge" with
        information on the source of each row. The column can be given a different
        name by providing a string argument. The column will have a Categorical
        type with the value of "left_only" for observations whose merge key only
        appears in the left DataFrame, "right_only" for observations
        whose merge key only appears in the right DataFrame, and "both"
        if the observation's merge key is found in both DataFrames.

    validate : str, optional
        If specified, checks if merge is of specified type.

        * "one_to_one" or "1:1": check if merge keys are unique in both
          left and right datasets.
        * "one_to_many" or "1:m": check if merge keys are unique in left
          dataset.
        * "many_to_one" or "m:1": check if merge keys are unique in right
          dataset.
        * "many_to_many" or "m:m": allowed, but does not result in checks.

    Returns
    -------
    DataFrame
        A DataFrame of the two merged objects.

    See Also
    --------
    merge_ordered : Merge with optional filling/interpolation.
    merge_asof : Merge on nearest keys.
    DataFrame.join : Similar method using indices.

    Examples
    --------
    >>> df1 = pd.DataFrame(
    ...     {"lkey": ["foo", "bar", "baz", "foo"], "value": [1, 2, 3, 5]}
    ... )
    >>> df2 = pd.DataFrame(
    ...     {"rkey": ["foo", "bar", "baz", "foo"], "value": [5, 6, 7, 8]}
    ... )
    >>> df1
        lkey value
    0   foo      1
    1   bar      2
    2   baz      3
    3   foo      5
    >>> df2
        rkey value
    0   foo      5
    1   bar      6
    2   baz      7
    3   foo      8

    Merge df1 and df2 on the lkey and rkey columns. The value columns have
    the default suffixes, _x and _y, appended.

    >>> df1.merge(df2, left_on="lkey", right_on="rkey")
      lkey  value_x rkey  value_y
    0  foo        1  foo        5
    1  foo        1  foo        8
    2  bar        2  bar        6
    3  baz        3  baz        7
    4  foo        5  foo        5
    5  foo        5  foo        8

    Merge DataFrames df1 and df2 with specified left and right suffixes
    appended to any overlapping columns.

    >>> df1.merge(df2, left_on="lkey", right_on="rkey", suffixes=("_left", "_right"))
      lkey  value_left rkey  value_right
    0  foo           1  foo            5
    1  foo           1  foo            8
    2  bar           2  bar            6
    3  baz           3  baz            7
    4  foo           5  foo            5
    5  foo           5  foo            8

    Merge DataFrames df1 and df2, but raise an exception if the DataFrames have
    any overlapping columns.

    >>> df1.merge(df2, left_on="lkey", right_on="rkey", suffixes=(False, False))
    Traceback (most recent call last):
    ...
    ValueError: columns overlap but no suffix specified:
        Index(['value'], dtype='str')

    >>> df1 = pd.DataFrame({"a": ["foo", "bar"], "b": [1, 2]})
    >>> df2 = pd.DataFrame({"a": ["foo", "baz"], "c": [3, 4]})
    >>> df1
          a  b
    0   foo  1
    1   bar  2
    >>> df2
          a  c
    0   foo  3
    1   baz  4

    >>> df1.merge(df2, how="inner", on="a")
          a  b  c
    0   foo  1  3

    >>> df1.merge(df2, how="left", on="a")
          a  b  c
    0   foo  1  3.0
    1   bar  2  NaN

    >>> df1 = pd.DataFrame({"left": ["foo", "bar"]})
    >>> df2 = pd.DataFrame({"right": [7, 8]})
    >>> df1
        left
    0   foo
    1   bar
    >>> df2
        right
    0   7
    1   8

    >>> df1.merge(df2, how="cross")
       left  right
    0   foo      7
    1   foo      8
    2   bar      7
    3   bar      8
    """
    left_df = _validate_operand(left)
    left._check_copy_deprecation(copy)
    right_df = _validate_operand(right)
    if how == "cross":
        return _cross_merge(
            left_df,
            right_df,
            on=on,
            left_on=left_on,
            right_on=right_on,
            left_index=left_index,
            right_index=right_index,
            sort=sort,
            suffixes=suffixes,
            indicator=indicator,
            validate=validate,
        )
    else:
        op = _MergeOperation(
            left_df,
            right_df,
            how=how,
            on=on,
            left_on=left_on,
            right_on=right_on,
            left_index=left_index,
            right_index=right_index,
            sort=sort,
            suffixes=suffixes,
            indicator=indicator,
            validate=validate,
        )
        return op.get_result()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_dataframe_empty_left [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_dataframe_empty_left(self, sort):
        merge(self.left.iloc[:0], self.right, sort=sort)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeRangeLikeFastPath.time_left_join_sorted_baseline [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_left_join_sorted_baseline(self, n):
        self.left_sorted.merge(self.right_sorted, on="k", how="left", sort=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_merger [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _merger(x, y) -> DataFrame:
        # perform the ordered merge operation
        op = _OrderedMerge(
            x,
            y,
            on=on,
            left_on=left_on,
            right_on=right_on,
            suffixes=suffixes,
            fill_method=fill_method,
            how=how,
        )
        return op.get_result()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::_check_merge [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py]
def _check_merge(x, y):
    for how in ["inner", "left", "outer"]:
        for sort in [True, False]:
            result = x.join(y, how=how, sort=sort)

            expected = merge(x.reset_index(), y.reset_index(), how=how, sort=sort)
            expected = expected.set_index("index")

            # TODO check_names on merge?
            tm.assert_frame_equal(result, expected, check_names=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_idx [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_on_cat_idx(self):
        merge(self.left_cat_idx, self.right_cat_idx, on="X")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_cat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_cat(self):
        merge(self.left_cat, self.right_cat, on="X")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_col [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_on_cat_col(self):
        merge(self.left_cat_col, self.right_cat_col, on="X")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_cross_merge [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
def _cross_merge(
    left: DataFrame,
    right: DataFrame,
    on: IndexLabel | AnyArrayLike | None = None,
    left_on: IndexLabel | AnyArrayLike | None = None,
    right_on: IndexLabel | AnyArrayLike | None = None,
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = False,
    suffixes: Suffixes = ("_x", "_y"),
    indicator: str | bool = False,
    validate: str | None = None,
) -> DataFrame:
    """
    See merge.__doc__ with how='cross'
    """

    if (
        left_index
        or right_index
        or right_on is not None
        or left_on is not None
        or on is not None
    ):
        raise MergeError(
            "Can not pass on, right_on, left_on or set right_index=True or "
            "left_index=True"
        )

    return _CrossMergeOperation(
        left,
        right,
        suffixes=suffixes,
        indicator=indicator,
    ).get_result()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_object [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_object(self):
        merge(self.left_object, self.right_object, on="X")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::UniqueMerge.time_unique_merge [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_unique_merge(self, unique_elements):
        merge(self.left, self.right, how="inner")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/roperator.py::rtruediv [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/roperator.py]
def rtruediv(left, right):
    return right / left
```
