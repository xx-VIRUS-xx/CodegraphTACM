# pandas-35 :: hybrid-cs

query: BUG: create new MI from MultiIndex._get_level_values (#33134)

## selected nodes

- rank=1 layer=FUNCTION tokens=739 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.get_level_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=2 layer=FUNCTION tokens=360 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=3 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py::TestDataFrameQueryWithMultiIndex.to_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py
- rank=4 layer=FUNCTION tokens=314 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_level_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=5 layer=FUNCTION tokens=1585 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=6 layer=FUNCTION tokens=476 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.droplevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=7 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=8 layer=FUNCTION tokens=260 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._drop_from_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=9 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py::m file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def unique(self, level=None):
        """
        Return unique values in the index.

        Unique values are returned in order of appearance, this does NOT sort.

        Parameters
        ----------
        level : int or hashable, optional
            Only return values from specified level (for MultiIndex).
            If int, gets the level by integer position, else by level name.

        Returns
        -------
        MultiIndex
            Unique values in the MultiIndex.

        See Also
        --------
        unique : Numpy array of unique values in that column.
        Series.unique : Return unique values of Series object.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays((list("abca"), list("defd")))
        >>> mi
        MultiIndex([('a', 'd'),
                    ('b', 'e'),
                    ('c', 'f'),
                    ('a', 'd')],
                   )
        >>> mi.unique()
        MultiIndex([('a', 'd'),
                    ('b', 'e'),
                    ('c', 'f')],
                   )
        """
        if level is None:
            return self.drop_duplicates()
        else:
            level = self._get_level_number(level)
            return self._get_level_values(level=level, unique=True)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py::TestDataFrameQueryWithMultiIndex.to_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py]
        def to_series(mi, level):
            level_values = mi.get_level_values(level)
            s = level_values.to_series()
            s.index = mi
            return s

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_level [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def _get_loc_level(self, key, level: int | list[int] = 0):
        """
        get_loc_level but with `level` known to be positional, not name-based.
        """

        # different name to distinguish from maybe_droplevels
        def maybe_mi_droplevels(indexer, levels):
            """
            If level does not exist or all levels were dropped, the exception
            has to be handled outside.
            """
            new_index = self[indexer]

            for i in sorted(levels, reverse=True):
                new_index = new_index._drop_level_numbers([i])

            return new_index

        if isinstance(level, (tuple, list)):
            if len(key) != len(level):
                raise AssertionError(
                    "Key for location must have same length as number of levels"
                )
            result = None
            for lev, k in zip(level, key, strict=True):
                loc, new_index = self._get_loc_level(k, level=lev)
                if isinstance(loc, slice):
                    mask = np.zeros(len(self), dtype=bool)
                    mask[loc] = True
                    loc = mask
                result = loc if result is None else result & loc

            try:
                # FIXME: we should be only dropping levels on which we are
                #  scalar-indexing
                mi = maybe_mi_droplevels(result, level)
            except ValueError:
                # droplevel failed because we tried to drop all levels,
                #  i.e. len(level) == self.nlevels
                mi = self[result]

            return result, mi

        # kludge for #1796
        if isinstance(key, list):
            key = tuple(key)

        if isinstance(key, tuple) and level == 0:
            try:
                # Check if this tuple is a single key in our first level
                if key in self.levels[0]:
                    indexer = self._get_level_indexer(key, level=level)
                    new_index = maybe_mi_droplevels(indexer, [0])
                    return indexer, new_index
            except (TypeError, InvalidIndexError):
                pass

            if not any(isinstance(k, slice) for k in key):
                if len(key) == self.nlevels and self.is_unique:
                    # Complete key in unique index -> standard get_loc
                    try:
                        return (self._engine.get_loc(key), None)
                    except KeyError as err:
                        raise KeyError(key) from err
                    except TypeError:
                        # e.g. partial string indexing
                        #  test_partial_string_timestamp_multiindex
                        pass

                # partial selection
                indexer = self.get_loc(key)
                ilevels = [i for i in range(len(key)) if key[i] != slice(None, None)]
                if len(ilevels) == self.nlevels:
                    if is_integer(indexer):
                        # we are dropping all levels
                        return indexer, None

                    # TODO: in some cases we still need to drop some levels,
                    #  e.g. test_multiindex_perf_warn
                    # test_partial_string_timestamp_multiindex
                    ilevels = [
                        i
                        for i in range(len(key))
                        if (
                            not isinstance(key[i], str)
                            or not self.levels[i]._supports_partial_string_indexing
                        )
                        and key[i] != slice(None, None)
                    ]
                    if len(ilevels) == self.nlevels:
                        # TODO: why?
                        ilevels = []
                return indexer, maybe_mi_droplevels(indexer, ilevels)

            else:
                indexer = None
                for i, k in enumerate(key):
                    if not isinstance(k, slice):
                        loc_level = self._get_level_indexer(k, level=i)
                        if isinstance(loc_level, slice):
                            if com.is_null_slice(loc_level) or com.is_full_slice(
                                loc_level, len(self)
                            ):
                                # everything
                                continue

                            # e.g. test_xs_IndexSlice_argument_not_implemented
                            k_index = np.zeros(len(self), dtype=bool)
                            k_index[loc_level] = True

                        else:
                            k_index = loc_level

                    elif com.is_null_slice(k):
                        # taking everything, does not affect `indexer` below
                        continue

                    else:
                        # FIXME: this message can be inaccurate, e.g.
                        #  test_series_varied_multiindex_alignment
                        raise TypeError(f"Expected label or tuple of labels, got {key}")

                    if indexer is None:
                        indexer = k_index
                    else:
                        indexer &= k_index
                if indexer is None:
                    indexer = slice(None, None)
                ilevels = [i for i in range(len(key)) if key[i] != slice(None, None)]
                return indexer, maybe_mi_droplevels(indexer, ilevels)
        else:
            indexer = self._get_level_indexer(key, level=level)
            if (
                isinstance(key, str)
                and self.levels[level]._supports_partial_string_indexing
            ):
                # check to see if we did an exact lookup vs sliced
                check = self.levels[level].get_loc(key)
                if not is_integer(check):
                    # e.g. test_partial_string_timestamp_multiindex
                    return indexer, self[indexer]

            try:
                result_index = maybe_mi_droplevels(indexer, [level])
            except ValueError:
                result_index = self[indexer]

            return indexer, result_index

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py::m [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py]
def m():
    return 5
```
