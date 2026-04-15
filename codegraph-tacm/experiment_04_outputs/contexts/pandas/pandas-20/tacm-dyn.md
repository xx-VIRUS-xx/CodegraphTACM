# pandas-20 :: tacm-dyn

query: BUG: freq not retained on apply_index (#33779)

## selected nodes

- rank=1 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=2 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FUNCTION tokens=407 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_resample file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=4 layer=FUNCTION tokens=445 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_convert_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=5 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_GroupByMixin._apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=6 layer=FUNCTION tokens=248 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._can_fast_union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=7 layer=CLASS tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py::TestTimedeltaIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py
- rank=8 layer=CLASS tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=9 layer=FUNCTION tokens=297 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindow.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=10 layer=CLASS tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_month.py::TestSemiMonthEnd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_month.py
- rank=11 layer=CLASS tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_month.py::TestSemiMonthBegin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_month.py
- rank=12 layer=CLASS tokens=249 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py::TestDatetimeIndexSetOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py
- rank=13 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindow._insert_on_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=14 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=15 layer=CLASS tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_day.py::TestBusinessDay file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_business_day.py
- rank=16 layer=CLASS tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::TestSetitemViewCopySemantics file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=17 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=18 layer=FILE tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=19 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::_get_ordinal_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=20 layer=CLASS tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_fiscal.py::TestFY5253LastOfMonth file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_fiscal.py
- rank=21 layer=CLASS tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::NDFrameApply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py

## context

```text
file plotting/_matplotlib/timeseries.py
imports: __future__, functools, typing, numpy, pandas, datetime, matplotlib
defines: maybe_resample, _is_sub, _is_sup, _upsample_others, _replot_ax, decorate_axes, _get_ax_freq, _get_period_alias, _get_freq, use_dynamic_x, _get_index_freq, maybe_convert_index, _format_coord, format_dateaxis, prepare_ts_data

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

def maybe_resample(series: Series, ax: Axes, kwargs: dict[str, Any]):
    # resample against axes freq if necessary

    if "how" in kwargs:
        raise ValueError(
            "'how' is not a valid keyword for plotting functions. If plotting "
            "multiple objects on shared axes, resample manually first."
        )

    freq, ax_freq = _get_freq(ax, series)

    if freq is None:  # pragma: no cover
        raise ValueError("Cannot use dynamic axis without frequency info")

    # Convert DatetimeIndex to PeriodIndex so the x-axis uses Period ordinals.
    # For BDay freq this ensures consecutive business days get consecutive
    # ordinals with no weekend gaps (GH#1482).
    if isinstance(series.index, ABCDatetimeIndex):
        series = series.to_period(freq=freq)

    if ax_freq is not None and freq != ax_freq:
        if is_superperiod(freq, ax_freq):  # upsample input
            series = series.copy(deep=False)
            # error: "Index" has no attribute "asfreq"
            series.index = series.index.asfreq(  # type: ignore[attr-defined]
                ax_freq, how="s"
            )
            freq = ax_freq
        elif _is_sup(freq, ax_freq):  # one is weekly
            how = "last"
            series = getattr(series.resample("D"), how)().dropna()
            series = getattr(series.resample(ax_freq), how)().dropna()
            freq = ax_freq
        elif is_subperiod(freq, ax_freq) or _is_sub(freq, ax_freq):
            _upsample_others(ax, freq, kwargs)
        else:  # pragma: no cover
            raise ValueError("Incompatible frequency conversion")
    return freq, series

def maybe_convert_index(ax: Axes, data: NDFrameT) -> NDFrameT:
    # Convert DatetimeIndex to ordinal-integer index for plotting, so the
    # x-axis uses consecutive integers rather than matplotlib date2num floats.
    # This ensures evenly-spaced points: for BDay freq, Fri→Mon is a 1-unit
    # step rather than a 3-unit gap.  See GH#1482.
    if isinstance(data.index, (ABCDatetimeIndex, ABCPeriodIndex)):
        freq = _get_index_freq(data.index)

        if freq is None:
            freq = _get_ax_freq(ax)

        if freq is None:
            raise ValueError("Could not get frequency alias for plotting")

        freq_str = _get_period_alias(freq)

        if isinstance(data.index, ABCDatetimeIndex):
            if freq_str == "B":
                # Avoid creating deprecated Period[B]; use numpy business-day
                # arithmetic to map each timestamp to its business-day ordinal.
                data = data.copy(deep=False)
                data.index = Index(
                    np.busday_count(
                        np.datetime64("1970-01-01", "D"),
                        data.index.tz_localize(None).values.astype("datetime64[D]"),
                    ),
                    dtype=np.int64,
                )
            else:
                data = data.tz_localize(None).to_period(freq=freq_str)
        elif isinstance(data.index, ABCPeriodIndex):
            if freq_str == "B":
                # Extract the existing Period[B] ordinals as plain int64 to
                # avoid creating new (deprecated) Period[B] objects.
                data = data.copy(deep=False)
                data.index = Index(data.index.asi8, dtype=np.int64)
            else:
                data.index = data.index.asfreq(freq=freq_str, how="start")
    return data

    def _apply(self, f, *args, **kwargs):
        """
        Dispatch to _upsample; we are stripping all of the _upsample kwargs and
        performing the original function call on the grouped object.
        """

        def func(x):
            x = self._resampler_cls(x, timegrouper=self._timegrouper, gpr_index=self.ax)

            if isinstance(f, str):
                return getattr(x, f)(**kwargs)

            return x.apply(f, *args, **kwargs)

        result = self._groupby.apply(func)

        # GH 47705
        if (
            isinstance(result, ABCDataFrame)
            and len(result) == 0
            and not isinstance(result.index, PeriodIndex)
        ):
            result = result.set_index(
                _asfreq_compat(self.obj.index[:0], freq=self.freq), append=True
            )

        return self._wrap_result(result)

    def _can_fast_union(self, other: Self) -> bool:
        # Assumes that type(self) == type(other), as per the annotation
        # The ability to fast_union also implies that `freq` should be
        #  retained on union.
        freq = self.freq

        if freq is None or freq != other.freq:
            return False

        if not self.is_monotonic_increasing:
            # Because freq is not None, we must then be monotonic decreasing
            # TODO: do union on the reversed indexes?
            return False

        if len(self) == 0 or len(other) == 0:
            # only reached via union_many
            return True

        # to make our life easier, "sort" the two ranges
        if self[0] <= other[0]:
            left, right = self, other
        else:
            left, right = other, self

        right_start = right[0]
        left_end = left[-1]

        # Only need to "adjoin", not overlap
        return (right_start == left_end + freq) or right_start in left

class TestTimedeltaIndex:  [indexes/timedeltas/test_setops.py:17]
methods: test_intersection, test_intersection_bug_1708
         test_intersection_equal
         test_intersection_non_monotonic
         test_intersection_zero_length, test_union
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_freq_infer, test_union_sort_false
         test_zero_length_input_index

class BaseWindow(SelectionMixin):  [core/window/rolling.py:116]
methods: _apply, _apply_columnwise, _apply_pairwise, _apply_series
         _apply_tablewise, _check_window_bounds
         _create_data, _dir_additions, _get_window_indexer
         _gotitem, _index_array, _insert_on_column
         _make_numeric_only, _numba_apply, _prep_values
         _resolve_output, _slice_axis_for_step, _validate
         _validate_numeric_only, aggregate, calc
         homogeneous_func, __getattr__, __init__, __iter__
         __repr__

    def __init__(
        self,
        obj: NDFrame,
        window=None,
        min_periods: int | None = None,
        center: bool | None = False,
        win_type: str | None = None,
        on: str | Index | None = None,
        closed: str | None = None,
        step: int | None = None,
        method: str = "single",
        *,
        selection=None,
    ) -> None:
        self.obj = obj
        self.on = on
        self.closed = closed
        self.step = step
        self.window = window
        self.min_periods = min_periods
        self.center = center
        self.win_type = win_type
        self.method = method
        self._win_freq_i8: int | None = None
        if self.on is None:
            self._on = self.obj.index
        elif isinstance(self.on, Index):
            self._on = self.on
        elif isinstance(self.obj, ABCDataFrame) and self.on in self.obj.columns:
            self._on = Index(self.obj[self.on])
        else:
            raise ValueError(
                f"invalid on specified as {self.on}, "
                "must be a column (of DataFrame), an Index or None"
            )

        self._selection = selection
        self._validate()

class TestSemiMonthEnd:  [tseries/offsets/test_month.py:35]
methods: test_apply_index, test_is_on_offset, test_offset
         test_offset_whole_year
         test_vectorized_offset_addition

class TestSemiMonthBegin:  [tseries/offsets/test_month.py:286]
methods: test_apply_index, test_is_on_offset, test_offset
         test_offset_whole_year
         test_vectorized_offset_addition

class TestDatetimeIndexSetOps:  [indexes/datetimes/test_setops.py:33]
methods: test_datetimeindex_diff, test_difference
         test_difference_freq, test_dti_intersection
         test_dti_setop_aware, test_dti_union_mixed
         test_intersection, test_intersection2
         test_intersection_bug_1708
         test_intersection_empty
         test_intersection_non_tick_no_fastpath
         test_intersection_same_timezone_different_units
         test_setops_preserve_freq
         test_symmetric_difference_same_timezone_different_units
         test_union, test_union2, test_union3
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_dataframe_index
         test_union_different_dates_same_timezone_different_units
         test_union_freq_both_none, test_union_freq_infer
         test_union_same_nonzero_timezone_different_units
         test_union_same_timezone_different_units
         test_union_with_DatetimeIndex

    def _insert_on_column(self, result: DataFrame, obj: DataFrame) -> None:
        # if we have an 'on' column we want to put it back into
        # the results in the same location
        from pandas import Series

        if self.on is not None and not self._on.equals(obj.index):
            name = self._on.name
            extra_col = Series(self._on, index=self.obj.index, name=name, copy=False)
            if name in result.columns:
                # TODO: sure we want to overwrite results?
                result[name] = extra_col
            elif name in result.index.names:
                pass
            elif name in self._selected_obj.columns:
                # insert in the same location as we had in _selected_obj
                old_cols = self._selected_obj.columns
                new_cols = result.columns
                old_loc = old_cols.get_loc(name)
                overlap = new_cols.intersection(old_cols[:old_loc])
                new_loc = len(overlap)
                result.insert(new_loc, name, extra_col)
            else:
                # insert at the end
                result[name] = extra_col

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

class TestBusinessDay:  [tseries/offsets/test_business_day.py:55]
methods: testRollback1, testRollback2, testRollforward1
         testRollforward2, test_add_datetime, test_apply
         test_apply_corner, test_apply_large_n
         test_different_normalize_equals, test_eq
         test_hash, test_is_on_offset, test_repr
         test_roll_date_object, test_with_offset
         test_with_offset_index

class TestSetitemViewCopySemantics:  [series/indexing/test_setitem.py:419]
methods: test_dt64tz_setitem_does_not_mutate_dti
         test_setitem_invalidates_datetime_index_freq

def _get_index_freq(index: Index) -> BaseOffset | None:
    freq = getattr(index, "freq", None)
    if freq is None:
        freq = getattr(index, "inferred_freq", None)
        freq = to_offset(freq)
    return freq

file core/arrays/period.py
imports: __future__, datetime, operator, typing, warnings, numpy, pandas
defines: PeriodArray, _field_accessor, f, raise_on_incompatible, period_array, validate_dtype_freq, dt64arr_to_periodarr, _get_ordinal_range, _range_from_fields, _make_field_arrays

def _get_ordinal_range(start, end, periods, freq, mult: int = 1):
    if com.count_not_none(start, end, periods) != 2:
        raise ValueError(
            "Of the three parameters: start, end, and periods, "
            "exactly two must be specified"
        )

    if freq is not None:
        freq = to_offset(freq, is_period=True)
        mult = freq.n

    if start is not None:
    # ... truncated

class TestFY5253LastOfMonth:  [tseries/offsets/test_fiscal.py:54]
methods: test_apply, test_is_on_offset

class NDFrameApply(Apply):  [pandas/core/apply.py:809]
methods: agg_axis, agg_or_apply_dict_like, agg_or_apply_list_like
         index
```
