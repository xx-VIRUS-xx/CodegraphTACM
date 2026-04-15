# pandas-20 :: hybrid-cs

query: BUG: freq not retained on apply_index (#33779)

## selected nodes

- rank=1 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=2 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_asfreq_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=3 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py::TestDatetimeIndex.assert_index_parameters file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py
- rank=4 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._get_insert_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=5 layer=FUNCTION tokens=493 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_convert_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=6 layer=FUNCTION tokens=464 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._validate_frequency file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=7 layer=FUNCTION tokens=323 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::use_dynamic_x file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=8 layer=FUNCTION tokens=768 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_pin_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=9 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._can_fast_union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=10 layer=FUNCTION tokens=252 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_GroupByMixin._apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=11 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_nonmonotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=12 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=13 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestIndexing.assert_reindex_indexer_is_ok file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py
- rank=14 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._reindex_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py]
def _get_index_freq(index: Index) -> BaseOffset | None:
    freq = getattr(index, "freq", None)
    if freq is None:
        freq = getattr(index, "inferred_freq", None)
        freq = to_offset(freq)
    return freq

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py::TestDatetimeIndex.assert_index_parameters [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py]
    def assert_index_parameters(self, index):
        assert index.freq == "40960ns"
        assert index.inferred_freq == "40960ns"

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_convert_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_pin_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _maybe_pin_freq(self, freq, validate_kwds: dict) -> None:
        """
        Constructor helper to pin the appropriate `freq` attribute.  Assumes
        that self._freq is currently set to any freq inferred in
        _from_sequence_not_strict.
        """
        if freq is None:
            # user explicitly passed None -> override any inferred_freq
            self._freq = None
        elif freq == "infer":
            # if self._freq is *not* None then we already inferred a freq
            #  and there is nothing left to do
            if self._freq is None:
                # Set _freq directly to bypass duplicative _validate_frequency
                # check.
                self._freq = to_offset(self.inferred_freq)  # type: ignore[assignment]
        elif freq is lib.no_default:
            # user did not specify anything, keep inferred freq if the original
            #  data had one, otherwise do nothing
            pass
        elif self._freq is None:
            # We cannot inherit a freq from the data, so we need to validate
            #  the user-passed freq
            freq = to_offset(freq)
            type(self)._validate_frequency(self, freq, **validate_kwds)
            self._freq = freq
        else:
            # Otherwise we just need to check that the user-passed freq
            #  doesn't conflict with the one we already have.
            freq = to_offset(freq)
            if freq != self._freq:
                # GH#61086 freq may be equivalent but not equal (e.g.
                # QS-FEB vs QS-MAY), so validate against the actual data.
                if len(self) == 0:
                    pass
                elif len(self) == 1:
                    if not freq.is_on_offset(self[0]):
                        raise ValueError(
                            f"Inferred frequency {self._freq} from passed "
                            "values does not conform to passed frequency "
                            f"{freq.freqstr}"
                        )
                elif self[0] + freq == self[1]:
                    # For standard offsets, the step is a deterministic
                    # function of the date, so agreement on one step proves
                    # equivalence. For Custom/FY5253 offsets, external
                    # state (holidays, 52/53-week patterns) could cause
                    # later steps to diverge, so we validate fully.
                    if hasattr(freq, "_holidays") or isinstance(freq, FY5253Mixin):
                        type(self)._validate_frequency(self, freq, **validate_kwds)
                else:
                    raise ValueError(
                        f"Inferred frequency {self._freq} from passed "
                        "values does not conform to passed frequency "
                        f"{freq.freqstr}"
                    )
            self._freq = freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._can_fast_union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _can_fast_union(self, other: Self) -> bool:
        # Assumes that type(self) == type(other), as per the annotation
        # The ability to fast_union also implies that `freq` should be
        #  retained on union.
        freq = self.freq

        if freq is None or freq != other.freq:
            return False

        if not self.is_monotonic_increasing:
            # Because freq is not None, we must then be monotonic decreasing
            # TODO: do union on the reversed indexes?
            return False

        if len(self) == 0 or len(other) == 0:
            # only reached via union_many
            return True

        # to make our life easier, "sort" the two ranges
        if self[0] <= other[0]:
            left, right = self, other
        else:
            left, right = other, self

        right_start = right[0]
        left_end = left[-1]

        # Only need to "adjoin", not overlap
        return (right_start == left_end + freq) or right_start in left

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def index_indexing(index, idx):
    if isinstance(index, IndexType):

        def index_getitem(index, idx):
            return index._data[idx]

        return index_getitem

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestIndexing.assert_reindex_indexer_is_ok [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py]
        def assert_reindex_indexer_is_ok(mgr, axis, new_labels, indexer, fill_value):
            mat = _as_array(mgr)
            reindexed_mat = algos.take_nd(mat, indexer, axis, fill_value=fill_value)
            reindexed = mgr.reindex_indexer(
                new_labels, indexer, axis, fill_value=fill_value
            )
            tm.assert_numpy_array_equal(
                reindexed_mat, _as_array(reindexed), check_dtype=False
            )
            tm.assert_index_equal(reindexed.axes[axis], new_labels)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._reindex_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _reindex_indexer(
        self,
        new_index: Index | None,
        indexer: npt.NDArray[np.intp] | None,
    ) -> Series:
        # Note: new_index is None iff indexer is None
        # if not None, indexer is np.intp
        if indexer is None and (
            new_index is None or new_index.names == self.index.names
        ):
            return self.copy(deep=False)

        new_values = algorithms.take_nd(
            self._values, indexer, allow_fill=True, fill_value=None
        )
        return self._constructor(new_values, index=new_index, copy=False)
```
