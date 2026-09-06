# pandas-44 :: minilm

query: BUG: DTI/TDI/PI get_indexer_non_unique with incompatible dtype (#32650)

## selected nodes

- rank=1 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=2 layer=FUNCTION tokens=348 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_FrequencyInferer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py
- rank=3 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._disallow_mismatched_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=4 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py::any_dtype_for_small_pos_integer_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py
- rank=5 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py::numeric_indexing_engine_type_and_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py
- rank=6 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py::ExtensionDtype.index_class file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py
- rank=7 layer=FUNCTION tokens=623 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::_convert_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=8 layer=FUNCTION tokens=412 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=9 layer=FUNCTION tokens=354 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=10 layer=FUNCTION tokens=678 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.astype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=11 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsIn.time_isin_mismatched_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py
- rank=12 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex._disallow_mismatched_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py
- rank=13 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::complex_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=14 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tslibs/test_fields.py::dtindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tslibs/test_fields.py
- rank=15 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::numeric_idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py
- rank=16 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericDtype._get_dtype_mapping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py
- rank=17 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=18 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::SeriesType.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=19 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/core.py::holds_integer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/core.py
- rank=20 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py::holds_integer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py
- rank=21 layer=FUNCTION tokens=157 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::any_numeric_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_mismatched_tz(self):
        # reached via e.g.
        #  ser = Series(range(len(dti)), index=dti)
        #  ser[dti2]
        self.dti.get_indexer(self.dti2)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_FrequencyInferer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py]
    def __init__(self, index) -> None:
        self.index = index
        self.i8values = index.asi8

        # For get_unit_from_dtype we need the dtype to the underlying ndarray,
        #  which for tz-aware is not the same as index.dtype
        if isinstance(index, ABCIndex):
            # error: Item "ndarray[Any, Any]" of "Union[ExtensionArray,
            # ndarray[Any, Any]]" has no attribute "_ndarray"
            self._creso = get_unit_from_dtype(
                index._data._ndarray.dtype  # type: ignore[union-attr]
            )
        else:
            # otherwise we have DTA/TDA
            self._creso = get_unit_from_dtype(index._ndarray.dtype)

        # This moves the values, which are implicitly in UTC, to the
        # the timezone so they are in local time
        if hasattr(index, "tz"):
            if index.tz is not None:
                self.i8values = tz_convert_from_utc(
                    self.i8values, index.tz, reso=self._creso
                )

        if len(index) < 3:
            raise ValueError("Need at least 3 dates to infer frequency")

        self.is_monotonic = (
            self.index._is_monotonic_increasing or self.index._is_monotonic_decreasing
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._disallow_mismatched_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
    def _disallow_mismatched_indexing(self, key: Period) -> None:
        if key._dtype != self.dtype:
            raise KeyError(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py::any_dtype_for_small_pos_integer_indexes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py]
def any_dtype_for_small_pos_integer_indexes(request):
    """
    Dtypes that can be given to an Index with small positive integers.

    This means that for any dtype `x` in the params list, `Index([1, 2, 3], dtype=x)` is
    valid and gives the correct Index (sub-)class.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py::numeric_indexing_engine_type_and_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py]
def numeric_indexing_engine_type_and_dtype(request):
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py::ExtensionDtype.index_class [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/base.py]
    def index_class(self) -> type_t[Index]:
        """
        The Index subclass to return from Index.__new__ when this dtype is
        encountered.
        """
        from pandas import Index

        return Index

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::_convert_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
def _convert_index(name: str, index: Index, encoding: str, errors: str) -> IndexCol:
    assert isinstance(name, str)

    index_name = index.name
    # error: Argument 1 to "_get_data_and_dtype_name" has incompatible type "Index";
    # expected "Union[ExtensionArray, ndarray]"
    converted, dtype_name = _get_data_and_dtype_name(index)  # type: ignore[arg-type]
    kind = _dtype_to_kind(dtype_name)
    atom = DataIndexableCol._get_atom(converted)

    if (
        lib.is_np_dtype(index.dtype, "iu")
        or needs_i8_conversion(index.dtype)
        or is_bool_dtype(index.dtype)
    ):
        # Includes Index, RangeIndex, DatetimeIndex, TimedeltaIndex, PeriodIndex,
        #  in which case "kind" is "integer", "integer", "datetime64",
        #  "timedelta64", and "integer", respectively.
        return IndexCol(
            name,
            values=converted,
            kind=kind,
            typ=atom,
            freq=getattr(index, "freq", None),
            tz=getattr(index, "tz", None),
            index_name=index_name,
        )

    if isinstance(index, MultiIndex):
        raise TypeError("MultiIndex not supported here!")

    inferred_type = lib.infer_dtype(index, skipna=False)
    # we won't get inferred_type of "datetime64" or "timedelta64" as these
    #  would go through the DatetimeIndex/TimedeltaIndex paths above

    values = np.asarray(index)

    if inferred_type == "date":
        converted = np.asarray([v.toordinal() for v in values], dtype=np.int32)
        return IndexCol(
            name, converted, "date", _tables().Time32Col(), index_name=index_name
        )
    elif inferred_type == "string":
        converted = _convert_string_array(values, encoding, errors)
        itemsize = converted.dtype.itemsize
        return IndexCol(
            name,
            converted,
            "string",
            _tables().StringCol(itemsize),
            index_name=index_name,
        )

    elif inferred_type in ["integer", "floating"]:
        return IndexCol(
            name, values=converted, kind=kind, typ=atom, index_name=index_name
        )
    else:
        assert isinstance(converted, np.ndarray) and converted.dtype == object
        assert kind == "object", kind
        atom = _tables().ObjectAtom()
        return IndexCol(name, converted, kind, atom, index_name=index_name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _get_indexer_non_comparable(
        self, target: Index, method: str_t | None, unique: bool = True
    ) -> npt.NDArray[np.intp] | tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
        Called from get_indexer or get_indexer_non_unique when the target
        is of a non-comparable dtype.

        For get_indexer lookups with method=None, get_indexer is an _equality_
        check, so non-comparable dtypes mean we will always have no matches.

        For get_indexer lookups with a method, get_indexer is an _inequality_
        check, so non-comparable dtypes mean we will always raise TypeError.

        Parameters
        ----------
        target : Index
        method : str or None
        unique : bool, default True
            * True if called from get_indexer.
            * False if called from get_indexer_non_unique.

        Raises
        ------
        TypeError
            If doing an inequality check, i.e. method is not None.
        """
        if method is not None:
            other_dtype = _unpack_nested_dtype(target)
            raise TypeError(f"Cannot compare dtypes {self.dtype} and {other_dtype}")

        no_matches = -1 * np.ones(target.shape, dtype=np.intp)
        if unique:
            # This is for get_indexer
            return no_matches
        else:
            # This is for get_indexer_non_unique
            missing = np.arange(len(target), dtype=np.intp)
            return no_matches, missing

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _intersection(
        self, other: Index, sort: bool = False
    ) -> Index | ArrayLike | MultiIndex:
        """
        intersection specialized to the case with matching dtypes.
        """
        if self._can_use_libjoin and other._can_use_libjoin:
            try:
                res_indexer, indexer, _ = self._inner_indexer(other)  # pyright: ignore[reportArgumentType]
            except TypeError:
                # non-comparable; should only be for object dtype
                pass
            else:
                # TODO: algos.unique1d should preserve DTA/TDA
                if is_numeric_dtype(self.dtype):
                    # This is faster, because Index.unique() checks for uniqueness
                    # before calculating the unique values.
                    res = algos.unique1d(res_indexer)
                else:
                    result = self.take(indexer)
                    res = result.drop_duplicates()  # type: ignore[assignment]
                return ensure_wrapped_if_datetimelike(res)  # type: ignore[no-untyped-call]

        res_values = self._intersection_via_get_indexer(other, sort=sort)
        res_values = _maybe_try_sort(res_values, sort)  # type: ignore[assignment]
        return res_values

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsIn.time_isin_mismatched_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py]
    def time_isin_mismatched_dtype(self, dtype):
        self.series.isin(self.mismatched)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py::DatetimeIndex._disallow_mismatched_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimes.py]
    def _disallow_mismatched_indexing(self, key) -> None:
        """
        Check for mismatched-tzawareness indexing and re-raise as KeyError.
        """
        # we get here with isinstance(key, self._data._recognized_scalars)
        try:
            # GH#36148
            self._data._assert_tzawareness_compat(key)
        except TypeError as err:
            raise KeyError(key) from err

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::complex_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def complex_dtype(request):
    """
    Parameterized fixture for complex dtypes.

    * complex
    * 'complex64'
    * 'complex128'
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tslibs/test_fields.py::dtindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tslibs/test_fields.py]
def dtindex():
    dtindex = np.arange(5, dtype=np.int64) * 10**9 * 3600 * 24 * 32
    dtindex.flags.writeable = False
    return dtindex

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::numeric_idx [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py]
def numeric_idx(request):
    """
    Several types of numeric-dtypes Index objects
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericDtype._get_dtype_mapping [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py]
    def _get_dtype_mapping(cls) -> Mapping[np.dtype, NumericDtype]:
        raise AbstractMethodError(cls)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def dtype(self) -> DtypeObj:
        """
        Return the dtype object of the underlying data.

        The dtype describes the type of elements stored in the Index, such as
        ``int64``, ``float64``, ``object``, or an extension dtype.

        See Also
        --------
        Index.inferred_type: Return a string of the type inferred from the values.

        Examples
        --------
        >>> idx = pd.Index([1, 2, 3])
        >>> idx
        Index([1, 2, 3], dtype='int64')
        >>> idx.dtype
        dtype('int64')
        """
        return self._data.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::SeriesType.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
    def __init__(self, dtype, index, namety) -> None:
        assert isinstance(index, IndexType)
        self.dtype = dtype
        self.index = index
        self.values = types.Array(self.dtype, 1, "C")
        self.namety = namety
        name = f"series({dtype}, {index}, {namety})"
        super().__init__(name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/core.py::holds_integer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/core.py]
def holds_integer(column: Index) -> bool:
    return column.dtype.kind in "iu"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py::holds_integer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py]
def holds_integer(column: Index) -> bool:
    return column.dtype.kind in "iu"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::any_numeric_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def any_numeric_dtype(request):
    """
    Parameterized fixture for all numeric dtypes.

    * int
    * 'int8'
    * 'uint8'
    * 'int16'
    * 'uint16'
    * 'int32'
    * 'uint32'
    * 'int64'
    * 'uint64'
    * float
    * 'float32'
    * 'float64'
    * complex
    * 'complex64'
    * 'complex128'
    * 'UInt8'
    * 'Int8'
    * 'UInt16'
    * 'Int16'
    * 'UInt32'
    * 'Int32'
    * 'UInt64'
    * 'Int64'
    * 'Float32'
    * 'Float64'
    """
    return request.param
```
