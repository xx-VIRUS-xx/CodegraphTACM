# pandas-55 :: hybrid

query: BUG: Fix incorrect _is_scalar_access check in iloc (#32085)

## selected nodes

- rank=1 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=2 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=3 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=4 layer=FUNCTION tokens=275 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=5 layer=FUNCTION tokens=1104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.iloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=6 layer=FUNCTION tokens=357 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.iat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=7 layer=FUNCTION tokens=393 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._setitem_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=8 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::assert_indexing_slices_equivalent file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py
- rank=9 layer=FUNCTION tokens=223 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_AtIndexer.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=10 layer=FUNCTION tokens=590 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._maybe_mask_setitem_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=11 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py
- rank=12 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::iloc_getitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=13 layer=FUNCTION tokens=360 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._has_valid_setitem_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=14 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::iloc_constructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._is_scalar_access [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _is_scalar_access(self, key: tuple) -> bool:
        """
        Returns
        -------
        bool
        """
        # this is a shortcut accessor to both .loc and .iloc
        # that provide the equivalent access of .at and .iat
        # a) avoid getting things via sections and (to minimize dtype changes)
        # b) provide a performant path
        if len(key) != self.ndim:
            return False

        return all(is_integer(k) for k in key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_iloc_scalar(self, index, index_structure):
        self.data.iloc[800000]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._is_scalar_access [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _is_scalar_access(self, key: tuple):
        raise NotImplementedError

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocIndexer._is_scalar_access [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _is_scalar_access(self, key: tuple) -> bool:
        """
        Returns
        -------
        bool
        """
        # this is a shortcut accessor to both .loc and .iloc
        # that provide the equivalent access of .at and .iat
        # a) avoid getting things via sections and (to minimize dtype changes)
        # b) provide a performant path
        if len(key) != self.ndim:
            return False

        for i, k in enumerate(key):
            if not is_scalar(k):
                return False

            ax = self.obj.axes[i]
            if isinstance(ax, MultiIndex):
                return False

            if isinstance(k, str) and ax._supports_partial_string_indexing:
                # partial string indexing, df.loc['2000', 'A']
                # should not be considered scalar
                return False

            if not ax._index_as_unique:
                return False

        return True

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.iloc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def iloc(self) -> _iLocIndexer:
        """
        Purely integer-location based indexing for selection by position.

        .. versionchanged:: 3.0

           Callables which return a tuple are deprecated as input.

        ``.iloc[]`` is primarily integer position based (from ``0`` to
        ``length-1`` of the axis), but may also be used with a boolean
        array.

        Allowed inputs are:

        - An integer, e.g. ``5``.
        - A list or array of integers, e.g. ``[4, 3, 0]``.
        - A slice object with ints, e.g. ``1:7``.
        - A boolean array.
        - A ``callable`` function with one argument (the calling Series or
          DataFrame) and that returns valid output for indexing (one of the above).
          This is useful in method chains, when you don't have a reference to the
          calling object, but would like to base your selection on
          some value.
        - A tuple of row and column indexes. The tuple elements consist of one of the
          above inputs, e.g. ``(0, 1)``.

        ``.iloc`` will raise ``IndexError`` if a requested indexer is
        out-of-bounds, except *slice* indexers which allow out-of-bounds
        indexing (this conforms with python/numpy *slice* semantics).

        See more at :ref:`Selection by Position <indexing.integer>`.

        See Also
        --------
        DataFrame.iat : Fast integer location scalar accessor.
        DataFrame.loc : Purely label-location based indexer for selection by label.
        Series.iloc : Purely integer-location based indexing for
                       selection by position.

        Examples
        --------
        >>> mydict = [
        ...     {"a": 1, "b": 2, "c": 3, "d": 4},
        ...     {"a": 100, "b": 200, "c": 300, "d": 400},
        ...     {"a": 1000, "b": 2000, "c": 3000, "d": 4000},
        ... ]
        >>> df = pd.DataFrame(mydict)
        >>> df
              a     b     c     d
        0     1     2     3     4
        1   100   200   300   400
        2  1000  2000  3000  4000

        **Indexing just the rows**

        With a scalar integer.

        >>> type(df.iloc[0])
        <class 'pandas.Series'>
        >>> df.iloc[0]
        a    1
        b    2
        c    3
        d    4
        Name: 0, dtype: int64

        With a list of integers.

        >>> df.iloc[[0]]
           a  b  c  d
        0  1  2  3  4
        >>> type(df.iloc[[0]])
        <class 'pandas.DataFrame'>

        >>> df.iloc[[0, 1]]
             a    b    c    d
        0    1    2    3    4
        1  100  200  300  400

        With a `slice` object.

        >>> df.iloc[:3]
              a     b     c     d
        0     1     2     3     4
        1   100   200   300   400
        2  1000  2000  3000  4000

        With a boolean mask the same length as the index.

        >>> df.iloc[[True, False, True]]
              a     b     c     d
        0     1     2     3     4
        2  1000  2000  3000  4000

        With a callable, useful in method chains. The `x` passed
        to the ``lambda`` is the DataFrame being sliced. This selects
        the rows whose index label even.

        >>> df.iloc[lambda x: x.index % 2 == 0]
              a     b     c     d
        0     1     2     3     4
        2  1000  2000  3000  4000

        **Indexing both axes**

        You can mix the indexer types for the index and columns. Use ``:`` to
        select the entire axis.

        With scalar integers.

        >>> df.iloc[0, 1]
        np.int64(2)

        With lists of integers.

        >>> df.iloc[[0, 2], [1, 3]]
              b     d
        0     2     4
        2  2000  4000

        With `slice` objects.

        >>> df.iloc[1:3, 0:3]
              a     b     c
        1   100   200   300
        2  1000  2000  3000

        With a boolean array whose length matches the columns.

        >>> df.iloc[:, [True, False, True, False]]
              a     c
        0     1     3
        1   100   300
        2  1000  3000

        With a callable function that expects the Series or DataFrame.

        >>> df.iloc[:, lambda df: [0, 2]]
              a     c
        0     1     3
        1   100   300
        2  1000  3000
        """
        return _iLocIndexer("iloc", self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.iat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def iat(self) -> _iAtIndexer:
        """
        Access a single value for a row/column pair by integer position.

        Similar to ``iloc``, in that both provide integer-based lookups. Use
        ``iat`` if you only need to get or set a single value in a DataFrame
        or Series.

        Raises
        ------
        IndexError
            When integer position is out of bounds.

        See Also
        --------
        DataFrame.at : Access a single value for a row/column label pair.
        DataFrame.loc : Access a group of rows and columns by label(s).
        DataFrame.iloc : Access a group of rows and columns by integer position(s).

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     [[0, 2, 3], [0, 4, 1], [10, 20, 30]], columns=["A", "B", "C"]
        ... )
        >>> df
            A   B   C
        0   0   2   3
        1   0   4   1
        2  10  20  30

        Get value at specified row/column pair

        >>> df.iat[1, 2]
        np.int64(1)

        Set value at specified row/column pair

        >>> df.iat[1, 2] = 10
        >>> df.iat[1, 2]
        np.int64(10)

        Get value within a series

        >>> df.loc[0].iat[1]
        np.int64(2)
        """
        return _iAtIndexer("iat", self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._setitem_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def _setitem_array(self, key, value) -> None:
        # also raises Exception if object array with NA values
        if com.is_bool_indexer(key):
            # bool indexer is indexing along rows
            if len(key) != len(self.index):
                raise ValueError(
                    f"Item wrong length {len(key)} instead of {len(self.index)}!"
                )
            key = check_bool_indexer(self.index, key)
            indexer = key.nonzero()[0]
            if isinstance(value, DataFrame):
                # GH#39931 reindex since iloc does not align
                value = value.reindex(self.index.take(indexer))
            self.iloc[indexer] = value

        # Note: unlike self.iloc[:, indexer] = value, this will
        #  never try to overwrite values inplace

        elif isinstance(value, DataFrame):
            check_key_length(self.columns, key, value)
            for k1, k2 in zip(key, value.columns, strict=False):
                self[k1] = value[k2]

        elif not is_list_like(value):
            for col in key:
                self[col] = value

        elif isinstance(value, np.ndarray) and value.ndim == 2:
            self._iset_not_inplace(key, value)

        elif np.ndim(value) > 1:
            # list of lists
            value = DataFrame(value).values
            self._setitem_array(key, value)

        else:
            self._iset_not_inplace(key, value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::assert_indexing_slices_equivalent [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py]
def assert_indexing_slices_equivalent(ser: Series, l_slc: slice, i_slc: slice) -> None:
    """
    Check that ser.iloc[i_slc] matches ser.loc[l_slc] and, if applicable,
    ser[l_slc].
    """
    expected = ser.iloc[i_slc]

    assert_series_equal(ser.loc[l_slc], expected)

    if not is_integer_dtype(ser.index):
        # For integer indices, .loc and plain getitem are position-based.
        assert_series_equal(ser[l_slc], expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_AtIndexer.__setitem__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def __setitem__(self, key, value) -> None:
        if not CHAINED_WARNING_DISABLED:
            if sys.getrefcount(self.obj) <= REF_COUNT_IDX:
                warnings.warn(
                    _chained_assignment_msg, ChainedAssignmentError, stacklevel=2
                )

        # GH#48323 - deprecate .at setitem with expansion
        self._warn_if_expanding(key)

        if self.ndim == 2 and not self._axes_are_unique:
            # GH#33041 fall back to .loc
            if not isinstance(key, tuple) or not all(is_scalar(x) for x in key):
                raise ValueError("Invalid call for scalar access (setting)!")

            self.obj.loc[key] = value
            return

        return super().__setitem__(key, value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._maybe_mask_setitem_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _maybe_mask_setitem_value(self, indexer, value):
        """
        If we have obj.iloc[mask] = series_or_frame and series_or_frame has the
        same length as obj, we treat this as obj.iloc[mask] = series_or_frame[mask],
        similar to Series.__setitem__.

        Note this is only for loc, not iloc.
        """

        if (
            isinstance(indexer, tuple)
            and len(indexer) == 2
            and isinstance(value, (ABCSeries, ABCDataFrame))
        ):
            pi, icols = indexer
            ndim = value.ndim
            if com.is_bool_indexer(pi) and len(value) == len(pi):
                newkey = pi.nonzero()[0]

                if is_scalar_indexer(icols, self.ndim - 1) and ndim == 1:
                    # e.g. test_loc_setitem_boolean_mask_allfalse
                    if len(newkey) == 0:
                        value = value.iloc[:0]
                    else:
                        # test_loc_setitem_ndframe_values_alignment
                        value = self.obj.iloc._align_series(indexer, value)
                    indexer = (newkey, icols)

                elif (
                    isinstance(icols, np.ndarray)
                    and icols.dtype.kind == "i"
                    and len(icols) == 1
                ):
                    if ndim == 1:
                        # We implicitly broadcast, though numpy does not, see
                        # github.com/pandas-dev/pandas/pull/45501#discussion_r789071825
                        # test_loc_setitem_ndframe_values_alignment
                        value = self.obj.iloc._align_series(indexer, value)
                        indexer = (newkey, icols)

                    elif ndim == 2 and value.shape[1] == 1:
                        if len(newkey) == 0:
                            value = value.iloc[:0]
                        else:
                            # test_loc_setitem_ndframe_values_alignment
                            value = self.obj.iloc._align_frame(indexer, value)
                        indexer = (newkey, icols)
        elif com.is_bool_indexer(indexer):
            indexer = indexer.nonzero()[0]

        return indexer, value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iloc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def iloc(x):
    return x.iloc

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::iloc_getitem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def iloc_getitem(iloc_indexer, i):
    if isinstance(iloc_indexer, IlocType):

        def getitem_impl(iloc_indexer, i):
            return iloc_indexer.obj.values[i]

        return getitem_impl

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._has_valid_setitem_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _has_valid_setitem_indexer(self, indexer) -> bool:
        """
        Validate that a positional indexer cannot enlarge its target
        will raise if needed, does not modify the indexer externally.

        Returns
        -------
        bool
        """
        if isinstance(indexer, dict):
            raise IndexError("iloc cannot enlarge its target object")

        if isinstance(indexer, ABCDataFrame):
            raise TypeError(
                "DataFrame indexer for .iloc is not supported. "
                "Consider using .loc with a DataFrame indexer for automatic alignment.",
            )

        if not isinstance(indexer, tuple):
            indexer = _tuplify(self.ndim, indexer)

        for ax, i in zip(self.obj.axes, indexer, strict=False):
            if isinstance(i, slice):
                # should check the stop slice?
                pass
            elif is_list_like_indexer(i):
                # should check the elements?
                pass
            elif is_integer(i):
                if i >= len(ax):
                    raise IndexError("iloc cannot enlarge its target object")
            elif isinstance(i, dict):
                raise IndexError("iloc cannot enlarge its target object")

        return True

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::iloc_constructor [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def iloc_constructor(context, builder, sig, args):
    (obj,) = args
    iloc_indexer = cgutils.create_struct_proxy(sig.return_type)(context, builder)
    iloc_indexer.obj = obj
    return impl_ret_borrowed(
        context, builder, sig.return_type, iloc_indexer._getvalue()
    )
```
