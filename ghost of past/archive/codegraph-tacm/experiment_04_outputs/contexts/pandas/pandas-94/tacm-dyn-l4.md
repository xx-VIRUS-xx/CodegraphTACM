# pandas-94 :: tacm-dyn-l4

query: BUG: TDI/DTI _shallow_copy creating invalid arrays (#30764)

## selected nodes

- rank=1 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=2 layer=CLASS tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=3 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=4 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=5 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::Indexing.time_shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=6 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py::TimedeltaIndexing.time_shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py
- rank=7 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py
- rank=8 layer=CLASS tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_constructors.py::TestShallowCopy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_constructors.py
- rank=9 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py
- rank=10 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=11 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=12 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=13 layer=FUNCTION tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=14 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::make_invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=15 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=16 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._iter_column_arrays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=17 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._from_arrays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=18 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=19 layer=CLASS tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py::TestVectorizedTimedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py
- rank=20 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._maybe_cast_slice_bound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=21 layer=CLASS tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=22 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=23 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta_dti file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=24 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::_test_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py
- rank=25 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=26 layer=CLASS tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::TestTimedelta64ArithmeticUnsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=27 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=28 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::SortedAndUnsortedDatetimeIndexLoc.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=29 layer=FILE tokens=216 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/clipboard/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/clipboard/__init__.py
- rank=30 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/clipboard/__init__.py::init_klipper_clipboard file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/clipboard/__init__.py
- rank=31 layer=FILE tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=32 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::_make_unpacked_invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=33 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::DatetimeIndexConstructor.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py
- rank=34 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.from_arrays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=35 layer=FUNCTION tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py::ParallelDatetimeFields.time_datetime_field_normalize file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py
- rank=36 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/array_with_attr/array.py::FloatAttrArray.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/array_with_attr/array.py

## context

```text
file core/ops/invalid.py
imports: __future__, operator, typing, numpy, collections, pandas
defines: invalid_comparison, make_invalid_op, invalid_op

class TestDatetimeIndexArithmetic:  [tests/arithmetic/test_datetime64.py:2021]
methods: test_dta_add_sub_index, test_dti_add_series
         test_dti_add_tdi
         test_dti_addsub_object_arraylike
         test_dti_addsub_offset_arraylike
         test_dti_iadd_tdi, test_dti_isub_tdi
         test_dti_sub_tdi
         test_ops_nat_mixed_datetime64_timedelta64
         test_sub_dti_dti
         test_timedelta64_equal_timedelta_supported_ops
         test_ufunc_coercions, timedelta64

    def tdi(self, monotonic):
        tdi = timedelta_range("1 Day", periods=10)
        if monotonic == "decreasing":
            tdi = tdi[::-1]
        elif monotonic is None:
            taker = np.arange(10, dtype=np.intp)
            np.random.default_rng(2).shuffle(taker)
            tdi = tdi.take(taker)
        return tdi

    def time_shallow_copy(self):
        self.index._view()

    def time_shallow_copy(self):
        self.index._view()

    def time_shallow_copy(self):
        self.index._view()

    def _check_setitem_invalid(self, ser, invalid, indexer):
        orig_ser = ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser[indexer] = invalid
            ser = orig_ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser.iloc[indexer] = invalid
            ser = orig_ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser.loc[indexer] = invalid
            ser = orig_ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser[:] = invalid

class TestShallowCopy:  [indexes/period/test_constructors.py:682]
methods: test_shallow_copy_disallow_i8, test_shallow_copy_empty
         test_shallow_copy_requires_disallow_period_index

    def _check_setitem_invalid(self, df, invalid, indexer):
        orig_df = df.copy()

        # iloc
        with pytest.raises(TypeError, match="Invalid value"):
            df.iloc[indexer, 0] = invalid
            df = orig_df.copy()

        # loc
        with pytest.raises(TypeError, match="Invalid value"):
            df.loc[indexer, "a"] = invalid
            df = orig_df.copy()

    def copy(self) -> Self:
        """
        Return a shallow copy of the array.

        Underlying ChunkedArray is immutable, so a deep copy is unnecessary.

        Returns
        -------
        type(self)
        """
        return self._from_pyarrow_array(self._pa_array)

    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

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

    def copy(self, *, deep: bool) -> Self:
        """
        Make deep or shallow copy of BlockManager

        Parameters
        ----------
        deep : bool, string or None, default True
            If False, return a shallow copy (do not copy data)

        Returns
        -------
        BlockManager
        """
        # TODO: Should deep=True be respected for axes?
        new_axes = [ax.view() for ax in self.axes]

        res = self.apply("copy", deep=deep)
        res.axes = new_axes

        if self.ndim > 1:
            # Avoid needing to re-compute these
            blknos = self._blknos
            if blknos is not None:
                res._blknos = blknos.copy()
                res._blklocs = self._blklocs.copy()

        if deep:
            res._consolidate_inplace()
        return res

def make_invalid_op(name: str) -> Callable[..., NoReturn]:
    """
    Return a binary method that always raises a TypeError.

    Parameters
    ----------
    name : str

    Returns
    -------
    invalid_op : function
    """

    def invalid_op(self: object, other: object = None) -> NoReturn:
        typ = type(self).__name__
        raise TypeError(f"cannot perform {name} with this index type: {typ}")

    invalid_op.__name__ = name
    return invalid_op

    def __array__(
        self, dtype: NpDtype | None = None, copy: bool | None = None
    ) -> np.ndarray:
        """Correctly construct numpy arrays when passed to `np.asarray()`."""
        if copy is False:
            # TODO: By using `zero_copy_only` it may be possible to implement this
            raise ValueError(
                "Unable to avoid copy while creating an array as requested."
            )
        elif copy is None:
            # `to_numpy(copy=False)` has the meaning of NumPy `copy=None`.
            copy = False

        return self.to_numpy(dtype=dtype, copy=copy)

    def _iter_column_arrays(self) -> Iterator[ArrayLike]:
        """
        Iterate over the arrays of all columns in order.
        This returns the values as stored in the Block (ndarray or ExtensionArray).

        Warning! The returned array is a view but doesn't handle Copy-on-Write,
        so this should be used with caution (for read-only purposes).
        """
        for i in range(len(self.columns)):
            yield self._get_column_array(i)

    def _from_arrays(
        cls,
        arrays,
        columns,
        index,
        dtype: Dtype | None = None,
        verify_integrity: bool = True,
    ) -> Self:
        """
    # ... truncated

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

class TestVectorizedTimedelta:  [indexes/timedeltas/test_scalar_compat.py:21]
methods: test_components, test_round, test_tdi_round
         test_tdi_round_invalid, test_tdi_total_seconds
         test_tdi_total_seconds_all_nat

    def _maybe_cast_slice_bound(self, label, side: str):
        """
        If label is a string, cast it to scalar type according to resolution.

        Parameters
        ----------
        label : object
        side : {'left', 'right'}

        Returns
        -------
        label : object

        Notes
        -----
        Value of `side` parameter should be validated in caller.
        """
        if isinstance(label, str):
            try:
                parsed, reso = self._parse_with_reso(label)
            except ValueError as err:
                # DTI -> parsing.DateParseError
                # TDI -> 'unit abbreviation w/o a number'
                # PI -> string cannot be parsed as datetime-like
                self._raise_invalid_indexer("slice", label, err)

            lower, upper = self._parsed_string_to_bounds(reso, parsed)
            return lower if side == "left" else upper
        elif not isinstance(label, self._data._recognized_scalars):
            self._raise_invalid_indexer("slice", label)

        return label

class TestDatetimeIndexComparisons:  [tests/arithmetic/test_datetime64.py:408]
methods: test_comparators, test_comparison_tzawareness_compat
         test_comparison_tzawareness_compat_scalars
         test_dti_cmp_datetimelike, test_dti_cmp_list
         test_dti_cmp_nat
         test_dti_cmp_nat_behaves_like_float_cmp_nan
         test_dti_cmp_object_dtype, test_dti_cmp_str
         test_dti_cmp_tdi_tzawareness
         test_nat_comparison_tzawareness
         test_scalar_comparison_tzawareness

    def dta(self, dta_dti):
        dta, dti = dta_dti
        return dta

    def dta_dti(self, unit, dtype):
        tz = getattr(dtype, "tz", None)

        dti = pd.date_range("2016-01-01", periods=55, freq="D", tz=tz, unit="ns")
        if tz is None:
            arr = np.asarray(dti).astype(f"M8[{unit}]")
        else:
            arr = np.asarray(dti.tz_convert("UTC").tz_localize(None)).astype(
                f"M8[{unit}]"
            )

        dta = DatetimeArray._simple_new(arr, dtype=dtype)
        return dta, dti

def _test_series(dti):
    return Series(np.random.default_rng(2).random(len(dti)), dti)

    def setup(self):
        dti = date_range("2016-01-01", periods=10000, tz="US/Pacific")
        dti2 = dti.tz_convert("UTC")
        self.dti = dti
        self.dti2 = dti2

class TestTimedelta64ArithmeticUnsorted:  [tests/arithmetic/test_timedelta64.py:273]
methods: _check, test_addition_ops, test_dti_tdi_numeric_ops
         test_subtraction_ops
         test_subtraction_ops_with_tz
         test_td64_op_with_list
         test_tda_add_dt64_object_array
         test_tda_add_sub_index
         test_tdi_iadd_timedeltalike
         test_tdi_isub_timedeltalike
         test_tdi_ops_attributes, test_timedelta
         test_timedelta_tick_arithmetic
         test_ufunc_coercions

file pandas/core/generic.py
imports: __future__, collections, copy, datetime, functools, json, operator, pickle
defines: NDFrame

    def setup(self):
        dti = date_range("2016-01-01", periods=10000, tz="US/Pacific")
        index = np.array(dti)

        unsorted_index = index.copy()
        unsorted_index[10] = unsorted_index[20]

        self.df_unsorted = DataFrame(index=unsorted_index, data={"a": 1})
        self.df_sort = DataFrame(index=index, data={"a": 1})

file io/clipboard/__init__.py
imports: pyperclip, contextlib, ctypes, os, platform, shutil, subprocess, time
defines: PyperclipTimeoutException, ClipboardUnavailable, CheckedCall, _stringifyText, init_osx_pbcopy_clipboard, copy_osx_pbcopy, paste_osx_pbcopy, init_osx_pyobjc_clipboard, copy_osx_pyobjc, paste_osx_pyobjc, init_qt_clipboard, copy_qt, paste_qt, init_xclip_clipboard, copy_xclip, paste_xclip, init_xsel_clipboard, copy_xsel, paste_xsel, init_wl_clipboard, copy_wl, paste_wl, init_klipper_clipboard, copy_klipper, paste_klipper, init_dev_clipboard_clipboard, copy_dev_clipboard, paste_dev_clipboard, init_no_clipboard, init_windows_clipboard, window, clipboard, copy_windows, paste_windows, init_wsl_clipboard, copy_wsl, paste_wsl, determine_clipboard, set_clipboard, lazy_load_stub_copy, lazy_load_stub_paste, is_available, waitForPaste, waitForNewPaste

file core/arrays/datetimelike.py
imports: __future__, datetime, functools, itertools, operator, typing, warnings, numpy
defines: DatetimeLikeArrayMixin, DatelikeOps, TimelikeOps, _make_unpacked_invalid_op, _period_dispatch, new_meth, ensure_arraylike_for_datetimelike, validate_periods, validate_periods, validate_periods, _validate_inferred_freq, dtype_to_unit

def _make_unpacked_invalid_op(op_name: str):
    op = make_invalid_op(op_name)
    return unpack_zerodim_and_defer(op_name)(op)

    def setup(self):
        N = 20_000
        dti = date_range("1900-01-01", periods=N)

        self.list_of_timestamps = dti.tolist()
        self.list_of_dates = dti.date.tolist()
        self.list_of_datetimes = dti.to_pydatetime().tolist()
        self.list_of_str = dti.strftime("%Y-%m-%d").tolist()

def is_available() -> bool:
    return copy != lazy_load_stub_copy and paste != lazy_load_stub_paste

    def copy(self):
        return self

# --- Layer 04: Variable context ---
# call-chain context
  called by: setup [categoricals.py]
  called by: setup [frame_methods.py]

# call-chain context
  called by: _partial_date_slice [datetimelike.py]
  called by: get_loc [datetimes.py]

# call-chain context
  called by: setup [categoricals.py]
  called by: setup [frame_methods.py]

# call-chain context
  called by: _make_unpacked_invalid_op [datetimelike.py]

# call-chain context
  called by: transpose [frame.py]
  called by: _dispatch_frame_op [frame.py]

# call-chain context
  called by: time_frame_from_arrays_float [frame_ctor.py]
  called by: time_frame_from_arrays_int [frame_ctor.py]

# call-chain context
  called by: setup [algorithms.py]
  called by: setup [algorithms.py]

# call-chain context
  called by: setup [categoricals.py]
  called by: setup [frame_methods.py]

```
