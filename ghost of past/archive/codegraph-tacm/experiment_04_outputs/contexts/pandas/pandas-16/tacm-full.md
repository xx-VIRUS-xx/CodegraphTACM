# pandas-16 :: tacm-full

query: BUG: incorrect freq in PeriodIndex-Period (#33801)

## selected nodes

- rank=1 layer=FUNCTION tokens=485 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=2 layer=FUNCTION tokens=696 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=3 layer=FUNCTION tokens=458 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.asfreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=4 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::Algorithms.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=5 layer=FUNCTION tokens=354 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.from_ordinals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=6 layer=FUNCTION tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.hour file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=7 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.minute file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=8 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.second file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=9 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=10 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestPeriodIndexEquals.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
- rank=11 layer=FUNCTION tokens=714 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::period_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=12 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py::TestDropDuplicatesPeriodIndex.idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py
- rank=13 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::TestPeriodArray.arr1d file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=14 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.asfreq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
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
            Whether the elements should be aligned to the end
            or start within pa period.

            * 'E', 'END', or 'FINISH' for end,
            * 'S', 'START', or 'BEGIN' for start.

            January 31st ('END') vs. January 1st ('START') for example.

        Returns
        -------
        PeriodIndex
            The transformed PeriodIndex with the new frequency.

        See Also
        --------
        arrays.PeriodArray.asfreq: Convert each Period in a PeriodArray to
            the given frequency.
        Period.asfreq : Convert a :class:`~pandas.Period` object to the given frequency.

        Examples
        --------
        >>> pidx = pd.period_range("2010-01-01", "2015-01-01", freq="Y")
        >>> pidx
        PeriodIndex(['2010', '2011', '2012', '2013', '2014', '2015'],
        dtype='period[Y-DEC]')

        >>> pidx.asfreq("M")
        PeriodIndex(['2010-12', '2011-12', '2012-12', '2013-12', '2014-12',
        '2015-12'], dtype='period[M]')

        >>> pidx.asfreq("M", how="S")
        PeriodIndex(['2010-01', '2011-01', '2012-01', '2013-01', '2014-01',
        '2015-01'], dtype='period[M]')
        """
        arr = self._data.asfreq(freq, how)
        return type(self)._simple_new(arr, name=self.name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::Algorithms.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def setup(self, typ):
        data = [
            Period("2011-01", freq="M"),
            Period("2011-02", freq="M"),
            Period("2011-03", freq="M"),
            Period("2011-04", freq="M"),
        ]

        if typ == "index":
            self.vector = PeriodIndex(data * 1000, freq="M")
        elif typ == "series":
            self.vector = Series(data * 1000)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.hour [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.minute [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py::TestDropDuplicatesPeriodIndex.idx [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py]
    def idx(self, freq):
        """
        Fixture to get PeriodIndex for 10 periods for different frequencies.
        """
        return period_range("2011-01-01", periods=10, freq=freq, name="idx")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::TestPeriodArray.arr1d [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py]
    def arr1d(self, period_index):
        """
        Fixture returning DatetimeArray from parametrized PeriodIndex objects
        """
        return period_index._data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::loc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def loc(x):
    return x.loc
```
