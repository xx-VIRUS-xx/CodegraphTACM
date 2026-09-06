# pandas-97 :: hybrid

query: BUG: TimedeltaIndex.union with sort=False (#30701)

## selected nodes

- rank=1 layer=FUNCTION tokens=1217 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=2 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=3 layer=FUNCTION tokens=871 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py::union_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py
- rank=4 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::timedelta_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=5 layer=FUNCTION tokens=435 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._fast_union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=6 layer=FUNCTION tokens=740 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=7 layer=FUNCTION tokens=383 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._union file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
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
        sort : bool or None, default None
            Whether to sort the resulting Index.

            * None : Sort the result, except when

              1. `self` and `other` are equal.
              2. `self` or `other` has length 0.
              3. Some values in `self` or `other` cannot be compared.
                 A RuntimeWarning is issued in this case.

            * False : do not sort the result.
            * True : Sort the result (which may raise TypeError).

        Returns
        -------
        Index
            Returns a new Index object with elements from both the original
            Index and the ``other`` Index.

            If either index contains duplicate entries, the result preserves
            duplicates up to the maximum number of occurrences in either index.

        See Also
        --------
        Index.unique : Return unique values in the index.
        Index.intersection : Form the intersection of two Index objects.
        Index.difference : Return a new Index with elements of index not in `other`.

        Examples
        --------
        Union matching dtypes

        >>> idx1 = pd.Index([1, 2, 3, 4])
        >>> idx2 = pd.Index([3, 4, 5, 6])
        >>> idx1.union(idx2)
        Index([1, 2, 3, 4, 5, 6], dtype='int64')

        Union mismatched dtypes

        >>> idx1 = pd.Index(["a", "b", "c", "d"])
        >>> idx2 = pd.Index([1, 2, 3, 4])
        >>> idx1.union(idx2)
        Index(['a', 'b', 'c', 'd', 1, 2, 3, 4], dtype='object')

        Union with duplicate values

        >>> idx1 = pd.Index([1, 2, 2, 3])
        >>> idx2 = pd.Index([3, 3, 4])
        >>> idx1.union(idx2)
        Index([1, 2, 2, 3, 3, 4], dtype='int64')

        MultiIndex case

        >>> idx1 = pd.MultiIndex.from_arrays(
        ...     [[1, 1, 2, 2], ["Red", "Blue", "Red", "Blue"]]
        ... )
        >>> idx1
        MultiIndex([(1,  'Red'),
            (1, 'Blue'),
            (2,  'Red'),
            (2, 'Blue')],
           )
        >>> idx2 = pd.MultiIndex.from_arrays(
        ...     [[3, 3, 2, 2], ["Red", "Green", "Red", "Green"]]
        ... )
        >>> idx2
        MultiIndex([(3,   'Red'),
            (3, 'Green'),
            (2,   'Red'),
            (2, 'Green')],
           )
        >>> idx1.union(idx2)
        MultiIndex([(1,  'Blue'),
            (1,   'Red'),
            (2,  'Blue'),
            (2, 'Green'),
            (2,   'Red'),
            (3, 'Green'),
            (3,   'Red')],
           )
        >>> idx1.union(idx2, sort=False)
        MultiIndex([(1,   'Red'),
            (1,  'Blue'),
            (2,   'Red'),
            (2,  'Blue'),
            (3,   'Red'),
            (3, 'Green'),
            (2, 'Green')],
           )
        """
        self._validate_sort_keyword(sort)
        self._assert_can_do_setop(other)
        other, result_name = self._convert_can_do_setop(other)

        if self.dtype != other.dtype:
            if (
                isinstance(self, ABCMultiIndex)
                and not is_object_dtype(_unpack_nested_dtype(other))
                and len(other) > 0
            ):
                raise NotImplementedError(
                    "Can only union MultiIndex with MultiIndex or Index of tuples, "
                    "try mi.to_flat_index().union(other) instead."
                )
            self, other = self._dti_setop_align_tzs(other, "union")

            dtype = self._find_common_type_compat(other)
            left = self.astype(dtype, copy=False)
            right = other.astype(dtype, copy=False)
            return left.union(right, sort=sort)

        elif not len(other) or self.equals(other):
            # NB: whether this (and the `if not len(self)` check below) come before
            #  or after the dtype equality check above affects the returned dtype
            result = self._get_reconciled_name_object(other)
            if sort is True:
                return result.sort_values()
            return result

        elif not len(self):
            result = other._get_reconciled_name_object(self)
            if sort is True:
                return result.sort_values()
            return result

        union_result = self._union(other, sort=sort)

        return self._wrap_setop_result(other, union_result)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py::union_indexes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/api.py]
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

    Returns
    -------
    Index
    """
    if len(indexes) == 0:
        raise AssertionError("Must have at least 1 Index to union")
    if len(indexes) == 1:
        result = indexes[0]
        if isinstance(result, list):
            if not sort or sort is lib.no_default:
                result = Index(result)
            else:
                result = Index(sorted(result))
        return result

    indexes, kind = _sanitize_and_check(indexes)

    if kind == "special":
        result = indexes[0]

        num_dtis = 0
        num_dti_tzs = 0
        for idx in indexes:
            if isinstance(idx, DatetimeIndex):
                num_dtis += 1
                if idx.tz is not None:
                    num_dti_tzs += 1
        if num_dti_tzs not in [0, num_dtis]:
            # TODO: this behavior is not tested (so may not be desired),
            #  but is kept in order to keep behavior the same when
            #  deprecating union_many
            # test_frame_from_dict_with_mixed_indexes
            raise TypeError("Cannot join tz-naive with tz-aware DatetimeIndex")

        if num_dtis == len(indexes):
            if sort is lib.no_default:
                sort = True
            result = indexes[0]

        elif num_dtis > 1:
            # If we have mixed timezones, our casting behavior may depend on
            #  the order of indexes, which we don't want.
            sort = False

            # TODO: what about Categorical[dt64]?
            # test_frame_from_dict_with_mixed_indexes
            indexes = [x.astype(object, copy=False) for x in indexes]
            result = indexes[0]

        for other in indexes[1:]:
            result = result.union(other, sort=None if sort else False)
        return result

    elif kind == "array":
        if not all_indexes_same(indexes):
            dtype = find_common_type([idx.dtype for idx in indexes])
            inds = [ind.astype(dtype, copy=False) for ind in indexes]
            index = inds[0].unique()
            other = inds[1].append(inds[2:])
            diff = other[index.get_indexer_for(other) == -1]
            if len(diff):
                index = index.append(diff.unique())
            if sort:
                index = index.sort_values()
        else:
            index = indexes[0]

        name = get_unanimous_names(*indexes)[0]
        if name != index.name:
            index = index.rename(name)
        return index
    elif kind == "list":
        dtypes = [idx.dtype for idx in indexes if isinstance(idx, Index)]
        if dtypes:
            dtype = find_common_type(dtypes)
        else:
            dtype = None
        all_lists = (idx.tolist() if isinstance(idx, Index) else idx for idx in indexes)
        return Index(
            lib.fast_unique_multiple_list_gen(all_lists, sort=bool(sort)),
            dtype=dtype,
        )
    else:
        raise ValueError(f"{kind=} must be 'special', 'array' or 'list'.")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._fast_union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _fast_union(self, other: Self, sort=None) -> Self:
        # Caller is responsible for ensuring self and other are non-empty

        # to make our life easier, "sort" the two ranges
        if self[0] <= other[0]:
            left, right = self, other
        elif sort is False:
            # TDIs are not in the "correct" order and we don't want
            #  to sort but want to remove overlaps
            left, right = self, other
            left_start = left[0]
            loc = right.searchsorted(left_start, side="left")
            right_chunk = right._values[:loc]
            dates = concat_compat((left._values, right_chunk))
            result = type(self)._simple_new(dates, name=self.name)
            return result
        else:
            left, right = other, self

        left_end = left[-1]
        right_end = right[-1]

        # concatenate
        if left_end < right_end:
            loc = right.searchsorted(left_end, side="right")
            right_chunk = right._values[loc:]
            dates = concat_compat([left._values, right_chunk])
            # The can_fast_union check ensures that the result.freq
            #  should match self.freq
            assert isinstance(dates, type(self._data))
            # error: Item "ExtensionArray" of "ExtensionArray |
            # ndarray[Any, Any]" has no attribute "_freq"
            assert dates._freq == self.freq  # type: ignore[union-attr]
            result = type(self)._simple_new(dates)
            return result
        else:
            return left

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._union [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
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
```
