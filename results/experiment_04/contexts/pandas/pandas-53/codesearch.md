# pandas-53 :: codesearch

query: BUG: using loc[int] with object index (#31905)

## selected nodes

- rank=1 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterNext file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=2 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=3 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py
- rank=4 layer=FUNCTION tokens=361 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=5 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterBegin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=6 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::node_incref file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h
- rank=7 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::List_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=8 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::List_iterNext file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=9 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._get_val_at file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=10 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_get_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=11 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterGetValue file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=12 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py
- rank=13 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_get_loc_impl file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=14 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c::object_is_index_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=15 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=16 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterEnd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=17 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterNext file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=18 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=19 layer=FUNCTION tokens=247 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dict_iterNext file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=20 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::List_iterBegin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=21 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=22 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_iterNext file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=23 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Series_iterNext file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=24 layer=FUNCTION tokens=1104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.iloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterNext [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static int Index_iterNext(JSOBJ obj, JSONTypeContext *tc) {
  const Py_ssize_t index = GET_TC(tc)->index;
  Py_XDECREF(GET_TC(tc)->itemValue);
  if (!GET_TC(tc)->cStr) {
    return 0;
  }

  if (index == 0) {
    strcpy(GET_TC(tc)->cStr, "name");
    GET_TC(tc)->itemValue = PyObject_GetAttrString(obj, "name");
  } else if (index == 1) {
    strcpy(GET_TC(tc)->cStr, "data");
    GET_TC(tc)->itemValue = get_values(obj);
    if (!GET_TC(tc)->itemValue) {
      return 0;
    }
  } else {
    return 0;
  }

  GET_TC(tc)->index++;
  return 1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Index_iterGetName(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc,
                                     size_t *outLen) {
  *outLen = strlen(GET_TC(tc)->cStr);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::loc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def loc(x):
    return x.loc

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex.insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py]
    def insert(self, loc: int, item: Hashable) -> Index:
        if is_integer(item) or is_float(item):
            # We can retain RangeIndex is inserting at the beginning or end,
            #  or right in the middle.
            if len(self) == 0 and loc == 0 and is_integer(item):
                new_rng = range(item, item + self.step, self.step)
                return type(self)._simple_new(new_rng, name=self._name)
            elif len(self):
                rng = self._range
                if loc == 0 and item == self[0] - self.step:
                    new_rng = range(rng.start - rng.step, rng.stop, rng.step)
                    return type(self)._simple_new(new_rng, name=self._name)

                elif loc == len(self) and item == self[-1] + self.step:
                    new_rng = range(rng.start, rng.stop + rng.step, rng.step)
                    return type(self)._simple_new(new_rng, name=self._name)

                elif len(self) == 2 and item == self[0] + self.step / 2:
                    # e.g. inserting 1 into [0, 2]
                    step = int(self.step / 2)
                    new_rng = range(self.start, self.stop, step)
                    return type(self)._simple_new(new_rng, name=self._name)

        return super().insert(loc, item)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterBegin [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void Index_iterBegin(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  GET_TC(tc)->index = 0;
  GET_TC(tc)->cStr = PyObject_Malloc(CSTR_SIZE);
  if (!GET_TC(tc)->cStr) {
    PyErr_NoMemory();
  }
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::node_incref [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h]
static inline void node_incref(node_t *node) { ++(node->ref_count); }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::List_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *List_iterGetName(JSOBJ Py_UNUSED(obj),
                                    JSONTypeContext *Py_UNUSED(tc),
                                    size_t *Py_UNUSED(outLen)) {
  return NULL;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::List_iterNext [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static int List_iterNext(JSOBJ obj, JSONTypeContext *tc) {
  if (GET_TC(tc)->index >= GET_TC(tc)->size) {
    return 0;
  }

  GET_TC(tc)->itemValue = PyList_GET_ITEM(obj, GET_TC(tc)->index);
  GET_TC(tc)->index++;
  return 1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._get_val_at [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def _get_val_at(self, loc):
        n = len(self)
        if loc < 0:
            loc += n

        if loc >= n or loc < 0:
            raise IndexError(
                f"index is out of bounds: must be an integer between -{n} and {n - 1}"
            )

        sp_loc = self.sp_index.lookup(loc)
        if sp_loc == -1:
            return self.fill_value
        else:
            val = self.sp_values[sp_loc]
            val = maybe_box_datetimelike(val, self.sp_values.dtype)
            return val

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_get_loc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def index_get_loc(index, item):
    def index_get_loc_impl(index, item):
        # Initialize the hash table if not initialized
        if len(index.hashmap) == 0:
            for i, val in enumerate(index._data):
                index.hashmap[val] = i
        return index.hashmap[item]

    return index_get_loc_impl

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterGetValue [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static JSOBJ Index_iterGetValue(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  return GET_TC(tc)->itemValue;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py]
    def index(self, value: Any, start: int = ..., stop: int = ..., /) -> int: ...

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_get_loc_impl [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
    def index_get_loc_impl(index, item):
        # Initialize the hash table if not initialized
        if len(index.hashmap) == 0:
            for i, val in enumerate(index._data):
                index.hashmap[val] = i
        return index.hashmap[item]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c::object_is_index_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c]
int object_is_index_type(PyObject *obj) {
  PyObject *module = PyImport_ImportModule("pandas");
  if (module == NULL) {
    PyErr_Clear();
    return 0;
  }
  PyObject *type_index = PyObject_GetAttrString(module, "Index");
  if (type_index == NULL) {
    Py_DECREF(module);
    PyErr_Clear();
    return 0;
  }
  int result = PyObject_IsInstance(obj, type_index);
  if (result == -1) {
    Py_DECREF(module);
    Py_DECREF(type_index);
    PyErr_Clear();
    return 0;
  }
  return result;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Set_iterGetName(JSOBJ Py_UNUSED(obj),
                                   JSONTypeContext *Py_UNUSED(tc),
                                   size_t *Py_UNUSED(outLen)) {
  return NULL;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Index_iterEnd [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void Index_iterEnd(JSOBJ Py_UNUSED(obj),
                          JSONTypeContext *Py_UNUSED(tc)) {}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterNext [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static int Tuple_iterNext(JSOBJ obj, JSONTypeContext *tc) {

  if (GET_TC(tc)->index >= GET_TC(tc)->size) {
    return 0;
  }

  PyObject *item = PyTuple_GET_ITEM(obj, GET_TC(tc)->index);

  GET_TC(tc)->itemValue = item;
  GET_TC(tc)->index++;
  return 1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def index_indexing(index, idx):
    if isinstance(index, IndexType):

        def index_getitem(index, idx):
            return index._data[idx]

        return index_getitem

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dict_iterNext [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static int Dict_iterNext(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  if (GET_TC(tc)->itemName) {
    Py_DECREF(GET_TC(tc)->itemName);
    GET_TC(tc)->itemName = NULL;
  }

  if (!PyDict_Next((PyObject *)GET_TC(tc)->dictObj, &GET_TC(tc)->index,
                   &GET_TC(tc)->itemName, &GET_TC(tc)->itemValue)) {
    return 0;
  }

  if (PyUnicode_Check(GET_TC(tc)->itemName)) {
    GET_TC(tc)->itemName = PyUnicode_AsUTF8String(GET_TC(tc)->itemName);
  } else if (!PyBytes_Check(GET_TC(tc)->itemName)) {
    GET_TC(tc)->itemName = PyObject_Str(GET_TC(tc)->itemName);
    PyObject *itemNameTmp = GET_TC(tc)->itemName;
    GET_TC(tc)->itemName = PyUnicode_AsUTF8String(GET_TC(tc)->itemName);
    Py_DECREF(itemNameTmp);
  } else {
    Py_INCREF(GET_TC(tc)->itemName);
  }
  return 1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::List_iterBegin [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void List_iterBegin(JSOBJ obj, JSONTypeContext *tc) {
  GET_TC(tc)->index = 0;
  GET_TC(tc)->size = PyList_GET_SIZE((PyObject *)obj);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Object_iterGetName(JSOBJ obj, JSONTypeContext *tc,
                                      size_t *outLen) {
  return GET_TC(tc)->iterGetName(obj, tc, outLen);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_iterNext [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static int Object_iterNext(JSOBJ obj, JSONTypeContext *tc) {
  return GET_TC(tc)->iterNext(obj, tc);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Series_iterNext [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static int Series_iterNext(JSOBJ obj, JSONTypeContext *tc) {
  const Py_ssize_t index = GET_TC(tc)->index;
  Py_XDECREF(GET_TC(tc)->itemValue);
  if (!GET_TC(tc)->cStr) {
    return 0;
  }

  if (index == 0) {
    strcpy(GET_TC(tc)->cStr, "name");
    GET_TC(tc)->itemValue = PyObject_GetAttrString(obj, "name");
  } else if (index == 1) {
    strcpy(GET_TC(tc)->cStr, "index");
    GET_TC(tc)->itemValue = PyObject_GetAttrString(obj, "index");
  } else if (index == 2) {
    strcpy(GET_TC(tc)->cStr, "data");
    GET_TC(tc)->itemValue = get_values(obj);
    if (!GET_TC(tc)->itemValue) {
      return 0;
    }
  } else {
    return 0;
  }

  GET_TC(tc)->index++;
  return 1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.iloc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def iloc(self) -> _iLocIndexer:
        """
        Purely integer-location based indexing for selection by position.

        .. versionchanged:: 3.0

           Callables which return a tuple are deprecated as input.

        ``.iloc[]`` is primarily integer position based (from ``0`` to
        ``length-1`` of the axis), but may also be used with a boolean
        array.

        Allowed inputs are:

        - An integer, e.g. ``5``.
        - A list or array of integers, e.g. ``[4, 3, 0]``.
        - A slice object with ints, e.g. ``1:7``.
        - A boolean array.
        - A ``callable`` function with one argument (the calling Series or
          DataFrame) and that returns valid output for indexing (one of the above).
          This is useful in method chains, when you don't have a reference to the
          calling object, but would like to base your selection on
          some value.
        - A tuple of row and column indexes. The tuple elements consist of one of the
          above inputs, e.g. ``(0, 1)``.

        ``.iloc`` will raise ``IndexError`` if a requested indexer is
        out-of-bounds, except *slice* indexers which allow out-of-bounds
        indexing (this conforms with python/numpy *slice* semantics).

        See more at :ref:`Selection by Position <indexing.integer>`.

        See Also
        --------
        DataFrame.iat : Fast integer location scalar accessor.
        DataFrame.loc : Purely label-location based indexer for selection by label.
        Series.iloc : Purely integer-location based indexing for
                       selection by position.

        Examples
        --------
        >>> mydict = [
        ...     {"a": 1, "b": 2, "c": 3, "d": 4},
        ...     {"a": 100, "b": 200, "c": 300, "d": 400},
        ...     {"a": 1000, "b": 2000, "c": 3000, "d": 4000},
        ... ]
        >>> df = pd.DataFrame(mydict)
        >>> df
              a     b     c     d
        0     1     2     3     4
        1   100   200   300   400
        2  1000  2000  3000  4000

        **Indexing just the rows**

        With a scalar integer.

        >>> type(df.iloc[0])
        <class 'pandas.Series'>
        >>> df.iloc[0]
        a    1
        b    2
        c    3
        d    4
        Name: 0, dtype: int64

        With a list of integers.

        >>> df.iloc[[0]]
           a  b  c  d
        0  1  2  3  4
        >>> type(df.iloc[[0]])
        <class 'pandas.DataFrame'>

        >>> df.iloc[[0, 1]]
             a    b    c    d
        0    1    2    3    4
        1  100  200  300  400

        With a `slice` object.

        >>> df.iloc[:3]
              a     b     c     d
        0     1     2     3     4
        1   100   200   300   400
        2  1000  2000  3000  4000

        With a boolean mask the same length as the index.

        >>> df.iloc[[True, False, True]]
              a     b     c     d
        0     1     2     3     4
        2  1000  2000  3000  4000

        With a callable, useful in method chains. The `x` passed
        to the ``lambda`` is the DataFrame being sliced. This selects
        the rows whose index label even.

        >>> df.iloc[lambda x: x.index % 2 == 0]
              a     b     c     d
        0     1     2     3     4
        2  1000  2000  3000  4000

        **Indexing both axes**

        You can mix the indexer types for the index and columns. Use ``:`` to
        select the entire axis.

        With scalar integers.

        >>> df.iloc[0, 1]
        np.int64(2)

        With lists of integers.

        >>> df.iloc[[0, 2], [1, 3]]
              b     d
        0     2     4
        2  2000  4000

        With `slice` objects.

        >>> df.iloc[1:3, 0:3]
              a     b     c
        1   100   200   300
        2  1000  2000  3000

        With a boolean array whose length matches the columns.

        >>> df.iloc[:, [True, False, True, False]]
              a     c
        0     1     3
        1   100   300
        2  1000  3000

        With a callable function that expects the Series or DataFrame.

        >>> df.iloc[:, lambda df: [0, 2]]
              a     c
        0     1     3
        1   100   300
        2  1000  3000
        """
        return _iLocIndexer("iloc", self)
```
