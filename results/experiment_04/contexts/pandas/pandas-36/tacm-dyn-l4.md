# pandas-36 :: tacm-dyn-l4

query: BUG: isna_old with td64, dt64tz, period (#33158)

## selected nodes

- rank=1 layer=FILE tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py
- rank=2 layer=CLASS tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_missing.py::TestIsNA file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_missing.py
- rank=3 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::TestSetitemNADatetimeLikeDtype.is_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=4 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.any file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=6 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.all file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=7 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=8 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_isna.py::TestIsna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_isna.py
- rank=9 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=10 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::_make_2d_ea_df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py
- rank=11 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._extended_gcd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=12 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=13 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.to_period file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=14 layer=FUNCTION tokens=425 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=15 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=16 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/scope.py::Scope.swapkey file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/scope.py
- rank=17 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_with_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=18 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py::_array_equivalent_object file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py
- rank=19 layer=FUNCTION tokens=169 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::simple_period_range_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py
- rank=20 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_misc.py::_Options.use file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_misc.py
- rank=21 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.isna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=22 layer=CLASS tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_ndarray_backed.py::TestEmpty file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_ndarray_backed.py
- rank=23 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py::_isna_recarray_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py
- rank=24 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py::_f4 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py
- rank=25 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py::EWMMeanState.run_ewm file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py
- rank=26 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py::online_ewma file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py
- rank=27 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/stat_ops.py::Rank.time_average_old file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/stat_ops.py
- rank=28 layer=FUNCTION tokens=10 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/date/array.py::DateDtype.type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/date/array.py

## context

```text
file core/dtypes/missing.py
imports: __future__, decimal, typing, warnings, numpy, pandas, re
defines: isna, isna, isna, isna, isna, isna, _isna, _isna_array, _isna_string_dtype, _isna_recarray_dtype, notna, notna, notna, notna, notna, notna, array_equivalent, _array_equivalent_float, _array_equivalent_datetimelike, _array_equivalent_object, array_equals, infer_fill_value, construct_1d_array_from_inferred_fill_value, maybe_fill, na_value_for_dtype, remove_na_arraylike, is_valid_na_for_dtype, isna_all

class TestIsNA:  [tests/dtypes/test_missing.py:71]
methods: test_0d_array, test_complex, test_datetime_other_units
         test_datetime_other_units_astype, test_decimal
         test_empty_object, test_isna_datetime
         test_isna_isnull, test_isna_isnull_frame
         test_isna_lists, test_isna_nat
         test_isna_numpy_nat, test_isna_old_datetimelike
         test_period, test_timedelta_other_units
         test_timedelta_other_units_dtype

    def is_inplace(self, val, obj):
        # td64   -> cast to object iff val is datetime64("NaT")
        # dt64   -> cast to object iff val is timedelta64("NaT")
        # dt64tz -> cast to object with anything _but_ NaT
        return val is NaT or val is None or val is np.nan or obj.dtype == val.dtype

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

    def any(self, *, axis: AxisInt | None = None, skipna: bool = True) -> bool:
        # GH#34479 the nanops call will raise a TypeError for non-td64 dtype
        return nanops.nanany(self._ndarray, axis=axis, skipna=skipna, mask=self.isna())

    def all(self, *, axis: AxisInt | None = None, skipna: bool = True) -> bool:
        # GH#34479 the nanops call will raise a TypeError for non-td64 dtype

        return nanops.nanall(self._ndarray, axis=axis, skipna=skipna, mask=self.isna())

    def to_period(
        self,
        freq: Frequency | None = None,
        axis: Axis = 0,
        copy: bool | lib.NoDefault = lib.no_default,
    ) -> DataFrame:
        """
    # ... truncated

class TestIsna:  [series/methods/test_isna.py:14]
methods: test_isna, test_isna_period_dtype

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

def _make_2d_ea_df(col_arrays, col_names):
    """
    Construct a DataFrame with a single 2D ExtensionArray block.

    Used for dt64tz and period types which support 2D blocks but don't
    consolidate automatically.
    """
    ea_type = type(col_arrays[0])
    ea_2d = ea_type._simple_new(
        np.stack([arr._ndarray for arr in col_arrays]),
        dtype=col_arrays[0].dtype,
    )
    return DataFrame(ea_2d.T, columns=col_names)

    def _extended_gcd(self, a: int, b: int) -> tuple[int, int, int]:
        """
        Extended Euclidean algorithms to solve Bezout's identity:
           a*x + b*y = gcd(x, y)
        Finds one particular solution for x, y: s, t
        Returns: gcd, s, t
        """
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = b, a
        while r:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        return old_r, old_s, old_t

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

    def to_period(
        self,
        freq: str | None = None,
        copy: bool | lib.NoDefault = lib.no_default,
    ) -> Series:
        """
    # ... truncated

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

def _create_mi_with_dt64tz_level():
    """
    MultiIndex with a level that is a tzaware DatetimeIndex.
    """
    # GH#8367 round trip with pickle
    return MultiIndex.from_product(
        [[1, 2], ["a", "b"], date_range("20130101", periods=3, tz="US/Eastern")],
        names=["one", "two", "three"],
    )

    def swapkey(self, old_key: str, new_key: str, new_value=None) -> None:
        """
        Replace a variable name, with a potentially new value.

        Parameters
        ----------
        old_key : str
            Current variable name to replace
        new_key : str
            New variable name to replace `old_key` with
        new_value : object
            Value to be replaced along with the possible renaming
        """
        if self.has_resolvers:
            maps = self.resolvers.maps + self.scope.maps
        else:
            maps = self.scope.maps

        maps.append(self.temps)

        for mapping in maps:
            if old_key in mapping:
                mapping[new_key] = new_value
                return

def index_with_missing(request):
    """
    Fixture for indices with missing values.

    Integer-dtype and empty cases are excluded because they cannot hold missing
    values.

    MultiIndex is excluded because isna() is not defined for MultiIndex.
    """
    ind = indices_dict[request.param]
    if request.param in ["tuples", "mi-with-dt64tz-level", "multi"]:
        # For setting missing values in the top level of MultiIndex
        vals = ind.tolist()
        vals[0] = (None, *vals[0][1:])
        vals[-1] = (None, *vals[-1][1:])
        return MultiIndex.from_tuples(vals)
    else:
        vals = ind.values.copy()
        vals[0] = None
        vals[-1] = None
        return type(ind)(vals, copy=False)

def _array_equivalent_object(
    left: np.ndarray, right: np.ndarray, strict_nan: bool
) -> bool:
    left = ensure_object(left)
    right = ensure_object(right)

    mask: npt.NDArray[np.bool_] | None = None
    if strict_nan:
        mask = isna(left) & isna(right)
        if not mask.any():
            mask = None

    # ... truncated

def simple_period_range_series():
    """
    Series with period range index and random data for test purposes.
    """

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

    return _simple_period_range_series

    def use(self, key, value) -> Generator[_Options]:
        """
        Temporarily set a parameter value using the with statement.
        Aliasing allowed.
        """
        old_value = self[key]
        try:
            self[key] = value
            yield self
        finally:
            self[key] = old_value

class TestEmpty:  [tests/arrays/test_ndarray_backed.py:19]
methods: test_empty_categorical, test_empty_dt64, test_empty_dt64tz
         test_empty_pandas_array, test_empty_td64

def _f4(old=True, unchanged=True):
    return old, unchanged

# --- Layer 04: Variable context ---
# call-chain context
  called by: time_any [series_methods.py]
  called by: inner [config.py]

# call-chain context
  called by: time_all [series_methods.py]
  called by: assert_attr_equal [asserters.py]

# call-chain context
  called by: setup [gil.py]
  called by: run [gil.py]

# call-chain context
  called by: setup [arithmetic.py]
  called by: setup [array.py]

# call-chain context
  called by: _intersection [range.py]

# call-chain context
  called by: setup [gil.py]
  called by: run [gil.py]

# call-chain context
  called by: update [ops.py]

# call-chain context
  called by: array_equivalent [missing.py]

# call-chain context
  called by: mpl_cleanup [conftest.py]

```
