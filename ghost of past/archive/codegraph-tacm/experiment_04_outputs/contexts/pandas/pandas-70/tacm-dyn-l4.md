# pandas-70 :: tacm-dyn-l4

query: BUG: regression when applying groupby aggregation on categorical columns (#31359)

## selected nodes

- rank=1 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py
- rank=2 layer=CLASS tokens=385 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_grouping.py::TestGrouping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_grouping.py
- rank=3 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py::recode_for_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py
- rank=4 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._groupby_and_aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=5 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::get_resampler_for_grouping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=6 layer=CLASS tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_describe.py::TestDataFrameDescribe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_describe.py
- rank=7 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::groupby_func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py
- rank=8 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=9 layer=CLASS tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=10 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical.tests_merge_categorical_unordered_equal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=11 layer=CLASS tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_getitem.py::TestGetitemBooleanMask file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_getitem.py
- rank=12 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py::_get_dataframe_dtype_counts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py
- rank=13 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py::get_categorical_invalid_expected file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py
- rank=14 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=15 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.select_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=16 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=17 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataWriter._prepare_categoricals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=18 layer=CLASS tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_parquet.py::TestParquetFastParquet file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_parquet.py
- rank=19 layer=CLASS tokens=459 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py::TestRolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py
- rank=20 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py::rolling_aggregation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py
- rank=21 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py::FromDicts.time_nested_dict_int64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py
- rank=22 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical._groupby_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=23 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_categorical.py::df_cat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_categorical.py
- rank=24 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::GroupStrings file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=25 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::GroupStrings.time_multi_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=26 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::SumBools.time_groupby_sum_booleans file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py

## context

```text
file core/groupby/categorical.py
imports: __future__, numpy, pandas
defines: recode_for_groupby

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

def groupby_func(request):
    """yields both aggregation and transformation functions."""
    return request.param

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

class TestGetitemBooleanMask:  [frame/indexing/test_getitem.py:338]
methods: df_dup_cols, test_getitem_bool_mask_categorical_index
         test_getitem_bool_mask_duplicate_columns_mixed_dtypes
         test_getitem_boolean_frame_unaligned_with_duplicate_columns
         test_getitem_boolean_frame_with_duplicate_columns
         test_getitem_boolean_series_with_duplicate_columns
         test_getitem_empty_frame_with_boolean
         test_getitem_frozenset_unique_in_column
         test_getitem_returns_view_when_column_is_unique_in_df

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

    def __getitem__(self, key):
        check_dict_or_set_indexers(key)
        key = lib.item_from_zerodim(key)
        key = com.apply_if_callable(key, self)

        if is_hashable(key, allow_slice=False) and not is_iterator(key):
            # is_iterator to exclude generator e.g. test_getitem_listlike
            # As of Python 3.12, slice is hashable which breaks MultiIndex (GH#57500)

            # Shortcut: return single column as Series when key refers to one column.
            # Previously we used "key in self.columns.drop_duplicates(keep=False)",
            # which built a new Index on every access when columns had duplicates.
    # ... truncated

    def _prepare_categoricals(self, data: DataFrame) -> DataFrame:
        """
        Check for categorical columns, retain categorical information for
        Stata file and convert categorical data to int
        """
    # ... truncated

class TestParquetFastParquet(Base):  [tests/io/test_parquet.py:1275]
methods: test_basic, test_bool_with_none, test_bytes_file_name
         test_categorical
         test_close_file_handle_on_read_error
         test_columns_dtypes_invalid
         test_duplicate_columns, test_empty_dataframe
         test_error_on_using_partition_cols_and_partition_on
         test_filesystem_notimplemented
         test_filter_row_groups
         test_invalid_dtype_backend
         test_invalid_filesystem
         test_partition_cols_string
         test_partition_cols_supported
         test_partition_on_supported, test_s3_roundtrip
         test_timezone_aware_index, test_unsupported
         test_unsupported_pa_filesystem_storage_options

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

class GroupStrings:  [asv_bench/benchmarks/groupby.py:343]
methods: setup, time_multi_columns

# --- Layer 04: Variable context ---
# call-chain context
  called by: __init__ [grouper.py]

# call-chain context
  called by: aggregate [resample.py]
  called by: _downsample [resample.py]

# call-chain context
  called by: resample [groupby.py]

# call-chain context
  called by: dtype_counts [info.py]
  called by: dtype_counts [info.py]

# call-chain context
  called by: time_select_dtype_int_include [dtypes.py]
  called by: time_select_dtype_int_exclude [dtypes.py]

# call-chain context
  called by: check_indexing_smoketest_or_raises [common.py]

# call-chain context
  called by: _prepare_pandas [stata.py]

# call-chain context
  called by: cython_operation [ops.py]

# call-chain context
  called by: transform_dict_like [apply.py]
  called by: compute_list_like [apply.py]

```
