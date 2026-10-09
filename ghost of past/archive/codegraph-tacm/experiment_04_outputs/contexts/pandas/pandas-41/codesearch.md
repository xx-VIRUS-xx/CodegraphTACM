# pandas-41 :: codesearch

query: BUG: ExtensionBlock.set not setting values inplace (#32831)

## selected nodes

- rank=1 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=2 layer=FUNCTION tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.set_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=3 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=4 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray._validate_setitem_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py
- rank=5 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendIndentUnchecked file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c
- rank=6 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendIntUnchecked file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c
- rank=7 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=8 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::new_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=9 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::node_init file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h
- rank=10 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendLongUnchecked file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c
- rank=11 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._set_item_mgr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=12 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=13 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterEnd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=14 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetValue file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=15 layer=FUNCTION tokens=455 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._setitem_single_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=16 layer=FUNCTION tokens=391 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.column_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=17 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newInteger file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=18 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendIndentNewlineUnchecked file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c
- rank=19 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=20 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endObject file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=21 layer=FUNCTION tokens=223 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::_reindex_for_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=22 layer=FUNCTION tokens=395 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=23 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::ArithmeticBlock.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None:
        # When an ndarray, we should have locs.tolist() == [0]
        # When a BlockPlacement we should have list(locs) == [0]
        if copy:
            self.values = self.values.copy()
        self.values[:] = values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray._validate_setitem_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py]
    def _validate_setitem_value(self, value):
        if isinstance(value, type(self)):
            value = value._ndarray

        # Match Block._standardize_fill_value behavior
        if self._ndarray.dtype.kind != "O" and is_valid_na_for_dtype(
            value, self._ndarray.dtype
        ):
            value = self.dtype.na_value

        try:
            return np_can_hold_element(self._ndarray.dtype, value)
        except LossySetitemError as err:
            raise TypeError(
                f"Invalid value '{value!s}' for dtype '{self.dtype}'"
            ) from err
        except NotImplementedError:
            # np_can_hold_element doesn't handle all dtypes (e.g. "U"),
            # fall back to no validation for those.
            return value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendIndentUnchecked [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c]
