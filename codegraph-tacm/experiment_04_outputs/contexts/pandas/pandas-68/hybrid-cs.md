# pandas-68 :: hybrid-cs

query: BUG: Fixed IntervalArray[int].shift (#31502)

## selected nodes

- rank=1 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=2 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::interval_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py
- rank=3 layer=FUNCTION tokens=264 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py::shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py
- rank=4 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Shift.time_shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=5 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=6 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=7 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Timeseries.time_timestamp_ops_diff_with_shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=8 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::int_min file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h
- rank=9 layer=FUNCTION tokens=1565 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=10 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.iget file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=11 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Align.time_series_align_int64_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=12 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py::data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py
- rank=13 layer=FUNCTION tokens=361 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=14 layer=FUNCTION tokens=290 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=15 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/interval/test_interval.py::interval file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/interval/test_interval.py
- rank=16 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=17 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::Arithmetic.time_intersect file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py
- rank=18 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::interval_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py]
def interval_array(left_right_dtypes):
    """
    Fixture to generate an IntervalArray of various dtypes containing NA if possible
    """
    left, right = left_right_dtypes
    return IntervalArray.from_arrays(left, right)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py::shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/transforms.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Shift.time_shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_shift(self, axis):
        self.df.shift(1, axis=axis)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def insert(self, loc: int, item: Interval) -> Self:
        """
        Return a new IntervalArray inserting new item at location. Follows
        Python numpy.insert semantics for negative values.  Only Interval
        objects and NA can be inserted into an IntervalIndex

        Parameters
        ----------
        loc : int
        item : Interval

        Returns
        -------
        IntervalArray
        """
        left_insert, right_insert = self._validate_scalar(item)

        new_left = self.left.insert(loc, left_insert)
        new_right = self.right.insert(loc, right_insert)

        return self._shallow_copy(new_left, new_right)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py]
    def shift(self, periods: int = 1, fill_value=None) -> Self:
        # NB: shift is always along axis=self.ndim-1
        if fill_value is None:
            new_data = shift(self._data, periods, 0)
            new_mask = shift(self._mask, periods, True)
        else:
            new_data = shift(self._data, periods, fill_value)
            new_mask = shift(self._mask, periods, False)
        return type(self)(new_data, new_mask)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Timeseries.time_timestamp_ops_diff_with_shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_timestamp_ops_diff_with_shift(self, tz):
        self.s - self.s.shift()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::int_min [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h]
