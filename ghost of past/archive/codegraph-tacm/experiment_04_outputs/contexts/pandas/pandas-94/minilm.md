# pandas-94 :: minilm

query: BUG: TDI/DTI _shallow_copy creating invalid arrays (#30764)

## selected nodes

- rank=1 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._ensure_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=2 layer=FUNCTION tokens=381 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=3 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=4 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=5 layer=FUNCTION tokens=419 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_ints_to_td64ns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py
- rank=6 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_common.py::DummyArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_common.py
- rank=7 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::is_extension_array_dtype_and_needs_i8_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py
- rank=8 layer=FUNCTION tokens=457 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::maybe_convert_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=9 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py::ExtensionDtype._can_fast_transpose file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py
- rank=10 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py::JSONArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/json/array.py
- rank=11 layer=FUNCTION tokens=317 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::_reconstruct_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py
- rank=12 layer=FUNCTION tokens=678 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=13 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._maybe_copy_array_input file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=14 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=15 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray._shallow_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=16 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray._coerce_to_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=17 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_FrequencyInferer.deltas_asi8 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py
- rank=18 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py::DummyArray.__array__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py]
    def dta(self, dta_dti):
        dta, dti = dta_dti
        return dta

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py::_ints_to_td64ns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/timedeltas.py]
def _ints_to_td64ns(data, unit: str = "ns") -> tuple[np.ndarray, bool]:
    """
    Convert an ndarray with integer-dtype to timedelta64[ns] dtype, treating
    the integers as multiples of the given timedelta unit.

    Parameters
    ----------
    data : numpy.ndarray with integer-dtype
    unit : str, default "ns"
        The timedelta unit to treat integers as multiples of.

    Returns
    -------
    numpy.ndarray : timedelta64[ns] array converted from data
    bool : whether a copy was made
    """
    copy_made = False
    unit = unit if unit is not None else "ns"

    if data.dtype != np.int64:
        # GH#60677 unsigned integers > int64 max overflow silently
        # when cast to int64 (which timedelta64 is backed by)
        if data.dtype == np.dtype("uint64") and (data > np.iinfo(np.int64).max).any():
            raise OutOfBoundsTimedelta(f"Cannot convert input with unit '{unit}'")
        # converting to int64 makes a copy, so we can avoid
        # re-copying later
        data = data.astype(np.int64)
        copy_made = True

    if unit != "ns":
        dtype_str = f"timedelta64[{unit}]"
        data = data.view(dtype_str)

        new_dtype = get_supported_dtype(data.dtype)
        if new_dtype != data.dtype:
            data = astype_overflowsafe(data, dtype=new_dtype)

            # the astype conversion makes a copy, so we can avoid re-copying later
            copy_made = True

    else:
        data = data.view("timedelta64[ns]")

    return data, copy_made

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_common.py::DummyArray.__array__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_common.py]
    def __array__(self, dtype=None, copy=None):
        return self.data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::is_extension_array_dtype_and_needs_i8_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py]
def is_extension_array_dtype_and_needs_i8_conversion(
    left_dtype: DtypeObj, right_dtype: DtypeObj
) -> bool:
    """
    Checks that we have the combination of an ExtensionArraydtype and
    a dtype that should be converted to int64

    Returns
    -------
    bool

    Related to issue #37609
    """
    return isinstance(left_dtype, ExtensionDtype) and needs_i8_conversion(right_dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::maybe_convert_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py]
