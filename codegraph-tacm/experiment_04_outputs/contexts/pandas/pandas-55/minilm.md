# pandas-55 :: minilm

query: BUG: Fix incorrect _is_scalar_access check in iloc (#32085)

## selected nodes

- rank=1 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py
- rank=2 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=3 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=4 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::typeof_iloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=5 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::iloc_constructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=6 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::MethodLookup.time_lookup_iloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=7 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DataFrameNumericIndexing.time_iloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=8 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=9 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::iloc_getitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=10 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=11 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocWithEllipsis.indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=12 layer=FUNCTION tokens=1104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.iloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=13 layer=FUNCTION tokens=275 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=14 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DataFrameNumericIndexing.time_iloc_dups file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=15 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=16 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_list_like file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=17 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::type_iloc_constructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=18 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._maybe_cast_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=19 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex._disallow_mismatched_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=20 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::IlocType.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=21 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::assert_indexing_slices_equivalent file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py
- rank=22 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray._validate_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py
- rank=23 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::BinOp._disallow_scalar_only_bool_ops file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=24 layer=FUNCTION tokens=590 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._maybe_mask_setitem_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=25 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::is_extension_array_dtype_and_needs_i8_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py
- rank=26 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py::f_0 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iloc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def iloc(x):
    return x.iloc

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_iloc_scalar(self, index, index_structure):
        self.data.iloc[800000]

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::typeof_iloc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def typeof_iloc(val, c) -> IlocType:
    objtype = typeof_impl(val.obj, c)
    return IlocType(objtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::iloc_constructor [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def iloc_constructor(context, builder, sig, args):
    (obj,) = args
    iloc_indexer = cgutils.create_struct_proxy(sig.return_type)(context, builder)
    iloc_indexer.obj = obj
    return impl_ret_borrowed(
        context, builder, sig.return_type, iloc_indexer._getvalue()
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::MethodLookup.time_lookup_iloc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_lookup_iloc(self, s):
        s.iloc

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DataFrameNumericIndexing.time_iloc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_iloc(self, index, index_structure):
        self.df.iloc[:100, 0]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._is_scalar_access [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _is_scalar_access(self, key: tuple):
        raise NotImplementedError

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::iloc_getitem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def iloc_getitem(iloc_indexer, i):
    if isinstance(iloc_indexer, IlocType):

        def getitem_impl(iloc_indexer, i):
            return iloc_indexer.obj.values[i]

        return getitem_impl

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_iloc_array(self, index, index_structure):
        self.data.iloc[self.array]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocWithEllipsis.indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py]
    def indexer(self, indexer_li):
        # Test iloc while we're here
        return indexer_li

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DataFrameNumericIndexing.time_iloc_dups [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_iloc_dups(self, index, index_structure):
        self.df_dup.iloc[self.idx_dupe]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_slice [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_iloc_slice(self, index, index_structure):
        self.data.iloc[:800000]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_list_like [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_iloc_list_like(self, index, index_structure):
        self.data.iloc[[800000]]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::type_iloc_constructor [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def type_iloc_constructor(context):
    def typer(obj):
        if isinstance(obj, SeriesType):
            return IlocType(obj)

    return typer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._maybe_cast_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py]
    def _maybe_cast_indexer(self, key) -> int:
        # GH#41933: we have to do this instead of self._data._validate_scalar
        #  because this will correctly get partial-indexing on Interval categories
        try:
            return self._data._unbox_scalar(key)
        except KeyError:
            if is_valid_na_for_dtype(key, self.categories.dtype):
                return -1
            raise

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex._disallow_mismatched_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py]
    def _disallow_mismatched_indexing(self, key) -> None:
        """
        Check for mismatched-tzawareness indexing and re-raise as KeyError.
        """
        # we get here with isinstance(key, self._data._recognized_scalars)
        try:
            # GH#36148
            self._data._assert_tzawareness_compat(key)
        except TypeError as err:
            raise KeyError(key) from err

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::IlocType.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
    def __init__(self, obj_type) -> None:
        self.obj_type = obj_type
        name = f"iLocIndexer({obj_type})"
        super().__init__(name=name)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray._validate_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py]
    def _validate_scalar(self, value):
        # used by NDArrayBackedExtensionIndex.insert
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::BinOp._disallow_scalar_only_bool_ops [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py]
    def _disallow_scalar_only_bool_ops(self) -> None:
        pass

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::is_extension_array_dtype_and_needs_i8_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py]
def is_extension_array_dtype_and_needs_i8_conversion(
    left_dtype: DtypeObj, right_dtype: DtypeObj
) -> bool:
    """
    Checks that we have the combination of an ExtensionArraydtype and
    a dtype that should be converted to int64

    Returns
    -------
    bool

    Related to issue #37609
    """
    return isinstance(left_dtype, ExtensionDtype) and needs_i8_conversion(right_dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py::f_0 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py]
    def f_0(grp):
        return grp.iloc[0]
```
