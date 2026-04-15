# pandas-44 :: tacm

query: BUG: DTI/TDI/PI get_indexer_non_unique with incompatible dtype (#32650)

## selected nodes

- rank=1 layer=FILE tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=2 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py
- rank=3 layer=CLASS tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_indexing.py::TestGetIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_indexing.py
- rank=4 layer=CLASS tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py::TestGetIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_indexing.py
- rank=5 layer=CLASS tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/base_class/test_indexing.py::TestGetIndexerNonUnique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/base_class/test_indexing.py
- rank=6 layer=CLASS tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=7 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/object/test_indexing.py::TestGetIndexerNonUnique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/object/test_indexing.py
- rank=8 layer=CLASS tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_indexing.py::TestGetIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/categorical/test_indexing.py
- rank=9 layer=CLASS tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_interval_tree.py::TestIntervalTree file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_interval_tree.py
- rank=10 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/string/test_indexing.py::TestGetIndexerNonUnique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/string/test_indexing.py
- rank=11 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_is_unique.py::Foo file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_is_unique.py
- rank=12 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex.get_indexer_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=13 layer=FUNCTION tokens=315 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_pointwise file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=14 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_unique_sides file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=15 layer=FUNCTION tokens=368 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=16 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._setitem_with_indexer_frame_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=17 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._intersection_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=18 layer=FUNCTION tokens=395 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=19 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=20 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_strict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=21 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=22 layer=FUNCTION tokens=258 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_for file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=23 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=24 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=25 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._index_as_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=26 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique_sorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=27 layer=FUNCTION tokens=320 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_left_join_on_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=28 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=29 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py

## context

```text
file core/reshape/merge.py
imports: __future__, datetime, functools, types, typing, warnings, numpy, pandas
defines: _MergeOperation, _CrossMergeOperation, _OrderedMerge, _AsOfMerge, merge, _cross_merge, _groupby_and_merge, merge_ordered, _merger, merge_asof, _maybe_promote_to_rangeindex, get_join_indexers, get_join_indexers_non_unique, restore_dropped_levels_multijoin, _convert_to_multiindex, _asof_by_function, _get_multiindex_indexer, _get_empty_indexer, _get_no_sort_one_missing_indexer, _left_join_on_index, _factorize_keys, _convert_arrays_and_get_rizer_klass, _sort_labels, _get_join_keys, _should_fill, _any, _validate_operand, _items_overlap_with_suffix, renamer

file pandas/_testing/compat.py
imports: __future__, typing, pandas
defines: get_dtype, get_obj

class TestGetIndexer:  [indexes/interval/test_indexing.py:255]
methods: test_get_index_non_unique_non_monotonic
         test_get_indexer_categorical
         test_get_indexer_categorical_with_nans
         test_get_indexer_datetime
         test_get_indexer_errors
         test_get_indexer_interval_index
         test_get_indexer_length_one
         test_get_indexer_length_one_interval
         test_get_indexer_multiindex_with_intervals
         test_get_indexer_non_monotonic
         test_get_indexer_non_unique_right
         test_get_indexer_non_unique_with_int_and_float
         test_get_indexer_read_only
         test_get_indexer_with_int_and_float
         test_get_indexer_with_interval
         test_get_indexer_with_nans

class TestGetIndexer:  [indexes/period/test_indexing.py:362]
methods: test_get_indexer, test_get_indexer2
         test_get_indexer_mismatched_dtype
         test_get_indexer_mismatched_dtype_different_length
         test_get_indexer_mismatched_dtype_with_method
         test_get_indexer_non_unique

class TestGetIndexerNonUnique:  [indexes/base_class/test_indexing.py:36]
methods: test_get_indexer_non_unique_dtype_mismatch
         test_get_indexer_non_unique_int_index

class IntervalIndex(ExtensionIndex):  [core/indexes/interval.py:163]
methods: _convert_slice_indexer, _engine, _from_join_target
         _get_engine_target, _get_indexer
         _get_indexer_monotonic, _get_indexer_pointwise
         _get_indexer_unique_sides, _getitem_slice
         _index_as_unique, _intersection
         _intersection_non_unique, _intersection_unique
         _is_comparable_dtype, _maybe_cast_slice_bound
         _maybe_convert_i8, _multiindex
         _needs_i8_conversion, _searchsorted_monotonic
         _should_fallback_to_positional, from_arrays
         from_breaks, from_tuples, get_indexer_non_unique
         get_loc, inferred_type, is_monotonic_decreasing
         is_overlapping, is_unique, left, length
         memory_usage, mid, right, __contains__, __new__
         __reduce__

class TestGetIndexerNonUnique:  [indexes/object/test_indexing.py:76]
methods: test_get_indexer_non_unique_nas
         test_get_indexer_non_unique_np_nats

class TestGetIndexer:  [indexes/categorical/test_indexing.py:206]
methods: test_get_indexer_array, test_get_indexer_base
         test_get_indexer_method
         test_get_indexer_nans_in_index_and_target
         test_get_indexer_non_unique
         test_get_indexer_requires_unique
         test_get_indexer_same_categories_different_order
         test_get_indexer_same_categories_same_order

class TestIntervalTree:  [indexes/interval/test_interval_tree.py:46]
methods: test_construction_overflow, test_duplicates
         test_get_indexer, test_get_indexer_closed
         test_get_indexer_non_unique
         test_get_indexer_non_unique_overflow
         test_get_indexer_overflow
         test_inf_bound_infinite_recursion
         test_is_overlapping
         test_is_overlapping_endpoints
         test_is_overlapping_trivial

class TestGetIndexerNonUnique:  [indexes/string/test_indexing.py:108]
methods: test_get_indexer_non_unique_nas

class Foo:  [series/methods/test_is_unique.py:27]
methods: __init__, __ne__

    def get_indexer_non_unique(
        self, target: Axes
    ) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
    # ... truncated

    def _get_indexer_pointwise(
        self, target: Index
    ) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
        pointwise implementation for get_indexer and get_indexer_non_unique.
        """
        indexer, missing = [], []
        for i, key in enumerate(target):
            try:
                locs = self.get_loc(key)
                if isinstance(locs, slice):
                    # Only needed for get_indexer_non_unique
                    locs = np.arange(locs.start, locs.stop, locs.step, dtype="intp")
                elif lib.is_integer(locs):
                    locs = np.array(locs, ndmin=1)
                else:
                    # otherwise we have ndarray[bool]
                    locs = np.where(locs)[0]
            except KeyError:
                missing.append(i)
                locs = np.array([-1])
            except InvalidIndexError:
                # i.e. non-scalar key e.g. a tuple.
                # see test_append_different_columns_types_raises
                missing.append(i)
                locs = np.array([-1])

            indexer.append(locs)

        concatenated_indexer = np.concatenate(indexer)
        return ensure_platform_int(concatenated_indexer), ensure_platform_int(missing)

    def _get_indexer_unique_sides(self, target: IntervalIndex) -> npt.NDArray[np.intp]:
        """
        _get_indexer specialized to the case where both of our sides are unique.
        """
        # Caller is responsible for checking
        #  `self.left.is_unique and self.right.is_unique`

        left_indexer = self.left.get_indexer(target.left)
        right_indexer = self.right.get_indexer(target.right)
        indexer = np.where(left_indexer == right_indexer, left_indexer, -1)
        return indexer

    def _get_indexer_non_comparable(
        self, target: Index, method: str_t | None, unique: bool = True
    ) -> npt.NDArray[np.intp] | tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
        Called from get_indexer or get_indexer_non_unique when the target
        is of a non-comparable dtype.

        For get_indexer lookups with method=None, get_indexer is an _equality_
        check, so non-comparable dtypes mean we will always have no matches.

        For get_indexer lookups with a method, get_indexer is an _inequality_
        check, so non-comparable dtypes mean we will always raise TypeError.

        Parameters
        ----------
        target : Index
        method : str or None
        unique : bool, default True
            * True if called from get_indexer.
            * False if called from get_indexer_non_unique.

        Raises
        ------
        TypeError
            If doing an inequality check, i.e. method is not None.
        """
        if method is not None:
            other_dtype = _unpack_nested_dtype(target)
            raise TypeError(f"Cannot compare dtypes {self.dtype} and {other_dtype}")

        no_matches = -1 * np.ones(target.shape, dtype=np.intp)
        if unique:
            # This is for get_indexer
            return no_matches
        else:
            # This is for get_indexer_non_unique
            missing = np.arange(len(target), dtype=np.intp)
            return no_matches, missing

    def _setitem_with_indexer_frame_value(
        self, indexer, value: DataFrame, name: str
    ) -> None:
        ilocs = self._ensure_iterable_column_indexer(indexer[1])

        sub_indexer = list(indexer)
        pi = indexer[0]

        multiindex_indexer = isinstance(self.obj.columns, MultiIndex)

        unique_cols = value.columns.is_unique

    # ... truncated

    def _intersection_unique(self, other: IntervalIndex) -> IntervalIndex:
        """
        Used when the IntervalIndex does not have any common endpoint,
        no matter left or right.
        Return the intersection with another IntervalIndex.
        Parameters
        ----------
        other : IntervalIndex
        Returns
        -------
        IntervalIndex
        """
        # Note: this is much more performant than super()._intersection(other)
        lindexer = self.left.get_indexer(other.left)
        rindexer = self.right.get_indexer(other.right)

        match = (lindexer == rindexer) & (lindexer != -1)
        indexer = lindexer.take(match.nonzero()[0])
        indexer = unique(indexer)

        return self.take(indexer)

    def _get_indexer(
        self,
        target: Index,
        method: str | None = None,
        limit: int | None = None,
        tolerance: Any | None = None,
    ) -> npt.NDArray[np.intp]:
        if isinstance(target, IntervalIndex):
            # We only get here with not self.is_overlapping
            # -> at most one match per interval in target
            # want exact matches -> need both left/right to match, so defer to
            # left/right get_indexer, compare elementwise, equality -> match
            if self.left.is_unique and self.right.is_unique:
                indexer = self._get_indexer_unique_sides(target)
            else:
                indexer = self._get_indexer_pointwise(target)[0]

        elif not (is_object_dtype(target.dtype) or is_string_dtype(target.dtype)):
            # homogeneous scalar index
            # we should always have self._should_partial_index(target) here
            if self.is_monotonic_increasing:
                # GH#47614 - use searchsorted for O(n*log(m)) instead of
                # IntervalTree which scales poorly for large target arrays
                indexer = self._get_indexer_monotonic(target)
            else:
                target = self._maybe_convert_i8(target)
                indexer = self._engine.get_indexer(target.values)
        else:
            # heterogeneous scalar index: defer elementwise to get_loc
            # we should always have self._should_partial_index(target) here
            return self._get_indexer_pointwise(target)[0]

        return ensure_platform_int(indexer)

    def get_indexer_non_unique(
        self, target: Axes
    ) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
    # ... truncated

    def _get_indexer_strict(
        self, key: Axes, axis_name: str_t
    ) -> tuple[Index, np.ndarray]:
        """
        Analogue to get_indexer that raises if any elements are missing.
        """
        keyarr = key
        if not isinstance(keyarr, Index):
            keyarr = com.asarray_tuplesafe(keyarr)

        if self._index_as_unique:
            indexer = self.get_indexer_for(keyarr)  # pyright: ignore[reportArgumentType]
            keyarr = self.reindex(keyarr)[0]  # pyright: ignore[reportArgumentType]
        else:
            keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

        self._raise_if_missing(keyarr, indexer, axis_name)

        keyarr = self.take(indexer)
        if isinstance(key, Index):
            # GH 42790 - Preserve name from an Index
            keyarr.name = key.name
        if lib.is_np_dtype(keyarr.dtype, "mM") or isinstance(
            keyarr.dtype, DatetimeTZDtype
        ):
            # DTI/TDI.take can infer a freq in some cases when we dont want one
            if isinstance(key, list) or (
                isinstance(key, type(self))
                # "Index" has no attribute "freq"
                and key.freq is None  # type: ignore[attr-defined]
            ):
                # error: "Index" has no attribute "_with_freq"; maybe "_with_infer"?
                keyarr = keyarr._with_freq(None)  # type: ignore[attr-defined]

        return keyarr, indexer

    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

    def get_indexer_for(self, target: Axes) -> npt.NDArray[np.intp]:
        """
        Guaranteed return of an indexer even when non-unique.

        This dispatches to get_indexer or get_indexer_non_unique
        as appropriate.

        Parameters
        ----------
        target : Index
            An iterable containing the values to be used for computing indexer.

        Returns
        -------
        np.ndarray[np.intp]
            List of indices.

        See Also
        --------
        Index.get_indexer : Computes indexer and mask for new index given
            the current index.
        Index.get_non_unique : Returns indexer and masks for new index given
            the current index.

        Examples
        --------
        >>> idx = pd.Index([np.nan, "var1", np.nan])
        >>> idx.get_indexer_for([np.nan])
        array([0, 2])
        """
        if self._index_as_unique:
            return self.get_indexer(target)
        indexer, _ = self.get_indexer_non_unique(target)
        return indexer

    def time_get_indexer_mismatched_tz(self):
        # reached via e.g.
        #  ser = Series(range(len(dti)), index=dti)
        #  ser[dti2]
        self.dti.get_indexer(self.dti2)

    def time_get_loc_non_unique(self, dtype):
        self.non_unique.get_loc(self.key)

    def _index_as_unique(self) -> bool:
        """
        Whether we should treat this as unique for the sake of
        get_indexer vs get_indexer_non_unique.

        For IntervalIndex compat.
        """
        return self.is_unique

    def time_get_loc_non_unique_sorted(self, dtype):
        self.non_unique_sorted.get_loc(self.key)

def _left_join_on_index(
    left_ax: Index, right_ax: Index, join_keys: list[ArrayLike], sort: bool = False
) -> tuple[Index, npt.NDArray[np.intp] | None, npt.NDArray[np.intp]]:
    if isinstance(right_ax, MultiIndex):
        lkey, rkey = _get_multiindex_indexer(join_keys, right_ax, sort=sort)
    else:
        # error: Incompatible types in assignment (expression has type
        # "Union[Union[ExtensionArray, ndarray[Any, Any]], Index, Series]",
        # variable has type "ndarray[Any, dtype[signedinteger[Any]]]")
        lkey = join_keys[0]  # type: ignore[assignment]
        # error: Incompatible types in assignment (expression has type "Index",
        # variable has type "ndarray[Any, dtype[signedinteger[Any]]]")
        rkey = right_ax._values  # type: ignore[assignment]

    left_key, right_key, count = _factorize_keys(lkey, rkey, sort=sort)
    left_indexer, right_indexer = libjoin.left_outer_join(
        left_key, right_key, count, sort=sort
    )

    if sort or len(left_ax) != len(left_indexer):
        # if asked to sort or there are 1-to-many matches
        join_index = left_ax.take(left_indexer)
        return join_index, left_indexer, right_indexer

    # left frame preserves order & length of its index
    return left_ax, None, right_indexer

    def _intersection(self, other, sort: bool = False):
        """
        intersection specialized to the case with matching dtypes.
        """
        # For IntervalIndex we also know other.closed == self.closed
        if self.left.is_unique and self.right.is_unique:
            taken = self._intersection_unique(other)
        elif other.left.is_unique and other.right.is_unique and self.isna().sum() <= 1:
            # Swap other/self if other is unique and self does not have
            # multiple NaNs
            taken = other._intersection_unique(self)
        else:
            # duplicates
            taken = self._intersection_non_unique(other)

        if sort:
            taken = taken.sort_values()

        return taken

    def tdi(self, monotonic):
        tdi = timedelta_range("1 Day", periods=10)
        if monotonic == "decreasing":
            tdi = tdi[::-1]
        elif monotonic is None:
            taker = np.arange(10, dtype=np.intp)
            np.random.default_rng(2).shuffle(taker)
            tdi = tdi.take(taker)
        return tdi
```
