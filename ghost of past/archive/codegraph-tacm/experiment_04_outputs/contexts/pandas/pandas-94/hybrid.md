# pandas-94 :: hybrid

query: BUG: TDI/DTI _shallow_copy creating invalid arrays (#30764)

## selected nodes

- rank=1 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=2 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=3 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=4 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=5 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py::JSONArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py
- rank=6 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=7 layer=FUNCTION tokens=381 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=8 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=9 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=10 layer=FUNCTION tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=11 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=12 layer=FUNCTION tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=13 layer=FUNCTION tokens=1031 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=14 layer=FUNCTION tokens=318 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.__from_arrow__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=15 layer=FUNCTION tokens=398 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::ensure_arraylike_for_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py]
    def dta(self, dta_dti):
        dta, dti = dta_dti
        return dta

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py]
    def tdi(self, monotonic):
        tdi = timedelta_range("1 Day", periods=10)
        if monotonic == "decreasing":
            tdi = tdi[::-1]
        elif monotonic is None:
            taker = np.arange(10, dtype=np.intp)
            np.random.default_rng(2).shuffle(taker)
            tdi = tdi.take(taker)
        return tdi

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray._shallow_copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def _shallow_copy(self, left, right) -> Self:
        """
        Return a new IntervalArray with the replacement attributes

        Parameters
        ----------
        left : Index
            Values to be used for the left-side of the intervals.
        right : Index
            Values to be used for the right-side of the intervals.
        """
        dtype = IntervalDtype(left.dtype, closed=self.closed)
        left, right, dtype = self._ensure_simple_new_inputs(left, right, dtype=dtype)

        return self._simple_new(left, right, dtype=dtype)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_add_dti_offset(self, offset):
        with warnings.catch_warnings(record=True):
            self.rng + offset

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def copy(self, deep: bool = True) -> Self:
        """
        Make a copy of this object's indices and data.

        When ``deep=True`` (default), a new object will be created with a
        copy of the calling object's data and indices. Modifications to
        the data or indices of the copy will not be reflected in the
        original object (see notes below).

        When ``deep=False``, a new object will be created without copying
        the calling object's data or index (only references to the data
        and index are copied). With Copy-on-Write, changes to the original
        will *not* be reflected in the shallow copy (and vice versa). The
        shallow copy uses a lazy (deferred) copy mechanism that copies the
        data only when any changes to the original or shallow copy are made,
        ensuring memory efficiency while maintaining data integrity.

        .. note::
            In pandas versions prior to 3.0, the default behavior without
            Copy-on-Write was different: changes to the original *were* reflected
            in the shallow copy (and vice versa). See the :ref:`Copy-on-Write
            user guide <copy_on_write>` for more information.

        Parameters
        ----------
        deep : bool, default True
            Make a deep copy, including a copy of the data and the indices.
            With ``deep=False`` neither the indices nor the data are copied.

        Returns
        -------
        Series or DataFrame
            Object type matches caller.

        See Also
        --------
        copy.copy : Return a shallow copy of an object.
        copy.deepcopy : Return a deep copy of an object.

        Notes
        -----
        When ``deep=True``, data is copied but actual Python objects
        will not be copied recursively, only the reference to the object.
        This is in contrast to :py:func:`copy.deepcopy` in the Standard Library,
        which recursively copies object data (see examples below).

        While ``Index`` objects are copied when ``deep=True``, the underlying
        numpy array is not copied for performance reasons. Since ``Index`` is
        immutable, the underlying data can be safely shared and a copy
        is not needed.

        Since pandas is not thread safe, see the
        :ref:`gotchas <gotchas.thread-safety>` when copying in a threading
        environment.

        Copy-on-Write protects shallow copies against accidental modifications.
        This means that any changes to the copied data would make a new copy
        of the data upon write (and vice versa). Changes made to either the
        original or copied variable would not be reflected in the counterpart.
        See :ref:`Copy_on_Write <copy_on_write>` for more information.

        Examples
        --------
        >>> s = pd.Series([1, 2], index=["a", "b"])
        >>> s
        a    1
        b    2
        dtype: int64

        >>> s_copy = s.copy(deep=True)
        >>> s_copy
        a    1
        b    2
        dtype: int64

        Due to Copy-on-Write, shallow copies still protect data modifications.
        Note shallow does not get modified below.

        >>> s = pd.Series([1, 2], index=["a", "b"])
        >>> shallow = s.copy(deep=False)
        >>> s.iloc[1] = 200
        >>> shallow
        a    1
        b    2
        dtype: int64

        When the data has object dtype, even a deep copy does not copy the
        underlying Python objects. Updating a nested data object will be
        reflected in the deep copy.

        >>> s = pd.Series([[1, 2], [3, 4]])
        >>> deep = s.copy()
        >>> s[0][0] = 10
        >>> s
        0    [10, 2]
        1     [3, 4]
        dtype: object
        >>> deep
        0    [10, 2]
        1     [3, 4]
        dtype: object
        """
        data = self._mgr.copy(deep=deep)
        return self._constructor_from_mgr(data, axes=data.axes).__finalize__(
            self, method="copy"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.__from_arrow__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def __from_arrow__(self, array: pa.Array | pa.ChunkedArray) -> PeriodArray:
        """
        Construct PeriodArray from pyarrow Array/ChunkedArray.
        """
        import pyarrow

        from pandas.core.arrays import PeriodArray
        from pandas.core.arrays.arrow._arrow_utils import (
            pyarrow_array_to_numpy_and_mask,
        )

        if isinstance(array, pyarrow.Array):
            chunks = [array]
        else:
            chunks = array.chunks

        results = []
        for arr in chunks:
            data, mask = pyarrow_array_to_numpy_and_mask(arr, dtype=np.dtype(np.int64))
            parr = PeriodArray(data.copy(), dtype=self, copy=False)
            # error: Invalid index type "ndarray[Any, dtype[bool_]]" for "PeriodArray";
            # expected type "Union[int, Sequence[int], Sequence[bool], slice]"
            parr[~mask] = NaT  # type: ignore[index]
            results.append(parr)

        if not results:
            return PeriodArray(np.array([], dtype="int64"), dtype=self, copy=False)
        return PeriodArray._concat_same_type(results)

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
```
