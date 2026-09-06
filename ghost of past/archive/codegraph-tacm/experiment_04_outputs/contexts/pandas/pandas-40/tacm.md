# pandas-40 :: tacm

query: BUG: 27453 right merge order (#31278)

## selected nodes

- rank=1 layer=FILE tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=2 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=3 layer=CLASS tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=4 layer=CLASS tokens=555 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMerge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=5 layer=CLASS tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=6 layer=CLASS tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_multi.py::TestMergeMultiIndexNaN file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_multi.py
- rank=7 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_groupby_and_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=8 layer=FUNCTION tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation.get_result file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=9 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMerge.check1 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=10 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::merge_asof file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=11 layer=FUNCTION tokens=304 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._indicator_pre_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=12 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._indicator_post_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=13 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._validate_how file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=14 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=15 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMerge.check2 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=16 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::merge_ordered file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=17 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_coerce_merge_keys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=18 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_dataframe_empty_right file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=19 layer=FUNCTION tokens=227 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_cross_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=20 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_merger file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=21 layer=FUNCTION tokens=312 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._check_dtype_match file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=22 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_2intkey file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=23 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._get_merge_keys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=24 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeEA.time_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=25 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeDatetime.time_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=26 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_dataframe_empty_left file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=27 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::UniqueMerge.time_unique_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=28 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_object file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=29 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_cat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=30 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=31 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_dataframes_cross file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=32 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeOrdered.time_merge_ordered file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=33 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_col file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=34 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=35 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeRangeLikeFastPath.time_right_join_unsorted_right file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=36 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeMultiIndex.time_merge_sorted_multiindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=37 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._get_join_info file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=38 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::I8Merge.time_i8merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=39 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_dataframe_integer_2key file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=40 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb::highlight_max file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb

## context

```text
file core/reshape/merge.py
imports: __future__, datetime, functools, types, typing, warnings, numpy, pandas
defines: _MergeOperation, _CrossMergeOperation, _OrderedMerge, _AsOfMerge, merge, _cross_merge, _groupby_and_merge, merge_ordered, _merger, merge_asof, _maybe_promote_to_rangeindex, get_join_indexers, get_join_indexers_non_unique, restore_dropped_levels_multijoin, _convert_to_multiindex, _asof_by_function, _get_multiindex_indexer, _get_empty_indexer, _get_no_sort_one_missing_indexer, _left_join_on_index, _factorize_keys, _convert_arrays_and_get_rizer_klass, _sort_labels, _get_join_keys, _should_fill, _any, _validate_operand, _items_overlap_with_suffix, renamer

file pandas/core/generic.py
imports: __future__, collections, copy, datetime, functools, json, operator, pickle
defines: NDFrame

class _MergeOperation:  [core/reshape/merge.py:925]
methods: _create_join_index, _get_join_indexers, _get_join_info
         _get_merge_keys, _handle_anti_join
         _indicator_name, _indicator_post_merge
         _indicator_pre_merge, _maybe_add_join_keys
         _maybe_coerce_merge_keys
         _maybe_require_matching_dtypes
         _maybe_restore_index_levels, _reindex_and_concat
         _validate_how, _validate_left_right_on
         _validate_tolerance, _validate_validate_kwd
         get_result, left_error_msg, right_error_msg
         __init__

class TestMerge:  [reshape/merge/test_merge.py:65]
methods: check1, check1, check2, check2, df, df2, left
         test_handle_join_key_pass_array
         test_index_and_on_parameters_confusion
         test_indicator
         test_intelligently_handle_join_key
         test_join_append_timedeltas
         test_join_append_timedeltas2
         test_left_merge_empty_dataframe
         test_merge_all_na_column, test_merge_common
         test_merge_copy, test_merge_datetime64tz_values
         test_merge_datetime64tz_with_dst_transition
         test_merge_different_column_key_names
         test_merge_empty_dataframe
         test_merge_empty_frame, test_merge_how_validation
         test_merge_index_as_on_arg
         test_merge_index_singlekey_inner
         test_merge_index_singlekey_right_vs_left
         test_merge_indicator_arg_validation
         test_merge_indicator_invalid
         test_merge_indicator_multiple_columns
         test_merge_indicator_result_integrity
         test_merge_inner_join_empty
         test_merge_join_key_dtype_cast
         test_merge_left_empty_right_empty
         test_merge_left_empty_right_notempty
         test_merge_left_notempty_right_empty
         test_merge_misspecified, test_merge_nan_right
         test_merge_nan_right2, test_merge_nocopy
         test_merge_non_string_columns
         test_merge_non_unique_index_many_to_many
         test_merge_non_unique_indexes
         test_merge_non_unique_period_index
         test_merge_nosort, test_merge_on_datetime64tz
         test_merge_on_datetime64tz_empty
         test_merge_on_index_with_more_values
         test_merge_on_periods, test_merge_overlap
         test_merge_period_values
         test_merge_preserves_row_order
         test_merge_readonly, test_merge_right_index_right
         test_merge_same_order_left_right
         test_merge_take_missing_values_from_index_of_other_dtype
         test_merge_two_empty_df_no_division_error
         test_merge_type
         test_merge_validate_error_message
         test_no_overlap_more_informative_error
         test_other_datetime_unit
         test_other_timedelta_unit
         test_overlapping_columns_error_message
         test_validation

class _AsOfMerge(_OrderedMerge):  [core/reshape/merge.py:2394]
methods: _check_dtype_match, _convert_values_for_libjoin
         _get_join_indexers
         _maybe_require_matching_dtypes
         _validate_left_right_on, _validate_tolerance
         __init__

class TestMergeMultiIndexNaN:  [reshape/merge/test_multi.py:815]
methods: test_merge_multiindex_nan_left_index
         test_merge_multiindex_nan_right_index

def _groupby_and_merge(
    by, left: DataFrame | Series, right: DataFrame | Series, merge_pieces
):
    """
    # ... truncated

    def get_result(self) -> DataFrame:
        """
        Execute the merge.
        """
        if self.indicator:
            self.left, self.right = self._indicator_pre_merge(self.left, self.right)

        join_index, left_indexer, right_indexer = self._get_join_info()

        result = self._reindex_and_concat(join_index, left_indexer, right_indexer)

        if self.indicator:
            result = self._indicator_post_merge(result)

        self._maybe_add_join_keys(result, left_indexer, right_indexer)

        self._maybe_restore_index_levels(result)

        return result.__finalize__(
            types.SimpleNamespace(
                input_objs=[self.left, self.right], left=self.left, right=self.right
            ),
            method="merge",
        )

        def check1(exp, kwarg):
            result = merge(left, right, how="inner", **kwarg)
            tm.assert_frame_equal(result, exp)
            result = merge(left, right, how="right", **kwarg)
            tm.assert_frame_equal(result, exp)

def merge_asof(
    left: DataFrame | Series,
    right: DataFrame | Series,
    on: IndexLabel | None = None,
    left_on: IndexLabel | None = None,
    right_on: IndexLabel | None = None,
    left_index: bool = False,
    right_index: bool = False,
    by=None,
    left_by=None,
    right_by=None,
    suffixes: Suffixes = ("_x", "_y"),
    # ... truncated

    def _indicator_pre_merge(
        self, left: DataFrame, right: DataFrame
    ) -> tuple[DataFrame, DataFrame]:
        """
        Add one indicator column to each of the left and right inputs.

        These columns are used to produce another column in the output of the
        merge, indicating for each row of the output whether it was produced
        using the left, right or both inputs.
        """
        columns = left.columns.union(right.columns)

        for i in ["_left_indicator", "_right_indicator"]:
            if i in columns:
                raise ValueError(
                    "Cannot use `indicator=True` option when "
                    f"data contains a column named {i}"
                )
        if self._indicator_name in columns:
            raise ValueError(
                "Cannot use name of an existing column for indicator column"
            )

        left = left.copy(deep=False)
        right = right.copy(deep=False)

        left["_left_indicator"] = 1
        left["_left_indicator"] = left["_left_indicator"].astype("int8")

        right["_right_indicator"] = 2
        right["_right_indicator"] = right["_right_indicator"].astype("int8")

        return left, right

    def _indicator_post_merge(self, result: DataFrame) -> DataFrame:
        """
        Add an indicator column to the merge result.

        This column indicates for each row of the output whether it was produced using
        the left, right or both inputs.
        """
        result["_left_indicator"] = result["_left_indicator"].fillna(0)
        result["_right_indicator"] = result["_right_indicator"].fillna(0)

        result[self._indicator_name] = Categorical(
            (result["_left_indicator"] + result["_right_indicator"]),
            categories=[1, 2, 3],
        )
        result[self._indicator_name] = result[
            self._indicator_name
        ].cat.rename_categories(["left_only", "right_only", "both"])

        result = result.drop(labels=["_left_indicator", "_right_indicator"], axis=1)
        return result

    def _validate_how(
        self, how: JoinHow | Literal["left_anti", "right_anti", "asof"]
    ) -> tuple[JoinHow | Literal["asof"], bool]:
        """
        Validate the 'how' parameter and return the actual join type and whether
        this is an anti join.
        """
        # GH 59435: raise when "how" is not a valid Merge type
        merge_type = {
            "left",
            "right",
            "inner",
            "outer",
            "left_anti",
            "right_anti",
            "cross",
            "asof",
        }
        if how not in merge_type:
            raise ValueError(
                f"'{how}' is not a valid Merge type: "
                f"left, right, inner, outer, left_anti, right_anti, cross, asof"
            )
        anti_join = False
        if how in {"left_anti", "right_anti"}:
            how = how.split("_")[0]  # type: ignore[assignment]
            anti_join = True
        how = cast("JoinHow | Literal['asof']", how)
        return how, anti_join

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
    # ... truncated

        def check2(exp, kwarg):
            result = merge(left, right, how="left", **kwarg)
            tm.assert_frame_equal(result, exp)
            result = merge(left, right, how="outer", **kwarg)
            tm.assert_frame_equal(result, exp)

            # TODO: should the next loop be un-indented? doing so breaks this test
            for kwarg in [
                {"left_index": True, "right_index": True},
                {"left_index": True, "right_on": "x"},
                {"left_on": "a", "right_index": True},
                {"left_on": "a", "right_on": "x"},
            ]:
                check1(exp_in, kwarg)
                check2(exp_out, kwarg)

def merge_ordered(
    left: DataFrame | Series,
    right: DataFrame | Series,
    on: IndexLabel | None = None,
    left_on: IndexLabel | None = None,
    right_on: IndexLabel | None = None,
    left_by=None,
    right_by=None,
    fill_method: str | None = None,
    suffixes: Suffixes = ("_x", "_y"),
    how: JoinHow = "outer",
) -> DataFrame:
    # ... truncated

    def _maybe_coerce_merge_keys(self) -> None:
        # we have valid merges but we may have to further
        # coerce these if they are originally incompatible types
        #
        # for example if these are categorical, but are not dtype_equal
        # or if we have object and integer dtypes

        for lk, rk, name in zip(
            self.left_join_keys, self.right_join_keys, self.join_names, strict=True
        ):
            if (len(lk) and not len(rk)) or (not len(lk) and len(rk)):
                continue
    # ... truncated

    def time_merge_dataframe_empty_right(self, sort):
        merge(self.left, self.right.iloc[:0], sort=sort)

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

        def _check_dtype_match(left: ArrayLike, right: ArrayLike, i: int) -> None:
            if left.dtype != right.dtype:
                if isinstance(left.dtype, CategoricalDtype) and isinstance(
                    right.dtype, CategoricalDtype
                ):
                    # The generic error message is confusing for categoricals.
                    #
                    # In this function, the join keys include both the original
                    # ones of the merge_asof() call, and also the keys passed
                    # to its by= argument. Unordered but equal categories
                    # are not supported for the former, but will fail
                    # later with a ValueError, so we don't *need* to check
                    # for them here.
                    msg = (
                        f"incompatible merge keys [{i}] {left.dtype!r} and "
                        f"{right.dtype!r}, both sides category, but not equal ones"
                    )
                else:
                    msg = (
                        f"incompatible merge keys [{i}] {left.dtype!r} and "
                        f"{right.dtype!r}, must be the same type"
                    )
                raise MergeError(msg)

    def time_merge_2intkey(self, sort):
        merge(self.left, self.right, sort=sort)

    def _get_merge_keys(
        self,
    ) -> tuple[
        list[ArrayLike],
        list[ArrayLike],
        list[Hashable],
        list[Hashable],
        list[Hashable],
    ]:
        """
    # ... truncated

    def time_merge(self, dtype, monotonic):
        merge(self.left, self.right)

    def time_merge(self, units, tz, monotonic):
        merge(self.left, self.right)

    def time_merge_dataframe_empty_left(self, sort):
        merge(self.left.iloc[:0], self.right, sort=sort)

    def time_unique_merge(self, unique_elements):
        merge(self.left, self.right, how="inner")

    def time_merge_object(self):
        merge(self.left_object, self.right_object, on="X")

    def time_merge_cat(self):
        merge(self.left_cat, self.right_cat, on="X")

    def merge(
        self,
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
    # ... truncated

    def time_merge_dataframes_cross(self, sort):
        merge(self.left.loc[:2000], self.right.loc[:2000], how="cross", sort=sort)

    def time_merge_ordered(self):
        merge_ordered(self.left, self.right, on="key", left_by="group")

    def time_merge_on_cat_col(self):
        merge(self.left_cat_col, self.right_cat_col, on="X")

    def time_merge_on_cat_idx(self):
        merge(self.left_cat_idx, self.right_cat_idx, on="X")

    def time_right_join_unsorted_right(self, n):
        self.left_sorted.merge(self.right_unsorted, on="k", how="right", sort=False)

    def time_merge_sorted_multiindex(self, dtypes, how):
        # copy to avoid MultiIndex._values caching
        df1 = self.df1.copy()
        df2 = self.df2.copy()
        merge(df1, df2, how=how, left_index=True, right_index=True)

    def _get_join_info(
        self,
    ) -> tuple[Index, npt.NDArray[np.intp] | None, npt.NDArray[np.intp] | None]:
        left_ax = self.left.index
        right_ax = self.right.index

        if self.left_index and self.right_index and self.how != "asof":
            join_index, left_indexer, right_indexer = left_ax.join(
                right_ax, how=self.how, return_indexers=True, sort=self.sort
            )

        elif self.right_index and self.how == "left":
    # ... truncated

    def time_i8merge(self, how):
        merge(self.left, self.right, how=how)

    def time_merge_dataframe_integer_2key(self, sort):
        merge(self.df, self.df3, sort=sort)

  {
   "cell_type": "markdown",
```
