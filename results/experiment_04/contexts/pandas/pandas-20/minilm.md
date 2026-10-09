# pandas-20 :: minilm

query: BUG: freq not retained on apply_index (#33779)

## selected nodes

- rank=1 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=2 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_clear_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=3 layer=FUNCTION tokens=361 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=4 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py
- rank=5 layer=FUNCTION tokens=315 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::_new_Index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=6 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py::TimedeltaProperties.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py
- rank=7 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::datetime_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=8 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_asfreq_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=9 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=10 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=11 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::mismatched_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py
- rank=12 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=13 layer=FUNCTION tokens=484 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._check_indexing_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=14 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_with_cache file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=15 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py
- rank=16 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py
- rank=17 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_no_cache file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=18 layer=FUNCTION tokens=227 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py::DatetimeProperties.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py
- rank=19 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::DatetimeIndexResampler._wrap_result file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=20 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._raise_invalid_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=21 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_nonmonotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=22 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::maybe_droplevels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=23 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameColumnApply.result_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=24 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=25 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.result_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py]
def _get_index_freq(index: Index) -> BaseOffset | None:
    freq = getattr(index, "freq", None)
    if freq is None:
        freq = getattr(index, "inferred_freq", None)
        freq = to_offset(freq)
    return freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_clear_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _maybe_clear_freq(self) -> None:
        self._freq = None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def _shift_with_freq(self, periods: int, axis: int, freq) -> Self:
        # see shift.__doc__
        # when freq is given, index is shifted, data is not
        index = self._get_axis(axis)

        if freq == "infer":
            freq = getattr(index, "freq", None)

            if freq is None:
                freq = getattr(index, "inferred_freq", None)

            if freq is None:
                msg = "Freq was not set in the index hence cannot be inferred"
                raise ValueError(msg)

        elif isinstance(freq, str):
            is_period = isinstance(index, PeriodIndex)
            freq = to_offset(freq, is_period=is_period)

        if isinstance(index, PeriodIndex):
            orig_freq = to_offset(index.freq)
            if freq != orig_freq:
                assert orig_freq is not None  # for mypy
                raise ValueError(
                    f"Given freq {PeriodDtype(freq)._freqstr} "
                    f"does not match PeriodIndex freq "
                    f"{PeriodDtype(orig_freq)._freqstr}"
                )
            new_ax: Index = index.shift(periods)
        else:
            new_ax = index.shift(periods, freq)

        result = self.set_axis(new_ax, axis=axis)
        return result.__finalize__(self, method="shift")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py]
    def freq(self):
        return self._freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::_new_Index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
