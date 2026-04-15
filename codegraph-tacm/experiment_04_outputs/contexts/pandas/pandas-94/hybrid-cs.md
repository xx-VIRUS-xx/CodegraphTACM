# pandas-94 :: hybrid-cs

query: BUG: TDI/DTI _shallow_copy creating invalid arrays (#30764)

## selected nodes

- rank=1 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=2 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py::JSONArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py
- rank=3 layer=FUNCTION tokens=398 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::ensure_arraylike_for_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=4 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=5 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=6 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_copy.py::assert_multiindex_copied file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_copy.py
- rank=7 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=8 layer=FUNCTION tokens=329 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=9 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=10 layer=FUNCTION tokens=381 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=11 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._maybe_copy_array_input file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=12 layer=FUNCTION tokens=751 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=13 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._ensure_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=14 layer=FUNCTION tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=15 layer=FUNCTION tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py]
    def copy(self) -> Self:
        """
        Return a shallow copy of the array.

        Underlying ChunkedArray is immutable, so a deep copy is unnecessary.

        Returns
        -------
        type(self)
        """
        return self._from_pyarrow_array(self._pa_array)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_copy.py::assert_multiindex_copied [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_copy.py]
def assert_multiindex_copied(copy, original):
    # Levels should be (at least, shallow copied)
    tm.assert_copy(copy.levels, original.levels)
    tm.assert_almost_equal(copy.codes, original.codes)

    # Labels doesn't matter which way copied
    tm.assert_almost_equal(copy.codes, original.codes)
    assert copy.codes is not original.codes

    # Names doesn't matter which way copied
    assert copy.names == original.names
    assert copy.names is not original.names

    # Sort order should be copied
    assert copy.sortorder == original.sortorder

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.__array__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def __array__(self, dtype=None, copy=None) -> np.ndarray:
        """the array interface, return my values"""
        if copy is False:
            # self.values is always a newly construct array, so raise.
            raise ValueError(
                "Unable to avoid copy while creating an array as requested."
            )
        if copy is True:
            # explicit np.array call to ensure a copy is made and unique objects
            # are returned, because self.values is cached
            return np.array(self.values, dtype=dtype)
        return self.values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.__array__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def __array__(
        self, dtype: npt.DTypeLike | None = None, copy: bool | None = None
    ) -> np.ndarray:
        if copy is False and not self._mgr.is_single_block and not self.empty:
            # check this manually, otherwise ._values will already return a copy
            # and np.array(values, copy=False) will not raise an error
            raise ValueError(
                "Unable to avoid copy while creating an array as requested."
            )
        values = self._values
        if copy is None:
            # Note: branch avoids `copy=None` for NumPy 1.x support
            arr = np.asarray(values, dtype=dtype)
        else:
            arr = np.array(values, dtype=dtype, copy=copy)

        if (
            copy is not True
            and astype_is_view(values.dtype, arr.dtype)
            and self._mgr.is_single_block
        ):
            # Check if both conversions can be done without a copy
            if astype_is_view(self.dtypes.iloc[0], values.dtype) and astype_is_view(
                values.dtype, arr.dtype
            ):
                arr = arr.view()
                arr.flags.writeable = False
        return arr

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.__array__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def __array__(
        self, dtype: NpDtype | None = None, copy: bool | None = None
    ) -> np.ndarray:
        if dtype == "i8":
            # For NumPy 1.x compatibility we cannot use copy=None.  And
            # `copy=False` has the meaning of `copy=None` here:
            if not copy:
                result = np.asarray(self.asi8, dtype=dtype)
                if self._readonly:
                    result = result.view()
                    result.flags.writeable = False
                return result
            else:
                return np.array(self.asi8, dtype=dtype)

        if copy is False:
            raise ValueError(
                "Unable to avoid copy while creating an array as requested."
            )

        if dtype == bool:
            return ~self._isnan

        # This will raise TypeError for non-object dtypes
        return np.array(list(self), dtype=object)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def copy(  # type: ignore[override]
        self,
        names=None,
        deep: bool = False,
        name=None,
    ) -> Self:
        """
        Make a copy of this object. Names, dtype, levels and codes can be passed and \
        will be set on new copy.

        The `copy` method provides a mechanism to create a duplicate of an
        existing MultiIndex object. This is particularly useful in scenarios where
        modifications are required on an index, but the original MultiIndex should
        remain unchanged. By specifying the `deep` parameter, users can control
        whether the copy should be a deep or shallow copy, providing flexibility
        depending on the size and complexity of the MultiIndex.

        Parameters
        ----------
        names : sequence, optional
            Names to set on the new MultiIndex object.
        deep : bool, default False
            If False, the new object will be a shallow copy. If True, a deep copy
            will be attempted. Deep copying can be potentially expensive for large
            MultiIndex objects.
        name : Label
            Kept for compatibility with 1-dimensional Index. Should not be used.

        Returns
        -------
        MultiIndex
            A new MultiIndex object with the specified modifications.

        See Also
        --------
        MultiIndex.from_arrays : Convert arrays to MultiIndex.
        MultiIndex.from_tuples : Convert list of tuples to MultiIndex.
        MultiIndex.from_frame : Convert DataFrame to MultiIndex.

        Notes
        -----
        In most cases, there should be no functional difference from using
        ``deep``, but if ``deep`` is passed it will attempt to deepcopy.
        This could be potentially expensive on large MultiIndex objects.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([["a"], ["b"], ["c"]])
        >>> mi
        MultiIndex([('a', 'b', 'c')],
                   )
        >>> mi.copy()
        MultiIndex([('a', 'b', 'c')],
                   )
        """
        names = self._validate_names(name=name, names=names, deep=deep)
        keep_id = not deep
        levels, codes = None, None

        if deep:
            from copy import deepcopy

            levels = deepcopy(self.levels)
            codes = deepcopy(self.codes)

        levels = levels if levels is not None else self.levels
        codes = codes if codes is not None else self.codes

        new_index = type(self)(
            levels=levels,
            codes=codes,
            sortorder=self.sortorder,
            names=names,
            verify_integrity=False,
        )
        new_index._cache = self._cache.copy()
        new_index._reset_cache("levels")  # GH32669
        if keep_id:
            new_index._id = self._id
        return new_index

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin.__array__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def __array__(
        self, dtype: NpDtype | None = None, copy: bool | None = None
    ) -> np.ndarray:
        # used for Timedelta/DatetimeArray, overwritten by PeriodArray
        if is_object_dtype(dtype):
            if copy is False:
                raise ValueError(
                    "Unable to avoid copy while creating an array as requested."
                )
            return np.array(list(self), dtype=object)

        if copy is True:
            return np.array(self._ndarray, dtype=dtype)

        result = self._ndarray
        if self._readonly:
            result = result.view()
            result.flags.writeable = False
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._shallow_copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _shallow_copy(self, values: ArrayLike, name: Hashable = no_default) -> Self:
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
        name = self._name if name is no_default else name

        return self._simple_new(values, name=name, refs=self._references)
```
