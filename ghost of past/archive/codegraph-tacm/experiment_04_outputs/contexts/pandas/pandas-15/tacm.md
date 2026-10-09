# pandas-15 :: tacm

query: BUG: pickle after _with_freq (#33811)

## selected nodes

- rank=1 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=2 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=3 layer=FILE tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=4 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=5 layer=FILE tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py
- rank=6 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_pickle.py
- rank=7 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_pickle.py
- rank=8 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=9 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::Unpickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=10 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=11 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_pickle.py
- rank=12 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=13 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=14 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=15 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=16 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=17 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::patch_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=18 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=19 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::to_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=20 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::write_legacy_pickles file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=21 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py
- rank=22 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=23 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.to_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=24 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=25 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=26 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_unpickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=27 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_pickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=28 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::loads file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=29 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py::round_trip_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py
- rank=30 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=31 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::infer_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py
- rank=32 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=33 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=34 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PandasExtensionDtype.__getstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=35 layer=FUNCTION tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._parse_with_reso file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=36 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=37 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::create_pickle_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=38 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/holiday.py::after_nearest_workday file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/holiday.py
- rank=39 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::get_random_path file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=40 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.to_timestamp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=41 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=42 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_to_timestamp.py::_get_with_delta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_to_timestamp.py
- rank=43 layer=FUNCTION tokens=334 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::_new_DatetimeIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=44 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::_simple_period_range_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py
- rank=45 layer=FUNCTION tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::DatetimeIndexResampler._downsample file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=46 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype.__setstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=47 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py::TestCustomBusinessDay._check_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
- rank=48 layer=FUNCTION tokens=9 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py::DummyArray.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py

## context

```text
file pandas/io/pickle.py
imports: __future__, pickle, typing, warnings, pandas
defines: to_pickle, read_pickle

file pandas/compat/pickle_compat.py
imports: __future__, contextlib, io, pickle, typing, numpy, pandas, collections
defines: Unpickler, loads, patch_pickle

file benchmarks/io/pickle.py
imports: numpy, pandas, pandas_vb_common
defines: Pickle

file pandas/core/generic.py
imports: __future__, collections, copy, datetime, functools, json, operator, pickle
defines: NDFrame

file pandas/tseries/frequencies.py
imports: __future__, typing, numpy, pandas
defines: _FrequencyInferer, _TimedeltaFrequencyInferer, get_period_alias, infer_freq, _is_multiple, _maybe_add_count, is_subperiod, is_superperiod, _maybe_coerce_freq, _quarter_months_conform, _is_annual, _is_quarterly, _is_monthly, _is_weekly

class TestPickle:  [indexes/datetimes/test_pickle.py:11]
methods: test_pickle, test_pickle_after_set_freq
         test_pickle_dont_infer_freq, test_pickle_unpickle
         test_roundtrip_pickle_with_tz

class TestPickle:  [indexes/timedeltas/test_pickle.py:5]
methods: test_pickle_after_set_freq

class Pickle(BaseIO):  [benchmarks/io/pickle.py:13]
methods: peakmem_read_pickle, peakmem_write_pickle, setup
         time_read_pickle, time_write_pickle

class Unpickler(pickle._Unpickler):  [pandas/compat/pickle_compat.py:66]
methods: find_class, load_newobj, load_reduce

class Series(base.IndexOpsMixin, NDFrame):  # type: ignore[misc]  [pandas/core/series.py:211]
methods: _align_for_op, _append_internal, _arith_method, _binop
         _can_hold_na, _cmp_method, _construct_result
         _construct_result, _construct_result
         _constructor, _constructor_expanddim
         _constructor_expanddim_from_mgr
         _constructor_from_mgr, _flex_method
         _get_rows_with_mask, _get_value
         _get_values_tuple, _get_with, _gotitem
         _init_dict, _ixs, _logical_method
         _needs_reindex_multi, _reduce, _references
         _reindex_indexer, _set_labels, _set_name
         _set_value, _set_values, _set_with
         _set_with_engine, _slice, _values, add, aggregate
         all, any, apply, argsort, array, autocorr, axes
         between, case_when, combine, combine_first
         compare, corr, count, cov, cummax, cummin
         cumprod, cumsum, diff, divmod, dot, drop, drop
         drop, drop, drop_duplicates, drop_duplicates
         drop_duplicates, drop_duplicates, dropna, dropna
         dropna, dtype, dtypes, duplicated, eq, explode
         floordiv, from_arrow, ge, groupby, gt, idxmax
         idxmin, info, isin, isna, isnull, items, keys
         kurt, le, lt, map, max, mean, median
         memory_usage, min, mod, mode, mul, name, name, ne
         nlargest, notna, notnull, nsmallest, pop, pow
         prod, quantile, quantile, quantile, quantile
         radd, rdivmod, reindex, rename, rename, rename
         rename_axis, rename_axis, rename_axis
         rename_axis, reorder_levels, repeat, reset_index
         reset_index, reset_index, reset_index, rfloordiv
         rmod, rmul, round, rpow, rsub, rtruediv
         searchsorted, sem, set_axis, skew, sort_index
         sort_index, sort_index, sort_index, sort_values
         sort_values, sort_values, sort_values, std, sub
         sum, swaplevel, to_dict, to_dict, to_dict
         to_frame, to_markdown, to_markdown, to_markdown
         to_markdown, to_period, to_string, to_string
         to_string, to_timestamp, transform, truediv
         unique, unstack, update, values, var, __array__
         __arrow_c_stream__, __getitem__, __init__
         __len__, __matmul__, __repr__, __rmatmul__
         __setitem__

class TestPickle:  [indexes/period/test_pickle.py:14]
methods: test_pickle_freq, test_pickle_round_trip

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

    def peakmem_read_pickle(self):
        read_pickle(self.fname)

    def time_read_pickle(self):
        read_pickle(self.fname)

    def peakmem_write_pickle(self):
        self.df.to_pickle(self.fname)

    def time_write_pickle(self):
        self.df.to_pickle(self.fname)

def patch_pickle() -> Generator[None]:
    """
    Temporarily patch pickle to use our unpickler.
    """
    orig_loads = pickle.loads
    try:
        setattr(pickle, "loads", loads)
        yield
    finally:
        setattr(pickle, "loads", orig_loads)

    def setup(self):
        self.fname = "__test__.pkl"
        N = 100000
        C = 5
        self.df = DataFrame(
            np.random.randn(N, C),
            columns=[f"float{i}" for i in range(C)],
            index=date_range("20000101", periods=N, freq="h"),
        )
        self.df["object"] = Index([f"i-{i}" for i in range(N)], dtype=object)
        self.df.to_pickle(self.fname)

def to_pickle(
    obj: Any,
    filepath_or_buffer: FilePath | WriteBuffer[bytes],
    compression: CompressionOptions = "infer",
    protocol: int = pickle.HIGHEST_PROTOCOL,
    storage_options: StorageOptions | None = None,
) -> None:
    """
    # ... truncated

def write_legacy_pickles(output_dir):
    pth = f"{platform_name()}.pickle"

    with open(os.path.join(output_dir, pth), "wb") as fh:
        pickle.dump(create_pickle_data(test=False), fh, pickle.DEFAULT_PROTOCOL)

    print(f"created pickle file: {pth}")

def pickle_respnder(df):
    with BytesIO() as bio:
        df.to_pickle(bio)
        return bio.getvalue()

def read_pickle(
    filepath_or_buffer: FilePath | ReadPickleBuffer,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,
) -> DataFrame | Series:
    """
    # ... truncated

    def to_pickle(
        self,
        path: FilePath | WriteBuffer[bytes],
        *,
        compression: CompressionOptions = "infer",
        protocol: int = pickle.HIGHEST_PROTOCOL,
        storage_options: StorageOptions | None = None,
    ) -> None:
        """
    # ... truncated

    def _with_freq(self, freq):
        arr = self._data._with_freq(freq)
        return type(self)._simple_new(arr, name=self._name)

    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

    # ... truncated

def python_unpickler(path):
    with open(path, "rb") as fh:
        fh.seek(0)
        return pickle.load(fh)

def python_pickler(obj, path):
    with open(path, "wb") as fh:
        pickle.dump(obj, fh, protocol=-1)

def loads(
    bytes_object: bytes,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
) -> Any:
    """
    Analogous to pickle._loads.
    """
    fd = io.BytesIO(bytes_object)
    return Unpickler(
        fd, fix_imports=fix_imports, encoding=encoding, errors=errors
    ).load()

def round_trip_pickle(obj: Any, tmp_path: Path) -> DataFrame | Series:
    """
    Pickle an object and then read it again.

    Parameters
    ----------
    obj : any object
        The object to pickle and then re-read.
    path : str, path object or file-like object, default None
        The path where the pickled object is written and then read.

    Returns
    -------
    pandas object
        The original object that was pickled and then re-read.
    """
    pd.to_pickle(obj, tmp_path)
    return pd.read_pickle(tmp_path)

def _create_mi_with_dt64tz_level():
    """
    MultiIndex with a level that is a tzaware DatetimeIndex.
    """
    # GH#8367 round trip with pickle
    return MultiIndex.from_product(
        [[1, 2], ["a", "b"], date_range("20130101", periods=3, tz="US/Eastern")],
        names=["one", "two", "three"],
    )

def infer_freq(
    index: DatetimeIndex | TimedeltaIndex | Series | DatetimeLikeArrayMixin,
) -> str | None:
    """
    # ... truncated

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

    def to_period(
        self,
        freq: str | None = None,
        copy: bool | lib.NoDefault = lib.no_default,
    ) -> Series:
        """
    # ... truncated

    def __getstate__(self) -> dict[str_type, Any]:
        # pickle support; we don't want to pickle the cache
        return {k: getattr(self, k, None) for k in self._metadata}

    def _parse_with_reso(self, label: str) -> tuple[datetime, Resolution]:
        # overridden by TimedeltaIndex
        try:
            if self.freq is None or hasattr(self.freq, "rule_code"):
                freq = self.freq
        except NotImplementedError:
            freq = getattr(self, "freqstr", getattr(self, "inferred_freq", None))

        freqstr: str | None
        if freq is not None and not isinstance(freq, str):
            freqstr = freq.rule_code
        else:
            freqstr = freq

        if isinstance(label, np.str_):
            # GH#45580
            label = str(label)

        parsed, reso_str = parsing.parse_datetime_string_with_reso(label, freqstr)
        reso = Resolution.from_attrname(reso_str)
        return parsed, reso

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
    # ... truncated

def create_pickle_data(test: bool = True):
    """create the pickle data"""
    data = {
        "A": [0.0, 1.0, 2.0, 3.0, np.nan],
        "B": [0, 1, 0, 1, 0],
        "C": ["foo1", "foo2", "foo3", "foo4", "foo5"],
        "D": date_range("1/1/2009", periods=5),
        "E": [0.0, 1, Timestamp("20100101"), "foo", 2.0],
    }

    scalars = {"timestamp": Timestamp("20130101"), "period": Period("2012", "M")}

    # ... truncated

def after_nearest_workday(dt: datetime) -> datetime:
    """
    returns next workday after nearest workday
    needed for Boxing day or multiple holidays in a series
    """
    return next_workday(nearest_workday(dt))

def get_random_path():
    return f"__{uuid.uuid4()}__.pickle"

    def to_timestamp(
        self,
        freq: Frequency | None = None,
        how: Literal["s", "e", "start", "end"] = "start",
        copy: bool | lib.NoDefault = lib.no_default,
    ) -> Series:
        """
    # ... truncated

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

def _get_with_delta(delta, freq="YE-DEC"):
    return date_range(
        to_datetime("1/1/2001") + delta,
        to_datetime("12/31/2009") + delta,
        freq=freq,
    )

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

    def _simple_period_range_series(start, end, freq="D"):
        with warnings.catch_warnings():
            # suppress Period[B] deprecation warning
            msg = "|".join(["Period with BDay freq", r"PeriodDtype\[B\] is deprecated"])
            warnings.filterwarnings(
                "ignore",
                msg,
                category=FutureWarning,
            )
            rng = period_range(start, end, freq=freq)
        return Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)

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

    def __setstate__(self, state) -> None:
        # for pickle compat. __get_state__ is defined in the
        # PandasExtensionDtype superclass and uses the public properties to
        # pickle -> need to set the settable private ones here (see GH26067)
        self._tz = state["tz"]
        self._unit = state["unit"]

        def _check_roundtrip(obj):
            unpickled = tm.round_trip_pickle(obj, temp_file)
            assert unpickled == obj

    def copy(self):
        return self
```
