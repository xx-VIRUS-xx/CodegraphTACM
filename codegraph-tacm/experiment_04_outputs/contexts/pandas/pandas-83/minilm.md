# pandas-83 :: minilm

query: BUG: concat not copying index and columns when copy=True (#31119)

## selected nodes

- rank=1 layer=FUNCTION tokens=899 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::concatenate_managers file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=2 layer=FUNCTION tokens=487 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._concat_same_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=3 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_concat_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=4 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.concat_horizontal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=5 layer=FUNCTION tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py::SparseFrameAccessor._prep_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py
- rank=6 layer=FUNCTION tokens=570 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._concat_objects file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=7 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.concat_vertical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=8 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/array_with_attr/array.py::FloatAttrArray._concat_same_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/array_with_attr/array.py
- rank=9 layer=FUNCTION tokens=1164 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=10 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._concat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::concatenate_managers [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py]
def concatenate_managers(
    mgrs_indexers, axes: list[Index], concat_axis: AxisInt, copy: bool
) -> BlockManager:
    """
    Concatenate block managers into one.

    Parameters
    ----------
    mgrs_indexers : list of (BlockManager, {axis: indexer,...}) tuples
    axes : list of Index
    concat_axis : int
    copy : bool

    Returns
    -------
    BlockManager
    """

    needs_copy = copy and concat_axis == 0

    # Assertions disabled for performance
    # for tup in mgrs_indexers:
    #    # caller is responsible for ensuring this
    #    indexers = tup[1]
    #    assert concat_axis not in indexers

    if concat_axis == 0:
        mgrs = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers, needs_copy)
        return mgrs[0].concat_horizontal(mgrs, axes)

    if len(mgrs_indexers) > 0 and mgrs_indexers[0][0].nblocks > 0:
        first_dtype = mgrs_indexers[0][0].blocks[0].dtype
        if first_dtype in [np.float64, np.float32]:
            # TODO: support more dtypes here.  This will be simpler once
            #  JoinUnit.is_na behavior is deprecated.
            #  (update 2024-04-13 that deprecation has been enforced)
            if (
                all(_is_homogeneous_mgr(mgr, first_dtype) for mgr, _ in mgrs_indexers)
                and len(mgrs_indexers) > 1
            ):
                # Fastpath!
                # Length restriction is just to avoid having to worry about 'copy'
                shape = tuple(len(x) for x in axes)
                nb = _concat_homogeneous_fastpath(mgrs_indexers, shape, first_dtype)
                return BlockManager((nb,), axes)

    mgrs = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers, needs_copy)

    if len(mgrs) == 1:
        mgr = mgrs[0]
        out = mgr.copy(deep=False)
        out.axes = axes
        return out

    blocks = []
    values: ArrayLike

    for placement, join_units in _get_combined_plan(mgrs):
        unit = join_units[0]
        blk = unit.block

        if _is_uniform_join_units(join_units):
            vals = [ju.block.values for ju in join_units]

            if not blk.is_extension:
                # _is_uniform_join_units ensures a single dtype, so
                #  we can use np.concatenate, which is more performant
                #  than concat_compat
                # error: Argument 1 to "concatenate" has incompatible type
                # "List[Union[ndarray[Any, Any], ExtensionArray]]";
                # expected "Union[_SupportsArray[dtype[Any]],
                # _NestedSequence[_SupportsArray[dtype[Any]]]]"
                values = np.concatenate(vals, axis=1)  # type: ignore[arg-type]
            elif is_1d_only_ea_dtype(blk.dtype):
                # TODO(EA2D): special-casing not needed with 2D EAs
                values = concat_compat(vals, axis=0, ea_compat_axis=True)
                values = ensure_block_shape(values, ndim=2)
            else:
                values = concat_compat(vals, axis=1)

            values = ensure_wrapped_if_datetimelike(values)

            fastpath = blk.values.dtype == values.dtype
        else:
            values = _concatenate_join_units(join_units, copy=copy)
            fastpath = False

        if fastpath:
            b = blk.make_block_same_class(values, placement=placement)
        else:
            b = new_block_2d(values, placement=placement)

        blocks.append(b)

    return BlockManager(tuple(blocks), axes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._concat_same_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def _concat_same_type(cls, to_concat: Sequence[Self]) -> Self:
        fill_value = to_concat[0].fill_value

        values = []
        length = 0

        if to_concat:
            sp_kind = to_concat[0].kind
        else:
            sp_kind = "integer"

        sp_index: SparseIndex
        if sp_kind == "integer":
            indices = []

            for arr in to_concat:
                int_idx = arr.sp_index.indices.copy()
                int_idx += length  # TODO: wraparound
                length += arr.sp_index.length

                values.append(arr.sp_values)
                indices.append(int_idx)

            data = np.concatenate(values)
            indices_arr = np.concatenate(indices)
            sp_index = IntIndex(length, indices_arr)

        else:
            # when concatenating block indices, we don't claim that you'll
            # get an identical index as concatenating the values and then
            # creating a new index. We don't want to spend the time trying
            # to merge blocks across arrays in `to_concat`, so the resulting
            # BlockIndex may have more blocks.
            blengths = []
            blocs = []

            for arr in to_concat:
                block_idx = arr.sp_index.to_block_index()

                values.append(arr.sp_values)
                blocs.append(block_idx.blocs.copy() + length)
                blengths.append(block_idx.blengths)
                length += arr.sp_index.length

            data = np.concatenate(values)
            blocs_arr = np.concatenate(blocs)
            blengths_arr = np.concatenate(blengths)

            sp_index = BlockIndex(length, blocs_arr, blengths_arr)

        return cls(data, sparse_index=sp_index, fill_value=fill_value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_concat_indexes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py]
def _concat_indexes(indexes) -> Index:
    return indexes[0].append(indexes[1:])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.concat_horizontal [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def concat_horizontal(cls, mgrs: list[Self], axes: list[Index]) -> Self:
        """
        Concatenate uniformly-indexed BlockManagers horizontally.
        """
        offset = 0
        blocks: list[Block] = []
        for mgr in mgrs:
            for blk in mgr.blocks:
                # We need to do getitem_block here otherwise we would be altering
                #  blk.mgr_locs in place, which would render it invalid. This is only
                #  relevant in the copy=False case.
                nb = blk.slice_block_columns(slice(None))
                nb._mgr_locs = nb._mgr_locs.add(offset)
                blocks.append(nb)

            offset += len(mgr.items)

        # TODO relevant axis already shallow-copied at caller?
        new_mgr = cls(tuple(blocks), axes)
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._concat_objects [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py]
    def _concat_objects(
        self,
        values,
        not_indexed_same: bool = False,
        is_transform: bool = False,
    ):
        from pandas.core.reshape.concat import concat

        if self.group_keys and not is_transform:
            if self.as_index:
                # possible MI return case
                group_keys = self._grouper.result_index
                group_levels = self._grouper.levels
                group_names = self._grouper.names

                result = concat(
                    values,
                    axis=0,
                    keys=group_keys,
                    levels=group_levels,
                    names=group_names,
                    sort=False,
                )
            else:
                result = concat(values, axis=0)

        elif not not_indexed_same:
            result = concat(values, axis=0)

            ax = self._selected_obj.index
            if self.dropna:
                labels = self._grouper.ids
                mask = labels != -1
                ax = ax[mask]

            # this is a very unfortunate situation
            # we can't use reindex to restore the original order
            # when the ax has duplicates
            # so we resort to this
            # GH 14776, 30667
            # TODO: can we reuse e.g. _reindex_non_unique?
            if ax.has_duplicates and not result.axes[0].equals(ax):
                # e.g. test_category_order_transformer
                target = algorithms.unique1d(ax._values)
                indexer, _ = result.index.get_indexer_non_unique(target)
                result = result.take(indexer, axis=0)
            else:
                result = result.reindex(ax, axis=0)

        else:
            result = concat(values, axis=0)

        if self.obj.ndim == 1:
            name = self.obj.name
        elif is_hashable(self._selection):
            name = self._selection
        else:
            name = None

        if isinstance(result, Series) and name is not None:
            result.name = name

        return result.__finalize__(self.obj, method="groupby")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.concat_vertical [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def concat_vertical(cls, mgrs: list[Self], axes: list[Index]) -> Self:
        """
        Concatenate uniformly-indexed BlockManagers vertically.
        """
        raise NotImplementedError("This logic lives (for now) in internals.concat")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/array_with_attr/array.py::FloatAttrArray._concat_same_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/array_with_attr/array.py]
    def _concat_same_type(cls, to_concat):
        data = np.concatenate([x.data for x in to_concat])
        attr = to_concat[0].attr if len(to_concat) else None
        return cls(data, attr)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.__new__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def __new__(
        cls,
        data: Any = None,
        dtype: Dtype | None = None,
        copy: bool | None = None,
        name: Hashable = None,
        tupleize_cols: bool = True,
    ) -> Self:
        from pandas.core.indexes.range import RangeIndex

        name = maybe_extract_name(name, data, cls)

        if dtype is not None:
            dtype = pandas_dtype(dtype)

        data_dtype = getattr(data, "dtype", None)

        refs = None
        if not copy and isinstance(data, (ABCSeries, Index)):
            refs = data._references

        # GH 63306, GH 63388
        data, copy = cls._maybe_copy_array_input(data, copy, dtype)

        # range
        if isinstance(data, (range, RangeIndex)):
            result = RangeIndex(start=data, copy=bool(copy), name=name)
            if dtype is not None:
                return result.astype(dtype, copy=False)  # type: ignore[return-value]  # pyright: ignore[reportReturnType]
            # error: Incompatible return value type (got "MultiIndex",
            # expected "Self")
            return result  # type: ignore[return-value]

        elif is_ea_or_datetimelike_dtype(dtype):
            # non-EA dtype indexes have special casting logic, so we punt here
            if isinstance(data, (set, frozenset)):
                data = list(data)

        elif is_ea_or_datetimelike_dtype(data_dtype):
            pass

        elif isinstance(data, (np.ndarray, ABCMultiIndex)):
            if isinstance(data, ABCMultiIndex):
                data = data._values

            if data.dtype.kind not in "iufcbmM":
                # GH#11836 we need to avoid having numpy coerce
                # things that look like ints/floats to ints unless
                # they are actually ints, e.g. '0' and 0.0
                # should not be coerced
                data = com.asarray_tuplesafe(data, dtype=_dtype_obj)
        elif isinstance(data, (ABCSeries, Index)):
            # GH 56244: Avoid potential inference on object types
            pass
        elif is_scalar(data):
            raise cls._raise_scalar_data_error(data)
        elif hasattr(data, "__array__"):
            return cls(np.asarray(data), dtype=dtype, copy=copy, name=name)
        elif not is_list_like(data) and not isinstance(data, memoryview):
            # 2022-11-16 the memoryview check is only necessary on some CI
            #  builds, not clear why
            raise cls._raise_scalar_data_error(data)

        else:
            if tupleize_cols:
                # GH21470: convert iterable to list before determining if empty
                if is_iterator(data):
                    data = list(data)

                if data and all(isinstance(e, tuple) for e in data):
                    # we must be all tuples, otherwise don't construct
                    # 10697
                    from pandas.core.indexes.multi import MultiIndex

                    # error: Incompatible return value type (got "MultiIndex",
                    # expected "Self")
                    return MultiIndex.from_tuples(  # type: ignore[return-value]
                        data, names=name
                    )
            # other iterable of some kind

            if not isinstance(data, (list, tuple)):
                # we allow set/frozenset, which Series/sanitize_array does not, so
                #  cast to list here
                data = list(data)
            if len(data) == 0:
                # unlike Series, we default to object dtype:
                data = np.array(data, dtype=object)

            if len(data) and isinstance(data[0], tuple):
                # Ensure we get 1-D array of tuples instead of 2D array.
                data = com.asarray_tuplesafe(data, dtype=_dtype_obj)

        try:
            arr = sanitize_array(data, None, dtype=dtype, copy=bool(copy))
        except ValueError as err:
            if "index must be specified when data is not list-like" in str(err):
                raise cls._raise_scalar_data_error(data) from err
            if "Data must be 1-dimensional" in str(err):
                raise ValueError("Index data must be 1-dimensional") from err
            raise
        arr = ensure_wrapped_if_datetimelike(arr)  # type: ignore[no-untyped-call]

        klass = cls._dtype_to_subclass(arr.dtype)

        arr = klass._ensure_array(arr, arr.dtype, copy=False)
        return klass._simple_new(arr, name, refs=refs)  # type: ignore[return-value]  # pyright: ignore[reportReturnType]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._concat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _concat(self, to_concat: list[Index], name: Hashable) -> Index:
        """
        Concatenate multiple Index objects.
        """
        to_concat_vals = [x._values for x in to_concat]

        result = concat_compat(to_concat_vals)

        return Index._with_infer(result, name=name, copy=False)
```
