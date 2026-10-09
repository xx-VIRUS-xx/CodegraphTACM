# pandas-16 :: tacm

query: BUG: incorrect freq in PeriodIndex-Period (#33801)

## selected nodes

- rank=1 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=2 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=3 layer=FILE tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=4 layer=CLASS tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_period_range.py::TestPeriodRangeDisallowedFreqs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_period_range.py
- rank=5 layer=CLASS tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::TestSortValues file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=6 layer=CLASS tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=7 layer=CLASS tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/period/test_arithmetic.py::TestPeriodComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/period/test_arithmetic.py
- rank=8 layer=CLASS tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=9 layer=CLASS tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_constructors.py::TestPeriodIndexDisallowedFreqs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_constructors.py
- rank=10 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_freq_attr.py::TestFreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_freq_attr.py
- rank=11 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_to_period.py::TestToPeriod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_to_period.py
- rank=12 layer=CLASS tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c::modulestate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=13 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.asfreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=14 layer=FUNCTION tokens=311 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.from_ordinals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=15 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.hour file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=16 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._cast_partial_indexing_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=17 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.minute file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=18 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.second file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=19 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::period_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=20 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._parsed_string_to_bounds file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=21 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.is_leap_year file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=22 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=23 layer=FUNCTION tokens=277 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::use_dynamic_x file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=24 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=25 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=26 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=27 layer=FUNCTION tokens=407 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_resample file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=28 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_format_coord file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=29 layer=FUNCTION tokens=229 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=30 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.asfreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=31 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::format_dateaxis file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=32 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._scalar_from_string file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=33 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._disallow_mismatched_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py

## context

```text
file core/indexes/period.py
imports: __future__, datetime, typing, numpy, pandas, collections
defines: PeriodIndex, _new_PeriodIndex, period_range

file plotting/_matplotlib/timeseries.py
imports: __future__, functools, typing, numpy, pandas, datetime, matplotlib
defines: maybe_resample, _is_sub, _is_sup, _upsample_others, _replot_ax, decorate_axes, _get_ax_freq, _get_period_alias, _get_freq, use_dynamic_x, _get_index_freq, maybe_convert_index, _format_coord, format_dateaxis, prepare_ts_data

file core/arrays/period.py
imports: __future__, datetime, operator, typing, warnings, numpy, pandas
defines: PeriodArray, _field_accessor, f, raise_on_incompatible, period_array, validate_dtype_freq, dt64arr_to_periodarr, _get_ordinal_range, _range_from_fields, _make_field_arrays

class TestPeriodRangeDisallowedFreqs:  [indexes/period/test_period_range.py:202]
methods: test_A_raises_from_time_series, test_constructor_U
         test_incorrect_case_freq_from_time_series_raises
         test_lowercase_freq_from_time_series_deprecated
         test_uppercase_freq_deprecated_from_time_series

class TestSortValues:  [indexes/datetimelike_/test_sort_values.py:42]
methods: check_sort_values_with_freq
         check_sort_values_without_freq, non_monotonic_idx
         test_argmin_argmax, test_sort_values
         test_sort_values_with_freq_datetimeindex
         test_sort_values_with_freq_periodindex
         test_sort_values_with_freq_periodindex2
         test_sort_values_with_freq_timedeltaindex
         test_sort_values_without_freq_datetimeindex
         test_sort_values_without_freq_periodindex
         test_sort_values_without_freq_periodindex_nat
         test_sort_values_without_freq_timedeltaindex

class PeriodIndex(DatetimeIndexOpsMixin):  [core/indexes/period.py:90]
methods: _cast_partial_indexing_scalar, _convert_tolerance
         _disallow_mismatched_indexing, _engine_type
         _is_comparable_dtype, _maybe_cast_slice_bound
         _maybe_convert_timedelta
         _parsed_string_to_bounds, _resolution_obj, asfreq
         asof_locs, from_fields, from_ordinals, get_loc
         hour, inferred_type, is_full, minute, second
         shift, to_timestamp, values, __new__

class TestPeriodComparisons:  [scalar/period/test_arithmetic.py:403]
methods: test_period_comparison_invalid_type
         test_period_comparison_mismatched_freq
         test_period_comparison_nat
         test_period_comparison_numpy_zerodim_arr
         test_period_comparison_same_freq
         test_period_comparison_same_period_different_object

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

class TestPeriodIndexDisallowedFreqs:  [indexes/period/test_constructors.py:23]
methods: test_period_index_T_L_U_N_raises
         test_period_index_depr_lowercase_frequency
         test_period_index_frequency_invalid_freq
         test_period_index_from_datetime_index_invalid_freq
         test_period_index_offsets_frequency_error_message

class TestFreq:  [indexes/period/test_freq_attr.py:10]
methods: test_freq_setter_deprecated

class TestToPeriod:  [frame/methods/test_to_period.py:15]
methods: test_to_period, test_to_period_columns
         test_to_period_invalid_axis
         test_to_period_raises, test_to_period_without_freq

class modulestate  [vendored/ujson/python/ujson.c:70]
methods: —

    def asfreq(self, freq=None, how: str = "E") -> Self:
        """
        Convert the PeriodIndex to the specified frequency `freq`.

        Equivalent to applying :meth:`pandas.Period.asfreq` with the given arguments
        to each :class:`~pandas.Period` in this PeriodIndex.

        Parameters
        ----------
        freq : str
            A frequency.
        how : str {'E', 'S'}, default 'E'
    # ... truncated

    def from_ordinals(cls, ordinals, *, freq, name=None) -> Self:
        """
        Construct a PeriodIndex from ordinals.

        Ordinals are integer offsets from the proleptic Gregorian epoch,
        interpreted according to the given frequency.

        Parameters
        ----------
        ordinals : array-like of int
            The period offsets from the proleptic Gregorian epoch.
        freq : str or period object
            One of pandas period strings or corresponding objects.
        name : str, default None
            Name of the resulting PeriodIndex.

        Returns
        -------
        PeriodIndex

        See Also
        --------
        PeriodIndex.from_fields : Construct a PeriodIndex from fields
            (year, month, day, etc.).
        PeriodIndex.to_timestamp : Cast to DatetimeArray/Index.

        Examples
        --------
        >>> idx = pd.PeriodIndex.from_ordinals([-1, 0, 1], freq="Q")
        >>> idx
        PeriodIndex(['1969Q4', '1970Q1', '1970Q2'], dtype='period[Q-DEC]')
        """
        ordinals = np.asarray(ordinals, dtype=np.int64)
        dtype = PeriodDtype(freq)
        data = PeriodArray._simple_new(ordinals, dtype=dtype)
        return cls._simple_new(data, name=name)

    def hour(self) -> Index:
        """
        The hour of the period.

        Returns the hour component for each period in the index.

        See Also
        --------
        PeriodIndex.minute : The minute of the period.
        PeriodIndex.second : The second of the period.
        PeriodIndex.to_timestamp : Cast to DatetimeArray/Index.

        Examples
        --------
        >>> idx = pd.PeriodIndex(["2023-01-01 10:00", "2023-01-01 11:00"], freq="h")
        >>> idx.hour
        Index([10, 11], dtype='int64')
        """
        return Index(self._data.hour, name=self.name, copy=False)

    def _cast_partial_indexing_scalar(self, label: datetime) -> Period:
        try:
            period = Period(label, freq=self.freq)
        except ValueError as err:
            # we cannot construct the Period
            raise KeyError(label) from err
        return period

    def minute(self) -> Index:
        """
        The minute of the period.

        Returns the minute component for each period in the index.

        See Also
        --------
        PeriodIndex.hour : The hour of the period.
        PeriodIndex.second : The second of the period.
        PeriodIndex.to_timestamp : Cast to DatetimeArray/Index.

        Examples
        --------
        >>> idx = pd.PeriodIndex(
        ...     ["2023-01-01 10:30:00", "2023-01-01 11:50:00"], freq="min"
        ... )
        >>> idx.minute
        Index([30, 50], dtype='int64')
        """
        return Index(self._data.minute, name=self.name, copy=False)

    def second(self) -> Index:
        """
        The second of the period.

        Returns the second component for each period in the index.

        See Also
        --------
        PeriodIndex.hour : The hour of the period.
        PeriodIndex.minute : The minute of the period.
        PeriodIndex.to_timestamp : Cast to DatetimeArray/Index.

        Examples
        --------
        >>> idx = pd.PeriodIndex(
        ...     ["2023-01-01 10:00:30", "2023-01-01 10:00:31"], freq="s"
        ... )
        >>> idx.second
        Index([30, 31], dtype='int64')
        """
        return Index(self._data.second, name=self.name, copy=False)

def period_range(
    start=None,
    end=None,
    periods: int | None = None,
    freq=None,
    name: Hashable | None = None,
) -> PeriodIndex:
    """
    # ... truncated

    def _parsed_string_to_bounds(self, reso: Resolution, parsed: datetime):
        freq = OFFSET_TO_PERIOD_FREQSTR.get(reso.attr_abbrev, reso.attr_abbrev)
        iv = Period(parsed, freq=freq)
        return (iv.asfreq(self.freq, how="start"), iv.asfreq(self.freq, how="end"))

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

def use_dynamic_x(ax: Axes, index: Index) -> bool:
    freq = _get_index_freq(index)
    ax_freq = _get_ax_freq(ax)

    if freq is None:  # convert irregular if axes has freq info
        freq = ax_freq
    # do not use tsplot if irregular was plotted first
    elif (ax_freq is None) and (len(ax.get_lines()) > 0):
        return False

    if freq is None:
        return False

    freq_str = _get_period_alias(freq)

    if freq_str is None:
        return False

    # FIXME: hack this for 0.10.1, creating more technical debt...sigh
    if isinstance(index, ABCDatetimeIndex):
        # error: "BaseOffset" has no attribute "_period_dtype_code"
        freq_str = OFFSET_TO_PERIOD_FREQSTR.get(freq_str, freq_str)
        base = to_offset(freq_str, is_period=True)._period_dtype_code  # type: ignore[attr-defined]
        if base <= FreqGroup.FR_DAY.value:
            return index[:1].is_normalized  # type: ignore[attr-defined]
        period = Period(index[0], freq_str)
        assert isinstance(period, Period)
        return period.to_timestamp().tz_localize(index.tz) == index[0]
    return True

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

    def __new__(
        cls,
        data=None,
        freq=None,
        dtype: Dtype | None = None,
        copy: bool | None = None,
        name: Hashable | None = None,
    ) -> Self:
        refs = None
        if not copy and isinstance(data, (Index, ABCSeries)):
            refs = data._references
        if dtype is not None:
            dtype = pandas_dtype(dtype)

        name = maybe_extract_name(name, data, cls)

        if freq is not None:
            freq = to_offset(freq, is_period=True)
        dtype2 = PeriodDtype(freq) if freq is not None else None
        dtype = validate_dtype_freq(dtype, dtype2)
        if dtype is not None:
            freq = dtype._freq

        # GH#63388
        data, copy = cls._maybe_copy_array_input(data, copy, dtype)

        data = period_array(data=data, dtype=dtype)

        if copy:
            data = data.copy()

        return cls._simple_new(data, name=name, refs=refs)

def _get_freq(ax: Axes, series: Series):
    # get frequency from data
    freq = getattr(series.index, "freq", None)
    if freq is None:
        freq = getattr(series.index, "inferred_freq", None)
        freq = to_offset(freq, is_period=True)

    ax_freq = _get_ax_freq(ax)

    # use axes freq if no data freq
    if freq is None:
        freq = ax_freq

    # get the period frequency
    freq = _get_period_alias(freq)
    return freq, ax_freq

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

def _format_coord(freq, t, y) -> str:
    if _get_period_alias(freq) == "B":
        # Avoid creating deprecated Period[B]; convert ordinal to datetime
        # using numpy business-day arithmetic.
        return f"t = {bday_to_datetime(int(t)).strftime('%Y-%m-%d')}  y = {y:8f}"
    time_period = Period(ordinal=int(t), freq=freq)
    return f"t = {time_period}  y = {y:8f}"

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

def format_dateaxis(
    subplot, freq: BaseOffset, index: DatetimeIndex | PeriodIndex
) -> None:
    """
    # ... truncated

    def _scalar_from_string(self, value: str) -> Period:
        return Period(value, freq=self.freq)

    def _disallow_mismatched_indexing(self, key: Period) -> None:
        if key._dtype != self.dtype:
            raise KeyError(key)
```
