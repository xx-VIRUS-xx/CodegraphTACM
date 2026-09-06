# pandas-92 :: hybrid

query: BUG: PeriodIndex.searchsorted accepting invalid inputs (#30763)

## selected nodes

- rank=1 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.index_class file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=2 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=3 layer=FUNCTION tokens=578 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.from_fields file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=4 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=5 layer=FUNCTION tokens=240 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_period_bins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=6 layer=FUNCTION tokens=485 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=7 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestPeriodIndexEquals.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
- rank=8 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=9 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.second file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=10 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::_new_PeriodIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=11 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_nonmonotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=12 layer=FUNCTION tokens=354 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.from_ordinals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=13 layer=FUNCTION tokens=411 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_fill_indexer_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=14 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::TestPeriodArray.arr1d file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=15 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_ascending file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=16 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=17 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._convert_tolerance file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=18 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.f file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=19 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_period_break file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.index_class [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def index_class(self) -> type_t[PeriodIndex]:
        from pandas import PeriodIndex

        return PeriodIndex

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.from_fields [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
    def from_fields(
        cls,
        *,
        year=None,
        quarter=None,
        month=None,
        day=None,
        hour=None,
        minute=None,
        second=None,
        freq=None,
    ) -> Self:
        """
        Construct a PeriodIndex from fields (year, month, day, etc.).

        Each field (year, quarter, month, day, hour, minute, second) can be
        specified as a scalar or array-like. The frequency is inferred from
        the fields provided or can be given explicitly.

        Parameters
        ----------
        year : int, array, or Series, default None
            Year for the PeriodIndex.
        quarter : int, array, or Series, default None
            Quarter for the PeriodIndex.
        month : int, array, or Series, default None
            Month for the PeriodIndex.
        day : int, array, or Series, default None
            Day for the PeriodIndex.
        hour : int, array, or Series, default None
            Hour for the PeriodIndex.
        minute : int, array, or Series, default None
            Minute for the PeriodIndex.
        second : int, array, or Series, default None
            Second for the PeriodIndex.
        freq : str or period object, optional
            One of pandas period strings or corresponding objects.

        Returns
        -------
        PeriodIndex

        See Also
        --------
        PeriodIndex.from_ordinals : Construct a PeriodIndex from ordinals.
        PeriodIndex.to_timestamp : Cast to DatetimeArray/Index.

        Examples
        --------
        >>> idx = pd.PeriodIndex.from_fields(year=[2000, 2002], quarter=[1, 3])
        >>> idx
        PeriodIndex(['2000Q1', '2002Q3'], dtype='period[Q-DEC]')
        """
        fields = {
            "year": year,
            "quarter": quarter,
            "month": month,
            "day": day,
            "hour": hour,
            "minute": minute,
            "second": second,
        }
        fields = {key: value for key, value in fields.items() if value is not None}
        arr = PeriodArray._from_fields(fields=fields, freq=freq)
        return cls._simple_new(arr)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_period_bins [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _get_time_period_bins(self, ax: DatetimeIndex):
        if not isinstance(ax, DatetimeIndex):
            raise TypeError(
                "axis must be a DatetimeIndex, but got "
                f"an instance of {type(ax).__name__}"
            )

        freq = self.freq

        if len(ax) == 0:
            binner = labels = PeriodIndex(
                data=[], freq=freq, name=ax.name, dtype=ax.dtype
            )
            return binner, [], labels

        labels = binner = period_range(start=ax[0], end=ax[-1], freq=freq, name=ax.name)

        end_stamps = (labels + freq).asfreq(freq, "s").to_timestamp()
        if ax.tz:
            end_stamps = end_stamps.tz_localize(ax.tz)
        bins = ax.searchsorted(end_stamps, side="left")

        return binner, bins, labels

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestPeriodIndexEquals.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py]
    def index(self):
        """Fixture for creating a PeriodIndex for use in equality tests."""
        return period_range("2013-01-01", periods=5, freq="D")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py]
    def time_searchsorted(self, dtype):
        key = "2" if dtype == "str" else 2
        self.s.searchsorted(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.second [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.from_ordinals [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_fill_indexer_searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _get_fill_indexer_searchsorted(
        self, target: Index, method: str_t, limit: int | None = None
    ) -> npt.NDArray[np.intp]:
        """
        Fallback pad/backfill get_indexer that works for monotonic decreasing
        indexes and non-monotonic targets.
        """
        if limit is not None:
            raise ValueError(
                f"limit argument for {method!r} method only well-defined "
                "if index and target are monotonic"
            )

        side: Literal["left", "right"] = "left" if method == "pad" else "right"

        # find exact matches first (this simplifies the algorithm)
        indexer = self.get_indexer(target)
        nonexact = indexer == -1
        indexer[nonexact] = self._searchsorted_monotonic(target[nonexact], side)
        if side == "left":
            # searchsorted returns "indices into a sorted array such that,
            # if the corresponding elements in v were inserted before the
            # indices, the order of a would be preserved".
            # Thus, we need to subtract 1 to find values to the left.
            indexer[nonexact] -= 1
            # This also mapped not found values (values of 0 from
            # np.searchsorted) to -1, which conveniently is also our
            # sentinel for missing values
        else:
            # Mark indices to the right of the largest value as not found
            indexer[indexer == len(self)] = -1
        return indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::TestPeriodArray.arr1d [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py]
    def arr1d(self, period_index):
        """
        Fixture returning DatetimeArray from parametrized PeriodIndex objects
        """
        return period_index._data

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        npvalue = self._validate_setitem_value(value).view("M8[ns]")

        # Cast to M8 to get datetime-like NaT placement,
        #  similar to dtl._period_dispatch
        m8arr = self._ndarray.view("M8[ns]")
        return m8arr.searchsorted(npvalue, side=side, sorter=sorter)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._convert_tolerance [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
    def _convert_tolerance(self, tolerance, target):
        # Returned tolerance must be in dtype/units so that
        #  `|self._get_engine_target() - target._engine_target()| <= tolerance`
        #  is meaningful.  Since PeriodIndex returns int64 for engine_target,
        #  we may need to convert timedelta64 tolerance to int64.
        tolerance = super()._convert_tolerance(tolerance, target)

        if self.dtype == target.dtype:
            # convert tolerance to i8
            tolerance = self._maybe_convert_timedelta(tolerance)

        return tolerance

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.f [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
            def f(values, freq=None, tz=None):
                dtype = PeriodDtype(freq)
                parr = PeriodArray._simple_new(values, dtype=dtype)
                return PeriodIndex._simple_new(parr, name=None)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_period_break [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py]
def _period_break(
    dates: PeriodIndex | DatetimeIndex, period: str
) -> npt.NDArray[np.intp]:
    """
    Returns the indices where the given period changes.

    Parameters
    ----------
    dates : PeriodIndex or DatetimeIndex
        Array of intervals to monitor.
    period : str
        Name of the period to monitor.
    """
    mask = _period_break_mask(dates, period)
    return np.nonzero(mask)[0]
```
