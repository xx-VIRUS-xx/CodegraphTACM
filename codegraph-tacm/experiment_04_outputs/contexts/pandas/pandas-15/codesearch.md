# pandas-15 :: codesearch

query: BUG: pickle after _with_freq (#33811)

## selected nodes

- rank=1 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py
- rank=2 layer=FUNCTION tokens=1162 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.asfreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=3 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=4 layer=FUNCTION tokens=768 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_pin_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=5 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::InferFreq.time_infer_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=6 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_clear_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=7 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodConstructor.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=8 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py::TimedeltaProperties.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py
- rank=9 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=10 layer=FUNCTION tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::_validate_inferred_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=11 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py::_f1 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py
- rank=12 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._maybe_clear_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=13 layer=FUNCTION tokens=270 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=14 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=15 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge_ordered.py::right file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge_ordered.py
- rank=16 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=17 layer=FUNCTION tokens=357 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::asfreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=18 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=19 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=20 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodUnaryMethods.time_asfreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=21 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodUnaryMethods.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=22 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::ReadPickleBuffer.readline file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py]
    def freq(self):
        return self._freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.asfreq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def asfreq(
        self,
        freq: Frequency,
        method: FillnaOptions | None = None,
        how: Literal["start", "end"] | None = None,
        normalize: bool = False,
        fill_value: Hashable | None = None,
    ) -> Self:
        """
        Convert time series to specified frequency.

        Returns the original data conformed to a new index with the specified
        frequency.

        If the index of this Series/DataFrame is a :class:`~pandas.PeriodIndex`, the
        new index is the result of transforming the original index with
        :meth:`PeriodIndex.asfreq <pandas.PeriodIndex.asfreq>` (so the original index
        will map one-to-one to the new index).

        Otherwise, the new index will be equivalent to ``pd.date_range(start, end,
        freq=freq)`` where ``start`` and ``end`` are, respectively, the min and
        max entries in the original index (see :func:`pandas.date_range`). The
        values corresponding to any timesteps in the new index which were not present
        in the original index will be null (``NaN``), unless a method for filling
        such unknowns is provided (see the ``method`` parameter below).

        The :meth:`resample` method is more appropriate if an operation on each group of
        timesteps (such as an aggregate) is necessary to represent the data at the new
        frequency.

        Parameters
        ----------
        freq : DateOffset or str
            Frequency DateOffset or string.
        method : {'backfill'/'bfill', 'pad'/'ffill'}, default None
            Method to use for filling holes in reindexed Series (note this
            does not fill NaNs that already were present):

            * 'pad' / 'ffill': propagate last valid observation forward to next
              valid based on the order of the index
            * 'backfill' / 'bfill': use NEXT valid observation to fill.
        how : {'start', 'end'}, default end
            For PeriodIndex only (see PeriodIndex.asfreq).
        normalize : bool, default False
            Whether to reset output index to midnight.
        fill_value : scalar, optional
            Value to use for missing values, applied during upsampling (note
            this does not fill NaNs that already were present).

        Returns
        -------
        Series/DataFrame
            Series/DataFrame object reindexed to the specified frequency.

        See Also
        --------
        reindex : Conform DataFrame to new index with optional filling logic.

        Notes
        -----
        To learn more about the frequency strings, please see
        :ref:`this link<timeseries.offset_aliases>`.

        Examples
        --------
        Start by creating a series with 4 one minute timestamps.

        >>> index = pd.date_range("1/1/2000", periods=4, freq="min")
        >>> series = pd.Series([0.0, None, 2.0, 3.0], index=index)
        >>> df = pd.DataFrame({"s": series})
        >>> df
                               s
        2000-01-01 00:00:00    0.0
        2000-01-01 00:01:00    NaN
        2000-01-01 00:02:00    2.0
        2000-01-01 00:03:00    3.0

        Upsample the series into 30 second bins.

        >>> df.asfreq(freq="30s")
                               s
        2000-01-01 00:00:00    0.0
        2000-01-01 00:00:30    NaN
        2000-01-01 00:01:00    NaN
        2000-01-01 00:01:30    NaN
        2000-01-01 00:02:00    2.0
        2000-01-01 00:02:30    NaN
        2000-01-01 00:03:00    3.0

        Upsample again, providing a ``fill value``.

        >>> df.asfreq(freq="30s", fill_value=9.0)
                               s
        2000-01-01 00:00:00    0.0
        2000-01-01 00:00:30    9.0
        2000-01-01 00:01:00    NaN
        2000-01-01 00:01:30    9.0
        2000-01-01 00:02:00    2.0
        2000-01-01 00:02:30    9.0
        2000-01-01 00:03:00    3.0

        Upsample again, providing a ``method``.

        >>> df.asfreq(freq="30s", method="bfill")
                               s
        2000-01-01 00:00:00    0.0
        2000-01-01 00:00:30    NaN
        2000-01-01 00:01:00    NaN
        2000-01-01 00:01:30    2.0
        2000-01-01 00:02:00    2.0
        2000-01-01 00:02:30    3.0
        2000-01-01 00:03:00    3.0
        """
        from pandas.core.resample import asfreq

        return asfreq(
            self,
            freq,
            method=method,
            how=how,
            normalize=normalize,
            fill_value=fill_value,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _with_freq(self, freq):
        arr = self._data._with_freq(freq)
        return type(self)._simple_new(arr, name=self._name)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::InferFreq.time_infer_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_infer_freq(self, freq):
        infer_freq(self.idx)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_clear_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _maybe_clear_freq(self) -> None:
        self._freq = None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodConstructor.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def setup(self, freq, is_offset):
        if is_offset:
            self.freq = to_offset(freq)
        else:
            self.freq = freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py::TimedeltaProperties.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py]
    def freq(self):
        return self._get_values().inferred_freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def freq(self, value) -> None:
        # error: Property "freq" defined in "PeriodArray" is read-only  [misc]
        self._data.freq = value  # type: ignore[misc]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::_validate_inferred_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
