# pandas-97 :: tacm

query: BUG: TimedeltaIndex.union with sort=False (#30701)

## selected nodes

- rank=1 layer=FILE tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py
- rank=2 layer=FILE tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py
- rank=3 layer=FILE tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py
- rank=4 layer=CLASS tokens=260 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_union_categoricals.py::TestUnionCategoricals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_union_categoricals.py
- rank=5 layer=CLASS tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py::TestTimedeltaIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_setops.py
- rank=6 layer=CLASS tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::TestSortValues file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=7 layer=CLASS tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/base_class/test_setops.py::TestIndexSetOps file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/base_class/test_setops.py
- rank=8 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_setops.py::TestSetOpsSort file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_setops.py
- rank=9 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py::TestCustomDatetimeIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_setops.py
- rank=10 layer=CLASS tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py::IOArgs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py
- rank=11 layer=FUNCTION tokens=300 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py::_get_combined_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py
- rank=12 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py::union_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py
- rank=13 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::union_categoricals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py
- rank=14 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=15 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=16 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::TestSortValues.check_sort_values_with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=17 layer=FUNCTION tokens=248 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py::get_objs_combined_axis file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py
- rank=18 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=19 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::value_counts_internal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py
- rank=20 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::union_with_duplicates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py
- rank=21 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::_maybe_try_sort file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=22 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._range_union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=23 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::factorize file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py
- rank=24 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=25 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py::sort file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py
- rank=26 layer=FUNCTION tokens=342 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=27 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=28 layer=FUNCTION tokens=358 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py::TestSortValues.check_sort_values_without_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
- rank=29 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::safe_sort file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py
- rank=30 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::UnionWithDuplicates.time_union_with_duplicates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=31 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::SeriesGroupBy.value_counts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=32 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=33 layer=FUNCTION tokens=7 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb::highlight_max file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/source/user_guide/style.ipynb

## context

```text
file pandas/core/algorithms.py
imports: __future__, decimal, operator, typing, warnings, numpy, pandas
defines: _ensure_data, _reconstruct_data, _ensure_arraylike, _get_hashtable_algo, _check_object_for_strings, unique, unique, unique, nunique_ints, unique_with_mask, isin, f, factorize_array, factorize, value_counts_internal, value_counts_arraylike, duplicated, mode, rank, take, searchsorted, diff, safe_sort, _sort_mixed, _sort_tuples, union_with_duplicates, map_array

file core/indexes/api.py
imports: __future__, typing, pandas, numpy
defines: get_objs_combined_axis, _get_distinct_objs, _get_combined_index, safe_sort_index, union_indexes, _sanitize_and_check, all_indexes_same, default_index

file core/interchange/column.py
imports: __future__, typing, numpy, pandas
defines: PandasColumn

class TestUnionCategoricals:  [tests/reshape/test_union_categoricals.py:15]
methods: test_union_categorical, test_union_categorical_empty
         test_union_categorical_match_types
         test_union_categorical_ordered_appearance
         test_union_categorical_ordered_true
         test_union_categorical_same_categories_different_order
         test_union_categorical_same_category
         test_union_categorical_same_category_str
         test_union_categorical_unwrap
         test_union_categoricals_empty
         test_union_categoricals_ignore_order
         test_union_categoricals_nan
         test_union_categoricals_ordered
         test_union_categoricals_sort
         test_union_categoricals_sort_false
         test_union_categoricals_sort_false_empty
         test_union_categoricals_sort_false_fastpath
         test_union_categoricals_sort_false_one_nan
         test_union_categoricals_sort_false_only_nan
         test_union_categoricals_sort_false_ordered_true
         test_union_categoricals_sort_false_skipresort

class TestTimedeltaIndex:  [indexes/timedeltas/test_setops.py:17]
methods: test_intersection, test_intersection_bug_1708
         test_intersection_equal
         test_intersection_non_monotonic
         test_intersection_zero_length, test_union
         test_union_bug_1730, test_union_bug_1745
         test_union_bug_4564, test_union_coverage
         test_union_freq_infer, test_union_sort_false
         test_zero_length_input_index

class TestSortValues:  [indexes/datetimelike_/test_sort_values.py:42]
methods: check_sort_values_with_freq
         check_sort_values_without_freq, non_monotonic_idx
         test_argmin_argmax, test_sort_values
         test_sort_values_with_freq_datetimeindex
         test_sort_values_with_freq_periodindex
         test_sort_values_with_freq_periodindex2
         test_sort_values_with_freq_timedeltaindex
         test_sort_values_without_freq_datetimeindex
         test_sort_values_without_freq_periodindex
         test_sort_values_without_freq_periodindex_nat
         test_sort_values_without_freq_timedeltaindex

class TestIndexSetOps:  [indexes/base_class/test_setops.py:22]
methods: test_difference_base, test_difference_object_type
         test_intersection_base
         test_intersection_different_type_base
         test_intersection_equal_sort
         test_intersection_equal_sort_true
         test_intersection_non_monotonic_non_unique
         test_intersection_nosort
         test_intersection_str_dates
         test_setops_mixed_freq_periods
         test_setops_preserve_object_dtype
         test_setops_sort_validation
         test_symmetric_difference, test_tuple_union_bug
         test_union_base, test_union_different_type_base
         test_union_name_preservation
         test_union_sort_other_incomparable
         test_union_sort_other_incomparable_true

class TestSetOpsSort:  [indexes/numeric/test_setops.py:151]
methods: test_union_sort_other_special, test_union_sort_special_true

class TestCustomDatetimeIndex:  [indexes/datetimes/test_setops.py:678]
methods: test_intersection_bug, test_intersection_dst_transition
         test_union

class IOArgs:  [pandas/io/common.py:92]
methods: —

def _get_combined_index(
    indexes: list[Index],
    intersect: bool = False,
    sort: bool | lib.NoDefault = False,
) -> Index:
    """
    Return the union or intersection of indexes.

    Parameters
    ----------
    indexes : list of Index or list objects
        When intersect=True, do not accept list of lists.
    intersect : bool, default False
        If True, calculate the intersection between indexes. Otherwise,
        calculate the union.
    sort : bool, default False
        Whether the result index should come out sorted or not. NoDefault
        used for deprecation of GH#57335

    Returns
    -------
    Index
    """
    # TODO: handle index names!
    indexes = _get_distinct_objs(indexes)
    if len(indexes) == 0:
        index: Index = default_index(0)
    elif len(indexes) == 1:
        index = indexes[0]
    elif intersect:
        index = indexes[0]
        for other in indexes[1:]:
            index = index.intersection(other)
    else:
        index = union_indexes(indexes, sort=sort if sort is lib.no_default else False)
        index = ensure_index(index)

    if sort and sort is not lib.no_default:
        index = safe_sort_index(index)
    return index

def union_indexes(indexes, sort: bool | lib.NoDefault = True) -> Index:
    """
    Return the union of indexes.

    The behavior of sort and names is not consistent.

    Parameters
    ----------
    indexes : list of Index or list objects
    sort : bool, default True
        Whether the result index should come out sorted or not. NoDefault
        used for deprecation of GH#57335.
    # ... truncated

def union_categoricals(
    to_union: Sequence[CategoricalIndex | Series | Categorical],
    sort_categories: bool = False,
    ignore_order: bool = False,
) -> Categorical:
    """
    # ... truncated

    def _union(self, other, sort):
        # We are called by `union`, which is responsible for this validation
        assert isinstance(other, type(self))
        assert self.dtype == other.dtype

        if self._can_range_setop(other):
            return self._range_union(other, sort=sort)

        if self._can_fast_union(other):
            result = self._fast_union(other, sort=sort)
            # in the case with sort=None, the _can_fast_union check ensures
            #  that result.freq == self.freq
            return result
        else:
            return super()._union(other, sort)._with_freq("infer")  # type: ignore[union-attr]

    def _union(self, other: Index, sort: bool | None) -> Index | ArrayLike | MultiIndex:
        """
        Specific union logic should go here. In subclasses, union behavior
        should be overwritten here rather than in `self.union`.

        Parameters
        ----------
        other : Index or array-like
        sort : False or None, default False
            Whether to sort the resulting index.

            * True : sort the result
    # ... truncated

    def check_sort_values_with_freq(self, idx):
        ordered = idx.sort_values()
        tm.assert_index_equal(ordered, idx)
        check_freq_ascending(ordered, idx, True)

        ordered = idx.sort_values(ascending=False)
        expected = idx[::-1]
        tm.assert_index_equal(ordered, expected)
        check_freq_ascending(ordered, idx, False)

        ordered, indexer = idx.sort_values(return_indexer=True)
        tm.assert_index_equal(ordered, idx)
        tm.assert_numpy_array_equal(indexer, np.array([0, 1, 2], dtype=np.intp))
        check_freq_ascending(ordered, idx, True)

        ordered, indexer = idx.sort_values(return_indexer=True, ascending=False)
        expected = idx[::-1]
        tm.assert_index_equal(ordered, expected)
        tm.assert_numpy_array_equal(indexer, np.array([2, 1, 0], dtype=np.intp))
        check_freq_ascending(ordered, idx, False)

def get_objs_combined_axis(
    objs,
    intersect: bool = False,
    axis: Axis = 0,
    sort: bool | lib.NoDefault = True,
) -> Index:
    """
    Extract combined index: return intersection or union (depending on the
    value of "intersect") of indexes on given axis, or None if all objects
    lack indexes (e.g. they are numpy arrays).

    Parameters
    ----------
    objs : list
        Series or DataFrame objects, may be mix of the two.
    intersect : bool, default False
        If True, calculate the intersection between indexes. Otherwise,
        calculate the union.
    axis : {0 or 'index', 1 or 'outer'}, default 0
        The axis to extract indexes from.
    sort : bool, default True
        Whether the result index should come out sorted or not. NoDefault
        use for deprecation in GH#57335.

    Returns
    -------
    Index
    """
    obs_idxes = [obj._get_axis(axis) for obj in objs]
    return _get_combined_index(obs_idxes, intersect=intersect, sort=sort)

    def _union(self, other: Index, sort: bool | None) -> Index:
        """
        Form the union of two Index objects and sorts if possible

        Parameters
        ----------
        other : Index or array-like

        sort : bool or None, default None
            Whether to sort (monotonically increasing) the resulting index.
            ``sort=None|True`` returns a ``RangeIndex`` if possible or a sorted
            ``Index`` with an int64 dtype if not.
    # ... truncated

def value_counts_internal(
    values,
    sort: bool = True,
    ascending: bool = False,
    normalize: bool = False,
    bins=None,
    dropna: bool = True,
) -> Series:
    from pandas import (
        DatetimeIndex,
        Index,
        Series,
    # ... truncated

def union_with_duplicates(
    lvals: ArrayLike | Index, rvals: ArrayLike | Index
) -> ArrayLike | Index:
    """
    # ... truncated

def _maybe_try_sort(result: Index | ArrayLike, sort: bool | None) -> Index | ArrayLike:
    if sort is not False:
        try:
            # error: Incompatible types in assignment (expression has type
            # "Union[ExtensionArray, ndarray[Any, Any], Index, Series,
            # Tuple[Union[Union[ExtensionArray, ndarray[Any, Any]], Index, Series],
            # ndarray[Any, Any]]]", variable has type "Union[Index,
            # Union[ExtensionArray, ndarray[Any, Any]]]")
            result = algos.safe_sort(result)  # type: ignore[assignment]
        except TypeError as err:
            if sort is True:
                raise
            warnings.warn(
                f"{err}, sort order is undefined for incomparable objects.",
                RuntimeWarning,
                stacklevel=find_stack_level(),
            )
    return result

    def _range_union(self, other, sort) -> Self:
        # Dispatch to RangeIndex union logic.
        left = self._as_range_index
        right = other._as_range_index
        res_i8 = left.union(right, sort=sort)
        return self._wrap_range_setop(other, res_i8)

def factorize(
    values,
    sort: bool = False,
    use_na_sentinel: bool = True,
    size_hint: int | None = None,
) -> tuple[np.ndarray, np.ndarray | Index]:
    """
    # ... truncated

    def union(self, other: Axes, sort: bool | None = None) -> Index:
        """
        Form the union of two Index objects.

        If the Index objects are incompatible, both Index objects will be
        cast to dtype('object') first.

        Parameters
        ----------
        other : Index or array-like
            Index or an array-like object containing elements to form the union
            with the original Index.
    # ... truncated

def sort(request):
    """
    Valid values for the 'sort' parameter used in the Index
    setops methods (intersection, union, etc.)

    Caution:
        Don't confuse this one with the "sort" fixture used
        for concat. That one has parameters [True, False].

        We can't combine them as sort=True is not permitted
        in the Index setops methods.
    """
    return request.param

    def _union(self, other, sort) -> MultiIndex:
        other, result_names = self._convert_can_do_setop(other)
        if other.has_duplicates:
            # This is only necessary if other has dupes,
            # otherwise difference is faster
            result = super(MultiIndex, self.rename(result_names))._union(
                other.rename(result_names), sort
            )

            if isinstance(result, MultiIndex):
                return result
            return MultiIndex.from_arrays(
                zip(*result, strict=True), sortorder=None, names=result_names
            )

        else:
            right_missing = other.difference(self, sort=False)
            if len(right_missing):
                result = self.append(right_missing)
            else:
                result = self._get_reconciled_name_object(other)

            if sort is not False:
                try:
                    result = result.sort_values()
                except TypeError:
                    if sort is True:
                        raise
                    warnings.warn(
                        "The values in the array are unorderable. "
                        "Pass `sort=False` to suppress this warning.",
                        RuntimeWarning,
                        stacklevel=find_stack_level(),
                    )
            return result

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

    def check_sort_values_without_freq(self, idx, expected):
        ordered = idx.sort_values(na_position="first")
        tm.assert_index_equal(ordered, expected)
        check_freq_nonmonotonic(ordered, idx)

        if not idx.isna().any():
            ordered = idx.sort_values()
            tm.assert_index_equal(ordered, expected)
            check_freq_nonmonotonic(ordered, idx)

        ordered = idx.sort_values(ascending=False)
        tm.assert_index_equal(ordered, expected[::-1])
        check_freq_nonmonotonic(ordered, idx)

        ordered, indexer = idx.sort_values(return_indexer=True, na_position="first")
        tm.assert_index_equal(ordered, expected)

        exp = np.array([0, 4, 3, 1, 2], dtype=np.intp)
        tm.assert_numpy_array_equal(indexer, exp)
        check_freq_nonmonotonic(ordered, idx)

        if not idx.isna().any():
            ordered, indexer = idx.sort_values(return_indexer=True)
            tm.assert_index_equal(ordered, expected)

            exp = np.array([0, 4, 3, 1, 2], dtype=np.intp)
            tm.assert_numpy_array_equal(indexer, exp)
            check_freq_nonmonotonic(ordered, idx)

        ordered, indexer = idx.sort_values(return_indexer=True, ascending=False)
        tm.assert_index_equal(ordered, expected[::-1])

        exp = np.array([2, 1, 3, 0, 4], dtype=np.intp)
        tm.assert_numpy_array_equal(indexer, exp)
        check_freq_nonmonotonic(ordered, idx)

def safe_sort(
    values: Index | ArrayLike,
    codes: npt.NDArray[np.intp] | None = None,
    use_na_sentinel: bool = True,
    assume_unique: bool = False,
    verify: bool = True,
) -> AnyArrayLike | tuple[AnyArrayLike, np.ndarray]:
    """
    # ... truncated

    def time_union_with_duplicates(self):
        self.left.union(self.right)

    def value_counts(
        self,
        normalize: bool = False,
        sort: bool = True,
        ascending: bool = False,
        bins=None,
        dropna: bool = True,
    ) -> Series | DataFrame:
        """
    # ... truncated

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

  {
   "cell_type": "markdown",
```
