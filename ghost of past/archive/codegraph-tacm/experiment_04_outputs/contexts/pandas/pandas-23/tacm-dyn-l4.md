# pandas-23 :: tacm-dyn-l4

query: BUG: DatetimeIndex.intersection losing freq and tz (#33604)

## selected nodes

- rank=1 layer=FILE tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=2 layer=CLASS tokens=249 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py::TestDatetimeIndexSetOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py
- rank=3 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_datetime_index.py::_create_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_datetime_index.py
- rank=4 layer=FUNCTION tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::_maybe_localize_point file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=5 layer=FUNCTION tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_period_bins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=6 layer=FILE tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=7 layer=FUNCTION tokens=334 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::_new_DatetimeIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=8 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::date_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=9 layer=CLASS tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py::TestTimedeltaIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py
- rank=10 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeIndex.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=11 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed._get_index_factory file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=12 layer=CLASS tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py::TestBusinessDatetimeIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py
- rank=13 layer=FUNCTION tokens=302 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::dt64arr_to_periodarr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=14 layer=FUNCTION tokens=238 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.write_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=15 layer=FUNCTION tokens=268 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=16 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.tz_localize file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=17 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=18 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::format_dateaxis file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=19 layer=FUNCTION tokens=445 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_convert_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=20 layer=FUNCTION tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_asfreq_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=21 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._tz_convert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=22 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._tz_localize file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=23 layer=FUNCTION tokens=178 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::_maybe_infer_tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=24 layer=FILE tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py
- rank=25 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::ResetIndex.time_reset_datetimeindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=26 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::TimeDT64ArrToPeriodArr.time_dt64arr_to_periodarr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=27 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py::TimedeltaIndexing.time_intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py

## context

```text
file core/arrays/datetimes.py
imports: __future__, datetime, typing, warnings, numpy, pandas
defines: DatetimeArray, tz_to_dtype, tz_to_dtype, tz_to_dtype, _field_accessor, f, _sequence_to_dt64, _construct_from_dt64_naive, objects_to_datetime64, maybe_convert_dtype, _maybe_infer_tz, _validate_dt64_dtype, _validate_tz_from_dtype, _infer_tz_from_endpoints, _maybe_normalize_endpoints, _maybe_localize_point, _generate_range

class TestDatetimeIndexSetOps:  [indexes/datetimes/test_setops.py:33]
methods: test_datetimeindex_diff, test_difference
         test_difference_freq, test_dti_intersection
         test_dti_setop_aware, test_dti_union_mixed
         test_intersection, test_intersection2
         test_intersection_bug_1708
         test_intersection_empty
         test_intersection_non_tick_no_fastpath
         test_intersection_same_timezone_different_units
         test_setops_preserve_freq
         test_symmetric_difference_same_timezone_different_units
         test_union, test_union2, test_union3
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_dataframe_index
         test_union_different_dates_same_timezone_different_units
         test_union_freq_both_none, test_union_freq_infer
         test_union_same_nonzero_timezone_different_units
         test_union_same_timezone_different_units
         test_union_with_DatetimeIndex

    def _create_series(values, timestamps, freq="D"):
        return Series(
            values,
            index=DatetimeIndex(
                [Timestamp(t, tz=tz) for t in timestamps], freq=freq, ambiguous=True
            ).as_unit(unit),
        )

def _maybe_localize_point(
    ts: Timestamp | None, freq, tz, ambiguous, nonexistent
) -> Timestamp | None:
    """
    Localize a start or end Timestamp to the timezone of the corresponding
    start or end Timestamp

    Parameters
    ----------
    ts : start or end Timestamp to potentially localize
    freq : Tick, DateOffset, or None
    tz : str, timezone object or None
    ambiguous: str, localization behavior for ambiguous times
    nonexistent: str, localization behavior for nonexistent times

    Returns
    -------
    ts : Timestamp
    """
    # Make sure start and end are timezone localized if:
    # 1) freq = a Timedelta-like frequency (Tick)
    # 2) freq = None i.e. generating a linspaced range
    if ts is not None and ts.tzinfo is None:
        # Note: We can't ambiguous='infer' a singular ambiguous time; however,
        # we have historically defaulted ambiguous=False
        ambiguous = ambiguous if ambiguous != "infer" else False
        localize_args = {"ambiguous": ambiguous, "nonexistent": nonexistent, "tz": None}
        if isinstance(freq, Tick) or freq is None:
            localize_args["tz"] = tz
        ts = ts.tz_localize(**localize_args)
    return ts

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

file core/indexes/datetimes.py
imports: __future__, datetime, operator, typing, warnings, numpy, pandas, collections
defines: DatetimeIndex, _new_DatetimeIndex, date_range, bdate_range, _time_to_micros

def _new_DatetimeIndex(cls, d):
    """
    This is called upon unpickling, rather than the default which doesn't
    have arguments and breaks __new__
    """
    if "data" in d and not isinstance(d["data"], DatetimeIndex):
        # Avoid need to verify integrity by calling simple_new directly
        data = d.pop("data")
        if not isinstance(data, DatetimeArray):
            # For backward compat with older pickles, we may need to construct
            #  a DatetimeArray to adapt to the newer _simple_new signature
            tz = d.pop("tz")
            freq = d.pop("freq")
            dta = DatetimeArray._simple_new(data, dtype=tz_to_dtype(tz), freq=freq)
        else:
            dta = data
            for key in ["tz", "freq"]:
                # These are already stored in our DatetimeArray; if they are
                #  also in the pickle and don't match, we have a problem.
                if key in d:
                    assert d[key] == getattr(dta, key)
                    d.pop(key)
        result = cls._simple_new(dta, **d)
    else:
        with warnings.catch_warnings():
            # TODO: If we knew what was going in to **d, we might be able to
            #  go through _simple_new instead
            warnings.simplefilter("ignore")
            result = cls.__new__(cls, **d)

    return result

def date_range(
    start=None,
    end=None,
    periods=None,
    freq=None,
    tz=None,
    normalize: bool = False,
    name: Hashable | None = None,
    inclusive: IntervalClosedType = "both",
    *,
    unit: TimeUnit | None = None,
    ambiguous: TimeAmbiguous = "raise",
    # ... truncated

class TestTimedeltaIndex:  [indexes/timedeltas/test_setops.py:17]
methods: test_intersection, test_intersection_bug_1708
         test_intersection_equal
         test_intersection_non_monotonic
         test_intersection_zero_length, test_union
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_freq_infer, test_union_sort_false
         test_zero_length_input_index

    def setup(self, index_type):
        N = 100000
        dtidxes = {
            "dst": date_range(
                start="10/29/2000 1:00:00", end="10/29/2000 1:59:59", freq="s"
            ),
            "repeated": date_range(start="2000", periods=N // 10, freq="s").repeat(10),
            "tz_aware": date_range(start="2000", periods=N, freq="s", tz="US/Eastern"),
            "tz_local": date_range(
                start="2000", periods=N, freq="s", tz=dateutil.tz.tzlocal()
            ),
            "tz_naive": date_range(start="2000", periods=N, freq="s"),
        }
        self.index = dtidxes[index_type]

    def _get_index_factory(self, attrs):
        index_class = self._alias_to_class(getattr(attrs, "index_class", ""))

        factory: Callable

        kwargs = {}
        if index_class == DatetimeIndex:

            def f(values, freq=None, tz=None):  # pyright: ignore[reportRedeclaration]
                # data are already in UTC, localize and convert if tz present
                dta = DatetimeArray._simple_new(
                    values.values, dtype=values.dtype, freq=freq
    # ... truncated

class TestBusinessDatetimeIndex:  [indexes/datetimes/test_setops.py:543]
methods: test_intersection, test_intersection_bug
         test_intersection_duplicates
         test_intersection_list
         test_month_range_union_tz_dateutil
         test_month_range_union_tz_pytz, test_union
         test_union_not_cacheable

def dt64arr_to_periodarr(
    data, freq, tz=None
) -> tuple[npt.NDArray[np.int64], BaseOffset]:
    """
    Convert a datetime-like array to values Period ordinals.

    Parameters
    ----------
    data : Union[Series[datetime64[ns]], DatetimeIndex, ndarray[datetime64ns]]
    freq : Optional[Union[str, Tick]]
        Must match the `freq` on the `data` if `data` is a DatetimeIndex
        or Series.
    tz : Optional[tzinfo]

    Returns
    -------
    ordinals : ndarray[int64]
    freq : Tick
        The frequency extracted from the Series or DatetimeIndex if that's
        used.

    """
    if not isinstance(data.dtype, np.dtype) or data.dtype.kind != "M":
        raise ValueError(f"Wrong dtype: {data.dtype}")

    if freq is None:
        if isinstance(data, ABCIndex):
            data, freq = data._values, data.freq
        elif isinstance(data, ABCSeries):
            data, freq = data._values, data.dt.freq

    elif isinstance(data, (ABCIndex, ABCSeries)):
        data = data._values

    reso = get_unit_from_dtype(data.dtype)
    freq = Period._maybe_convert_freq(freq)
    base = freq._period_dtype_code
    return c_dt64arr_to_periodarr(data.view("i8"), base, tz, reso=reso), freq

    def write_index(self, key: str, index: Index) -> None:
        if isinstance(index, MultiIndex):
            setattr(self.attrs, f"{key}_variety", "multi")
            self.write_multi_index(key, index)
        else:
            setattr(self.attrs, f"{key}_variety", "regular")
            converted = _convert_index("index", index, self.encoding, self.errors)

            self.write_array(key, converted.values)

            node = getattr(self.group, key)
            node._v_attrs.kind = converted.kind
            node._v_attrs.name = index.name

            if isinstance(index, (DatetimeIndex, PeriodIndex)):
                node._v_attrs.index_class = self._class_to_alias(type(index))

            if isinstance(index, (DatetimeIndex, PeriodIndex, TimedeltaIndex)):
                node._v_attrs.freq = index.freq

            if isinstance(index, DatetimeIndex) and index.tz is not None:
                node._v_attrs.tz = _get_tz(index.tz)

    def _intersection(self, other: Index, sort: bool = False) -> Index:
        """
        intersection specialized to the case with matching dtypes and both non-empty.
        """
        other = cast("DatetimeTimedeltaMixin", other)

        if self._can_range_setop(other):
            return self._range_intersect(other, sort=sort)

        if not self._can_fast_intersect(other):
            result = Index._intersection(self, other, sort=sort)
            # We need to invalidate the freq because Index._intersection
            #  uses _shallow_copy on a view of self._data, which will preserve
            #  self.freq if we're not careful.
            # At this point we should have result.dtype == self.dtype
            #  and type(result) is type(self._data)
            result = self._wrap_setop_result(other, result)
            # error: "Index" has no attribute "_with_freq"; maybe "_with_infer"?
            return result._with_freq(None)._with_freq("infer")  # type: ignore[attr-defined]

        else:
            return self._fast_intersect(other, sort)

    def tz_localize(
        self,
        tz,
        ambiguous: TimeAmbiguous = "raise",
        nonexistent: TimeNonexistent = "raise",
    ) -> Self:
        """
    # ... truncated

file plotting/_matplotlib/timeseries.py
imports: __future__, functools, typing, numpy, pandas, datetime, matplotlib
defines: maybe_resample, _is_sub, _is_sup, _upsample_others, _replot_ax, decorate_axes, _get_ax_freq, _get_period_alias, _get_freq, use_dynamic_x, _get_index_freq, maybe_convert_index, _format_coord, format_dateaxis, prepare_ts_data

def format_dateaxis(
    subplot, freq: BaseOffset, index: DatetimeIndex | PeriodIndex
) -> None:
    """
    # ... truncated

def maybe_convert_index(ax: Axes, data: NDFrameT) -> NDFrameT:
    # Convert DatetimeIndex to ordinal-integer index for plotting, so the
    # x-axis uses consecutive integers rather than matplotlib date2num floats.
    # This ensures evenly-spaced points: for BDay freq, Fri→Mon is a 1-unit
    # step rather than a 3-unit gap.  See GH#1482.
    if isinstance(data.index, (ABCDatetimeIndex, ABCPeriodIndex)):
        freq = _get_index_freq(data.index)

        if freq is None:
            freq = _get_ax_freq(ax)

        if freq is None:
            raise ValueError("Could not get frequency alias for plotting")

        freq_str = _get_period_alias(freq)

        if isinstance(data.index, ABCDatetimeIndex):
            if freq_str == "B":
                # Avoid creating deprecated Period[B]; use numpy business-day
                # arithmetic to map each timestamp to its business-day ordinal.
                data = data.copy(deep=False)
                data.index = Index(
                    np.busday_count(
                        np.datetime64("1970-01-01", "D"),
                        data.index.tz_localize(None).values.astype("datetime64[D]"),
                    ),
                    dtype=np.int64,
                )
            else:
                data = data.tz_localize(None).to_period(freq=freq_str)
        elif isinstance(data.index, ABCPeriodIndex):
            if freq_str == "B":
                # Extract the existing Period[B] ordinals as plain int64 to
                # avoid creating new (deprecated) Period[B] objects.
                data = data.copy(deep=False)
                data.index = Index(data.index.asi8, dtype=np.int64)
            else:
                data.index = data.index.asfreq(freq=freq_str, how="start")
    return data

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

file benchmarks/tslibs/tz_convert.py
imports: datetime, numpy, pandas, tslib
defines: TimeTZConvert

def _validate_tz_from_dtype(
    dtype, tz: tzinfo | None, explicit_tz_none: bool = False
) -> tzinfo | None:
    """
    # ... truncated

    def time_reset_datetimeindex(self, tz):
        self.df.reset_index()

    def time_dt64arr_to_periodarr(self, size, freq, tz):
        dt64arr_to_periodarr(self.i8values, freq, tz)

# --- Layer 04: Variable context ---
# call-chain context
  called by: _generate_range [datetimes.py]

# call-chain context
  called by: setup [algorithms.py]
  called by: setup [algorithms.py]

# call-chain context
  called by: read_index_node [pytables.py]

# call-chain context
  called by: time_dt64arr_to_periodarr [period.py]
  called by: _from_datetime64 [period.py]

# call-chain context
  called by: write [pytables.py]
  called by: write [pytables.py]

# call-chain context
  called by: setup [reshape.py]
  called by: time_infer_dst [timeseries.py]

# call-chain context
  called by: _ts_plot [core.py]

# call-chain context
  called by: _make_plot [core.py]
  called by: _make_plot [core.py]

# call-chain context
  called by: _wrap_result [resample.py]
  called by: ohlc [resample.py]

# call-chain context
  called by: _from_sequence_not_strict [datetimes.py]

```
