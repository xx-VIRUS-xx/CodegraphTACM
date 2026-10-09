# pandas-90 :: tacm-dyn

query: BUG: func 'to_pickle' and 'read_pickle' where not accepting URL GH#30163 (#30301)

## selected nodes

- rank=1 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=2 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py::round_trip_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py
- rank=4 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=5 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=6 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=7 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::to_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=8 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=9 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=10 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=11 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::patch_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=12 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.to_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=13 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_pickle.py
- rank=14 layer=CLASS tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py::TestCustomBusinessDay file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
- rank=15 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py::TestCustomBusinessDay._check_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
- rank=16 layer=CLASS tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::TestProtocol file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=17 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_pickle.py
- rank=18 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py
- rank=19 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::write_legacy_pickles file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=20 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::HDFStore.select_as_coordinates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=21 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=22 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=23 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=24 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.combiner file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=25 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=26 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::Unpickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=27 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=28 layer=CLASS tokens=800 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=29 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_pickle.py
- rank=30 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_pickle.py
- rank=31 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_any_index.py::TestRoundTrips file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_any_index.py
- rank=32 layer=CLASS tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::TestCompression file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=33 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype.__setstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=34 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PandasExtensionDtype.__getstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=35 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=36 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::get_random_path file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=37 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_validate_args.py::_fname file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_validate_args.py

## context

