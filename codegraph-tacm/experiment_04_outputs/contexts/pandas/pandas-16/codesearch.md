# pandas-16 :: codesearch

query: BUG: incorrect freq in PeriodIndex-Period (#33801)

## selected nodes

- rank=1 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=2 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::_new_PeriodIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=3 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodConstructor.time_period_constructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=4 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_date_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=5 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py::TestDropDuplicatesPeriodIndex.idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py
- rank=6 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints_daily file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=7 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_pydatetime file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=8 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestPeriodIndexEquals.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
- rank=9 layer=FUNCTION tokens=349 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_get_datevalue file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py
- rank=10 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=11 layer=FUNCTION tokens=485 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=12 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._cast_partial_indexing_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=13 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=14 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_period_break_mask file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py
- rank=15 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::_simple_period_range_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py
- rank=16 layer=FUNCTION tokens=696 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=17 layer=FUNCTION tokens=339 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_get_periods_per_ymd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py
- rank=18 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::datetime_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=19 layer=FUNCTION tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype._parse_dtype_strict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=20 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.f file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py]
def period_index(freqstr):
    """
    A fixture to provide PeriodIndex objects with different frequencies.

    Most PeriodArray behavior is already tested in PeriodIndex tests,
    so here we just test that the PeriodArray behavior matches
    the PeriodIndex behavior.
    """
    # TODO: non-monotone indexes; NaTs, different start dates
    with warnings.catch_warnings():
        # suppress deprecation of Period[B]
        warnings.filterwarnings(
            "ignore", message="Period with BDay freq", category=FutureWarning
        )
        freqstr = PeriodDtype(to_offset(freqstr))._freqstr
        pi = pd.period_range(start=Timestamp("2000-01-01"), periods=100, freq=freqstr)
    return pi

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::_new_PeriodIndex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
def _new_PeriodIndex(cls, **d):
    # GH13277 for unpickling
    values = d.pop("data")
    if values.dtype == "int64":
        freq = d.pop("freq", None)
        dtype = PeriodDtype(freq)
        values = PeriodArray(values, dtype=dtype)
        return cls._simple_new(values, **d)
    else:
        return cls(values, **d)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodConstructor.time_period_constructor [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def time_period_constructor(self, freq, is_offset):
        Period("2012-06-01", freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_date_range [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_date_range(self, freq, is_offset):
        PeriodIndex(self.rng, freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py::TestDropDuplicatesPeriodIndex.idx [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py]
    def idx(self, freq):
        """
        Fixture to get PeriodIndex for 10 periods for different frequencies.
        """
        return period_range("2011-01-01", periods=10, freq=freq, name="idx")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints_daily [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_ints_daily(self, freq, is_offset):
        PeriodIndex(self.daily_ints, freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_pydatetime [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_pydatetime(self, freq, is_offset):
        PeriodIndex(self.rng2, freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestPeriodIndexEquals.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py]
    def index(self):
        """Fixture for creating a PeriodIndex for use in equality tests."""
        return period_range("2013-01-01", periods=5, freq="D")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_get_datevalue [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py]
def _get_datevalue(date, freq):
    if isinstance(date, Period):
        freq_obj = to_offset(freq, is_period=True)
        dtype_code = freq_obj._period_dtype_code
        if FreqGroup.from_period_dtype_code(dtype_code) == FreqGroup.FR_BUS:
            # Avoid creating deprecated Period[B] via asfreq.  If the Period
            # is already BDay, its ordinal IS the business-day count; otherwise
            # convert via timestamp.
            if date.freqstr == "B":
                return date.ordinal
            return bday_count(date.to_timestamp())
        return date.asfreq(freq).ordinal
    elif isinstance(date, (str, datetime, pydt.date, np.datetime64)):
        freq_obj = to_offset(freq, is_period=True)
        dtype_code = freq_obj._period_dtype_code
        if FreqGroup.from_period_dtype_code(dtype_code) == FreqGroup.FR_BUS:
            # Avoid creating deprecated Period[B]; use numpy business-day count.
            return bday_count(date)
        return Period(date, freq).ordinal  # pyright: ignore[reportAttributeAccessIssue]
    elif is_integer(date) or is_float(date):
        return date
    elif date is None:
        return None
    raise ValueError(f"Unrecognizable date '{date}'")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_ints(self, freq, is_offset):
        PeriodIndex(self.ints, freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.to_period [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py]
    def to_period(self, freq=None) -> PeriodIndex:
        """
        Cast to PeriodArray/PeriodIndex at a particular frequency.

        Converts DatetimeArray/Index to PeriodArray/PeriodIndex.

        Parameters
        ----------
        freq : str or Period, optional
            One of pandas' :ref:`period aliases <timeseries.period_aliases>`
            or a Period object. Will be inferred by default.

        Returns
        -------
        PeriodArray/PeriodIndex
            Immutable ndarray holding ordinal values at a particular frequency.

        Raises
        ------
        ValueError
            When converting a DatetimeArray/Index with non-regular values,
            so that a frequency cannot be inferred.

        See Also
        --------
        PeriodIndex: Immutable ndarray holding ordinal values.
        DatetimeIndex.to_pydatetime: Return DatetimeIndex as object.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {"y": [1, 2, 3]},
        ...     index=pd.to_datetime(
        ...         [
        ...             "2000-03-31 00:00:00",
        ...             "2000-05-31 00:00:00",
        ...             "2000-08-31 00:00:00",
        ...         ]
        ...     ),
        ... )
        >>> df.index.to_period("M")
        PeriodIndex(['2000-03', '2000-05', '2000-08'],
                    dtype='period[M]')

        Infer the daily frequency

        >>> idx = pd.date_range("2017-01-01", periods=2)
        >>> idx.to_period()
        PeriodIndex(['2017-01-01', '2017-01-02'],
                    dtype='period[D]')
        """
        from pandas.core.indexes.api import PeriodIndex

        arr = self._data.to_period(freq)
        return PeriodIndex._simple_new(arr, name=self.name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._cast_partial_indexing_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
    def _cast_partial_indexing_scalar(self, label: datetime) -> Period:
        try:
            period = Period(label, freq=self.freq)
        except ValueError as err:
            # we cannot construct the Period
            raise KeyError(label) from err
        return period

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def freq(self) -> BaseOffset:
        """
        The frequency object of this PeriodDtype.

        The `freq` property returns the `BaseOffset` object that represents the
        frequency of the PeriodDtype. This frequency specifies the interval (e.g.,
        daily, monthly, yearly) associated with the Period type. It is essential
        for operations that depend on time-based calculations within a period index
        or series.

        See Also
        --------
        Period : Represents a period of time.
        PeriodIndex : Immutable ndarray holding ordinal values indicating
            regular periods.
        PeriodDtype : An ExtensionDtype for Period data.
        date_range : Return a fixed frequency range of dates.

        Examples
        --------
        >>> dtype = pd.PeriodDtype(freq="D")
        >>> dtype.freq
        <Day>
        """
        return self._freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_period_break_mask [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py]
def _period_break_mask(
    dates: PeriodIndex | DatetimeIndex, period: str
) -> npt.NDArray[np.bool_]:
    # DatetimeIndex has no .week attribute; use .isocalendar().week instead
    if period == "week" and isinstance(dates, DatetimeIndex):
        current = dates.isocalendar().week.values
        previous = (dates - 1 * dates.freq).isocalendar().week.values  # type: ignore[operator]
    else:
        current = getattr(dates, period)
        previous = getattr(dates - 1 * dates.freq, period)  # type: ignore[operator]
    return current != previous

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::_simple_period_range_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py]
    def _simple_period_range_series(start, end, freq="D"):
        with warnings.catch_warnings():
            # suppress Period[B] deprecation warning
            msg = "|".join(["Period with BDay freq", r"PeriodDtype\[B\] is deprecated"])
            warnings.filterwarnings(
                "ignore",
                msg,
                category=FutureWarning,
            )
            rng = period_range(start, end, freq=freq)
        return Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.to_period [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py]
    def to_period(self, freq=None) -> PeriodArray:
        """
        Cast to PeriodArray/PeriodIndex at a particular frequency.

        Converts DatetimeArray/Index to PeriodArray/PeriodIndex.

        Parameters
        ----------
        freq : str or Period, optional
            One of pandas' :ref:`period aliases <timeseries.period_aliases>`
            or a Period object. Will be inferred by default.

        Returns
        -------
        PeriodArray/PeriodIndex
            Immutable ndarray holding ordinal values at a particular frequency.

        Raises
        ------
        ValueError
            When converting a DatetimeArray/Index with non-regular values,
            so that a frequency cannot be inferred.

        See Also
        --------
        PeriodIndex: Immutable ndarray holding ordinal values.
        DatetimeIndex.to_pydatetime: Return DatetimeIndex as object.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {"y": [1, 2, 3]},
        ...     index=pd.to_datetime(
        ...         [
        ...             "2000-03-31 00:00:00",
        ...             "2000-05-31 00:00:00",
        ...             "2000-08-31 00:00:00",
        ...         ]
        ...     ),
        ... )
        >>> df.index.to_period("M")
        PeriodIndex(['2000-03', '2000-05', '2000-08'],
                    dtype='period[M]')

        Infer the daily frequency

        >>> idx = pd.date_range("2017-01-01", periods=2)
        >>> idx.to_period()
        PeriodIndex(['2017-01-01', '2017-01-02'],
                    dtype='period[D]')
        """
        from pandas.core.arrays import PeriodArray

        if self.tz is not None:
            warnings.warn(
                "Converting to PeriodArray/Index representation "
                "will drop timezone information.",
                UserWarning,
                stacklevel=find_stack_level(),
            )

        if freq is None:
            freq = self.freqstr or self.inferred_freq
            if isinstance(self.freq, BaseOffset) and hasattr(
                self.freq, "_period_dtype_code"
            ):
                freq = PeriodDtype(self.freq)._freqstr

            if freq is None:
                raise ValueError(
                    "You must pass a freq argument as current index has none."
                )

            res = get_period_alias(freq)

            #  https://github.com/pandas-dev/pandas/issues/33358
            if res is None:
                res = freq

            freq = res
        return PeriodArray._from_datetime64(self._ndarray, freq, tz=self.tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_get_periods_per_ymd [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py]
def _get_periods_per_ymd(freq: BaseOffset) -> tuple[int, int, int]:
    # error: "BaseOffset" has no attribute "_period_dtype_code"
    dtype_code = freq._period_dtype_code  # type: ignore[attr-defined]
    freq_group = FreqGroup.from_period_dtype_code(dtype_code)

    ppd = -1  # placeholder for above-day freqs

    if dtype_code >= FreqGroup.FR_HR.value:  # pyright: ignore[reportAttributeAccessIssue]
        # error: "BaseOffset" has no attribute "_creso"
        ppd = periods_per_day(freq._creso)  # type: ignore[attr-defined]
        ppm = 28 * ppd
        ppy = 365 * ppd
    elif freq_group == FreqGroup.FR_BUS:
        ppm = 19
        ppy = 261
    elif freq_group == FreqGroup.FR_DAY:
        ppm = 28
        ppy = 365
    elif freq_group == FreqGroup.FR_WK:
        ppm = 3
        ppy = 52
    elif freq_group == FreqGroup.FR_MTH:
        ppm = 1
        ppy = 12
    elif freq_group == FreqGroup.FR_QTR:
        ppm = -1  # placeholder
        ppy = 4
    elif freq_group == FreqGroup.FR_ANN:
        ppm = -1  # placeholder
        ppy = 1
    else:
        raise NotImplementedError(f"Unsupported frequency: {dtype_code}")

    return ppd, ppm, ppy

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::datetime_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py]
def datetime_index(freqstr):
    """
    A fixture to provide DatetimeIndex objects with different frequencies.

    Most DatetimeArray behavior is already tested in DatetimeIndex tests,
    so here we just test that the DatetimeArray behavior matches
    the DatetimeIndex behavior.
    """
    # TODO: non-monotone indexes; NaTs, different start dates, timezones
    dti = pd.date_range(
        start=Timestamp("2000-01-01"), periods=100, freq=freqstr, unit="ns"
    )
    return dti

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype._parse_dtype_strict [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _parse_dtype_strict(cls, freq: str_type) -> BaseOffset:
        if isinstance(freq, str):  # note: freq is already of type str!
            if freq.startswith(("Period[", "period[")):
                m = cls._match.search(freq)
                if m is not None:
                    freq = m.group("freq")

            freq_offset = to_offset(freq, is_period=True)
            if freq_offset is not None:
                return freq_offset

        raise TypeError(
            "PeriodDtype argument should be string or BaseOffset, "
            f"got {type(freq).__name__}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.f [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
            def f(values, freq=None, tz=None):
                dtype = PeriodDtype(freq)
                parr = PeriodArray._simple_new(values, dtype=dtype)
                return PeriodIndex._simple_new(parr, name=None)
```
