# pandas-35 :: codesearch

query: BUG: create new MI from MultiIndex._get_level_values (#33134)

## selected nodes

- rank=1 layer=FUNCTION tokens=739 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.get_level_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=2 layer=FUNCTION tokens=314 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_level_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=3 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_level_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=4 layer=FUNCTION tokens=260 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._drop_from_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=5 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.read_multi_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=6 layer=FUNCTION tokens=728 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=7 layer=FUNCTION tokens=1264 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_level_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=8 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py::BaseGrouper.levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py
- rank=9 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py::TestDataFrameQueryWithMultiIndex.to_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.get_level_values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def get_level_values(self, level) -> Index:
        """
        Return vector of label values for requested level.

        Length of returned vector is equal to the length of the index.
        The `get_level_values` method is a crucial utility for extracting
        specific level values from a `MultiIndex`. This function is particularly
        useful when working with multi-level data, allowing you to isolate
        and manipulate individual levels without having to deal with the
        complexity of the entire `MultiIndex` structure. It seamlessly handles
        both integer and string-based level access, providing flexibility in
        how you can interact with the data. Additionally, this method ensures
        that the returned `Index` maintains the integrity of the original data,
        even when missing values are present, by appropriately casting the
        result to a suitable data type.

        Parameters
        ----------
        level : int or str
            ``level`` is either the integer position of the level in the
            MultiIndex, or the name of the level.

        Returns
        -------
        Index
            Values is a level of this MultiIndex converted to
            a single :class:`Index` (or subclass thereof).

        See Also
        --------
        MultiIndex : A multi-level, or hierarchical, index object for pandas objects.
        Index : Immutable sequence used for indexing and alignment.
        MultiIndex.remove_unused_levels : Create new MultiIndex from current that
            removes unused levels.

        Notes
        -----
        If the level contains missing values, the result may be casted to
        ``float`` with missing values specified as ``NaN``. This is because
        the level is converted to a regular ``Index``.

        Examples
        --------
        Create a MultiIndex:

        >>> mi = pd.MultiIndex.from_arrays((list("abc"), list("def")))
        >>> mi.names = ["level_1", "level_2"]

        Get level values by supplying level as either integer or name:

        >>> mi.get_level_values(0)
        Index(['a', 'b', 'c'], dtype='str', name='level_1')
        >>> mi.get_level_values("level_2")
        Index(['d', 'e', 'f'], dtype='str', name='level_2')

        If a level contains missing values, the return type of the level
        may be cast to ``float``.

        >>> pd.MultiIndex.from_arrays([[1, None, 2], [3, 4, 5]]).dtypes
        level_0    int64
        level_1    int64
        dtype: object
        >>> pd.MultiIndex.from_arrays([[1, None, 2], [3, 4, 5]]).get_level_values(0)
        Index([1.0, nan, 2.0], dtype='float64')
        """
        level = self._get_level_number(level)
        values = self._get_level_values(level)
        return values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_level_values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _get_level_values(self, level: Level) -> Index:
        """
        Return an Index of values for requested level.

        This is primarily useful to get an individual level of values from a
        MultiIndex, but is provided on Index as well for compatibility.

        Parameters
        ----------
        level : int or str
            It is either the integer position or the name of the level.

        Returns
        -------
        Index
            Calling object, as there is only one level in the Index.

        See Also
        --------
        MultiIndex.get_level_values : Get values for a level of a MultiIndex.

        Notes
        -----
        For Index, level should be 0, since there are no multiple levels.

        Examples
        --------
        >>> idx = pd.Index(list("abc"))
        >>> idx
        Index(['a', 'b', 'c'], dtype='str')

        Get level values by supplying `level` as integer:

        >>> idx.get_level_values(0)
        Index(['a', 'b', 'c'], dtype='str')
        """
        self._validate_index_level(level)
        return self

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_level_values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def _get_level_values(self, level: int, unique: bool = False) -> Index:  # type: ignore[override]
        """
        Return vector of label values for requested level,
        equal to the length of the index

        **this is an internal method**

        Parameters
        ----------
        level : int
        unique : bool, default False
            if True, drop duplicated values

        Returns
        -------
        Index
        """
        lev = self.levels[level]
        level_codes = self.codes[level]
        name = self._names[level]
        if unique:
            level_codes = algos.unique(level_codes)
        filled = algos.take_nd(lev._values, level_codes, fill_value=lev._na_value)
        return lev._shallow_copy(filled, name=name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._drop_from_level [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def _drop_from_level(
        self, codes, level, errors: IgnoreRaise = "raise"
    ) -> MultiIndex:
        codes = com.index_labels_to_array(codes)
        i = self._get_level_number(level)
        index = self.levels[i]
        values = index.get_indexer(codes)
        # If nan should be dropped it will equal -1 here. We have to check which values
        # are not nan and equal -1, this means they are missing in the index
        nan_codes = isna(codes)
        values[(np.equal(nan_codes, False)) & (values == -1)] = -2
        if index.shape[0] == self.shape[0]:
            values[np.equal(nan_codes, True)] = -2

        not_found = codes[values == -2]
        if len(not_found) != 0 and errors != "ignore":
            raise KeyError(f"labels {not_found} not found in level")
        mask = ~algos.isin(self.codes[i], values)

        return self[mask]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.read_multi_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def read_multi_index(
        self, key: str, start: int | None = None, stop: int | None = None
    ) -> MultiIndex:
        nlevels = getattr(self.attrs, f"{key}_nlevels")

        levels = []
        codes = []
        names: list[Hashable] = []
        for i in range(nlevels):
            level_key = f"{key}_level{i}"
            node = getattr(self.group, level_key)
            lev = self.read_index_node(node, start=start, stop=stop)
            levels.append(lev)
            names.append(lev.name)

            label_key = f"{key}_label{i}"
            level_codes = self.read_array(label_key, start=start, stop=stop)
            codes.append(level_codes)

        return MultiIndex(
            levels=levels, codes=codes, names=names, verify_integrity=True
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
    def __init__(
        self, index: MultiIndex, level: Level, constructor, sort: bool = True
    ) -> None:
        self.constructor = constructor
        self.sort = sort

        # remove_unused_levels ensures every value in the unstacked level
        # has at least one entry, which guarantees that the mask returned by
        # get_new_values satisfies mask.any(0).all() i.e. no column in the
        # unstacked result is entirely empty.
        self.index = index.remove_unused_levels()

        self.level = self.index._get_level_number(level)

        # `nan` values have code `-1`, when sorting, we lift to assign them
        # at index 0
        self.has_nan = -1 in self.index.codes[self.level]
        should_lift = self.has_nan and self.sort
        self.lift = 1 if should_lift else 0

        # Note: the "pop" below alters these in-place.
        self.new_index_levels = list(self.index.levels)
        self.new_index_names = list(self.index.names)

        self.removed_name = self.new_index_names.pop(self.level)
        self.removed_level = self.new_index_levels.pop(self.level)
        self.removed_level_full = index.levels[self.level]
        self.unique_nan_index: int = -1
        if not self.sort:
            unique_codes: np.ndarray = unique(self.index.codes[self.level])
            if self.has_nan:
                # drop nan codes, because they are not represented in level
                nan_mask = unique_codes == -1

                unique_codes = unique_codes[~nan_mask]
                self.unique_nan_index = np.flatnonzero(nan_mask)[0]

            self.removed_level = self.removed_level.take(unique_codes)
            self.removed_level_full = self.removed_level_full.take(unique_codes)

        if config["mode"]["performance_warnings"]:
            # Bug fix GH 20601
            # If the data frame is too big, the number of unique index combination
            # will cause int32 overflow on windows environments.
            # We want to check and raise a warning before this happens
            num_rows = max(index_level.size for index_level in self.new_index_levels)
            num_columns = self.removed_level.size

            # GH20601: This forces an overflow if the number of cells is too high.
            # GH 26314: Previous ValueError raised was too restrictive for many users.
            num_cells = num_rows * num_columns
            if num_cells > np.iinfo(np.int32).max:
                warnings.warn(
                    f"The following operation may generate {num_cells} cells "
                    f"in the resulting pandas object.",
                    PerformanceWarning,
                    stacklevel=find_stack_level(),
                )

        self._make_selectors()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_level_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def _get_level_indexer(
        self, key, level: int = 0, indexer: npt.NDArray[np.bool_] | None = None
    ):
        # `level` kwarg is _always_ positional, never name
        # return a boolean array or slice showing where the key is
        # in the totality of values
        # if the indexer is provided, then use this

        level_index = self.levels[level]
        level_codes = self.codes[level]

        def convert_indexer(start, stop, step, indexer=indexer, codes=level_codes):
            # Compute a bool indexer to identify the positions to take.
            # If we have an existing indexer, we only need to examine the
            # subset of positions where the existing indexer is True.
            if indexer is not None:
                # we only need to look at the subset of codes where the
                # existing indexer equals True
                codes = codes[indexer]

            if step is None or step == 1:
                new_indexer = (codes >= start) & (codes < stop)
            else:
                r = np.arange(start, stop, step, dtype=codes.dtype)
                new_indexer = algos.isin(codes, r)

            if indexer is None:
                return new_indexer

            indexer = indexer.copy()
            indexer[indexer] = new_indexer
            return indexer

        if isinstance(key, slice):
            # handle a slice, returning a slice if we can
            # otherwise a boolean indexer
            step = key.step
            is_negative_step = step is not None and step < 0

            try:
                if key.start is not None:
                    start = level_index.get_loc(key.start)
                elif is_negative_step:
                    start = len(level_index) - 1
                else:
                    start = 0

                if key.stop is not None:
                    stop = level_index.get_loc(key.stop)
                elif is_negative_step:
                    stop = 0
                elif isinstance(start, slice):
                    stop = len(level_index)
                else:
                    stop = len(level_index) - 1
            except KeyError:
                # we have a partial slice (like looking up a partial date
                # string)
                start = stop = level_index.slice_indexer(key.start, key.stop, key.step)
                step = start.step

            if isinstance(start, slice) or isinstance(stop, slice):
                # we have a slice for start and/or stop
                # a partial date slicer on a DatetimeIndex generates a slice
                # note that the stop ALREADY includes the stopped point (if
                # it was a string sliced)
                start = getattr(start, "start", start)
                stop = getattr(stop, "stop", stop)
                return convert_indexer(start, stop, step)

            elif level > 0 or self._lexsort_depth == 0 or step is not None:
                # need to have like semantics here to right
                # searching as when we are using a slice
                # so adjust the stop by 1 (so we include stop)
                stop = (stop - 1) if is_negative_step else (stop + 1)
                return convert_indexer(start, stop, step)
            else:
                # sorted, so can return slice object -> view
                i = algos.searchsorted(level_codes, start, side="left")
                j = algos.searchsorted(level_codes, stop, side="right")
                return slice(i, j, step)

        else:
            idx = self._get_loc_single_level_index(level_index, key)

            if level > 0 or self._lexsort_depth == 0:
                # Desired level is not sorted
                if isinstance(idx, slice):
                    # test_get_loc_partial_timestamp_multiindex
                    locs = (level_codes >= idx.start) & (level_codes < idx.stop)
                    return locs

                locs = np.asarray(level_codes == idx, dtype=bool)

                if not locs.any():
                    # The label is present in self.levels[level] but unused:
                    raise KeyError(key)
                return locs

            if isinstance(idx, slice):
                # e.g. test_partial_string_timestamp_multiindex
                start = algos.searchsorted(level_codes, idx.start, side="left")
                # NB: "left" here bc of slice semantics
                end = algos.searchsorted(level_codes, idx.stop, side="left")
            else:
                start = algos.searchsorted(level_codes, idx, side="left")
                end = algos.searchsorted(level_codes, idx, side="right")

            if start == end:
                # The label is present in self.levels[level] but unused:
                raise KeyError(key)
            return slice(maybe_unbox_numpy_scalar(start), maybe_unbox_numpy_scalar(end))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py::BaseGrouper.levels [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/ops.py]
    def levels(self) -> list[Index]:
        if len(self.groupings) > 1:
            # mypy doesn't know result_index must be a MultiIndex
            return list(self.result_index.levels)  # type: ignore[attr-defined]
        else:
            return [self.result_index]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py::TestDataFrameQueryWithMultiIndex.to_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py]
        def to_series(mi, level):
            level_values = mi.get_level_values(level)
            s = level_values.to_series()
            s.index = mi
            return s
```
