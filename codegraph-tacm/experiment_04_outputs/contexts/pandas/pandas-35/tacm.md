# pandas-35 :: tacm

query: BUG: create new MI from MultiIndex._get_level_values (#33134)

## selected nodes

- rank=1 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=2 layer=FILE tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=3 layer=FILE tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py
- rank=4 layer=CLASS tokens=477 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=5 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_get_level_values.py::TestGetLevelValues file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_get_level_values.py
- rank=6 layer=CLASS tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=7 layer=CLASS tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=8 layer=CLASS tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_indexing.py::TestContains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_indexing.py
- rank=9 layer=CLASS tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_scalar.py::TestMultiIndexScalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_scalar.py
- rank=10 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::NumpyBlock file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=11 layer=CLASS tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::EABackedBlock file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=12 layer=FUNCTION tokens=368 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_values_for_csv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=13 layer=FUNCTION tokens=313 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.dropna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=14 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.putmask file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=15 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.codes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=16 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.maybe_mi_droplevels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=17 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Values.time_datetime_level_values_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=18 layer=FUNCTION tokens=259 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.levshape file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=19 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.nlevels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=20 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Values.time_datetime_level_values_sliced file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=21 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.get_level_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=22 layer=FUNCTION tokens=297 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=23 layer=FUNCTION tokens=223 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.new_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=24 layer=FUNCTION tokens=157 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.remove_unused_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=25 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Values.setup_cache file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=26 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.delete file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=27 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=28 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=29 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py::TestDataFrameQueryWithMultiIndex.to_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py
- rank=30 layer=FUNCTION tokens=8 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py::_f1 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py

## context

```text
file core/internals/blocks.py
imports: __future__, inspect, re, typing, warnings, numpy, pandas
defines: Block, EABackedBlock, ExtensionBlock, NumpyBlock, NDArrayBackedExtensionBlock, DatetimeLikeBlock, maybe_coerce_values, get_block_type, new_block_2d, new_block, check_ndim, extract_pandas_array, extend_blocks, ensure_block_shape, external_values

file core/indexes/base.py
imports: __future__, collections, datetime, functools, itertools, operator, typing, warnings
defines: Index, _maybe_return_indexers, join, _new_Index, maybe_sequence_to_range, ensure_index_from_sequences, ensure_index, trim_front, _validate_join_method, maybe_extract_name, get_unanimous_names, _unpack_nested_dtype, _maybe_try_sort, get_values_for_csv

file io/sas/sas_constants.py
imports: __future__, typing
defines: SASIndex

class MultiIndex(Index):  [core/indexes/multi.py:198]
methods: _check_indexing_error, _constructor, _convert_can_do_setop
         _drop_from_level, _engine, _format_multi
         _formatter_func, _get_codes_for_sorting
         _get_indexer_level_0, _get_indexer_strict
         _get_level_indexer, _get_level_number
         _get_level_values, _get_loc_level
         _get_loc_single_level_index, _get_names
         _get_reconciled_name_object, _get_values_for_csv
         _getitem_slice, _is_comparable_dtype
         _is_lexsorted, _is_memory_usage_qualified
         _lexsort_depth, _maybe_match_names
         _maybe_preserve_names, _maybe_to_slice, _nbytes
         _partial_tup_index, _raise_if_missing
         _recode_for_new_levels, _reorder_ilevels
         _reorder_indexer, _set_codes, _set_levels
         _set_names, _shallow_copy
         _should_fallback_to_positional
         _sort_levels_monotonic, _to_bool_indexer, _union
         _validate_codes, _validate_fill_value, _values
         _verify_integrity, _view, _wrap_difference_result
         _wrap_intersection_result, _wrap_reindex_result
         append, argsort, array, astype, cats, codes
         convert_indexer, copy, delete, drop, dropna
         dtype, dtypes, duplicated, equal_levels, equals
         f, fillna, from_arrays, from_frame, from_product
         from_tuples, get_level_values, get_loc
         get_loc_level, get_locs, get_slice_bound
         inferred_type, insert, is_monotonic_decreasing
         is_monotonic_increasing, isin, levels, levshape
         maybe_mi_droplevels, memory_usage, nbytes
         nlevels, putmask, remove_unused_levels
         reorder_levels, repeat, set_codes, set_levels
         size, slice_locs, sortlevel, swaplevel, take
         to_flat_index, to_frame, truncate, unique, values
         view, __array__, __contains__, __getitem__
         __len__, __new__, __reduce__

class TestGetLevelValues:  [indexes/multi/test_get_level_values.py:14]
methods: test_get_level_values_box_datetime64

class Values:  [asv_bench/benchmarks/multiindex_object.py:196]
methods: setup_cache, time_datetime_level_values_copy
         time_datetime_level_values_sliced

class _Unstacker:  [core/reshape/reshape.py:75]
methods: _indexer_and_to_sort, _indexer_is_identity
         _make_selectors, _make_sorted_values, _repeater
         arange_result, get_new_columns, get_new_values
         get_result, mask_all, new_index, sorted_labels
         __init__

class TestContains:  [indexes/multi/test_indexing.py:797]
methods: test_contains, test_contains_td64_level
         test_contains_top_level
         test_contains_with_missing_value
         test_contains_with_nat, test_large_mi_contains
         test_multiindex_contains_dropped

class TestMultiIndexScalar:  [tests/indexing/test_scalar.py:279]
methods: test_multiindex_at_get, test_multiindex_at_get_one_level
         test_multiindex_at_set

class NumpyBlock(Block):  [core/internals/blocks.py:2164]
methods: array_values, get_values, is_numeric, is_view

class EABackedBlock(Block):  [core/internals/blocks.py:1640]
methods: array_values, delete, get_values, pad_or_backfill, putmask
         setitem, shift, where

    def _get_values_for_csv(
        self, *, na_rep: str = "nan", **kwargs
    ) -> npt.NDArray[np.object_]:
        new_levels = []
        new_codes = []

        # go through the levels and format them
        for level, level_codes in zip(self.levels, self.codes, strict=True):
            level_strs = level._get_values_for_csv(na_rep=na_rep, **kwargs)
            # add nan values, if there are any
            mask = level_codes == -1
            if mask.any():
                nan_index = len(level_strs)
                # numpy 1.21 deprecated implicit string casting
                level_strs = level_strs.astype(str)
                level_strs = np.append(level_strs, na_rep)
                assert not level_codes.flags.writeable  # i.e. copy is needed
                level_codes = level_codes.copy()  # make writeable
                level_codes[mask] = nan_index
            new_levels.append(level_strs)
            new_codes.append(level_codes)

        if len(new_levels) == 1:
            # a single-level multi-index
            return Index(
                new_levels[0].take(new_codes[0]), copy=False
            )._get_values_for_csv()
        else:
            # reconstruct the multi-index
            mi = MultiIndex(
                levels=new_levels,
                codes=new_codes,
                names=self.names,
                sortorder=self.sortorder,
                verify_integrity=False,
            )
            return mi._values

    def dropna(self, how: AnyAll = "any") -> MultiIndex:
        """
        Return MultiIndex without NA/NaN values.

        Parameters
        ----------
        how : {'any', 'all'}, default 'any'
            Drop the value when any or all levels are NaN.

        Returns
        -------
        Index
            Returns a MultiIndex object after removing NA/NaN values.

        See Also
        --------
        Index.fillna : Fill NA/NaN values with the specified value.
        Index.isna : Detect missing values.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays(([np.nan, np.nan, 2.0], [3.0, np.nan, 4.0]))
        >>> mi.dropna()
        MultiIndex([(2.0, 4.0)],
                   )
        >>> mi.dropna(how="all")
        MultiIndex([(nan, 3.0),
                    (2.0, 4.0)],
                   )
        """
        nans = [level_codes == -1 for level_codes in self.codes]
        if how == "any":
            indexer = np.any(nans, axis=0)
        elif how == "all":
            indexer = np.all(nans, axis=0)
        else:
            raise ValueError(f"invalid how option: {how}")

        new_codes = [level_codes[~indexer] for level_codes in self.codes]
        return self.set_codes(codes=new_codes)

    def putmask(self, mask, value: MultiIndex) -> MultiIndex:  # type: ignore[override]
        """
        Return a new MultiIndex of the values set with the mask.

        Parameters
        ----------
        mask : array like
        value : MultiIndex
            Must either be the same length as self or length one

        Returns
        -------
        MultiIndex
        """
        mask, noop = validate_putmask(self, mask)
        if noop:
            return self.copy()

        if len(mask) == len(value):
            subset = value[mask].remove_unused_levels()
        else:
            subset = value.remove_unused_levels()

        new_levels = []
        new_codes = []

        for i, (value_level, level, level_codes) in enumerate(
            zip(subset.levels, self.levels, self.codes, strict=True)
        ):
            new_level = level.union(value_level, sort=False)
            value_codes = new_level.get_indexer_for(subset.get_level_values(i))
            new_code = ensure_int64(level_codes)
            new_code[mask] = value_codes
            new_levels.append(new_level)
            new_codes.append(new_code)

        return MultiIndex(
            levels=new_levels, codes=new_codes, names=self.names, verify_integrity=False
        )

    def codes(self) -> FrozenList:
        """
        Codes of the MultiIndex.

        Codes are the position of the index value in the list of level values
        for each level.

        Returns
        -------
        tuple of numpy.ndarray
            The codes of the MultiIndex. Each array in the tuple corresponds
            to a level in the MultiIndex.

        See Also
        --------
        MultiIndex.set_codes : Set new codes on MultiIndex.

        Examples
        --------
        >>> arrays = [[1, 1, 2, 2], ["red", "blue", "red", "blue"]]
        >>> mi = pd.MultiIndex.from_arrays(arrays, names=("number", "color"))
        >>> mi.codes
        FrozenList([[0, 0, 1, 1], [1, 0, 1, 0]])
        """
        return self._codes

        def maybe_mi_droplevels(indexer, levels):
            """
            If level does not exist or all levels were dropped, the exception
            has to be handled outside.
            """
            new_index = self[indexer]

            for i in sorted(levels, reverse=True):
                new_index = new_index._drop_level_numbers([i])

            return new_index

    def time_datetime_level_values_copy(self, mi):
        mi.copy().values

    def levshape(self) -> Shape:
        """
        A tuple representing the length of each level in the MultiIndex.

        In a `MultiIndex`, each level can contain multiple unique values. The
        `levshape` property provides a quick way to assess the size of each
        level by returning a tuple where each entry represents the number of
        unique values in that specific level. This is particularly useful in
        scenarios where you need to understand the structure and distribution
        of your index levels, such as when working with multidimensional data.

        See Also
        --------
        MultiIndex.shape : Return a tuple of the shape of the MultiIndex.
        MultiIndex.levels : Returns the levels of the MultiIndex.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([["a"], ["b"], ["c"]])
        >>> mi
        MultiIndex([('a', 'b', 'c')],
                   )
        >>> mi.levshape
        (1, 1, 1)
        """
        return tuple(len(x) for x in self.levels)

    def nlevels(self) -> int:
        """
        Integer number of levels in this MultiIndex.

        This property returns the count of levels (i.e., the depth of the
        hierarchical index), which corresponds to the number of arrays
        or columns used to construct the MultiIndex.

        See Also
        --------
        MultiIndex.levels : Get the levels of the MultiIndex.
        MultiIndex.codes : Get the codes of the MultiIndex.
        MultiIndex.from_arrays : Convert arrays to MultiIndex.
        MultiIndex.from_tuples : Convert list of tuples to MultiIndex.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([["a"], ["b"], ["c"]])
        >>> mi
        MultiIndex([('a', 'b', 'c')],
                   )
        >>> mi.nlevels
        3
        """
        return len(self._levels)

    def time_datetime_level_values_sliced(self, mi):
        mi[:10].values

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
    # ... truncated

    def insert(self, loc: int, item) -> MultiIndex:
        """
        Make new MultiIndex inserting new item at location

        Parameters
        ----------
        loc : int
        item : tuple
            Must be same length as number of levels in the MultiIndex

        Returns
        -------
        new_index : Index
        """
        item = self._validate_fill_value(item)

        new_levels = []
        new_codes = []
        for k, level, level_codes in zip(item, self.levels, self.codes, strict=True):
            if k not in level:
                # have to insert into level
                # must insert at end otherwise you have to recompute all the
                # other codes
                lev_loc = len(level)
                level = level.insert(lev_loc, k)
                if isna(level[lev_loc]):  # GH 59003, 60388
                    lev_loc = -1
            else:
                lev_loc = level.get_loc(k)

            new_levels.append(level)
            new_codes.append(np.insert(ensure_int64(level_codes), loc, lev_loc))

        return MultiIndex(
            levels=new_levels, codes=new_codes, names=self.names, verify_integrity=False
        )

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
    # ... truncated

    def setup_cache(self):
        level1 = range(1000)
        level2 = date_range(start="1/1/2012", periods=100)
        mi = MultiIndex.from_product([level1, level2])
        return mi

    def delete(self, loc) -> MultiIndex:
        """
        Make new index with passed location deleted

        Returns
        -------
        new_index : MultiIndex
        """
        new_codes = [np.delete(level_codes, loc) for level_codes in self.codes]
        return MultiIndex(
            levels=self.levels,
            codes=new_codes,
            names=self.names,
            verify_integrity=False,
        )

    def _get_loc_level(self, key, level: int | list[int] = 0):
        """
        get_loc_level but with `level` known to be positional, not name-based.
        """
    # ... truncated

    def unique(self, level=None):
        """
        Return unique values in the index.

        Unique values are returned in order of appearance, this does NOT sort.

        Parameters
        ----------
        level : int or hashable, optional
            Only return values from specified level (for MultiIndex).
            If int, gets the level by integer position, else by level name.

    # ... truncated

        def to_series(mi, level):
            level_values = mi.get_level_values(level)
            s = level_values.to_series()
            s.index = mi
            return s

def _f1(new=False):
    return new
```
