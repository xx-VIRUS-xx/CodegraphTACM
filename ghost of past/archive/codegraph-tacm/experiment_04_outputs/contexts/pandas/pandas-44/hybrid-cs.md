# pandas-44 :: hybrid-cs

query: BUG: DTI/TDI/PI get_indexer_non_unique with incompatible dtype (#32650)

## selected nodes

- rank=1 layer=FUNCTION tokens=412 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=2 layer=FUNCTION tokens=948 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex.get_indexer_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=3 layer=FUNCTION tokens=1044 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=4 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer_dups file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=5 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._left_indexer_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=6 layer=FUNCTION tokens=419 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_strict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=7 layer=FUNCTION tokens=440 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=8 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=9 layer=FUNCTION tokens=362 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_pointwise file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=10 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._index_as_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex.get_indexer_non_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
    def get_indexer_non_unique(
        self, target: Axes
    ) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
        Compute indexer and mask for new index given the current index.

        The indexer should be then used as an input to ndarray.take to align the
        current data to the new index.

        Parameters
        ----------
        target : IntervalIndex or list of Intervals
            An iterable containing the values to be used for computing indexer.

        Returns
        -------
        indexer : np.ndarray[np.intp]
            Integers from 0 to n - 1 indicating that the index at these
            positions matches the corresponding target values. Missing values
            in the target are marked by -1.
        missing : np.ndarray[np.intp]
            An indexer into the target of the values not found.
            These correspond to the -1 in the indexer array.

        See Also
        --------
        Index.get_indexer : Computes indexer and mask for new index given
            the current index.
        Index.get_indexer_for : Returns an indexer even when non-unique.

        Examples
        --------
        >>> index = pd.Index(["c", "b", "a", "b", "b"])
        >>> index.get_indexer_non_unique(["b", "b"])
        (array([1, 3, 4, 1, 3, 4]), array([], dtype=int64))

        In the example below there are no matched values.

        >>> index = pd.Index(["c", "b", "a", "b", "b"])
        >>> index.get_indexer_non_unique(["q", "r", "t"])
        (array([-1, -1, -1]), array([0, 1, 2]))

        For this reason, the returned ``indexer`` contains only integers equal to -1.
        It demonstrates that there's no match between the index and the ``target``
        values at these positions. The mask [0, 1, 2] in the return value shows that
        the first, second, and third elements are missing.

        Notice that the return value is a tuple contains two items. In the example
        below the first item is an array of locations in ``index``. The second
        item is a mask shows that the first and third elements are missing.

        >>> index = pd.Index(["c", "b", "a", "b", "b"])
        >>> index.get_indexer_non_unique(["f", "b", "s"])
        (array([-1,  1,  3,  4, -1]), array([0, 2]))
        """
        target = ensure_index(target)

        if not self._should_compare(target) and not self._should_partial_index(target):
            # e.g. IntervalIndex with different closed or incompatible subtype
            #  -> no matches
            return self._get_indexer_non_comparable(target, None, unique=False)

        elif isinstance(target, IntervalIndex):
            if self.left.is_unique and self.right.is_unique:
                # fastpath available even if we don't have self._index_as_unique
                indexer = self._get_indexer_unique_sides(target)
                missing = (indexer == -1).nonzero()[0]
            else:
                return self._get_indexer_pointwise(target)

        elif is_object_dtype(target.dtype) or not self._should_partial_index(target):
            # target might contain intervals: defer elementwise to get_loc
            return self._get_indexer_pointwise(target)

        else:
            # Note: this case behaves differently from other Index subclasses
            #  because IntervalIndex does partial-int indexing
            target = self._maybe_convert_i8(target)
            indexer, missing = self._engine.get_indexer_non_unique(target.values)  # type: ignore[union-attr]

        return ensure_platform_int(indexer), ensure_platform_int(missing)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_non_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def get_indexer_non_unique(
        self, target: Axes
    ) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
        Compute indexer and mask for new index given the current index.

        The indexer should be then used as an input to ndarray.take to align the
        current data to the new index.

        Parameters
        ----------
        target : Index
            An iterable containing the values to be used for computing indexer.

        Returns
        -------
        indexer : np.ndarray[np.intp]
            Integers from 0 to n - 1 indicating that the index at these
            positions matches the corresponding target values. Missing values
            in the target are marked by -1.
        missing : np.ndarray[np.intp]
            An indexer into the target of the values not found.
            These correspond to the -1 in the indexer array.

        See Also
        --------
        Index.get_indexer : Computes indexer and mask for new index given
            the current index.
        Index.get_indexer_for : Returns an indexer even when non-unique.

        Examples
        --------
        >>> index = pd.Index(["c", "b", "a", "b", "b"])
        >>> index.get_indexer_non_unique(["b", "b"])
        (array([1, 3, 4, 1, 3, 4]), array([], dtype=int64))

        In the example below there are no matched values.

        >>> index = pd.Index(["c", "b", "a", "b", "b"])
        >>> index.get_indexer_non_unique(["q", "r", "t"])
        (array([-1, -1, -1]), array([0, 1, 2]))

        For this reason, the returned ``indexer`` contains only integers equal to -1.
        It demonstrates that there's no match between the index and the ``target``
        values at these positions. The mask [0, 1, 2] in the return value shows that
        the first, second, and third elements are missing.

        Notice that the return value is a tuple contains two items. In the example
        below the first item is an array of locations in ``index``. The second
        item is a mask shows that the first and third elements are missing.

        >>> index = pd.Index(["c", "b", "a", "b", "b"])
        >>> index.get_indexer_non_unique(["f", "b", "s"])
        (array([-1,  1,  3,  4, -1]), array([0, 2]))
        """
        target = self._maybe_cast_listlike_indexer(target)

        if not self._should_compare(target) and not self._should_partial_index(target):
            # _should_partial_index e.g. IntervalIndex with numeric scalars
            #  that can be matched to Interval scalars.
            return self._get_indexer_non_comparable(target, method=None, unique=False)

        pself, ptarget = self._maybe_downcast_for_indexing(target)
        if pself is not self or ptarget is not target:
            return pself.get_indexer_non_unique(ptarget)

        if self.dtype != target.dtype:
            # TODO: if object, could use infer_dtype to preempt costly
            #  conversion if still non-comparable?
            dtype = self._find_common_type_compat(target)

            this = self.astype(dtype, copy=False)
            that = target.astype(dtype, copy=False)
            return this.get_indexer_non_unique(that)

        # TODO: get_indexer has fastpaths for both Categorical-self and
        #  Categorical-target. Can we do something similar here?

        # Note: _maybe_downcast_for_indexing ensures we never get here
        #  with MultiIndex self and non-Multi target
        if self._is_multi and target._is_multi:
            engine = self._engine
            # Item "IndexEngine" of "Union[IndexEngine, ExtensionEngine]" has
            # no attribute "_extract_level_codes"
            tgt_values = engine._extract_level_codes(target)  # type: ignore[union-attr]
        else:
            tgt_values = target._get_engine_target()

        indexer, missing = self._engine.get_indexer_non_unique(tgt_values)  # pyright: ignore[reportArgumentType]
        return ensure_platform_int(indexer), ensure_platform_int(missing)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer_dups [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_dups(self, dtype, monotonic):
        self.data.get_indexer_for(self.indexer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._left_indexer_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _left_indexer_unique(self, other: Self) -> npt.NDArray[np.intp]:
        # Caller is responsible for ensuring other.dtype == self.dtype
        sv = self._get_join_target()
        ov = other._get_join_target()
        # similar but not identical to ov.searchsorted(sv)
        return libjoin.left_join_indexer_unique(sv, ov)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_strict [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer(self, dtype, monotonic):
        self.data.get_indexer(self.indexer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_pointwise [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._index_as_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _index_as_unique(self) -> bool:
        """
        Whether we should treat this as unique for the sake of
        get_indexer vs get_indexer_non_unique.

        For IntervalIndex compat.
        """
        return self.is_unique
```
