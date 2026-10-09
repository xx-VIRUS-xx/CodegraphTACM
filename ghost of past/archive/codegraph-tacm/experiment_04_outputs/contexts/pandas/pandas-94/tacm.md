# pandas-94 :: tacm

query: BUG: TDI/DTI _shallow_copy creating invalid arrays (#30764)

## selected nodes

- rank=1 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=2 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=3 layer=FILE tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=4 layer=FILE tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=5 layer=CLASS tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexArithmetic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=6 layer=CLASS tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_constructors.py::TestShallowCopy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_constructors.py
- rank=7 layer=CLASS tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py::TestVectorizedTimedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py
- rank=8 layer=CLASS tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py::TestDatetimeIndexComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_datetime64.py
- rank=9 layer=CLASS tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::TestTimedelta64ArithmeticUnsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=10 layer=CLASS tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_tz_convert.py::TestTZConvert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_tz_convert.py
- rank=11 layer=CLASS tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=12 layer=CLASS tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=13 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatelikeOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=14 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=15 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=16 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py::Indexing.time_shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/period.py
- rank=17 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py::TimedeltaIndexing.time_shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py
- rank=18 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py
- rank=19 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py
- rank=20 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=21 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=22 layer=FUNCTION tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=23 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::ensure_arraylike_for_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=24 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::make_invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=25 layer=FUNCTION tokens=300 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::transpose_homogeneous_masked_arrays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=26 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=27 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=28 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::_make_unpacked_invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=29 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=30 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._maybe_cast_slice_bound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=31 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=32 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta_dti file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=33 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::_test_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py
- rank=34 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=35 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::SortedAndUnsortedDatetimeIndexLoc.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=36 layer=FUNCTION tokens=275 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.__from_arrow__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=37 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::DatetimeIndexConstructor.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py
- rank=38 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.from_arrays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=39 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=40 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=41 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex.from_arrays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=42 layer=FUNCTION tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py::ParallelDatetimeFields.time_datetime_field_normalize file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py
- rank=43 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/array_with_attr/array.py::FloatAttrArray.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/array_with_attr/array.py

## context

```text
file core/ops/invalid.py
imports: __future__, operator, typing, numpy, collections, pandas
defines: invalid_comparison, make_invalid_op, invalid_op

file pandas/core/generic.py
imports: __future__, collections, copy, datetime, functools, json, operator, pickle
defines: NDFrame

file core/arrays/datetimelike.py
imports: __future__, datetime, functools, itertools, operator, typing, warnings, numpy
defines: DatetimeLikeArrayMixin, DatelikeOps, TimelikeOps, _make_unpacked_invalid_op, _period_dispatch, new_meth, ensure_arraylike_for_datetimelike, validate_periods, validate_periods, validate_periods, _validate_inferred_freq, dtype_to_unit

file core/arrays/masked.py
imports: __future__, typing, warnings, numpy, pandas
defines: BaseMaskedArray, transpose_homogeneous_masked_arrays

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

class TestShallowCopy:  [indexes/period/test_constructors.py:682]
methods: test_shallow_copy_disallow_i8, test_shallow_copy_empty
         test_shallow_copy_requires_disallow_period_index

class TestVectorizedTimedelta:  [indexes/timedeltas/test_scalar_compat.py:21]
methods: test_components, test_round, test_tdi_round
         test_tdi_round_invalid, test_tdi_total_seconds
         test_tdi_total_seconds_all_nat

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

class TestTZConvert:  [datetimes/methods/test_tz_convert.py:21]
methods: test_dti_tz_convert_compat_timestamp
         test_dti_tz_convert_day_freq_not_preserved
         test_dti_tz_convert_dst
         test_dti_tz_convert_hour_overflow_dst
         test_dti_tz_convert_hour_overflow_dst_timestamps
         test_dti_tz_convert_trans_pos_plus_1__bug
         test_dti_tz_convert_tzlocal
         test_dti_tz_convert_utc_to_local_no_modify
         test_tz_convert_nat, test_tz_convert_roundtrip
         test_tz_convert_unsorted

class TestMaybeCastSliceBound:  [indexes/timedeltas/test_indexing.py:288]
methods: monotonic, tdi, test_maybe_cast_slice_bound_invalid_str
         test_slice_invalid_str_with_timedeltaindex

class TimelikeOps(DatetimeLikeArrayMixin):  [core/arrays/datetimelike.py:1884]
methods: _concat_same_type, _creso, _ensure_matching_resos
         _generate_range, _is_dates_only
         _maybe_clear_freq, _maybe_pin_freq, _round
         _validate_dtype, _validate_frequency
         _values_for_json, _with_freq, all, any, as_unit
         ceil, copy, factorize, floor, freq, freq
         interpolate, round, take, unit, __array_ufunc__

class DatelikeOps(DatetimeLikeArrayMixin):  [core/arrays/datetimelike.py:1826]
methods: strftime

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

def ensure_arraylike_for_datetimelike(
    data, copy: bool, cls_name: str
) -> tuple[ArrayLike, bool]:
    if not hasattr(data, "dtype"):
        # e.g. list, tuple
        if not isinstance(data, (list, tuple)) and np.ndim(data) == 0:
            # i.e. generator
            data = list(data)

        data = construct_1d_object_array_from_listlike(data)
        copy = False
    elif isinstance(data, ABCMultiIndex):
        raise TypeError(f"Cannot create a {cls_name} from a MultiIndex.")
    else:
        data = extract_array(data, extract_numpy=True)

    if isinstance(data, IntegerArray) or (
        isinstance(data, ArrowExtensionArray) and data.dtype.kind in "iu"
    ):
        data = data.to_numpy("int64", na_value=iNaT)
        copy = False
    elif isinstance(data, ArrowExtensionArray):
        data = data._maybe_convert_datelike_array()
        data = data.to_numpy()
        copy = False
    elif not isinstance(data, (np.ndarray, ExtensionArray)):
        # GH#24539 e.g. xarray, dask object
        data = np.asarray(data)

    elif isinstance(data, ABCCategorical):
        # GH#18664 preserve tz in going DTI->Categorical->DTI
        # TODO: cases where we need to do another pass through maybe_convert_dtype,
        #  e.g. the categories are timedelta64s
        data = data.categories.take(data.codes, fill_value=NaT)._values
        copy = False

    return data, copy

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

def transpose_homogeneous_masked_arrays(
    masked_arrays: Sequence[BaseMaskedArray],
) -> list[BaseMaskedArray]:
    """Transpose masked arrays in a list, but faster.

    Input should be a list of 1-dim masked arrays of equal length and all have the
    same dtype. The caller is responsible for ensuring validity of input data.
    """
    masked_arrays = list(masked_arrays)
    dtype = masked_arrays[0].dtype

    values = [arr._data.reshape(1, -1) for arr in masked_arrays]
    transposed_values = np.concatenate(
        values,
        axis=0,
        out=np.empty(
            (len(masked_arrays), len(masked_arrays[0])),
            order="F",
            dtype=dtype.numpy_dtype,
        ),
    )

    masks = [arr._mask.reshape(1, -1) for arr in masked_arrays]
    transposed_masks = np.concatenate(
        masks, axis=0, out=np.empty_like(transposed_values, dtype=bool)
    )

    arr_type = dtype.construct_array_type()
    transposed_arrays: list[BaseMaskedArray] = []
    for i in range(transposed_values.shape[1]):
        transposed_arr = arr_type(transposed_values[:, i], mask=transposed_masks[:, i])
        transposed_arrays.append(transposed_arr)

    return transposed_arrays

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

    def copy(self, order: str = "C") -> Self:
        new_obj = super().copy(order=order)
        new_obj._freq = self.freq
        return new_obj

def _make_unpacked_invalid_op(op_name: str):
    op = make_invalid_op(op_name)
    return unpack_zerodim_and_defer(op_name)(op)

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

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

    def setup(self):
        dti = date_range("2016-01-01", periods=10000, tz="US/Pacific")
        index = np.array(dti)

        unsorted_index = index.copy()
        unsorted_index[10] = unsorted_index[20]

        self.df_unsorted = DataFrame(index=unsorted_index, data={"a": 1})
        self.df_sort = DataFrame(index=index, data={"a": 1})

    def __from_arrow__(self, array: pa.Array | pa.ChunkedArray) -> PeriodArray:
        """
        Construct PeriodArray from pyarrow Array/ChunkedArray.
        """
        import pyarrow

        from pandas.core.arrays import PeriodArray
        from pandas.core.arrays.arrow._arrow_utils import (
            pyarrow_array_to_numpy_and_mask,
        )

        if isinstance(array, pyarrow.Array):
            chunks = [array]
        else:
            chunks = array.chunks

        results = []
        for arr in chunks:
            data, mask = pyarrow_array_to_numpy_and_mask(arr, dtype=np.dtype(np.int64))
            parr = PeriodArray(data.copy(), dtype=self, copy=False)
            # error: Invalid index type "ndarray[Any, dtype[bool_]]" for "PeriodArray";
            # expected type "Union[int, Sequence[int], Sequence[bool], slice]"
            parr[~mask] = NaT  # type: ignore[index]
            results.append(parr)

        if not results:
            return PeriodArray(np.array([], dtype="int64"), dtype=self, copy=False)
        return PeriodArray._concat_same_type(results)

    def setup(self):
        N = 20_000
        dti = date_range("1900-01-01", periods=N)

        self.list_of_timestamps = dti.tolist()
        self.list_of_dates = dti.date.tolist()
        self.list_of_datetimes = dti.to_pydatetime().tolist()
        self.list_of_str = dti.strftime("%Y-%m-%d").tolist()

    def from_arrays(
        cls,
        left,
        right,
        closed: IntervalClosedType | None = "right",
        copy: bool = False,
        dtype: Dtype | None = None,
    ) -> Self:
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

    def from_arrays(
        cls,
        left,
        right,
        closed: IntervalClosedType = "right",
        name: Hashable | None = None,
        copy: bool = False,
        dtype: Dtype | None = None,
    ) -> IntervalIndex:
        """
    # ... truncated

    def time_datetime_field_normalize(self):
        @run_parallel(num_threads=2)
        def run(dti):
            dti.normalize()

        run(self.dti)

    def copy(self):
        return type(self)(self.data.copy(), self.attr)
```
