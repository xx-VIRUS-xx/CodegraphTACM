# pandas-97 :: codesearch

query: BUG: TimedeltaIndex.union with sort=False (#30701)

## selected nodes

- rank=1 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py::TimedeltaIndexing.time_union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py
- rank=2 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::timedelta_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=3 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::SortIndex.time_sort_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=4 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestTimedeltaIndexEquals.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
- rank=5 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::SortMultiKey.time_sort_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=6 layer=FUNCTION tokens=1246 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.sort_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=7 layer=FUNCTION tokens=480 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.sort_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=8 layer=FUNCTION tokens=1078 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.sort_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=9 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timedelta/test_timedelta.py::TestNonNano.td file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
- rank=10 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::SetOperations.time_operation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=11 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=12 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::ArithmeticBlock.time_make_union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py
- rank=13 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::Arithmetic.time_make_union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py
- rank=14 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeIndex.time_add_timedelta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=15 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Sortlevel.time_sortlevel_one file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py::TimedeltaIndexing.time_union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timedelta.py]
    def time_union(self):
        self.index.union(self.index2)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::SortIndex.time_sort_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_sort_index(self, monotonic):
        self.s.sort_index()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py::TestTimedeltaIndexEquals.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_equals.py]
    def index(self):
        """Fixture for creating a TimedeltaIndex for use in equality tests."""
        return timedelta_range("1 day", periods=10)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::SortMultiKey.time_sort_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_sort_index(self, monotonic):
        self.df_by_index.sort_index()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.sort_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def sort_index(
        self,
        *,
        axis: Axis = 0,
        level: IndexLabel | None = None,
        ascending: bool | Sequence[bool] = True,
        inplace: bool = False,
        kind: SortKind = "quicksort",
        na_position: NaPosition = "last",
        sort_remaining: bool = True,
        ignore_index: bool = False,
        key: IndexKeyFunc | None = None,
    ) -> Series | None:
        """
        Sort Series by index labels.

        Returns a new Series sorted by label if `inplace` argument is
        ``False``, otherwise updates the original series and returns None.

        Parameters
        ----------
        axis : {0 or 'index'}
            Unused. Parameter needed for compatibility with DataFrame.
        level : int, optional
            If not None, sort on values in specified index level(s).
        ascending : bool or list-like of bools, default True
            Sort ascending vs. descending. When the index is a MultiIndex the
            sort direction can be controlled for each level individually.
        inplace : bool, default False
            If True, perform operation in-place.
        kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, default 'quicksort'
            Choice of sorting algorithm. See also :func:`numpy.sort` for more
            information. 'mergesort' and 'stable' are the only stable algorithms. For
            DataFrames, this option is only applied when sorting on a single
            column or label.
        na_position : {'first', 'last'}, default 'last'
            If 'first' puts NaNs at the beginning, 'last' puts NaNs at the end.
            Not implemented for MultiIndex.
        sort_remaining : bool, default True
            If True and sorting by level and index is multilevel, sort by other
            levels too (in order) after sorting by specified level.
        ignore_index : bool, default False
            If True, the resulting axis will be labeled 0, 1, …, n - 1.
        key : callable, optional
            If not None, apply the key function to the index values
            before sorting. This is similar to the `key` argument in the
            builtin :meth:`sorted` function, with the notable difference that
            this `key` function should be *vectorized*. It should expect an
            ``Index`` and return an ``Index`` of the same shape.

        Returns
        -------
        Series or None
            The original Series sorted by the labels or None if ``inplace=True``.

        See Also
        --------
        DataFrame.sort_index: Sort DataFrame by the index.
        DataFrame.sort_values: Sort DataFrame by the value.
        Series.sort_values : Sort Series by the value.

        Examples
        --------
        >>> s = pd.Series(["a", "b", "c", "d"], index=[3, 2, 1, 4])
        >>> s.sort_index()
        1    c
        2    b
        3    a
        4    d
        dtype: str

        Sort Descending

        >>> s.sort_index(ascending=False)
        4    d
        3    a
        2    b
        1    c
        dtype: str

        By default NaNs are put at the end, but use `na_position` to place
        them at the beginning

        >>> s = pd.Series(["a", "b", "c", "d"], index=[3, 2, 1, np.nan])
        >>> s.sort_index(na_position="first")
        NaN     d
         1.0    c
         2.0    b
         3.0    a
        dtype: str

        Specify index level to sort

        >>> arrays = [
        ...     np.array(["qux", "qux", "foo", "foo", "baz", "baz", "bar", "bar"]),
        ...     np.array(["two", "one", "two", "one", "two", "one", "two", "one"]),
        ... ]
        >>> s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=arrays)
        >>> s.sort_index(level=1)
        bar  one    8
        baz  one    6
        foo  one    4
        qux  one    2
        bar  two    7
        baz  two    5
        foo  two    3
        qux  two    1
        dtype: int64

        Does not sort by remaining levels when sorting by levels

        >>> s.sort_index(level=1, sort_remaining=False)
        qux  one    2
        foo  one    4
        baz  one    6
        bar  one    8
        qux  two    1
        foo  two    3
        baz  two    5
        bar  two    7
        dtype: int64

        Apply a key function before sorting

        >>> s = pd.Series([1, 2, 3, 4], index=["A", "b", "C", "d"])
        >>> s.sort_index(key=lambda x: x.str.lower())
        A    1
        b    2
        C    3
        d    4
        dtype: int64
        """

        return super().sort_index(
            axis=axis,
            level=level,
            ascending=ascending,
            inplace=inplace,
            kind=kind,
            na_position=na_position,
            sort_remaining=sort_remaining,
            ignore_index=ignore_index,
            key=key,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.sort_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def sort_index(
        self,
        *,
        axis: Axis = 0,
        level: IndexLabel | None = None,
        ascending: bool | Sequence[bool] = True,
        inplace: bool = False,
        kind: SortKind = "quicksort",
        na_position: NaPosition = "last",
        sort_remaining: bool = True,
        ignore_index: bool = False,
        key: IndexKeyFunc | None = None,
    ) -> Self | None:
        inplace = validate_bool_kwarg(inplace, "inplace")
        axis = self._get_axis_number(axis)
        ascending = validate_ascending(ascending)

        target = self._get_axis(axis)

        indexer = get_indexer_indexer(
            target, level, ascending, kind, na_position, sort_remaining, key
        )

        if indexer is None:
            if inplace:
                result = self
            else:
                result = self.copy(deep=False)

            if ignore_index:
                if axis == 1:
                    result.columns = default_index(len(self.columns))
                else:
                    result.index = default_index(len(self))
            if inplace:
                return None
            else:
                return result

        baxis = self._get_block_manager_axis(axis)
        new_data = self._mgr.take(indexer, axis=baxis, verify=False)

        # reconstruct axis if needed
        if not ignore_index:
            new_axis = new_data.axes[baxis]._sort_levels_monotonic()
        else:
            new_axis = default_index(len(indexer))
        new_data.set_axis(baxis, new_axis)

        result = self._constructor_from_mgr(new_data, axes=new_data.axes)

        if inplace:
            return self._update_inplace(result)
        else:
            return result.__finalize__(self, method="sort_index")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.sort_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def sort_index(
        self,
        *,
        axis: Axis = 0,
        level: IndexLabel | None = None,
        ascending: bool | Sequence[bool] = True,
        inplace: bool = False,
        kind: SortKind = "quicksort",
        na_position: NaPosition = "last",
        sort_remaining: bool = True,
        ignore_index: bool = False,
        key: IndexKeyFunc | None = None,
    ) -> DataFrame | None:
        """
        Sort object by labels (along an axis).

        Returns a new DataFrame sorted by label if `inplace` argument is
        ``False``, otherwise updates the original DataFrame and returns None.

        Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns'}, default 0
            The axis along which to sort.  The value 0 identifies the rows,
            and 1 identifies the columns.
        level : int or level name or list of ints or list of level names
            If not None, sort on values in specified index level(s).
        ascending : bool or list-like of bools, default True
            Sort ascending vs. descending. When the index is a MultiIndex the
            sort direction can be controlled for each level individually.
        inplace : bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, default 'quicksort'
            Choice of sorting algorithm. See also :func:`numpy.sort` for more
            information. `mergesort` and `stable` are the only stable algorithms. For
            DataFrames, this option is only applied when sorting on a single
            column or label.
        na_position : {'first', 'last'}, default 'last'
            Puts NaNs at the beginning if `first`; `last` puts NaNs at the end.
            Not implemented for MultiIndex.
        sort_remaining : bool, default True
            If True and sorting by level and index is multilevel, sort by other
            levels too (in order) after sorting by specified level.
        ignore_index : bool, default False
            If True, the resulting axis will be labeled 0, 1, …, n - 1.
        key : callable, optional
            If not None, apply the key function to the index values
            before sorting. This is similar to the `key` argument in the
            builtin :meth:`sorted` function, with the notable difference that
            this `key` function should be *vectorized*. It should expect an
            ``Index`` and return an ``Index`` of the same shape. For MultiIndex
            inputs, the key is applied *per level*.

        Returns
        -------
        DataFrame or None
            The original DataFrame sorted by the labels or None if ``inplace=True``.

        See Also
        --------
        Series.sort_index : Sort Series by the index.
        DataFrame.sort_values : Sort DataFrame by the value.
        Series.sort_values : Sort Series by the value.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     [1, 2, 3, 4, 5], index=[100, 29, 234, 1, 150], columns=["A"]
        ... )
        >>> df.sort_index()
             A
        1    4
        29   2
        100  1
        150  5
        234  3

        By default, it sorts in ascending order, to sort in descending order,
        use ``ascending=False``

        >>> df.sort_index(ascending=False)
             A
        234  3
        150  5
        100  1
        29   2
        1    4

        A key function can be specified which is applied to the index before
        sorting. For a ``MultiIndex`` this is applied to each level separately.

        >>> df = pd.DataFrame({"a": [1, 2, 3, 4]}, index=["A", "b", "C", "d"])
        >>> df.sort_index(key=lambda x: x.str.lower())
           a
        A  1
        b  2
        C  3
        d  4
        """
        return super().sort_index(
            axis=axis,
            level=level,
            ascending=ascending,
            inplace=inplace,
            kind=kind,
            na_position=na_position,
            sort_remaining=sort_remaining,
            ignore_index=ignore_index,
            key=key,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timedelta/test_timedelta.py::TestNonNano.td [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timedelta/test_timedelta.py]
    def td(self, unit, val):
        return Timedelta._from_value_and_reso(val, unit)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::SetOperations.time_operation [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py]
    def time_operation(self, index_structure, dtype, method, sort):
        getattr(self.left, method)(self.right, sort=sort)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _intersection(self, other: Index, sort: bool = False) -> Index:
        """
        intersection specialized to the case with matching dtypes and both non-empty.
        """
        other = cast("DatetimeTimedeltaMixin", other)

        if self._can_range_setop(other):
            return self._range_intersect(other, sort=sort)

        if not self._can_fast_intersect(other):
            result = Index._intersection(self, other, sort=sort)
            # We need to invalidate the freq because Index._intersection
            #  uses _shallow_copy on a view of self._data, which will preserve
            #  self.freq if we're not careful.
            # At this point we should have result.dtype == self.dtype
            #  and type(result) is type(self._data)
            result = self._wrap_setop_result(other, result)
            # error: "Index" has no attribute "_with_freq"; maybe "_with_infer"?
            return result._with_freq(None)._with_freq("infer")  # type: ignore[attr-defined]

        else:
            return self._fast_intersect(other, sort)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::ArithmeticBlock.time_make_union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py]
    def time_make_union(self, fill_value):
        self.arr1.sp_index.make_union(self.arr2.sp_index)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::Arithmetic.time_make_union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py]
    def time_make_union(self, dense_proportion, fill_value):
        self.array1.sp_index.make_union(self.array2.sp_index)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::DatetimeIndex.time_add_timedelta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_add_timedelta(self, index_type):
        self.index + timedelta(minutes=2)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Sortlevel.time_sortlevel_one [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py]
    def time_sortlevel_one(self):
        self.mi.sortlevel(1)
```
