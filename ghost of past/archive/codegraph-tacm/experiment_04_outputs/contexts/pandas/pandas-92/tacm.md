# pandas-92 :: tacm

query: BUG: PeriodIndex.searchsorted accepting invalid inputs (#30763)

## selected nodes

- rank=1 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=2 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=3 layer=FILE tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=4 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FILE tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py
- rank=6 layer=CLASS tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_searchsorted.py::TestSearchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_searchsorted.py
- rank=7 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_searchsorted.py::TestSearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_searchsorted.py
- rank=8 layer=CLASS tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=9 layer=CLASS tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_searchsorted.py::TestSeriesSearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_searchsorted.py
- rank=10 layer=CLASS tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_timedeltas.py::TestTimedeltaArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_timedeltas.py
- rank=11 layer=CLASS tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/numpy_/test_indexing.py::TestSearchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/numpy_/test_indexing.py
- rank=12 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=13 layer=CLASS tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=14 layer=CLASS tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=15 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_asof.py::TestSeriesAsof file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_asof.py
- rank=16 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=17 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=18 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=19 layer=FUNCTION tokens=311 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.from_ordinals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=20 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::make_invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=21 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.hour file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=22 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.asfreq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=23 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.minute file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=24 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.second file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=25 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.asof_locs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=26 layer=FUNCTION tokens=245 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py
- rank=27 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=28 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._engine_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=29 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::period_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=30 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=31 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=32 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=33 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py::IndexOpsMixin.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py
- rank=34 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._resolution_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=35 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=36 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=37 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=38 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::default_array_ufunc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=39 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py
- rank=40 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.is_full file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=41 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py
- rank=42 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=43 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex.from_fields file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=44 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py
- rank=45 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._disallow_mismatched_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=46 layer=FUNCTION tokens=306 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_monotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=47 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringDtype.type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py

## context

```text
file core/ops/invalid.py
imports: __future__, operator, typing, numpy, collections, pandas
defines: invalid_comparison, make_invalid_op, invalid_op

file core/indexes/period.py
imports: __future__, datetime, typing, numpy, pandas, collections
defines: PeriodIndex, _new_PeriodIndex, period_range

file asv_bench/benchmarks/categoricals.py
imports: string, sys, warnings, numpy, pandas
defines: Constructor, AsType, Concat, ValueCounts, Repr, SetCategories, RemoveCategories, Rank, IsMonotonic, Contains, CategoricalSlicing, Indexing, SearchSorted

file pandas/core/frame.py
imports: __future__, collections, functools, io, itertools, operator, sys, typing
defines: DataFrame, _from_nested_dict, _reindex_for_setitem

file core/interchange/column.py
imports: __future__, typing, numpy, pandas
defines: PandasColumn

class TestSearchsorted:  [indexes/period/test_searchsorted.py:14]
methods: test_searchsorted
         test_searchsorted_different_argument_classes
         test_searchsorted_invalid

class TestSearchSorted:  [indexes/timedeltas/test_searchsorted.py:11]
methods: test_searchsorted_different_argument_classes
         test_searchsorted_invalid_argument_dtype

class SearchSorted:  [asv_bench/benchmarks/categoricals.py:323]
methods: setup, time_categorical_contains
         time_categorical_index_contains

class TestSeriesSearchSorted:  [series/methods/test_searchsorted.py:14]
methods: test_searchsorted, test_searchsorted_dataframe_fail
         test_searchsorted_datetime64_list
         test_searchsorted_datetime64_scalar
         test_searchsorted_datetime64_scalar_mixed_timezones
         test_searchsorted_numeric_dtypes_scalar
         test_searchsorted_numeric_dtypes_vector
         test_searchsorted_sorter

class TestTimedeltaArray:  [tests/arrays/test_timedeltas.py:196]
methods: test_astype_int, test_searchsorted_invalid_types
         test_setitem_clears_freq, test_setitem_objects

class TestSearchsorted:  [arrays/numpy_/test_indexing.py:9]
methods: test_searchsorted_numeric_dtypes_scalar
         test_searchsorted_numeric_dtypes_vector
         test_searchsorted_sorter, test_searchsorted_string

class SearchSorted:  [asv_bench/benchmarks/series_methods.py:122]
methods: setup, time_searchsorted

class PeriodIndex(DatetimeIndexOpsMixin):  [core/indexes/period.py:90]
methods: _cast_partial_indexing_scalar, _convert_tolerance
         _disallow_mismatched_indexing, _engine_type
         _is_comparable_dtype, _maybe_cast_slice_bound
         _maybe_convert_timedelta
         _parsed_string_to_bounds, _resolution_obj, asfreq
         asof_locs, from_fields, from_ordinals, get_loc
         hour, inferred_type, is_full, minute, second
         shift, to_timestamp, values, __new__

class TestDataFrameIndexingWhere:  [frame/indexing/test_where.py:48]
methods: _check_align, _check_get, _check_set, create
         test_df_where_change_dtype
         test_df_where_with_category, test_where_align
         test_where_alignment, test_where_array_like
         test_where_axis, test_where_axis_multiple_dtypes
         test_where_axis_with_upcast, test_where_bug
         test_where_bug_mixed
         test_where_bug_transposition, test_where_callable
         test_where_categorical_filtering
         test_where_complex
         test_where_dataframe_col_match
         test_where_datetime, test_where_datetimelike_noop
         test_where_ea_other
         test_where_empty_df_and_empty_cond_having_non_bool_dtypes
         test_where_get
         test_where_interval_fullop_downcast
         test_where_interval_noop, test_where_invalid
         test_where_invalid_input_multiple
         test_where_invalid_input_single
         test_where_ndframe_align, test_where_none
         test_where_series_slicing, test_where_set
         test_where_tz_values, test_where_upcasting

class TestSeriesAsof:  [series/methods/test_asof.py:20]
methods: test_all_nans, test_asof_nanosecond_index_access
         test_basic, test_errors, test_periodindex
         test_scalar, test_with_nan

    def time_searchsorted(self, dtype):
        key = "2" if dtype == "str" else 2
        self.s.searchsorted(key)

    def time_categorical_contains(self):
        self.c.searchsorted(self.key)

    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

    def from_ordinals(cls, ordinals, *, freq, name=None) -> Self:
        """
        Construct a PeriodIndex from ordinals.

        Ordinals are integer offsets from the proleptic Gregorian epoch,
        interpreted according to the given frequency.

        Parameters
        ----------
        ordinals : array-like of int
            The period offsets from the proleptic Gregorian epoch.
        freq : str or period object
            One of pandas period strings or corresponding objects.
        name : str, default None
            Name of the resulting PeriodIndex.

        Returns
        -------
        PeriodIndex

        See Also
        --------
        PeriodIndex.from_fields : Construct a PeriodIndex from fields
            (year, month, day, etc.).
        PeriodIndex.to_timestamp : Cast to DatetimeArray/Index.

        Examples
        --------
        >>> idx = pd.PeriodIndex.from_ordinals([-1, 0, 1], freq="Q")
        >>> idx
        PeriodIndex(['1969Q4', '1970Q1', '1970Q2'], dtype='period[Q-DEC]')
        """
        ordinals = np.asarray(ordinals, dtype=np.int64)
        dtype = PeriodDtype(freq)
        data = PeriodArray._simple_new(ordinals, dtype=dtype)
        return cls._simple_new(data, name=name)

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

    def hour(self) -> Index:
        """
        The hour of the period.

        Returns the hour component for each period in the index.

        See Also
        --------
        PeriodIndex.minute : The minute of the period.
        PeriodIndex.second : The second of the period.
        PeriodIndex.to_timestamp : Cast to DatetimeArray/Index.

        Examples
        --------
        >>> idx = pd.PeriodIndex(["2023-01-01 10:00", "2023-01-01 11:00"], freq="h")
        >>> idx.hour
        Index([10, 11], dtype='int64')
        """
        return Index(self._data.hour, name=self.name, copy=False)

    def asfreq(self, freq=None, how: str = "E") -> Self:
        """
        Convert the PeriodIndex to the specified frequency `freq`.

        Equivalent to applying :meth:`pandas.Period.asfreq` with the given arguments
        to each :class:`~pandas.Period` in this PeriodIndex.

        Parameters
        ----------
        freq : str
            A frequency.
        how : str {'E', 'S'}, default 'E'
    # ... truncated

    def minute(self) -> Index:
        """
        The minute of the period.

        Returns the minute component for each period in the index.

        See Also
        --------
        PeriodIndex.hour : The hour of the period.
        PeriodIndex.second : The second of the period.
        PeriodIndex.to_timestamp : Cast to DatetimeArray/Index.

        Examples
        --------
        >>> idx = pd.PeriodIndex(
        ...     ["2023-01-01 10:30:00", "2023-01-01 11:50:00"], freq="min"
        ... )
        >>> idx.minute
        Index([30, 50], dtype='int64')
        """
        return Index(self._data.minute, name=self.name, copy=False)

    def second(self) -> Index:
        """
        The second of the period.

        Returns the second component for each period in the index.

        See Also
        --------
        PeriodIndex.hour : The hour of the period.
        PeriodIndex.minute : The minute of the period.
        PeriodIndex.to_timestamp : Cast to DatetimeArray/Index.

        Examples
        --------
        >>> idx = pd.PeriodIndex(
        ...     ["2023-01-01 10:00:30", "2023-01-01 10:00:31"], freq="s"
        ... )
        >>> idx.second
        Index([30, 31], dtype='int64')
        """
        return Index(self._data.second, name=self.name, copy=False)

    def asof_locs(self, where: Index, mask: npt.NDArray[np.bool_]) -> np.ndarray:
        """
        where : array of timestamps
        mask : np.ndarray[bool]
            Array of booleans where data is not NA.
        """
        if isinstance(where, DatetimeIndex):
            where = PeriodIndex(where._values, freq=self.freq, copy=False)
        elif not isinstance(where, PeriodIndex):
            raise TypeError("asof_locs `where` must be DatetimeIndex or PeriodIndex")

        return super().asof_locs(where, mask)

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

    def setup(self, dtype):
        N = 10**5
        data = np.array([1] * N + [2] * N + [3] * N).astype(dtype)
        self.s = Series(data)

    def _engine_type(self) -> type[libindex.PeriodEngine]:
        return libindex.PeriodEngine

def period_range(
    start=None,
    end=None,
    periods: int | None = None,
    freq=None,
    name: Hashable | None = None,
) -> PeriodIndex:
    """
    # ... truncated

    def values(self) -> npt.NDArray[np.object_]:
        return np.asarray(self, dtype=object)

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def setup(self):
        N = 10**5
        self.ci = pd.CategoricalIndex(np.arange(N)).sort_values()
        self.c = self.ci.values
        self.key = self.ci.categories[1]

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def _resolution_obj(self) -> Resolution:
        # for compat with DatetimeIndex
        return self.dtype._resolution_obj

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def searchsorted(
        self,
        v: ArrayLike | object,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        if config["mode"]["performance_warnings"]:
            msg = "searchsorted requires high memory usage."
            warnings.warn(msg, PerformanceWarning, stacklevel=find_stack_level())
        v = np.asarray(v)
        return np.asarray(self, dtype=self.dtype.subtype).searchsorted(v, side, sorter)

def default_array_ufunc(self, ufunc: np.ufunc, method: str, *inputs, **kwargs):
    """
    Fallback to the behavior we would get if we did not define __array_ufunc__.

    Notes
    -----
    We are assuming that `self` is among `inputs`.
    """
    if not any(x is self for x in inputs):
        raise NotImplementedError

    new_inputs = [x if x is not self else np.asarray(x) for x in inputs]

    return getattr(ufunc, method)(*new_inputs, **kwargs)

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def is_full(self) -> bool:
        """
        Returns True if this PeriodIndex is range-like in that all Periods
        between start and end are present, in order.
        """
        if len(self) == 0:
            return True
        if not self.is_monotonic_increasing:
            raise ValueError("Index is not monotonic")
        values = self.asi8
        return bool(((values[1:] - values[:-1]) < 2).all())

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def searchsorted(  # type: ignore[override]
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def from_fields(
        cls,
        *,
        year=None,
        quarter=None,
        month=None,
        day=None,
        hour=None,
        minute=None,
        second=None,
        freq=None,
    ) -> Self:
    # ... truncated

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

    def _disallow_mismatched_indexing(self, key: Period) -> None:
        if key._dtype != self.dtype:
            raise KeyError(key)

    def _get_indexer_monotonic(self, target: Index) -> npt.NDArray[np.intp]:
        """
        Use searchsorted on endpoints for O(n*log(m)) scalar lookups on
        a monotonic non-overlapping IntervalIndex, instead of IntervalTree
        which scales poorly for large target arrays. See GH#47614.
        """
        # Caller is responsible for checking self.is_monotonic_increasing
        closed_right = self.closed in ("right", "both")
        closed_left = self.closed in ("left", "both")

        # searchsorted on right endpoints to find candidate bin
        side: Literal["left", "right"] = "left" if closed_right else "right"
        indexer = self.right.searchsorted(target, side=side)

        nbins = len(self)
        past_end = indexer >= nbins
        indexer = np.minimum(indexer, nbins - 1)

        # Verify values fall within the candidate bin's left bound
        left_values = self.left[indexer]
        if closed_left:
            left_miss = target < left_values
        else:
            left_miss = target <= left_values

        na_mask = isna(target)
        invalid = past_end | left_miss | na_mask
        indexer = np.where(invalid, -1, indexer)
        return ensure_platform_int(indexer)

    def type(self) -> type[str]:
        return str
```
