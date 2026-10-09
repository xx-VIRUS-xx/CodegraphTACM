# pandas-35 :: minilm

query: BUG: create new MI from MultiIndex._get_level_values (#33134)

## selected nodes

- rank=1 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.write_multi_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=2 layer=FUNCTION tokens=271 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter._generate_multiindex_header_rows file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py
- rank=3 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::ToRecords.time_to_records_multiindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=4 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IndexEquals.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=5 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=6 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._view file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=7 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_multiindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=8 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::maybe_droplevels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=9 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_with_cache file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=10 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_put.py::make_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_put.py
- rank=11 layer=FUNCTION tokens=216 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_with_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=12 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.new_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=13 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IndexEquals.time_non_object_equals_multiindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=14 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.maybe_mi_droplevels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=15 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Duplicates.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=16 layer=FUNCTION tokens=476 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.droplevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=17 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Equals.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=18 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.read_multi_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=19 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Unique.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py
- rank=20 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py::FromSeries.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py
- rank=21 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter._save_header file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py
- rank=22 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/conftest.py::idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/conftest.py
- rank=23 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_no_cache file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=24 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::GenericFixed.write_multi_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def write_multi_index(self, key: str, index: MultiIndex) -> None:
        setattr(self.attrs, f"{key}_nlevels", index.nlevels)

        for i, (lev, level_codes, name) in enumerate(
            zip(index.levels, index.codes, index.names, strict=True)
        ):
            # write the level
            if isinstance(lev.dtype, ExtensionDtype) and not isinstance(
                lev.dtype, StringDtype
            ):
                raise NotImplementedError(
                    "Saving a MultiIndex with an extension dtype is not supported."
                )
            level_key = f"{key}_level{i}"
            conv_level = _convert_index(level_key, lev, self.encoding, self.errors)
            self.write_array(level_key, conv_level.values)
            node = getattr(self.group, level_key)
            node._v_attrs.kind = conv_level.kind
            node._v_attrs.name = name

            # write the name
            setattr(node._v_attrs, f"{key}_name{name}", name)

            # write the labels
            label_key = f"{key}_label{i}"
            self.write_array(label_key, level_codes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter._generate_multiindex_header_rows [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py]
    def _generate_multiindex_header_rows(self) -> Iterator[list[Hashable]]:
        columns = self.obj.columns
        for i in range(columns.nlevels):
            # we need at least 1 index column to write our col names
            col_line = []
            if self.index:
                # name is the first column
                col_line.append(columns.names[i])

                if isinstance(self.index_label, list) and len(self.index_label) > 1:
                    col_line.extend([""] * (len(self.index_label) - 1))

            col_line.extend(columns._get_level_values(i))
            yield col_line

        # Write out the index line if it's not empty.
        # Otherwise, we will print out an extraneous
        # blank line between the mi and the data rows.
        if self.encoded_labels and set(self.encoded_labels) != {""}:
            yield self.encoded_labels + [""] * len(columns)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::ToRecords.time_to_records_multiindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_to_records_multiindex(self):
        self.df_mi.to_records(index=True)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IndexEquals.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def setup(self):
        idx_large_fast = RangeIndex(100_000)
        idx_small_slow = date_range(start="1/1/2012", periods=1)
        self.mi_large_slow = MultiIndex.from_product([idx_large_fast, idx_small_slow])

        self.idx_non_object = RangeIndex(1)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._view [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def _view(self) -> MultiIndex:
        result = type(self)(
            levels=self.levels,
            codes=self.codes,
            sortorder=self.sortorder,
            names=self.names,
            verify_integrity=False,
        )
        result._cache = self._cache.copy()
        result._reset_cache("levels")  # GH32669
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_multiindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def _create_multiindex():
    """
    MultiIndex used to test the general functionality of this object
    """

    # See Also: tests.multi.conftest.idx
    major_axis = Index(["foo", "bar", "baz", "qux"])
    minor_axis = Index(["one", "two"])

    major_codes = np.array([0, 0, 1, 2, 3, 3])
    minor_codes = np.array([0, 1, 0, 1, 0, 1])
    index_names = ["first", "second"]
    return MultiIndex(
        levels=[major_axis, minor_axis],
        codes=[major_codes, minor_codes],
        names=index_names,
        verify_integrity=False,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::maybe_droplevels [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
def maybe_droplevels(index: Index, key) -> Index:
    """
    Attempt to drop level or levels from the given index.

    Parameters
    ----------
    index: Index
    key : scalar or tuple

    Returns
    -------
    Index
    """
    # drop levels
    original_index = index
    if isinstance(key, tuple):
        # Caller is responsible for ensuring the key is not an entry in the first
        #  level of the MultiIndex.
        for _ in key:
            try:
                index = index._drop_level_numbers([0])
            except ValueError:
                # we have dropped too much, so back out
                return original_index
    else:
        try:
            index = index._drop_level_numbers([0])
        except ValueError:
            pass

    return index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_with_cache [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_reindex_multiindex_with_cache(self):
        # MultiIndex._values gets cached
        self.s.reindex(self.s_subset.index)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_put.py::make_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_put.py]
    def make_index(names=None):
        dti = date_range("2013-12-01", "2013-12-02")
        mi = MultiIndex.from_product([dti, range(2), range(3)], names=names)
        return mi

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IndexEquals.time_non_object_equals_multiindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def time_non_object_equals_multiindex(self):
        self.idx_non_object.equals(self.mi_large_slow)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.maybe_mi_droplevels [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
        def maybe_mi_droplevels(indexer, levels):
            """
            If level does not exist or all levels were dropped, the exception
            has to be handled outside.
            """
            new_index = self[indexer]

            for i in sorted(levels, reverse=True):
                new_index = new_index._drop_level_numbers([i])

            return new_index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Duplicates.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py]
    def setup(self):
        size = 65536
        arrays = [np.random.randint(0, 8192, size), np.random.randint(0, 1024, size)]
        mask = np.random.rand(size) < 0.1
        self.mi_unused_levels = MultiIndex.from_arrays(arrays)
        self.mi_unused_levels = self.mi_unused_levels[mask]

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Equals.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py]
    def setup(self):
        self.mi = MultiIndex.from_product(
            [
                date_range("2000-01-01", periods=1000),
                RangeIndex(1000),
            ]
        )
        self.mi_deepcopy = self.mi.copy(deep=True)
        self.idx_non_object = RangeIndex(1)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py::Unique.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/multiindex_object.py]
    def setup(self, dtype_val):
        level = Series(
            [1, 2, dtype_val[1], dtype_val[1], *list(range(1000000))],
            dtype=dtype_val[0],
        )
        self.midx = MultiIndex.from_arrays([level, level])

        level_dups = Series(
            [1, 2, dtype_val[1], dtype_val[1]] + list(range(500_000)) * 2,
            dtype=dtype_val[0],
        )

        self.midx_dups = MultiIndex.from_arrays([level_dups, level_dups])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py::FromSeries.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py]
    def setup(self):
        mi = MultiIndex.from_product([range(100), range(100)])
        self.s = Series(np.random.randn(10000), index=mi)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter._save_header [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py]
    def _save_header(self) -> None:
        if not self.has_mi_columns or self._has_aliases:
            self.writer.writerow(self.encoded_labels)
        else:
            for row in self._generate_multiindex_header_rows():
                self.writer.writerow(row)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/conftest.py::idx [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/conftest.py]
def idx():
    # a MultiIndex used to test the general functionality of the
    # general functionality of this object
    major_axis = Index(["foo", "bar", "baz", "qux"])
    minor_axis = Index(["one", "two"])

    major_codes = np.array([0, 0, 1, 2, 3, 3])
    minor_codes = np.array([0, 1, 0, 1, 0, 1])
    index_names = ["first", "second"]
    mi = MultiIndex(
        levels=[major_axis, minor_axis],
        codes=[major_codes, minor_codes],
        names=index_names,
        verify_integrity=False,
    )
    return mi

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_no_cache [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_reindex_multiindex_no_cache(self):
        # Copy to avoid MultiIndex._values getting cached
        self.s.reindex(self.s_subset_no_cache.index.copy())

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def array(self):
        """
        Raises a ValueError for `MultiIndex` because there's no single
        array backing a MultiIndex.

        Raises
        ------
        ValueError
        """
        raise ValueError(
            "MultiIndex has no single backing array. Use "
            "'MultiIndex.to_numpy()' to get a NumPy array of tuples."
        )
```
