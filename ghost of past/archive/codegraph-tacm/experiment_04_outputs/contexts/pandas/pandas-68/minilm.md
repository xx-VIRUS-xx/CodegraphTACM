# pandas-68 :: minilm

query: BUG: Fixed IntervalArray[int].shift (#31502)

## selected nodes

- rank=1 layer=FUNCTION tokens=680 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.from_arrays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=2 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::_new_IntervalIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=3 layer=FUNCTION tokens=677 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex.from_arrays file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=4 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=5 layer=FUNCTION tokens=297 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.closed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=6 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=7 layer=FUNCTION tokens=233 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=8 layer=FUNCTION tokens=405 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.set_closed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=9 layer=FUNCTION tokens=365 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.right file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=10 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IntervalIndexMethod.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=11 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::interval_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py
- rank=12 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py::empty_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py
- rank=13 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._engine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=14 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py::monotonic_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py
- rank=15 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py::data_missing_for_sorting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::_new_IntervalIndex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
def _new_IntervalIndex(cls, d):
    """
    This is called upon unpickling, rather than the default which doesn't have
    arguments and breaks __new__.
    """
    return cls.from_arrays(**d)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex.from_arrays [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
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
        Construct from two arrays defining the left and right bounds.

        Each interval is formed by pairing the corresponding elements of
        *left* and *right*, producing an :class:`IntervalIndex` of the same
        length as the input arrays.

        Parameters
        ----------
        left : array-like (1-dimensional)
            Left bounds for each interval.
        right : array-like (1-dimensional)
            Right bounds for each interval.
        closed : {'left', 'right', 'both', 'neither'}, default 'right'
            Whether the intervals are closed on the left-side, right-side, both
            or neither.
        name : str, optional
            Name of the resulting IntervalIndex.
        copy : bool, default False
            Copy the data.
        dtype : dtype, optional
            If None, dtype will be inferred.

        Returns
        -------
        IntervalIndex

        Raises
        ------
        ValueError
            When a value is missing in only one of `left` or `right`.
            When a value in `left` is greater than the corresponding value
            in `right`.

        See Also
        --------
        interval_range : Function to create a fixed frequency IntervalIndex.
        IntervalIndex.from_breaks : Construct an IntervalIndex from an array of
            splits.
        IntervalIndex.from_tuples : Construct an IntervalIndex from an
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
        >>> pd.IntervalIndex.from_arrays([0, 1, 2], [1, 2, 3])
        IntervalIndex([(0, 1], (1, 2], (2, 3]],
                      dtype='interval[int64, right]')
        """
        with rewrite_exception("IntervalArray", cls.__name__):
            array = IntervalArray.from_arrays(
                left, right, closed, copy=copy, dtype=dtype
            )
        return cls._simple_new(array, name=name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.__getitem__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def __getitem__(self, key: PositionalIndexer) -> Self | IntervalOrNA:
        key = check_array_indexer(self, key)
        left = self._left[key]
        right = self._right[key]

        if not isinstance(left, (np.ndarray, ExtensionArray)):
            # scalar
            if is_scalar(left) and isna(left):
                return self._fill_value
            return Interval(left, right, self.closed)
        if np.ndim(left) > 1:
            # GH#30588 multi-dimensional indexer disallowed
            raise ValueError("multi-dimensional indexing not allowed")
        # Argument 2 to "_simple_new" of "IntervalArray" has incompatible type
        # "Union[Period, Timestamp, Timedelta, NaTType, DatetimeArray, TimedeltaArray,
        # ndarray[Any, Any]]"; expected "Union[Union[DatetimeArray, TimedeltaArray],
        # ndarray[Any, Any]]"
        result = self._simple_new(left, right, dtype=self.dtype)  # type: ignore[arg-type]
        if getitem_returns_view(self, key):
            result._readonly = self._readonly
        return result

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.__array__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def __array__(
        self, dtype: NpDtype | None = None, copy: bool | None = None
    ) -> np.ndarray:
        """
        Return the IntervalArray's data as a numpy array of Interval
        objects (with dtype='object')
        """
        if copy is False:
            raise ValueError(
                "Unable to avoid copy while creating an array as requested."
            )

        left = self._left
        right = self._right
        mask = self.isna()
        closed = self.closed

        result = np.empty(len(left), dtype=object)
        for i, left_value in enumerate(left):
            if mask[i]:
                result[i] = np.nan
            else:
                result[i] = Interval(left_value, right[i], closed)
        return result

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IntervalIndexMethod.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def setup(self, N):
        left = np.append(np.arange(N), np.array(0))
        right = np.append(np.arange(1, N + 1), np.array(1))
        self.intv = IntervalIndex.from_arrays(left, right)
        self.intv._engine

        self.intv2 = IntervalIndex.from_arrays(left + 1, right + 1)
        self.intv2._engine

        self.left = IntervalIndex.from_breaks(np.arange(N))
        self.right = IntervalIndex.from_breaks(np.arange(N - 3, 2 * N - 3))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::interval_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py]
def interval_array(left_right_dtypes):
    """
    Fixture to generate an IntervalArray of various dtypes containing NA if possible
    """
    left, right = left_right_dtypes
    return IntervalArray.from_arrays(left, right)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py::empty_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py]
def empty_index(dtype="int64", closed="right"):
    return IntervalIndex(np.array([], dtype=dtype), closed=closed)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._engine [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
    def _engine(self) -> IntervalTree:  # type: ignore[override]
        # IntervalTree does not supports numpy array unless they are 64 bit
        left = self._maybe_convert_i8(self.left)
        left = maybe_upcast_numeric_to_64bit(left)
        right = self._maybe_convert_i8(self.right)
        right = maybe_upcast_numeric_to_64bit(right)
        return IntervalTree(left, right, closed=self.closed)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py::monotonic_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py]
def monotonic_index(start, end, dtype="int64", closed="right"):
    return IntervalIndex.from_breaks(np.arange(start, end, dtype=dtype), closed=closed)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py::data_missing_for_sorting [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py]
def data_missing_for_sorting():
    return IntervalArray.from_tuples([(1, 2), None, (0, 1)])
```
