# pandas-95 :: minilm

query: BUG: PeriodArray comparisons inconsistent with Period comparisons (#30722)

## selected nodes

- rank=1 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=2 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimePeriodArrToDT64Arr.time_periodarray_to_dt64arr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=3 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::assert_period_array_equal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py
- rank=4 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::TestPeriodArray.arr1d file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=5 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_period_break file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py
- rank=6 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._convert_tolerance file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=7 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._from_datetime64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=8 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=9 layer=FUNCTION tokens=696 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=10 layer=FUNCTION tokens=485 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=11 layer=FUNCTION tokens=241 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._difference_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=12 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.f file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=13 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::_new_PeriodIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=14 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestPeriodIndexEquals.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
- rank=15 layer=FUNCTION tokens=429 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::period_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=16 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::_simple_period_range_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py
- rank=17 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py
- rank=18 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::datetime_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=19 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._sub_periodlike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=20 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py::arr_shape file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimePeriodArrToDT64Arr.time_periodarray_to_dt64arr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def time_periodarray_to_dt64arr(self, size, freq):
        periodarr_to_dt64arr(self.i8values, freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::assert_period_array_equal [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py]
def assert_period_array_equal(left, right, obj: str = "PeriodArray") -> None:
    _check_isinstance(left, right, PeriodArray)

    assert_numpy_array_equal(left._ndarray, right._ndarray, obj=f"{obj}._ndarray")
    assert_attr_equal("dtype", left, right, obj=obj)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::TestPeriodArray.arr1d [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py]
    def arr1d(self, period_index):
        """
        Fixture returning DatetimeArray from parametrized PeriodIndex objects
        """
        return period_index._data

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._from_datetime64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def _from_datetime64(cls, data, freq, tz=None) -> Self:
        """
        Construct a PeriodArray from a datetime64 array

        Parameters
        ----------
        data : ndarray[datetime64[ns], datetime64[ns, tz]]
        freq : str or Tick
        tz : tzinfo, optional

        Returns
        -------
        PeriodArray[freq]
        """
        if isinstance(freq, BaseOffset):
            freq = PeriodDtype(freq)._freqstr
        data, freq = dt64arr_to_periodarr(data, freq, tz)
        dtype = PeriodDtype(freq)
        return cls(data, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def freq(self, value) -> None:
        # error: Property "freq" defined in "PeriodArray" is read-only  [misc]
        self._data.freq = value  # type: ignore[misc]

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._difference_compat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _difference_compat(
        self, target: Index, indexer: npt.NDArray[np.intp]
    ) -> ArrayLike:
        # Compatibility for PeriodArray, for which __sub__ returns an ndarray[object]
        #  of DateOffset objects, which do not support __abs__ (and would be slow
        #  if they did)

        if isinstance(self.dtype, PeriodDtype):
            # Note: we only get here with matching dtypes
            own_values = cast("PeriodArray", self._data)._ndarray
            target_values = cast("PeriodArray", target._data)._ndarray
            diff = own_values[indexer] - target_values
        else:
            # error: Unsupported left operand type for - ("ExtensionArray")
            diff = self._values[indexer] - target._values  # type: ignore[operator]
        return abs(diff)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.f [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
            def f(values, freq=None, tz=None):
                dtype = PeriodDtype(freq)
                parr = PeriodArray._simple_new(values, dtype=dtype)
                return PeriodIndex._simple_new(parr, name=None)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestPeriodIndexEquals.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py]
    def index(self):
        """Fixture for creating a PeriodIndex for use in equality tests."""
        return period_range("2013-01-01", periods=5, freq="D")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::period_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
def period_array(
    data: Sequence[Period | str | None] | AnyArrayLike,
    dtype: PeriodDtype | None = None,
) -> PeriodArray:
    """
    Construct a new PeriodArray from a sequence of Period scalars.

    Parameters
    ----------
    data : Sequence of Period objects
        A sequence of Period objects. These are required to all have
        the same ``freq.`` Missing values can be indicated by ``None``
        or ``pandas.NaT``.
    dtype : PeriodDtype or None, default None
        The dtype for the array. If not specified, is inferred from the data.

    Returns
    -------
    PeriodArray

    See Also
    --------
    PeriodArray
    pandas.PeriodIndex

    Examples
    --------
    >>> period_array([pd.Period("2017", freq="Y"), pd.Period("2018", freq="Y")])
    <PeriodArray>
    ['2017', '2018']
    Length: 2, dtype: period[Y-DEC]

    >>> period_array([pd.Period("2017", freq="Y"), pd.Period("2018", freq="Y"), pd.NaT])
    <PeriodArray>
    ['2017', '2018', 'NaT']
    Length: 3, dtype: period[Y-DEC]

    Integers that look like years are handled

    >>> period_array([2000, 2001, 2002], dtype=PeriodDtype("D"))
    <PeriodArray>
    ['2000-01-01', '2001-01-01', '2002-01-01']
    Length: 3, dtype: period[D]

    Datetime-like strings may also be passed

    >>> period_array(
    ...     ["2000-Q1", "2000-Q2", "2000-Q3", "2000-Q4"], dtype=PeriodDtype("Q")
    ... )
    <PeriodArray>
    ['2000Q1', '2000Q2', '2000Q3', '2000Q4']
    Length: 4, dtype: period[Q-DEC]
    """
    return PeriodArray._from_sequence(data, dtype=dtype)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py]
def data(dtype):
    return PeriodArray(np.arange(1970, 1980), dtype=dtype)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._sub_periodlike [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _sub_periodlike(self, other: Period | PeriodArray) -> npt.NDArray[np.object_]:
        # If the operation is well-defined, we return an object-dtype ndarray
        # of DateOffsets.  Null entries are filled with pd.NaT
        if not isinstance(self.dtype, PeriodDtype):
            raise TypeError(
                f"cannot subtract {type(other).__name__} from {type(self).__name__}"
            )

        self = cast("PeriodArray", self)
        self._check_compatible_with(other)

        other_i8, o_mask = self._get_i8_values_and_mask(other)
        new_i8_data = add_overflowsafe(self.asi8, np.asarray(-other_i8, dtype="i8"))
        new_data = np.array([self.freq.base * x for x in new_i8_data])

        if o_mask is None:
            # i.e. Period scalar
            mask = self._isnan
        else:
            # i.e. PeriodArray
            mask = self._isnan | o_mask
        new_data[mask] = NaT
        return new_data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py::arr_shape [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py]
def arr_shape():
    return 11, 7
```
