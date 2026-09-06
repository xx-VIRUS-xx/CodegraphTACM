# pandas-97 :: tacm-full

query: BUG: TimedeltaIndex.union with sort=False (#30701)

## selected nodes

- rank=1 layer=FUNCTION tokens=1647 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::union_categoricals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py
- rank=2 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=3 layer=FUNCTION tokens=740 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=4 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::_maybe_try_sort file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=5 layer=FUNCTION tokens=895 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=6 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._range_union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=7 layer=FUNCTION tokens=138 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py::sort file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::union_categoricals [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py]
def union_categoricals(
    to_union: Sequence[CategoricalIndex | Series | Categorical],
    sort_categories: bool = False,
    ignore_order: bool = False,
) -> Categorical:
    """
    Combine list-like of Categorical-like, unioning categories.

    All categories must have the same dtype.

    Parameters
    ----------
    to_union : list-like
        Categorical, CategoricalIndex, or Series with dtype='category'.
    sort_categories : bool, default False
        If true, resulting categories will be lexsorted, otherwise
        they will be ordered as they appear in the data.
    ignore_order : bool, default False
        If true, the ordered attribute of the Categoricals will be ignored.
        Results in an unordered categorical.

    Returns
    -------
    Categorical
        The union of categories being combined.

    Raises
    ------
    TypeError
        - all inputs do not have the same dtype
        - all inputs do not have the same ordered property
        - all inputs are ordered and their categories are not identical
        - sort_categories=True and Categoricals are ordered
    ValueError
        Empty list of categoricals passed

    See Also
    --------
    CategoricalDtype : Type for categorical data with the categories and orderedness.
    Categorical : Represent a categorical variable in classic R / S-plus fashion.

    Notes
    -----
    To learn more about categories, see `link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#unioning>`__

    Examples
    --------
    If you want to combine categoricals that do not necessarily have
    the same categories, `union_categoricals` will combine a list-like
    of categoricals. The new categories will be the union of the
    categories being combined.

    >>> a = pd.Categorical(["b", "c"])
    >>> b = pd.Categorical(["a", "b"])
    >>> pd.api.types.union_categoricals([a, b])
    ['b', 'c', 'a', 'b']
    Categories (3, str): ['b', 'c', 'a']

    By default, the resulting categories will be ordered as they appear
    in the `categories` of the data. If you want the categories to be
    lexsorted, use `sort_categories=True` argument.

    >>> pd.api.types.union_categoricals([a, b], sort_categories=True)
    ['b', 'c', 'a', 'b']
    Categories (3, str): ['a', 'b', 'c']

    `union_categoricals` also works with the case of combining two
    categoricals of the same categories and order information (e.g. what
    you could also `append` for).

    >>> a = pd.Categorical(["a", "b"], ordered=True)
    >>> b = pd.Categorical(["a", "b", "a"], ordered=True)
    >>> pd.api.types.union_categoricals([a, b])
    ['a', 'b', 'a', 'b', 'a']
    Categories (2, str): ['a' < 'b']

    Raises `TypeError` because the categories are ordered and not identical.

    >>> a = pd.Categorical(["a", "b"], ordered=True)
    >>> b = pd.Categorical(["a", "b", "c"], ordered=True)
    >>> pd.api.types.union_categoricals([a, b])
    Traceback (most recent call last):
        ...
    TypeError: to union ordered Categoricals, all categories must be the same

    Ordered categoricals with different categories or orderings can be
    combined by using the `ignore_order=True` argument.

    >>> a = pd.Categorical(["a", "b", "c"], ordered=True)
    >>> b = pd.Categorical(["c", "b", "a"], ordered=True)
    >>> pd.api.types.union_categoricals([a, b], ignore_order=True)
    ['a', 'b', 'c', 'c', 'b', 'a']
    Categories (3, str): ['a', 'b', 'c']

    `union_categoricals` also works with a `CategoricalIndex`, or `Series`
    containing categorical data, but note that the resulting array will
    always be a plain `Categorical`

    >>> a = pd.Series(["b", "c"], dtype="category")
    >>> b = pd.Series(["a", "b"], dtype="category")
    >>> pd.api.types.union_categoricals([a, b])
    ['b', 'c', 'a', 'b']
    Categories (3, str): ['b', 'c', 'a']
    """
    from pandas import Categorical
    from pandas.core.arrays.categorical import recode_for_categories

    if len(to_union) == 0:
        raise ValueError("No Categoricals to union")

    def _maybe_unwrap(
        x: CategoricalIndex | Series | Categorical,
    ) -> Categorical:
        if isinstance(x, (ABCCategoricalIndex, ABCSeries)):
            return x._values
        elif isinstance(x, Categorical):
            return x
        else:
            raise TypeError("all components to combine must be Categorical")

    to_union = cast("list[Categorical]", [_maybe_unwrap(x) for x in to_union])
    first = to_union[0]

    if not lib.dtypes_all_equal([obj.categories.dtype for obj in to_union]):
        raise TypeError("dtype of categories must be the same")

    ordered: bool | None = False
    if all(first._categories_match_up_to_permutation(other) for other in to_union[1:]):
        # identical categories - fastpath
        categories = first.categories
        ordered = first.ordered

        all_codes = [first._encode_with_my_categories(x)._codes for x in to_union]
        new_codes = np.concatenate(all_codes)

        if sort_categories and not ignore_order and ordered:
            raise TypeError("Cannot use sort_categories=True with ordered Categoricals")

        if sort_categories and not categories.is_monotonic_increasing:
            categories = categories.sort_values()
            indexer = categories.get_indexer(first.categories)

            from pandas.core.algorithms import take_nd

            new_codes = take_nd(indexer, new_codes, fill_value=-1)
    elif ignore_order or all(not c.ordered for c in to_union):
        # different categories - union and recode
        cats = first.categories.append([c.categories for c in to_union[1:]])
        categories = cats.unique()
        if sort_categories:
            categories = categories.sort_values()

        all_codes = [
            recode_for_categories(c.codes, c.categories, categories, copy=False)
            for c in to_union
        ]
        new_codes = np.concatenate(all_codes)
    else:
        # ordered - to show a proper error message
        if all(c.ordered for c in to_union):
            msg = "to union ordered Categoricals, all categories must be the same"
            raise TypeError(msg)
        raise TypeError("Categorical.ordered must be the same")

    if ignore_order:
        ordered = False

    dtype = CategoricalDtype(categories=categories, ordered=ordered)
    return Categorical._simple_new(new_codes, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
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
            * False : do not sort the result.
            * None : sort the result, except when `self` and `other` are equal
              or when the values cannot be compared.

        Returns
        -------
        Index, MultiIndex, or ArrayLike
        """
        lvals = self._values
        rvals = other._values

        if (
            sort in (None, True)
            and (self.is_unique or other.is_unique)
            and self._can_use_libjoin
            and other._can_use_libjoin
        ):
            # Both are monotonic and at least one is unique, so can use outer join
            #  (actually don't need either unique, but without this restriction
            #  test_union_same_value_duplicated_in_both fails)
            try:
                return self._outer_indexer(other)[0]  # pyright: ignore[reportArgumentType]
            except TypeError:
                # incomparable objects; should only be for object dtype
                value_list = list(lvals)

                # worth making this faster? a very unusual case
                value_set = set(lvals)
                value_list.extend(x for x in rvals if x not in value_set)
                # If objects are unorderable, we must have object dtype.
                return np.array(value_list, dtype=object)

        elif not other.is_unique:
            # other has duplicates
            result_dups = algos.union_with_duplicates(self, other)
            return _maybe_try_sort(result_dups, sort)

        # The rest of this method is analogous to Index._intersection_via_get_indexer

        # Self may have duplicates; other already checked as unique
        # find indexes of things in "other" that are not in "self"
        if self._index_as_unique:
            indexer = self.get_indexer(other)
            missing = (indexer == -1).nonzero()[0]
        else:
            missing = algos.unique1d(self.get_indexer_non_unique(other)[1])

        result: Index | MultiIndex | ArrayLike
        if self._is_multi:
            # Preserve MultiIndex to avoid losing dtypes
            result = self.append(other.take(missing))

        elif len(missing) > 0:
            other_diff = rvals.take(missing)
            result = concat_compat((lvals, other_diff))
        else:
            result = lvals

        result = _maybe_try_sort(result, sort)

        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::_maybe_try_sort [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py]
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
            ``sort=False`` can return a ``RangeIndex`` if self is monotonically
            increasing and other is fully contained in self. Otherwise, returns
            an unsorted ``Index`` with an int64 dtype.

        Returns
        -------
        union : Index
        """
        if isinstance(other, RangeIndex):
            if sort in (None, True) or (
                sort is False and self.step > 0 and self._range_in_self(other._range)
            ):
                # GH 47557: Can still return a RangeIndex
                # if other range in self and sort=False
                start_s, step_s = self.start, self.step
                end_s = self.start + self.step * (len(self) - 1)
                start_o, step_o = other.start, other.step
                end_o = other.start + other.step * (len(other) - 1)
                if self.step < 0:
                    start_s, step_s, end_s = end_s, -step_s, start_s
                if other.step < 0:
                    start_o, step_o, end_o = end_o, -step_o, start_o
                if len(self) == 1 and len(other) == 1:
                    step_s = step_o = abs(self.start - other.start)
                elif len(self) == 1:
                    step_s = step_o
                elif len(other) == 1:
                    step_o = step_s
                start_r = min(start_s, start_o)
                end_r = max(end_s, end_o)
                if step_o == step_s:
                    if (
                        (start_s - start_o) % step_s == 0
                        and (start_s - end_o) <= step_s
                        and (start_o - end_s) <= step_s
                    ):
                        return type(self)(start_r, end_r + step_s, step_s)
                    if (
                        (step_s % 2 == 0)
                        and (abs(start_s - start_o) == step_s / 2)
                        and (abs(end_s - end_o) == step_s / 2)
                    ):
                        # e.g. range(0, 10, 2) and range(1, 11, 2)
                        #  but not range(0, 20, 4) and range(1, 21, 4) GH#44019
                        return type(self)(start_r, end_r + step_s / 2, step_s / 2)  # type: ignore[arg-type]

                elif step_o % step_s == 0:
                    if (
                        (start_o - start_s) % step_s == 0
                        and (start_o + step_s >= start_s)
                        and (end_o - step_s <= end_s)
                    ):
                        return type(self)(start_r, end_r + step_s, step_s)
                elif step_s % step_o == 0:
                    if (
                        (start_s - start_o) % step_o == 0
                        and (start_s + step_o >= start_o)
                        and (end_s - step_o <= end_o)
                    ):
                        return type(self)(start_r, end_r + step_o, step_o)

        return super()._union(other, sort=sort)  # type: ignore[return-value]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._range_union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _range_union(self, other, sort) -> Self:
        # Dispatch to RangeIndex union logic.
        left = self._as_range_index
        right = other._as_range_index
        res_i8 = left.union(right, sort=sort)
        return self._wrap_range_setop(other, res_i8)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py::sort [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py]
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
```
