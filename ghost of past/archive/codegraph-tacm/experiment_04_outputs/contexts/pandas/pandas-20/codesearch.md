# pandas-20 :: codesearch

query: BUG: freq not retained on apply_index (#33779)

## selected nodes

- rank=1 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py
- rank=2 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py::TestDatetimeIndex.assert_index_parameters file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py
- rank=3 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestIndexing.assert_reindex_indexer_is_ok file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py
- rank=4 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=5 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_doctools.py::TablePlotter._insert_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_doctools.py
- rank=6 layer=FUNCTION tokens=266 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestSetitemCoercion._assert_setitem_index_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py
- rank=7 layer=FUNCTION tokens=351 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLTable._index_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=8 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py
- rank=9 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._reindex_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=10 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_concat_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=11 layer=FUNCTION tokens=801 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.reindex_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=12 layer=FUNCTION tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py::SparseFrameAccessor._prep_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py
- rank=13 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_take_new_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=14 layer=FUNCTION tokens=324 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._reindex_with_indexers file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=15 layer=FUNCTION tokens=527 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/take.py::_take_preprocess_indexer_and_fill_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/take.py
- rank=16 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._maybe_cast_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=17 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py
- rank=18 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._wrap_reindex_result file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py::_get_index_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/timeseries.py]
def _get_index_freq(index: Index) -> BaseOffset | None:
    freq = getattr(index, "freq", None)
    if freq is None:
        freq = getattr(index, "inferred_freq", None)
        freq = to_offset(freq)
    return freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py::TestDatetimeIndex.assert_index_parameters [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_datetime.py]
    def assert_index_parameters(self, index):
        assert index.freq == "40960ns"
        assert index.inferred_freq == "40960ns"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestIndexing.assert_reindex_indexer_is_ok [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py]
        def assert_reindex_indexer_is_ok(mgr, axis, new_labels, indexer, fill_value):
            mat = _as_array(mgr)
            reindexed_mat = algos.take_nd(mat, indexer, axis, fill_value=fill_value)
            reindexed = mgr.reindex_indexer(
                new_labels, indexer, axis, fill_value=fill_value
            )
            tm.assert_numpy_array_equal(
                reindexed_mat, _as_array(reindexed), check_dtype=False
            )
            tm.assert_index_equal(reindexed.axes[axis], new_labels)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def index_indexing(index, idx):
    if isinstance(index, IndexType):

        def index_getitem(index, idx):
            return index._data[idx]

        return index_getitem

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_doctools.py::TablePlotter._insert_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_doctools.py]
    def _insert_index(self, data):
        # insert is destructive
        data = data.copy()
        idx_nlevels = data.index.nlevels
        if idx_nlevels == 1:
            data.insert(0, "Index", data.index)
        else:
            for i in range(idx_nlevels):
                data.insert(i, f"Index{i}", data.index._get_level_values(i))

        col_nlevels = data.columns.nlevels
        if col_nlevels > 1:
            col = data.columns._get_level_values(0)
            values = [
                data.columns._get_level_values(i)._values for i in range(1, col_nlevels)
            ]
            col_df = pd.DataFrame(values)
            data.columns = col_df.columns
            data = pd.concat([col_df, data])
            data.columns = col
        return data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestSetitemCoercion._assert_setitem_index_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py]
    def _assert_setitem_index_conversion(
        self, original_series, loc_key, expected_index, expected_dtype
    ):
        """test index's coercion triggered by assign key"""
        temp = original_series.copy()
        # GH#33469 pre-2.0 with int loc_key and temp.index.dtype == np.float64
        #  `temp[loc_key] = 5` treated loc_key as positional
        temp[loc_key] = 5
        exp = pd.Series([1, 2, 3, 4, 5], index=expected_index)
        tm.assert_series_equal(temp, exp)
        # check dtype explicitly for sure
        assert temp.index.dtype == expected_dtype

        temp = original_series.copy()
        temp.loc[loc_key] = 5
        exp = pd.Series([1, 2, 3, 4, 5], index=expected_index)
        tm.assert_series_equal(temp, exp)
        # check dtype explicitly for sure
        assert temp.index.dtype == expected_dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLTable._index_name [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py]
    def _index_name(self, index, index_label):
        # for writing: index=True to include index in sql table
        if index is True:
            nlevels = self.frame.index.nlevels
            # if index_label is specified, set this as index name(s)
            if index_label is not None:
                if not isinstance(index_label, list):
                    index_label = [index_label]
                if len(index_label) != nlevels:
                    raise ValueError(
                        "Length of 'index_label' should match number of "
                        f"levels, which is {nlevels}"
                    )
                return index_label
            # return the used column labels for the index columns
            if (
                nlevels == 1
                and "index" not in self.frame.columns
                and self.frame.index.name is None
            ):
                return ["index"]
            else:
                return com.fill_missing_names(self.frame.index.names)

        # for reading: index=(list of) string to specify column to set as index
        elif isinstance(index, str):
            return [index]
        elif isinstance(index, list):
            return index
        else:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py]
    def index(self) -> bool:
        return self.fmt.index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._reindex_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _reindex_indexer(
        self,
        new_index: Index | None,
        indexer: npt.NDArray[np.intp] | None,
    ) -> Series:
        # Note: new_index is None iff indexer is None
        # if not None, indexer is np.intp
        if indexer is None and (
            new_index is None or new_index.names == self.index.names
        ):
            return self.copy(deep=False)

        new_values = algorithms.take_nd(
            self._values, indexer, allow_fill=True, fill_value=None
        )
        return self._constructor(new_values, index=new_index, copy=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_concat_indexes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py]
