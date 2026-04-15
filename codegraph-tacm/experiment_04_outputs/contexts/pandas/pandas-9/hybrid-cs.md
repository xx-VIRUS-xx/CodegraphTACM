# pandas-9 :: hybrid-cs

query: BUG: CategoricalIndex.__contains__ incorrect NaTs (#33947)

## selected nodes

- rank=1 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype.index_class file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=2 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_category.py::TestCategoricalIndex.simple_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_category.py
- rank=3 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=4 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=5 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::CategoricalIndexIndexing.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=6 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.__contains__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=7 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical.__contains__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=8 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::_maybe_unwrap file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py
- rank=9 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/aggregate/test_numba.py::incorrect_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/aggregate/test_numba.py
- rank=10 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/transform/test_numba.py::incorrect_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/transform/test_numba.py
- rank=11 layer=FUNCTION tokens=447 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=12 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py
- rank=13 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::IsMonotonic.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=14 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._na_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=15 layer=FUNCTION tokens=367 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.notna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=16 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestIndexing.assert_reindex_axis_is_ok file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py
- rank=17 layer=FUNCTION tokens=792 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.map file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=18 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=19 layer=FUNCTION tokens=387 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.notna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=20 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=21 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=22 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=23 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::na_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py
- rank=24 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_append.py::TestAppend.ci file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_append.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype.index_class [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def index_class(self) -> type_t[CategoricalIndex]:
        from pandas import CategoricalIndex

        return CategoricalIndex

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_category.py::TestCategoricalIndex.simple_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_category.py]
    def simple_index(self) -> CategoricalIndex:
        """
        Fixture that provides a CategoricalIndex.
        """
        return CategoricalIndex(list("aabbca"), categories=list("cab"), ordered=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_index_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_index_contains(self):
        self.key in self.ci

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::CategoricalIndexIndexing.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def setup(self, index):
        N = 10**5
        values = list("a" * N + "b" * N + "c" * N)
        indices = {
            "monotonic_incr": CategoricalIndex(values),
            "monotonic_decr": CategoricalIndex(reversed(values)),
            "non_monotonic": CategoricalIndex(list("abc" * N)),
        }
        self.data = indices[index]
        self.data_unique = CategoricalIndex([str(i) for i in range(N * 3)])

        self.int_scalar = 10000
        self.int_list = list(range(10000))

        self.cat_scalar = "b"
        self.cat_list = ["1", "3"]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.__contains__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py]
    def __contains__(self, key) -> bool:
        if isna(key) and key is not self.dtype.na_value:
            # GH#52840
            if lib.is_float(key) and is_nan_na():
                key = self.dtype.na_value
            elif self._data.dtype.kind == "f" and lib.is_float(key):
                return bool((np.isnan(self._data) & ~self._mask).any())

        return bool(super().__contains__(key))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical.__contains__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py]
    def __contains__(self, key) -> bool:
        """
        Returns True if `key` is in this Categorical.
        """
        # if key is a NaN, check if any NaN is in self.
        if is_valid_na_for_dtype(key, self.categories.dtype):
            return bool(self.isna().any())

        return contains(self, key, container=self._codes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::_maybe_unwrap [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py]
    def _maybe_unwrap(
        x: CategoricalIndex | Series | Categorical,
    ) -> Categorical:
        if isinstance(x, (ABCCategoricalIndex, ABCSeries)):
            return x._values
        elif isinstance(x, Categorical):
            return x
        else:
            raise TypeError("all components to combine must be Categorical")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/aggregate/test_numba.py::incorrect_function [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/aggregate/test_numba.py]
    def incorrect_function(values, index, *, a):
        return sum(values) * 2.7 + a

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/transform/test_numba.py::incorrect_function [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/transform/test_numba.py]
    def incorrect_function(values, index, *, a):
        return values + a

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py]
def contains(cat, key, container) -> bool:
    """
    Helper for membership check for ``key`` in ``cat``.

    This is a helper method for :meth:`__contains__`
    and :class:`CategoricalIndex.__contains__`.

    Returns True if ``key`` is in ``cat.categories`` and the
    location of ``key`` in ``categories`` is in ``container``.

    Parameters
    ----------
    cat : :class:`Categorical`or :class:`CategoricalIndex`
    key : a hashable object
        The key to check membership for.
    container : Container (e.g. list-like or mapping)
        The container to check for membership in.

    Returns
    -------
    is_in : bool
        True if ``key`` is in ``self.categories`` and location of
        ``key`` in ``categories`` is in ``container``, else False.

    Notes
    -----
    This method does not check for NaN values. Do that separately
    before calling this method.
    """
    hash(key)

    # get location of key in categories.
    # If a KeyError, the key isn't in categories, so logically
    #  can't be in container either.
    try:
        loc = cat.categories.get_loc(key)
    except (KeyError, TypeError):
        return False

    # loc is the location of key in categories, but also the *value*
    # for key in container. So, `key` may be in categories,
    # but still not in `container`. Example ('b' in categories,
    # but not in values):
    # 'b' in Categorical(['a'], categories=['a', 'b'])  # False
    if is_scalar(loc):
        return loc in container
    else:
        # if categories is an IntervalIndex, loc is an array.
        return any(loc_ in container for loc_ in loc)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py]