def _new_Index(cls: type[Index], d: dict) -> Index:
    """
    This is called upon unpickling, rather than the default which doesn't
    have arguments and breaks __new__.
    """
    # required for backward compat, because PI can't be instantiated with
    # ordinals through __new__ GH #13277
    d["copy"] = False
    if issubclass(cls, ABCPeriodIndex):
        from pandas.core.indexes.period import _new_PeriodIndex

        return _new_PeriodIndex(cls, **d)  # type: ignore[no-untyped-call]

    if issubclass(cls, ABCMultiIndex):
        if "labels" in d and "codes" not in d:
            # GH#23752 "labels" kwarg has been replaced with "codes"
            d["codes"] = d.pop("labels")

        # Since this was a valid MultiIndex at pickle-time, we don't need to
        #  check validty at un-pickle time.
        d["verify_integrity"] = False

    elif "dtype" not in d and "data" in d:
        # Prevent Index.__new__ from conducting inference;
        #  "data" key not in RangeIndex
        d["dtype"] = d["data"].dtype
    return cls.__new__(cls, **d)  # pyright: ignore[reportArgumentType]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py::TimedeltaProperties.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py]
    def freq(self):
        return self._get_values().inferred_freq

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_asfreq_compat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
def _asfreq_compat(index: FreqIndexT, freq) -> FreqIndexT:
    """
    Helper to mimic asfreq on (empty) DatetimeIndex and TimedeltaIndex.

    Parameters
    ----------
    index : PeriodIndex, DatetimeIndex, or TimedeltaIndex
    freq : DateOffset

    Returns
    -------
    same type as index
    """
    if len(index) != 0:
        # This should never be reached, always checked by the caller
        raise ValueError(
            "Can only set arbitrary freq for empty DatetimeIndex or TimedeltaIndex"
        )
    if isinstance(index, PeriodIndex):
        new_index = index.asfreq(freq=freq)
    elif isinstance(index, DatetimeIndex):
        new_index = DatetimeIndex([], dtype=index.dtype, freq=freq, name=index.name)
    elif isinstance(index, TimedeltaIndex):
        new_index = TimedeltaIndex([], dtype=index.dtype, freq=freq, name=index.name)
    else:  # pragma: no cover
        raise TypeError(type(index))
    return new_index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def freq(self, value) -> None:
        if value is not None:
            value = to_offset(value)
            self._validate_frequency(self, value)
            if self.dtype.kind == "m" and not isinstance(value, (Tick, Day)):
                raise TypeError("TimedeltaArray/Index freq must be a Tick")

            if self.ndim > 1:
                raise ValueError("Cannot set freq with ndim > 1")

        self._freq = value

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::mismatched_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py]
def mismatched_freq(request):
    """
    Several timedelta-like and DateOffset instances that are _not_
    compatible with Monthly or Annual frequencies.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def freq(self, value) -> None:
        # error: Property "freq" defined in "PeriodArray" is read-only  [misc]
        self._data.freq = value  # type: ignore[misc]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._check_indexing_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _check_indexing_method(
        self,
        method: str_t | None,
        limit: int | None = None,
        tolerance: Any = None,
    ) -> None:
        """
        Raise if we have a get_indexer `method` that is not supported or valid.
        """
        if method not in [None, "bfill", "backfill", "pad", "ffill", "nearest"]:
            # in practice the clean_reindex_fill_method call would raise
            #  before we get here
            raise ValueError("Invalid fill method")  # pragma: no cover

        if self._is_multi:
            if method == "nearest":
                raise NotImplementedError(
                    "method='nearest' not implemented yet "
                    "for MultiIndex; see GitHub issue 9365"
                )
            if method in ("pad", "backfill"):
                if tolerance is not None:
                    raise NotImplementedError(
                        "tolerance not implemented yet for MultiIndex"
                    )

        if isinstance(self.dtype, (IntervalDtype, CategoricalDtype)):
            # GH#37871 for now this is only for IntervalIndex and CategoricalIndex
            if method is not None:
                raise NotImplementedError(
                    f"method {method} not yet implemented for {type(self).__name__}"
                )

        if method is None:
            if tolerance is not None:
                raise ValueError(
                    "tolerance argument only valid if doing pad, "
                    "backfill or nearest reindexing"
                )
            if limit is not None:
                raise ValueError(
                    "limit argument only valid if doing pad, "
                    "backfill or nearest reindexing"
                )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_with_cache [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_reindex_multiindex_with_cache(self):
        # MultiIndex._values gets cached
        self.s.reindex(self.s_subset.index)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py]
    def __init__(self, freq) -> None:
        # attributes need to be set first before calling
        # super init (as that calls serialize)
        self._freq = freq
        pyarrow.ExtensionType.__init__(self, pyarrow.int64(), "pandas.period")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py]
    def index(self) -> bool:
        return self.fmt.index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_no_cache [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_reindex_multiindex_no_cache(self):
        # Copy to avoid MultiIndex._values getting cached
        self.s.reindex(self.s_subset_no_cache.index.copy())

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::DatetimeIndexResampler._wrap_result [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _wrap_result(self, result):
        result = super()._wrap_result(result)

        # we may have a different kind that we were asked originally
        # convert if needed
        if isinstance(self.ax, PeriodIndex) and not isinstance(
            result.index, PeriodIndex
        ):
            if isinstance(result.index, MultiIndex):
                # GH 24103 - e.g. groupby resample
                if not isinstance(result.index.levels[-1], PeriodIndex):
                    new_level = result.index.levels[-1].to_period(self.freq)
                    result.index = result.index.set_levels(new_level, level=-1)
            else:
                result.index = result.index.to_period(self.freq)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._raise_invalid_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _raise_invalid_indexer(
        self,
        form: Literal["slice", "positional"],
        key: object,
        reraise: lib.NoDefault | None | Exception = lib.no_default,
    ) -> None:
        """
        Raise consistent invalid indexer message.
        """
        msg = (
            f"cannot do {form} indexing on {type(self).__name__} with these "
            f"indexers [{key}] of type {type(key).__name__}"
        )
        if reraise is not lib.no_default:
            raise TypeError(msg) from reraise
        raise TypeError(msg)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::maybe_droplevels [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
def maybe_droplevels(index: Index, key) -> Index:
    """
    Attempt to drop level or levels from the given index.

    Parameters
    ----------
    index: Index
    key : scalar or tuple

    Returns
    -------
    Index
    """
    # drop levels
    original_index = index
    if isinstance(key, tuple):
        # Caller is responsible for ensuring the key is not an entry in the first
        #  level of the MultiIndex.
        for _ in key:
            try:
                index = index._drop_level_numbers([0])
            except ValueError:
                # we have dropped too much, so back out
                return original_index
    else:
        try:
            index = index._drop_level_numbers([0])
        except ValueError:
            pass

    return index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameColumnApply.result_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def result_index(self) -> Index:
        return self.index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def freq(self) -> BaseOffset:  # type: ignore[override]
        """
        Return the frequency object for this PeriodArray.
        """
        return self.dtype.freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.result_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def result_index(self) -> Index:
        pass
```