static inline int int_min(int a, int b) { return a < b ? a : b; }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def shift(
        self,
        periods: int | Sequence[int] = 1,
        freq=None,
        axis: Axis = 0,
        fill_value: Hashable = lib.no_default,
        suffix: str | None = None,
    ) -> Self | DataFrame:
        """
        Shift index by desired number of periods with an optional time `freq`.

        When `freq` is not passed, shift the index without realigning the data.
        If `freq` is passed (in this case, the index must be date or datetime,
        or it will raise a `NotImplementedError`), the index will be
        increased using the periods and the `freq`. `freq` can be inferred
        when specified as "infer" as long as either freq or inferred_freq
        attribute is set in the index.

        Parameters
        ----------
        periods : int or Sequence
            Number of periods to shift. Can be positive or negative.
            If an iterable of ints, the data will be shifted once by each int.
            This is equivalent to shifting by one value at a time and
            concatenating all resulting frames. The resulting columns will have
            the shift suffixed to their column names. For multiple periods,
            axis must not be 1.
        freq : DateOffset, tseries.offsets, timedelta, or str, optional
            Offset to use from the tseries module or time rule (e.g. 'EOM').
            If `freq` is specified then the index values are shifted but the
            data is not realigned. That is, use `freq` if you would like to
            extend the index when shifting and preserve the original data.
            If `freq` is specified as "infer" then it will be inferred from
            the freq or inferred_freq attributes of the index. If neither of
            those attributes exist, a ValueError is thrown.
        axis : {0 or 'index', 1 or 'columns', None}, default None
            Shift direction. For `Series` this parameter is unused and defaults to 0.
        fill_value : object, optional
            The scalar value to use for newly introduced missing values.
            the default depends on the dtype of `self`.
            For Boolean and numeric NumPy data types, ``np.nan`` is used.
            For datetime, timedelta, or period data, etc. :attr:`NaT` is used.
            For extension dtypes, ``self.dtype.na_value`` is used.
        suffix : str, optional
            If str and periods is an iterable, this is added after the column
            name and before the shift value for each shifted column name.
            For `Series` this parameter is unused and defaults to `None`.

        Returns
        -------
        Series/DataFrame
            Copy of input object, shifted.

        See Also
        --------
        Index.shift : Shift values of Index.
        DatetimeIndex.shift : Shift values of DatetimeIndex.
        PeriodIndex.shift : Shift values of PeriodIndex.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     [[10, 13, 17], [20, 23, 27], [15, 18, 22], [30, 33, 37], [45, 48, 52]],
        ...     columns=["Col1", "Col2", "Col3"],
        ...     index=pd.date_range("2020-01-01", "2020-01-05"),
        ... )
        >>> df
                    Col1  Col2  Col3
        2020-01-01    10    13    17
        2020-01-02    20    23    27
        2020-01-03    15    18    22
        2020-01-04    30    33    37
        2020-01-05    45    48    52

        >>> df.shift(periods=3)
                    Col1  Col2  Col3
        2020-01-01   NaN   NaN   NaN
        2020-01-02   NaN   NaN   NaN
        2020-01-03   NaN   NaN   NaN
        2020-01-04  10.0  13.0  17.0
        2020-01-05  20.0  23.0  27.0

        >>> df.shift(periods=1, axis="columns")
                    Col1  Col2  Col3
        2020-01-01   NaN    10    13
        2020-01-02   NaN    20    23
        2020-01-03   NaN    15    18
        2020-01-04   NaN    30    33
        2020-01-05   NaN    45    48

        >>> df.shift(periods=3, fill_value=0)
                    Col1  Col2  Col3
        2020-01-01     0     0     0
        2020-01-02     0     0     0
        2020-01-03     0     0     0
        2020-01-04    10    13    17
        2020-01-05    20    23    27

        >>> df.shift(periods=3, freq="D")
                    Col1  Col2  Col3
        2020-01-04    10    13    17
        2020-01-05    20    23    27
        2020-01-06    15    18    22
        2020-01-07    30    33    37
        2020-01-08    45    48    52

        >>> df.shift(periods=3, freq="infer")
                    Col1  Col2  Col3
        2020-01-04    10    13    17
        2020-01-05    20    23    27
        2020-01-06    15    18    22
        2020-01-07    30    33    37
        2020-01-08    45    48    52

        >>> df["Col1"].shift(periods=[0, 1, 2])
                    Col1_0  Col1_1  Col1_2
        2020-01-01      10     NaN     NaN
        2020-01-02      20    10.0     NaN
        2020-01-03      15    20.0    10.0
        2020-01-04      30    15.0    20.0
        2020-01-05      45    30.0    15.0
        """
        axis = self._get_axis_number(axis)

        if freq is not None and fill_value is not lib.no_default:
            # GH#53832
            raise ValueError(
                "Passing a 'freq' together with a 'fill_value' is not allowed."
            )

        if periods == 0:
            return self.copy(deep=False)

        if is_list_like(periods) and isinstance(self, ABCSeries):
            return self.to_frame().shift(
                periods=periods, freq=freq, axis=axis, fill_value=fill_value
            )
        periods = cast("int", periods)

        if freq is None:
            # when freq is None, data is shifted, index is not
            axis = self._get_axis_number(axis)
            assert axis == 0  # axis == 1 cases handled in DataFrame.shift
            new_data = self._mgr.shift(periods=periods, fill_value=fill_value)
            return self._constructor_from_mgr(
                new_data, axes=new_data.axes
            ).__finalize__(self, method="shift")

        return self._shift_with_freq(periods, axis, freq)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.iget [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def iget(self, i: int | tuple[int, int] | tuple[slice, int]) -> np.ndarray:
        # In the case where we have a tuple[slice, int], the slice will always
        #  be slice(None)
        # Note: only reached with self.ndim == 2
        # Invalid index type "Union[int, Tuple[int, int], Tuple[slice, int]]"
        # for "Union[ndarray[Any, Any], ExtensionArray]"; expected type
        # "Union[int, integer[Any]]"
        return self.values[i]  # type: ignore[index]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Align.time_series_align_int64_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_series_align_int64_index(self):
        self.ts1 + self.ts2

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py::data [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py]
def data():
    """Length-10 IntervalArray for semantics test."""
    return IntervalArray(make_data(10))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/interval/test_interval.py::interval [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/interval/test_interval.py]
def interval():
    return Interval(0, 1)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def shift(self, periods: int, fill_value) -> Self:
        if fill_value is lib.no_default:
            fill_value = None

        return self.apply("shift", periods=periods, fill_value=fill_value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::Arithmetic.time_intersect [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py]
    def time_intersect(self, dense_proportion, fill_value):
        self.array1.sp_index.intersect(self.array2.sp_index)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def iat(x):
    return x.iat
```
