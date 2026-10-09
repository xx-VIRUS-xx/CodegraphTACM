# pandas-15 :: tacm-dyn-l4

query: BUG: pickle after _with_freq (#33811)

## selected nodes

- rank=1 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=2 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_pickle.py
- rank=3 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::to_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=4 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::write_legacy_pickles file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=5 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py
- rank=6 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=7 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=8 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=9 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=10 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::patch_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=11 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_pickle.py
- rank=12 layer=FILE tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=13 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.to_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=14 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=15 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=16 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=17 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=18 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_unpickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=19 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_pickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=20 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::loads file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=21 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=22 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=23 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py::round_trip_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py
- rank=24 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=25 layer=FUNCTION tokens=407 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::maybe_resample file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=26 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::prepare_ts_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=27 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=28 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=29 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=30 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PandasExtensionDtype.__getstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=31 layer=FUNCTION tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._parse_with_reso file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=32 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=33 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=34 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::create_pickle_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=35 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/holiday.py::after_nearest_workday file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/holiday.py
- rank=36 layer=FILE tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py
- rank=37 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::infer_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py
- rank=38 layer=FILE tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/numpy/function.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/numpy/function.py
- rank=39 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_to_timestamp.py::_get_with_delta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_to_timestamp.py
- rank=40 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::_simple_period_range_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py
- rank=41 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=42 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=43 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.truncate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=44 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_pickle.py

## context

```text
file pandas/io/pickle.py
imports: __future__, pickle, typing, warnings, pandas
defines: to_pickle, read_pickle

class TestPickle:  [indexes/datetimes/test_pickle.py:11]
methods: test_pickle, test_pickle_after_set_freq
         test_pickle_dont_infer_freq, test_pickle_unpickle
         test_roundtrip_pickle_with_tz

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

    def peakmem_read_pickle(self):
        read_pickle(self.fname)

    def time_read_pickle(self):
        read_pickle(self.fname)

file pandas/compat/pickle_compat.py
imports: __future__, contextlib, io, pickle, typing, numpy, pandas, collections
defines: Unpickler, loads, patch_pickle

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

class TestPickle:  [indexes/timedeltas/test_pickle.py:5]
methods: test_pickle_after_set_freq

file benchmarks/io/pickle.py
imports: numpy, pandas, pandas_vb_common
defines: Pickle

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

file pandas/core/generic.py
imports: __future__, collections, copy, datetime, functools, json, operator, pickle
defines: NDFrame

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

class DataFrame(NDFrame, OpsMixin):  [pandas/core/frame.py:269]
methods: T, _align_for_op, _append_internal, _arith_method
         _arith_method_with_reindex, _arith_op
         _box_col_values, _can_fast_transpose, _cmp_method
         _combine_frame, _construct_result, _constructor
         _constructor_from_mgr
         _constructor_sliced_from_mgr, _dict_round
         _dispatch_frame_op, _ensure_valid_index
         _flex_arith_method, _flex_cmp_method
         _from_arrays, _get_agg_axis, _get_column_array
         _get_data, _get_item, _get_value
         _get_values_for_csv, _getitem_bool_array
         _getitem_multilevel, _gotitem, _info_repr
         _is_homogeneous_type, _iset_item, _iset_item_mgr
         _iset_not_inplace, _iter_column_arrays, _ixs
         _maybe_align_series_as_frame, _reduce
         _reduce_axis1, _reindex_multi
         _replace_columnwise, _repr_fits_horizontal_
         _repr_fits_vertical_, _repr_html_
         _sanitize_column, _series, _series_round
         _set_item, _set_item_frame_value, _set_item_mgr
         _set_value, _setitem_array, _setitem_frame
         _setitem_slice, _should_reindex_frame_op
         _to_dict_of_blocks, _values, add, aggregate, all
         all, all, all, any, any, any, any, apply, assign
         axes, blk_func, c, check_int_infer_dtype, combine
         combine_first, combiner, compare, corr, corrwith
         count, cov, create_index, cummax, cummin, cumprod
         cumsum, diff, dot, dot, dot, drop, drop, drop
         drop, drop_duplicates, drop_duplicates
         drop_duplicates, drop_duplicates, dropna, dropna
         dropna, dtype_predicate, duplicated, eq, eval
         eval, eval, explode, f, f, floordiv, from_arrow
         from_dict, from_records, func, ge, groupby, gt
         idxmax, idxmin, igetitem, infer, info, insert
         isetitem, isin, isin_, isna, isnull, items
         iterrows, itertuples, join, kurt, kurt, kurt
         kurt, le, lt, map, max, max, max, max
         maybe_reorder, mean, mean, mean, mean, median
         median, median, median, melt, memory_usage, merge
         min, min, min, min, mod, mode, mul, ne, nlargest
         notna, notnull, nsmallest, nunique, pivot
         pivot_table, pop, pow, predicate, prod, quantile
         quantile, quantile, quantile, query, query, query
         query, radd, reindex, rename, rename, rename
         rename, reorder_levels, reset_index, reset_index
         reset_index, reset_index, rfloordiv, rmod, rmul
         round, rpow, rsub, rtruediv, select_dtypes, sem
         sem, sem, sem, set_axis, set_index, set_index
         set_index, shape, shift, skew, skew, skew, skew
         sort_index, sort_index, sort_index, sort_index
         sort_values, sort_values, sort_values, stack, std
         std, std, std, style, sub, sum, swaplevel
         to_dict, to_dict, to_dict, to_dict, to_dict
         to_feather, to_html, to_html, to_html, to_iceberg
         to_markdown, to_markdown, to_markdown
         to_markdown, to_numpy, to_orc, to_orc, to_orc
         to_orc, to_parquet, to_parquet, to_parquet
         to_period, to_records, to_series, to_stata
         to_string, to_string, to_string, to_timestamp
         to_xml, to_xml, to_xml, transform, transpose
         truediv, unstack, update, value_counts, values
         var, var, var, var, __arrow_c_stream__
         __dataframe__, __divmod__, __getitem__, __init__
         __len__, __matmul__, __matmul__, __matmul__
         __rdivmod__, __repr__, __rmatmul__, __setitem__

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

    def peakmem_write_pickle(self):
        self.df.to_pickle(self.fname)

    def shift(
        self,
        periods: int | Sequence[int] = 1,
        freq: Frequency | None = None,
        axis: Axis = 0,
        fill_value: Hashable = lib.no_default,
        suffix: str | None = None,
    ) -> DataFrame:
        """
    # ... truncated

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

file plotting/_matplotlib/timeseries.py
imports: __future__, functools, typing, numpy, pandas, datetime, matplotlib
defines: maybe_resample, _is_sub, _is_sup, _upsample_others, _replot_ax, decorate_axes, _get_ax_freq, _get_period_alias, _get_freq, use_dynamic_x, _get_index_freq, maybe_convert_index, _format_coord, format_dateaxis, prepare_ts_data

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

def prepare_ts_data(
    series: Series, ax: Axes, kwargs: dict[str, Any]
) -> tuple[BaseOffset | str, Series]:
    freq, data = maybe_resample(series, ax, kwargs)

    # Set ax with freq info
    decorate_axes(ax, freq)
    # digging deeper
    if hasattr(ax, "left_ax"):
        decorate_axes(ax.left_ax, freq)
    if hasattr(ax, "right_ax"):
        decorate_axes(ax.right_ax, freq)

    return freq, data

def _get_freq(ax: Axes, series: Series):
    # get frequency from data
    freq = getattr(series.index, "freq", None)
    if freq is None:
        freq = getattr(series.index, "inferred_freq", None)
        freq = to_offset(freq, is_period=True)

    ax_freq = _get_ax_freq(ax)

    # use axes freq if no data freq
    if freq is None:
        freq = ax_freq

    # get the period frequency
    freq = _get_period_alias(freq)
    return freq, ax_freq

def _create_mi_with_dt64tz_level():
    """
    MultiIndex with a level that is a tzaware DatetimeIndex.
    """
    # GH#8367 round trip with pickle
    return MultiIndex.from_product(
        [[1, 2], ["a", "b"], date_range("20130101", periods=3, tz="US/Eastern")],
        names=["one", "two", "three"],
    )

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

    def to_period(
        self,
        freq: Frequency | None = None,
        axis: Axis = 0,
        copy: bool | lib.NoDefault = lib.no_default,
    ) -> DataFrame:
        """
    # ... truncated

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

file pandas/tseries/frequencies.py
imports: __future__, typing, numpy, pandas
defines: _FrequencyInferer, _TimedeltaFrequencyInferer, get_period_alias, infer_freq, _is_multiple, _maybe_add_count, is_subperiod, is_superperiod, _maybe_coerce_freq, _quarter_months_conform, _is_annual, _is_quarterly, _is_monthly, _is_weekly

    def time_write_pickle(self):
        self.df.to_pickle(self.fname)

    def freq(self):
        return self._freq

# --- Layer 04: Variable context ---
# call-chain context
  called by: setup [pickle.py]
  called by: time_write_pickle [pickle.py]

# call-chain context
  called by: write_legacy_file [generate_legacy_storage_files.py]

# call-chain context
  called by: time_read_pickle [pickle.py]
  called by: peakmem_read_pickle [pickle.py]

# call-chain context
  called by: get [pytables.py]

# call-chain context
  called by: setup [pickle.py]
  called by: time_write_pickle [pickle.py]

# call-chain context
  called by: normalize [datetimes.py]
  called by: to_timestamp [period.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: __arrow_ext_deserialize__ [extension_types.py]
  called by: __arrow_ext_deserialize__ [extension_types.py]

# call-chain context
  called by: time_timestamp_ops_diff_with_shift [arithmetic.py]
  called by: time_shift [frame_methods.py]

# call-chain context
  called by: _test_roundtrip [test_pickle.py]
  called by: _check_roundtrip [test_custom_business_day.py]

# call-chain context
  called by: prepare_ts_data [timeseries.py]

# call-chain context
  called by: _make_plot [core.py]
  called by: _ts_plot [core.py]

# call-chain context
  called by: maybe_resample [timeseries.py]

# call-chain context
  called by: normalize [datetimes.py]
  called by: to_timestamp [period.py]

# call-chain context
  called by: _get_string_slice [datetimelike.py]
  called by: _maybe_cast_slice_bound [datetimelike.py]

# call-chain context
  called by: setup [gil.py]
  called by: run [gil.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

```
