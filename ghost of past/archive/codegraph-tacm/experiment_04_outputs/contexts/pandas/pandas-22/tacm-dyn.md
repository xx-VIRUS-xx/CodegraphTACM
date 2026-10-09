# pandas-22 :: tacm-dyn

query: BUG: support count function for custom BaseIndexer rolling windows (#33605)

## selected nodes

- rank=1 layer=FILE tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=2 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::CustomIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=3 layer=CLASS tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=4 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=5 layer=FILE tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py
- rank=6 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::PrescribedWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=7 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=8 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=9 layer=CLASS tokens=459 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py::TestRolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py
- rank=10 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=11 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py::is_platform_windows file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py
- rank=12 layer=FILE tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=13 layer=CLASS tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::FixedForwardWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=14 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::BaseIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=15 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=16 layer=CLASS tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=17 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::BaseIndexer.get_window_bounds file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=18 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::tests_empty_df_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=19 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::Apply.time_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=20 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=21 layer=CLASS tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::AggEngine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=22 layer=CLASS tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::TransformEngine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=23 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomSeries.custom_series_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py
- rank=24 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomDataFrame.custom_frame_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py
- rank=25 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=26 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=27 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py::rolling_aggregation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py
- rank=28 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=29 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py::TestRolling.func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py
- rank=30 layer=FILE tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/numba_.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/numba_.py
- rank=31 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::AggEngine.function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=32 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=33 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::FixedWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py

## context

```text
file core/window/rolling.py
imports: __future__, copy, datetime, functools, inspect, typing, numpy, pandas
defines: BaseWindow, BaseWindowGroupby, Window, RollingAndExpandingMixin, Rolling, RollingGroupby

class CustomIndexer(BaseIndexer):  [tests/window/test_rolling.py:1354]
methods: get_window_bounds

class Rolling(RollingAndExpandingMixin):  [core/window/rolling.py:1979]
methods: _raise_monotonic_error, _validate
         _validate_datetimelike_monotonic, aggregate
         apply, corr, count, cov, first, kurt, last, max
         mean, median, min, nunique, pipe, pipe, pipe
         quantile, rank, sem, skew, std, sum, var

    def count(self, numeric_only: bool = False):
        """
        Calculate the rolling count of non NaN observations.

        This is useful for identifying windows with missing data, as it counts
        only non-NaN entries within each window.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns.

    # ... truncated

file pandas/compat/__init__.py
imports: __future__, platform, sys, typing, pandas
defines: set_function_name, is_platform_little_endian, is_platform_windows, is_platform_linux, is_platform_mac, is_platform_arm, is_platform_power, is_platform_riscv64

class PrescribedWindowIndexer(BaseIndexer):  [tests/window/test_rolling.py:2055]
methods: get_window_bounds, __init__

    def aggregate(self, func=None, *args, **kwargs):
        """
        Aggregate using one or more operations over the specified axis.

        This method allows combining multiple aggregation functions (e.g.
        ``'sum'``, ``'mean'``) in a single call, returning a result for each
        function applied to each rolling window.

        Parameters
        ----------
        func : function, str, list or dict
            Function to use for aggregating the data. If a function, must either
    # ... truncated

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

class TestRolling:  [tests/window/test_groupby.py:52]
methods: func, func, isnumpyarray, test_as_index_false
         test_by_column_not_in_values
         test_datelike_on_monotonic_within_each_group
         test_datelike_on_not_monotonic_within_each_group
         test_getitem, test_getitem_multiple
         test_groupby_level, test_groupby_monotonic
         test_groupby_rolling
         test_groupby_rolling_agg_namedagg
         test_groupby_rolling_center_center
         test_groupby_rolling_center_min_periods
         test_groupby_rolling_center_on
         test_groupby_rolling_count_closed_on
         test_groupby_rolling_custom_indexer
         test_groupby_rolling_empty_frame
         test_groupby_rolling_group_keys
         test_groupby_rolling_index_changed
         test_groupby_rolling_index_level_and_column_label
         test_groupby_rolling_nans_in_index
         test_groupby_rolling_no_sort
         test_groupby_rolling_non_monotonic
         test_groupby_rolling_object_doesnt_affect_groupby_apply
         test_groupby_rolling_resulting_multiindex
         test_groupby_rolling_resulting_multiindex2
         test_groupby_rolling_resulting_multiindex3
         test_groupby_rolling_sem
         test_groupby_rolling_string_index
         test_groupby_rolling_subset_with_closed
         test_groupby_rolling_var
         test_groupby_subselect_rolling
         test_groupby_subset_rolling_subset_with_closed
         test_groupby_unsupported_argument
         test_nan_and_zero_endpoints, test_rolling
         test_rolling_apply, test_rolling_apply_mutability
         test_rolling_corr_cov_other_diff_size_as_groups
         test_rolling_corr_cov_other_same_size_as_groups
         test_rolling_corr_cov_pairwise
         test_rolling_corr_cov_unordered
         test_rolling_ddof, test_rolling_quantile

    def rolling(
        self,
        window: int | dt.timedelta | str | BaseOffset | BaseIndexer,
        min_periods: int | None = None,
        center: bool = False,
        win_type: str | None = None,
        on: str | None = None,
        closed: IntervalClosedType | None = None,
        step: int | None = None,
        method: str = "single",
    ) -> Window | Rolling:
        """
    # ... truncated

def is_platform_windows() -> bool:
    """
    Checking if the running platform is windows.

    Returns
    -------
    bool
        True if the running platform is windows.
    """
    return sys.platform in ["win32", "cygwin"]

file core/indexers/objects.py
imports: __future__, datetime, numpy, pandas
defines: BaseIndexer, FixedWindowIndexer, VariableWindowIndexer, VariableOffsetWindowIndexer, ExpandingIndexer, FixedForwardWindowIndexer, GroupbyIndexer, ExponentialMovingWindowIndexer

class FixedForwardWindowIndexer(BaseIndexer):  [core/indexers/objects.py:429]
methods: get_window_bounds

class BaseIndexer:  [core/indexers/objects.py:21]
methods: get_window_bounds, __init__

    def rolling(
        self,
        window: int | datetime.timedelta | str | BaseOffset | BaseIndexer,
        min_periods: int | None = None,
        center: bool = False,
        win_type: str | None = None,
        on: str | None = None,
        closed: IntervalClosedType | None = None,
        method: str = "single",
    ) -> RollingGroupby:
        """
    # ... truncated

class RollingAndExpandingMixin(BaseWindow):  [core/window/rolling.py:1537]
methods: _generate_cython_apply_func, apply, apply_func, corr
         corr_func, count, cov, cov_func, first, kurt
         last, max, mean, median, min, nunique, pipe, pipe
         pipe, quantile, rank, sem, skew, std, sum, var
         zsqrt_func

    def get_window_bounds(
        self,
        num_values: int = 0,
        min_periods: int | None = None,
        center: bool | None = None,
        closed: str | None = None,
        step: int | None = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Computes the bounds of a window.

        Parameters
        ----------
        num_values : int, default 0
            number of values that will be aggregated over
        min_periods : int, default None
            min_periods passed from the top level rolling API
        center : bool, default None
            center passed from the top level rolling API
        closed : str, default None
            closed passed from the top level rolling API
        step : int, default None
            step passed from the top level rolling API

        Returns
        -------
        A tuple of ndarray[int64]s, indicating the boundaries of each
        window
        """
        raise NotImplementedError

def tests_empty_df_rolling(roller):
    # GH 15819 Verifies that datetime and integer rolling windows can be
    # applied to empty DataFrames
    expected = DataFrame()
    result = DataFrame().rolling(roller).sum()
    tm.assert_frame_equal(result, expected)

    # Verifies that datetime and integer rolling windows can be applied to
    # empty DataFrames with datetime index
    expected = DataFrame(index=DatetimeIndex([]))
    result = DataFrame(index=DatetimeIndex([])).rolling(roller).sum()
    tm.assert_frame_equal(result, expected)

    def time_rolling(self, constructor, window, dtype, function, raw):
        self.roll.apply(function, raw=raw)

    def count(self, axis: Axis = 0, numeric_only: bool = False) -> Series:
        """
        Count non-NA cells for each column or row.

        The values `None`, `NaN`, `NaT`, ``pandas.NA`` are considered NA.

        Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns'}, default 0
            If 0 or 'index' counts are generated for each column.
            If 1 or 'columns' counts are generated for each row.
        numeric_only : bool, default False
    # ... truncated

class AggEngine:  [asv_bench/benchmarks/groupby.py:1048]
methods: function, function, function, function, setup
         time_dataframe_cython, time_dataframe_numba
         time_series_cython, time_series_numba

class TransformEngine:  [asv_bench/benchmarks/groupby.py:1006]
methods: function, function, function, function, setup
         time_dataframe_cython, time_dataframe_numba
         time_series_cython, time_series_numba

            def custom_series_function(self):
                return "OK"

            def custom_frame_function(self):
                return "OK"

class Series(base.IndexOpsMixin, NDFrame):  # type: ignore[misc]  [pandas/core/series.py:211]
methods: _align_for_op, _append_internal, _arith_method, _binop
         _can_hold_na, _cmp_method, _construct_result
         _construct_result, _construct_result
         _constructor, _constructor_expanddim
         _constructor_expanddim_from_mgr
         _constructor_from_mgr, _flex_method
         _get_rows_with_mask, _get_value
         _get_values_tuple, _get_with, _gotitem
         _init_dict, _ixs, _logical_method
         _needs_reindex_multi, _reduce, _references
         _reindex_indexer, _set_labels, _set_name
         _set_value, _set_values, _set_with
         _set_with_engine, _slice, _values, add, aggregate
         all, any, apply, argsort, array, autocorr, axes
         between, case_when, combine, combine_first
         compare, corr, count, cov, cummax, cummin
         cumprod, cumsum, diff, divmod, dot, drop, drop
         drop, drop, drop_duplicates, drop_duplicates
         drop_duplicates, drop_duplicates, dropna, dropna
         dropna, dtype, dtypes, duplicated, eq, explode
         floordiv, from_arrow, ge, groupby, gt, idxmax
         idxmin, info, isin, isna, isnull, items, keys
         kurt, le, lt, map, max, mean, median
         memory_usage, min, mod, mode, mul, name, name, ne
         nlargest, notna, notnull, nsmallest, pop, pow
         prod, quantile, quantile, quantile, quantile
         radd, rdivmod, reindex, rename, rename, rename
         rename_axis, rename_axis, rename_axis
         rename_axis, reorder_levels, repeat, reset_index
         reset_index, reset_index, reset_index, rfloordiv
         rmod, rmul, round, rpow, rsub, rtruediv
         searchsorted, sem, set_axis, skew, sort_index
         sort_index, sort_index, sort_index, sort_values
         sort_values, sort_values, sort_values, std, sub
         sum, swaplevel, to_dict, to_dict, to_dict
         to_frame, to_markdown, to_markdown, to_markdown
         to_markdown, to_period, to_string, to_string
         to_string, to_timestamp, transform, truediv
         unique, unstack, update, values, var, __array__
         __arrow_c_stream__, __getitem__, __init__
         __len__, __matmul__, __repr__, __rmatmul__
         __setitem__

    def count(self) -> int:
        """
        Return number of non-NA/null observations in the Series.

        This method counts the number of elements that are not missing
        (i.e., not NaN or None) in the Series.

        Returns
        -------
        int
            Number of non-null values in the Series.

        See Also
        --------
        DataFrame.count : Count non-NA cells for each column or row.

        Examples
        --------
        >>> s = pd.Series([0.0, 1.0, np.nan])
        >>> s.count()
        2
        """
        return maybe_unbox_numpy_scalar(notna(self._values).sum().astype("int64"))

def rolling_aggregation(request):
    """Make a rolling aggregation function as fixture."""
    return request.param

file pandas/core/frame.py
imports: __future__, collections, functools, io, itertools, operator, sys, typing
defines: DataFrame, _from_nested_dict, _reindex_for_setitem

        def func(x):
            return getattr(x.B.rolling(4), f)(pairwise=True)

file core/util/numba_.py
imports: __future__, inspect, types, typing, numpy, pandas, collections, numba
defines: maybe_use_numba, set_use_numba, get_jit_arguments, jit_user_function, prepare_function_arguments

        def function(values):
            total = 0
            for i, value in enumerate(values):
                if i % 2:
                    total += value + 5
                else:
                    total += value * 2
            return total

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

class FixedWindowIndexer(BaseIndexer):  [core/indexers/objects.py:108]
methods: get_window_bounds
```
