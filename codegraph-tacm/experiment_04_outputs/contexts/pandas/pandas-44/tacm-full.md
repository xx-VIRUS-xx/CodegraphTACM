# pandas-44 :: tacm-full

query: BUG: DTI/TDI/PI get_indexer_non_unique with incompatible dtype (#32650)

## selected nodes

- rank=1 layer=FUNCTION tokens=412 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=2 layer=FUNCTION tokens=584 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._setitem_with_indexer_frame_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=3 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=4 layer=FUNCTION tokens=419 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_strict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=5 layer=FUNCTION tokens=299 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_for file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=6 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._index_as_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=7 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=8 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=9 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique_sorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=10 layer=FUNCTION tokens=1044 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=11 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=12 layer=FUNCTION tokens=362 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_pointwise file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=13 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_unique_sides file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=14 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::CategoricalIndexIndexing.time_get_indexer_list file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._setitem_with_indexer_frame_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _setitem_with_indexer_frame_value(
        self, indexer, value: DataFrame, name: str
    ) -> None:
        ilocs = self._ensure_iterable_column_indexer(indexer[1])

        sub_indexer = list(indexer)
        pi = indexer[0]

        multiindex_indexer = isinstance(self.obj.columns, MultiIndex)

        unique_cols = value.columns.is_unique

        # We do not want to align the value in case of iloc GH#37728
        if name == "iloc":
            for i, loc in enumerate(ilocs):
                val = value.iloc[:, i]
                self._setitem_single_column(loc, val, pi)

        elif not unique_cols and value.columns.equals(self.obj.columns):
            # We assume we are already aligned, see
            # test_iloc_setitem_frame_duplicate_columns_multiple_blocks
            for loc in ilocs:
                item = self.obj.columns[loc]
                if item in value:
                    sub_indexer[1] = item
                    val = self._align_series(
                        tuple(sub_indexer),
                        value.iloc[:, loc],
                        multiindex_indexer,
                    )
                else:
                    val = np.nan

                self._setitem_single_column(loc, val, pi)

        elif not unique_cols:
            raise ValueError("Setting with non-unique columns is not allowed.")

        else:
            for loc in ilocs:
                item = self.obj.columns[loc]
                if item in value:
                    sub_indexer[1] = item
                    ser = value[item]
                    val = self._align_series(
                        tuple(sub_indexer),
                        ser,
                        multiindex_indexer,
                    )
                    # If _align_series did not need to reindex, pass the
                    # original Series so that _setitem_single_column can
                    # preserve CoW ref tracking through isetitem.
                    if val is ser._values:
                        val = ser
                else:
                    val = np.nan

                self._setitem_single_column(loc, val, pi)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_for [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._index_as_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _index_as_unique(self) -> bool:
        """
        Whether we should treat this as unique for the sake of
        get_indexer vs get_indexer_non_unique.

        For IntervalIndex compat.
        """
        return self.is_unique

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_mismatched_tz(self):
        # reached via e.g.
        #  ser = Series(range(len(dti)), index=dti)
        #  ser[dti2]
        self.dti.get_indexer(self.dti2)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def time_get_loc_non_unique(self, dtype):
        self.non_unique.get_loc(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique_sorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def time_get_loc_non_unique_sorted(self, dtype):
        self.non_unique_sorted.get_loc(self.key)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py]
    def tdi(self, monotonic):
        tdi = timedelta_range("1 Day", periods=10)
        if monotonic == "decreasing":
            tdi = tdi[::-1]
        elif monotonic is None:
            taker = np.arange(10, dtype=np.intp)
            np.random.default_rng(2).shuffle(taker)
            tdi = tdi.take(taker)
        return tdi

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_unique_sides [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::CategoricalIndexIndexing.time_get_indexer_list [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_list(self, index):
        self.data_unique.get_indexer(self.cat_list)
```