def _concat_indexes(indexes) -> Index:
    return indexes[0].append(indexes[1:])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.reindex_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def reindex_indexer(
        self,
        new_axis: Index,
        indexer: npt.NDArray[np.intp] | None,
        axis: AxisInt,
        fill_value=None,
        allow_dups: bool = False,
        only_slice: bool = False,
        *,
        use_na_proxy: bool = False,
    ) -> Self:
        """
        Parameters
        ----------
        new_axis : Index
        indexer : ndarray[intp] or None
        axis : int
        fill_value : object, default None
        allow_dups : bool, default False
        only_slice : bool, default False
            Whether to take views, not copies, along columns.
        use_na_proxy : bool, default False
            Whether to use an np.void ndarray for newly introduced columns.

        pandas-indexer with -1's only.
        """
        if indexer is None:
            if new_axis is self.axes[axis]:
                # TODO(CoW) need to handle CoW?
                return self

            result = self.copy(deep=False)
            result.axes = list(self.axes)
            result.axes[axis] = new_axis
            return result

        # Should be intp, but in some cases we get int64 on 32bit builds
        assert isinstance(indexer, np.ndarray)

        # some axes don't allow reindexing with dups
        if not allow_dups:
            self.axes[axis]._validate_can_reindex(indexer)

        if axis >= self.ndim:
            raise IndexError("Requested axis not found in manager")

        if axis == 0:
            new_blocks = list(
                self._slice_take_blocks_ax0(
                    indexer,
                    fill_value=fill_value,
                    only_slice=only_slice,
                    use_na_proxy=use_na_proxy,
                )
            )
        else:
            new_blocks = []
            for blk in self.blocks:
                if blk.dtype == np.void:
                    # GH#58316: np.void placeholders cast to b'' when
                    # reindexed; preserve np.void so _setitem_single_column
                    # can later infer the correct dtype
                    vals = np.empty((blk.values.shape[0], len(indexer)), dtype=np.void)
                    new_blocks.append(NumpyBlock(vals, blk.mgr_locs, ndim=2))
                else:
                    new_blocks.append(
                        blk.take_nd(
                            indexer,
                            axis=1,
                            fill_value=(
                                fill_value if fill_value is not None else blk.fill_value
                            ),
                        )
                    )

        new_axes = list(self.axes)
        new_axes[axis] = new_axis
        if self.ndim == 2:
            new_axes[1 - axis] = self.axes[1 - axis].view()

        new_mgr = type(self).from_blocks(new_blocks, new_axes)
        if axis == 1:
            # We can avoid the need to rebuild these
            new_mgr._blknos = self.blknos.copy()
            new_mgr._blklocs = self.blklocs.copy()
        return new_mgr

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py::SparseFrameAccessor._prep_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py]
    def _prep_index(data, index, columns):
        from pandas.core.indexes.api import (
            default_index,
            ensure_index,
        )

        N, K = data.shape
        if index is None:
            index = default_index(N)
        else:
            index = ensure_index(index)
        if columns is None:
            columns = default_index(K)
        else:
            columns = ensure_index(columns)

        if len(columns) != K:
            raise ValueError(f"Column length mismatch: {len(columns)} vs. {K}")
        if len(index) != N:
            raise ValueError(f"Index length mismatch: {len(index)} vs. {N}")
        return index, columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_take_new_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
