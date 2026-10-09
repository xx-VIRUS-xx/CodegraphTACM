# pandas-70 :: tacm

query: BUG: regression when applying groupby aggregation on categorical columns (#31359)

## selected nodes

- rank=1 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py
- rank=2 layer=FILE tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py
- rank=3 layer=FILE tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=4 layer=FILE tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/__init__.py
- rank=5 layer=FILE tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/base.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/base.py
- rank=6 layer=FILE tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/portable.h file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/portable.h
- rank=7 layer=CLASS tokens=385 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_grouping.py::TestGrouping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_grouping.py
- rank=8 layer=CLASS tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_describe.py::TestDataFrameDescribe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_describe.py
- rank=9 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=10 layer=CLASS tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=11 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py::recode_for_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py
- rank=12 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._groupby_and_aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=13 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::get_resampler_for_grouping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=14 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::groupby_func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py
- rank=15 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical.tests_merge_categorical_unordered_equal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=16 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py::_get_dataframe_dtype_counts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py
- rank=17 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py::get_categorical_invalid_expected file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py
- rank=18 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataWriter._prepare_categoricals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=19 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.select_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=20 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py::select_describe_func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py
- rank=21 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py::rolling_aggregation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py
- rank=22 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py::FromDicts.time_nested_dict_int64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py
- rank=23 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical._groupby_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=24 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::get_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=25 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_categorical.py::df_cat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_categorical.py
- rank=26 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby._gotitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=27 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataStrLWriter._convert_key file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=28 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical.remove_unused_categories file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=29 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py::non_coercible_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py
- rank=30 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::GroupStrings.time_multi_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=31 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler.aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=32 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical._encode_with_my_categories file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=33 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=34 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=35 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py::BaseGrouper.result_index_and_ids file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py
- rank=36 layer=FUNCTION tokens=296 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_CrossMergeOperation.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=37 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.get_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=38 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.num_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=39 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=40 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.select_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=41 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_raises.py::groupby_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_raises.py

## context

```text
file core/groupby/categorical.py
imports: __future__, numpy, pandas
defines: recode_for_groupby

file core/methods/describe.py
imports: __future__, abc, typing, numpy, pandas, collections
defines: NDFrameDescriberAbstract, SeriesDescriber, DataFrameDescriber, describe_ndframe, reorder_columns, describe_numeric_1d, describe_categorical_1d, describe_timestamp_1d, select_describe_func, _refine_percentiles

file core/groupby/groupby.py
imports: __future__, collections, datetime, functools, typing, warnings, numpy, pandas
defines: GroupByPlot, BaseGroupBy, GroupBy, get_groupby, _insert_quantile_level

file core/groupby/__init__.py
imports: pandas
defines: —

file core/groupby/base.py
imports: __future__, dataclasses, typing, collections
defines: OutputKey

file include/pandas/portable.h
imports: string
defines: —

class TestGrouping:  [tests/groupby/test_grouping.py:180]
methods: test_agg_with_dict_raises, test_empty_groups
         test_evaluate_with_empty_groups
         test_groupby_apply_empty_with_group_keys_false
         test_groupby_args
         test_groupby_categorical_index_and_columns
         test_groupby_dict_mapping
         test_groupby_duplicate_index_level_names
         test_groupby_empty, test_groupby_grouper
         test_groupby_grouper_f_sanity_checked
         test_groupby_grouper_immutable_list_item
         test_groupby_level
         test_groupby_level_index_names
         test_groupby_level_index_value_all_na
         test_groupby_level_with_nas
         test_groupby_levels_and_columns
         test_groupby_multiindex_level_empty
         test_groupby_multiindex_partial_indexing_equivalence
         test_groupby_multiindex_tuple
         test_groupby_series_named_with_tuple
         test_groupby_tuple_keys_handle_multiindex
         test_groupby_with_datetime_key
         test_grouper_column_and_index
         test_grouper_creation_bug
         test_grouper_creation_bug2
         test_grouper_creation_bug3
         test_grouper_getting_correct_binner
         test_grouper_index_types, test_grouper_iter
         test_grouper_multilevel_freq
         test_grouper_returning_tuples
         test_grouping_error_on_multidim_input
         test_grouping_labels, test_level_preserve_order
         test_list_grouper_with_nat
         test_multiindex_columns_empty_level
         test_multiindex_negative_level

class TestDataFrameDescribe:  [frame/methods/test_describe.py:15]
methods: test_datetime_is_numeric_includes_datetime
         test_describe_bool_frame
         test_describe_bool_in_mixed_frame
         test_describe_categorical
         test_describe_categorical_columns
         test_describe_datetime_columns
         test_describe_does_not_raise_error_for_dictlike_elements
         test_describe_empty_categorical_column
         test_describe_empty_object
         test_describe_exclude_pa_dtype
         test_describe_percentiles_integer_idx
         test_describe_timedelta_values
         test_describe_tz_values, test_describe_tz_values2
         test_describe_when_include_all_exclude_not_allowed
         test_describe_when_included_dtypes_not_present
         test_describe_with_duplicate_columns
         test_ea_with_na, test_refine_percentiles

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class TestMergeCategorical:  [reshape/merge/test_merge.py:1944]
methods: test_basic, test_dtype_on_categorical_dates
         test_dtype_on_merged_different, test_identical
         test_merge_categorical
         test_merge_category_index_levels_stay_category
         test_merge_on_int_array
         test_merging_with_bool_or_int_cateorical_column
         test_multiindex_merge_with_unordered_categoricalindex
         test_other_columns
         test_self_join_multiple_categories
         tests_merge_categorical_unordered_equal

def recode_for_groupby(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    # ... truncated

    def _groupby_and_aggregate(self, how, *args, **kwargs):
        """
        Re-evaluate the obj with a groupby aggregation.
        """
    # ... truncated

def get_resampler_for_grouping(
    groupby: GroupBy,
    rule,
    how=None,
    fill_method=None,
    limit: int | None = None,
    on=None,
    **kwargs,
) -> Resampler:
    """
    Return our appropriate resampler when grouping as well.
    """
    # .resample uses 'on' similar to how .groupby uses 'key'
    tg = TimeGrouper(freq=rule, key=on, **kwargs)
    resampler = tg._get_resampler(groupby.obj)
    return resampler._get_resampler_for_grouping(groupby=groupby, key=tg.key)

def groupby_func(request):
    """yields both aggregation and transformation functions."""
    return request.param

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

def _get_dataframe_dtype_counts(df: DataFrame) -> Mapping[str, int]:
    """
    Create mapping between datatypes and their number of occurrences.
    """
    # groupby dtype.name to collect e.g. Categorical columns
    return df.dtypes.value_counts().groupby(lambda x: x.name).sum()

    def get_categorical_invalid_expected():
        # Categorical is special without 'observed=True', we get a NaN entry
        #  corresponding to the unobserved group. If we passed observed=True
        #  to groupby, expected would just be 'df.set_index(keys)[columns]'
        #  as below
        lev = Categorical([0], dtype=values.dtype)
        if len(keys) != 1:
            idx = MultiIndex.from_product([lev, lev], names=keys)
        else:
            # all columns are dropped, but we end up with one row
            # Categorical is special without 'observed=True'
            idx = Index(lev, name=keys[0])

        if using_infer_string:
            columns = Index([], dtype="str")
        else:
            columns = []
        expected = DataFrame([], columns=columns, index=idx)
        return expected

    def _prepare_categoricals(self, data: DataFrame) -> DataFrame:
        """
        Check for categorical columns, retain categorical information for
        Stata file and convert categorical data to int
        """
    # ... truncated

    def select_dtypes(self, include=None, exclude=None) -> DataFrame:
        """
        Return a subset of the DataFrame's columns based on the column dtypes.

        This method allows for filtering columns based on their data types.
        It is useful when working with heterogeneous DataFrames where operations
        need to be performed on a specific subset of data types.

        Parameters
        ----------
        include, exclude : scalar or list-like
            A selection of dtypes or strings to be included/excluded. At least
    # ... truncated

def select_describe_func(
    data: Series,
) -> Callable:
    """Select proper function for describing series based on data type.

    Parameters
    ----------
    data : Series
        Series to be described.
    """
    if is_bool_dtype(data.dtype):
        return describe_categorical_1d
    elif is_numeric_dtype(data):
        return describe_numeric_1d
    elif data.dtype.kind == "M" or isinstance(data.dtype, DatetimeTZDtype):
        return describe_timestamp_1d
    elif data.dtype.kind == "m":
        return describe_numeric_1d
    else:
        return describe_categorical_1d

def rolling_aggregation(request):
    """Make a rolling aggregation function as fixture."""
    return request.param

    def time_nested_dict_int64(self):
        # nested dict, integer indexes, regression described in #621
        DataFrame(self.data2)

    def _groupby_op(
        self,
        *,
        how: str,
        has_dropped_na: bool,
        min_count: int,
        ngroups: int,
        ids: npt.NDArray[np.intp],
        **kwargs,
    ):
        from pandas.core.groupby.ops import WrappedCythonOp

    # ... truncated

def get_groupby(
    obj: NDFrame,
    by: _KeysArgType | None = None,
    grouper: ops.BaseGrouper | None = None,
    group_keys: bool = True,
) -> GroupBy:
    """
    # ... truncated

def df_cat(df):
    """
    DataFrame with multiple categorical columns and a column of integers.
    Shortened so as not to contain all possible combinations of categories.
    Useful for testing `observed` kwarg functionality on GroupBy objects.

    Parameters
    ----------
    df: DataFrame
        Non-categorical, longer DataFrame from another fixture, used to derive
        this one

    Returns
    -------
    df_cat: DataFrame
    """
    df_cat = df.copy()[:4]  # leave out some groups
    df_cat["A"] = df_cat["A"].astype("category")
    df_cat["B"] = df_cat["B"].astype("category")
    df_cat["C"] = Series([1, 2, 3, 4])
    df_cat = df_cat.drop(["D"], axis=1)
    return df_cat

    def _gotitem(self, key, ndim, subset=None):
        # we are setting the index on the actual object
        # here so our index is carried through to the selected obj
        # when we do the splitting for the groupby
        if self.on is not None:
            # GH 43355
            subset = self.obj.set_index(self._on)
        return super()._gotitem(key, ndim, subset=subset)

    def _convert_key(self, key: tuple[int, int]) -> int:
        v, o = key
        if self._native_byteorder:
            return v + self._o_offet * o
        else:
            # v, o will be swapped when applying byteorder
            return o + self._o_offet * v

    def remove_unused_categories(self) -> Self:
        """
        Remove categories which are not used.

        This method is useful when working with datasets
        that undergo dynamic changes where categories may no longer be
        relevant, allowing to maintain a clean, efficient data structure.

        Returns
        -------
        Categorical
            Categorical with unused categories dropped.
    # ... truncated

def non_coercible_categorical(monkeypatch):
    """
    Monkeypatch Categorical.__array__ to ensure no implicit conversion.

    Raises
    ------
    ValueError
        When Categorical.__array__ is called.
    """

    # TODO(Categorical): identify other places where this may be
    # useful and move to a conftest.py
    def array(self, dtype=None):
        raise ValueError("I cannot be converted.")

    with monkeypatch.context() as m:
        m.setattr(Categorical, "__array__", array)
        yield

    def time_multi_columns(self):
        self.df.groupby(list("abcd")).max()

    def aggregate(self, func=None, *args, **kwargs):
        """
        Aggregate using one or more operations over the specified axis.

        This method applies aggregation functions to resampled groups, enabling
        summary statistics to be computed for each time period.

        Parameters
        ----------
        func : function, str, list or dict
            Function to use for aggregating the data. If a function, must either
            work when passed a DataFrame or when passed to DataFrame.apply.
    # ... truncated

    def _encode_with_my_categories(self, other: Categorical) -> Categorical:
        """
        Re-encode another categorical using this Categorical's categories.

        Notes
        -----
        This assumes we have already checked
        self._categories_match_up_to_permutation(other).
        """
        # Indexing on codes is more efficient if categories are the same,
        #  so we can apply some optimizations based on the degree of
        #  dtype-matching.
        codes = recode_for_categories(
            other.codes, other.categories, self.categories, copy=False
        )
        return self._from_backing_data(codes)

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
    # ... truncated

    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

    # ... truncated

    def result_index_and_ids(self) -> tuple[Index, npt.NDArray[np.intp]]:
        levels = [
            Index._with_infer(ping.uniques, copy=False) for ping in self.groupings
        ]
        obs = [
            ping._observed or not ping._passed_categorical for ping in self.groupings
        ]
        sorts = [ping._sort for ping in self.groupings]
        # When passed a categorical grouping, keep all categories
        for k, (ping, level) in enumerate(zip(self.groupings, levels, strict=True)):
            if ping._passed_categorical:
                levels[k] = level.set_categories(ping._orig_cats)  # type: ignore[attr-defined]
    # ... truncated

    def __init__(
        self,
        left: DataFrame | Series,
        right: DataFrame | Series,
        suffixes: Suffixes = ("_x", "_y"),
        indicator: str | bool = False,
    ) -> None:
        _left = _validate_operand(left)
        _right = _validate_operand(right)
        self.left = self.orig_left = _left
        self.right = self.orig_right = _right
        self.how: JoinHow = "inner"
        self.on = None
        self.suffixes = suffixes
        self.sort = False
        self.left_index = False
        self.right_index = False
        self.indicator = indicator
        self.anti_join = False
        self.left_on: list = []
        self.right_on: list = []
        self.left_join_keys: list[ArrayLike] = []
        self.right_join_keys: list[ArrayLike] = []
        self.join_names: list[Hashable] = []

        # GH#40993: raise when merging between different levels
        if _left.columns.nlevels != _right.columns.nlevels:
            raise MergeError(
                "Not allowed to merge between different levels. "
                f"({_left.columns.nlevels} levels on the left, "
                f"{_right.columns.nlevels} on the right)"
            )

    def get_columns(self) -> Iterable[Column]:
        """
        Return an iterator yielding the columns.
        """

    def num_columns(self) -> int:
        """
        Return the number of columns in the DataFrame.
        """

    def time_pivot_table_categorical(self):
        self.df2.pivot_table(
            index="col1", values="col3", columns="col2", aggfunc="sum", fill_value=0
        )

    def select_columns(self, indices: Sequence[int]) -> DataFrame:
        """
        Create a new DataFrame by selecting a subset of columns by index.
        """

def groupby_series(request):
    return request.param
```
