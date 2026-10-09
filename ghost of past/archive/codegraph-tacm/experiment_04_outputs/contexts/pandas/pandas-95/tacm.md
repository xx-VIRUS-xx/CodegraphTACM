# pandas-95 :: tacm

query: BUG: PeriodArray comparisons inconsistent with Period comparisons (#30722)

## selected nodes

- rank=1 layer=FILE tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=2 layer=FILE tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py
- rank=3 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=4 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=5 layer=CLASS tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_operators.py::TestCategoricalOpsWithFactor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_operators.py
- rank=6 layer=CLASS tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::TestTimedelta64ArrayComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=7 layer=CLASS tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_object.py::TestObjectComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_object.py
- rank=8 layer=CLASS tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetime64SeriesComparison file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=9 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py::OffsetWithNamespace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py
- rank=10 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_comparisons.py::Inf file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
- rank=11 layer=CLASS tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py::Visitor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py
- rank=12 layer=CLASS tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_arithmetic.py::TestSeriesComparison file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_arithmetic.py
- rank=13 layer=CLASS tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=14 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimePeriodArrToDT64Arr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=15 layer=CLASS tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::TestTimedelta64ArrayLikeComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=16 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::DataFramePeriodColumn file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=17 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::Algorithms file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=18 layer=CLASS tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_fillna.py::TestFillNA file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_fillna.py
- rank=19 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::DataFramePeriodColumn.time_set_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=20 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.asfreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=21 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._check_compatible_with file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=22 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._scalar_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=23 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::period_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=24 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._scalar_from_string file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=25 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._box_func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=26 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._unbox_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=27 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_daily_finder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py
- rank=28 layer=FUNCTION tokens=229 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=29 layer=FUNCTION tokens=272 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.__arrow_array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=30 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::TestComparison.interval_constructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py
- rank=31 layer=FUNCTION tokens=232 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py::check_for_inconsistent_pandas_namespace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/check_for_inconsistent_pandas_namespace.py
- rank=32 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=33 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=34 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::raise_on_incompatible file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=35 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._generate_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=36 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._format_native_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=37 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.is_leap_year file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=38 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._add_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=39 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=40 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._add_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=41 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.dayofweek file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=42 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=43 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py::expected_with_na_handling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py
- rank=44 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimePeriodArrToDT64Arr.time_periodarray_to_dt64arr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=45 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=46 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.freqstr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=47 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py

## context

```text
file core/arrays/period.py
imports: __future__, datetime, operator, typing, warnings, numpy, pandas
defines: PeriodArray, _field_accessor, f, raise_on_incompatible, period_array, validate_dtype_freq, dt64arr_to_periodarr, _get_ordinal_range, _range_from_fields, _make_field_arrays

file pandas/scripts/check_for_inconsistent_pandas_namespace.py
imports: argparse, ast, collections, sys, typing, tokenize_rt
defines: OffsetWithNamespace, Visitor, replace_inconsistent_pandas_namespace, check_for_inconsistent_pandas_namespace, main

file core/indexes/period.py
imports: __future__, datetime, typing, numpy, pandas, collections
defines: PeriodIndex, _new_PeriodIndex, period_range

file asv_bench/benchmarks/period.py
imports: pandas
defines: PeriodIndexConstructor, DataFramePeriodColumn, Algorithms, Indexing

class TestCategoricalOpsWithFactor:  [arrays/categorical/test_operators.py:15]
methods: test_categories_none_comparisons, test_comparisons

class TestTimedelta64ArrayComparisons:  [tests/arithmetic/test_timedelta64.py:170]
methods: test_comp_nat, test_comparisons_coverage
         test_comparisons_nat

class TestObjectComparisons:  [tests/arithmetic/test_object.py:26]
methods: test_comp_nat_object_dtype
         test_comparison_object_numeric_nas
         test_more_na_comparisons, test_object_comparisons

class TestDatetime64SeriesComparison:  [tests/arithmetic/test_datetime64.py:158]
methods: test_dt64_compare_datetime_scalar
         test_dt64arr_timestamp_equality
         test_nat_comparisons, test_nat_comparisons_scalar
         test_series_comparison_scalars
         test_timestamp_compare_series
         test_ts_series_numpy_maximum

class OffsetWithNamespace(NamedTuple):  [pandas/scripts/check_for_inconsistent_pandas_namespace.py:37]
methods: —

class Inf:  [scalar/timestamp/test_comparisons.py:290]
methods: __eq__, __ge__, __gt__, __le__, __lt__

class Visitor(ast.NodeVisitor):  [pandas/scripts/check_for_inconsistent_pandas_namespace.py:43]
methods: visit_Attribute, visit_ImportFrom, __init__

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

class PeriodArray(dtl.DatelikeOps, libperiod.PeriodMixin):  [core/arrays/period.py:123]
methods: _add_offset, _add_timedelta_arraylike
         _add_timedeltalike_scalar
         _addsub_int_array_or_scalar, _box_func
         _check_compatible_with
         _check_timedeltalike_freq_compat
         _format_native_types, _formatter
         _from_datetime64, _from_fields, _from_sequence
         _from_sequence_of_strings, _generate_range
         _pad_or_backfill, _reduce, _scalar_from_string
         _scalar_type, _simple_new, _unbox_scalar, asfreq
         astype, dayofweek, dayofyear, daysinmonth, dtype
         freq, freqstr, is_leap_year, searchsorted
         to_timestamp, weekday, __array__, __arrow_array__
         __init__

class TimePeriodArrToDT64Arr:  [benchmarks/tslibs/period.py:126]
methods: setup, time_periodarray_to_dt64arr

class TestTimedelta64ArrayLikeComparisons:  [tests/arithmetic/test_timedelta64.py:63]
methods: test_compare_timedelta64_zerodim
         test_compare_timedeltalike_scalar
         test_td64_comparisons_invalid
         test_td64arr_cmp_arraylike_invalid
         test_td64arr_cmp_mixed_invalid

class DataFramePeriodColumn:  [asv_bench/benchmarks/period.py:47]
methods: setup, time_set_index, time_setitem_period_column

class Algorithms:  [asv_bench/benchmarks/period.py:61]
methods: setup, time_drop_duplicates, time_value_counts

class TestFillNA:  [period/methods/test_fillna.py:10]
methods: test_fillna_period

    def time_set_index(self):
        # GH#21582 limited by comparisons of Period objects
        self.df["col2"] = self.rng
        self.df.set_index("col2", append=True)

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

    def _check_compatible_with(self, other: Period | NaTType | PeriodArray) -> None:  # type: ignore[override]
        if other is NaT:
            return
        elif isinstance(other, Period):
            self._require_matching_unit(other._dtype._freqstr)
        else:
            # error: Item "NaTType" of "NaTType | PeriodArray" has no
            # attribute "freq"
            self._require_matching_unit(other.dtype._freqstr)  # type: ignore[union-attr]

    def _scalar_type(self) -> type[Period]:
        return Period

def period_array(
    data: Sequence[Period | str | None] | AnyArrayLike,
    dtype: PeriodDtype | None = None,
) -> PeriodArray:
    """
    # ... truncated

    def _scalar_from_string(self, value: str) -> Period:
        return Period(value, freq=self.freq)

    def _box_func(self, x) -> Period | NaTType:
        return Period._from_ordinal(ordinal=x, dtype=self.dtype)

    def _unbox_scalar(  # type: ignore[override]
        self,
        value: Period | NaTType,
    ) -> np.int64:
        if value is NaT:
            # error: Item "Period" of "Union[Period, NaTType]" has no attribute "value"
            return np.int64(value._value)  # type: ignore[union-attr]
        elif isinstance(value, self._scalar_type):
            self._check_compatible_with(value)
            return np.int64(value.ordinal)
        else:
            raise ValueError(f"'value' should be a Period. Got '{value}' instead.")

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

    def astype(self, dtype, copy: bool = True):
        # We handle Period[T] -> Period[U]
        # Our parent handles everything else.
        dtype = pandas_dtype(dtype)
        if dtype == self._dtype:
            if not copy:
                return self
            else:
                return self.copy()
        if isinstance(dtype, PeriodDtype):
            return self.asfreq(dtype.freq)

        if lib.is_np_dtype(dtype, "M") or isinstance(dtype, DatetimeTZDtype):
            # GH#45038 match PeriodIndex behavior.
            tz = getattr(dtype, "tz", None)
            unit = dtl.dtype_to_unit(dtype)
            # error: Argument 1 to "as_unit" of "TimelikeOps" has incompatible
            # type "str"; expected "Literal['s', 'ms', 'us', 'ns']"  [arg-type]
            return self.to_timestamp().tz_localize(tz).as_unit(unit)  # type: ignore[arg-type]

        return super().astype(dtype, copy=copy)

    def __arrow_array__(self, type=None):
        """
        Convert myself into a pyarrow Array.
        """
        import pyarrow

        from pandas.core.arrays.arrow.extension_types import ArrowPeriodType

        if type is not None:
            if pyarrow.types.is_integer(type):
                return pyarrow.array(self._ndarray, mask=self.isna(), type=type)
            elif isinstance(type, ArrowPeriodType):
                # ensure we have the same freq
                if self.freqstr != type.freq:
                    raise TypeError(
                        "Not supported to convert PeriodArray to array with different "
                        f"'freq' ({self.freqstr} vs {type.freq})"
                    )
            else:
                raise TypeError(
                    f"Not supported to convert PeriodArray to '{type}' type"
                )

        period_type = ArrowPeriodType(self.freqstr)
        storage_array = pyarrow.array(self._ndarray, mask=self.isna(), type="int64")
        return pyarrow.ExtensionArray.from_storage(period_type, storage_array)

    def interval_constructor(self, request):
        """
        Fixture for all pandas native interval constructors.
        To be used as the LHS of IntervalArray comparisons.
        """
        return request.param

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

    def _generate_range(cls, start, end, periods, freq):
        periods = dtl.validate_periods(periods)

        if freq is not None:
            freq = Period._maybe_convert_freq(freq)

        if start is not None or end is not None:
            subarr, freq = _get_ordinal_range(start, end, periods, freq)
        else:
            raise ValueError("Not enough parameters to construct Period range")

        return subarr, freq

    def _format_native_types(
        self, *, na_rep: str | float = "NaT", date_format=None, **kwargs
    ) -> npt.NDArray[np.object_]:
        """
        actually format my specific types
        """
        return libperiod.period_array_strftime(
            self.asi8, self.dtype._dtype_code, na_rep, date_format
        )

    def is_leap_year(self) -> npt.NDArray[np.bool_]:
        """
        Logical indicating if the date belongs to a leap year.

        Returns a boolean array where ``True`` indicates the period's year
        is a leap year.

        See Also
        --------
        PeriodIndex.qyear : Fiscal year the Period lies in according to its
            starting-quarter.
        PeriodIndex.year : The year of the period.

        Examples
        --------
        >>> idx = pd.PeriodIndex(["2023", "2024", "2025"], freq="Y")
        >>> idx.is_leap_year
        array([False,  True, False])
        """
        return isleapyear_arr(np.asarray(self.year))

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

    def _add_offset(self, other: BaseOffset):
        assert not isinstance(other, Tick)

        if isinstance(other, Day):
            return self + np.timedelta64(other.n, "D")

        self._require_matching_unit(other._period_unit, base=True)
        return self._addsub_int_array_or_scalar(other.n, operator.add)

    def dayofweek(self):
        """
        The day of the week with Monday=0, Sunday=6.

        .. deprecated:: 3.1.0
            Use :attr:`PeriodIndex.day_of_week` instead.
        """
        from pandas.errors import Pandas4Warning
        from pandas.util._exceptions import find_stack_level

        warnings.warn(
            "PeriodArray.dayofweek is deprecated and will be removed in a "
            "future version. Use PeriodArray.day_of_week instead.",
            Pandas4Warning,
            stacklevel=find_stack_level(),
        )
        return self.day_of_week

    def dtype(self) -> PeriodDtype:
        return self._dtype

    def expected_with_na_handling(lvalues, rvalues, op):
        # Similar to comparison_op, handle zerodim arrays with na value separately
        if (rvalues.ndim == 0) and isna(rvalues.item()):
            # numpy does not like comparisons vs None
            if op is operator.ne:
                return np.ones(lvalues.shape, dtype=bool)
            else:
                return np.zeros(lvalues.shape, dtype=bool)
        return op(lvalues, rvalues)

    def time_periodarray_to_dt64arr(self, size, freq):
        periodarr_to_dt64arr(self.i8values, freq)

    def freq(self) -> BaseOffset:  # type: ignore[override]
        """
        Return the frequency object for this PeriodArray.
        """
        return self.dtype.freq

    def freqstr(self) -> str:
        return PeriodDtype(self.freq)._freqstr

    def len(self, text: str) -> int:
        return len(text)
```
