# pandas-40 :: tacm-dyn

query: BUG: 27453 right merge order (#31278)

## selected nodes

- rank=1 layer=FILE tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=2 layer=CLASS tokens=555 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMerge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=3 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_groupby_and_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=4 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMerge.check1 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=5 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::merge_asof file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=6 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMerge.check2 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=7 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_dataframe_empty_right file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=8 layer=CLASS tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=9 layer=FUNCTION tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation.get_result file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=10 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_2intkey file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=11 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeEA.time_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=12 layer=FUNCTION tokens=304 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._indicator_pre_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=13 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=14 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeDatetime.time_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=15 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=16 layer=CLASS tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_multi.py::TestMergeMultiIndexNaN file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_multi.py
- rank=17 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.reorder_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=18 layer=CLASS tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_multi.py::TestMergeMulti file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_multi.py
- rank=19 layer=FUNCTION tokens=207 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_multi.py::TestMergeMulti.run_asserts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_multi.py
- rank=20 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::UniqueMerge.time_unique_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=21 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._indicator_post_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=22 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_object file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=23 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._validate_how file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=24 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=25 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/excel/test_writers.py::merge_cells file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/excel/test_writers.py

## context

```text
file core/reshape/merge.py
imports: __future__, datetime, functools, types, typing, warnings, numpy, pandas
defines: _MergeOperation, _CrossMergeOperation, _OrderedMerge, _AsOfMerge, merge, _cross_merge, _groupby_and_merge, merge_ordered, _merger, merge_asof, _maybe_promote_to_rangeindex, get_join_indexers, get_join_indexers_non_unique, restore_dropped_levels_multijoin, _convert_to_multiindex, _asof_by_function, _get_multiindex_indexer, _get_empty_indexer, _get_no_sort_one_missing_indexer, _left_join_on_index, _factorize_keys, _convert_arrays_and_get_rizer_klass, _sort_labels, _get_join_keys, _should_fill, _any, _validate_operand, _items_overlap_with_suffix, renamer

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

def _groupby_and_merge(
    by, left: DataFrame | Series, right: DataFrame | Series, merge_pieces
):
    """
    # ... truncated

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

    def time_merge_dataframe_empty_right(self, sort):
        merge(self.left, self.right.iloc[:0], sort=sort)

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

    def time_merge_2intkey(self, sort):
        merge(self.left, self.right, sort=sort)

    def time_merge(self, dtype, monotonic):
        merge(self.left, self.right)

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

    def time_merge(self, units, tz, monotonic):
        merge(self.left, self.right)

class DataFrame(NDFrame, OpsMixin):  [pandas/core/frame.py:269]
methods: T, _align_for_op, _append_internal, _arith_method
         _arith_method_with_reindex, _arith_op
         _box_col_values, _can_fast_transpose, _cmp_method
         _combine_frame, _construct_result, _constructor
         _constructor_from_mgr
         _constructor_sliced_from_mgr, _dict_round
         _dispatch_frame_op, _ensure_valid_index
         _flex_arith_method, _flex_cmp_method
         _from_arrays, _get_agg_axis, _get_column_array
         _get_data, _get_item, _get_value
         _get_values_for_csv, _getitem_bool_array
         _getitem_multilevel, _gotitem, _info_repr
         _is_homogeneous_type, _iset_item, _iset_item_mgr
         _iset_not_inplace, _iter_column_arrays, _ixs
         _maybe_align_series_as_frame, _reduce
         _reduce_axis1, _reindex_multi
         _replace_columnwise, _repr_fits_horizontal_
         _repr_fits_vertical_, _repr_html_
         _sanitize_column, _series, _series_round
         _set_item, _set_item_frame_value, _set_item_mgr
         _set_value, _setitem_array, _setitem_frame
         _setitem_slice, _should_reindex_frame_op
         _to_dict_of_blocks, _values, add, aggregate, all
         all, all, all, any, any, any, any, apply, assign
         axes, blk_func, c, check_int_infer_dtype, combine
         combine_first, combiner, compare, corr, corrwith
         count, cov, create_index, cummax, cummin, cumprod
         cumsum, diff, dot, dot, dot, drop, drop, drop
         drop, drop_duplicates, drop_duplicates
         drop_duplicates, drop_duplicates, dropna, dropna
         dropna, dtype_predicate, duplicated, eq, eval
         eval, eval, explode, f, f, floordiv, from_arrow
         from_dict, from_records, func, ge, groupby, gt
         idxmax, idxmin, igetitem, infer, info, insert
         isetitem, isin, isin_, isna, isnull, items
         iterrows, itertuples, join, kurt, kurt, kurt
         kurt, le, lt, map, max, max, max, max
         maybe_reorder, mean, mean, mean, mean, median
         median, median, median, melt, memory_usage, merge
         min, min, min, min, mod, mode, mul, ne, nlargest
         notna, notnull, nsmallest, nunique, pivot
         pivot_table, pop, pow, predicate, prod, quantile
         quantile, quantile, quantile, query, query, query
         query, radd, reindex, rename, rename, rename
         rename, reorder_levels, reset_index, reset_index
         reset_index, reset_index, rfloordiv, rmod, rmul
         round, rpow, rsub, rtruediv, select_dtypes, sem
         sem, sem, sem, set_axis, set_index, set_index
         set_index, shape, shift, skew, skew, skew, skew
         sort_index, sort_index, sort_index, sort_index
         sort_values, sort_values, sort_values, stack, std
         std, std, std, style, sub, sum, swaplevel
         to_dict, to_dict, to_dict, to_dict, to_dict
         to_feather, to_html, to_html, to_html, to_iceberg
         to_markdown, to_markdown, to_markdown
         to_markdown, to_numpy, to_orc, to_orc, to_orc
         to_orc, to_parquet, to_parquet, to_parquet
         to_period, to_records, to_series, to_stata
         to_string, to_string, to_string, to_timestamp
         to_xml, to_xml, to_xml, transform, transpose
         truediv, unstack, update, value_counts, values
         var, var, var, var, __arrow_c_stream__
         __dataframe__, __divmod__, __getitem__, __init__
         __len__, __matmul__, __matmul__, __matmul__
         __rdivmod__, __repr__, __rmatmul__, __setitem__

class TestMergeMultiIndexNaN:  [reshape/merge/test_multi.py:815]
methods: test_merge_multiindex_nan_left_index
         test_merge_multiindex_nan_right_index

    def reorder_levels(self, order: Sequence[int | str], axis: Axis = 0) -> DataFrame:
        """
        Rearrange index or column levels using input ``order``.

        May not drop or duplicate levels.

        Parameters
        ----------
        order : list of int or list of str
            List representing new level order. Reference level by number
            (position) or by key (label).
        axis : {0 or 'index', 1 or 'columns'}, default 0
    # ... truncated

class TestMergeMulti:  [reshape/merge/test_multi.py:75]
methods: bind_cols, expected, household, portfolio, run_asserts
         test_compress_group_combinations
         test_join_multi_levels, test_join_multi_levels2
         test_join_multi_levels_invalid
         test_join_multi_levels_merge_equivalence
         test_join_multi_levels_outer
         test_left_join_index_multi_match
         test_left_join_index_multi_match_multiindex
         test_left_join_index_preserve_order
         test_left_join_multi_index
         test_left_merge_na_buglet
         test_merge_datetime_index
         test_merge_datetime_multi_index_empty_df
         test_merge_multiple_cols_with_mixed_cols_index
         test_merge_na_keys, test_merge_on_multikey
         test_merge_right_vs_left

            def run_asserts(left, right, sort):
                res = left.join(right, on=icols, how="left", sort=sort)

                assert len(left) < len(res) + 1
                assert not res["4th"].isna().any()
                assert not res["5th"].isna().any()

                tm.assert_series_equal(res["4th"], -res["5th"], check_names=False)
                result = bind_cols(res.iloc[:, :-2])
                tm.assert_series_equal(res["4th"], result, check_names=False)
                assert result.name is None

                if sort:
                    tm.assert_frame_equal(res, res.sort_values(icols, kind="mergesort"))

                out = merge(left, right.reset_index(), on=icols, sort=sort, how="left")

                res.index = RangeIndex(len(res))
                tm.assert_frame_equal(out, res)

    def time_unique_merge(self, unique_elements):
        merge(self.left, self.right, how="inner")

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

    def time_merge_object(self):
        merge(self.left_object, self.right_object, on="X")

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

def merge_cells(request):
    return request.param
```
