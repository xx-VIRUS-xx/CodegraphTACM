# pandas-9 :: minilm

query: BUG: CategoricalIndex.__contains__ incorrect NaTs (#33947)

## selected nodes

- rank=1 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._maybe_cast_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=2 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_category.py::TestCategoricalIndex.simple_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_category.py
- rank=3 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=4 layer=FUNCTION tokens=448 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._is_dtype_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=5 layer=FUNCTION tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_insert_nat_bin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=6 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=7 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Constructor.time_datetimes_with_nat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=8 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=9 layer=FUNCTION tokens=216 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._wrap_result file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=10 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype.index_class file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=11 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._maybe_cast_listlike_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=12 layer=FUNCTION tokens=226 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Rank.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=13 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py::BinGrouper.indices file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py
- rank=14 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::IsMonotonic.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=15 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype.categories file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=16 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=17 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_quantile.py::TestQuantileExtensionDtype.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_quantile.py
- rank=18 layer=FUNCTION tokens=792 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.map file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=19 layer=FUNCTION tokens=277 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.write_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=20 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._check_compatible_with file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=21 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::CategoricalSlicing.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_category.py::TestCategoricalIndex.simple_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_category.py]
    def simple_index(self) -> CategoricalIndex:
        """
        Fixture that provides a CategoricalIndex.
        """
        return CategoricalIndex(list("aabbca"), categories=list("cab"), ordered=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_index_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_index_contains(self):
        self.key in self.ci

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._is_dtype_compat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py]
    def _is_dtype_compat(self, other: Index) -> Categorical:
        """
        *this is an internal non-public method*

        provide a comparison between the dtype of self and other (coercing if
        needed)

        Parameters
        ----------
        other : Index

        Returns
        -------
        Categorical

        Raises
        ------
        TypeError if the dtypes are not compatible
        """
        if isinstance(other.dtype, CategoricalDtype):
            cat = extract_array(other)
            cat = cast("Categorical", cat)
            if not cat._categories_match_up_to_permutation(self._values):
                raise TypeError(
                    "categories must match existing categories when appending"
                )

        elif other._is_multi:
            # preempt raising NotImplementedError in isna call
            raise TypeError("MultiIndex is not dtype-compatible with CategoricalIndex")
        else:
            values = other

            codes = self.categories.get_indexer(values)
            if ((codes == -1) & ~values.isna()).any():
                # GH#37667 see test_equals_non_category
                raise TypeError(
                    "categories must match existing categories when appending"
                )
            cat = Categorical(other, dtype=self.dtype)
            other = CategoricalIndex(cat)
            if not other.isin(values).all():
                raise TypeError(
                    "cannot append a non-category item to a CategoricalIndex"
                )
            cat = other._values

        return cat

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_insert_nat_bin [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
def _insert_nat_bin(
    binner: PeriodIndex, bins: np.ndarray, labels: PeriodIndex, nat_count: int
) -> tuple[PeriodIndex, np.ndarray, PeriodIndex]:
    # NaT handling as in pandas._lib.lib.generate_bins_dt64()
    # shift bins by the number of NaT
    assert nat_count > 0
    bins += nat_count
    bins = np.insert(bins, 0, nat_count)

    # Incompatible types in assignment (expression has type "Index", variable
    # has type "PeriodIndex")
    binner = binner.insert(0, NaT)  # type: ignore[assignment]
    # Incompatible types in assignment (expression has type "Index", variable
    # has type "PeriodIndex")
    labels = labels.insert(0, NaT)  # type: ignore[assignment]
    return binner, bins, labels

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def setup(self):
        N = 10**5
        self.ci = pd.CategoricalIndex(np.arange(N))
        self.c = self.ci.values
        self.key = self.ci.categories[0]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Constructor.time_datetimes_with_nat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_datetimes_with_nat(self):
        pd.Categorical(self.datetimes_with_nat)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._wrap_result [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _wrap_result(self, result):
        """
        Potentially wrap any results.
        """
        if isinstance(result, ABCSeries) and self._selection is not None:
            result.name = self._selection

        if isinstance(result, ABCSeries) and result.empty:
            # When index is all NaT, result is empty but index is not
            obj = self.obj
            result.index = _asfreq_compat(obj.index[:0], freq=self.freq)
            result.name = getattr(obj, "name", None)

        if self._timegrouper._arrow_dtype is not None:
            result.index = result.index.astype(self._timegrouper._arrow_dtype)
            result.index.name = self.obj.index.name

        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype.index_class [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def index_class(self) -> type_t[CategoricalIndex]:
        from pandas import CategoricalIndex

        return CategoricalIndex

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._maybe_cast_listlike_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py]
    def _maybe_cast_listlike_indexer(self, values) -> CategoricalIndex:
        if isinstance(values, CategoricalIndex):
            values = values._data
        if isinstance(values, Categorical):
            # Indexing on codes is more efficient if categories are the same,
            #  so we can apply some optimizations based on the degree of
            #  dtype-matching.
            cat = self._data._encode_with_my_categories(values)
            codes = cat._codes
        else:
            codes = self.categories.get_indexer(values)
            codes = codes.astype(self.codes.dtype, copy=False)
            cat = self._data._from_backing_data(codes)
        return type(self)._simple_new(cat)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Rank.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def setup(self):
        N = 10**5
        ncats = 15

        self.s_str = pd.Series(np.random.randint(0, ncats, size=N).astype(str))
        self.s_str_cat = pd.Series(self.s_str, dtype="category")
        with warnings.catch_warnings(record=True):
            str_cat_type = pd.CategoricalDtype(set(self.s_str), ordered=True)
            self.s_str_cat_ordered = self.s_str.astype(str_cat_type)

        self.s_int = pd.Series(np.random.randint(0, ncats, size=N))
        self.s_int_cat = pd.Series(self.s_int, dtype="category")
        with warnings.catch_warnings(record=True):
            int_cat_type = pd.CategoricalDtype(set(self.s_int), ordered=True)
            self.s_int_cat_ordered = self.s_int.astype(int_cat_type)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py::BinGrouper.indices [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py]
    def indices(self):
        indices = collections.defaultdict(list)

        i: np.int64 | int = 0
        for label, bin in zip(self.binlabels, self.bins, strict=True):
            if i < bin:
                if label is not NaT:
                    indices[label] = list(range(i, bin))
                i = bin
        return indices

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::IsMonotonic.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def setup(self):
        N = 1000
        self.c = pd.CategoricalIndex(list("a" * N + "b" * N + "c" * N))
        self.s = pd.Series(self.c)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype.categories [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def categories(self) -> Index:
        """
        An ``Index`` containing the unique categories allowed.

        If no categories were explicitly provided at construction time, this
        will be ``None`` until the ``CategoricalDtype`` is attached to actual
        data.

        See Also
        --------
        ordered : Whether the categories have an ordered relationship.

        Examples
        --------
        >>> cat_type = pd.CategoricalDtype(categories=["a", "b"], ordered=True)
        >>> cat_type.categories
        Index(['a', 'b'], dtype='str')
        """
        return self._categories

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def setup(self):
        N = 10**5
        self.index = pd.CategoricalIndex(range(N), range(N))
        self.series = pd.Series(range(N), index=self.index).sort_index()
        self.category = self.index[500]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_quantile.py::TestQuantileExtensionDtype.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_quantile.py]
    def index(self, request):
        # NB: not actually an Index object
        idx = request.param
        idx.name = "A"
        return idx

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.write_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def write_index(self, key: str, index: Index) -> None:
        if isinstance(index, MultiIndex):
            setattr(self.attrs, f"{key}_variety", "multi")
            self.write_multi_index(key, index)
        else:
            setattr(self.attrs, f"{key}_variety", "regular")
            converted = _convert_index("index", index, self.encoding, self.errors)

            self.write_array(key, converted.values)

            node = getattr(self.group, key)
            node._v_attrs.kind = converted.kind
            node._v_attrs.name = index.name

            if isinstance(index, (DatetimeIndex, PeriodIndex)):
                node._v_attrs.index_class = self._class_to_alias(type(index))

            if isinstance(index, (DatetimeIndex, PeriodIndex, TimedeltaIndex)):
                node._v_attrs.freq = index.freq

            if isinstance(index, DatetimeIndex) and index.tz is not None:
                node._v_attrs.tz = _get_tz(index.tz)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray._check_compatible_with [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def _check_compatible_with(self, other: Period | NaTType | PeriodArray) -> None:  # type: ignore[override]
        if other is NaT:
            return
        elif isinstance(other, Period):
            self._require_matching_unit(other._dtype._freqstr)
        else:
            # error: Item "NaTType" of "NaTType | PeriodArray" has no
            # attribute "freq"
            self._require_matching_unit(other.dtype._freqstr)  # type: ignore[union-attr]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::CategoricalSlicing.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def setup(self, index):
        N = 10**6
        categories = ["a", "b", "c"]
        if index == "monotonic_incr":
            codes = np.repeat([0, 1, 2], N)
        elif index == "monotonic_decr":
            codes = np.repeat([2, 1, 0], N)
        elif index == "non_monotonic":
            codes = np.tile([0, 1, 2], N)
        else:
            raise ValueError(f"Invalid index param: {index}")

        self.data = pd.Categorical.from_codes(codes, categories=categories)
        self.scalar = 10000
        self.list = list(range(10000))
        self.cat_scalar = "b"
```