def data_missing():
    """Length 2 array with [NA, Valid]"""
    return Categorical([np.nan, "A"])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::IsMonotonic.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def setup(self):
        N = 1000
        self.c = pd.CategoricalIndex(list("a" * N + "b" * N + "c" * N))
        self.s = pd.Series(self.c)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._na_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _na_value(self) -> Hashable:
        """The expected NA value to use with this index."""
        dtype = self.dtype
        if isinstance(dtype, np.dtype):
            if dtype.kind in "mM":
                return NaT
            return np.nan
        return dtype.na_value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.notna [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def notna(self) -> npt.NDArray[np.bool_]:
        """
        Detect existing (non-missing) values.

        Return a boolean same-sized object indicating if the values are not NA.
        Non-missing values get mapped to ``True``. Characters such as empty
        strings ``''`` or :attr:`numpy.inf` are not considered NA values.
        NA values, such as None or :attr:`numpy.NaN`, get mapped to ``False``
        values.

        Returns
        -------
        numpy.ndarray[bool]
            Boolean array to indicate which entries are not NA.

        See Also
        --------
        Index.notnull : Alias of notna.
        Index.isna: Inverse of notna.
        notna : Top-level notna.

        Examples
        --------
        Show which entries in an Index are not NA. The result is an
        array.

        >>> idx = pd.Index([5.2, 6.0, np.nan])
        >>> idx
        Index([5.2, 6.0, nan], dtype='float64')
        >>> idx.notna()
        array([ True,  True, False])

        Empty strings are not considered NA values. None is considered a NA
        value.

        >>> idx = pd.Index(["black", "", "red", None])
        >>> idx
        Index(['black', '', 'red', nan], dtype='str')
        >>> idx.notna()
        array([ True,  True,  True, False])
        """
        return ~self.isna()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestIndexing.assert_reindex_axis_is_ok [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py]
        def assert_reindex_axis_is_ok(mgr, axis, new_labels, fill_value):
            mat = _as_array(mgr)
            indexer = mgr.axes[axis].get_indexer_for(new_labels)

            reindexed = mgr.reindex_axis(new_labels, axis, fill_value=fill_value)
            tm.assert_numpy_array_equal(
                algos.take_nd(mat, indexer, axis, fill_value=fill_value),
                _as_array(reindexed),
                check_dtype=False,
            )
            tm.assert_index_equal(reindexed.axes[axis], new_labels)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.map [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py]
    def map(self, mapper, na_action: Literal["ignore"] | None = None):
        """
        Map values using input an input mapping or function.

        Maps the values (their categories, not the codes) of the index to new
        categories. If the mapping correspondence is one-to-one the result is a
        :class:`~pandas.CategoricalIndex` which has the same order property as
        the original, otherwise an :class:`~pandas.Index` is returned.

        If a `dict` or :class:`~pandas.Series` is used any unmapped category is
        mapped to `NaN`. Note that if this happens an :class:`~pandas.Index`
        will be returned.

        Parameters
        ----------
        mapper : function, dict, or Series
            Mapping correspondence.
        na_action : {None, 'ignore'}, default 'ignore'
            If 'ignore', propagate NaN values, without passing them to
            the mapping correspondence.

        Returns
        -------
        pandas.CategoricalIndex or pandas.Index
            Mapped index.

        See Also
        --------
        Index.map : Apply a mapping correspondence on an
            :class:`~pandas.Index`.
        Series.map : Apply a mapping correspondence on a
            :class:`~pandas.Series`.
        Series.apply : Apply more complex functions on a
            :class:`~pandas.Series`.

        Examples
        --------
        >>> idx = pd.CategoricalIndex(["a", "b", "c"])
        >>> idx
        CategoricalIndex(['a', 'b', 'c'], categories=['a', 'b', 'c'],
                          ordered=False, dtype='category')
        >>> idx.map(lambda x: x.upper())
        CategoricalIndex(['A', 'B', 'C'], categories=['A', 'B', 'C'],
                         ordered=False, dtype='category')
        >>> idx.map({"a": "first", "b": "second", "c": "third"})
        CategoricalIndex(['first', 'second', 'third'], categories=['first',
                         'second', 'third'], ordered=False, dtype='category')

        If the mapping is one-to-one the ordering of the categories is
        preserved:

        >>> idx = pd.CategoricalIndex(["a", "b", "c"], ordered=True)
        >>> idx
        CategoricalIndex(['a', 'b', 'c'], categories=['a', 'b', 'c'],
                         ordered=True, dtype='category')
        >>> idx.map({"a": 3, "b": 2, "c": 1})
        CategoricalIndex([3, 2, 1], categories=[3, 2, 1], ordered=True,
                         dtype='category')

        If the mapping is not one-to-one an :class:`~pandas.Index` is returned:

        >>> idx.map({"a": "first", "b": "second", "c": "first"})
        Index(['first', 'second', 'first'], dtype='str')

        If a `dict` is used, all unmapped categories are mapped to `NaN` and
        the result is an :class:`~pandas.Index`:

        >>> idx.map({"a": "first", "b": "second"})
        Index(['first', 'second', nan], dtype='str')
        """
        mapped = self._values.map(mapper, na_action=na_action)
        return Index(mapped, name=self.name, copy=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_contains(self):
        self.c.searchsorted(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.notna [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def notna(self) -> Series:
        """
        Detect existing (non-missing) values.

        Return a boolean same-sized Series indicating if the values are not NA.
        Non-missing values get mapped to True. Characters such as empty
        strings ``''`` or :attr:`numpy.inf` are not considered NA values.
        NA values, such as None or :attr:`numpy.NaN`, get mapped to False
        values.

        Returns
        -------
        Series
            Mask of bool values for each element in Series that
            indicates whether an element is not an NA value.

        See Also
        --------
        Series.isna : Detect missing values.
        DataFrame.isna : Detect missing values.
        Series.isnull : Alias of isna.
        DataFrame.isnull : Alias of isna.
        DataFrame.notna : Boolean inverse of isna.
        DataFrame.notnull : Alias of notna.
        Series.dropna : Omit axes labels with missing values.
        DataFrame.dropna : Omit axes labels with missing values.
        notna : Top-level notna.

        Examples
        --------
        Show which entries in a Series are not NA.

        >>> ser = pd.Series([5, 6, np.nan])
        >>> ser
        0    5.0
        1    6.0
        2    NaN
        dtype: float64
        >>> ser.notna()
        0     True
        1     True
        2    False
        dtype: bool
        """
        return super().notna()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def setup(self):
        N = 10**5
        self.ci = pd.CategoricalIndex(np.arange(N))
        self.c = self.ci.values
        self.key = self.ci.categories[0]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_contains(self):
        self.key in self.c

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def index(request):
    """
    Fixture for many "simple" kinds of indices.

    These indices are unlikely to cover corner cases, e.g.
        - no names
        - no NaTs/NaNs
        - no values near implementation bounds
        - ...
    """
    # copy to avoid mutation, e.g. setting .name
    return indices_dict[request.param].copy(deep=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::na_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py]
def na_cmp():
    # we are pd.NA
    return lambda x, y: x is pd.NA and y is pd.NA

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_append.py::TestAppend.ci [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_append.py]
    def ci(self):
        categories = list("cab")
        return CategoricalIndex(list("aabbca"), categories=categories, ordered=False)
```
