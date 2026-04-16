# pandas-9 :: tacm-dyn-l4

query: BUG: CategoricalIndex.__contains__ incorrect NaTs (#33947)

## selected nodes

- rank=1 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=2 layer=CLASS tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=3 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=4 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=5 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/object/test_indexing.py::TestGetIndexerNonUnique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/object/test_indexing.py
- rank=6 layer=CLASS tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/interval/test_contains.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/interval/test_contains.py
- rank=7 layer=CLASS tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_indexing.py
- rank=8 layer=CLASS tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_indexing.py
- rank=9 layer=CLASS tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_indexing.py
- rank=10 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.__contains__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=11 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py
- rank=12 layer=CLASS tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=13 layer=CLASS tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py
- rank=14 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=15 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_indexing.py
- rank=16 layer=FUNCTION tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=17 layer=CLASS tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/timedeltas/test_constructors.py::TestTimedeltaArrayConstructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/timedeltas/test_constructors.py
- rank=18 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py
- rank=19 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=20 layer=CLASS tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py::TestTimedeltaIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py
- rank=21 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_indexing.py
- rank=22 layer=CLASS tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=23 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=24 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_EastAsianTextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=25 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Contains.time_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py
- rank=26 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=27 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.equals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=28 layer=CLASS tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_period_range.py::TestPeriodRangeDisallowedFreqs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_period_range.py
- rank=29 layer=CLASS tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_floats.py::TestFloatIndexers file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_floats.py
- rank=30 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_indexing.py
- rank=31 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=32 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.sort_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=33 layer=CLASS tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py::DictLike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py
- rank=34 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py::DictLike.__contains__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py
- rank=35 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py::TestTimedeltaEngine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py
- rank=36 layer=CLASS tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py::TestDatetimeEngine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py
- rank=37 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Contains.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py
- rank=38 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py::TestCustomDatetimeIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py
- rank=39 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.set_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=40 layer=CLASS tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocListlike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=41 layer=CLASS tokens=249 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py::TestDatetimeIndexSetOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py
- rank=42 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=43 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=44 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=45 layer=CLASS tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_map.py::TestMap file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_map.py
- rank=46 layer=CLASS tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_misc.py::_Options file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_misc.py

## context

```text
file core/indexes/category.py
imports: __future__, typing, numpy, pandas, collections
defines: CategoricalIndex

class CategoricalIndex(NDArrayBackedExtensionIndex):  [core/indexes/category.py:78]
methods: _can_hold_strings, _engine_type, _format_attrs
         _formatter_func, _is_comparable_dtype
         _is_dtype_compat, _maybe_cast_indexer
         _maybe_cast_listlike_indexer
         _should_fallback_to_positional, equals
         inferred_type, map, reindex, __contains__, __new__

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

class TestGetIndexerNonUnique:  [indexes/object/test_indexing.py:76]
methods: test_get_indexer_non_unique_nas
         test_get_indexer_non_unique_np_nats

class TestContains:  [scalar/interval/test_contains.py:10]
methods: test_contains, test_contains_infinite_length
         test_contains_interval, test_contains_mixed_types
         test_contains_zero_length

class TestContains:  [indexes/multi/test_indexing.py:797]
methods: test_contains, test_contains_td64_level
         test_contains_top_level
         test_contains_with_missing_value
         test_contains_with_nat, test_large_mi_contains
         test_multiindex_contains_dropped

class TestContains:  [indexes/categorical/test_indexing.py:336]
methods: test_contains, test_contains_interval, test_contains_list
         test_contains_na_dtype, test_contains_nan

class TestContains:  [tests/indexes/test_indexing.py:93]
methods: test_contains_requires_hashable_raises
         test_contains_with_float_index
         test_index_contains, test_index_not_contains
         test_mixed_index_contains
         test_mixed_index_not_contains

    def __contains__(self, key: Any) -> bool:
        """
        Return a boolean indicating whether the provided key is in the index.

        Parameters
        ----------
        key : label
            The key to check if it is present in the index.

        Returns
        -------
        bool
    # ... truncated

class TestContains:  [arrays/categorical/test_indexing.py:285]
methods: test_contains, test_contains_interval, test_contains_list

class Contains:  [asv_bench/benchmarks/categoricals.py:240]
methods: setup, time_categorical_contains
         time_categorical_index_contains

class TestContains:  [indexes/period/test_indexing.py:745]
methods: test_contains, test_contains_freq_mismatch
         test_contains_nat

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

class TestContains:  [indexes/numeric/test_indexing.py:547]
methods: test_contains_float64_nans, test_contains_float64_not_nans
         test_contains_none

    def setup(self):
        N = 10**5
        self.ci = pd.CategoricalIndex(np.arange(N))
        self.c = self.ci.values
        self.key = self.ci.categories[0]

class TestTimedeltaArrayConstructor:  [arrays/timedeltas/test_constructors.py:7]
methods: test_copy, test_from_sequence_dtype
         test_incorrect_dtype_raises, test_other_type_raises

class Contains(Dtypes):  [asv_bench/benchmarks/strings.py:217]
methods: setup, time_contains

class TestContains:  [indexes/timedeltas/test_indexing.py:337]
methods: test_contains, test_contains_nonunique

class TestTimedeltaIndex:  [indexes/timedeltas/test_setops.py:17]
methods: test_intersection, test_intersection_bug_1708
         test_intersection_equal
         test_intersection_non_monotonic
         test_intersection_zero_length, test_union
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_freq_infer, test_union_sort_false
         test_zero_length_input_index

class TestContains:  [indexes/datetimes/test_indexing.py:506]
methods: test_contains_nonunique, test_dti_contains_with_duplicates

class SearchSorted:  [asv_bench/benchmarks/categoricals.py:323]
methods: setup, time_categorical_contains
         time_categorical_index_contains

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

    def len(self, text: str) -> int:
        """
        Calculate display width considering unicode East Asian Width
        """
        if not isinstance(text, str):
            return len(text)

        return sum(
            self._EAW_MAP.get(east_asian_width(c), self.ambiguous_width) for c in text
        )

    def time_contains(self, dtype, regex):
        self.s.str.contains("A", regex=regex)

    def len(self, text: str) -> int:
        return len(text)

    def equals(self, other: object) -> bool:
        """
        Determine if two CategoricalIndex objects contain the same elements.

        The order and orderedness of elements matters. The categories matter,
        but the order of the categories matters only when ``ordered=True``.

        Parameters
        ----------
        other : object
            The CategoricalIndex object to compare with.

    # ... truncated

class TestPeriodRangeDisallowedFreqs:  [indexes/period/test_period_range.py:202]
methods: test_A_raises_from_time_series, test_constructor_U
         test_incorrect_case_freq_from_time_series_raises
         test_lowercase_freq_from_time_series_deprecated
         test_uppercase_freq_deprecated_from_time_series

class TestFloatIndexers:  [tests/indexing/test_floats.py:28]
methods: check, compare
         test_float_slice_getitem_with_integer_index_raises
         test_floatindex_slicing_bug
         test_floating_index_doc_example
         test_floating_misc
         test_integer_positional_indexing
         test_scalar_float, test_scalar_integer
         test_scalar_integer_contains_float
         test_scalar_non_numeric
         test_scalar_non_numeric_series_fallback
         test_scalar_with_mixed, test_slice_float
         test_slice_integer
         test_slice_integer_frame_getitem
         test_slice_non_numeric

class TestContains:  [indexes/interval/test_indexing.py:742]
methods: test_contains_dunder

    def time_categorical_contains(self):
        self.key in self.c

    def sort_values(
        self,
        by: IndexLabel,
        *,
        axis: Axis = 0,
        ascending: bool | list[bool] | tuple[bool, ...] = True,
        inplace: bool = False,
        kind: SortKind = "quicksort",
        na_position: str = "last",
        ignore_index: bool = False,
        key: ValueKeyFunc | None = None,
    ) -> DataFrame | None:
    # ... truncated

class DictLike:  [tests/dtypes/test_inference.py:365]
methods: keys, __contains__, __getitem__, __init__

            def __contains__(self, key) -> bool:
                return self.d.__contains__(key)

class TestTimedeltaEngine:  [tests/indexes/test_engines.py:56]
methods: test_not_contains_requires_timedelta

class TestDatetimeEngine:  [tests/indexes/test_engines.py:30]
methods: test_not_contains_requires_timestamp

    def setup(self, dtype, regex):
        super().setup(dtype)

class TestCustomDatetimeIndex:  [indexes/datetimes/test_setops.py:678]
methods: test_intersection_bug, test_intersection_dst_transition
         test_union

    def set_index(
        self,
        keys,
        *,
        drop: bool = True,
        append: bool = False,
        inplace: bool = False,
        verify_integrity: bool | lib.NoDefault = lib.no_default,
    ) -> DataFrame | None:
        """
    # ... truncated

class TestLocListlike:  [tests/indexing/test_loc.py:2896]
methods: test_loc_getitem_list_of_labels_categoricalindex_with_na
         test_loc_getitem_listlike_of_datetimelike_keys
         test_loc_getitem_series_label_list_missing_integer_values
         test_loc_getitem_series_label_list_missing_values
         test_loc_named_index

class TestDatetimeIndexSetOps:  [indexes/datetimes/test_setops.py:33]
methods: test_datetimeindex_diff, test_difference
         test_difference_freq, test_dti_intersection
         test_dti_setop_aware, test_dti_union_mixed
         test_intersection, test_intersection2
         test_intersection_bug_1708
         test_intersection_empty
         test_intersection_non_tick_no_fastpath
         test_intersection_same_timezone_different_units
         test_setops_preserve_freq
         test_symmetric_difference_same_timezone_different_units
         test_union, test_union2, test_union3
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_dataframe_index
         test_union_different_dates_same_timezone_different_units
         test_union_freq_both_none, test_union_freq_infer
         test_union_same_nonzero_timezone_different_units
         test_union_same_timezone_different_units
         test_union_with_DatetimeIndex

def contains(cat, key, container) -> bool:
    """
    Helper for membership check for ``key`` in ``cat``.

    This is a helper method for :meth:`__contains__`
    and :class:`CategoricalIndex.__contains__`.

    Returns True if ``key`` is in ``cat.categories`` and the
    location of ``key`` in ``categories`` is in ``container``.

    Parameters
    ----------
    # ... truncated

class TestMap:  [datetimes/methods/test_map.py:13]
methods: test_index_map, test_map, test_map_bug_1677
         test_map_fallthrough

class TestBetweenTime:  [frame/methods/test_between_time.py:20]
methods: test_between_time, test_between_time_axis
         test_between_time_axis_aliases
         test_between_time_axis_raises
         test_between_time_datetimeindex
         test_between_time_formats
         test_between_time_incorrect_arg_inclusive
         test_between_time_raises, test_between_time_types
         test_localized_between_time

class _Options(dict):  [pandas/plotting/_misc.py:697]
methods: _get_canonical_key, reset, use, __contains__, __delitem__
         __getitem__, __init__, __setitem__

    def __contains__(self, key) -> bool:
        key = self._get_canonical_key(key)
        return super().__contains__(key)

class TestHashTableWithNans:  [tests/libs/test_hashtable.py:544]
methods: test_get_set_contains_len, test_map_locations, test_unique

class SequenceNotStr(Protocol[_T_co]):  [pandas/pandas/_typing.py:110]
methods: count, index, __contains__, __getitem__, __getitem__
         __iter__, __len__, __reversed__

    def __contains__(self, value: object, /) -> bool: ...

    def time_categorical_contains(self):
        self.c.searchsorted(self.key)

# --- Layer 04: Variable context ---
# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: setup [algorithms.py]
  called by: setup [algorithms.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: time_frame_float_equal [frame_methods.py]
  called by: time_frame_float_unequal [frame_methods.py]

# call-chain context
  called by: time_sort_values [categoricals.py]
  called by: setup [categoricals.py]

# call-chain context
  called by: setup [frame_methods.py]
  called by: setup [groupby.py]

# call-chain context
  called by: time_contains [strings.py]
  called by: __contains__ [categorical.py]

```
