# pandas-91 :: hybrid-cs

query: BUG: TimedeltaIndex.searchsorted accepting invalid types/dtypes (#30831)

## selected nodes

- rank=1 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py
- rank=2 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=3 layer=FUNCTION tokens=832 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=4 layer=FUNCTION tokens=341 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_delta_bins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=5 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py::NumericEngineIndexing.time_get_loc_near_middle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py
- rank=6 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=7 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py::MaskedNumericEngineIndexing.time_get_loc_near_middle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py
- rank=8 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=9 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.check_int_infer_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=10 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=11 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::timedelta_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=12 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py::construct file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py
- rank=13 layer=FUNCTION tokens=214 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._dtype_to_subclass file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=14 layer=FUNCTION tokens=731 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=15 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.has_invalid_return_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=16 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_validate_td64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py]
    def _test_searchsorted_bool_dtypes(self, data_for_sorting, as_series):
        # We call this from test_searchsorted in cases where we have a
        #  boolean-like dtype. The non-bool test assumes we have more than 2
        #  unique values.
        dtype = data_for_sorting.dtype
        data_for_sorting = pd.array([True, False], dtype=dtype)
        b, a = data_for_sorting
        arr = type(data_for_sorting)._from_sequence([a, b], dtype=dtype)

        if as_series:
            arr = pd.Series(arr)
        assert arr.searchsorted(a) == 0
        assert arr.searchsorted(a, side="right") == 1

        assert arr.searchsorted(b) == 1
        assert arr.searchsorted(b, side="right") == 2

        result = arr.searchsorted(arr.take([0, 1]))
        expected = np.array([0, 1], dtype=np.intp)

        tm.assert_numpy_array_equal(result, expected)

        # sorter
        sorter = np.array([1, 0])
        assert data_for_sorting.searchsorted(a, sorter=sorter) == 0

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py]
    def time_searchsorted(self, dtype):
        key = "2" if dtype == "str" else 2
        self.s.searchsorted(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def searchsorted(  # type: ignore[override]
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
        Find indices where elements should be inserted to maintain order.

        Find the indices into a sorted Series `self` such that, if the
        corresponding elements in `value` were inserted before the indices,
        the order of `self` would be preserved.

        .. note::
            The Series *must* be monotonically sorted, otherwise
            wrong locations will likely be returned. Pandas does *not*
            check this for you.

        Parameters
        ----------
        value : array-like or scalar
            Values to insert into `self`.
        side : {'left', 'right'}, optional
            If 'left', the index of the first suitable location found is given.
            If 'right', return the last such index.  If there is no suitable
            index, return either 0 or N (where N is the length of `self`).
        sorter : 1-D array-like, optional
            Optional array of integer indices that sort `self` into ascending
            order. They are typically the result of ``np.argsort``.

        Returns
        -------
        int or array of int
            A scalar or array of insertion points with the
            same shape as `value`.

        See Also
        --------
        sort_values : Sort by the values along either axis.
        numpy.searchsorted : Similar method from NumPy.

        Notes
        -----
        Binary search is used to find the required insertion points.

        Examples
        --------
        >>> ser = pd.Series([1, 2, 3])
        >>> ser
        0    1
        1    2
        2    3
        dtype: int64
        >>> ser.searchsorted(4)
        np.int64(3)
        >>> ser.searchsorted([0, 4])
        array([0, 3])
        >>> ser.searchsorted([1, 3], side="left")
        array([0, 2])
        >>> ser.searchsorted([1, 3], side="right")
        array([1, 3])
        >>> ser = pd.Series(pd.to_datetime(["3/11/2000", "3/12/2000", "3/13/2000"]))
        >>> ser
        0   2000-03-11
        1   2000-03-12
        2   2000-03-13
        dtype: datetime64[us]
        >>> ser.searchsorted("3/14/2000")
        np.int64(3)
        >>> ser = pd.Categorical(
        ...     ["apple", "bread", "bread", "cheese", "milk"], ordered=True
        ... )
        >>> ser
        ['apple', 'bread', 'bread', 'cheese', 'milk']
        Categories (4, str): ['apple' < 'bread' < 'cheese' < 'milk']
        >>> ser.searchsorted("bread")
        np.int64(1)
        >>> ser.searchsorted(["bread"], side="right")
        array([3])

        If the values are not monotonically sorted, wrong locations
        may be returned:

        >>> ser = pd.Series([2, 1, 3])
        >>> ser
        0    2
        1    1
        2    3
        dtype: int64
        >>> ser.searchsorted(1)  # doctest: +SKIP
        0  # wrong result, correct would be 1
        """
        return base.IndexOpsMixin.searchsorted(self, value, side=side, sorter=sorter)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_delta_bins [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _get_time_delta_bins(self, ax: TimedeltaIndex):
        if not isinstance(ax, TimedeltaIndex):
            raise TypeError(
                "axis must be a TimedeltaIndex, but got "
                f"an instance of {type(ax).__name__}"
            )

        if not isinstance(self.freq, (Tick, Day)):
            # GH#51896
            raise ValueError(
                "Resampling on a TimedeltaIndex requires fixed-duration `freq`, "
                f"e.g. '24h' or '3D', not {self.freq}"
            )

        if not len(ax):
            binner = labels = TimedeltaIndex(data=[], freq=self.freq, name=ax.name)
            return binner, [], labels

        start, end = ax.min(), ax.max()

        if self.closed == "right":
            end += self.freq  # type: ignore[operator]

        labels = binner = timedelta_range(
            start=start, end=end, freq=self.freq, name=ax.name
        )

        end_stamps = labels
        if self.closed == "left":
            end_stamps += self.freq

        bins = ax.searchsorted(end_stamps, side=self.closed)

        if self.offset:
            # GH 10530 & 31809
            labels += self.offset

        return binner, bins, labels

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py::NumericEngineIndexing.time_get_loc_near_middle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py]
    def time_get_loc_near_middle(self, engine_and_dtype, index_type, unique, N):
        # searchsorted performance may be different near the middle of a range
        #  vs near an endpoint
        self.data.get_loc(self.key_middle)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        if not all(isinstance(x, IntervalDtype) for x in dtypes):
            return None

        closed = cast("IntervalDtype", dtypes[0]).closed
        if not all(cast("IntervalDtype", x).closed == closed for x in dtypes):
            return np.dtype(object)

        from pandas.core.dtypes.cast import find_common_type

        common = find_common_type([cast("IntervalDtype", x).subtype for x in dtypes])
        if common == object:
            return np.dtype(object)
        return IntervalDtype(common, closed=closed)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py::MaskedNumericEngineIndexing.time_get_loc_near_middle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing_engines.py]
    def time_get_loc_near_middle(self, engine_and_dtype, index_type, unique, N):
        # searchsorted performance may be different near the middle of a range
        #  vs near an endpoint
        self.data.get_loc(self.key_middle)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        if all(isinstance(t, DatetimeTZDtype) and t.tz == self.tz for t in dtypes):
            np_dtype = np.max(
                [cast("DatetimeTZDtype", t).base for t in [self, *dtypes]]
            )
            unit = np.datetime_data(np_dtype)[0]
            unit = cast("TimeUnit", unit)
            return type(self)(unit=unit, tz=self.tz)
        return super()._get_common_dtype(dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.check_int_infer_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
        def check_int_infer_dtype(dtypes):
            converted_dtypes: list[type] = []
            for dtype in dtypes:
                # Numpy maps int to different types (int32, in64) on Windows and Linux
                # see https://github.com/numpy/numpy/issues/9464
                if (isinstance(dtype, str) and dtype == "int") or (dtype is int):
                    converted_dtypes.append(np.int32)
                    converted_dtypes.append(np.int64)
                elif dtype == "float" or dtype is float:
                    # GH#42452 : np.dtype("float") coerces to np.float64 from Numpy 1.20
                    converted_dtypes.extend([np.float64, np.float32])
                else:
                    converted_dtypes.append(infer_dtype_from_object(dtype))
            return frozenset(converted_dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py]
def types_data_frame(types_data):
    dtypes = {
        "TextCol": "str",
        "DateCol": "str",
        "IntDateCol": "int64",
        "IntDateOnlyCol": "int64",
        "FloatCol": "float",
        "IntCol": "int64",
        "BoolCol": "int64",
        "IntColWithNull": "float",
        "BoolColWithNull": "float",
    }
    df = DataFrame(types_data)
    return df[dtypes.keys()].astype(dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::timedelta_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py]
def timedelta_index():
    """
    A fixture to provide TimedeltaIndex objects with different frequencies.
     Most TimedeltaArray behavior is already tested in TimedeltaIndex tests,
    so here we just test that the TimedeltaArray behavior matches
    the TimedeltaIndex behavior.
    """
    # TODO: flesh this out
    return TimedeltaIndex(["1 Day", "3 Hours", "NaT"])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py::construct [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_indexing.py]
    def construct(dtype):
        if dtype is dtlike_dtypes[-1]:
            # PeriodArray will try to cast ints to strings
            return DatetimeIndex(vals).astype(dtype)
        return Index(vals, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._dtype_to_subclass [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _dtype_to_subclass(cls, dtype: DtypeObj) -> type[Index]:
        # Delay import for perf. https://github.com/pandas-dev/pandas/pull/31423

        if isinstance(dtype, ExtensionDtype):
            return dtype.index_class

        if dtype.kind == "M":
            from pandas import DatetimeIndex

            return DatetimeIndex

        elif dtype.kind == "m":
            from pandas import TimedeltaIndex

            return TimedeltaIndex

        elif dtype.kind == "O":
            # NB: assuming away MultiIndex
            return Index

        elif issubclass(dtype.type, str) or is_numeric_dtype(dtype):
            return Index

        raise NotImplementedError(dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py]
    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
        Find indices where elements should be inserted to maintain order.

        Find the indices into a sorted array `self` (a) such that, if the
        corresponding elements in `value` were inserted before the indices,
        the order of `self` would be preserved.

        Assuming that `self` is sorted:

        ======  ================================
        `side`  returned index `i` satisfies
        ======  ================================
        left    ``self[i-1] < value <= self[i]``
        right   ``self[i-1] <= value < self[i]``
        ======  ================================

        Parameters
        ----------
        value : array-like, list or scalar
            Value(s) to insert into `self`.
        side : {'left', 'right'}, optional
            If 'left', the index of the first suitable location found is given.
            If 'right', return the last such index.  If there is no suitable
            index, return either 0 or N (where N is the length of `self`).
        sorter : 1-D array-like, optional
            Optional array of integer indices that sort array a into ascending
            order. They are typically the result of argsort.

        Returns
        -------
        array of ints or int
            If value is array-like, array of insertion points.
            If value is scalar, a single integer.

        See Also
        --------
        numpy.searchsorted : Similar method from NumPy.

        Examples
        --------
        >>> arr = pd.array([1, 2, 3, 5], dtype="int64[pyarrow]")
        >>> arr.searchsorted([4])
        array([3])
        """
        if self._hasna:
            raise ValueError(
                "searchsorted requires array to be sorted, which is impossible "
                "with NAs present."
            )
        if isinstance(value, ExtensionArray):
            value = value.astype(object)
        # Base class searchsorted would cast to object, which is *much* slower.
        dtype = None
        if isinstance(self.dtype, ArrowDtype):
            pa_dtype = self.dtype.pyarrow_dtype
            if (
                pa.types.is_timestamp(pa_dtype) or pa.types.is_duration(pa_dtype)
            ) and pa_dtype.unit == "ns":
                # np.array[datetime/timedelta].searchsorted(datetime/timedelta)
                # erroneously fails when numpy type resolution is nanoseconds
                dtype = object
        return self.to_numpy(dtype=dtype).searchsorted(value, side=side, sorter=sorter)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.has_invalid_return_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py]
    def has_invalid_return_type(self) -> bool:
        types = self.operand_types
        obj_dtype_set = frozenset([np.dtype("object")])
        return self.return_type == object and types - obj_dtype_set

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_validate_td64_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py]
def _validate_td64_dtype(dtype) -> DtypeObj:
    dtype = pandas_dtype(dtype)
    if dtype == np.dtype("m8"):
        # no precision disallowed GH#24806
        msg = (
            "Passing in 'timedelta' dtype with no precision is not allowed. "
            "Please pass in 'timedelta64[ns]' instead."
        )
        raise ValueError(msg)

    if not lib.is_np_dtype(dtype, "m"):
        raise ValueError(f"dtype '{dtype}' is invalid, should be np.timedelta64 dtype")
    elif not is_supported_dtype(dtype):
        raise ValueError("Supported timedelta64 resolutions are 's', 'ms', 'us', 'ns'")

    return dtype
```