def _validate_inferred_freq(
    freq: BaseOffset | None, inferred_freq: BaseOffset | None
) -> BaseOffset | None:
    """
    If the user passes a freq and another freq is inferred from passed data,
    require that they match.

    Parameters
    ----------
    freq : DateOffset or None
    inferred_freq : DateOffset or None

    Returns
    -------
    freq : DateOffset or None
    """
    if inferred_freq is not None:
        if freq is not None and freq != inferred_freq:
            raise ValueError(
                f"Inferred frequency {inferred_freq} from passed "
                "values does not conform to passed frequency "
                f"{freq.freqstr}"
            )
        if freq is None:
            freq = inferred_freq

    return freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py::_f1 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py]
def _f1(new=False):
    return new

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._maybe_clear_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _maybe_clear_freq(self) -> None:
        # inplace operations like __setitem__ may invalidate the freq of
        # DatetimeArray and TimedeltaArray
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._with_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _with_freq(self, freq) -> Self:
        """
        Helper to get a view on the same data, with a new freq.

        Parameters
        ----------
        freq : DateOffset, None, or "infer"

        Returns
        -------
        Same type as self
        """
        # GH#29843
        if freq is None:
            # Always valid
            pass
        elif len(self) == 0 and isinstance(freq, BaseOffset):
            # Always valid.  In the TimedeltaArray case, we require a Tick offset
            if self.dtype.kind == "m" and not isinstance(freq, (Tick, Day)):
                raise TypeError("TimedeltaArray/Index freq must be a Tick")
        else:
            # As an internal method, we can ensure this assertion always holds
            assert freq == "infer"
            freq = to_offset(self.inferred_freq)

        arr = self.view()
        arr._freq = freq
        return arr

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py]
def _get_index_freq(index: Index) -> BaseOffset | None:
    freq = getattr(index, "freq", None)
    if freq is None:
        freq = getattr(index, "inferred_freq", None)
        freq = to_offset(freq)
    return freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge_ordered.py::right [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge_ordered.py]
def right():
    return DataFrame({"key": ["b", "c", "d", "f"], "rvalue": [1, 2, 3.0, 4]})

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def peakmem_read_pickle(self):
        read_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::asfreq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
def asfreq(
    obj: NDFrameT,
    freq,
    method=None,
    how=None,
    normalize: bool = False,
    fill_value=None,
) -> NDFrameT:
    """
    Utility frequency conversion method for Series/DataFrame.

    See :meth:`pandas.NDFrame.asfreq` for full documentation.
    """
    if isinstance(obj.index, PeriodIndex):
        if method is not None:
            raise NotImplementedError("'method' argument is not supported")

        if how is None:
            how = "E"

        if isinstance(freq, BaseOffset):
            if hasattr(freq, "_period_dtype_code"):
                freq = PeriodDtype(freq)._freqstr

        new_obj = obj.copy()
        new_obj.index = obj.index.asfreq(freq, how=how)

    elif len(obj.index) == 0:
        new_obj = obj.copy()

        new_obj.index = _asfreq_compat(obj.index, freq)
    else:
        unit: TimeUnit = "ns"
        if isinstance(obj.index, DatetimeIndex):
            # TODO: should we disallow non-DatetimeIndex?
            unit = obj.index.unit
        dti = date_range(obj.index.min(), obj.index.max(), freq=freq, unit=unit)
        dti.name = obj.index.name
        new_obj = obj.reindex(dti, method=method, fill_value=fill_value)
        if normalize:
            new_obj.index = new_obj.index.normalize()

    return new_obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def time_read_pickle(self):
        read_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def peakmem_write_pickle(self):
        self.df.to_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodUnaryMethods.time_asfreq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def time_asfreq(self, freq):
        self.per.asfreq("Y")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodUnaryMethods.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def setup(self, freq):
        self.per = Period("2012-06-01", freq=freq)
        if freq == "M":
            self.default_fmt = "%Y-%m"
        elif freq == "min":
            self.default_fmt = "%Y-%m-%d %H:%M"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::ReadPickleBuffer.readline [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py]
    def readline(self) -> bytes: ...
```
