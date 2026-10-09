# pandas-20 :: hybrid

query: BUG: freq not retained on apply_index (#33779)

## selected nodes

- rank=1 layer=FUNCTION tokens=361 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=2 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_asfreq_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=3 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_nonmonotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=4 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=5 layer=FUNCTION tokens=252 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_GroupByMixin._apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=6 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._get_insert_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=7 layer=FUNCTION tokens=464 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._validate_frequency file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=8 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=9 layer=FUNCTION tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling._validate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=10 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_ascending file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=11 layer=FUNCTION tokens=323 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::use_dynamic_x file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=12 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::DatetimeIndexResampler._wrap_result file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=13 layer=FUNCTION tokens=409 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed._get_index_factory file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=14 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.apply_series_numba file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=15 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sasreader.py::SASReader.close file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sasreader.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py]
def _get_index_freq(index: Index) -> BaseOffset | None:
    freq = getattr(index, "freq", None)
    if freq is None:
        freq = getattr(index, "inferred_freq", None)
        freq = to_offset(freq)
    return freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_GroupByMixin._apply [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._get_insert_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _get_insert_freq(self, loc: int, item):
        """
        Find the `freq` for self.insert(loc, item).
        """
        value = self._data._validate_scalar(item)
        item = self._data._box_func(value)

        freq = None
        if self.freq is not None:
            # freq can be preserved on edge cases
            if self.size:
                if item is NaT:
                    pass
                elif loc in (0, -len(self)) and item + self.freq == self[0]:
                    freq = self.freq
                elif (loc == len(self)) and item - self.freq == self[-1]:
                    freq = self.freq
            # Adding a single item to an empty index may preserve freq
            elif isinstance(self.freq, Tick):
                # all TimedeltaIndex cases go through here; is_on_offset
                #  would raise TypeError
                freq = self.freq
            elif self.freq.is_on_offset(item):
                freq = self.freq
        return freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._validate_frequency [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _validate_frequency(cls, index, freq: BaseOffset, **kwargs) -> None:
        """
        Validate that a frequency is compatible with the values of a given
        Datetime Array/Index or Timedelta Array/Index

        Parameters
        ----------
        index : DatetimeIndex or TimedeltaIndex
            The index on which to determine if the given frequency is valid
        freq : DateOffset
            The frequency to validate
        """
        inferred = index.inferred_freq
        if index.size == 0 or inferred == freq.freqstr:
            return None

        try:
            on_freq = cls._generate_range(
                start=index[0],
                end=None,
                periods=len(index),
                freq=freq,
                unit=index.unit,
                **kwargs,
            )
            if not np.array_equal(index.asi8, on_freq.asi8):
                raise ValueError
        except ValueError as err:
            if "non-fixed" in str(err):
                # non-fixed frequencies are not meaningful for timedelta64;
                #  we retain that error message
                raise err
            # GH#11587 the main way this is reached is if the `np.array_equal`
            #  check above is False.  This can also be reached if index[0]
            #  is `NaT`, in which case the call to `cls._generate_range` will
            #  raise a ValueError, which we re-raise with a more targeted
            #  message.
            raise ValueError(
                f"Inferred frequency {inferred} from passed values "
                f"does not conform to passed frequency {freq.freqstr}"
            ) from err

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling._validate [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def _validate(self) -> None:
        super()._validate()

        # we allow rolling on a datetimelike index
        if (
            self.obj.empty
            or isinstance(self._on, (DatetimeIndex, TimedeltaIndex, PeriodIndex))
            or (isinstance(self._on.dtype, ArrowDtype) and self._on.dtype.kind in "mM")
        ) and isinstance(self.window, (str, BaseOffset, timedelta)):
            self._validate_datetimelike_monotonic()

            # this will raise ValueError on non-fixed freqs
            try:
                freq = to_offset(self.window)
            except (TypeError, ValueError) as err:
                raise ValueError(
                    f"passed window {self.window} is not "
                    "compatible with a datetimelike index"
                ) from err
            if isinstance(self._on, PeriodIndex):
                # error: Incompatible types in assignment (expression has type
                # "float", variable has type "Optional[int]")
                self._win_freq_i8 = freq.nanos / (  # type: ignore[assignment]
                    self._on.freq.nanos / self._on.freq.n
                )
            else:
                try:
                    unit = dtype_to_unit(self._on.dtype)  # type: ignore[arg-type]
                except TypeError:
                    # if not a datetime dtype, eg for empty dataframes
                    unit = "ns"
                unit = cast("TimeUnit", unit)
                self._win_freq_i8 = Timedelta(freq.nanos).as_unit(unit)._value

            # min_periods must be an integer
            if self.min_periods is None:
                self.min_periods = 1

            if self.step is not None:
                raise NotImplementedError(
                    "step is not supported with frequency windows"
                )

        elif isinstance(self.window, BaseIndexer):
            # Passed BaseIndexer subclass should handle all other rolling kwargs
            pass
        elif not is_integer(self.window) or self.window < 0:
            raise ValueError("window must be an integer 0 or greater")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::use_dynamic_x [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed._get_index_factory [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def _get_index_factory(self, attrs):
        index_class = self._alias_to_class(getattr(attrs, "index_class", ""))

        factory: Callable

        kwargs = {}
        if index_class == DatetimeIndex:

            def f(values, freq=None, tz=None):  # pyright: ignore[reportRedeclaration]
                # data are already in UTC, localize and convert if tz present
                dta = DatetimeArray._simple_new(
                    values.values, dtype=values.dtype, freq=freq
                )
                result = DatetimeIndex._simple_new(dta, name=None)
                if tz is not None:
                    result = result.tz_localize("UTC").tz_convert(tz)
                return result

            factory = f
        elif index_class == PeriodIndex:

            def f(values, freq=None, tz=None):
                dtype = PeriodDtype(freq)
                parr = PeriodArray._simple_new(values, dtype=dtype)
                return PeriodIndex._simple_new(parr, name=None)

            factory = f
        else:
            factory = index_class
            kwargs["copy"] = False

        if "freq" in attrs:
            kwargs["freq"] = attrs["freq"]
            if index_class is Index:
                # DTI/PI would be gotten by _alias_to_class
                factory = TimedeltaIndex

        if "tz" in attrs:
            kwargs["tz"] = attrs["tz"]
            assert index_class is DatetimeIndex  # just checking

        return factory, kwargs

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.apply_series_numba [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def apply_series_numba(self):
        if self.engine_kwargs.get("parallel", False):
            raise NotImplementedError(
                "Parallel apply is not supported when raw=False and engine='numba'"
            )
        if not self.obj.index.is_unique or not self.columns.is_unique:
            raise NotImplementedError(
                "The index/columns must be unique when raw=False and engine='numba'"
            )
        self.validate_values_for_numba()
        results = self.apply_with_numba()
        return results, self.result_index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sasreader.py::SASReader.close [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sasreader.py]
    def close(self) -> None: ...
```
