# pandas-9 :: tacm

query: BUG: CategoricalIndex.__contains__ incorrect NaTs (#33947)

## selected nodes

- rank=1 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=2 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FILE tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=4 layer=FILE tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py
- rank=5 layer=FILE tokens=11 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/errors/cow.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/errors/cow.py
- rank=6 layer=CLASS tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=7 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py
- rank=8 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/object/test_indexing.py::TestGetIndexerNonUnique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/object/test_indexing.py
- rank=9 layer=CLASS tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/interval/test_contains.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/interval/test_contains.py
- rank=10 layer=CLASS tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_indexing.py
- rank=11 layer=CLASS tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_indexing.py
- rank=12 layer=CLASS tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_indexing.py
- rank=13 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py
- rank=14 layer=CLASS tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=15 layer=CLASS tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py
- rank=16 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_indexing.py
- rank=17 layer=CLASS tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/timedeltas/test_constructors.py::TestTimedeltaArrayConstructor file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/timedeltas/test_constructors.py
- rank=18 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=19 layer=CLASS tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py::TestTimedeltaIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py
- rank=20 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_indexing.py
- rank=21 layer=CLASS tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=22 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_indexing.py
- rank=23 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=24 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=25 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=26 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.__contains__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=27 layer=FUNCTION tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=28 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=29 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_EastAsianTextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=30 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.equals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=31 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Contains.time_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py
- rank=32 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py
- rank=33 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._maybe_cast_listlike_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=34 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=35 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Contains.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=36 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=37 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._is_dtype_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=38 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=39 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=40 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.inferred_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=41 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.map file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=42 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._formatter_func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=43 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._can_hold_strings file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=44 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._is_comparable_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=45 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._should_fallback_to_positional file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=46 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Contains.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py
- rank=47 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=48 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._format_attrs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=49 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=50 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._maybe_cast_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=51 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._engine_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=52 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/readers.py::read_csv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/readers.py
- rank=53 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py::to_numeric file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py
- rank=54 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::union_categoricals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py
- rank=55 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py::Styler.to_latex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py
- rank=56 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/readers.py::read_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/readers.py
- rank=57 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=58 layer=FUNCTION tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=59 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader.read file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=60 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=61 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.replace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py

## context

```text
file core/indexes/category.py
imports: __future__, typing, numpy, pandas, collections
defines: CategoricalIndex

file pandas/core/frame.py
imports: __future__, collections, functools, io, itertools, operator, sys, typing
defines: DataFrame, _from_nested_dict, _reindex_for_setitem

file core/arrays/categorical.py
imports: __future__, csv, functools, itertools, operator, shutil, typing, warnings
defines: Categorical, CategoricalAccessor, _cat_compare_op, func, contains, _get_codes_for_values, recode_for_categories, factorize_from_iterable, factorize_from_iterables

file asv_bench/benchmarks/strings.py
imports: warnings, numpy, pandas
defines: Dtypes, Construction, Methods, Repeat, Cat, Contains, Split, Extract, Dummies, Encode, Slice, Iter, StringArrayConstruction

file pandas/errors/cow.py
imports: —
defines: —

class CategoricalIndex(NDArrayBackedExtensionIndex):  [core/indexes/category.py:78]
methods: _can_hold_strings, _engine_type, _format_attrs
         _formatter_func, _is_comparable_dtype
         _is_dtype_compat, _maybe_cast_indexer
         _maybe_cast_listlike_indexer
         _should_fallback_to_positional, equals
         inferred_type, map, reindex, __contains__, __new__

class Contains(Dtypes):  [asv_bench/benchmarks/strings.py:217]
methods: setup, time_contains

class TestGetIndexerNonUnique:  [indexes/object/test_indexing.py:76]
methods: test_get_indexer_non_unique_nas
         test_get_indexer_non_unique_np_nats

class TestContains:  [scalar/interval/test_contains.py:10]
methods: test_contains, test_contains_infinite_length
         test_contains_interval, test_contains_mixed_types
         test_contains_zero_length

class TestContains:  [indexes/multi/test_indexing.py:797]
methods: test_contains, test_contains_td64_level
         test_contains_top_level
         test_contains_with_missing_value
         test_contains_with_nat, test_large_mi_contains
         test_multiindex_contains_dropped

class TestContains:  [indexes/categorical/test_indexing.py:336]
methods: test_contains, test_contains_interval, test_contains_list
         test_contains_na_dtype, test_contains_nan

class TestContains:  [tests/indexes/test_indexing.py:93]
methods: test_contains_requires_hashable_raises
         test_contains_with_float_index
         test_index_contains, test_index_not_contains
         test_mixed_index_contains
         test_mixed_index_not_contains

class TestContains:  [arrays/categorical/test_indexing.py:285]
methods: test_contains, test_contains_interval, test_contains_list

class Contains:  [asv_bench/benchmarks/categoricals.py:240]
methods: setup, time_categorical_contains
         time_categorical_index_contains

class TestContains:  [indexes/period/test_indexing.py:745]
methods: test_contains, test_contains_freq_mismatch
         test_contains_nat

class TestContains:  [indexes/numeric/test_indexing.py:547]
methods: test_contains_float64_nans, test_contains_float64_not_nans
         test_contains_none

class TestTimedeltaArrayConstructor:  [arrays/timedeltas/test_constructors.py:7]
methods: test_copy, test_from_sequence_dtype
         test_incorrect_dtype_raises, test_other_type_raises

class TestContains:  [indexes/timedeltas/test_indexing.py:337]
methods: test_contains, test_contains_nonunique

class TestTimedeltaIndex:  [indexes/timedeltas/test_setops.py:17]
methods: test_intersection, test_intersection_bug_1708
         test_intersection_equal
         test_intersection_non_monotonic
         test_intersection_zero_length, test_union
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_freq_infer, test_union_sort_false
         test_zero_length_input_index

class TestContains:  [indexes/datetimes/test_indexing.py:506]
methods: test_contains_nonunique, test_dti_contains_with_duplicates

class SearchSorted:  [asv_bench/benchmarks/categoricals.py:323]
methods: setup, time_categorical_contains
         time_categorical_index_contains

class TestContains:  [indexes/interval/test_indexing.py:742]
methods: test_contains_dunder

    def len(self):
        """
        Compute the length of each element in the Series/Index.

        The element may be a sequence (such as a string, tuple or list) or a collection
        (such as a dictionary).

        Returns
        -------
        Series or Index of int
            A Series or Index of integer values indicating the length of each
            element in the Series or Index.
    # ... truncated

    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

    # ... truncated

def contains(cat, key, container) -> bool:
    """
    Helper for membership check for ``key`` in ``cat``.

    This is a helper method for :meth:`__contains__`
    and :class:`CategoricalIndex.__contains__`.

    Returns True if ``key`` is in ``cat.categories`` and the
    location of ``key`` in ``categories`` is in ``container``.

    Parameters
    ----------
    # ... truncated

    def __contains__(self, key: Any) -> bool:
        """
        Return a boolean indicating whether the provided key is in the index.

        Parameters
        ----------
        key : label
            The key to check if it is present in the index.

        Returns
        -------
        bool
    # ... truncated

    def setup(self):
        N = 10**5
        self.ci = pd.CategoricalIndex(np.arange(N))
        self.c = self.ci.values
        self.key = self.ci.categories[0]

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

    def len(self, text: str) -> int:
        """
        Calculate display width considering unicode East Asian Width
        """
        if not isinstance(text, str):
            return len(text)

        return sum(
            self._EAW_MAP.get(east_asian_width(c), self.ambiguous_width) for c in text
        )

    def equals(self, other: object) -> bool:
        """
        Determine if two CategoricalIndex objects contain the same elements.

        The order and orderedness of elements matters. The categories matter,
        but the order of the categories matters only when ``ordered=True``.

        Parameters
        ----------
        other : object
            The CategoricalIndex object to compare with.

    # ... truncated

    def time_contains(self, dtype, regex):
        self.s.str.contains("A", regex=regex)

    def len(self, text: str) -> int:
        return len(text)

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

    def time_categorical_contains(self):
        self.key in self.c

    def time_categorical_index_contains(self):
        self.key in self.ci

    def time_categorical_contains(self):
        self.c.searchsorted(self.key)

    def _is_dtype_compat(self, other: Index) -> Categorical:
        """
        *this is an internal non-public method*

        provide a comparison between the dtype of self and other (coercing if
        needed)

        Parameters
        ----------
        other : Index

        Returns
    # ... truncated

    def reindex(
        self, target, method=None, level=None, limit: int | None = None, tolerance=None
    ) -> tuple[Index, npt.NDArray[np.intp] | None]:
        """
        Create index with target's values (move/add/delete values as necessary)

        Returns
        -------
        new_index : pd.Index
            Resulting index
        indexer : np.ndarray[np.intp] or None
            Indices of output values in original index

        """
        if method is not None:
            raise NotImplementedError(
                "argument method is not implemented for CategoricalIndex.reindex"
            )
        if level is not None:
            raise NotImplementedError(
                "argument level is not implemented for CategoricalIndex.reindex"
            )
        if limit is not None:
            raise NotImplementedError(
                "argument limit is not implemented for CategoricalIndex.reindex"
            )
        return super().reindex(target)

    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

    def inferred_type(self) -> str:
        return "categorical"

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
    # ... truncated

    def _formatter_func(self, val) -> str:
        return self.categories._formatter_func(val)

    def _can_hold_strings(self):
        return self.categories._can_hold_strings

    def _is_comparable_dtype(self, dtype: DtypeObj) -> bool:
        return self.categories._is_comparable_dtype(dtype)

    def _should_fallback_to_positional(self) -> bool:
        return self.categories._should_fallback_to_positional

    def setup(self, dtype, regex):
        super().setup(dtype)

    def setup(self):
        N = 10**5
        self.ci = pd.CategoricalIndex(np.arange(N)).sort_values()
        self.c = self.ci.values
        self.key = self.ci.categories[1]

    def _format_attrs(self):
        """
        Return a list of tuples of the (attr,formatted_value)
        """
        attrs: list[tuple[str, str | int | bool | None]]

        attrs = [
            (
                "categories",
                f"[{', '.join(self._data._repr_categories())}]",
            ),
            ("ordered", self.ordered),
        ]
        extra = super()._format_attrs()
        return attrs + extra

    def __new__(
        cls,
        data=None,
        categories=None,
        ordered=None,
        dtype: Dtype | None = None,
        copy: bool = False,
        name: Hashable | None = None,
    ) -> Self:
        name = maybe_extract_name(name, data, cls)

        if is_scalar(data):
            # GH#38944 include None here, which pre-2.0 subbed in []
            cls._raise_scalar_data_error(data)

        data = Categorical(
            data, categories=categories, ordered=ordered, dtype=dtype, copy=copy
        )

        return cls._simple_new(data, name=name)

    def _maybe_cast_indexer(self, key) -> int:
        # GH#41933: we have to do this instead of self._data._validate_scalar
        #  because this will correctly get partial-indexing on Interval categories
        try:
            return self._data._unbox_scalar(key)
        except KeyError:
            if is_valid_na_for_dtype(key, self.categories.dtype):
                return -1
            raise

    def _engine_type(self) -> type[libindex.IndexEngine]:
        # self.codes can have dtype int8, int16, int32 or int64, so we need
        # to return the corresponding engine type (libindex.Int8Engine, etc.).
        return {
            np.int8: libindex.Int8Engine,
            np.int16: libindex.Int16Engine,
            np.int32: libindex.Int32Engine,
            np.int64: libindex.Int64Engine,
        }[self.codes.dtype.type]

def read_csv(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None | lib.NoDefault = lib.no_default,
    delimiter: str | None | lib.NoDefault = None,
    # Column and Index Locations and Names
    header: int | Sequence[int] | None | Literal["infer"] = "infer",
    names: Sequence[Hashable] | None | lib.NoDefault = lib.no_default,
    index_col: IndexLabel | Literal[False] | None = None,
    usecols: UsecolsArgType = None,
    # General Parsing Configuration
    dtype: DtypeArg | None = None,
    # ... truncated

def to_numeric(
    arg,
    errors: DateTimeErrorChoices = "raise",
    downcast: Literal["integer", "signed", "unsigned", "float"] | None = None,
    dtype_backend: DtypeBackend | lib.NoDefault = lib.no_default,
):
    """
    # ... truncated

def union_categoricals(
    to_union: Sequence[CategoricalIndex | Series | Categorical],
    sort_categories: bool = False,
    ignore_order: bool = False,
) -> Categorical:
    """
    # ... truncated

    def to_latex(
        self,
        buf: FilePath | WriteBuffer[str] | None = None,
        *,
        column_format: str | None = None,
        position: str | None = None,
        position_float: str | None = None,
        hrules: bool | None = None,
        clines: str | None = None,
        label: str | None = None,
        caption: str | tuple | None = None,
        sparse_index: bool | None = None,
    # ... truncated

def read_table(
    filepath_or_buffer: FilePath | ReadCsvBuffer[bytes] | ReadCsvBuffer[str],
    *,
    sep: str | None | lib.NoDefault = lib.no_default,
    delimiter: str | None | lib.NoDefault = None,
    # Column and Index Locations and Names
    header: int | Sequence[int] | None | Literal["infer"] = "infer",
    names: Sequence[Hashable] | None | lib.NoDefault = lib.no_default,
    index_col: IndexLabel | Literal[False] | None = None,
    usecols: UsecolsArgType = None,
    # General Parsing Configuration
    dtype: DtypeArg | None = None,
    # ... truncated

    def func(self, other):
        hashable = is_hashable(other)
        if is_list_like(other) and len(other) != len(self) and not hashable:
            # in hashable case we may have a tuple that is itself a category
            raise ValueError("Lengths must match.")

        if not self.ordered:
            if opname in ["__lt__", "__gt__", "__le__", "__ge__"]:
                raise TypeError(
                    "Unordered Categoricals can only compare equality or not"
                )
        if isinstance(other, Categorical):
    # ... truncated

    def astype(
        self,
        dtype,
        copy: bool | lib.NoDefault = lib.no_default,
        errors: IgnoreRaise = "raise",
    ) -> Self:
        """
    # ... truncated

    def read(
        self,
        nrows: int | None = None,
        convert_dates: bool | None = None,
        convert_categoricals: bool | None = None,
        index_col: str | None = None,
        convert_missing: bool | None = None,
        preserve_dtypes: bool | None = None,
        columns: Sequence[str] | None = None,
        order_categoricals: bool | None = None,
    ) -> DataFrame:
        """
    # ... truncated

    def astype(self, dtype: Dtype, copy: bool = True) -> Index:
        """
        Create an Index with values cast to dtypes.

        The class of a new Index is determined by dtype. When conversion is
        impossible, a TypeError exception is raised.

        Parameters
        ----------
        dtype : numpy dtype or pandas type
            Dtype for the result Index.
        copy : bool, default True
    # ... truncated

    def replace(
        self,
        to_replace=None,
        value=lib.no_default,
        *,
        inplace: bool = False,
        regex: bool = False,
    ) -> Self:
        """
    # ... truncated
```
