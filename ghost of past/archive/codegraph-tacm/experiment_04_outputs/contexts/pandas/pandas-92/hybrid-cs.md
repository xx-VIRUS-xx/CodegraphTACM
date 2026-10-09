# pandas-92 :: hybrid-cs

query: BUG: PeriodIndex.searchsorted accepting invalid inputs (#30763)

## selected nodes

- rank=1 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=2 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py
- rank=3 layer=FUNCTION tokens=832 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=4 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=5 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py
- rank=6 layer=FUNCTION tokens=958 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py::IndexOpsMixin.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py
- rank=7 layer=FUNCTION tokens=795 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_period_bins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=8 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=9 layer=FUNCTION tokens=606 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py]
    def time_searchsorted(self, dtype):
        key = "2" if dtype == "str" else 2
        self.s.searchsorted(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py]
    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        # Parent's searchsorted calls _validate_setitem_value, which is
        # too strict for search (e.g. rejects float into int). Delegate
        # directly to numpy which handles cross-dtype searches correctly.
        return self._ndarray.searchsorted(value, side=side, sorter=sorter)  # type: ignore[arg-type]

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        npvalue = self._validate_setitem_value(value).view("M8[ns]")

        # Cast to M8 to get datetime-like NaT placement,
        #  similar to dtl._period_dispatch
        m8arr = self._ndarray.view("M8[ns]")
        return m8arr.searchsorted(npvalue, side=side, sorter=sorter)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py::IndexOpsMixin.searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py]
    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
        Find indices where elements should be inserted to maintain order.

        Find the indices into a sorted Index `self` such that, if the
        corresponding elements in `value` were inserted before the indices,
        the order of `self` would be preserved.

        .. note::

            The Index *must* be monotonically sorted, otherwise
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
        if isinstance(value, ABCDataFrame):
            msg = (
                "Value must be 1-D array-like or scalar, "
                f"{type(value).__name__} is not supported"
            )
            raise ValueError(msg)

        values = self._values
        if not isinstance(values, np.ndarray):
            # Going through EA.searchsorted directly improves performance GH#38083
            return values.searchsorted(value, side=side, sorter=sorter)

        return algorithms.searchsorted(
            values,
            value,
            side=side,
            sorter=sorter,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_period_bins [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _get_period_bins(self, ax: PeriodIndex):
        if not isinstance(ax, PeriodIndex):
            raise TypeError(
                "axis must be a PeriodIndex, but got "
                f"an instance of {type(ax).__name__}"
            )

        memb = ax.asfreq(self.freq, how=self.convention)

        # NaT handling as in pandas._lib.lib.generate_bins_dt64()
        nat_count = 0
        if memb.hasnans:
            # error: Incompatible types in assignment (expression has type
            # "bool_", variable has type "int")  [assignment]
            nat_count = np.sum(memb._isnan)  # type: ignore[assignment]
            memb = memb[~memb._isnan]

        if not len(memb):
            # index contains no valid (non-NaT) values
            bins = np.array([], dtype=np.int64)
            binner = labels = PeriodIndex(data=[], freq=self.freq, name=ax.name)
            if len(ax) > 0:
                # index is all NaT
                binner, bins, labels = _insert_nat_bin(binner, bins, labels, len(ax))
            return binner, bins, labels

        freq_mult = self.freq.n

        start = ax.min().asfreq(self.freq, how=self.convention)  # type: ignore[attr-defined]
        end = ax.max().asfreq(self.freq, how="end")  # type: ignore[attr-defined]
        bin_shift = 0

        if isinstance(self.freq, Tick):
            # GH 23882 & 31809: get adjusted bin edge labels with 'origin'
            # and 'origin' support. This call only makes sense if the freq is a
            # Tick since offset and origin are only used in those cases.
            # Not doing this check could create an extra empty bin.
            p_start, end = _get_period_range_edges(
                start,
                end,
                self.freq,
                closed=self.closed,
                origin=self.origin,
                offset=self.offset,
            )

            # Get offset for bin edge (not label edge) adjustment
            start_offset = Period(start, self.freq) - Period(p_start, self.freq)
            # error: Item "Period" of "Union[Period, Any]" has no attribute "n"
            bin_shift = start_offset.n % freq_mult  # type: ignore[union-attr]
            start = p_start

        labels = binner = period_range(
            start=start, end=end, freq=self.freq, name=ax.name
        )

        i8 = memb.asi8

        # when upsampling to subperiods, we need to generate enough bins
        expected_bins_count = len(binner) * freq_mult
        i8_extend = expected_bins_count - (i8[-1] - i8[0])
        rng = np.arange(i8[0], i8[-1] + i8_extend, freq_mult)
        rng += freq_mult
        # adjust bin edge indexes to account for base
        rng -= bin_shift

        # Wrap in PeriodArray for PeriodArray.searchsorted
        prng = type(memb._data)(rng, dtype=memb.dtype)
        bins = memb.searchsorted(prng, side="left")

        if nat_count > 0:
            binner, bins, labels = _insert_nat_bin(binner, bins, labels, nat_count)

        return binner, bins, labels

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py]
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
        >>> arr = pd.array([1, 2, 3, 5])
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
        return self._data.searchsorted(value, side=side, sorter=sorter)
```
