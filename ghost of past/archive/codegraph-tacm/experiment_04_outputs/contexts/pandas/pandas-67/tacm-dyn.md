# pandas-67 :: tacm-dyn

query: BUG: Block.iget not wrapping timedelta64/datetime64 (#31666)

## selected nodes

- rank=1 layer=FILE tokens=233 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py
- rank=2 layer=CLASS tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=3 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py::_classes_and_not_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py
- rank=4 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=5 layer=FILE tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py
- rank=6 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py::is_ea_or_datetimelike_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py
- rank=7 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=8 layer=CLASS tokens=257 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=9 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.iget file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=10 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=11 layer=CLASS tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=12 layer=CLASS tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=13 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic.timedelta64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=14 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unwrap_setitem_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=15 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=16 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._get_column_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=17 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py
- rank=18 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py::_make_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py
- rank=19 layer=CLASS tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::DataIndexableCol file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=20 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::DataIndexableCol.get_atom_timedelta64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=21 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::DataIndexableCol.get_atom_datetime64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=22 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py::make_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py
- rank=23 layer=FUNCTION tokens=178 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py::_parse_latex_table_wrapping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py
- rank=24 layer=FILE tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/ops.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/ops.py
- rank=25 layer=FUNCTION tokens=425 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=26 layer=CLASS tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reductions/test_reductions.py::TestIndexReductions file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reductions/test_reductions.py
- rank=27 layer=CLASS tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/sparse/test_array.py::TestSparseArrayAnalytics file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/sparse/test_array.py
- rank=28 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py

## context

```text
file core/dtypes/common.py
imports: __future__, typing, warnings, numpy, pandas, collections
defines: ensure_str, ensure_python_int, classes, _classes_and_not_datetimelike, is_object_dtype, is_sparse, is_scipy_sparse, is_datetime64_dtype, is_datetime64tz_dtype, is_timedelta64_dtype, is_period_dtype, is_interval_dtype, is_categorical_dtype, is_string_or_object_np_dtype, is_string_dtype, condition, is_dtype_equal, is_integer_dtype, is_signed_integer_dtype, is_unsigned_integer_dtype, is_int64_dtype, is_datetime64_any_dtype, is_datetime64_ns_dtype, is_timedelta64_ns_dtype, is_numeric_v_string_like, needs_i8_conversion, is_numeric_dtype, is_any_real_numeric_dtype, is_float_dtype, is_bool_dtype, is_1d_only_ea_dtype, is_extension_array_dtype, is_ea_or_datetimelike_dtype, is_complex_dtype, _is_dtype, _get_dtype, _is_dtype_type, infer_dtype_from_object, _validate_date_like_dtype, validate_all_hashable, pandas_dtype, is_all_strings

class ExtensionBlock(EABackedBlock):  [core/internals/blocks.py:1905]
methods: _maybe_squeeze_arg, _slice, _unstack
         _unwrap_setitem_indexer, fillna, iget, is_numeric
         is_view, set_inplace, shape, slice_block_rows

def _classes_and_not_datetimelike(*klasses) -> Callable:
    """
    Evaluate if the tipo is a subclass of the klasses
    and not a datetimelike.
    """
    return lambda tipo: (
        issubclass(tipo, klasses)
        and not issubclass(tipo, (np.datetime64, np.timedelta64))
    )

    def iget(self, i: int, track_ref: bool = True) -> SingleBlockManager:
        """
        Return the data as a SingleBlockManager.
        """
        block = self.blocks[self.blknos[i]]
        values = block.iget(self.blklocs[i])

        # shortcut for select a single-dim from a 2-dim BM
        bp = BlockPlacement(slice(0, len(values)))
        nb = type(block)(
            values, placement=bp, ndim=1, refs=block.refs if track_ref else None
        )
        return SingleBlockManager(nb, self.axes[1].view())

file io/formats/format.py
imports: __future__, collections, contextlib, csv, decimal, functools, io, math
defines: SeriesFormatter, DataFrameFormatter, DataFrameRenderer, _GenericArrayFormatter, FloatArrayFormatter, _IntArrayFormatter, _Datetime64Formatter, _ExtensionArrayFormatter, _Datetime64TZFormatter, _Timedelta64Formatter, EngFormatter, get_dataframe_repr_params, get_series_repr_params, save_to_buffer, _get_buffer, format_array, format_percentiles, get_precision, _format_datetime64, _format_datetime64_dateonly, get_format_datetime64, get_format_timedelta64, _formatter, _make_fixed_width, _trim_zeros_complex, _trim_zeros_single_float, _trim_zeros_float, _has_names, set_eng_float_format, get_level_lengths, buffer_put_lines

def is_ea_or_datetimelike_dtype(dtype: DtypeObj | None) -> bool:
    """
    Check for ExtensionDtype, datetime64 dtype, or timedelta64 dtype.

    Notes
    -----
    Checks only for dtype objects, not dtype-castable strings or types.
    """
    return isinstance(dtype, ExtensionDtype) or (lib.is_np_dtype(dtype, "mM"))

file core/internals/blocks.py
imports: __future__, inspect, re, typing, warnings, numpy, pandas
defines: Block, EABackedBlock, ExtensionBlock, NumpyBlock, NDArrayBackedExtensionBlock, DatetimeLikeBlock, maybe_coerce_values, get_block_type, new_block_2d, new_block, check_ndim, extract_pandas_array, extend_blocks, ensure_block_shape, external_values

class Block(PandasObject, libinternals.Block):  [core/internals/blocks.py:139]
methods: _can_consolidate, _can_hold_element, _can_hold_na
         _consolidate_key, _get_refs_and_copy, _maybe_copy
         _maybe_squeeze_arg, _replace_coerce
         _replace_regex, _slice, _split, _split_op_result
         _standardize_fill_value, _unstack
         _unwrap_setitem_indexer, _validate_ndim, apply
         array_values, astype, coerce_to_target_dtype
         convert, convert_dtypes, copy, delete, diff
         dtype, external_values, fill_value, fillna
         get_values, get_values_for_csv
         getitem_block_columns, iget, interpolate, is_bool
         is_extension, is_object, is_view, make_block
         make_block_same_class, mgr_locs, mgr_locs
         pad_or_backfill, putmask, quantile, reduce
         replace, replace_list, round, set_inplace
         setitem, shape, shift, should_store
         slice_block_columns, split_and_operate
         take_block_columns, take_nd, where, __len__
         __repr__

    def iget(self, i: int | tuple[int, int] | tuple[slice, int]) -> np.ndarray:
        # In the case where we have a tuple[slice, int], the slice will always
        #  be slice(None)
        # Note: only reached with self.ndim == 2
        # Invalid index type "Union[int, Tuple[int, int], Tuple[slice, int]]"
        # for "Union[ndarray[Any, Any], ExtensionArray]"; expected type
        # "Union[int, integer[Any]]"
        return self.values[i]  # type: ignore[index]

    def iget_values(self, i: int) -> ArrayLike:
        """
        Return the data for column i as the values (ndarray or ExtensionArray).

        Warning! The returned array is a view but doesn't handle Copy-on-Write,
        so this should be used with caution.
        """
        # TODO(CoW) making the arrays read-only might make this safer to use?
        block = self.blocks[self.blknos[i]]
        values = block.iget(self.blklocs[i])
        return values

class BlockManager(libinternals.BlockManager, BaseBlockManager):  [core/internals/managers.py:1077]
methods: _consolidate_check, _consolidate_inplace, _equal_values
         _insert_update_blklocs_and_blknos
         _insert_update_mgr_locs, _interleave
         _iset_single, _iset_split_block
         _verify_integrity, as_array, column_arrays
         column_setitem, concat_horizontal
         concat_vertical, fast_xs, from_blocks
         grouped_reduce, idelete, iget, iget_values
         insert, is_consolidated, iset, operate_blockwise
         quantile, reduce, to_iter_dict, unstack
         value_getitem, value_getitem, __init__

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

        def timedelta64(*args):
            # see casting notes in NumPy gh-12927
            return np.sum(list(map(np.timedelta64, args, intervals)))

    def _unwrap_setitem_indexer(self, indexer):
        """
        Adapt a 2D-indexer to our 1D values.

        This is intended for 'setitem', not 'iget' or '_slice'.
        """
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

    def _get_column_array(self, i: int) -> ArrayLike:
        """
        Get the values of the i'th column (ndarray or ExtensionArray, as stored
        in the Block)

        Warning! The returned array is a view but doesn't handle Copy-on-Write,
        so this should be used with caution (for read-only purposes).
        """
        return self._mgr.iget_values(i)

file core/internals/api.py
imports: __future__, typing, warnings, numpy, pandas
defines: _DatetimeTZBlock, _make_block, make_block, _maybe_infer_ndim, maybe_infer_ndim

def _make_block(values: ArrayLike, placement: np.ndarray) -> Block:
    """
    This is an analogue to blocks.new_block(_2d) that ensures:
    1) correct dimension for EAs that support 2D (`ensure_block_shape`), and
    2) correct EA class for datetime64/timedelta64 (`maybe_coerce_values`).

    The input `values` is assumed to be either numpy array or ExtensionArray:
    - In case of a numpy array, it is assumed to already be in the expected
      shape for Blocks (2D, (cols, rows)).
    - In case of an ExtensionArray the input can be 1D, also for EAs that are
      internally stored as 2D.

    For the rest no preprocessing or validation is done, except for those dtypes
    that are internally stored as EAs but have an exact numpy equivalent (and at
    the moment use that numpy dtype), i.e. datetime64/timedelta64.
    """
    dtype = values.dtype
    klass = get_block_type(dtype)
    placement_obj = BlockPlacement(placement)

    if (isinstance(dtype, ExtensionDtype) and dtype._supports_2d) or isinstance(
        values, (DatetimeArray, TimedeltaArray)
    ):
        values = ensure_block_shape(values, ndim=2)

    values = maybe_coerce_values(values)
    return klass(values, ndim=2, placement=placement_obj)

class DataIndexableCol(DataCol):  [pandas/io/pytables.py:2866]
methods: get_atom_data, get_atom_datetime64, get_atom_string
         get_atom_timedelta64, validate_names

    def get_atom_timedelta64(cls, shape):
        return _tables().Int64Col()

    def get_atom_datetime64(cls, shape):
        return _tables().Int64Col()

def make_block(
    values, placement, klass=None, ndim=None, dtype: Dtype | None = None
) -> Block:
    """
    # ... truncated

def _parse_latex_table_wrapping(table_styles: CSSStyles, caption: str | None) -> bool:
    """
    Indicate whether LaTeX {tabular} should be wrapped with a {table} environment.

    Parses the `table_styles` and detects any selectors which must be included outside
    of {tabular}, i.e. indicating that wrapping must occur, and therefore return True,
    or if a caption exists and requires similar.
    """
    IGNORED_WRAPPERS = ["toprule", "midrule", "bottomrule", "column_format"]
    # ignored selectors are included with {tabular} so do not need wrapping
    return (
        table_styles is not None
        and any(d["selector"] not in IGNORED_WRAPPERS for d in table_styles)
    ) or caption is not None

file core/internals/ops.py
imports: __future__, typing, pandas, collections
defines: BlockPairInfo, _iter_block_pairs, operate_blockwise, _reset_block_mgr_locs, _get_same_shape_values, blockwise_all

    def _values(self):
        """
        Return the internal repr of this data (defined by Block.interval_values).
        This are the values as stored in the Block (ndarray or ExtensionArray
        depending on the Block class), with datetime64[ns] and timedelta64[ns]
        wrapped in ExtensionArrays to match Index._values behavior.

        Differs from the public ``.values`` for certain data types, because of
        historical backwards compatibility of the public attribute (e.g. period
        returns object ndarray and datetimetz a datetime64[ns] ndarray for
        ``.values`` while it returns an ExtensionArray for ``._values`` in those
        cases).

        Differs from ``.array`` in that this still returns the numpy array if
        the Block is backed by a numpy array (except for datetime64 and
        timedelta64 dtypes), while ``.array`` ensures to always return an
        ExtensionArray.

        Overview:

        dtype       | values        | _values       | array                 |
        ----------- | ------------- | ------------- | --------------------- |
        Numeric     | ndarray       | ndarray       | NumpyExtensionArray   |
        Category    | Categorical   | Categorical   | Categorical           |
        dt64[ns]    | ndarray[M8ns] | DatetimeArray | DatetimeArray         |
        dt64[ns tz] | ndarray[M8ns] | DatetimeArray | DatetimeArray         |
        td64[ns]    | ndarray[m8ns] | TimedeltaArray| TimedeltaArray        |
        Period      | ndarray[obj]  | PeriodArray   | PeriodArray           |
        Nullable    | EA            | EA            | EA                    |

        """
        return self._mgr.internal_values()

class TestIndexReductions:  [tests/reductions/test_reductions.py:231]
methods: test_invalid_td64_reductions, test_max_min_range
         test_min_max_categorical
         test_minmax_nat_datetime64, test_minmax_period
         test_minmax_period_empty_nat
         test_minmax_timedelta64
         test_minmax_timedelta_empty_or_na, test_minmax_tz
         test_numpy_minmax_datetime64
         test_numpy_minmax_integer
         test_numpy_minmax_period, test_numpy_minmax_range
         test_numpy_minmax_timedelta64, test_timedelta_ops

class TestSparseArrayAnalytics:  [arrays/sparse/test_array.py:233]
methods: test_asarray_datetime64, test_cumsum, test_density
         test_modf, test_nbytes_block, test_nbytes_integer
         test_npoints, test_ufunc, test_ufunc_args

    def dtype(self) -> DtypeObj:
        return self.values.dtype
```