def maybe_convert_dtype(data, copy: bool, tz: tzinfo | None = None):
    """
    Convert data based on dtype conventions, issuing
    errors where appropriate.

    Parameters
    ----------
    data : np.ndarray or pd.Index
    copy : bool
    tz : tzinfo or None, default None

    Returns
    -------
    data : np.ndarray or pd.Index
    copy : bool

    Raises
    ------
    TypeError : PeriodDType data is passed
    """
    if not hasattr(data, "dtype"):
        # e.g. collections.deque
        return data, copy

    if is_float_dtype(data.dtype):
        # pre-2.0 we treated these as wall-times, inconsistent with ints
        # GH#23675, GH#45573 deprecated to treat symmetrically with integer dtypes.
        # Note: data.astype(np.int64) fails ARM tests, see
        # https://github.com/pandas-dev/pandas/issues/49468.
        data = data.astype(DT64NS_DTYPE).view("i8")
        copy = False

    elif lib.is_np_dtype(data.dtype, "m") or is_bool_dtype(data.dtype):
        # GH#29794 enforcing deprecation introduced in GH#23539
        raise TypeError(f"dtype {data.dtype} cannot be converted to datetime64[ns]")
    elif isinstance(data.dtype, PeriodDtype):
        # Note: without explicitly raising here, PeriodIndex
        #  test_setops.test_join_does_not_recur fails
        raise TypeError(
            "Passing PeriodDtype data is invalid. Use `data.to_timestamp()` instead"
        )

    elif isinstance(data.dtype, ExtensionDtype) and not isinstance(
        data.dtype, DatetimeTZDtype
    ):
        # TODO: We have no tests for these
        data = np.array(data, dtype=np.object_)
        copy = False

    return data, copy

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py::ExtensionDtype._can_fast_transpose [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py]
    def _can_fast_transpose(self) -> bool:
        """
        Is transposing an array with this dtype zero-copy?

        Only relevant for cases where _supports_2d is True.
        """
        return False

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::_reconstruct_data [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py]
def _reconstruct_data(
    values: ArrayLikeT, dtype: DtypeObj, original: AnyArrayLike
) -> ArrayLikeT:
    """
    reverse of _ensure_data

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
    dtype : np.dtype or ExtensionDtype
    original : AnyArrayLike

    Returns
    -------
    ExtensionArray or np.ndarray
    """
    if isinstance(values, ABCExtensionArray) and values.dtype == dtype:
        # Catch DatetimeArray/TimedeltaArray
        return values

    if not isinstance(dtype, np.dtype):
        # i.e. ExtensionDtype; note we have ruled out above the possibility
        #  that values.dtype == dtype
        cls = dtype.construct_array_type()

        # error: Incompatible return value type
        # (got "ExtensionArray",
        # expected "ndarray[tuple[Any, ...], dtype[Any]]")
        return cls._from_sequence(values, dtype=dtype)  # type: ignore[return-value]

    # error: Incompatible return value type
    # (got "ndarray[tuple[Any, ...], dtype[Any]]",
    # expected "ExtensionArray")
    return values.astype(dtype, copy=False)  # type: ignore[return-value]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.astype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def astype(self, dtype: Dtype, copy: bool = True) -> Index:
        """
        Create an Index with values cast to dtypes.

        The class of a new Index is determined by dtype. When conversion is
        impossible, a TypeError exception is raised.

        Parameters
        ----------
        dtype : numpy dtype or pandas type
            Dtype for the result Index.
        copy : bool, default True
            By default, astype always returns a newly allocated object.
            If copy is set to False and internal requirements on dtype are
            satisfied, the original data is used to create a new Index
            or the original Index is returned.

        Returns
        -------
        Index
            Index with values cast to specified dtype.

        See Also
        --------
        Index.dtype: Return the dtype object of the underlying data.
        Index.dtypes: Return the dtype object of the underlying data.
        Index.convert_dtypes: Convert columns to the best possible dtypes.

        Examples
        --------
        >>> idx = pd.Index([1, 2, 3])
        >>> idx
        Index([1, 2, 3], dtype='int64')
        >>> idx.astype("float")
        Index([1.0, 2.0, 3.0], dtype='float64')
        """
        if dtype is not None:
            dtype = pandas_dtype(dtype)

        if self.dtype == dtype:
            # Ensure that self.astype(self.dtype) is self
            return self.copy() if copy else self

        values = self._data
        if isinstance(values, ExtensionArray):
            with rewrite_exception(type(values).__name__, type(self).__name__):
                new_values = values.astype(dtype, copy=copy)

        elif isinstance(dtype, ExtensionDtype):
            cls = dtype.construct_array_type()
            # Note: for RangeIndex and CategoricalDtype self vs self._values
            #  behaves differently here.
            new_values = cls._from_sequence(self, dtype=dtype, copy=copy)

        else:
            # GH#13149 specifically use astype_array instead of astype
            new_values = astype_array(values, dtype=dtype, copy=copy)

        # pass copy=False because any copying will be done in the astype above
        result = Index(new_values, name=self.name, dtype=new_values.dtype, copy=False)
        if (
            not copy
            and self._references is not None
            and astype_is_view(self.dtype, dtype)
        ):
            result._references = self._references
            result._references.add_index_reference(result)
        return result

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_add_dti_offset(self, offset):
        with warnings.catch_warnings(record=True):
            self.rng + offset

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray._coerce_to_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py]
    def _coerce_to_array(
        cls, values, *, dtype: DtypeObj, copy: bool = False
    ) -> tuple[np.ndarray, np.ndarray]:
        raise AbstractMethodError(cls)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_FrequencyInferer.deltas_asi8 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py]
    def deltas_asi8(self) -> npt.NDArray[np.int64]:
        # NB: we cannot use self.i8values here because we may have converted
        #  the tz in __init__
        return unique_deltas(self.index.asi8)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py::DummyArray.__array__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py]
    def __array__(self, dtype=None, copy=None):
        return np.asarray(self.data, dtype=dtype)
```
