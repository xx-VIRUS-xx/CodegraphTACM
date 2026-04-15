# pandas-41 :: minilm

query: BUG: ExtensionBlock.set not setting values inplace (#32831)

## selected nodes

- rank=1 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=2 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=3 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=4 layer=FUNCTION tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.set_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=5 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::JoinUnit.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=6 layer=FUNCTION tokens=309 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.setitem_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=7 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents.is_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=8 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::EABackedBlock.shift file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=9 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/config/test_config.py::TestConfig.clean_config file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/config/test_config.py
- rank=10 layer=FUNCTION tokens=498 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager._iset_split_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=11 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.make_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=12 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block._unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=13 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager._blknos file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=14 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager._blklocs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=15 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=16 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.any_extension_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=17 layer=FUNCTION tokens=332 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager._iset_single file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=18 layer=FUNCTION tokens=533 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::EABackedBlock.setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=19 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.mgr_locs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=20 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/accessor.py::PandasDelegate._delegate_property_set file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/accessor.py
- rank=21 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py::IndexOpsMixin._values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py
- rank=22 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::new_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=23 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.set_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None:
        """
        Modify block values in-place with new item value.

        If copy=True, first copy the underlying values in place before modifying
        (for Copy-on-Write).

        Notes
        -----
        `set_inplace` never creates a new array or new Block, whereas `setitem`
        _may_ create a new array and always creates a new Block.

        Caller is responsible for checking values.dtype == self.dtype.
        """
        if copy:
            self.values = self.values.copy()
        self.values[locs] = values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__setitem__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def __setitem__(self, key, value) -> None:
        if self._readonly:
            raise ValueError("Cannot modify read-only array")
        # I suppose we could allow setting of non-fill_value elements.
        # TODO(SparseArray.__setitem__): remove special cases in
        # ExtensionBlock.where
        msg = "SparseArray does not support item assignment via setitem"
        raise TypeError(msg)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None:
        # When an ndarray, we should have locs.tolist() == [0]
        # When a BlockPlacement we should have list(locs) == [0]
        if copy:
            self.values = self.values.copy()
        self.values[:] = values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.set_values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def set_values(self, values: ArrayLike) -> None:
        """
        Set the values of the single block in place.

        Use at your own risk! This does not check if the passed values are
        valid for the current Block/SingleBlockManager (length, dtype, etc),
        and this does not properly keep track of references.
        """
        # NOTE(CoW) Currently this is only used for FrameColumnApply.series_generator
        # which handles CoW by setting the refs manually if necessary
        self.blocks[0].values = values
        self.blocks[0]._mgr_locs = BlockPlacement(slice(len(values)))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::JoinUnit.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py]
    def __init__(self, block: Block) -> None:
        self.block = block

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.setitem_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def setitem_inplace(self, indexer, value) -> None:
        """
        Set values with indexer.

        For SingleBlockManager, this backs s[indexer] = value

        This is an inplace version of `setitem()`, mutating the manager/values
        in place, not returning a new Manager (and Block), and thus never changing
        the dtype.
        """
        if not self._has_no_reference(0):
            self.blocks = (self._block.copy(deep=True),)
            self._reset_cache()

        arr = self.array

        # EAs will do this validation in their own __setitem__ methods.
        if isinstance(arr, np.ndarray):
            # Note: checking for ndarray instead of np.dtype means we exclude
            #  dt64/td64, which do their own validation.
            value = np_can_hold_element(arr.dtype, value)

        if isinstance(value, np.ndarray) and value.ndim == 1 and len(value) == 1:
            # NumPy 1.25 deprecation: https://github.com/numpy/numpy/pull/10615
            value = value[0, ...]

        arr[indexer] = value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents.is_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py]
    def is_inplace(self, obj, expected):
        """
        Whether we expect the setting to be in-place or not.
        """
        return expected.dtype == obj.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::EABackedBlock.shift [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def shift(self, periods: int, fill_value: Any = None) -> list[Block]:
        """
        Shift the block by `periods`.

        Dispatches to underlying ExtensionArray and re-boxes in an
        ExtensionBlock.
        """
        new_values = self.values.shift(periods=periods, fill_value=fill_value)
        return [self.make_block_same_class(new_values)]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/config/test_config.py::TestConfig.clean_config [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/config/test_config.py]
    def clean_config(self, monkeypatch):
        with monkeypatch.context() as m:
            m.setattr(cf, "_global_config", {})
            m.setattr(cf, "options", cf.DictWrapper(cf._global_config))
            m.setattr(cf, "_deprecated_options", {})
            m.setattr(cf, "_registered_options", {})

            # Our test fixture in conftest.py sets "chained_assignment"
            # to "raise" only after all test methods have been setup.
            # However, after this setup, there is no longer any
            # "chained_assignment" option, so re-register it.
            cf.register_option("chained_assignment", "raise")
            yield

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager._iset_split_block [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def _iset_split_block(
        self,
        blkno_l: int,
        blk_locs: np.ndarray | list[int],
        value: ArrayLike | None = None,
        refs: BlockValuesRefs | None = None,
    ) -> None:
        """Removes columns from a block by splitting the block.

        Avoids copying the whole block through slicing and updates the manager
        after determining the new block structure. Optionally adds a new block,
        otherwise has to be done by the caller.

        Parameters
        ----------
        blkno_l: The block number to operate on, relevant for updating the manager
        blk_locs: The locations of our block that should be deleted.
        value: The value to set as a replacement.
        refs: The reference tracking object of the value to set.
        """
        blk = self.blocks[blkno_l]

        if self._blklocs is None:
            self._rebuild_blknos_and_blklocs()

        nbs_tup = tuple(blk.delete(blk_locs))
        if value is not None:
            locs = blk.mgr_locs.as_array[blk_locs]
            first_nb = new_block_2d(value, BlockPlacement(locs), refs=refs)
        else:
            first_nb = nbs_tup[0]
            nbs_tup = tuple(nbs_tup[1:])

        nr_blocks = len(self.blocks)
        blocks_tup = (
            *self.blocks[:blkno_l],
            first_nb,
            *self.blocks[blkno_l + 1 :],
            *nbs_tup,
        )
        self.blocks = blocks_tup

        if not nbs_tup and value is not None:
            # No need to update anything if split did not happen
            return

        self._blklocs[first_nb.mgr_locs.indexer] = np.arange(len(first_nb))

        for i, nb in enumerate(nbs_tup):
            self._blklocs[nb.mgr_locs.indexer] = np.arange(len(nb))
            self._blknos[nb.mgr_locs.indexer] = i + nr_blocks

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.make_block [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def make_block(
        self,
        values,
        placement: BlockPlacement | None = None,
        refs: BlockValuesRefs | None = None,
    ) -> Block:
        """
        Create a new block, with type inference propagate any values that are
        not specified
        """
        if placement is None:
            placement = self._mgr_locs
        if self.is_extension:
            values = ensure_block_shape(values, ndim=self.ndim)

        return new_block(values, placement=placement, ndim=self.ndim, refs=refs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block._unstack [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def _unstack(
        self,
        unstacker,
        fill_value,
        new_placement: npt.NDArray[np.intp],
        needs_masking: npt.NDArray[np.bool_],
    ):
        """
        Return a list of unstacked blocks of self

        Parameters
        ----------
        unstacker : reshape._Unstacker
        fill_value : int
            Only used in ExtensionBlock._unstack
        new_placement : np.ndarray[np.intp]
        needs_masking : np.ndarray[bool]
            Only used in ExtensionBlock._unstack

        Returns
        -------
        blocks : list of Block
            New blocks of unstacked values.
        """
        new_values = unstacker.get_new_values(self.values.T, fill_value=fill_value)

        bp = BlockPlacement(new_placement)
        blocks = [new_block_2d(new_values.T, placement=bp)]
        return blocks

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager._blknos [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def _blknos(self) -> None:  # type: ignore[override]
        """compat with BlockManager"""
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager._blklocs [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def _blklocs(self) -> None:  # type: ignore[override]
        """compat with BlockManager"""
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _set_with_engine(self, key, value) -> None:
        loc = self.index.get_loc(key)

        # this is equivalent to self._values[key] = value
        self._mgr.setitem_inplace(loc, value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.any_extension_types [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def any_extension_types(self) -> bool:
        """Whether any of the blocks in this manager are extension blocks"""
        return any(block.is_extension for block in self.blocks)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager._iset_single [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def _iset_single(
        self,
        loc: int,
        value: ArrayLike,
        inplace: bool,
        blkno: int,
        blk: Block,
        refs: BlockValuesRefs | None = None,
    ) -> None:
        """
        Fastpath for iset when we are only setting a single position and
        the Block currently in that position is itself single-column.

        In this case we can swap out the entire Block and blklocs and blknos
        are unaffected.
        """
        # Caller is responsible for verifying value.shape

        if inplace and blk.should_store(value):
            copy = not self._has_no_reference_block(blkno)
            iloc = self.blklocs[loc]
            blk.set_inplace(slice(iloc, iloc + 1), value, copy=copy)
            return

        nb = new_block_2d(value, placement=blk._mgr_locs, refs=refs)
        old_blocks = self.blocks
        new_blocks = (*old_blocks[:blkno], nb, *old_blocks[blkno + 1 :])
        # Invalidate cache before mutating blocks so that a concurrent
        # reader never sees stale cache + new blocks.
        self._interleaved_dtype = None
        self.blocks = new_blocks
        return

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::EABackedBlock.setitem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def setitem(self, indexer, value):
        """
        Attempt self.values[indexer] = value, possibly creating a new array.

        This differs from Block.setitem by not allowing setitem to change
        the dtype of the Block.

        Parameters
        ----------
        indexer : tuple, list-like, array-like, slice, int
            The subset of self.values to set
        value : object
            The value being set

        Returns
        -------
        Block

        Notes
        -----
        `indexer` is a direct slice/positional indexer. `value` must
        be a compatible shape.
        """
        orig_indexer = indexer
        orig_value = value

        indexer = self._unwrap_setitem_indexer(indexer)
        value = self._maybe_squeeze_arg(value)

        values = self.values
        if values.ndim == 2:
            # GH#45419 Adapt indexer/value to storage layout (nblocks, nrows)
            #  instead of transposing values, since EA.T may not be a view.
            if not isinstance(indexer, tuple):
                indexer = (indexer, slice(None))
            if len(indexer) == 2:
                indexer = indexer[::-1]
            if isinstance(value, np.ndarray) and value.ndim == 2:
                value = value.T
        check_setitem_lengths(indexer, value, values)

        try:
            values[indexer] = value
        except (ValueError, TypeError):
            if isinstance(self.dtype, IntervalDtype):
                # see TestSetitemFloatIntervalWithIntIntervalValues
                nb = self.coerce_to_target_dtype(orig_value, raise_on_upcast=True)
                return nb.setitem(orig_indexer, orig_value)

            elif isinstance(self, NDArrayBackedExtensionBlock):
                nb = self.coerce_to_target_dtype(orig_value, raise_on_upcast=True)
                return nb.setitem(orig_indexer, orig_value)

            else:
                raise

        else:
            return self

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.mgr_locs [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def mgr_locs(self, new_mgr_locs: BlockPlacement) -> None:
        self._mgr_locs = new_mgr_locs

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/accessor.py::PandasDelegate._delegate_property_set [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/accessor.py]
    def _delegate_property_set(self, name: str, value, *args, **kwargs) -> None:
        raise TypeError(f"The property {name} cannot be set")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py::IndexOpsMixin._values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py]
    def _values(self) -> ExtensionArray | np.ndarray:
        # must be defined here as a property for mypy
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::new_block [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
def new_block(
    values,
    placement: BlockPlacement,
    *,
    ndim: int,
    refs: BlockValuesRefs | None = None,
) -> Block:
    # caller is responsible for ensuring:
    # - values is NOT a NumpyExtensionArray
    # - check_ndim/ensure_block_shape already checked
    # - maybe_coerce_values already called/unnecessary
    klass = get_block_type(values.dtype)
    return klass(values, ndim=ndim, placement=placement, refs=refs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::setitem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def setitem(x):
    return x
```
