# pandas-35 :: hybrid

query: BUG: create new MI from MultiIndex._get_level_values (#33134)

## selected nodes

- rank=1 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=2 layer=FUNCTION tokens=739 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.get_level_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=3 layer=FUNCTION tokens=476 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.droplevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=4 layer=FUNCTION tokens=216 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_with_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=5 layer=FUNCTION tokens=952 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.remove_unused_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=6 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.new_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=7 layer=FUNCTION tokens=352 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._get_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=8 layer=FUNCTION tokens=686 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.set_codes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=9 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_put.py::make_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_put.py
- rank=10 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IndexEquals.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def _create_mi_with_dt64tz_level():
    """
    MultiIndex with a level that is a tzaware DatetimeIndex.
    """
    # GH#8367 round trip with pickle
    return MultiIndex.from_product(
        [[1, 2], ["a", "b"], date_range("20130101", periods=3, tz="US/Eastern")],
        names=["one", "two", "three"],
    )

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.droplevel [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def droplevel(self, level: IndexLabel = 0) -> Index:
        """
        Return index with requested level(s) removed.

        If resulting index has only 1 level left, the result will be
        of Index type, not MultiIndex. The original index is not modified inplace.

        Parameters
        ----------
        level : int, str, or list-like, default 0
            If a string is given, must be the name of a level
            If list-like, elements must be names or indexes of levels.

        Returns
        -------
        Index or MultiIndex
            Returns an Index or MultiIndex object, depending on the resulting index
            after removing the requested level(s).

        See Also
        --------
        Index.dropna : Return Index without NA/NaN values.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays(
        ...     [[1, 2], [3, 4], [5, 6]], names=["x", "y", "z"]
        ... )
        >>> mi
        MultiIndex([(1, 3, 5),
                    (2, 4, 6)],
                   names=['x', 'y', 'z'])

        >>> mi.droplevel()
        MultiIndex([(3, 5),
                    (4, 6)],
                   names=['y', 'z'])

        >>> mi.droplevel(2)
        MultiIndex([(1, 3),
                    (2, 4)],
                   names=['x', 'y'])

        >>> mi.droplevel("z")
        MultiIndex([(1, 3),
                    (2, 4)],
                   names=['x', 'y'])

        >>> mi.droplevel(["x", "y"])
        Index([5, 6], dtype='int64', name='z')
        """
        if not isinstance(level, (tuple, list)):
            level = [level]

        levnums = sorted((self._get_level_number(lev) for lev in level), reverse=True)

        return self._drop_level_numbers(levnums)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_with_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def index_with_missing(request):
    """
    Fixture for indices with missing values.

    Integer-dtype and empty cases are excluded because they cannot hold missing
    values.

    MultiIndex is excluded because isna() is not defined for MultiIndex.
    """
    ind = indices_dict[request.param]
    if request.param in ["tuples", "mi-with-dt64tz-level", "multi"]:
        # For setting missing values in the top level of MultiIndex
        vals = ind.tolist()
        vals[0] = (None, *vals[0][1:])
        vals[-1] = (None, *vals[-1][1:])
        return MultiIndex.from_tuples(vals)
    else:
        vals = ind.values.copy()
        vals[0] = None
        vals[-1] = None
        return type(ind)(vals, copy=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.remove_unused_levels [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def remove_unused_levels(self) -> MultiIndex:
        """
        Create new MultiIndex from current that removes unused levels.

        Unused level(s) means levels that are not expressed in the
        labels. The resulting MultiIndex will have the same outward
        appearance, meaning the same .values and ordering. It will
        also be .equals() to the original.

        The `remove_unused_levels` method is useful in cases where you have a
        MultiIndex with hierarchical levels, but some of these levels are no
        longer needed due to filtering or subsetting operations. By removing
        the unused levels, the resulting MultiIndex becomes more compact and
        efficient, which can improve performance in subsequent operations.

        Returns
        -------
        MultiIndex
            A new MultiIndex with unused levels removed.

        See Also
        --------
        MultiIndex.droplevel : Remove specified levels from a MultiIndex.
        MultiIndex.reorder_levels : Rearrange levels of a MultiIndex.
        MultiIndex.set_levels : Set new levels on a MultiIndex.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_product([range(2), list("ab")])
        >>> mi
        MultiIndex([(0, 'a'),
                    (0, 'b'),
                    (1, 'a'),
                    (1, 'b')],
                   )

        >>> mi[2:]
        MultiIndex([(1, 'a'),
                    (1, 'b')],
                   )

        The 0 from the first level is not represented
        and can be removed

        >>> mi2 = mi[2:].remove_unused_levels()
        >>> mi2.levels
        FrozenList([[1], ['a', 'b']])
        """
        new_levels = []
        new_codes = []

        changed = False
        for lev, level_codes in zip(self.levels, self.codes, strict=True):
            # Since few levels are typically unused, bincount() is more
            # efficient than unique() - however it only accepts positive values
            # (and drops order):
            uniques = np.where(np.bincount(level_codes + 1) > 0)[0] - 1
            has_na = int(len(uniques) and (uniques[0] == -1))

            if len(uniques) != len(lev) + has_na:
                if lev.isna().any() and len(uniques) == len(lev):
                    break
                # We have unused levels
                changed = True

                # Recalculate uniques, now preserving order.
                # Can easily be cythonized by exploiting the already existing
                # "uniques" and stop parsing "level_codes" when all items
                # are found:
                uniques = algos.unique(level_codes)
                if has_na:
                    na_idx = np.where(uniques == -1)[0]
                    # Just ensure that -1 is in first position:
                    uniques[[0, na_idx[0]]] = uniques[[na_idx[0], 0]]

                # codes get mapped from uniques to 0:len(uniques)
                # -1 (if present) is mapped to last position
                code_mapping = np.zeros(len(lev) + has_na)
                # ... and reassigned value -1:
                code_mapping[uniques] = np.arange(len(uniques)) - has_na

                level_codes = code_mapping[level_codes]

                # new levels are simple
                lev = lev.take(uniques[has_na:])

            new_levels.append(lev)
            new_codes.append(level_codes)

        result = self.view()

        if changed:
            result._reset_identity()
            result._set_levels(new_levels, validate=False)
            result._set_codes(new_codes, validate=False)

        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.new_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
    def new_index(self) -> MultiIndex | Index:
        # Does not depend on values or value_columns
        if self.sort:
            labels = self.sorted_labels[:-1]
        else:
            v = self.level
            codes = list(self.index.codes)
            labels = codes[:v] + codes[v + 1 :]
        result_codes = [lab.take(self.compressor) for lab in labels]

        # construct the new index
        if len(self.new_index_levels) == 1:
            level, level_codes = self.new_index_levels[0], result_codes[0]
            if (level_codes == -1).any():
                level = level.insert(len(level), level._na_value)
            return level.take(level_codes).rename(self.new_index_names[0])

        return MultiIndex(
            levels=self.new_index_levels,
            codes=result_codes,
            names=self.new_index_names,
            verify_integrity=False,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._get_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _get_value(self, label, takeable: bool = False):
        """
        Quickly retrieve single value at passed index label.

        Parameters
        ----------
        label : object
        takeable : interpret the index as indexers, default False

        Returns
        -------
        scalar value
        """
        if takeable:
            return self._values[label]

        # Similar to Index.get_value, but we do not fall back to positional
        loc = self.index.get_loc(label)

        if is_integer(loc):
            return self._values[loc]

        if isinstance(self.index, MultiIndex):
            mi = self.index
            new_values = self._values[loc]
            if len(new_values) == 1 and mi.nlevels == 1:
                # If more than one level left, we can not return a scalar
                return new_values[0]

            new_index = mi[loc]
            new_index = maybe_droplevels(new_index, label)
            new_ser = self._constructor(
                new_values, index=new_index, name=self.name, copy=False
            )
            if isinstance(loc, slice):
                new_ser._mgr.add_references(self._mgr)
            return new_ser.__finalize__(self)

        else:
            return self.iloc[loc]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.set_codes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def set_codes(
        self, codes, *, level=None, verify_integrity: bool = True
    ) -> MultiIndex:
        """
        Set new codes on MultiIndex. Defaults to returning new index.

        The codes map each index entry to its position in the corresponding
        level array. This method returns a new MultiIndex with the updated
        codes.

        Parameters
        ----------
        codes : sequence or list of sequence
            New codes to apply.
        level : int, level name, or sequence of int/level names (default None)
            Level(s) to set (None for all levels).
        verify_integrity : bool, default True
            If True, checks that levels and codes are compatible.

        Returns
        -------
        new index (of same type and class...etc) or None
            The same type as the caller or None if ``inplace=True``.

        See Also
        --------
        MultiIndex.set_levels : Set new levels on MultiIndex.
        MultiIndex.codes : Get the codes of the levels in the MultiIndex.
        MultiIndex.levels : Get the levels of the MultiIndex.

        Examples
        --------
        >>> idx = pd.MultiIndex.from_tuples(
        ...     [(1, "one"), (1, "two"), (2, "one"), (2, "two")], names=["foo", "bar"]
        ... )
        >>> idx
        MultiIndex([(1, 'one'),
            (1, 'two'),
            (2, 'one'),
            (2, 'two')],
           names=['foo', 'bar'])

        >>> idx.set_codes([[1, 0, 1, 0], [0, 0, 1, 1]])
        MultiIndex([(2, 'one'),
                    (1, 'one'),
                    (2, 'two'),
                    (1, 'two')],
                   names=['foo', 'bar'])
        >>> idx.set_codes([1, 0, 1, 0], level=0)
        MultiIndex([(2, 'one'),
                    (1, 'two'),
                    (2, 'one'),
                    (1, 'two')],
                   names=['foo', 'bar'])
        >>> idx.set_codes([0, 0, 1, 1], level="bar")
        MultiIndex([(1, 'one'),
                    (1, 'one'),
                    (2, 'two'),
                    (2, 'two')],
                   names=['foo', 'bar'])
        >>> idx.set_codes([[1, 0, 1, 0], [0, 0, 1, 1]], level=[0, 1])
        MultiIndex([(2, 'one'),
                    (1, 'one'),
                    (2, 'two'),
                    (1, 'two')],
                   names=['foo', 'bar'])
        """

        level, codes = _require_listlike(level, codes, "Codes")
        idx = self._view()
        idx._reset_identity()
        idx._set_codes(codes, level=level, verify_integrity=verify_integrity)
        return idx

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_put.py::make_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_put.py]
    def make_index(names=None):
        dti = date_range("2013-12-01", "2013-12-02")
        mi = MultiIndex.from_product([dti, range(2), range(3)], names=names)
        return mi

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IndexEquals.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def setup(self):
        idx_large_fast = RangeIndex(100_000)
        idx_small_slow = date_range(start="1/1/2012", periods=1)
        self.mi_large_slow = MultiIndex.from_product([idx_large_fast, idx_small_slow])

        self.idx_non_object = RangeIndex(1)
```
