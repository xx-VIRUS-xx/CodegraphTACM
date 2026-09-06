# pandas-95 :: tacm-full

query: BUG: PeriodArray comparisons inconsistent with Period comparisons (#30722)

## selected nodes

- rank=1 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::DataFramePeriodColumn.time_set_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=2 layer=FUNCTION tokens=2324 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_daily_finder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py
- rank=3 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::TestComparison.interval_constructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py
- rank=4 layer=FUNCTION tokens=696 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=5 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=6 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._add_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=7 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py::expected_with_na_handling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py
- rank=8 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=9 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::DataFramePeriodColumn.time_set_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_set_index(self):
        # GH#21582 limited by comparisons of Period objects
        self.df["col2"] = self.rng
        self.df.set_index("col2", append=True)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::_daily_finder [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py]
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
    if n > 1:
        if periodsperday > 0:
            periodsperday = max(1, periodsperday // n)
            periodspermonth = 28 * periodsperday
            periodsperyear = 365 * periodsperday
        else:
            periodspermonth = max(1, periodspermonth // n)
            periodsperyear = max(1, periodsperyear // n)

    # save this for later usage
    vmin_orig = vmin
    (vmin, vmax) = (int(vmin), int(vmax))

    dates_: DatetimeIndex | PeriodIndex
    if freq_group == FreqGroup.FR_BUS:
        # BDay branch: use numpy business-day arithmetic to avoid
        #  (deprecated) Period[B].
        ordinals = np.arange(vmin, vmax + 1, step=freq.n, dtype=np.int64)
        dates_ = DatetimeIndex(
            np.busday_offset(np.datetime64("1970-01-01", "D"), ordinals).astype(
                "datetime64[ns]"
            ),
            freq=freq,
        )
    else:
        dates_ = period_range(
            start=Period(ordinal=vmin, freq=freq),
            end=Period(ordinal=vmax, freq=freq),
            freq=freq,
        )
        ordinals = dates_.asi8

    span = len(ordinals)

    # Initialize the output
    info = np.zeros(
        span, dtype=[("val", np.int64), ("maj", bool), ("min", bool), ("fmt", "|S20")]
    )
    info["val"][:] = ordinals
    info["fmt"][:] = ""
    info["maj"][[0, -1]] = True
    # .. and set some shortcuts
    info_maj = info["maj"]
    info_min = info["min"]
    info_fmt = info["fmt"]

    def first_label(label_flags):
        if (label_flags[0] == 0) and (label_flags.size > 1) and ((vmin_orig % 1) > 0.0):
            return label_flags[1]
        else:
            return label_flags[0]

    # Case 1. Less than a month
    if span <= periodspermonth:
        day_start = _period_break(dates_, "day")
        month_start = _period_break(dates_, "month")
        year_start = _period_break(dates_, "year")

        def _hour_finder(label_interval: int, force_year_start: bool) -> None:
            target = dates_.hour
            mask = _period_break_mask(dates_, "hour")
            info_maj[day_start] = True
            info_min[mask & (target % label_interval == 0)] = True
            info_fmt[mask & (target % label_interval == 0)] = "%H:%M"
            info_fmt[day_start] = "%H:%M\n%d-%b"
            info_fmt[year_start] = "%H:%M\n%d-%b\n%Y"
            if force_year_start and not has_level_label(year_start, vmin_orig):
                info_fmt[first_label(day_start)] = "%H:%M\n%d-%b\n%Y"

        def _minute_finder(label_interval: int) -> None:
            target = dates_.minute
            hour_start = _period_break(dates_, "hour")
            mask = _period_break_mask(dates_, "minute")
            info_maj[hour_start] = True
            info_min[mask & (target % label_interval == 0)] = True
            info_fmt[mask & (target % label_interval == 0)] = "%H:%M"
            info_fmt[day_start] = "%H:%M\n%d-%b"
            info_fmt[year_start] = "%H:%M\n%d-%b\n%Y"

        def _second_finder(label_interval: int) -> None:
            target = dates_.second
            minute_start = _period_break(dates_, "minute")
            mask = _period_break_mask(dates_, "second")
            info_maj[minute_start] = True
            info_min[mask & (target % label_interval == 0)] = True
            info_fmt[mask & (target % label_interval == 0)] = "%H:%M:%S"
            info_fmt[day_start] = "%H:%M:%S\n%d-%b"
            info_fmt[year_start] = "%H:%M:%S\n%d-%b\n%Y"

        if span < periodsperday / 12000:
            _second_finder(1)
        elif span < periodsperday / 6000:
            _second_finder(2)
        elif span < periodsperday / 2400:
            _second_finder(5)
        elif span < periodsperday / 1200:
            _second_finder(10)
        elif span < periodsperday / 800:
            _second_finder(15)
        elif span < periodsperday / 400:
            _second_finder(30)
        elif span < periodsperday / 150:
            _minute_finder(1)
        elif span < periodsperday / 70:
            _minute_finder(2)
        elif span < periodsperday / 24:
            _minute_finder(5)
        elif span < periodsperday / 12:
            _minute_finder(15)
        elif span < periodsperday / 6:
            _minute_finder(30)
        elif span < periodsperday / 2.5:
            _hour_finder(1, False)
        elif span < periodsperday / 1.5:
            _hour_finder(2, False)
        elif span < periodsperday * 1.25:
            _hour_finder(3, False)
        elif span < periodsperday * 2.5:
            _hour_finder(6, True)
        elif span < periodsperday * 4:
            _hour_finder(12, True)
        else:
            info_maj[month_start] = True
            info_min[day_start] = True
            info_fmt[day_start] = "%d"
            info_fmt[month_start] = "%d\n%b"
            info_fmt[year_start] = "%d\n%b\n%Y"
            if not has_level_label(year_start, vmin_orig):
                if not has_level_label(month_start, vmin_orig):
                    info_fmt[first_label(day_start)] = "%d\n%b\n%Y"
                else:
                    info_fmt[first_label(month_start)] = "%d\n%b\n%Y"

    # Case 2. Less than three months
    elif span <= periodsperyear // 4:
        month_start = _period_break(dates_, "month")
        info_maj[month_start] = True
        if dtype_code < FreqGroup.FR_HR.value:  # pyright: ignore[reportAttributeAccessIssue]
            info["min"] = True
        else:
            day_start = _period_break(dates_, "day")
            info["min"][day_start] = True
        week_start = _period_break(dates_, "week")
        year_start = _period_break(dates_, "year")
        info_fmt[week_start] = "%d"
        info_fmt[month_start] = "\n\n%b"
        info_fmt[year_start] = "\n\n%b\n%Y"
        if not has_level_label(year_start, vmin_orig):
            if not has_level_label(month_start, vmin_orig):
                info_fmt[first_label(week_start)] = "\n\n%b\n%Y"
            else:
                info_fmt[first_label(month_start)] = "\n\n%b\n%Y"
    # Case 3. Less than 14 months ...............
    elif span <= 1.15 * periodsperyear:
        year_start = _period_break(dates_, "year")
        month_start = _period_break(dates_, "month")
        week_start = _period_break(dates_, "week")
        info_maj[month_start] = True
        info_min[week_start] = True
        info_min[year_start] = False
        info_min[month_start] = False
        info_fmt[month_start] = "%b"
        info_fmt[year_start] = "%b\n%Y"
        if not has_level_label(year_start, vmin_orig):
            info_fmt[first_label(month_start)] = "%b\n%Y"
    # Case 4. Less than 2.5 years ...............
    elif span <= 2.5 * periodsperyear:
        year_start = _period_break(dates_, "year")
        quarter_start = _period_break(dates_, "quarter")
        month_start = _period_break(dates_, "month")
        info_maj[quarter_start] = True
        info_min[month_start] = True
        info_fmt[quarter_start] = "%b"
        info_fmt[year_start] = "%b\n%Y"
    # Case 4. Less than 4 years .................
    elif span <= 4 * periodsperyear:
        year_start = _period_break(dates_, "year")
        month_start = _period_break(dates_, "month")
        info_maj[year_start] = True
        info_min[month_start] = True
        info_min[year_start] = False

        month_break = dates_[month_start].month  # pyright: ignore[reportAttributeAccessIssue]
        jan_or_jul = month_start[(month_break == 1) | (month_break == 7)]
        info_fmt[jan_or_jul] = "%b"
        info_fmt[year_start] = "%b\n%Y"
    # Case 5. Less than 11 years ................
    elif span <= 11 * periodsperyear:
        year_start = _period_break(dates_, "year")
        quarter_start = _period_break(dates_, "quarter")
        info_maj[year_start] = True
        info_min[quarter_start] = True
        info_min[year_start] = False
        info_fmt[year_start] = "%Y"
    # Case 6. More than 12 years ................
    else:
        year_start = _period_break(dates_, "year")
        year_break = dates_[year_start].year  # pyright: ignore[reportAttributeAccessIssue]
        nyears = span / periodsperyear
        (min_anndef, maj_anndef) = _get_default_annual_spacing(nyears)
        major_idx = year_start[(year_break % maj_anndef == 0)]
        info_maj[major_idx] = True
        minor_idx = year_start[(year_break % min_anndef == 0)]
        info_min[minor_idx] = True
        info_fmt[major_idx] = "%Y"

    return info

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::TestComparison.interval_constructor [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py]
    def interval_constructor(self, request):
        """
        Fixture for all pandas native interval constructors.
        To be used as the LHS of IntervalArray comparisons.
        """
        return request.param

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py]
    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.
        StringMethods.len : Compute the length of each element in the Series/Index.

        Examples
        --------
        >>> import pyarrow as pa
        >>> s = pd.Series(
        ...     [
        ...         [1, 2, 3],
        ...         [3],
        ...     ],
        ...     dtype=pd.ArrowDtype(pa.list_(pa.int64())),
        ... )
        >>> s.list.len()
        0    3
        1    1
        dtype: int32[pyarrow]
        """
        from pandas import Series

        value_lengths = pc.list_value_length(self._pa_array)
        return Series(
            value_lengths,
            dtype=ArrowDtype(value_lengths.type),
            index=self._data.index,
            name=self._data.name,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._add_period [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _add_period(self, other: Period) -> PeriodArray:
        if not lib.is_np_dtype(self.dtype, "m"):
            raise TypeError(f"cannot add Period to a {type(self).__name__}")

        # We will wrap in a PeriodArray and defer to the reversed operation
        from pandas.core.arrays.period import PeriodArray

        i8vals = np.broadcast_to(other.ordinal, self.shape)
        dtype = PeriodDtype(other.freq)
        parr = PeriodArray(i8vals, dtype=dtype)
        return parr + self

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py::expected_with_na_handling [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py]
    def expected_with_na_handling(lvalues, rvalues, op):
        # Similar to comparison_op, handle zerodim arrays with na value separately
        if (rvalues.ndim == 0) and isna(rvalues.item()):
            # numpy does not like comparisons vs None
            if op is operator.ne:
                return np.ones(lvalues.shape, dtype=bool)
            else:
                return np.zeros(lvalues.shape, dtype=bool)
        return op(lvalues, rvalues)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py]
    def len(self, text: str) -> int:
        return len(text)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::loc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def loc(x):
    return x.loc
```
