# pandas-68 :: tacm-dyn

query: BUG: Fixed IntervalArray[int].shift (#31502)

## selected nodes

- rank=1 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py
- rank=2 layer=CLASS tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py::TestTimedeltaIndexShift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py
- rank=3 layer=FUNCTION tokens=264 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=4 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FILE tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=6 layer=FILE tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py
- rank=7 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py::IntervalArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py
- rank=8 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=9 layer=CLASS tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py::TestDatetimeIndexShift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
- rank=10 layer=CLASS tokens=478 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_shift.py::TestDataFrameShift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_shift.py
- rank=11 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=12 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=13 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::diff file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py
- rank=14 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py::IntervalArray.time_from_tuples file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py
- rank=15 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=16 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=17 layer=CLASS tokens=227 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=18 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.repeat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=19 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.diff file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=20 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=21 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=22 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=23 layer=FUNCTION tokens=243 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=24 layer=FUNCTION tokens=281 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=25 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Shift.time_shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=26 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::EABackedBlock.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=27 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.__len__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=28 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=29 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Timeseries.time_timestamp_ops_diff_with_shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=30 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_shift.py::TestPeriodIndexShift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_shift.py
- rank=31 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::Shift.time_defaults file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=32 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Fixed._complevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=33 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::Shift.time_fill_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=34 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Fixed.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=35 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::PeakMemFixedWindowMinMax file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py

## context

```text
file core/array_algos/transforms.py
imports: __future__, typing, numpy, pandas
defines: shift

class TestTimedeltaIndexShift:  [timedeltas/methods/test_shift.py:10]
methods: test_shift_no_freq, test_tdi_shift_empty
         test_tdi_shift_hours, test_tdi_shift_int
         test_tdi_shift_minutes
         test_tdi_shift_nonstandard_freq

    def shift(self, periods: int = 1, fill_value: object = None) -> IntervalArray:
        if not len(self) or periods == 0:
            return self.copy()

        self._validate_scalar(fill_value)

        # ExtensionArray.shift doesn't work for two reasons
        # 1. IntervalArray.dtype.na_value may not be correct for the dtype.
        # 2. IntervalArray._from_sequence only accepts NaN for missing values,
        #    not other values like NaT

        empty_len = min(abs(periods), len(self))
        if isna(fill_value):
            from pandas import Index

            fill_value = Index(self._left, copy=False)._na_value
            empty = IntervalArray.from_breaks(
                [fill_value] * (empty_len + 1), closed=self.closed
            )
        else:
            empty = self._from_sequence([fill_value] * empty_len, dtype=self.dtype)

        if periods > 0:
            a = empty
            b = self[:-periods]
        else:
            a = self[abs(periods) :]
            b = empty
        return self._concat_same_type([a, b])

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

file core/arrays/interval.py
imports: __future__, operator, typing, warnings, numpy, pandas
defines: IntervalArray, _maybe_convert_platform_interval

file asv_bench/benchmarks/array.py
imports: numpy, pandas, pyarrow
defines: BooleanArray, IntegerArray, IntervalArray, StringArray, ArrowStringArray, ArrowExtensionArray

class IntervalArray:  [asv_bench/benchmarks/array.py:45]
methods: setup, time_from_tuples

    def shift(
        self,
        periods: int | Sequence[int] = 1,
        freq=None,
        fill_value=lib.no_default,
        suffix: str | None = None,
    ):
        """
    # ... truncated

class TestDatetimeIndexShift:  [datetimes/methods/test_shift.py:17]
methods: test_dti_shift_across_dst, test_dti_shift_freqs
         test_dti_shift_int, test_dti_shift_localized
         test_dti_shift_near_midnight
         test_dti_shift_no_freq, test_dti_shift_tzaware
         test_shift_bday, test_shift_bmonth
         test_shift_empty, test_shift_periods

class TestDataFrameShift:  [frame/methods/test_shift.py:19]
methods: get_cat_values, test_datetime_frame_shift_with_freq
         test_datetime_frame_shift_with_freq_error
         test_period_index_frame_shift_with_freq
         test_period_index_frame_shift_with_freq_error
         test_series_shift_interval_preserves_closed
         test_shift, test_shift_2d_dta_block
         test_shift_32bit_take, test_shift_always_copy
         test_shift_axis1_categorical_columns
         test_shift_axis1_many_periods
         test_shift_axis1_multiple_blocks
         test_shift_axis1_multiple_blocks_with_int_fill
         test_shift_axis1_with_valid_fill_value_one_array
         test_shift_axis_one_empty, test_shift_bool
         test_shift_by_offset, test_shift_by_zero
         test_shift_categorical, test_shift_categorical1
         test_shift_categorical_fill_value
         test_shift_disallow_freq_and_fill_value
         test_shift_dst, test_shift_dst_beyond
         test_shift_dt64values_axis1_invalid_fill
         test_shift_dt64values_int_fill_deprecated
         test_shift_dt_index_multiple_periods_unsorted
         test_shift_duplicate_columns, test_shift_empty
         test_shift_fill_value
         test_shift_freq_infer_after_float_to_datetime
         test_shift_int
         test_shift_invalid_fill_value_deprecation
         test_shift_mismatched_freq, test_shift_named_axis
         test_shift_non_writable_array
         test_shift_object_non_scalar_fill
         test_shift_other_axis
         test_shift_other_axis_with_freq
         test_shift_preserve_freqstr
         test_shift_with_iterable_basic_functionality
         test_shift_with_iterable_check_other_arguments
         test_shift_with_iterable_freq_and_fill_value
         test_shift_with_iterable_series
         test_shift_with_offsets_freq
         test_shift_with_offsets_freq_empty
         test_shift_with_periodindex

    def shift(self, periods: int = 1, fill_value: object = None) -> ExtensionArray:
        """
        Shift values by desired number.

        Newly introduced missing values are filled with
        ``self.dtype.na_value``.

        Parameters
        ----------
        periods : int, default 1
            The number of periods to shift. Negative values are allowed
            for shifting backwards.
    # ... truncated

    def shift(
        self,
        periods: int | Sequence[int] = 1,
        freq=None,
        axis: Axis = 0,
        fill_value: Hashable = lib.no_default,
        suffix: str | None = None,
    ) -> Self | DataFrame:
        """
    # ... truncated

def diff(arr, n: int | float | np.integer | np.floating, axis: AxisInt = 0):
    """
    difference of n between self,
    analogous to s-s.shift(n)

    Parameters
    ----------
    arr : ndarray or ExtensionArray
    n : int
        number of periods
    axis : {0, 1}
        axis to shift on
    # ... truncated

    def time_from_tuples(self):
        pd.arrays.IntervalArray.from_tuples(self.tuples)

    def shift(self, periods: int = 1, fill_value=None) -> Self:
        # NB: shift is always along axis=self.ndim-1
        if fill_value is None:
            new_data = shift(self._data, periods, 0)
            new_mask = shift(self._mask, periods, True)
        else:
            new_data = shift(self._data, periods, fill_value)
            new_mask = shift(self._mask, periods, False)
        return type(self)(new_data, new_mask)

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

class IntervalArray(IntervalMixin, ExtensionArray):  [core/arrays/interval.py:122]
methods: _cmp_method, _combined, _concat_same_type
         _ensure_simple_new_inputs, _formatter
         _from_combined, _from_factorized, _from_sequence
         _hash_pandas_object, _putmask, _shallow_copy
         _simple_new, _validate, _validate_listlike
         _validate_scalar, _validate_setitem_value
         argsort, astype, closed, contains, copy, delete
         dtype, equals, fillna, from_arrays, from_breaks
         from_tuples, insert, is_non_overlapping_monotonic
         isin, isna, left, length, max, mid, min, nbytes
         ndim, overlaps, repeat, right, set_closed, shift
         size, take, to_tuples, unique, __array__
         __arrow_array__, __eq__, __ge__, __getitem__
         __getitem__, __getitem__, __gt__, __iter__
         __le__, __len__, __lt__, __ne__, __new__
         __setitem__

    def repeat(
        self,
        repeats: int | Sequence[int],
        axis: AxisInt | None = None,
    ) -> Self:
        """
    # ... truncated

    def diff(self, periods: int = 1, axis: Axis = 0) -> DataFrame:
        """
        First discrete difference of element.

        Calculates the difference of a DataFrame element compared with another
        element in the DataFrame (default is element in previous row).

        Parameters
        ----------
        periods : int, default 1
            Periods to shift for calculating difference, accepts negative
            values.
    # ... truncated

    def shift(self, periods: int = 1, freq=None) -> Self:
        """
        Shift index by desired number of time frequency increments.
        This method is for shifting the values of datetime-like indexes
        by a specified time increment a given number of times.

        Parameters
        ----------
        periods : int, default 1
            Number of periods (or increments) to shift by,
            can be positive or negative.
        freq : pandas.DateOffset, pandas.Timedelta or string, optional
    # ... truncated

    def shift(self, periods: int, fill_value) -> Self:
        if fill_value is lib.no_default:
            fill_value = None

        return self.apply("shift", periods=periods, fill_value=fill_value)

    def shift(self, periods: int = 1, freq: Frequency | None = None) -> Self:
        """
        Shift index by desired number of time frequency increments.

        This method is for shifting the values of datetime-like indexes
        by a specified time increment a given number of times.

        Parameters
        ----------
        periods : int, default 1
            Number of periods (or increments) to shift by,
            can be positive or negative.
    # ... truncated

    def shift(self, periods: int = 1, freq=None) -> Self:
        """
        Shift index by desired number of time frequency increments.

        This method is for shifting the values of datetime-like indexes
        by a specified time increment a given number of times.

        Parameters
        ----------
        periods : int, default 1
            Number of periods (or increments) to shift by,
            can be positive or negative.
        freq : pandas.DateOffset, pandas.Timedelta or string, optional
            Frequency increment to shift by.
            If None, the index is shifted by its own `freq` attribute.
            Offset aliases are valid strings, e.g., 'D', 'W', 'M' etc.

        Returns
        -------
        pandas.DatetimeIndex
            Shifted index.

        See Also
        --------
        Index.shift : Shift values of Index.
        PeriodIndex.shift : Shift values of PeriodIndex.
        """
        raise NotImplementedError

    def shift(self, periods: int = 1, freq=None) -> Self:
        """
        Shift index by desired number of time frequency increments.

        This method is for shifting the values of datetime-like indexes
        by a specified time increment a given number of times.

        Parameters
        ----------
        periods : int, default 1
            Number of periods (or increments) to shift by,
            can be positive or negative.
        freq : pandas.DateOffset, pandas.Timedelta or string, optional
            Frequency increment to shift by.
            If None, the index is shifted by its own `freq` attribute.
            Offset aliases are valid strings, e.g., 'D', 'W', 'M' etc.

        Returns
        -------
        pandas.DatetimeIndex
            Shifted index.

        See Also
        --------
        Index.shift : Shift values of Index.
        PeriodIndex.shift : Shift values of PeriodIndex.
        """
        if freq is not None:
            raise TypeError(
                f"`freq` argument is not supported for {type(self).__name__}.shift"
            )
        return self + periods

    def time_shift(self, axis):
        self.df.shift(1, axis=axis)

    def shift(self, periods: int, fill_value: Any = None) -> list[Block]:
        """
        Shift the block by `periods`.

        Dispatches to underlying ExtensionArray and re-boxes in an
        ExtensionBlock.
        """
        new_values = self.values.shift(periods=periods, fill_value=fill_value)
        return [self.make_block_same_class(new_values)]

    def __len__(self) -> int:
        return len(self._left)

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

    def time_timestamp_ops_diff_with_shift(self, tz):
        self.s - self.s.shift()

class TestPeriodIndexShift:  [period/methods/test_shift.py:11]
methods: test_pi_shift_ndarray, test_shift, test_shift_corner_cases
         test_shift_gh8083, test_shift_nat
         test_shift_periods

    def time_defaults(self):
        self.df.groupby("g").shift()

    def _complevel(self) -> int:
        return self.parent._complevel

    def time_fill_value(self):
        self.df.groupby("g").shift(fill_value=99)

    def copy(self) -> Fixed:
        new_self = copy.copy(self)
        return new_self

class PeakMemFixedWindowMinMax:  [asv_bench/benchmarks/rolling.py:262]
methods: peakmem_fixed, setup
```
