# pandas-95 :: tacm-dyn-l4

query: BUG: PeriodArray comparisons inconsistent with Period comparisons (#30722)

## selected nodes

- rank=1 layer=FILE tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=2 layer=CLASS tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_operators.py::TestCategoricalOpsWithFactor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_operators.py
- rank=3 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::DataFramePeriodColumn.time_set_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=4 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::period_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=5 layer=FILE tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py
- rank=6 layer=CLASS tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::TestTimedelta64ArrayComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=7 layer=CLASS tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_object.py::TestObjectComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_object.py
- rank=8 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_daily_finder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py
- rank=9 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=10 layer=CLASS tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetime64SeriesComparison file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=11 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::TestComparison.interval_constructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py
- rank=12 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py::OffsetWithNamespace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py
- rank=13 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_comparisons.py::Inf file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
- rank=14 layer=FUNCTION tokens=232 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py::check_for_inconsistent_pandas_namespace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py
- rank=15 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=16 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=17 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.asfreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=18 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._series_round file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=19 layer=CLASS tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_arithmetic.py::TestSeriesComparison file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_arithmetic.py
- rank=20 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._add_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=21 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=22 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimePeriodArrToDT64Arr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=23 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py::expected_with_na_handling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py
- rank=24 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=25 layer=CLASS tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_arithmetic.py::TestFrameArithmeticUnsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_arithmetic.py
- rank=26 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimePeriodArrToDT64Arr.time_periodarray_to_dt64arr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=27 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::raise_on_incompatible file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=28 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=29 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=30 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=31 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=32 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._check_compatible_with file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=33 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._scalar_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py

## context

```text
file core/arrays/period.py
imports: __future__, datetime, operator, typing, warnings, numpy, pandas
defines: PeriodArray, _field_accessor, f, raise_on_incompatible, period_array, validate_dtype_freq, dt64arr_to_periodarr, _get_ordinal_range, _range_from_fields, _make_field_arrays

class TestCategoricalOpsWithFactor:  [arrays/categorical/test_operators.py:15]
methods: test_categories_none_comparisons, test_comparisons

    def time_set_index(self):
        # GH#21582 limited by comparisons of Period objects
        self.df["col2"] = self.rng
        self.df.set_index("col2", append=True)

def period_array(
    data: Sequence[Period | str | None] | AnyArrayLike,
    dtype: PeriodDtype | None = None,
) -> PeriodArray:
    """
    # ... truncated

file pandas/scripts/check_for_inconsistent_pandas_namespace.py
imports: argparse, ast, collections, sys, typing, tokenize_rt
defines: OffsetWithNamespace, Visitor, replace_inconsistent_pandas_namespace, check_for_inconsistent_pandas_namespace, main

class TestTimedelta64ArrayComparisons:  [tests/arithmetic/test_timedelta64.py:170]
methods: test_comp_nat, test_comparisons_coverage
         test_comparisons_nat

class TestObjectComparisons:  [tests/arithmetic/test_object.py:26]
methods: test_comp_nat_object_dtype
         test_comparison_object_numeric_nas
         test_more_na_comparisons, test_object_comparisons

def _daily_finder(vmin: float, vmax: float, freq: BaseOffset) -> np.ndarray:
    # error: "BaseOffset" has no attribute "_period_dtype_code"
    dtype_code = freq._period_dtype_code  # type: ignore[attr-defined]
    freq_group = FreqGroup.from_period_dtype_code(dtype_code)

    periodsperday, periodspermonth, periodsperyear = _get_periods_per_ymd(freq)

    # When the frequency has a multiplier n > 1 (e.g. '1000ms' instead of
    # '1ms'), the period_range below steps by n, so span is n times smaller
    # than the raw ordinal count.  Adjust the per-day/month/year counts to
    # match so that the threshold comparisons remain correct.  GH#50355
    n = freq.n
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

class TestDatetime64SeriesComparison:  [tests/arithmetic/test_datetime64.py:158]
methods: test_dt64_compare_datetime_scalar
         test_dt64arr_timestamp_equality
         test_nat_comparisons, test_nat_comparisons_scalar
         test_series_comparison_scalars
         test_timestamp_compare_series
         test_ts_series_numpy_maximum

    def interval_constructor(self, request):
        """
        Fixture for all pandas native interval constructors.
        To be used as the LHS of IntervalArray comparisons.
        """
        return request.param

class OffsetWithNamespace(NamedTuple):  [pandas/scripts/check_for_inconsistent_pandas_namespace.py:37]
methods: —

class Inf:  [scalar/timestamp/test_comparisons.py:290]
methods: __eq__, __ge__, __gt__, __le__, __lt__

def check_for_inconsistent_pandas_namespace(
    content: str, path: str, *, replace: bool
) -> str | None:
    tree = ast.parse(content)

    visitor = Visitor()
    visitor.visit(tree)

    inconsistencies = visitor.imported_from_pandas.intersection(
        visitor.pandas_namespace.values()
    )

    if not inconsistencies:
        # No inconsistent namespace usage, nothing to replace.
        return None

    if not replace:
        inconsistency = inconsistencies.pop()
        lineno, col_offset, prefix = next(
            key for key, val in visitor.pandas_namespace.items() if val == inconsistency
        )
        msg = ERROR_MESSAGE.format(
            lineno=lineno,
            col_offset=col_offset,
            prefix=prefix,
            name=inconsistency,
            path=path,
        )
        sys.stdout.write(msg)
        sys.exit(1)

    return replace_inconsistent_pandas_namespace(visitor, content)

    def to_period(self, freq=None) -> PeriodArray:
        """
        Cast to PeriodArray/PeriodIndex at a particular frequency.

        Converts DatetimeArray/Index to PeriodArray/PeriodIndex.

        Parameters
        ----------
        freq : str or Period, optional
            One of pandas' :ref:`period aliases <timeseries.period_aliases>`
            or a Period object. Will be inferred by default.

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

    def asfreq(self, freq=None, how: str = "E") -> Self:
        """
        Convert the PeriodArray to the specified frequency `freq`.

        Equivalent to applying :meth:`pandas.Period.asfreq` with the given arguments
        to each :class:`~pandas.Period` in this PeriodArray.

        Parameters
        ----------
        freq : str
            A frequency.
        how : str {'E', 'S'}, default 'E'
    # ... truncated

        def _series_round(ser: Series, decimals: int) -> Series:
            if is_integer_dtype(ser.dtype) or is_float_dtype(ser.dtype):
                return ser.round(decimals)
            elif isinstance(ser._values, (DatetimeArray, TimedeltaArray, PeriodArray)):
                # GH#57781
                # TODO: also the ArrowDtype analogues?
                warnings.warn(
                    "obj.round has no effect with datetime, timedelta, "
                    "or period dtypes. Use obj.dt.round(...) instead.",
                    UserWarning,
                    stacklevel=find_stack_level(),
                )
            return ser

class TestSeriesComparison:  [tests/series/test_arithmetic.py:556]
methods: test_categorical_comparisons, test_comp_ops_df_compat
         test_compare_series_interval_keyword
         test_comparison_different_length
         test_comparison_frozenset
         test_comparison_operators_with_nas
         test_comparison_tuples, test_comparisons, test_ne
         test_ser_cmp_result_names
         test_ser_flex_cmp_return_dtypes
         test_ser_flex_cmp_return_dtypes_empty
         test_unequal_categorical_comparison_raises_type_error

    def _add_period(self, other: Period) -> PeriodArray:
        if not lib.is_np_dtype(self.dtype, "m"):
            raise TypeError(f"cannot add Period to a {type(self).__name__}")

        # We will wrap in a PeriodArray and defer to the reversed operation
        from pandas.core.arrays.period import PeriodArray

        i8vals = np.broadcast_to(other.ordinal, self.shape)
        dtype = PeriodDtype(other.freq)
        parr = PeriodArray(i8vals, dtype=dtype)
        return parr + self

    def to_period(self, freq=None) -> PeriodIndex:
        """
        Cast to PeriodArray/PeriodIndex at a particular frequency.

        Converts DatetimeArray/Index to PeriodArray/PeriodIndex.

        Parameters
        ----------
        freq : str or Period, optional
            One of pandas' :ref:`period aliases <timeseries.period_aliases>`
            or a Period object. Will be inferred by default.

    # ... truncated

class TimePeriodArrToDT64Arr:  [benchmarks/tslibs/period.py:126]
methods: setup, time_periodarray_to_dt64arr

    def expected_with_na_handling(lvalues, rvalues, op):
        # Similar to comparison_op, handle zerodim arrays with na value separately
        if (rvalues.ndim == 0) and isna(rvalues.item()):
            # numpy does not like comparisons vs None
            if op is operator.ne:
                return np.ones(lvalues.shape, dtype=bool)
            else:
                return np.zeros(lvalues.shape, dtype=bool)
        return op(lvalues, rvalues)

    def astype(self, dtype, copy: bool = True):
        # Some notes on cases we don't have to handle here in the base class:
        #   1. PeriodArray.astype handles period -> period
        #   2. DatetimeArray.astype handles conversion between tz.
        #   3. DatetimeArray.astype handles datetime -> period
        dtype = pandas_dtype(dtype)

        if dtype == object:
            if self.dtype.kind == "M":
                self = cast("DatetimeArray", self)
                # *much* faster than self._box_values
                #  for e.g. test_get_loc_tuple_monotonic_above_size_cutoff
    # ... truncated

class TestFrameArithmeticUnsorted:  [tests/frame/test_arithmetic.py:1301]
methods: test_add_with_dti_mismatched_tzs, test_align_frame
         test_align_int_fill_bug
         test_alignment_non_pandas
         test_alignment_non_pandas_index_columns
         test_alignment_non_pandas_length_mismatch
         test_binary_ops_align
         test_binary_ops_align_series_dataframe
         test_boolean_comparison, test_combineFrame
         test_combineFunc, test_combine_series
         test_combine_timeseries
         test_comparison_protected_from_errstate
         test_comparisons, test_dunder_methods_binary
         test_frame_add_tz_mismatch_converts_to_utc
         test_inplace_ops_alignment
         test_inplace_ops_identity
         test_inplace_ops_identity2
         test_logical_typeerror_with_non_valid
         test_no_warning, test_operators_none_as_na
         test_strings_to_numbers_comparisons_raises

    def time_periodarray_to_dt64arr(self, size, freq):
        periodarr_to_dt64arr(self.i8values, freq)

def raise_on_incompatible(left, right) -> IncompatibleFrequency:
    """
    Helper function to render a consistent error message when raising
    IncompatibleFrequency.

    Parameters
    ----------
    left : PeriodArray
    right : None, DateOffset, Period, ndarray, or timedelta-like

    Returns
    -------
    IncompatibleFrequency
        Exception to be raised by the caller.
    """
    # GH#24283 error message format depends on whether right is scalar
    if isinstance(right, (np.ndarray, ABCTimedeltaArray)) or right is None:
        other_freq = None
    elif isinstance(right, BaseOffset):
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore", r"PeriodDtype\[B\] is deprecated", category=FutureWarning
            )
            other_freq = PeriodDtype(right)._freqstr
    elif isinstance(right, (ABCPeriodIndex, PeriodArray, Period)):
        other_freq = right.freqstr
    else:
        other_freq = delta_to_tick(Timedelta(right)).freqstr

    own_freq = PeriodDtype(left.freq)._freqstr
    msg = DIFFERENT_FREQ.format(
        cls=type(left).__name__, own_freq=own_freq, other_freq=other_freq
    )
    return IncompatibleFrequency(msg)

    def to_period(
        self,
        freq: Frequency | None = None,
        axis: Axis = 0,
        copy: bool | lib.NoDefault = lib.no_default,
    ) -> DataFrame:
        """
    # ... truncated

file core/indexes/period.py
imports: __future__, datetime, typing, numpy, pandas, collections
defines: PeriodIndex, _new_PeriodIndex, period_range

    def len(self, text: str) -> int:
        return len(text)

# --- Layer 04: Variable context ---
# call-chain context
  called by: __new__ [period.py]

# call-chain context
  called by: main [check_for_inconsistent_pandas_namespace.py]

# call-chain context
  called by: setup [gil.py]
  called by: run [gil.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: time_asfreq [period.py]
  called by: to_timestamp [period.py]

# call-chain context
  called by: _dict_round [frame.py]

# call-chain context
  called by: __add__ [datetimelike.py]

# call-chain context
  called by: setup [gil.py]
  called by: run [gil.py]

# call-chain context
  called by: setup_cache [algorithms.py]
  called by: setup [algorithms.py]

# call-chain context
  called by: __init__ [period.py]
  called by: _add_timedeltalike_scalar [period.py]

# call-chain context
  called by: setup [gil.py]
  called by: run [gil.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

```
