# pandas-68 :: tacm

query: BUG: Fixed IntervalArray[int].shift (#31502)

## selected nodes

- rank=1 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py
- rank=2 layer=FILE tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=3 layer=FILE tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py
- rank=4 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/common.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/common.py
- rank=5 layer=FILE tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/astype.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/astype.py
- rank=6 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py::IntervalArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py
- rank=7 layer=CLASS tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py::TestTimedeltaIndexShift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py
- rank=8 layer=CLASS tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py::TestDatetimeIndexShift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
- rank=9 layer=CLASS tokens=478 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_shift.py::TestDataFrameShift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_shift.py
- rank=10 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_shift.py::TestPeriodIndexShift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/methods/test_shift.py
- rank=11 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::PeakMemFixedWindowMinMax file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=12 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/test_to_latex.py::TestToLatexFormatters file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/test_to_latex.py
- rank=13 layer=FUNCTION tokens=264 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=14 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=15 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=16 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=17 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::PeakMemFixedWindowMinMax.peakmem_fixed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=18 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=19 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::diff file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py
- rank=20 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py::IntervalArray.time_from_tuples file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py
- rank=21 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=22 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=23 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=24 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=25 layer=FUNCTION tokens=243 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=26 layer=FUNCTION tokens=281 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=27 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Shift.time_shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=28 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::EABackedBlock.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=29 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=30 layer=FUNCTION tokens=222 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py::shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py
- rank=31 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Timeseries.time_timestamp_ops_diff_with_shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=32 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::Shift.time_defaults file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=33 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.repeat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=34 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py::IntervalArray.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/array.py
- rank=35 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Fixed._complevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=36 layer=FUNCTION tokens=282 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py
- rank=37 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::Shift.time_fill_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=38 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Fixed.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=39 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.__len__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=40 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=41 layer=FUNCTION tokens=169 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=42 layer=FUNCTION tokens=11 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Fixed.shape file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py

## context

```text
file core/array_algos/transforms.py
imports: __future__, typing, numpy, pandas
defines: shift

file core/arrays/interval.py
imports: __future__, operator, typing, warnings, numpy, pandas
defines: IntervalArray, _maybe_convert_platform_interval

file asv_bench/benchmarks/array.py
imports: numpy, pandas, pyarrow
defines: BooleanArray, IntegerArray, IntervalArray, StringArray, ArrowStringArray, ArrowExtensionArray

file core/window/common.py
imports: __future__, collections, typing, numpy, pandas
defines: flex_binary_moment, dataframe_from_int_dict, zsqrt, prep_binary

file core/dtypes/astype.py
imports: __future__, inspect, typing, warnings, numpy, pandas
defines: _astype_nansafe, _astype_nansafe, _astype_nansafe, astype_float_to_int_nansafe, astype_array, astype_array_safe, astype_is_view

class IntervalArray:  [asv_bench/benchmarks/array.py:45]
methods: setup, time_from_tuples

class TestTimedeltaIndexShift:  [timedeltas/methods/test_shift.py:10]
methods: test_shift_no_freq, test_tdi_shift_empty
         test_tdi_shift_hours, test_tdi_shift_int
         test_tdi_shift_minutes
         test_tdi_shift_nonstandard_freq

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

class TestPeriodIndexShift:  [period/methods/test_shift.py:11]
methods: test_pi_shift_ndarray, test_shift, test_shift_corner_cases
         test_shift_gh8083, test_shift_nat
         test_shift_periods

class PeakMemFixedWindowMinMax:  [asv_bench/benchmarks/rolling.py:262]
methods: peakmem_fixed, setup

class TestToLatexFormatters:  [io/formats/test_to_latex.py:931]
methods: test_to_latex_float_format_no_fixed_width_3decimals
         test_to_latex_float_format_no_fixed_width_integer
         test_to_latex_na_rep_and_float_format
         test_to_latex_with_formatters

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

    def shift(
        self,
        periods: int | Sequence[int] = 1,
        freq=None,
        fill_value=lib.no_default,
        suffix: str | None = None,
    ):
        """
    # ... truncated

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

    def peakmem_fixed(self, operation):
        for x in range(5):
            getattr(self.roll, operation)()

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

def shift(values: np.ndarray, periods: int, fill_value: Scalar) -> np.ndarray:
    new_values = values

    if periods == 0 or values.size == 0:
        return new_values.copy()

    # Always shift along the last axis.
    axis = new_values.ndim - 1

    # make sure array sent to np.roll is c_contiguous
    f_ordered = values.flags.f_contiguous
    if f_ordered:
        new_values = new_values.T
        axis = 0

    if new_values.size:
        new_values = np.roll(
            new_values,
            np.intp(periods),
            axis=axis,
        )

    axis_indexer = [slice(None)] * values.ndim
    if periods > 0:
        axis_indexer[axis] = slice(None, periods)
    else:
        axis_indexer[axis] = slice(periods, None)
    new_values[tuple(axis_indexer)] = fill_value

    # restore original order
    if f_ordered:
        new_values = new_values.T

    return new_values

    def time_timestamp_ops_diff_with_shift(self, tz):
        self.s - self.s.shift()

    def time_defaults(self):
        self.df.groupby("g").shift()

    def repeat(
        self,
        repeats: int | Sequence[int],
        axis: AxisInt | None = None,
    ) -> Self:
        """
    # ... truncated

    def setup(self):
        N = 10_000
        self.tuples = [(i, i + 1) for i in range(N)]

    def _complevel(self) -> int:
        return self.parent._complevel

    def shift(self, periods: int = 1, fill_value=None) -> Self:
        """
        Shift values by desired number.

        Newly introduced missing values are filled with
        ``self.dtype.na_value``.

        Parameters
        ----------
        periods : int, default 1
            The number of periods to shift. Negative values are allowed
            for shifting backwards.

        fill_value : object, optional
            The scalar value to use for newly introduced missing values.
            The default is ``self.dtype.na_value``.

        Returns
        -------
        ExtensionArray
            Shifted.

        Notes
        -----
        If ``self`` is empty or ``periods`` is 0, a copy of ``self`` is
        returned.

        If ``periods > len(self)``, then an array of size
        len(self) is returned, with all values filled with
        ``self.dtype.na_value``.
        """
        # NB: shift is always along axis=self.ndim-1
        fill_value = self._validate_scalar(fill_value)
        new_values = shift(self._ndarray, periods, fill_value)

        return self._from_backing_data(new_values)

    def time_fill_value(self):
        self.df.groupby("g").shift(fill_value=99)

    def copy(self) -> Fixed:
        new_self = copy.copy(self)
        return new_self

    def __len__(self) -> int:
        return len(self._left)

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

    def shift(self, periods: int, fill_value: Any = None) -> list[Block]:
        """shift the block by periods, possibly upcast"""
        # convert integer to float if necessary. need to do a lot more than
        # that, handle boolean etc also

        # Note: periods is never 0 here, as that is handled at the top of
        #  NDFrame.shift.  If that ever changes, we can do a check for periods=0
        #  and possibly avoid coercing.

        if not lib.is_scalar(fill_value) and self.dtype != _dtype_obj:
            # with object dtype there is nothing to promote, and the user can
            #  pass pretty much any weird fill_value they like
    # ... truncated

    def shape(self):
        return self.nrows
```
