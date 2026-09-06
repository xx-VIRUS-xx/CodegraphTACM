# pandas-23 :: tacm-full

query: BUG: DatetimeIndex.intersection losing freq and tz (#33604)

## selected nodes

- rank=1 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_datetime_index.py::_create_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_datetime_index.py
- rank=2 layer=FUNCTION tokens=240 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_period_bins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=3 layer=FUNCTION tokens=409 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed._get_index_factory file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=4 layer=FUNCTION tokens=277 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.write_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=5 layer=FUNCTION tokens=344 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::dt64arr_to_periodarr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=6 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_asfreq_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=7 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._tz_convert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=8 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::_new_DatetimeIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=9 layer=FUNCTION tokens=807 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_bins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=10 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._tz_localize file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=11 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=12 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._from_datetime64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=13 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py::TimeTZConvert.time_tz_localize_to_utc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py
- rank=14 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py::TimeTZConvert.time_tz_convert_from_utc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py
- rank=15 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::ResetIndex.time_reset_datetimeindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_datetime_index.py::_create_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_datetime_index.py]
    def _create_series(values, timestamps, freq="D"):
        return Series(
            values,
            index=DatetimeIndex(
                [Timestamp(t, tz=tz) for t in timestamps], freq=freq, ambiguous=True
            ).as_unit(unit),
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.write_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::dt64arr_to_periodarr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._tz_convert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
        def _tz_convert(ax, tz):
            if not hasattr(ax, "tz_convert"):
                if len(ax) > 0:
                    ax_name = self._get_axis_name(axis)
                    raise TypeError(
                        f"{ax_name} is not a valid DatetimeIndex or PeriodIndex"
                    )
                ax = DatetimeIndex([], tz=tz)
            else:
                ax = ax.tz_convert(tz)
            return ax

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::_new_DatetimeIndex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_bins [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _get_time_bins(self, ax: DatetimeIndex):
        if not isinstance(ax, DatetimeIndex):
            raise TypeError(
                "axis must be a DatetimeIndex, but got "
                f"an instance of {type(ax).__name__}"
            )

        if len(ax) == 0:
            binner = labels = DatetimeIndex(
                data=[], freq=self.freq, name=ax.name, dtype=ax.dtype
            )
            return binner, [], labels

        # GH#43486: filter NaTs up front, mirroring _get_period_bins
        nat_count = 0
        if ax.hasnans:
            nat_count = ax.isna().sum()
            ax = ax[~ax.isna()]

        if len(ax) == 0:
            # all-NaT case
            binner = labels = DatetimeIndex(
                data=[], freq=self.freq, name=ax.name, dtype=ax.dtype
            )
            bins = np.array([], dtype=np.int64)
            binner = binner.insert(0, NaT)
            labels = labels.insert(0, NaT)
            return binner, np.insert(bins, 0, nat_count), labels

        first, last = _get_timestamp_range_edges(
            ax.min(),  # type: ignore[arg-type]
            ax.max(),  # type: ignore[arg-type]
            self.freq,
            unit=ax.unit,
            closed=self.closed,
            origin=self.origin,
            offset=self.offset,
        )
        # GH #12037
        # use first/last directly instead of call replace() on them
        # because replace() will swallow the nanosecond part
        # thus last bin maybe slightly before the end if the end contains
        # nanosecond part and lead to `Values falls after last bin` error
        # GH 25758: If DST lands at midnight (e.g. 'America/Havana'), user feedback
        # has noted that ambiguous=True provides the most sensible result
        binner = labels = date_range(
            freq=self.freq,
            start=first,
            end=last,
            tz=ax.tz,
            name=ax.name,
            ambiguous=True,
            nonexistent="shift_forward",
            unit=ax.unit,
        )

        ax_values = ax.asi8
        binner, bin_edges = self._adjust_bin_edges(binner, ax_values)

        # general version, knowing nothing about relative frequencies
        bins = lib.generate_bins_dt64(ax_values, bin_edges, self.closed, hasnans=False)

        if self.closed == "right":
            labels = binner
            if self.label == "right":
                labels = labels[1:]  # type: ignore[assignment]
        elif self.label == "right":
            labels = labels[1:]  # type: ignore[assignment]

        if nat_count > 0:
            # shift bins by the number of NaT (they sort to the front of asi8)
            bins = bins + nat_count
            bins = np.insert(bins, 0, nat_count)
            binner = binner.insert(0, NaT)
            labels = labels.insert(0, NaT)

        # if we end up with more labels than bins
        # adjust the labels
        # GH4076
        if len(bins) < len(labels):
            labels = labels[: len(bins)]  # type: ignore[assignment]

        return binner, bins, labels

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._tz_localize [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
        def _tz_localize(ax, tz, ambiguous, nonexistent):
            if not hasattr(ax, "tz_localize"):
                if len(ax) > 0:
                    ax_name = self._get_axis_name(axis)
                    raise TypeError(
                        f"{ax_name} is not a valid DatetimeIndex or PeriodIndex"
                    )
                ax = DatetimeIndex([], tz=tz)
            else:
                ax = ax.tz_localize(tz, ambiguous=ambiguous, nonexistent=nonexistent)
            return ax

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py::TimeTZConvert.time_tz_localize_to_utc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py]
    def time_tz_localize_to_utc(self, size, tz):
        # effectively:
        #  dti = DatetimeIndex(self.i8data)
        #  dti.tz_localize(tz, ambiguous="NaT", nonexistent="NaT")
        tz_localize_to_utc(self.i8data, tz, ambiguous="NaT", nonexistent="NaT")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py::TimeTZConvert.time_tz_convert_from_utc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py]
    def time_tz_convert_from_utc(self, size, tz):
        # effectively:
        #  dti = DatetimeIndex(self.i8data, tz=tz)
        #  dti.tz_localize(None)
        if old_sig:
            tz_convert_from_utc(self.i8data, timezone.utc, tz)
        else:
            tz_convert_from_utc(self.i8data, tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::ResetIndex.time_reset_datetimeindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_reset_datetimeindex(self, tz):
        self.df.reset_index()
```
