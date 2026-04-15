# pandas-20 :: tacm-full

query: BUG: freq not retained on apply_index (#33779)

## selected nodes

- rank=1 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._can_fast_union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=2 layer=FUNCTION tokens=252 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_GroupByMixin._apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=3 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._get_insert_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=4 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=5 layer=FUNCTION tokens=361 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=6 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::check_freq_nonmonotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=7 layer=FUNCTION tokens=242 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::DatetimeIndexResampler._downsample file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=8 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_asfreq_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=9 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.apply_func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=10 layer=FUNCTION tokens=454 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_resample file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=11 layer=FUNCTION tokens=869 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._validate_left_right_on file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=12 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_cross_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py]
    def len(self):
        """
        Compute the length of each element in the Series/Index.

        The element may be a sequence (such as a string, tuple or list) or a collection
        (such as a dictionary).

        Returns
        -------
        Series or Index of int
            A Series or Index of integer values indicating the length of each
            element in the Series or Index.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.

        Examples
        --------
        Returns the length (number of characters) in a string. Returns the
        number of entries for dictionaries, lists or tuples.

        >>> s = pd.Series(
        ...     ["dog", "", 5, {"foo": "bar"}, [2, 3, 5, 7], ("one", "two", "three")]
        ... )
        >>> s
        0                  dog
        1
        2                    5
        3       {'foo': 'bar'}
        4         [2, 3, 5, 7]
        5    (one, two, three)
        dtype: object
        >>> s.str.len()
        0    3.0
        1    0.0
        2    NaN
        3    1.0
        4    4.0
        5    3.0
        dtype: float64
        """
        result = self._data.array._str_len()
        return self._wrap_result(result, returns_string=False)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::DatetimeIndexResampler._downsample [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _downsample(self, how, **kwargs):
        """
        Downsample the cython defined function.

        Parameters
        ----------
        how : string / cython mapped function
        **kwargs : kw args passed to how function
        """
        ax = self.ax

        # Excludes `on` column when provided
        obj = self._obj_with_exclusions

        if not len(ax):
            # reset to the new freq
            obj = obj.copy()
            obj.index = obj.index._with_freq(self.freq)
            assert obj.index.freq == self.freq, (obj.index.freq, self.freq)
            return obj

        # we are downsampling
        # we want to call the actual grouper method here
        result = obj.groupby(self._grouper).aggregate(how, **kwargs)
        return self._wrap_result(result)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.apply_func [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
        def apply_func(values, begin, end, min_periods, raw=raw):
            if not raw:
                # GH 45912
                values = Series(values, index=self._on, copy=False)
            return window_func(values, begin, end, min_periods)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_resample [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py]
def maybe_resample(series: Series, ax: Axes, kwargs: dict[str, Any]):
    # resample against axes freq if necessary

    if "how" in kwargs:
        raise ValueError(
            "'how' is not a valid keyword for plotting functions. If plotting "
            "multiple objects on shared axes, resample manually first."
        )

    freq, ax_freq = _get_freq(ax, series)

    if freq is None:  # pragma: no cover
        raise ValueError("Cannot use dynamic axis without frequency info")

    # Convert DatetimeIndex to PeriodIndex so the x-axis uses Period ordinals.
    # For BDay freq this ensures consecutive business days get consecutive
    # ordinals with no weekend gaps (GH#1482).
    if isinstance(series.index, ABCDatetimeIndex):
        series = series.to_period(freq=freq)

    if ax_freq is not None and freq != ax_freq:
        if is_superperiod(freq, ax_freq):  # upsample input
            series = series.copy(deep=False)
            # error: "Index" has no attribute "asfreq"
            series.index = series.index.asfreq(  # type: ignore[attr-defined]
                ax_freq, how="s"
            )
            freq = ax_freq
        elif _is_sup(freq, ax_freq):  # one is weekly
            how = "last"
            series = getattr(series.resample("D"), how)().dropna()
            series = getattr(series.resample(ax_freq), how)().dropna()
            freq = ax_freq
        elif is_subperiod(freq, ax_freq) or _is_sub(freq, ax_freq):
            _upsample_others(ax, freq, kwargs)
        else:  # pragma: no cover
            raise ValueError("Incompatible frequency conversion")
    return freq, series

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._validate_left_right_on [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _validate_left_right_on(self, left_on, right_on):
        left_on, right_on = super()._validate_left_right_on(left_on, right_on)

        # we only allow on to be a single item for on
        if len(left_on) != 1 and not self.left_index:
            raise MergeError("can only asof on a key for left")

        if len(right_on) != 1 and not self.right_index:
            raise MergeError("can only asof on a key for right")

        if self.left_index and isinstance(self.left.index, MultiIndex):
            raise MergeError("left can only have one index")

        if self.right_index and isinstance(self.right.index, MultiIndex):
            raise MergeError("right can only have one index")

        # set 'by' columns
        if self.by is not None:
            if self.left_by is not None or self.right_by is not None:
                raise MergeError("Can only pass by OR left_by and right_by")
            self.left_by = self.right_by = self.by
        if self.left_by is None and self.right_by is not None:
            raise MergeError("missing left_by")
        if self.left_by is not None and self.right_by is None:
            raise MergeError("missing right_by")

        # GH#29130 Check that merge keys do not have dtype object
        if not self.left_index:
            left_on_0 = left_on[0]  # pyright: ignore[reportOptionalSubscript]
            if isinstance(left_on_0, _known):
                lo_dtype = left_on_0.dtype
            else:
                lo_dtype = (
                    self.left._get_label_or_level_values(left_on_0).dtype
                    if left_on_0 in self.left.columns
                    else self.left.index.get_level_values(left_on_0)
                )
        else:
            lo_dtype = self.left.index.dtype

        if not self.right_index:
            right_on_0 = right_on[0]  # pyright: ignore[reportOptionalSubscript]
            if isinstance(right_on_0, _known):
                ro_dtype = right_on_0.dtype
            else:
                ro_dtype = (
                    self.right._get_label_or_level_values(right_on_0).dtype
                    if right_on_0 in self.right.columns
                    else self.right.index.get_level_values(right_on_0)
                )
        else:
            ro_dtype = self.right.index.dtype

        if (
            is_object_dtype(lo_dtype)
            or is_object_dtype(ro_dtype)
            or is_string_dtype(lo_dtype)
            or is_string_dtype(ro_dtype)
        ):
            raise MergeError(
                f"Incompatible merge dtype, {lo_dtype!r} and "
                f"{ro_dtype!r}, both sides must have numeric dtype"
            )

        # add 'by' to our key-list so we can have it in the
        # output as a key
        if self.left_by is not None:
            if not is_list_like(self.left_by):
                self.left_by = [self.left_by]
            if not is_list_like(self.right_by):
                self.right_by = [self.right_by]

            if len(self.left_by) != len(self.right_by):
                raise MergeError("left_by and right_by must be the same length")

            left_on = self.left_by + list(left_on)
            right_on = self.right_by + list(right_on)  # pyright: ignore[reportOptionalOperand]

        return left_on, right_on

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_cross_merge [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
def _cross_merge(
    left: DataFrame,
    right: DataFrame,
    on: IndexLabel | AnyArrayLike | None = None,
    left_on: IndexLabel | AnyArrayLike | None = None,
    right_on: IndexLabel | AnyArrayLike | None = None,
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = False,
    suffixes: Suffixes = ("_x", "_y"),
    indicator: str | bool = False,
    validate: str | None = None,
) -> DataFrame:
    """
    See merge.__doc__ with how='cross'
    """

    if (
        left_index
        or right_index
        or right_on is not None
        or left_on is not None
        or on is not None
    ):
        raise MergeError(
            "Can not pass on, right_on, left_on or set right_index=True or "
            "left_index=True"
        )

    return _CrossMergeOperation(
        left,
        right,
        suffixes=suffixes,
        indicator=indicator,
    ).get_result()
```
