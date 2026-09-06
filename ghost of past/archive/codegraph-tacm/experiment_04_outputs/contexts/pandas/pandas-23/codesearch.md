# pandas-23 :: codesearch

query: BUG: DatetimeIndex.intersection losing freq and tz (#33604)

## selected nodes

- rank=1 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::apply_tzinfo_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c
- rank=2 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::datetime_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=3 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::TzLocalize.time_infer_dst file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=4 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::Indexing.time_intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=5 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=6 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::Arithmetic.time_intersect file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py
- rank=7 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::ResetIndex.time_reset_datetimeindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=8 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py::TimedeltaIndexing.time_intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py
- rank=9 layer=FUNCTION tokens=493 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_convert_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=10 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=11 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeAccessor.time_dt_accessor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=12 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsinWithArange.time_isin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py
- rank=13 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_pydatetime file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=14 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_asfreq_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=15 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Cut.time_cut_interval file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=16 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::ArithmeticBlock.time_intersect file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py
- rank=17 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=18 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strftime.py::PeriodStrftime.time_frame_period_formatting_iso8601_strftime_Z file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strftime.py
- rank=19 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeAccessor.time_dt_accessor_time file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=20 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Reindex.time_reindex_axis0 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=21 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::IndexArithmetic.time_subtract file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=22 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Align.time_series_align_int64_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=23 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Timeseries.time_timestamp_ops_diff file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=24 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::InferFreq.time_infer_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=25 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::GetItem.time_integer_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py
- rank=26 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py::TimeTZConvert.time_tz_convert_from_utc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py
- rank=27 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Reindex.time_reindex_axis1_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=28 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/eval.py::Query.time_query_datetime_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/eval.py
- rank=29 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_date_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=30 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::period_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=31 layer=FUNCTION tokens=359 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::PyDateTimeToIso file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c
- rank=32 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Timeseries.time_timestamp_ops_diff_with_shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=33 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeAccessor.time_dt_accessor_date file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=34 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Concat.time_concat_non_overlapping_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=35 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/datetimes/test_reductions.py::TestReductions.arr1d file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/datetimes/test_reductions.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::apply_tzinfo_offset [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c]
static int apply_tzinfo_offset(PyObject *obj, npy_datetimestruct *out) {
  PyObject *offset = extract_utc_offset(obj);
  /* Apply the time zone offset if datetime obj is tz-aware */
  if (offset != NULL) {
    if (offset == Py_None) {
      Py_DECREF(offset);
      return 0;
    }
    /*
     * The timedelta should have a function "total_seconds"
     * which contains the value we want.
     */
    PyObject *tmp = PyObject_CallMethod(offset, "total_seconds", NULL);
    Py_DECREF(offset);
    if (tmp == NULL) {
      return -1;
    }
    PyObject *tmp_int = PyNumber_Long(tmp);
    if (tmp_int == NULL) {
      Py_DECREF(tmp);
      return -1;
    }
    int seconds_offset = PyLong_AsLong(tmp_int);
    if (seconds_offset == -1 && PyErr_Occurred()) {
      Py_DECREF(tmp_int);
      Py_DECREF(tmp);
      return -1;
    }
    Py_DECREF(tmp_int);
    Py_DECREF(tmp);

    /* Convert to a minutes offset and apply it */
    add_minutes_to_datetimestruct(out, -(seconds_offset / 60));
  }

  return 0;
}

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::TzLocalize.time_infer_dst [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_infer_dst(self, tz):
        self.index.tz_localize(tz, ambiguous="infer")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::Indexing.time_intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_intersection(self):
        self.index[:750].intersection(self.index[250:])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_intersection(self):
        self.index[:750].intersection(self.index[250:])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::Arithmetic.time_intersect [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py]
    def time_intersect(self, dense_proportion, fill_value):
        self.array1.sp_index.intersect(self.array2.sp_index)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::ResetIndex.time_reset_datetimeindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_reset_datetimeindex(self, tz):
        self.df.reset_index()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py::TimedeltaIndexing.time_intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py]
    def time_intersection(self):
        self.index.intersection(self.index2)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_mismatched_tz(self):
        # reached via e.g.
        #  ser = Series(range(len(dti)), index=dti)
        #  ser[dti2]
        self.dti.get_indexer(self.dti2)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeAccessor.time_dt_accessor [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_dt_accessor(self, tz):
        self.series.dt

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsinWithArange.time_isin [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py]
    def time_isin(self, dtype, M, offset_factor):
        self.series.isin(self.values)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_pydatetime [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_pydatetime(self, freq, is_offset):
        PeriodIndex(self.rng2, freq=freq)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Cut.time_cut_interval [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py]
    def time_cut_interval(self, bins):
        # GH 27668
        pd.cut(self.int_series, self.interval_bins)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::ArithmeticBlock.time_intersect [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py]
    def time_intersect(self, fill_value):
        self.arr2.sp_index.intersect(self.arr2.sp_index)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_ints [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_ints(self, freq, is_offset):
        PeriodIndex(self.ints, freq=freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strftime.py::PeriodStrftime.time_frame_period_formatting_iso8601_strftime_Z [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strftime.py]
    def time_frame_period_formatting_iso8601_strftime_Z(self, nobs, freq):
        self.data["p"].dt.strftime(date_format="%Y-%m-%dT%H:%M:%SZ")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeAccessor.time_dt_accessor_time [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_dt_accessor_time(self, tz):
        self.series.dt.time

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Reindex.time_reindex_axis0 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_reindex_axis0(self):
        self.df.reindex(self.idx)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::IndexArithmetic.time_subtract [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_subtract(self, dtype):
        self.index - 2

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Align.time_series_align_int64_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_series_align_int64_index(self):
        self.ts1 + self.ts2

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Timeseries.time_timestamp_ops_diff [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_timestamp_ops_diff(self, tz):
        self.s2.diff()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::InferFreq.time_infer_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_infer_freq(self, freq):
        infer_freq(self.idx)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::GetItem.time_integer_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py]
    def time_integer_indexing(self):
        self.sp_arr[78]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py::TimeTZConvert.time_tz_convert_from_utc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/tz_convert.py]
    def time_tz_convert_from_utc(self, size, tz):
        # effectively:
        #  dti = DatetimeIndex(self.i8data, tz=tz)
        #  dti.tz_localize(None)
        if old_sig:
            tz_convert_from_utc(self.i8data, timezone.utc, tz)
        else:
            tz_convert_from_utc(self.i8data, tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Reindex.time_reindex_axis1_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_reindex_axis1_missing(self):
        self.df.reindex(columns=self.idx)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/eval.py::Query.time_query_datetime_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/eval.py]
    def time_query_datetime_index(self):
        self.df.query("index < @self.ts")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::PeriodIndexConstructor.time_from_date_range [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py]
    def time_from_date_range(self, freq, is_offset):
        PeriodIndex(self.rng, freq=freq)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c::PyDateTimeToIso [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/pd_datetime.c]
static char *PyDateTimeToIso(PyObject *obj, NPY_DATETIMEUNIT base,
                             size_t *len) {
  npy_datetimestruct dts;
  int ret;

  ret = convert_pydatetime_to_datetimestruct(obj, &dts);
  if (ret != 0) {
    if (!PyErr_Occurred()) {
      PyErr_SetString(PyExc_ValueError,
                      "Could not convert PyDateTime to numpy datetime");
    }
    return NULL;
  }

  *len = (size_t)get_datetime_iso_8601_strlen(0, base);
  char *result = PyObject_Malloc(*len);
  // Check to see if PyDateTime has a timezone.
  // Don't convert to UTC if it doesn't.
  int is_tz_aware = 0;
  if (PyObject_HasAttrString(obj, "tzinfo")) {
    PyObject *offset = extract_utc_offset(obj);
    if (offset == NULL) {
      PyObject_Free(result);
      return NULL;
    }
    is_tz_aware = offset != Py_None;
    Py_DECREF(offset);
  }
  ret = make_iso_8601_datetime(&dts, result, *len, is_tz_aware, base);

  if (ret != 0) {
    PyErr_SetString(PyExc_ValueError,
                    "Could not convert datetime value to string");
    PyObject_Free(result);
    return NULL;
  }

  // Note that get_datetime_iso_8601_strlen just gives a generic size
  // for ISO string conversion, not the actual size used
  *len = strlen(result);
  return result;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Timeseries.time_timestamp_ops_diff_with_shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_timestamp_ops_diff_with_shift(self, tz):
        self.s - self.s.shift()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeAccessor.time_dt_accessor_date [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_dt_accessor_date(self, tz):
        self.series.dt.date

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Concat.time_concat_non_overlapping_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_concat_non_overlapping_index(self):
        pd.concat([self.df_a, self.df_b])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/datetimes/test_reductions.py::TestReductions.arr1d [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/datetimes/test_reductions.py]
    def arr1d(self, tz_naive_fixture):
        """Fixture returning DatetimeArray with parametrized timezones"""
        tz = tz_naive_fixture
        dtype = DatetimeTZDtype(tz=tz) if tz is not None else np.dtype("M8[ns]")
        arr = DatetimeArray._from_sequence(
            [
                "2000-01-03",
                "2000-01-03",
                "NaT",
                "2000-01-02",
                "2000-01-05",
                "2000-01-04",
            ],
            dtype=dtype,
        )
        return arr
```
