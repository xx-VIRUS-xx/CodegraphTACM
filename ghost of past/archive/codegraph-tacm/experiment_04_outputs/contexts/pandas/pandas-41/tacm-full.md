# pandas-41 :: tacm-full

query: BUG: ExtensionBlock.set not setting values inplace (#32831)

## selected nodes

- rank=1 layer=FUNCTION tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents._check_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=2 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents.is_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=3 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestCanHoldElement.check_series_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py
- rank=4 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=5 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=6 layer=FUNCTION tokens=391 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.column_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=7 layer=FUNCTION tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.set_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=8 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=9 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=10 layer=FUNCTION tokens=470 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._iset_not_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=11 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=12 layer=FUNCTION tokens=546 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=13 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.replace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=14 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Fillna.time_fillna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=15 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=16 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=17 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block._unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents.is_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py]
    def is_inplace(self, obj, expected):
        """
        Whether we expect the setting to be in-place or not.
        """
        return expected.dtype == obj.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestCanHoldElement.check_series_setitem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py]
    def check_series_setitem(self, elem, index: Index, inplace: bool):
        arr = index._data.copy()
        ser = Series(arr, copy=False)

        self.check_can_hold_element(ser, elem, inplace)

        if is_scalar(elem):
            ser[0] = elem
        else:
            ser[: len(elem)] = elem

        if inplace:
            assert ser._values is arr  # i.e. setting was done inplace
        else:
            assert ser.dtype == object

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__setitem__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def __setitem__(self, key, value) -> None:
        if self._readonly:
            raise ValueError("Cannot modify read-only array")
        # I suppose we could allow setting of non-fill_value elements.
        # TODO(SparseArray.__setitem__): remove special cases in
        # ExtensionBlock.where
        msg = "SparseArray does not support item assignment via setitem"
        raise TypeError(msg)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_name [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _set_name(self, name, inplace: bool = False) -> Series:
        """
        Set the Series name.

        Parameters
        ----------
        name : str
        inplace : bool
            Whether to modify `self` directly or return a copy.
        """
        inplace = validate_bool_kwarg(inplace, "inplace")
        ser = self if inplace else self.copy(deep=False)
        ser.name = name
        return ser

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py]
    def len(self):
        """
        Compute the length of each element in the Series/Index.

        The element may be a sequence (such as a string, tuple or list) or a collection
        (such as a dictionary).

        Returns
        -------
        Series or Index of int
            A Series or Index of integer values indicating the length of each
            element in the Series or Index.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.

        Examples
        --------
        Returns the length (number of characters) in a string. Returns the
        number of entries for dictionaries, lists or tuples.

        >>> s = pd.Series(
        ...     ["dog", "", 5, {"foo": "bar"}, [2, 3, 5, 7], ("one", "two", "three")]
        ... )
        >>> s
        0                  dog
        1
        2                    5
        3       {'foo': 'bar'}
        4         [2, 3, 5, 7]
        5    (one, two, three)
        dtype: object
        >>> s.str.len()
        0    3.0
        1    0.0
        2    NaN
        3    1.0
        4    4.0
        5    3.0
        dtype: float64
        """
        result = self._data.array._str_len()
        return self._wrap_result(result, returns_string=False)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._iset_not_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def _iset_not_inplace(self, key, value) -> None:
        # GH#39510 when setting with df[key] = obj with a list-like key and
        #  list-like value, we iterate over those listlikes and set columns
        #  one at a time.  This is different from dispatching to
        #  `self.loc[:, key]= value`  because loc.__setitem__ may overwrite
        #  data inplace, whereas this will insert new arrays.

        def igetitem(obj, i: int):
            # Note: we catch DataFrame obj before getting here, but
            #  hypothetically would return obj.iloc[:, i]
            if isinstance(obj, np.ndarray):
                return obj[..., i]
            else:
                return obj[i]

        if self.columns.is_unique:
            if np.shape(value)[-1] != len(key):
                raise ValueError("Columns must be same length as key")

            for i, col in enumerate(key):
                self[col] = igetitem(value, i)

        else:
            ilocs = self.columns.get_indexer_non_unique(key)[0]
            if (ilocs < 0).any():
                # key entries not in self.columns
                raise NotImplementedError

            if np.shape(value)[-1] != len(ilocs):
                raise ValueError("Columns must be same length as key")

            assert np.ndim(value) <= 2

            orig_columns = self.columns

            # Using self.iloc[:, i] = ... may set values inplace, which
            #  by convention we do not do in __setitem__
            try:
                self.columns = Index(range(len(self.columns)))
                for i, iloc in enumerate(ilocs):
                    self[iloc] = igetitem(value, i)
            finally:
                self.columns = orig_columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None:
        # When an ndarray, we should have locs.tolist() == [0]
        # When a BlockPlacement we should have list(locs) == [0]
        if copy:
            self.values = self.values.copy()
        self.values[:] = values

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.replace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def replace(self, to_replace, value, inplace: bool) -> Self:
        inplace = validate_bool_kwarg(inplace, "inplace")
        # NDFrame.replace ensures the not-is_list_likes here
        assert not lib.is_list_like(to_replace)
        assert not lib.is_list_like(value)
        return self.apply(
            "replace",
            to_replace=to_replace,
            value=value,
            inplace=inplace,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Fillna.time_fillna [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_fillna(self, inplace, dtype):
        self.df.fillna(value=self.fill_values, inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _set_with_engine(self, key, value) -> None:
        loc = self.index.get_loc(key)

        # this is equivalent to self._values[key] = value
        self._mgr.setitem_inplace(loc, value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py]
    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.
        StringMethods.len : Compute the length of each element in the Series/Index.

        Examples
        --------
        >>> import pyarrow as pa
        >>> s = pd.Series(
        ...     [
        ...         [1, 2, 3],
        ...         [3],
        ...     ],
        ...     dtype=pd.ArrowDtype(pa.list_(pa.int64())),
        ... )
        >>> s.list.len()
        0    3
        1    1
        dtype: int32[pyarrow]
        """
        from pandas import Series

        value_lengths = pc.list_value_length(self._pa_array)
        return Series(
            value_lengths,
            dtype=ArrowDtype(value_lengths.type),
            index=self._data.index,
            name=self._data.name,
        )

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
```
