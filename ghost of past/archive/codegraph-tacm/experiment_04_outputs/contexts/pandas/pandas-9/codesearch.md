# pandas-9 :: codesearch

query: BUG: CategoricalIndex.__contains__ incorrect NaTs (#33947)

## selected nodes

- rank=1 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py
- rank=2 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._na_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=3 layer=FUNCTION tokens=367 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.notna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=4 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestIndexing.assert_reindex_axis_is_ok file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py
- rank=5 layer=FUNCTION tokens=387 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.notna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=6 layer=FUNCTION tokens=581 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.notna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=7 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::na_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py
- rank=8 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=9 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py::expected_with_na_handling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py
- rank=10 layer=FUNCTION tokens=589 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.notna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=11 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._isnan file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=12 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=13 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::_where_numexpr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py
- rank=14 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype.index_class file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=15 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestIndexing.assert_reindex_indexer_is_ok file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py
- rank=16 layer=FUNCTION tokens=254 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py::get_categorical_invalid_expected file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py
- rank=17 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/test_decimal.py::na_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/test_decimal.py
- rank=18 layer=FUNCTION tokens=292 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::cmp_npy_datetimestruct file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
- rank=19 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_missing_for_sorting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py
- rank=20 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py::TestDatetimeIndex.assert_index_parameters file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py]
def data_missing():
    """Length 2 array with [NA, Valid]"""
    return Categorical([np.nan, "A"])

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.notna [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def notna(self) -> DataFrame:
        """
        Detect existing (non-missing) values.

        Return a boolean same-sized object indicating if the values are not NA.
        Non-missing values get mapped to True. Characters such as empty
        strings ``''`` or :attr:`numpy.inf` are not considered NA values.
        NA values, such as None or :attr:`numpy.NaN`, get mapped to False
        values.

        Returns
        -------
        Series/DataFrame
            Mask of bool values for each element in Series/DataFrame
            that indicates whether an element is not an NA value.

        See Also
        --------
        Series.notnull : Alias of notna.
        DataFrame.notnull : Alias of notna.
        Series.isna : Boolean inverse of notna.
        DataFrame.isna : Boolean inverse of notna.
        Series.dropna : Omit axes labels with missing values.
        DataFrame.dropna : Omit axes labels with missing values.
        notna : Top-level notna.

        Examples
        --------
        Show which entries in a DataFrame are not NA.

        >>> df = pd.DataFrame(
        ...     dict(
        ...         age=[5, 6, np.nan],
        ...         born=[
        ...             pd.NaT,
        ...             pd.Timestamp("1939-05-27"),
        ...             pd.Timestamp("1940-04-25"),
        ...         ],
        ...         name=["Alfred", "Batman", ""],
        ...         toy=[None, "Batmobile", "Joker"],
        ...     )
        ... )
        >>> df
           age       born    name        toy
        0  5.0        NaT  Alfred        NaN
        1  6.0 1939-05-27  Batman  Batmobile
        2  NaN 1940-04-25              Joker

        >>> df.notna()
             age   born  name    toy
        0   True  False  True  False
        1   True   True  True   True
        2  False   True  True   True

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
        return ~self.isna()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::na_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py]
def na_cmp():
    # we are pd.NA
    return lambda x, y: x is pd.NA and y is pd.NA

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_index_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_index_contains(self):
        self.key in self.ci

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py::expected_with_na_handling [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_array_ops.py]
    def expected_with_na_handling(lvalues, rvalues, op):
        # Similar to comparison_op, handle zerodim arrays with na value separately
        if (rvalues.ndim == 0) and isna(rvalues.item()):
            # numpy does not like comparisons vs None
            if op is operator.ne:
                return np.ones(lvalues.shape, dtype=bool)
            else:
                return np.zeros(lvalues.shape, dtype=bool)
        return op(lvalues, rvalues)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.notna [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def notna(self) -> Self:
        """
        Detect existing (non-missing) values.

        Return a boolean same-sized object indicating if the values are not NA.
        Non-missing values get mapped to True. Characters such as empty
        strings ``''`` or :attr:`numpy.inf` are not considered NA values.
        NA values, such as None or :attr:`numpy.NaN`, get mapped to False
        values.

        Returns
        -------
        Series/DataFrame
            Mask of bool values for each element in Series/DataFrame
            that indicates whether an element is not an NA value.

        See Also
        --------
        Series.notnull : Alias of notna.
        DataFrame.notnull : Alias of notna.
        Series.isna : Boolean inverse of notna.
        DataFrame.isna : Boolean inverse of notna.
        Series.dropna : Omit axes labels with missing values.
        DataFrame.dropna : Omit axes labels with missing values.
        notna : Top-level notna.

        Examples
        --------
        Show which entries in a DataFrame are not NA.

        >>> df = pd.DataFrame(
        ...     dict(
        ...         age=[5, 6, np.nan],
        ...         born=[
        ...             pd.NaT,
        ...             pd.Timestamp("1939-05-27"),
        ...             pd.Timestamp("1940-04-25"),
        ...         ],
        ...         name=["Alfred", "Batman", ""],
        ...         toy=[None, "Batmobile", "Joker"],
        ...     )
        ... )
        >>> df
           age       born    name        toy
        0  5.0        NaT  Alfred        NaN
        1  6.0 1939-05-27  Batman  Batmobile
        2  NaN 1940-04-25              Joker

        >>> df.notna()
             age   born  name    toy
        0   True  False  True  False
        1   True   True  True   True
        2  False   True  True   True

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
        return notna(self).__finalize__(self, method="notna")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._isnan [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _isnan(self) -> npt.NDArray[np.bool_]:
        """
        Return if each value is NaN.
        """
        if self._can_hold_na:
            return isna(self)
        else:
            # shouldn't reach to this condition by checking hasnans beforehand
            values = np.empty(len(self), dtype=np.bool_)
            values.fill(False)
            return values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::_where_numexpr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py]
def _where_numexpr(cond, left_op, right_op):
    # Caller is responsible for extracting ndarray if necessary
    result = None

    if _can_use_numexpr(None, "where", left_op, right_op, "where"):
        result = ne.evaluate(
            "where(cond_value, a_value, b_value)",
            local_dict={"cond_value": cond, "a_value": left_op, "b_value": right_op},
            casting="safe",
        )

    if result is None:
        result = _where_standard(cond, left_op, right_op)

    return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype.index_class [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def index_class(self) -> type_t[CategoricalIndex]:
        from pandas import CategoricalIndex

        return CategoricalIndex

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestIndexing.assert_reindex_indexer_is_ok [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py]
        def assert_reindex_indexer_is_ok(mgr, axis, new_labels, indexer, fill_value):
            mat = _as_array(mgr)
            reindexed_mat = algos.take_nd(mat, indexer, axis, fill_value=fill_value)
            reindexed = mgr.reindex_indexer(
                new_labels, indexer, axis, fill_value=fill_value
            )
            tm.assert_numpy_array_equal(
                reindexed_mat, _as_array(reindexed), check_dtype=False
            )
            tm.assert_index_equal(reindexed.axes[axis], new_labels)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py::get_categorical_invalid_expected [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py]
    def get_categorical_invalid_expected():
        # Categorical is special without 'observed=True', we get a NaN entry
        #  corresponding to the unobserved group. If we passed observed=True
        #  to groupby, expected would just be 'df.set_index(keys)[columns]'
        #  as below
        lev = Categorical([0], dtype=values.dtype)
        if len(keys) != 1:
            idx = MultiIndex.from_product([lev, lev], names=keys)
        else:
            # all columns are dropped, but we end up with one row
            # Categorical is special without 'observed=True'
            idx = Index(lev, name=keys[0])

        if using_infer_string:
            columns = Index([], dtype="str")
        else:
            columns = []
        expected = DataFrame([], columns=columns, index=idx)
        return expected

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/test_decimal.py::na_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/test_decimal.py]
def na_cmp():
    return lambda x, y: x.is_nan() and y.is_nan()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::cmp_npy_datetimestruct [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c]
int cmp_npy_datetimestruct(const npy_datetimestruct *a,
                           const npy_datetimestruct *b) {
  if (a->year > b->year) {
    return 1;
  } else if (a->year < b->year) {
    return -1;
  }

  if (a->month > b->month) {
    return 1;
  } else if (a->month < b->month) {
    return -1;
  }

  if (a->day > b->day) {
    return 1;
  } else if (a->day < b->day) {
    return -1;
  }

  if (a->hour > b->hour) {
    return 1;
  } else if (a->hour < b->hour) {
    return -1;
  }

  if (a->min > b->min) {
    return 1;
  } else if (a->min < b->min) {
    return -1;
  }

  if (a->sec > b->sec) {
    return 1;
  } else if (a->sec < b->sec) {
    return -1;
  }

  if (a->us > b->us) {
    return 1;
  } else if (a->us < b->us) {
    return -1;
  }

  if (a->ps > b->ps) {
    return 1;
  } else if (a->ps < b->ps) {
    return -1;
  }

  if (a->as > b->as) {
    return 1;
  } else if (a->as < b->as) {
    return -1;
  }

  return 0;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_missing_for_sorting [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py]
def data_missing_for_sorting():
    return Categorical(["A", None, "B"], categories=["B", "A"], ordered=True)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py::TestDatetimeIndex.assert_index_parameters [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py]
    def assert_index_parameters(self, index):
        assert index.freq == "40960ns"
        assert index.inferred_freq == "40960ns"
```
