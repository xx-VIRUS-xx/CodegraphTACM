# pandas-94 :: codesearch

query: BUG: TDI/DTI _shallow_copy creating invalid arrays (#30764)

## selected nodes

- rank=1 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._maybe_copy_array_input file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=2 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py::JSONArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py
- rank=3 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._ensure_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=4 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=5 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::tupleobject_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=6 layer=FUNCTION tokens=439 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py::_prep_ndarraylike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py
- rank=7 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::pyobject_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=8 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray._coerce_to_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=9 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::floatobject_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=10 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_astype.py::Int16DtypeNoCopy.construct_array_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_astype.py
- rank=11 layer=FUNCTION tokens=381 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=12 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=13 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::complexobject_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=14 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/boolean.py::BooleanArray._coerce_to_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/boolean.py
- rank=15 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_arrayAddItem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=16 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__deepcopy__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py
- rank=17 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=18 layer=FUNCTION tokens=398 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::ensure_arraylike_for_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=19 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::traced_realloc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=20 layer=FUNCTION tokens=280 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray._cmp_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py
- rank=21 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=22 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py::ArrowStringArray._box_pa_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._maybe_copy_array_input [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _maybe_copy_array_input(
        cls, data: object, copy: bool | None, dtype: Dtype | None
    ) -> tuple[Any, bool]:
        """
        Ensure that the input data is copied if necessary.
        GH#63388
        """
        if isinstance(data, (ExtensionArray, np.ndarray)):
            if copy is not False:
                if dtype is None or astype_is_view(data.dtype, pandas_dtype(dtype)):
                    data = data.copy()
                    copy = False
        return data, bool(copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py::JSONArray.__array__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py]
    def __array__(self, dtype=None, copy=None):
        if copy is False:
            raise ValueError(
                "Unable to avoid copy while creating an array as requested."
            )
        if dtype is None:
            dtype = object
        if dtype == object:
            # on py38 builds it looks like numpy is inferring to a non-1D array
            return construct_1d_object_array_from_listlike(list(self))
        if copy is None:
            # Note: branch avoids `copy=None` for NumPy 1.x support
            return np.asarray(self.data, dtype=dtype)
        return np.asarray(self.data, dtype=dtype, copy=copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._ensure_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _ensure_array(cls, data: ArrayLike, dtype: DtypeObj, copy: bool) -> ArrayLike:
        """
        Ensure we have a valid array to pass to _simple_new.
        """
        if data.ndim > 1:
            # GH#13601, GH#20285, GH#27125
            raise ValueError("Index data must be 1-dimensional")
        elif dtype == np.float16:
            # float16 not supported (no indexing engine)
            raise NotImplementedError("float16 indexes are not supported")

        if copy:
            # asarray_tuplesafe does not always copy underlying data,
            #  so need to make sure that this happens
            data = data.copy()
        return data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newArray [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newArray(void *Py_UNUSED(prv), void *Py_UNUSED(decoder)) {
  return PyList_New(0);
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py::_prep_ndarraylike [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py]
def _prep_ndarraylike(values, copy: bool = True) -> np.ndarray:
    # values is specifically _not_ ndarray, EA, Index, or Series
    # We only get here with `not treat_as_nested(values)`

    if len(values) == 0:
        # TODO: check for length-zero range, in which case return int64 dtype?
        # TODO: reuse anything in try_cast?
        return np.empty((0, 0), dtype=object)
    elif isinstance(values, range):
        arr = range_to_ndarray(values)
        return arr[..., np.newaxis]

    def convert(v):
        if not is_list_like(v) or isinstance(v, ABCDataFrame):
            return v

        v = extract_array(v, extract_numpy=True)
        if isinstance(v, (list, tuple, range)):
            v = construct_1d_object_array_from_listlike(v)
        if isinstance(v, np.ndarray) and v.dtype == object:
            v = lib.maybe_convert_objects(v)
        # We don't do maybe_infer_objects here bc we will end up doing
        #  it column-by-column in ndarray_to_mgr
        return v

    # we could have a 1-dim or 2-dim list here
    # this is equiv of np.asarray, but does object conversion
    # and platform dtype preservation
    # does not convert e.g. [1, "a", True] to ["1", "a", "True"] like
    #  np.asarray would
    if is_list_like(values[0]):
        values = np.array([convert(v) for v in values])
    elif isinstance(values[0], np.ndarray) and values[0].ndim == 0:
        # GH#21861 see test_constructor_list_of_lists
        values = np.array([convert(v) for v in values])
    else:
        values = convert(values)

    return _ensure_2d(values)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::pyobject_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h]
static inline int pyobject_cmp(PyObject *a, PyObject *b) {
  if (a == b) {
    return 1;
  }
  if (Py_TYPE(a) == Py_TYPE(b)) {
    // special handling for some built-in types which could have NaNs
    // as we would like to have them equivalent, but the usual
    // PyObject_RichCompareBool would return False
    if (PyFloat_CheckExact(a)) {
      return floatobject_cmp((PyFloatObject *)a, (PyFloatObject *)b);
    }
    if (PyComplex_CheckExact(a)) {
      return complexobject_cmp((PyComplexObject *)a, (PyComplexObject *)b);
    }
    if (PyTuple_Check(a)) {
      // compare tuple subclasses as builtin tuples
      return tupleobject_cmp((PyTupleObject *)a, (PyTupleObject *)b);
    }
    // frozenset isn't yet supported
  }

  int result = PyObject_RichCompareBool(a, b, Py_EQ);
  if (result < 0) {
    PyErr_Clear();
    return 0;
  }
  return result;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray._coerce_to_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py]
    def _coerce_to_array(
        cls, values, *, dtype: DtypeObj, copy: bool = False
    ) -> tuple[np.ndarray, np.ndarray]:
        raise AbstractMethodError(cls)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::floatobject_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h]
static inline int floatobject_cmp(PyFloatObject *a, PyFloatObject *b) {
  return (isnan(PyFloat_AS_DOUBLE(a)) && isnan(PyFloat_AS_DOUBLE(b))) ||
         (PyFloat_AS_DOUBLE(a) == PyFloat_AS_DOUBLE(b));
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_astype.py::Int16DtypeNoCopy.construct_array_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_astype.py]
    def construct_array_type(self):
        return IntegerArrayNoCopy

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._shallow_copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py]
    def _shallow_copy(  # type: ignore[override]
        self, values: ArrayLike, name: Hashable = no_default
    ) -> Index:
        """
        Create a new RangeIndex with the same class as the caller, don't copy the
        data, use the same object attributes with passed in attributes taking
        precedence.

        *this is an internal non-public method*

        Parameters
        ----------
        values : the values to create the new RangeIndex, optional
        name : Label, defaults to self.name
        """
        name = self._name if name is no_default else name

        if values.dtype.kind == "f":
            return Index(values, name=name, dtype=np.float64, copy=False)
        if values.dtype.kind == "i" and values.ndim == 1:
            # GH 46675 & 43885: If values is equally spaced, return a
            # more memory-compact RangeIndex instead of Index with 64-bit dtype
            if len(values) == 1:
                start = values[0]
                new_range = range(start, start + self.step, self.step)
                return type(self)._simple_new(new_range, name=name)
            maybe_range = ibase.maybe_sequence_to_range(values)
            if isinstance(maybe_range, range):
                return type(self)._simple_new(maybe_range, name=name)
        return self._constructor._simple_new(values, name=name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._shallow_copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def _shallow_copy(self, values: np.ndarray, name=lib.no_default) -> MultiIndex:  # type: ignore[override]
        """
        Create a new Index with the same class as the caller, don't copy the
        data, use the same object attributes with passed in attributes taking
        precedence.

        *this is an internal non-public method*

        Parameters
        ----------
        values : the values to create the new Index, optional
        name : Label, defaults to self.name
        """
        names = name if name is not lib.no_default else self.names

        return type(self).from_tuples(values, sortorder=None, names=names)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::complexobject_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h]
static inline int complexobject_cmp(PyComplexObject *a, PyComplexObject *b) {
  return (isnan(a->cval.real) && isnan(b->cval.real) && isnan(a->cval.imag) &&
          isnan(b->cval.imag)) ||
         (isnan(a->cval.real) && isnan(b->cval.real) &&
          a->cval.imag == b->cval.imag) ||
         (a->cval.real == b->cval.real && isnan(a->cval.imag) &&
          isnan(b->cval.imag)) ||
         (a->cval.real == b->cval.real && a->cval.imag == b->cval.imag);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/boolean.py::BooleanArray._coerce_to_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/boolean.py]
    def _coerce_to_array(
        cls, value, *, dtype: DtypeObj, copy: bool = False
    ) -> tuple[np.ndarray, np.ndarray]:
        if dtype:
            assert dtype == "boolean"
        return coerce_to_array(value, copy=copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_arrayAddItem [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static int Object_arrayAddItem(void *Py_UNUSED(prv), JSOBJ obj, JSOBJ value) {
  int ret = PyList_Append(obj, value);
  Py_DECREF((PyObject *)value);
  return ret == 0 ? 1 : 0;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__deepcopy__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py]
    def __deepcopy__(self, memo: dict[int, Any] | None) -> NoReturn:
        raise TypeError("Expression objects are not copiable")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newNull(void *Py_UNUSED(prv)) { Py_RETURN_NONE; }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::ensure_arraylike_for_datetimelike [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
def ensure_arraylike_for_datetimelike(
    data, copy: bool, cls_name: str
) -> tuple[ArrayLike, bool]:
    if not hasattr(data, "dtype"):
        # e.g. list, tuple
        if not isinstance(data, (list, tuple)) and np.ndim(data) == 0:
            # i.e. generator
            data = list(data)

        data = construct_1d_object_array_from_listlike(data)
        copy = False
    elif isinstance(data, ABCMultiIndex):
        raise TypeError(f"Cannot create a {cls_name} from a MultiIndex.")
    else:
        data = extract_array(data, extract_numpy=True)

    if isinstance(data, IntegerArray) or (
        isinstance(data, ArrowExtensionArray) and data.dtype.kind in "iu"
    ):
        data = data.to_numpy("int64", na_value=iNaT)
        copy = False
    elif isinstance(data, ArrowExtensionArray):
        data = data._maybe_convert_datelike_array()
        data = data.to_numpy()
        copy = False
    elif not isinstance(data, (np.ndarray, ExtensionArray)):
        # GH#24539 e.g. xarray, dask object
        data = np.asarray(data)

    elif isinstance(data, ABCCategorical):
        # GH#18664 preserve tz in going DTI->Categorical->DTI
        # TODO: cases where we need to do another pass through maybe_convert_dtype,
        #  e.g. the categories are timedelta64s
        data = data.categories.take(data.codes, fill_value=NaT)._values
        copy = False

    return data, copy

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::traced_realloc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h]
static void *traced_realloc(void *old_ptr, size_t size) {
  PyTraceMalloc_Untrack(KHASH_TRACE_DOMAIN, (uintptr_t)old_ptr);
  void *ptr = realloc(old_ptr, size);
  if (ptr != NULL) {
    PyTraceMalloc_Track(KHASH_TRACE_DOMAIN, (uintptr_t)ptr, size);
  }
  return ptr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray._cmp_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py]
    def _cmp_method(self, other, op):
        if isinstance(other, NumpyExtensionArray):
            other = other._ndarray

        other = ops.maybe_prepare_scalar_for_op(other, (len(self),))
        pd_op = ops.get_array_op(op)
        other = ensure_wrapped_if_datetimelike(other)
        result = pd_op(self._ndarray, other)

        if op is divmod or op is ops.rdivmod:
            a, b = result
            if isinstance(a, np.ndarray):
                # for e.g. op vs TimedeltaArray, we may already
                #  have an ExtensionArray, in which case we do not wrap
                return self._wrap_ndarray_result(a), self._wrap_ndarray_result(b)
            return a, b

        if isinstance(result, np.ndarray):
            # for e.g. multiplication vs TimedeltaArray, we may already
            #  have an ExtensionArray, in which case we do not wrap
            return self._wrap_ndarray_result(result)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__array__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py]
    def __array__(
        self, dtype: NpDtype | None = None, copy: bool | None = None
    ) -> np.ndarray:
        """Correctly construct numpy arrays when passed to `np.asarray()`."""
        if copy is False:
            # TODO: By using `zero_copy_only` it may be possible to implement this
            raise ValueError(
                "Unable to avoid copy while creating an array as requested."
            )
        elif copy is None:
            # `to_numpy(copy=False)` has the meaning of NumPy `copy=None`.
            copy = False

        return self.to_numpy(dtype=dtype, copy=copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py::ArrowStringArray._box_pa_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py]
    def _box_pa_array(
        cls, value, pa_type: pa.DataType | None = None, copy: bool = False
    ) -> pa.Array | pa.ChunkedArray:
        pa_array = super()._box_pa_array(value, pa_type)
        if pa.types.is_string(pa_array.type) and pa_type is None:
            pa_array = pc.cast(pa_array, pa.large_string())
        return pa_array
```
