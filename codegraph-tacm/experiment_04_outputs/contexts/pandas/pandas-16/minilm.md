# pandas-16 :: minilm

query: BUG: incorrect freq in PeriodIndex-Period (#33801)

## selected nodes

- rank=1 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=2 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestPeriodIndexEquals.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
- rank=3 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::_new_PeriodIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=4 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=5 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=6 layer=FUNCTION tokens=227 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py::DatetimeProperties.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py
- rank=7 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py::TestDropDuplicatesPeriodIndex.idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py
- rank=8 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::datetime_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=9 layer=FUNCTION tokens=714 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::period_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=10 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.freqstr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=11 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::mismatched_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py
- rank=12 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=13 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._cast_partial_indexing_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=14 layer=FUNCTION tokens=485 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=15 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_nonmonotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=16 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py::TestDropDuplicatesPeriodIndex.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py
- rank=17 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_date_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=18 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints_daily file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=19 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.f file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=20 layer=FUNCTION tokens=277 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin.freqstr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=21 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.index_class file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=22 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodProperties.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=23 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_ascending file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=24 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::PeriodIndexResamplerGroupby._resampler_cls file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestPeriodIndexEquals.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py]
    def index(self):
        """Fixture for creating a PeriodIndex for use in equality tests."""
        return period_range("2013-01-01", periods=5, freq="D")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def freq(self, value) -> None:
        # error: Property "freq" defined in "PeriodArray" is read-only  [misc]
        self._data.freq = value  # type: ignore[misc]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py::DatetimeProperties.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py]
    def freq(self):
        """
        Tries to return a string representing a frequency generated by infer_freq.

        Returns None if it can't autodetect the frequency.

        See Also
        --------
        Series.dt.to_period : Cast to PeriodArray/PeriodIndex at a particular
            frequency.

        Examples
        --------
        >>> ser = pd.Series(["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"])
        >>> ser = pd.to_datetime(ser)
        >>> ser.dt.freq
        'D'

        >>> ser = pd.Series(["2022-01-01", "2024-01-01", "2026-01-01", "2028-01-01"])
        >>> ser = pd.to_datetime(ser)
        >>> ser.dt.freq
        '2YS-JAN'
        """
        return self._get_values().inferred_freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py::TestDropDuplicatesPeriodIndex.idx [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py]
    def idx(self, freq):
        """
        Fixture to get PeriodIndex for 10 periods for different frequencies.
        """
        return period_range("2011-01-01", periods=10, freq=freq, name="idx")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::period_range [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
def period_range(
    start=None,
    end=None,
    periods: int | None = None,
    freq=None,
    name: Hashable | None = None,
) -> PeriodIndex:
    """
    Return a fixed frequency PeriodIndex.

    The day (calendar) is the default frequency.

    Parameters
    ----------
    start : str, datetime, date, pandas.Timestamp, or period-like, default None
        Left bound for generating periods.
    end : str, datetime, date, pandas.Timestamp, or period-like, default None
        Right bound for generating periods.
    periods : int, default None
        Number of periods to generate.
    freq : str or DateOffset, optional
        Frequency alias. By default the freq is taken from `start` or `end`
        if those are Period objects. Otherwise, the default is ``"D"`` for
        daily frequency.
    name : str, default None
        Name of the resulting PeriodIndex.

    Returns
    -------
    PeriodIndex
        A PeriodIndex of fixed frequency periods.

    See Also
    --------
    date_range : Returns a fixed frequency DatetimeIndex.
    Period : Represents a period of time.
    PeriodIndex : Immutable ndarray holding ordinal values indicating regular periods
        in time.

    Notes
    -----
    Of the three parameters: ``start``, ``end``, and ``periods``, exactly two
    must be specified.

    To learn more about the frequency strings, please see
    :ref:`this link<timeseries.offset_aliases>`.

    Examples
    --------
    >>> pd.period_range(start="2017-01-01", end="2018-01-01", freq="M")
    PeriodIndex(['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06',
             '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
             '2018-01'],
            dtype='period[M]')

    If ``start`` or ``end`` are ``Period`` objects, they will be used as anchor
    endpoints for a ``PeriodIndex`` with frequency matching that of the
    ``period_range`` constructor.

    >>> pd.period_range(
    ...     start=pd.Period("2017Q1", freq="Q"),
    ...     end=pd.Period("2017Q2", freq="Q"),
    ...     freq="M",
    ... )
    PeriodIndex(['2017-03', '2017-04', '2017-05', '2017-06'],
                dtype='period[M]')
    """
    if com.count_not_none(start, end, periods) != 2:
        raise ValueError(
            "Of the three parameters: start, end, and periods, "
            "exactly two must be specified"
        )
    if freq is None and (not isinstance(start, Period) and not isinstance(end, Period)):
        freq = "D"

    data, freq = PeriodArray._generate_range(start, end, periods, freq)
    dtype = PeriodDtype(freq)
    data = PeriodArray(data, dtype=dtype)
    return PeriodIndex(data, name=name, copy=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.freqstr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def freqstr(self) -> str:
        return PeriodDtype(self.freq)._freqstr

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::mismatched_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py]
def mismatched_freq(request):
    """
    Several timedelta-like and DateOffset instances that are _not_
    compatible with Monthly or Annual frequencies.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_ints(self, freq, is_offset):
        PeriodIndex(self.ints, freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._cast_partial_indexing_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
    def _cast_partial_indexing_scalar(self, label: datetime) -> Period:
        try:
            period = Period(label, freq=self.freq)
        except ValueError as err:
            # we cannot construct the Period
            raise KeyError(label) from err
        return period

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_nonmonotonic [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py]
def check_freq_nonmonotonic(ordered, orig):
    """
    Check the expected freq on a PeriodIndex/DatetimeIndex/TimedeltaIndex
    when the original index is _not_ generated (or generate-able) with
    period_range/date_range//timedelta_range.
    """
    if isinstance(ordered, PeriodIndex):
        assert ordered.freq == orig.freq
    elif isinstance(ordered, (DatetimeIndex, TimedeltaIndex)):
        assert ordered.freq is None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py::TestDropDuplicatesPeriodIndex.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py]
    def freq(self, request):
        """
        Fixture to test for different frequencies for PeriodIndex.
        """
        return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_date_range [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_date_range(self, freq, is_offset):
        PeriodIndex(self.rng, freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints_daily [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_ints_daily(self, freq, is_offset):
        PeriodIndex(self.daily_ints, freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.f [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
            def f(values, freq=None, tz=None):
                dtype = PeriodDtype(freq)
                parr = PeriodArray._simple_new(values, dtype=dtype)
                return PeriodIndex._simple_new(parr, name=None)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin.freqstr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def freqstr(self) -> str | None:
        """
        Return the frequency object as a string if it's set, otherwise None.

        See Also
        --------
        DatetimeIndex.inferred_freq : Returns a string representing a frequency
            generated by infer_freq.

        Examples
        --------
        For DatetimeIndex:

        >>> idx = pd.DatetimeIndex(["1/1/2020 10:00:00+00:00"], freq="D")
        >>> idx.freqstr
        'D'

        The frequency can be inferred if there are more than 2 points:

        >>> idx = pd.DatetimeIndex(
        ...     ["2018-01-01", "2018-01-03", "2018-01-05"], freq="infer"
        ... )
        >>> idx.freqstr
        '2D'

        For PeriodIndex:

        >>> idx = pd.PeriodIndex(["2023-1", "2023-2", "2023-3"], freq="M")
        >>> idx.freqstr
        'M'
        """
        if self.freq is None:
            return None
        return self.freq.freqstr

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.index_class [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def index_class(self) -> type_t[PeriodIndex]:
        from pandas import PeriodIndex

        return PeriodIndex

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodProperties.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def setup(self, freq, attr):
        self.per = Period("2012-06-01", freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_ascending [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py]
def check_freq_ascending(ordered, orig, ascending):
    """
    Check the expected freq on a PeriodIndex/DatetimeIndex/TimedeltaIndex
    when the original index is generated (or generate-able) with
    period_range/date_range/timedelta_range.
    """
    if isinstance(ordered, PeriodIndex):
        assert ordered.freq == orig.freq
    elif isinstance(ordered, (DatetimeIndex, TimedeltaIndex)):
        if ascending:
            assert ordered.freq.n == orig.freq.n
        else:
            assert ordered.freq.n == -1 * orig.freq.n

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::PeriodIndexResamplerGroupby._resampler_cls [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _resampler_cls(self):
        return PeriodIndexResampler
```
