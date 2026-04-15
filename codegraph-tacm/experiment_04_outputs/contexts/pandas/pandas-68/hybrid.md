# pandas-68 :: hybrid

query: BUG: Fixed IntervalArray[int].shift (#31502)

## selected nodes

- rank=1 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=2 layer=FUNCTION tokens=680 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.from_arrays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=3 layer=FUNCTION tokens=437 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.from_breaks file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=4 layer=FUNCTION tokens=405 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.set_closed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=5 layer=FUNCTION tokens=328 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py
- rank=6 layer=FUNCTION tokens=365 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.right file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=7 layer=FUNCTION tokens=361 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._shift_with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=8 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::EABackedBlock.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=9 layer=FUNCTION tokens=386 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.left file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=10 layer=FUNCTION tokens=297 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.closed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=11 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=12 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::interval_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py
- rank=13 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.__len__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.from_arrays [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def from_arrays(
        cls,
        left,
        right,
        closed: IntervalClosedType | None = "right",
        copy: bool = False,
        dtype: Dtype | None = None,
    ) -> Self:
        """
        Construct from two arrays defining the left and right bounds.

        This method creates an IntervalArray from two arrays of equal length,
        where the i-th interval spans from left[i] to right[i].

        Parameters
        ----------
        left : array-like (1-dimensional)
            Left bounds for each interval.
        right : array-like (1-dimensional)
            Right bounds for each interval.
        closed : {'left', 'right', 'both', 'neither'}, default 'right'
            Whether the intervals are closed on the left-side, right-side, both
            or neither.
        copy : bool, default False
            Copy the data.
        dtype : dtype, optional
            If None, dtype will be inferred.

        Returns
        -------
        IntervalArray

        Raises
        ------
        ValueError
            When a value is missing in only one of `left` or `right`.
            When a value in `left` is greater than the corresponding value
            in `right`.

        See Also
        --------
        interval_range : Function to create a fixed frequency IntervalIndex.
        IntervalArray.from_breaks : Construct an IntervalArray from an array of
            splits.
        IntervalArray.from_tuples : Construct an IntervalArray from an
            array-like of tuples.

        Notes
        -----
        Each element of `left` must be less than or equal to the `right`
        element at the same position. If an element is missing, it must be
        missing in both `left` and `right`. A TypeError is raised when
        using an unsupported type for `left` or `right`. At the moment,
        'category', 'object', and 'string' subtypes are not supported.

        Examples
        --------
        >>> pd.arrays.IntervalArray.from_arrays([0, 1, 2], [1, 2, 3])
        <IntervalArray>
        [(0, 1], (1, 2], (2, 3]]
        Length: 3, dtype: interval[int64, right]
        """
        left = _maybe_convert_platform_interval(left)
        right = _maybe_convert_platform_interval(right)

        left, right, dtype = cls._ensure_simple_new_inputs(
            left,
            right,
            closed=closed,
            copy=copy,
            dtype=dtype,
        )
        cls._validate(left, right, dtype=dtype)

        return cls._simple_new(left, right, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.from_breaks [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def from_breaks(
        cls,
        breaks,
        closed: IntervalClosedType | None = "right",
        copy: bool = False,
        dtype: Dtype | None = None,
    ) -> Self:
        """
        Construct an IntervalArray from an array of splits.

        This method creates intervals from consecutive pairs of break points,
        where each break point is the right edge of one interval and the left
        edge of the next.

        Parameters
        ----------
        breaks : array-like (1-dimensional)
            Left and right bounds for each interval.
        closed : {'left', 'right', 'both', 'neither'}, default 'right'
            Whether the intervals are closed on the left-side, right-side, both
            or neither.
        copy : bool, default False
            Copy the data.
        dtype : dtype or None, default None
            If None, dtype will be inferred.

        Returns
        -------
        IntervalArray

        See Also
        --------
        interval_range : Function to create a fixed frequency IntervalIndex.
        IntervalArray.from_arrays : Construct from a left and right array.
        IntervalArray.from_tuples : Construct from a sequence of tuples.

        Examples
        --------
        >>> pd.arrays.IntervalArray.from_breaks([0, 1, 2, 3])
        <IntervalArray>
        [(0, 1], (1, 2], (2, 3]]
        Length: 3, dtype: interval[int64, right]
        """

        breaks = _maybe_convert_platform_interval(breaks)

        return cls.from_arrays(breaks[:-1], breaks[1:], closed, copy=copy, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.set_closed [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def set_closed(self, closed: IntervalClosedType) -> Self:
        """
        Return an identical IntervalArray closed on the specified side.

        This method creates a new IntervalArray with the same bounds but with
        a different closure specification.

        Parameters
        ----------
        closed : {'left', 'right', 'both', 'neither'}
            Whether the intervals are closed on the left-side, right-side, both
            or neither.

        Returns
        -------
        IntervalArray
            A new IntervalArray with the specified side closures.

        See Also
        --------
        IntervalArray.closed : Returns inclusive side of the Interval.
        arrays.IntervalArray.closed : Returns inclusive side of the IntervalArray.

        Examples
        --------
        >>> index = pd.arrays.IntervalArray.from_breaks(range(4))
        >>> index
        <IntervalArray>
        [(0, 1], (1, 2], (2, 3]]
        Length: 3, dtype: interval[int64, right]
        >>> index.set_closed("both")
        <IntervalArray>
        [[0, 1], [1, 2], [2, 3]]
        Length: 3, dtype: interval[int64, both]
        """
        if closed not in VALID_CLOSED:
            msg = f"invalid option for 'closed': {closed}"
            raise ValueError(msg)

        left, right = self._left, self._right
        dtype = IntervalDtype(left.dtype, closed=closed)
        return self._simple_new(left, right, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray.shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.right [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def right(self) -> Index:
        """
        Return the right endpoints of each Interval in the IntervalArray as an Index.

        This property extracts the right endpoints from each interval contained within
        the IntervalArray. This can be helpful in use cases where you need to work
        with or compare only the upper bounds of intervals, such as when performing
        range-based filtering, determining interval overlaps, or visualizing the end
        boundaries of data segments.

        See Also
        --------
        arrays.IntervalArray.left : Return the left endpoints of each Interval in
            the IntervalArray as an Index.
        arrays.IntervalArray.mid : Return the midpoint of each Interval in the
            IntervalArray as an Index.
        arrays.IntervalArray.contains : Check elementwise if the Intervals contain
            the value.

        Examples
        --------

        >>> interv_arr = pd.arrays.IntervalArray([pd.Interval(0, 1), pd.Interval(2, 5)])
        >>> interv_arr
        <IntervalArray>
        [(0, 1], (2, 5]]
        Length: 2, dtype: interval[int64, right]
        >>> interv_arr.right
        Index([1, 5], dtype='int64')
        """
        from pandas import Index

        return Index(self._right, copy=False)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::EABackedBlock.shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def shift(self, periods: int, fill_value: Any = None) -> list[Block]:
        """
        Shift the block by `periods`.

        Dispatches to underlying ExtensionArray and re-boxes in an
        ExtensionBlock.
        """
        new_values = self.values.shift(periods=periods, fill_value=fill_value)
        return [self.make_block_same_class(new_values)]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.left [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def left(self) -> Index:
        """
        Return the left endpoints of each Interval in the IntervalArray as an Index.

        This property provides access to the left endpoints of the intervals
        contained within the IntervalArray. This can be useful for analyses where
        the starting point of each interval is of interest, such as in histogram
        creation, data aggregation, or any scenario requiring the identification
        of the beginning of defined ranges. This property returns a ``pandas.Index``
        object containing the midpoint for each interval.

        See Also
        --------
        arrays.IntervalArray.right : Return the right endpoints of each Interval in
            the IntervalArray as an Index.
        arrays.IntervalArray.mid : Return the midpoint of each Interval in the
            IntervalArray as an Index.
        arrays.IntervalArray.contains : Check elementwise if the Intervals contain
            the value.

        Examples
        --------

        >>> interv_arr = pd.arrays.IntervalArray([pd.Interval(0, 1), pd.Interval(2, 5)])
        >>> interv_arr
        <IntervalArray>
        [(0, 1], (2, 5]]
        Length: 2, dtype: interval[int64, right]
        >>> interv_arr.left
        Index([0, 2], dtype='int64')
        """
        from pandas import Index

        return Index(self._left, copy=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.closed [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def closed(self) -> IntervalClosedType:
        """
        String describing the inclusive side the intervals.

        Either ``left``, ``right``, ``both`` or ``neither``.

        See Also
        --------
        IntervalArray.closed : Returns inclusive side of the IntervalArray.
        Interval.closed : Returns inclusive side of the Interval.
        IntervalIndex.closed : Returns inclusive side of the IntervalIndex.

        Examples
        --------

        For arrays:

        >>> interv_arr = pd.arrays.IntervalArray([pd.Interval(0, 1), pd.Interval(1, 5)])
        >>> interv_arr
        <IntervalArray>
        [(0, 1], (1, 5]]
        Length: 2, dtype: interval[int64, right]
        >>> interv_arr.closed
        'right'

        For Interval Index:

        >>> interv_idx = pd.interval_range(start=0, end=2)
        >>> interv_idx
        IntervalIndex([(0, 1], (1, 2]], dtype='interval[int64, right]')
        >>> interv_idx.closed
        'right'
        """
        return self.dtype.closed

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::interval_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py]
def interval_array(left_right_dtypes):
    """
    Fixture to generate an IntervalArray of various dtypes containing NA if possible
    """
    left, right = left_right_dtypes
    return IntervalArray.from_arrays(left, right)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.__len__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py]
    def __len__(self) -> int: ...
```
