# pandas-23 :: minilm

query: BUG: DatetimeIndex.intersection losing freq and tz (#33604)

## selected nodes

- rank=1 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::datetime_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=2 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=3 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::ResetIndex.time_reset_datetimeindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=4 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=5 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py::TimedeltaIndexing.time_intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py
- rank=6 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._is_all_dates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=7 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::SeriesDtypesConstructors.time_dtindex_from_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py
- rank=8 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_asfreq_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=9 layer=FUNCTION tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeIndex.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=10 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::Indexing.time_intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=11 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=12 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=13 layer=FUNCTION tokens=252 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/datetimes.py::_box_as_indexlike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/datetimes.py
- rank=14 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::SeriesDtypesConstructors.time_dtindex_from_index_with_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py
- rank=15 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/eval.py::Query.time_query_datetime_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/eval.py
- rank=16 layer=FUNCTION tokens=547 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._maybe_downcast_for_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=17 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=18 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=19 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._tz_localize file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=20 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestDatetimeIndexEquals.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
- rank=21 layer=FUNCTION tokens=243 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._dti_setop_align_tzs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=22 layer=FUNCTION tokens=409 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed._get_index_factory file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=23 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype.index_class file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=24 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeIndex.time_to_date file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_mismatched_tz(self):
        # reached via e.g.
        #  ser = Series(range(len(dti)), index=dti)
        #  ser[dti2]
        self.dti.get_indexer(self.dti2)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::ResetIndex.time_reset_datetimeindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_reset_datetimeindex(self, tz):
        self.df.reset_index()

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py::TimedeltaIndexing.time_intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py]
    def time_intersection(self):
        self.index.intersection(self.index2)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._is_all_dates [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _is_all_dates(self) -> bool:
        """
        Whether or not the index values only consist of dates.
        """
        if needs_i8_conversion(self.dtype):
            return True
        elif self.dtype != _dtype_obj:
            # TODO(ExtensionIndex): 3rd party EA might override?
            # Note: this includes IntervalIndex, even when the left/right
            #  contain datetime-like objects.
            return False
        elif self._is_multi:
            return False
        return is_datetime_array(ensure_object(self._values))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::SeriesDtypesConstructors.time_dtindex_from_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py]
    def time_dtindex_from_series(self):
        DatetimeIndex(self.s)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeIndex.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::Indexing.time_intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_intersection(self):
        self.index[:750].intersection(self.index[250:])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_intersection(self):
        self.index[:750].intersection(self.index[250:])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::DatetimeArray.tz [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py]
    def tz(self, value):
        # GH 3746: Prevent localizing or converting the index by setting tz
        raise AttributeError(
            "Cannot directly set timezone. Use tz_localize() "
            "or tz_convert() as appropriate"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/datetimes.py::_box_as_indexlike [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/datetimes.py]
def _box_as_indexlike(
    dt_array: ArrayLike, utc: bool = False, name: Hashable | None = None
) -> Index:
    """
    Properly boxes the ndarray of datetimes to DatetimeIndex
    if it is possible or to generic Index instead

    Parameters
    ----------
    dt_array: 1-d array
        Array of datetimes to be wrapped in an Index.
    utc : bool
        Whether to convert/localize timestamps to UTC.
    name : string, default None
        Name for a resulting index

    Returns
    -------
    result : datetime of converted dates
        - DatetimeIndex if convertible to sole datetime64 type
        - general Index otherwise
    """

    if lib.is_np_dtype(dt_array.dtype, "M"):
        tz = "utc" if utc else None
        return DatetimeIndex(dt_array, tz=tz, name=name)
    return Index(dt_array, name=name, dtype=dt_array.dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::SeriesDtypesConstructors.time_dtindex_from_index_with_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py]
    def time_dtindex_from_index_with_series(self):
        Index(self.s)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/eval.py::Query.time_query_datetime_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/eval.py]
    def time_query_datetime_index(self):
        self.df.query("index < @self.ts")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._maybe_downcast_for_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _maybe_downcast_for_indexing(self, other: Index) -> tuple[Index, Index]:
        """
        When dealing with an object-dtype Index and a non-object Index, see
        if we can upcast the object-dtype one to improve performance.
        """

        if isinstance(self, ABCDatetimeIndex) and isinstance(other, ABCDatetimeIndex):
            if (
                self.tz is not None
                and other.tz is not None
                and not tz_compare(self.tz, other.tz)
            ):
                # standardize on UTC
                return self.tz_convert("UTC"), other.tz_convert("UTC")

        elif self.inferred_type == "date" and isinstance(other, ABCDatetimeIndex):
            try:
                return type(other)(self), other
            except OutOfBoundsDatetime:
                return self, other
        elif self.inferred_type == "timedelta" and isinstance(other, ABCTimedeltaIndex):
            # TODO: we dont have tests that get here
            return type(other)(self), other

        elif self.dtype.kind == "u" and other.dtype.kind == "i":
            # GH#41873
            if other.min() >= 0:  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
                # lookup min as it may be cached
                # TODO: may need itemsize check if we have non-64-bit Indexes
                return self, other.astype(self.dtype)

        elif self._is_multi and not other._is_multi:
            try:
                # "Type[Index]" has no attribute "from_tuples"
                other = type(self).from_tuples(other)  # type: ignore[attr-defined]
            except (TypeError, ValueError):
                # let's instead try with a straight Index
                self = Index(self._values, copy=False)

        if not is_object_dtype(self.dtype) and is_object_dtype(other.dtype):
            # Reverse op so we dont need to re-implement on the subclasses
            other, self = other._maybe_downcast_for_indexing(self)

        return self, other

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def _create_mi_with_dt64tz_level():
    """
    MultiIndex with a level that is a tzaware DatetimeIndex.
    """
    # GH#8367 round trip with pickle
    return MultiIndex.from_product(
        [[1, 2], ["a", "b"], date_range("20130101", periods=3, tz="US/Eastern")],
        names=["one", "two", "three"],
    )

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestDatetimeIndexEquals.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py]
    def index(self):
        """Fixture for creating a DatetimeIndex for use in equality tests."""
        return date_range("2013-01-01", periods=5)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._dti_setop_align_tzs [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _dti_setop_align_tzs(self, other: Index, setop: str_t) -> tuple[Index, Index]:
        """
        With mismatched timezones, cast both to UTC.
        """
        # Caller is responsible for checking
        #  `self.dtype != other.dtype`
        if (
            isinstance(self, ABCDatetimeIndex)
            and isinstance(other, ABCDatetimeIndex)
            and self.tz is not None
            and other.tz is not None
        ):
            # GH#39328, GH#45357, GH#60080
            # If both timezones are the same, no need to convert to UTC
            if self.tz == other.tz:
                return self, other
            else:
                left = self.tz_convert("UTC")
                right = other.tz_convert("UTC")
                return left, right
        return self, other

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype.index_class [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def index_class(self) -> type_t[DatetimeIndex]:
        from pandas import DatetimeIndex

        return DatetimeIndex

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeIndex.time_to_date [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_to_date(self, index_type):
        self.index.date
```
