# pandas-35 :: tacm-full

query: BUG: create new MI from MultiIndex._get_level_values (#33134)

## selected nodes

- rank=1 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py::TestDataFrameQueryWithMultiIndex.to_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py
- rank=2 layer=FUNCTION tokens=412 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_values_for_csv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=3 layer=FUNCTION tokens=354 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.dropna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=4 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=5 layer=FUNCTION tokens=358 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.putmask file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=6 layer=FUNCTION tokens=228 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.codes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=7 layer=FUNCTION tokens=352 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._get_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=8 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._maybe_make_multi_index_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=9 layer=FUNCTION tokens=300 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.levshape file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=10 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.nlevels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=11 layer=FUNCTION tokens=314 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_level_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=12 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Values.time_datetime_level_values_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=13 layer=FUNCTION tokens=338 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=14 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Values.time_datetime_level_values_sliced file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=15 layer=FUNCTION tokens=243 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._transform_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=16 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.new_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=17 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py::FromSeries.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py::TestDataFrameQueryWithMultiIndex.to_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_query_eval.py]
        def to_series(mi, level):
            level_values = mi.get_level_values(level)
            s = level_values.to_series()
            s.index = mi
            return s

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_values_for_csv [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.dropna [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.putmask [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.codes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._maybe_make_multi_index_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py]
    def _maybe_make_multi_index_columns(
        self,
        columns: SequenceT,
        col_names: Sequence[Hashable] | None = None,
    ) -> SequenceT | MultiIndex:
        # possibly create a column mi here
        if is_potential_multi_index(columns):
            columns_mi = cast("Sequence[tuple[Hashable, ...]]", columns)
            return MultiIndex.from_tuples(columns_mi, names=col_names)
        return columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.levshape [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.nlevels [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Values.time_datetime_level_values_copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py]
    def time_datetime_level_values_copy(self, mi):
        mi.copy().values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Values.time_datetime_level_values_sliced [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py]
    def time_datetime_level_values_sliced(self, mi):
        mi[:10].values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._transform_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _transform_index(self, func: Callable, *, level: int | None = None) -> Index:
        """
        Apply function to all values found in index.

        This includes transforming multiindex entries separately.
        Only apply function to one level of the MultiIndex if level is specified.
        """
        if isinstance(self, ABCMultiIndex):
            values = [
                (
                    self.get_level_values(i).map(func)
                    if i == level or level is None
                    else self.get_level_values(i)
                )
                for i in range(self.nlevels)
            ]
            return type(self).from_arrays(values)
        else:
            items = [func(x) for x in self]
            return Index(items, name=self.name, tupleize_cols=False)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py::FromSeries.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py]
    def setup(self):
        mi = MultiIndex.from_product([range(100), range(100)])
        self.s = Series(np.random.randn(10000), index=mi)
```
