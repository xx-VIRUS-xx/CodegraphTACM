# pandas-53 :: tacm

query: BUG: using loc[int] with object index (#31905)

## selected nodes

- rank=1 layer=FILE tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=2 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/__init__.py
- rank=3 layer=FILE tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=4 layer=FILE tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/_color_data.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/_color_data.py
- rank=5 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Float64IndexMethod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=6 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=7 layer=CLASS tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLabelSlicing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=8 layer=CLASS tokens=373 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py::TestLocSetitemWithExpansion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_loc.py
- rank=9 layer=CLASS tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=10 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::UnionWithDuplicates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=11 layer=CLASS tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IndexAppend file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=12 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::IndexEquals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=13 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::SetOperations file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=14 layer=CLASS tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c::modulestate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=15 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=16 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=17 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=18 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=19 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=20 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Float64IndexMethod.time_get_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=21 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=22 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=23 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=24 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_sorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=25 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Range.time_get_loc_inc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=26 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Range.time_get_loc_dec file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=27 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=28 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c::object_is_index_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=29 layer=FUNCTION tokens=266 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=30 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique_sorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=31 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_single_level_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=32 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.isetitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=33 layer=FUNCTION tokens=211 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestSetitemCoercion._assert_setitem_index_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py
- rank=34 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=35 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py
- rank=36 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=37 layer=FUNCTION tokens=216 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::SetOperations.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=38 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.fast_xs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=39 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.get_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=40 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=41 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::IndexingMixin.loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=42 layer=FUNCTION tokens=229 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin.delete file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=43 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.delete file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=44 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex.get_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=45 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DataFrameNumericIndexing.time_loc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=46 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_loc_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=47 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_loc_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py

## context

```text
file vendored/ujson/python/ujson.c
imports: Python, numpy
defines: modulestate, PyModuleDef, object_is_decimal_type, object_is_dataframe_type, object_is_series_type, object_is_index_type, object_is_nat_type, object_is_na_type, object_is_decimal_type, object_is_dataframe_type, object_is_series_type, object_is_index_type, object_is_nat_type, object_is_na_type, module_traverse, module_clear, module_free, PyInit__ujson

file pandas/_config/__init__.py
imports: pandas
defines: using_string_dtype, using_python_scalars, is_nan_na

file asv_bench/benchmarks/index_object.py
imports: gc, numpy, pandas
defines: SetOperations, SetDisjoint, UnionWithDuplicates, Range, IndexEquals, IndexAppend, Indexing, Float64IndexMethod, IntervalIndexMethod, GC

file io/formats/_color_data.py
imports: __future__
defines: —

class Float64IndexMethod:  [asv_bench/benchmarks/index_object.py:202]
methods: setup, time_get_loc

class Indexing:  [asv_bench/benchmarks/index_object.py:154]
methods: setup, time_boolean_array, time_boolean_series, time_get
         time_get_loc, time_get_loc_non_unique
         time_get_loc_non_unique_sorted
         time_get_loc_sorted, time_slice, time_slice_step

class TestLabelSlicing:  [tests/indexing/test_loc.py:2606]
methods: test_loc_getitem_float_slice_floatindex
         test_loc_getitem_label_slice_across_dst
         test_loc_getitem_label_slice_period_timedelta
         test_loc_getitem_slice_columns_mixed_dtype
         test_loc_getitem_slice_floats_inexact
         test_loc_getitem_slice_label_td64obj
         test_loc_getitem_slice_labels_int_in_object_index
         test_loc_getitem_slice_unordered_dt_index
         test_loc_getitem_slicing_datetimes_frame

class TestLocSetitemWithExpansion:  [tests/indexing/test_loc.py:2011]
methods: test_loc_setitem_categorical_column_retains_dtype
         test_loc_setitem_datetime_keys_cast
         test_loc_setitem_datetimeindex_str_column_name
         test_loc_setitem_ea_not_full_column
         test_loc_setitem_empty_series
         test_loc_setitem_empty_series_float
         test_loc_setitem_empty_series_str_idx
         test_loc_setitem_expansion_both
         test_loc_setitem_incremental_with_dst
         test_loc_setitem_with_expansion_and_existing_dst
         test_loc_setitem_with_expansion_categorical
         test_loc_setitem_with_expansion_dtype_retention
         test_loc_setitem_with_expansion_dtype_retention_empty
         test_loc_setitem_with_expansion_empty_stays_object
         test_loc_setitem_with_expansion_fractional_not_truncated
         test_loc_setitem_with_expansion_inf_upcast_empty
         test_loc_setitem_with_expansion_large_dataframe
         test_loc_setitem_with_expansion_multi_column
         test_loc_setitem_with_expansion_multiindex_retains_dtypes
         test_loc_setitem_with_expansion_new_row_and_new_columns
         test_loc_setitem_with_expansion_nonunique_index
         test_loc_setitem_with_expansion_preserves_ea_dtype
         test_loc_setitem_with_expansion_preserves_nullable_int
         test_loc_setitem_with_expansion_retains_ea_dtype
         test_setitem_with_expansion
         test_setitem_with_expansion_pyarrow_scalar_retains_dtype

class Range:  [asv_bench/benchmarks/index_object.py:73]
methods: setup, time_get_loc_dec, time_get_loc_inc, time_iter_dec
         time_iter_inc, time_max, time_max_trivial
         time_min, time_min_trivial, time_sort_values_asc
         time_sort_values_des

class UnionWithDuplicates:  [asv_bench/benchmarks/index_object.py:64]
methods: setup, time_union_with_duplicates

class IndexAppend:  [asv_bench/benchmarks/index_object.py:123]
methods: setup, time_append_int_list, time_append_obj_list
         time_append_range_list, time_append_range_list_same

class IndexEquals:  [asv_bench/benchmarks/index_object.py:111]
methods: setup, time_non_object_equals_multiindex

class SetOperations:  [asv_bench/benchmarks/index_object.py:16]
methods: setup, time_operation

class modulestate  [vendored/ujson/python/ujson.c:70]
methods: —

    def _set_value(self, label, value, takeable: bool = False) -> None:
        """
        Quickly set single value at passed label.

        If label is not contained, a new object is created with the label
        placed at the end of the result index.

        Parameters
        ----------
        label : object
            Partial indexing with MultiIndex not allowed.
        value : object
            Scalar value.
        takeable : interpret the index as indexers, default False
        """
        if not takeable:
            try:
                loc = self.index.get_loc(label)
            except KeyError:
                # set using a non-recursive method
                self.loc[label] = value
                return
        else:
            loc = label

        self._set_values(loc, value)

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
    # ... truncated

    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

    # ... truncated

    def insert(self, loc: int, item: Hashable) -> Index:
        """
        Make new Index inserting new item at location.

        Follows Python numpy.insert semantics for negative values.

        Parameters
        ----------
        loc : int
            The integer location where the new item will be inserted.
        item : object
            The new item to be inserted into the Index.
    # ... truncated

    def _get_loc_level(self, key, level: int | list[int] = 0):
        """
        get_loc_level but with `level` known to be positional, not name-based.
        """
    # ... truncated

    def time_get_loc(self):
        self.ind.get_loc(0)

    def insert(self, loc: int, item) -> Self:
        """
        Insert an item at the given position.

        This method creates a new ExtensionArray with the specified item
        inserted at the given index. The original array is not modified.

        Parameters
        ----------
        loc : int
            Index where the `item` needs to be inserted.
        item : scalar-like
    # ... truncated

    def time_get_loc(self, dtype):
        self.idx.get_loc(self.key)

    def get_loc(self, key: Hashable) -> int | slice | npt.NDArray[np.bool_]:
        """
        Get integer location, slice or boolean mask for requested label.

        The return type depends on the characteristics of the index: an
        integer for a unique index, a slice for a monotonic index with
        duplicate entries, or a boolean mask for a non-monotonic index
        with duplicates.

        Parameters
        ----------
        key : label
    # ... truncated

    def time_get_loc_sorted(self, dtype):
        self.sorted.get_loc(self.key)

    def time_get_loc_inc(self):
        self.idx_inc.get_loc(900_000)

    def time_get_loc_dec(self):
        self.idx_dec.get_loc(100_000)

    def time_get_loc_non_unique(self, dtype):
        self.non_unique.get_loc(self.key)

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

    def insert(self, loc: int, item):
        """
        Make new Index inserting new item at location.
        Follows Python numpy.insert semantics for negative values.

        Parameters
        ----------
        loc : int
            The integer location where the new item will be inserted.
        item : object
            The new item to be inserted into the Index.

        Returns
        -------
        Index
            Returns a new Index object resulting from inserting the specified item at
            the specified location within the original Index.

        See Also
        --------
        Index.append : Append a collection of Indexes together.

        Examples
        --------
        >>> idx = pd.Index(["a", "b", "c"])
        >>> idx.insert(1, "x")
        Index(['a', 'x', 'b', 'c'], dtype='str')
        """
        result = super().insert(loc, item)
        if isinstance(result, type(self)):
            # i.e. parent class method did not cast
            result._data._freq = self._get_insert_freq(loc, item)
        return result

    def time_get_loc_non_unique_sorted(self, dtype):
        self.non_unique_sorted.get_loc(self.key)

    def _get_loc_single_level_index(self, level_index: Index, key: Hashable) -> int:
        """
        If key is NA value, location of index unify as -1.

        Parameters
        ----------
        level_index: Index
        key : label

        Returns
        -------
        loc : int
            If key is NA value, loc is -1
            Else, location of key in index.

        See Also
        --------
        Index.get_loc : The get_loc method for (single-level) index.
        """
        if is_scalar(key) and isna(key):
            # TODO: need is_valid_na_for_dtype(key, level_index.dtype)
            return -1
        else:
            return level_index.get_loc(key)  # type: ignore[return-value]

    def isetitem(self, loc, value) -> None:
        """
        Set the given value in the column with position `loc`.

        This is a positional analogue to ``__setitem__``.

        Parameters
        ----------
        loc : int or sequence of ints
            Index position for the column.
        value : scalar or arraylike
            Value(s) for the column.
    # ... truncated

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

    def _set_with_engine(self, key, value) -> None:
        loc = self.index.get_loc(key)

        # this is equivalent to self._values[key] = value
        self._mgr.setitem_inplace(loc, value)

    def insert(self, loc: int, item) -> Self:
        """
        Make new ExtensionArray inserting new item at location. Follows
        Python list.append semantics for negative values.

        Parameters
        ----------
        loc : int
        item : object

        Returns
        -------
        type(self)
        """
        loc = validate_insert_loc(loc, len(self))

        code = self._validate_scalar(item)

        new_vals = np.concatenate(
            (
                self._ndarray[:loc],
                np.asarray([code], dtype=self._ndarray.dtype),
                self._ndarray[loc:],
            )
        )
        return self._from_backing_data(new_vals)

    def insert(self, loc: int, item: Hashable, value: ArrayLike, refs=None) -> None:
        """
        Insert item at selected position.

        Parameters
        ----------
        loc : int
        item : hashable
        value : np.ndarray or ExtensionArray
        refs : The reference tracking object of the value to set.
        """
    # ... truncated

    def setup(self, index_structure, dtype, method):
        N = 10**5
        dates_left = date_range("1/1/2000", periods=N, freq="min")
        fmt = "%Y-%m-%d %H:%M:%S"
        date_str_left = Index(dates_left.strftime(fmt))
        int_left = Index(np.arange(N))
        ea_int_left = Index(np.arange(N), dtype="Int64")
        str_left = Index([f"i-{i}" for i in range(N)], dtype=object)

        data = {
            "datetime": dates_left,
            "date_string": date_str_left,
            "int": int_left,
            "strings": str_left,
            "ea_int": ea_int_left,
        }

        if index_structure == "non_monotonic":
            data = {k: mi[::-1] for k, mi in data.items()}

        data = {k: {"left": idx, "right": idx[:-1]} for k, idx in data.items()}

        self.left = data[dtype]["left"]
        self.right = data[dtype]["right"]

    def fast_xs(self, loc: int) -> SingleBlockManager:
        """
        Return the array corresponding to `frame.iloc[loc]`.

        Parameters
        ----------
        loc : int

        Returns
        -------
        np.ndarray or ExtensionArray
        """
    # ... truncated

    def get_loc(self, key):
        """
        Get integer location for requested label

        Returns
        -------
        loc : int, slice, or ndarray[int]
        """
        self._check_indexing_error(key)

        try:
            key = self._data._validate_scalar(key, unbox=False)
        except TypeError as err:
            raise KeyError(key) from err

        return Index.get_loc(self, key)

    def insert(
        self,
        loc: int,
        column: Hashable,
        value: object,
        allow_duplicates: bool | lib.NoDefault = lib.no_default,
    ) -> None:
        """
    # ... truncated

    def loc(self) -> _LocIndexer:
        """
        Access a group of rows and columns by label(s) or a boolean array.

        ``.loc[]`` is primarily label based, but may also be used with a
        boolean array.

        Allowed inputs are:

        - A single label, e.g. ``5`` or ``'a'``, (note that ``5`` is
          interpreted as a *label* of the index, and **never** as an
          integer position along the index).
    # ... truncated

    def delete(self, loc) -> Self:
        """
        Make new Index with passed location(-s) deleted.

        Parameters
        ----------
        loc : int or list of int
            Location of item(-s) which will be deleted.
            Use a list of locations to delete more than one value at the same time.

        Returns
        -------
        Index
            Will be same type as self, except for RangeIndex.

        See Also
        --------
        numpy.delete : Delete any rows and column from NumPy array (ndarray).

        Examples
        --------
        >>> idx = pd.Index(["a", "b", "c"])
        >>> idx.delete(1)
        Index(['a', 'c'], dtype='str')
        >>> idx = pd.Index(["a", "b", "c"])
        >>> idx.delete([0, 2])
        Index(['b'], dtype='str')
        """
        result = super().delete(loc)
        result._data._freq = self._get_delete_freq(loc)
        return result

    def delete(
        self, loc: int | np.integer | list[int] | npt.NDArray[np.integer]
    ) -> Self:
        """
    # ... truncated

    def get_loc(self, key):
        """
        Get integer location for requested label

        Returns
        -------
        loc : int
        """
    # ... truncated

    def time_loc(self, index, index_structure):
        self.df.loc[:100, 0]

    def time_loc_scalar(self, index, index_structure):
        self.data.loc[800000]

    def time_loc_slice(self, index, index_structure):
        self.data.loc[:800000]
```
