# pandas-14 :: tacm-dyn-l4

query: BUG: DataFrame[object] + Series[dt64], test parametrization (#33824)

## selected nodes

- rank=1 layer=FILE tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=2 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=3 layer=CLASS tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_astype.py::TestAstype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_astype.py
- rank=4 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py::unpack_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py
- rank=5 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=6 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.items file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=7 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.combine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=8 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=9 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=10 layer=CLASS tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_diff.py::TestSeriesDiff file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_diff.py
- rank=11 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py::skip_if_installed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py
- rank=12 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
- rank=13 layer=CLASS tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/casting.py::BaseCastingTests file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/casting.py
- rank=14 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.time_add_np_dt64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py
- rank=15 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::downsample_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py
- rank=16 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::resample_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py
- rank=17 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=18 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::_check_where_equivalences file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=19 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.join file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=20 layer=FILE tokens=470 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=21 layer=CLASS tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_empty.py::TestEmptyConcat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_empty.py
- rank=22 layer=CLASS tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_comparisons.py::TestTimestampComparison file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
- rank=23 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::box_with_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=24 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.__dataframe__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=25 layer=CLASS tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetime64OverflowHandling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=26 layer=CLASS tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_getitem.py::TestGetitemBooleanMask file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_getitem.py
- rank=27 layer=CLASS tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/constructors.py::BaseConstructorsTests file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/constructors.py
- rank=28 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby._apply_pairwise file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=29 layer=CLASS tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_conversion.py::TestAsArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_conversion.py
- rank=30 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/hashing.py::hash_pandas_object file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/hashing.py
- rank=31 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=32 layer=CLASS tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_is_monotonic.py::TestIsMonotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_is_monotonic.py
- rank=33 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::get_nat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c

## context

```text
file vendored/ujson/python/ujson.c
imports: Python, numpy
defines: modulestate, PyModuleDef, object_is_decimal_type, object_is_dataframe_type, object_is_series_type, object_is_index_type, object_is_nat_type, object_is_na_type, object_is_decimal_type, object_is_dataframe_type, object_is_series_type, object_is_index_type, object_is_nat_type, object_is_na_type, module_traverse, module_clear, module_free, PyInit__ujson

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class TestAstype:  [series/methods/test_astype.py:111]
methods: test_astype, test_astype_bytes
         test_astype_cast_nan_inf_int
         test_astype_cast_object_int
         test_astype_cast_object_int_fail
         test_astype_datetime, test_astype_datetime64tz
         test_astype_dt64_to_str
         test_astype_dt64tz_to_str
         test_astype_ea_to_datetimetzdtype
         test_astype_empty_constructor_equality
         test_astype_float_to_period
         test_astype_float_to_uint_negatives_raise
         test_astype_from_float_to_str
         test_astype_generic_timestamp_no_frequency
         test_astype_ignores_errors_for_extension_dtypes
         test_astype_mixed_object_to_dt64tz
         test_astype_nan_to_bool
         test_astype_no_pandas_dtype
         test_astype_object_to_dt64_non_nano
         test_astype_retain_attrs
         test_astype_str_cast_dt64
         test_astype_str_cast_td64, test_astype_str_map
         test_astype_to_str_preserves_na
         test_astype_unicode
         test_dt64_series_astype_object
         test_td64_series_astype_object

def unpack_obj(obj, klass, axis):
    """
    Helper to ensure we have the right type of object for a test parametrized
    over frame_or_series.
    """
    if klass is not DataFrame:
        obj = obj["A"]
        if axis != 0:
            pytest.skip(f"Test is only for DataFrame with axis={axis}")
    return obj

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

    def items(self) -> Iterable[tuple[Hashable, Series]]:
        r"""
        Iterate over (column name, Series) pairs.

        Iterates over the DataFrame columns, returning a tuple with
        the column name and the content as a Series.

        Yields
        ------
        label : object
            The column names for the DataFrame being iterated over.
        content : Series
    # ... truncated

    def combine(
        self,
        other: DataFrame,
        func: Callable[[Series, Series], Series | Hashable],
        fill_value=None,
        overwrite: bool = True,
    ) -> DataFrame:
        """
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

class TestSeriesDiff:  [series/methods/test_diff.py:12]
methods: test_diff_bool, test_diff_dt64, test_diff_dt64tz
         test_diff_int, test_diff_np
         test_diff_object_dtype
         test_diff_series_requires_integer, test_diff_tz

def skip_if_installed(package: str) -> pytest.MarkDecorator:
    """
    Skip a test if a package is installed.

    Parameters
    ----------
    package : str
        The name of the package.

    Returns
    -------
    pytest.MarkDecorator
        a pytest.mark.skipif to use as either a test decorator or a
        parametrization mark.
    """
    return pytest.mark.skipif(
        bool(import_optional_dependency(package, errors="ignore")),
        reason=f"Skipping because {package} is installed.",
    )

    def ts(self, dt64):
        return Timestamp._from_dt64(dt64)

class BaseCastingTests:  [extension/base/casting.py:11]
methods: as_str, test_astype_empty_dataframe
         test_astype_object_frame
         test_astype_object_series, test_astype_own_type
         test_astype_str, test_astype_string
         test_to_numpy, test_tolist

    def time_add_np_dt64(self, offset):
        offset + self.dt64

def downsample_method(request):
    """Fixture for parametrization of Grouper downsample methods."""
    return request.param

def resample_method(request):
    """Fixture for parametrization of Grouper resample methods."""
    return request.param

def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

def _check_where_equivalences(df, mask, other, expected):
    # similar to tests.series.indexing.test_setitem.SetitemCastingEquivalences
    #  but with DataFrame in mind and less fleshed-out
    res = df.where(mask, other)
    tm.assert_frame_equal(res, expected)

    res = df.mask(~mask, other)
    tm.assert_frame_equal(res, expected)

    # Note: frame.mask(~mask, other, inplace=True) takes some more work bc
    #  Block.putmask does *not* downcast.  The change to 'expected' here
    #  is specific to the cases in test_where_dt64_2d.
    df = df.copy()
    df.mask(~mask, other, inplace=True)
    if not mask.all():
        # with mask.all(), Block.putmask is a no-op, so does not downcast
        expected = expected.copy()
        expected["A"] = expected["A"].astype(object)
    tm.assert_frame_equal(df, expected)

    def join(
        self,
        other: DataFrame | Series | Iterable[DataFrame | Series],
        on: IndexLabel | None = None,
        how: MergeHow = "left",
        lsuffix: str = "",
        rsuffix: str = "",
        sort: bool = False,
        validate: JoinValidate | None = None,
    ) -> DataFrame:
        """
    # ... truncated

file vendored/ujson/python/objToJSON.c
imports: Python, datetime, pandas, numpy
defines: NpyArrContext, __NpyArrContext, PdBlockContext, __PdBlockContext, TypeContext, __TypeContext, PyObjectEncoder, __PyObjectEncoder, get_nat, createTypeContext, get_values, get_sub_attr, get_attr_length, get_long_attr, total_seconds, PyBytesToUTF8, PyUnicodeToUTF8, NpyDateTimeToIsoCallback, NpyTimeDeltaToIsoCallback, PyDateTimeToIsoCallback, PyTimeToJSON, PyDecimalToUTF8Callback, NpyArr_freeItemValue, NpyArr_iterNextNone, NpyArr_iterBegin, NpyArr_iterEnd, NpyArrPassThru_iterBegin, NpyArrPassThru_iterEnd, NpyArr_iterNextItem, NpyArr_iterNext, NpyArr_iterGetValue, NpyArr_iterGetName, PdBlockPassThru_iterEnd, PdBlock_iterNextItem, PdBlock_iterGetName, PdBlock_iterGetName_Transpose, PdBlock_iterNext, PdBlockPassThru_iterBegin, PdBlock_iterBegin, PdBlock_iterEnd, Tuple_iterBegin, Tuple_iterNext, Tuple_iterEnd, Tuple_iterGetValue, Tuple_iterGetName, Set_iterBegin, Set_iterNext, Set_iterEnd, Set_iterGetValue, Set_iterGetName, Dir_iterBegin, Dir_iterEnd, Dir_iterNext, Dir_iterGetValue, Dir_iterGetName, List_iterBegin, List_iterNext, List_iterEnd, List_iterGetValue, List_iterGetName, Index_iterBegin, Index_iterNext, Index_iterEnd, Index_iterGetValue, Index_iterGetName, Series_iterBegin, Series_iterNext, Series_iterEnd, Series_iterGetValue, Series_iterGetName, DataFrame_iterBegin, DataFrame_iterNext, DataFrame_iterEnd, DataFrame_iterGetValue, DataFrame_iterGetName, Dict_iterBegin, Dict_iterNext, Dict_iterEnd, Dict_iterGetValue, Dict_iterGetName, NpyArr_freeLabels, NpyArr_encodeLabels, Object_invokeDefaultHandler, Object_beginTypeContext, Object_endTypeContext, Object_getStringValue, Object_getLongValue, Object_getDoubleValue, Object_getBigNumStringValue, Object_releaseObject, Object_iterBegin, Object_iterNext, Object_iterEnd, Object_iterGetValue, Object_iterGetName, objToJSON

class TestEmptyConcat:  [reshape/concat/test_empty.py:15]
methods: float_result_type, get_result_type, int_result_type
         test_concat_empty_dataframe
         test_concat_empty_dataframe_different_dtypes
         test_concat_empty_dataframe_dtypes
         test_concat_empty_df_object_dtype
         test_concat_empty_series
         test_concat_empty_series_dtype_category_with_array
         test_concat_empty_series_dtypes
         test_concat_empty_series_dtypes_match_roundtrips
         test_concat_empty_series_dtypes_roundtrips
         test_concat_empty_series_dtypes_sparse
         test_concat_empty_series_dtypes_triple
         test_concat_empty_series_timelike
         test_concat_inner_join_empty
         test_concat_to_empty_ea, test_empty_dtype_coerce
         test_handle_empty_objects

class TestTimestampComparison:  [scalar/timestamp/test_comparisons.py:14]
methods: test_cant_compare_tz_naive_w_aware, test_compare_date
         test_compare_invalid, test_compare_non_nano_dt64
         test_compare_zerodim_array, test_comparison
         test_comparison_dt64_ndarray
         test_comparison_dt64_ndarray_tzaware
         test_comparison_object_array
         test_timestamp_compare_oob_dt64
         test_timestamp_compare_scalars
         test_timestamp_compare_with_early_datetime

def box_with_array(request):
    """
    Fixture to test behavior for Index, Series, DataFrame, and pandas Array
    classes
    """
    return request.param

    def __dataframe__(self, nan_as_null: bool = False, allow_copy: bool = True):
        """Construct a new interchange object, potentially changing the parameters."""

class TestDatetime64OverflowHandling:  [tests/arithmetic/test_datetime64.py:1636]
methods: test_datetimeindex_sub_datetimeindex_overflow
         test_datetimeindex_sub_timestamp_overflow
         test_dt64_overflow_masking
         test_dt64_series_arith_overflow

class TestGetitemBooleanMask:  [series/indexing/test_getitem.py:419]
methods: test_getitem_boolean
         test_getitem_boolean_contiguous_preserve_freq
         test_getitem_boolean_corner
         test_getitem_boolean_different_order
         test_getitem_boolean_dt64_copies
         test_getitem_boolean_empty
         test_getitem_boolean_object

    def _apply_pairwise(
        self,
        target: DataFrame | Series,
        other: DataFrame | Series | None,
        pairwise: bool | None,
        func: Callable[[DataFrame | Series, DataFrame | Series], DataFrame | Series],
        numeric_only: bool,
    ) -> DataFrame | Series:
        """
    # ... truncated

class SubclassedFrame(DataFrame):  [series/methods/test_to_frame.py:56]
methods: —

# --- Layer 04: Variable context ---
# call-chain context
  called by: setup [categoricals.py]
  called by: time_items [frame_methods.py]

# call-chain context
  called by: combine_first [frame.py]
  called by: compare_op [test_numeric.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: inner [gil.py]
  called by: setup [csv.py]

# call-chain context
  called by: from_dataframe [from_dataframe.py]

# call-chain context
  called by: cov [ewm.py]
  called by: corr [ewm.py]

```