def _take_new_index(
    obj: DataFrame | Series,
    indexer: npt.NDArray[np.intp],
    new_index: Index,
) -> DataFrame | Series:
    if isinstance(obj, ABCSeries):
        new_values = algos.take_nd(obj._values, indexer)
        return obj._constructor(new_values, index=new_index, name=obj.name)
    elif isinstance(obj, ABCDataFrame):
        new_mgr = obj._mgr.reindex_indexer(new_axis=new_index, indexer=indexer, axis=1)
        return obj._constructor_from_mgr(new_mgr, axes=new_mgr.axes)
    else:
        raise ValueError("'obj' should be either a Series or a DataFrame")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._reindex_with_indexers [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def _reindex_with_indexers(
        self,
        reindexers,
        fill_value=None,
        allow_dups: bool = False,
    ) -> Self:
        """allow_dups indicates an internal call here"""
        # reindex doing multiple operations on different axes if indicated
        new_data = self._mgr
        for axis in sorted(reindexers.keys()):
            index, indexer = reindexers[axis]
            baxis = self._get_block_manager_axis(axis)

            if index is None:
                continue

            index = ensure_index(index)
            if indexer is not None:
                indexer = ensure_platform_int(indexer)

            # TODO: speed up on homogeneous DataFrame objects (see _reindex_multi)
            new_data = new_data.reindex_indexer(
                index,
                indexer,
                axis=baxis,
                fill_value=fill_value,
                allow_dups=allow_dups,
            )

        if new_data is self._mgr:
            new_data = new_data.copy(deep=False)

        return self._constructor_from_mgr(new_data, axes=new_data.axes).__finalize__(
            self
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/take.py::_take_preprocess_indexer_and_fill_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/take.py]
def _take_preprocess_indexer_and_fill_value(
    arr: np.ndarray,
    indexer: npt.NDArray[np.intp],
    fill_value,
    allow_fill: bool,
    mask: npt.NDArray[np.bool_] | None = None,
):
    mask_info: tuple[np.ndarray | None, bool] | None = None

    if not allow_fill:
        dtype, fill_value = arr.dtype, arr.dtype.type()
        mask_info = None, False
    else:
        # check for promotion based on types only (do this first because
        # it's faster than computing a mask)
        if lib.is_float(fill_value) and fill_value.is_integer():
            # Avoid warning if possible
            fill_value = int(fill_value)
        dtype, fill_value = maybe_promote(arr.dtype, fill_value)
        if dtype != arr.dtype:
            if not (
                (lib.is_float(fill_value) and np.isnan(fill_value))
                or (arr.dtype.kind == "U" and isinstance(fill_value, str))
            ):
                # GH#53910
                warnings.warn(
                    "reindexing with a fill_value that cannot be held by the "
                    "original dtype is deprecated. Explicitly cast to a common "
                    f"dtype (in this case {dtype}) instead.",
                    Pandas4Warning,
                    stacklevel=find_stack_level(),
                )
            # check if promotion is actually required based on indexer
            if mask is not None:
                needs_masking = True
            else:
                mask = indexer == -1
                needs_masking = bool(mask.any())
            mask_info = mask, needs_masking
            if not needs_masking:
                # if not, then depromote, set fill_value to dummy
                # (it won't be used but we don't want the cython code
                # to crash when trying to cast it to dtype)
                dtype, fill_value = arr.dtype, arr.dtype.type()

    return dtype, fill_value, mask_info

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._maybe_cast_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py]
    def _maybe_cast_indexer(self, key) -> int:
        # GH#41933: we have to do this instead of self._data._validate_scalar
        #  because this will correctly get partial-indexing on Interval categories
        try:
            return self._data._unbox_scalar(key)
        except KeyError:
            if is_valid_na_for_dtype(key, self.categories.dtype):
                return -1
            raise

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py]
    def index(self, value: Any, start: int = ..., stop: int = ..., /) -> int: ...

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._wrap_reindex_result [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py]
    def _wrap_reindex_result(
        self, target: Index, indexer: npt.NDArray[np.intp] | None, preserve_names: bool
    ) -> Index:
        if not isinstance(target, type(self)) and target.dtype.kind == "i":
            target = self._shallow_copy(target._values, name=target.name)
        return super()._wrap_reindex_result(target, indexer, preserve_names)
```
