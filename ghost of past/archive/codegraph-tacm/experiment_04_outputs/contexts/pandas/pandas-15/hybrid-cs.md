# pandas-15 :: hybrid-cs

query: BUG: pickle after _with_freq (#33811)

## selected nodes

- rank=1 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=2 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=3 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=4 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=5 layer=FUNCTION tokens=270 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=6 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=7 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py
- rank=8 layer=FUNCTION tokens=768 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_pin_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=9 layer=FUNCTION tokens=326 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=10 layer=FUNCTION tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::_validate_inferred_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=11 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodConstructor.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py
- rank=12 layer=FUNCTION tokens=677 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray._from_sequence_not_strict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=13 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py
- rank=14 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::InferFreq.time_infer_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=15 layer=FUNCTION tokens=361 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=16 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=17 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=18 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_clear_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=19 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._get_insert_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=20 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=21 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::get_random_path file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _with_freq(self, freq):
        arr = self._data._with_freq(freq)
        return type(self)._simple_new(arr, name=self._name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def peakmem_read_pickle(self):
        read_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def time_read_pickle(self):
        read_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def peakmem_write_pickle(self):
        self.df.to_pickle(self.fname)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_write_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def time_write_pickle(self):
        self.df.to_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py]
def pickle_respnder(df):
    with BytesIO() as bio:
        df.to_pickle(bio)
        return bio.getvalue()

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.__new__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def __new__(cls, freq) -> PeriodDtype:  # noqa: PYI034
        """
        Parameters
        ----------
        freq : PeriodDtype, BaseOffset, or string
        """
        if isinstance(freq, PeriodDtype):
            return freq

        elif isinstance(freq, PeriodDtypeBase):
            freq = to_offset(freq, is_period=True)

        if not isinstance(freq, BaseOffset):
            freq = cls._parse_dtype_strict(freq)

        if isinstance(freq, BDay):
            # GH#53446
            # TODO(3.0): enforcing this will close GH#10575
            warnings.warn(
                "PeriodDtype[B] is deprecated and will be removed in a future "
                "version. Use a DatetimeIndex with freq='B' instead",
                FutureWarning,  # pdlint: ignore[warning_class]
                stacklevel=find_stack_level(),
            )

        try:
            dtype_code = cls._cache_dtypes[freq]
        except KeyError:
            dtype_code = freq._period_dtype_code
            cls._cache_dtypes[freq] = dtype_code
        u = PeriodDtypeBase.__new__(cls, dtype_code, freq.n)
        u._freq = freq
        return u

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py::PeriodConstructor.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/period.py]
    def setup(self, freq, is_offset):
        if is_offset:
            self.freq = to_offset(freq)
        else:
            self.freq = freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray._from_sequence_not_strict [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py]
    def _from_sequence_not_strict(
        cls,
        data,
        *,
        dtype=None,
        copy: bool = False,
        tz=lib.no_default,
        freq: str | BaseOffset | lib.NoDefault | None = lib.no_default,
        dayfirst: bool = False,
        yearfirst: bool = False,
        ambiguous: TimeAmbiguous = "raise",
    ) -> Self:
        """
        A non-strict version of _from_sequence, called from DatetimeIndex.__new__.
        """

        # if the user either explicitly passes tz=None or a tz-naive dtype, we
        #  disallow inferring a tz.
        explicit_tz_none = tz is None
        if tz is lib.no_default:
            tz = None
        else:
            tz = timezones.maybe_get_tz(tz)

        dtype = _validate_dt64_dtype(dtype)
        # if dtype has an embedded tz, capture it
        tz = _validate_tz_from_dtype(dtype, tz, explicit_tz_none)

        unit = None
        if dtype is not None:
            unit = dtl.dtype_to_unit(dtype)

        data, copy = dtl.ensure_arraylike_for_datetimelike(
            data, copy, cls_name="DatetimeArray"
        )
        inferred_freq = None
        if isinstance(data, DatetimeArray):
            inferred_freq = data.freq

        subarr, tz = _sequence_to_dt64(
            data,
            copy=copy,
            tz=tz,
            dayfirst=dayfirst,
            yearfirst=yearfirst,
            ambiguous=ambiguous,
            out_unit=unit,
        )
        # We have to call this again after possibly inferring a tz above
        _validate_tz_from_dtype(dtype, tz, explicit_tz_none)
        if tz is not None and explicit_tz_none:
            raise ValueError(
                "Passed data is timezone-aware, incompatible with 'tz=None'. "
                "Use obj.tz_localize(None) instead."
            )

        data_unit = np.datetime_data(subarr.dtype)[0]
        data_unit = cast("TimeUnit", data_unit)
        data_dtype = tz_to_dtype(tz, data_unit)
        result = cls._simple_new(subarr, freq=inferred_freq, dtype=data_dtype)
        if unit is not None and unit != result.unit:
            # If unit was specified in user-passed dtype, cast to it here
            # error: Argument 1 to "as_unit" of "TimelikeOps" has
            # incompatible type "str"; expected "Literal['s', 'ms', 'us', 'ns']"
            # [arg-type]
            result = result.as_unit(unit)  # type: ignore[arg-type]

        validate_kwds = {"ambiguous": ambiguous}
        result._maybe_pin_freq(freq, validate_kwds)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py]
    def freq(self):
        return self._freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::InferFreq.time_infer_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_infer_freq(self, freq):
        infer_freq(self.idx)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py]
def _get_index_freq(index: Index) -> BaseOffset | None:
    freq = getattr(index, "freq", None)
    if freq is None:
        freq = getattr(index, "inferred_freq", None)
        freq = to_offset(freq)
    return freq

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_clear_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _maybe_clear_freq(self) -> None:
        self._freq = None

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def freq(self, value) -> None:
        # error: Property "freq" defined in "PeriodArray" is read-only  [misc]
        self._data.freq = value  # type: ignore[misc]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::get_random_path [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py]
def get_random_path():
    return f"__{uuid.uuid4()}__.pickle"
```
