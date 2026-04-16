# pandas-84 :: codesearch

query: BUG: Fix MutliIndexed unstack failures at tuple names (#30943)

## selected nodes

- rank=1 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=2 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=3 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::List_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=4 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::tupleobject_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=5 layer=FUNCTION tokens=896 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=6 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::tupleobject_hash file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=7 layer=FUNCTION tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/utils.py::unpack_1tuple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/utils.py
- rank=8 layer=FUNCTION tokens=394 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=9 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dir_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=10 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=11 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dict_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=12 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::kh_needed_n_buckets file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=13 layer=FUNCTION tokens=299 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_stack_multi_column_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=14 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=15 layer=FUNCTION tokens=684 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._getitem_nested_tuple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=16 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Series_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=17 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterEnd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=18 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=19 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py::index_flat2 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Tuple_iterGetName(JSOBJ Py_UNUSED(obj),
                                     JSONTypeContext *Py_UNUSED(tc),
                                     size_t *Py_UNUSED(outLen)) {
  return NULL;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Index_iterGetName(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc,
                                     size_t *outLen) {
  *outLen = strlen(GET_TC(tc)->cStr);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::List_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *List_iterGetName(JSOBJ Py_UNUSED(obj),
                                    JSONTypeContext *Py_UNUSED(tc),
                                    size_t *Py_UNUSED(outLen)) {
  return NULL;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::tupleobject_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h]
static inline int tupleobject_cmp(PyTupleObject *a, PyTupleObject *b) {
  Py_ssize_t i;

  if (Py_SIZE(a) != Py_SIZE(b)) {
    return 0;
  }

  for (i = 0; i < Py_SIZE(a); ++i) {
    if (!pyobject_cmp(PyTuple_GET_ITEM(a, i), PyTuple_GET_ITEM(b, i))) {
      return 0;
    }
  }
  return 1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_multiple [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
def _unstack_multiple(
    data: Series | DataFrame, clocs, fill_value=None, sort: bool = True
):
    if len(clocs) == 0:
        return data

    # NOTE: This doesn't deal with hierarchical columns yet

    index = data.index
    index = cast("MultiIndex", index)  # caller is responsible for checking

    # GH 19966 Make sure if MultiIndexed index has tuple name, they will be
    # recognised as a whole
    if clocs in index.names:
        clocs = [clocs]
    clocs = [index._get_level_number(i) for i in clocs]

    rlocs = [i for i in range(index.nlevels) if i not in clocs]

    clevels = [index.levels[i] for i in clocs]
    ccodes = [index.codes[i] for i in clocs]
    cnames = [index.names[i] for i in clocs]
    rlevels = [index.levels[i] for i in rlocs]
    rcodes = [index.codes[i] for i in rlocs]
    rnames = [index.names[i] for i in rlocs]

    shape = tuple(len(x) for x in clevels)
    group_index = get_group_index(ccodes, shape, sort=False, xnull=False)

    comp_ids, obs_ids = compress_group_index(group_index, sort=False)
    recons_codes = decons_obs_group_ids(comp_ids, obs_ids, shape, ccodes, xnull=False)

    if not rlocs:
        # Everything is in clocs, so the dummy df has a regular index
        dummy_index = Index(obs_ids, name="__placeholder__", copy=False)
    else:
        dummy_index = MultiIndex(
            levels=[*rlevels, obs_ids],
            codes=[*rcodes, comp_ids],
            names=[*rnames, "__placeholder__"],
            verify_integrity=False,
        )

    if isinstance(data, Series):
        dummy = data.copy(deep=False)
        dummy.index = dummy_index

        unstacked = dummy.unstack("__placeholder__", fill_value=fill_value, sort=sort)
        new_levels = clevels
        new_names = cnames
        new_codes = recons_codes
    else:
        if isinstance(data.columns, MultiIndex):
            result = data
            while clocs:
                val = clocs.pop(0)
                # error: Incompatible types in assignment (expression has type
                # "DataFrame | Series", variable has type "DataFrame")
                result = result.unstack(  # type: ignore[assignment]
                    val, fill_value=fill_value, sort=sort
                )
                clocs = [v if v < val else v - 1 for v in clocs]

            return result

        # GH#42579 deep=False to avoid consolidating
        dummy_df = data.copy(deep=False)
        dummy_df.index = dummy_index

        # error: Incompatible types in assignment (expression has type "DataFrame |
        # Series", variable has type "DataFrame")
        unstacked = dummy_df.unstack(  # type: ignore[assignment]
            "__placeholder__", fill_value=fill_value, sort=sort
        )
        if isinstance(unstacked, Series):
            unstcols = unstacked.index
        else:
            unstcols = unstacked.columns
        assert isinstance(unstcols, MultiIndex)  # for mypy
        new_levels = [unstcols.levels[0], *clevels]
        new_names = [data.columns.name, *cnames]

        new_codes = [unstcols.codes[0]]
        new_codes.extend(rec.take(unstcols.codes[-1]) for rec in recons_codes)

    new_columns = MultiIndex(
        levels=new_levels, codes=new_codes, names=new_names, verify_integrity=False
    )

    if isinstance(unstacked, Series):
        unstacked.index = new_columns
    else:
        unstacked.columns = new_columns

    return unstacked

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::tupleobject_hash [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h]
static inline Py_hash_t tupleobject_hash(PyTupleObject *key) {
  Py_ssize_t i, len = Py_SIZE(key);
  PyObject **item = key->ob_item;

  Py_uhash_t acc = _PandasHASH_XXPRIME_5;
  for (i = 0; i < len; i++) {
    Py_uhash_t lane = kh_python_hash_func(item[i]);
    if (lane == (Py_uhash_t)-1) {
      return -1;
    }
    acc += lane * _PandasHASH_XXPRIME_2;
    acc = _PandasHASH_XXROTATE(acc);
    acc *= _PandasHASH_XXPRIME_1;
  }

  /* Add input length, mangled to keep the historical value of hash(()). */
  acc += len ^ (_PandasHASH_XXPRIME_5 ^ 3527539UL);

  if (acc == (Py_uhash_t)-1) {
    return 1546275796;
  }
  return acc;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/utils.py::unpack_1tuple [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/utils.py]
def unpack_1tuple(tup):
    """
    If we have a length-1 tuple/list that contains a slice, unpack to just
    the slice.

    Notes
    -----
    The list case is deprecated.
    """
    if len(tup) == 1 and isinstance(tup[0], slice):
        # if we don't have a MultiIndex, we may still be able to handle
        #  a 1-tuple.  see test_1tuple_without_multiindex

        if isinstance(tup, list):
            # GH#31299
            raise ValueError(
                "Indexing with a single-item list containing a "
                "slice is not allowed. Pass a tuple instead.",
            )

        return tup[0]
    return tup

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::unstack [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
def unstack(
    obj: Series | DataFrame, level, fill_value=None, sort: bool = True
) -> Series | DataFrame:
    if isinstance(level, (tuple, list)):
        if len(level) != 1:
            # _unstack_multiple only handles MultiIndexes,
            # and isn't needed for a single level
            return _unstack_multiple(obj, level, fill_value=fill_value, sort=sort)
        else:
            level = level[0]

    if not is_integer(level) and not level == "__placeholder__":
        # check if level is valid in case of regular index
        obj.index._get_level_number(level)

    if isinstance(obj, DataFrame):
        if isinstance(obj.index, MultiIndex):
            return _unstack_frame(obj, level, fill_value=fill_value, sort=sort)
        else:
            return obj.T.stack()
    elif not isinstance(obj.index, MultiIndex):
        # GH 36113
        # Give nicer error messages when unstack a Series whose
        # Index is not a MultiIndex.
        raise ValueError(
            f"index must be a MultiIndex to unstack, {type(obj.index)} was passed"
        )
    else:
        if is_1d_only_ea_dtype(obj.dtype):
            return _unstack_extension_series(obj, level, fill_value, sort=sort)
        unstacker = _Unstacker(
            obj.index, level=level, constructor=obj._constructor_expanddim, sort=sort
        )
        return unstacker.get_result(obj, value_columns=None, fill_value=fill_value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dir_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Dir_iterGetName(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc,
                                   size_t *outLen) {
  *outLen = PyBytes_GET_SIZE(GET_TC(tc)->itemName);
  return PyBytes_AS_STRING(GET_TC(tc)->itemName);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Set_iterGetName(JSOBJ Py_UNUSED(obj),
                                   JSONTypeContext *Py_UNUSED(tc),
                                   size_t *Py_UNUSED(outLen)) {
  return NULL;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dict_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Dict_iterGetName(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc,
                                    size_t *outLen) {
  *outLen = PyBytes_GET_SIZE(GET_TC(tc)->itemName);
  return PyBytes_AS_STRING(GET_TC(tc)->itemName);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::kh_needed_n_buckets [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h]
static inline khuint_t kh_needed_n_buckets(khuint_t n_elements) {
  khuint_t candidate = n_elements;
  kroundup32(candidate);
  khuint_t upper_bound = (khuint_t)(candidate * __ac_HASH_UPPER + 0.5);
  return (upper_bound < n_elements) ? 2 * candidate : candidate;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_stack_multi_column_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
def _stack_multi_column_index(columns: MultiIndex) -> MultiIndex | Index:
    """Creates a MultiIndex from the first N-1 levels of this MultiIndex."""
    if len(columns.levels) <= 2:
        return columns.levels[0]._rename(name=columns.names[0])

    levs = (
        [lev[c] if c >= 0 else None for c in codes]
        for lev, codes in zip(columns.levels[:-1], columns.codes[:-1], strict=True)
    )

    # Remove duplicate tuples in the MultiIndex.
    tuples = zip(*levs, strict=True)
    unique_tuples = (key for key, _ in itertools.groupby(tuples))
    new_levs = zip(*unique_tuples, strict=True)

    # The dtype of each level must be explicitly set to avoid inferring the wrong type.
    # See GH-36991.
    return MultiIndex.from_arrays(
        [
            # Not all indices can accept None values.
            Index(new_lev, dtype=lev.dtype) if None not in new_lev else new_lev
            for new_lev, lev in zip(new_levs, columns.levels[:-1], strict=True)
        ],
        names=columns.names[:-1],
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Object_iterGetName(JSOBJ obj, JSONTypeContext *tc,
                                      size_t *outLen) {
  return GET_TC(tc)->iterGetName(obj, tc, outLen);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._getitem_nested_tuple [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _getitem_nested_tuple(self, tup: tuple):
        # we have a nested tuple so have at least 1 multi-index level
        # we should be able to match up the dimensionality here

        for key in tup:
            check_dict_or_set_indexers(key)

        # we have too many indexers for our dim, but have at least 1
        # multi-index dimension, try to see if we have something like
        # a tuple passed to a series with a multi-index
        if len(tup) > self.ndim:
            if self.name != "loc":
                # This should never be reached, but let's be explicit about it
                raise ValueError("Too many indices")  # pragma: no cover
            if all(
                is_hashable(x, allow_slice=False) or com.is_null_slice(x) for x in tup
            ):
                # GH#10521 Series should reduce MultiIndex dimensions instead of
                #  DataFrame, IndexingError is not raised when slice(None,None,None)
                #  with one row.
                with suppress(IndexingError):
                    return cast("_LocIndexer", self)._handle_lowerdim_multi_index_axis0(
                        tup
                    )
            elif isinstance(self.obj, ABCSeries) and any(
                isinstance(k, tuple) for k in tup
            ):
                # GH#35349 Raise if tuple in tuple for series
                # Do this after the all-hashable-or-null-slice check so that
                #  we are only getting non-hashable tuples, in particular ones
                #  that themselves contain a slice entry
                # See test_loc_series_getitem_too_many_dimensions
                raise IndexingError("Too many indexers")

            # this is a series with a multi-index specified a tuple of
            # selectors
            axis = self.axis or 0
            return self._getitem_axis(tup, axis=axis)

        # handle the multi-axis by taking sections and reducing
        # this is iterative
        obj = self.obj
        # GH#41369 Loop in reverse order ensures indexing along columns before rows
        # which selects only necessary blocks which avoids dtype conversion if possible
        axis = len(tup) - 1
        for key in reversed(tup):
            if com.is_null_slice(key):
                axis -= 1
                continue

            obj = getattr(obj, self.name)._getitem_axis(key, axis=axis)
            axis -= 1

            # if we have a scalar, we are done
            if is_scalar(obj) or not hasattr(obj, "ndim"):
                break

        return obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Series_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Series_iterGetName(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc,
                                      size_t *outLen) {
  *outLen = strlen(GET_TC(tc)->cStr);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterEnd [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void Tuple_iterEnd(JSOBJ Py_UNUSED(obj),
                          JSONTypeContext *Py_UNUSED(tc)) {}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *DataFrame_iterGetName(JSOBJ Py_UNUSED(obj),
                                         JSONTypeContext *tc, size_t *outLen) {
  *outLen = strlen(GET_TC(tc)->cStr);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py::index_flat2 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py]
def index_flat2(index_flat):
    return index_flat
```