```text
file pandas/io/pickle.py
imports: __future__, pickle, typing, warnings, pandas
defines: to_pickle, read_pickle

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

class Pickle(BaseIO):  [benchmarks/io/pickle.py:13]
methods: peakmem_read_pickle, peakmem_write_pickle, setup
         time_read_pickle, time_write_pickle

    def peakmem_read_pickle(self):
        read_pickle(self.fname)

    def time_read_pickle(self):
        read_pickle(self.fname)

def to_pickle(
    obj: Any,
    filepath_or_buffer: FilePath | WriteBuffer[bytes],
    compression: CompressionOptions = "infer",
    protocol: int = pickle.HIGHEST_PROTOCOL,
    storage_options: StorageOptions | None = None,
) -> None:
    """
    # ... truncated

def read_pickle(
    filepath_or_buffer: FilePath | ReadPickleBuffer,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,
) -> DataFrame | Series:
    """
    # ... truncated

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

class TestPickle:  [indexes/datetimes/test_pickle.py:11]
methods: test_pickle, test_pickle_after_set_freq
         test_pickle_dont_infer_freq, test_pickle_unpickle
         test_roundtrip_pickle_with_tz

class TestCustomBusinessDay:  [tseries/offsets/test_custom_business_day.py:34]
methods: _check_roundtrip, test_calendar
         test_cbd_raises_if_calendar_not_busdaycalendar
         test_holidays, test_pickle_compat_0_14_1
         test_repr, test_roundtrip_pickle, test_weekmask
         test_weekmask_and_holidays

        def _check_roundtrip(obj):
            unpickled = tm.round_trip_pickle(obj, temp_file)
            assert unpickled == obj

class TestProtocol:  [tests/io/test_pickle.py:420]
methods: test_read

class TestPickle:  [indexes/period/test_pickle.py:14]
methods: test_pickle_freq, test_pickle_round_trip

def pickle_respnder(df):
    with BytesIO() as bio:
        df.to_pickle(bio)
        return bio.getvalue()

def write_legacy_pickles(output_dir):
    pth = f"{platform_name()}.pickle"

    with open(os.path.join(output_dir, pth), "wb") as fh:
        pickle.dump(create_pickle_data(test=False), fh, pickle.DEFAULT_PROTOCOL)

    print(f"created pickle file: {pth}")

    def select_as_coordinates(
        self,
        key: str,
        where=None,
        start: int | None = None,
        stop: int | None = None,
    ):
        """
        return the selection as an Index

        .. warning::

           Pandas uses PyTables for reading and writing HDF5 files, which allows
           serializing object-dtype data with pickle when using the "fixed" format.
           Loading pickled data received from untrusted sources can be unsafe.

           See: https://docs.python.org/3/library/pickle.html for more.


        Parameters
        ----------
        key : str
        where : list of Term (or convertible) objects, optional
        start : integer (defaults to None), row number to start selection
        stop  : integer (defaults to None), row number to stop selection
        """
        where = _ensure_term(where, scope_level=1)
        tbl = self.get_storer(key)
        if not isinstance(tbl, Table):
            raise TypeError("can only read_coordinates with a table")
        return tbl.read_coordinates(where=where, start=start, stop=stop)

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

        def combiner(x: Series, y: Series):
            # GH#60128 The combiner is supposed to preserve EA Dtypes.
            return y if y.name not in self.columns else y.where(x.isna(), x)

file pandas/compat/pickle_compat.py
imports: __future__, contextlib, io, pickle, typing, numpy, pandas, collections
defines: Unpickler, loads, patch_pickle

class Unpickler(pickle._Unpickler):  [pandas/compat/pickle_compat.py:66]
methods: find_class, load_newobj, load_reduce

file pandas/core/generic.py
imports: __future__, collections, copy, datetime, functools, json, operator, pickle
defines: NDFrame

class NDFrame(PandasObject, indexing.IndexingMixin):  [pandas/core/generic.py:209]
methods: _accum_func, _align_frame, _align_series
         _check_copy_deprecation
         _check_inplace_and_allows_duplicate_labels
         _check_label_or_level_ambiguity
         _clip_with_one_bound, _clip_with_scalar
         _consolidate, _consolidate_inplace
         _construct_axes_dict, _constructor
         _dir_additions, _drop_axis
         _drop_labels_or_levels, _find_valid_index
         _from_mgr, _get_axis, _get_axis_name
         _get_axis_number, _get_axis_resolvers
         _get_block_manager_axis, _get_bool_data
         _get_cleaned_column_resolvers
         _get_index_resolvers, _get_label_or_level_values
         _get_numeric_data, _getitem_slice, _indexed_same
         _info_axis, _init_mgr, _inplace_method
         _is_label_or_level_reference, _is_label_reference
         _is_level_reference, _is_mixed_type
         _logical_func, _min_count_stat_function
         _needs_reindex_multi, _pad_or_backfill
         _reindex_axes, _reindex_multi
         _reindex_with_indexers, _rename, _rename, _rename
         _rename, _repr_data_resource_, _repr_latex_
         _set_axis, _set_axis_name, _set_axis_name
         _set_axis_name, _set_axis_name, _set_axis_nocheck
         _set_axis_nocheck, _set_axis_nocheck
         _set_axis_nocheck, _shift_with_freq, _slice
         _stat_function, _stat_function_ddof
         _to_latex_via_styler, _tz_convert, _tz_localize
         _update_inplace, _validate_dtype, _values, _where
         _wrap, abs, add_prefix, add_suffix, align, all
         any, asfreq, asof, astype, at_time, attrs, attrs
         axes, between_time, bfill, blk_func, blk_func
         block_accum_func, clip, compare, convert_dtypes
         copy, cummax, cummin, cumprod, cumsum, describe
         drop, drop, drop, drop, droplevel, dtypes, empty
         equals, ewm, expanding, f, f, ffill, fillna
         filter, first_valid_index, flags, get, head
         infer_objects, interpolate, isna, isnull, items
         keys, kurt, last_valid_index, mask, max, mean
         median, min, ndim, notna, notnull, pct_change
         pipe, pipe, pipe, pop, prod, rank, ranker
         reindex, reindex_like, rename_axis, rename_axis
         rename_axis, rename_axis, replace, resample
         rolling, sample, sem, set_axis, set_flags, shape
         shift, size, skew, sort_index, sort_index
         sort_index, sort_index, sort_values, sort_values
         sort_values, sort_values, squeeze, std, sum, tail
         take, to_clipboard, to_csv, to_csv, to_csv
         to_excel, to_hdf, to_json, to_latex, to_latex
         to_latex, to_pickle, to_sql, to_xarray, truncate
         tz_convert, tz_localize, values, var, where, xs
         __abs__, __array__, __array_ufunc__, __bool__
         __contains__, __copy__, __deepcopy__, __delitem__
         __finalize__, __getattr__, __getitem__
         __getstate__, __iadd__, __iand__, __ifloordiv__
         __imod__, __imul__, __init__, __invert__, __ior__
         __ipow__, __isub__, __iter__, __itruediv__
         __ixor__, __len__, __neg__, __pos__, __repr__
         __round__, __setattr__, __setstate__

class TestPickle:  [indexes/interval/test_pickle.py:5]
methods: test_pickle_round_trip_closed

class TestPickle:  [indexes/timedeltas/test_pickle.py:5]
methods: test_pickle_after_set_freq

class TestRoundTrips:  [tests/indexes/test_any_index.py:104]
methods: test_pickle_preserves_name, test_pickle_roundtrip

class TestCompression:  [tests/io/test_pickle.py:284]
methods: compress_file, test_read_explicit, test_read_infer
         test_write_explicit, test_write_explicit_bad
         test_write_infer

    def __setstate__(self, state) -> None:
        # for pickle compat. __get_state__ is defined in the
        # PandasExtensionDtype superclass and uses the public properties to
        # pickle -> need to set the settable private ones here (see GH26067)
        self._tz = state["tz"]
        self._unit = state["unit"]

    def __getstate__(self) -> dict[str_type, Any]:
        # pickle support; we don't want to pickle the cache
        return {k: getattr(self, k, None) for k in self._metadata}

    def _where(
        self,
        cond,
        other=lib.no_default,
        *,
        inplace: bool = False,
        axis: Axis | None = None,
        level=None,
    ) -> Self:
        """
    # ... truncated

def get_random_path():
    return f"__{uuid.uuid4()}__.pickle"

def _fname():
    return "func"
```
