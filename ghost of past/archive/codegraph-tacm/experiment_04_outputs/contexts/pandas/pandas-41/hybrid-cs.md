# pandas-41 :: hybrid-cs

query: BUG: ExtensionBlock.set not setting values inplace (#32831)

## selected nodes

- rank=1 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=2 layer=FUNCTION tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.set_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=3 layer=FUNCTION tokens=391 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.column_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=4 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=5 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=6 layer=FUNCTION tokens=455 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._setitem_single_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=7 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=8 layer=FUNCTION tokens=546 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=9 layer=FUNCTION tokens=309 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.setitem_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=10 layer=FUNCTION tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents._check_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=11 layer=FUNCTION tokens=730 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=12 layer=FUNCTION tokens=503 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block._replace_regex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=13 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.arange_result file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__setitem__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def __setitem__(self, key, value) -> None:
        if self._readonly:
            raise ValueError("Cannot modify read-only array")
        # I suppose we could allow setting of non-fill_value elements.
        # TODO(SparseArray.__setitem__): remove special cases in
        # ExtensionBlock.where
        msg = "SparseArray does not support item assignment via setitem"
        raise TypeError(msg)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.column_setitem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def column_setitem(
        self, loc: int, idx: int | slice | np.ndarray, value, inplace_only: bool = False
    ) -> None:
        """
        Set values ("setitem") into a single column (not setting the full column).

        This is a method on the BlockManager level, to avoid creating an
        intermediate Series at the DataFrame level (`s = df[loc]; s[idx] = value`)
        """
        if not self._has_no_reference(loc):
            blkno = self.blknos[loc]
            # Split blocks to only copy the column we want to modify
            blk_loc = self.blklocs[loc]
            # Copy our values
            values = self.blocks[blkno].values
            if values.ndim == 1:
                values = values.copy()
            else:
                # Use [blk_loc] as indexer to keep ndim=2, this already results in a
                # copy
                values = values[[blk_loc]]
            self._iset_split_block(blkno, [blk_loc], values)

        # this manager is only created temporarily to mutate the values in place
        # so don't track references, otherwise the `setitem` would perform CoW again
        col_mgr = self.iget(loc, track_ref=False)
        if inplace_only:
            col_mgr.setitem_inplace(idx, value)
        else:
            new_mgr = col_mgr.setitem((idx,), value)
            self.iset(loc, new_mgr._block.values, inplace=True)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None:
        # When an ndarray, we should have locs.tolist() == [0]
        # When a BlockPlacement we should have list(locs) == [0]
        if copy:
            self.values = self.values.copy()
        self.values[:] = values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._setitem_single_block [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _setitem_single_block(self, indexer, value, name: str) -> None:
        """
        _setitem_with_indexer for the case when we have a single Block.
        """
        from pandas import Series

        if (isinstance(value, ABCSeries) and name != "iloc") or isinstance(value, dict):
            # TODO(EA): ExtensionBlock.setitem this causes issues with
            # setting for extensionarrays that store dicts. Need to decide
            # if it's worth supporting that.
            value = self._align_series(indexer, Series(value))

        info_axis = self.obj._info_axis_number
        item_labels = self.obj._get_axis(info_axis)
        if isinstance(indexer, tuple):
            # if we are setting on the info axis ONLY
            # set using those methods to avoid block-splitting
            # logic here
            if (
                self.ndim == len(indexer) == 2
                and is_integer(indexer[1])
                and com.is_null_slice(indexer[0])
            ):
                col = item_labels[indexer[info_axis]]
                if len(item_labels.get_indexer_for([col])) == 1:
                    # e.g. test_loc_setitem_empty_append_expands_rows
                    loc = item_labels.get_loc(col)
                    self._setitem_single_column(loc, value, indexer[0])
                    return

            indexer = maybe_convert_ix(*indexer)  # e.g. test_setitem_frame_align

        if isinstance(value, ABCDataFrame) and name != "iloc":
            value = self._align_frame(indexer, value)._values

        # actually do the set
        self.obj._mgr = self.obj._mgr.setitem(indexer=indexer, value=value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _set_with_engine(self, key, value) -> None:
        loc = self.index.get_loc(key)

        # this is equivalent to self._values[key] = value
        self._mgr.setitem_inplace(loc, value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.__setitem__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def __setitem__(self, key, value) -> None:
        """
        Set one or more values inplace.

        This method is not required to satisfy the pandas extension array
        interface.

        Parameters
        ----------
        key : int, ndarray, or slice
            When called from, e.g. ``Series.__setitem__``, ``key`` will be
            one of

            * scalar int
            * ndarray of integers.
            * boolean ndarray
            * slice object

        value : ExtensionDtype.type, Sequence[ExtensionDtype.type], or object
            value or values to be set of ``key``.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the array is readonly and modification is attempted.
        """
        # Some notes to the ExtensionArray implementer who may have ended up
        # here. While this method is not required for the interface, if you
        # *do* choose to implement __setitem__, then some semantics should be
        # observed:
        #
        # * Setting multiple values : ExtensionArrays should support setting
        #   multiple values at once, 'key' will be a sequence of integers and
        #  'value' will be a same-length sequence.
        #
        # * Broadcasting : For a sequence 'key' and a scalar 'value',
        #   each position in 'key' should be set to 'value'.
        #
        # * Coercion : Most users will expect basic coercion to work. For
        #   example, a string like '2018-01-01' is coerced to a datetime
        #   when setting on a datetime64ns array. In general, if the
        #   __init__ method coerces that value, then so should __setitem__
        # Note, also, that Series/DataFrame.where internally use __setitem__
        # on a copy of the data.
        # Check if the array is readonly
        if self._readonly:
            raise ValueError("Cannot modify read-only array")

        raise NotImplementedError(f"{type(self)} does not implement __setitem__.")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents._check_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py]
    def _check_inplace(self, is_inplace, orig, arr, obj):
        if is_inplace is None:
            # We are not (yet) checking whether setting is inplace or not
            pass
        elif is_inplace:
            if arr.dtype.kind in ["m", "M"]:
                # We may not have the same DTA/TDA, but will have the same
                #  underlying data
                assert arr._ndarray is obj._values._ndarray
            else:
                assert obj._values is arr
        else:
            # otherwise original array should be unchanged
            tm.assert_equal(arr, orig._values)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.setitem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def setitem(self, indexer, value) -> Self:
        """
        Set values with indexer.

        For SingleBlockManager, this backs s[indexer] = value
        """
        if isinstance(indexer, np.ndarray) and indexer.ndim > self.ndim:
            raise ValueError(f"Cannot set values with ndim > {self.ndim}")

        if not self._has_no_reference(0):
            # this method is only called if there is a single block -> hardcoded 0
            # Split blocks to only copy the columns we want to modify
            if self.ndim == 2 and isinstance(indexer, tuple):
                blk_loc = self.blklocs[indexer[1]]
                if is_list_like(blk_loc) and blk_loc.ndim == 2:
                    blk_loc = np.squeeze(blk_loc, axis=0)
                elif not is_list_like(blk_loc):
                    # Keep dimension and copy data later
                    blk_loc = [blk_loc]  # type: ignore[assignment]
                if len(blk_loc) == 0:
                    return self.copy(deep=False)

                values = self.blocks[0].values
                if values.ndim == 2:
                    values = values[blk_loc]
                    # "T" has no attribute "_iset_split_block"
                    self._iset_split_block(  # type: ignore[attr-defined]
                        0, blk_loc, values
                    )

                    indexer = list(indexer)
                    # first block equals values we are setting to -> set to all columns
                    if lib.is_integer(indexer[1]):
                        col_indexer = 0
                    elif len(blk_loc) > 1:
                        col_indexer = slice(None)  # type: ignore[assignment]
                    else:
                        col_indexer = np.arange(len(blk_loc))  # type: ignore[assignment]
                    indexer[1] = col_indexer

                    row_indexer = indexer[0]
                    if isinstance(row_indexer, np.ndarray) and row_indexer.ndim == 2:
                        # numpy cannot handle a 2d indexer in combo with a slice
                        row_indexer = np.squeeze(row_indexer, axis=1)
                    if isinstance(row_indexer, np.ndarray) and len(row_indexer) == 0:
                        # numpy does not like empty indexer combined with slice
                        # and we are setting nothing anyway
                        return self
                    indexer[0] = row_indexer
                    self.blocks[0].setitem(tuple(indexer), value)
                    return self
            # No need to split if we either set all columns or on a single block
            # manager
            self = self.copy(deep=True)

        return self.apply("setitem", indexer=indexer, value=value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block._replace_regex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def _replace_regex(
        self,
        to_replace,
        value,
        inplace: bool = False,
        mask=None,
    ) -> list[Block]:
        """
        Replace elements by the given value.

        Parameters
        ----------
        to_replace : object or pattern
            Scalar to replace or regular expression to match.
        value : object
            Replacement object.
        inplace : bool, default False
            Perform inplace modification.
        mask : array-like of bool, optional
            True indicate corresponding element is ignored.

        Returns
        -------
        List[Block]
        """
        if not is_re(to_replace) and not self._can_hold_element(to_replace):
            # i.e. only if self.is_object is True, but could in principle include a
            #  String ExtensionBlock
            return [self.copy(deep=False)]

        if is_re(to_replace) and self.dtype not in [object, "string"]:
            # only object or string dtype can hold strings, and a regex object
            # will only match strings
            return [self.copy(deep=False)]

        if not (
            self._can_hold_element(value) or (self.dtype == "string" and is_re(value))
        ):
            # GH#57733 - astype to object may return a block sharing memory
            # with self (e.g. StringArray backed by object ndarray). Since
            # replace_regex mutates values in-place, we must ensure the
            # block's data is independent.
            block = self.astype(np.dtype(object))
            if astype_is_view(self.dtype, np.dtype(object)):
                block = block._maybe_copy(inplace=True)
        else:
            block = self._maybe_copy(inplace)

        rx = re.compile(to_replace)

        replace_regex(block.values, rx, value, mask)
        return [block]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.arange_result [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
    def arange_result(self) -> npt.NDArray[np.intp]:
        # We cache this for reuse in ExtensionBlock._unstack
        dummy_arr = np.arange(len(self.index), dtype=np.intp)
        return self.get_new_values(dummy_arr, fill_value=-1)
```