void Buffer_AppendIndentUnchecked(JSONObjectEncoder *enc, JSINT32 value) {
  int i;
  if (enc->indent > 0) {
    while (value-- > 0)
      for (i = 0; i < enc->indent; i++)
        Buffer_AppendCharUnchecked(enc, ' ');
  }
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendIntUnchecked [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c]
void Buffer_AppendIntUnchecked(JSONObjectEncoder *enc, JSINT32 value) {
  char *wstr;
  JSUINT32 uvalue = (value < 0) ? -value : value;
  wstr = enc->offset;

  // Conversion. Number is reversed.
  do {
    *wstr++ = (char)(48 + (uvalue % 10));
  } while (uvalue /= 10);
  if (value < 0)
    *wstr++ = '-';

  // Reverse string
  strreverse(enc->offset, wstr - 1);
  enc->offset += (wstr - (enc->offset));
}

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::node_init [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h]
static inline node_t *node_init(double value, int levels) {
  node_t *result;
  result = (node_t *)malloc(sizeof(node_t));
  if (result) {
    result->value = value;
    result->levels = levels;
    result->is_nil = 0;
    result->ref_count = 0;
    result->next = (node_t **)malloc(levels * sizeof(node_t *));
    result->width = (int *)malloc(levels * sizeof(int));
    if (!(result->next && result->width) && (levels != 0)) {
      free(result->next);
      free(result->width);
      free(result);
      return NULL;
    }
  }
  return result;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendLongUnchecked [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c]
void Buffer_AppendLongUnchecked(JSONObjectEncoder *enc, JSINT64 value) {
  char *wstr;
  JSUINT64 uvalue;
  if (value == INT64_MIN) {
    uvalue = INT64_MAX + UINT64_C(1);
  } else {
    uvalue = (value < 0) ? -value : value;
  }

  wstr = enc->offset;
  // Conversion. Number is reversed.

  do {
    *wstr++ = (char)(48 + (uvalue % 10ULL));
  } while (uvalue /= 10ULL);
  if (value < 0)
    *wstr++ = '-';

  // Reverse string
  strreverse(enc->offset, wstr - 1);
  enc->offset += (wstr - (enc->offset));
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._set_item_mgr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def _set_item_mgr(
        self, key, value: ArrayLike, refs: BlockValuesRefs | None = None
    ) -> None:
        try:
            loc = self._info_axis.get_loc(key)
        except KeyError:
            # This item wasn't present, just insert at end
            self._mgr.insert(len(self._info_axis), key, value, refs)
        else:
            self._iset_item_mgr(loc, value, refs=refs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Set_iterGetName(JSOBJ Py_UNUSED(obj),
                                   JSONTypeContext *Py_UNUSED(tc),
                                   size_t *Py_UNUSED(outLen)) {
  return NULL;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterEnd [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void Set_iterEnd(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  if (GET_TC(tc)->itemValue) {
    Py_DECREF(GET_TC(tc)->itemValue);
    GET_TC(tc)->itemValue = NULL;
  }

  if (GET_TC(tc)->iterator) {
    Py_DECREF(GET_TC(tc)->iterator);
    GET_TC(tc)->iterator = NULL;
  }
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetValue [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static JSOBJ Set_iterGetValue(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  return GET_TC(tc)->itemValue;
}

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newInteger [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newInteger(void *Py_UNUSED(prv), JSINT32 value) {
  return PyLong_FromLong(value);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendIndentNewlineUnchecked [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c]
void Buffer_AppendIndentNewlineUnchecked(JSONObjectEncoder *enc) {
  if (enc->indent > 0)
    Buffer_AppendCharUnchecked(enc, '\n');
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newNull(void *Py_UNUSED(prv)) { Py_RETURN_NONE; }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endObject [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_endObject(void *Py_UNUSED(prv), JSOBJ obj) { return obj; }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::_reindex_for_setitem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
def _reindex_for_setitem(
    value: DataFrame | Series, index: Index
) -> tuple[ArrayLike, BlockValuesRefs | None]:
    # reindex if necessary

    if value.index.equals(index) or not len(index):
        if isinstance(value, Series):
            return value._values, value._references
        return value._values.copy(), None

    # GH#4107
    try:
        reindexed_value = value.reindex(index)._values
    except ValueError as err:
        # raised in MultiIndex.from_tuples, see test_insert_error_msmgs
        if not value.index.is_unique:
            # duplicate axis
            raise err

        raise TypeError(
            "incompatible index of inserted column with frame index"
        ) from err
    return reindexed_value, None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unstack [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def _unstack(
        self,
        unstacker,
        fill_value,
        new_placement: npt.NDArray[np.intp],
        needs_masking: npt.NDArray[np.bool_],
    ):
        # ExtensionArray-safe unstack.
        # We override Block._unstack, which unstacks directly on the
        # values of the array. For EA-backed blocks, this would require
        # converting to a 2-D ndarray of objects.
        # Instead, we unstack an ndarray of integer positions, followed by
        # a `take` on the actual values.

        # Caller is responsible for ensuring self.shape[-1] == len(unstacker.index)
        new_values = unstacker.arange_result

        # needs_masking[i] calculated once in BlockManager.unstack tells
        #  us if there are any -1s in the relevant indices.  When False,
        #  that allows us to go through a faster path in 'take', among
        #  other things avoiding e.g. Categorical._validate_scalar.
        blocks = [
            # TODO: could cast to object depending on fill_value?
            type(self)(
                self.values.take(
                    indices, allow_fill=needs_masking[i], fill_value=fill_value
                ),
                BlockPlacement(place),
                ndim=2,
            )
            for i, (indices, place) in enumerate(
                zip(new_values.T, new_placement, strict=True)
            )
        ]
        return blocks

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::ArithmeticBlock.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py]
    def setup(self, fill_value):
        N = 10**6
        self.arr1 = self.make_block_array(
            length=N, num_blocks=1000, block_size=10, fill_value=fill_value
        )
        self.arr2 = self.make_block_array(
            length=N, num_blocks=1000, block_size=10, fill_value=fill_value
        )
```
