# pandas-44 :: codesearch

query: BUG: DTI/TDI/PI get_indexer_non_unique with incompatible dtype (#32650)

## selected nodes

- rank=1 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer_dups file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=2 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_numeric.py::TestFloatNumericIndex.mixed_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_numeric.py
- rank=3 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::coerce_indexer_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=4 layer=FUNCTION tokens=412 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=5 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tslibs/test_fields.py::dtindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tslibs/test_fields.py
- rank=6 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=7 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=8 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py::dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py
- rank=9 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py
- rank=10 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::FindValidIndex.time_first_valid_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=11 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py::numeric_indexing_engine_type_and_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py
- rank=12 layer=FUNCTION tokens=214 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._dtype_to_subclass file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=13 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_numeric.py::TestNumericInt.simple_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_numeric.py
- rank=14 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=15 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py::get_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py
- rank=16 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=17 layer=FUNCTION tokens=423 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::SparseDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=18 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=19 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/dim2.py::Dim2CompatTests.get_reduction_result_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/dim2.py
- rank=20 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::typeof_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py
- rank=21 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::_get_na_rep file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=22 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._left_indexer_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=23 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._to_bool_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=24 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py::IntegerDtype._get_dtype_mapping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py
- rank=25 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::get_datetime_metadata_from_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
- rank=26 layer=FUNCTION tokens=551 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/sorting.py::get_indexer_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/sorting.py
- rank=27 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::data_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py
- rank=28 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py::empty_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer_dups [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_dups(self, dtype, monotonic):
        self.data.get_indexer_for(self.indexer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_numeric.py::TestFloatNumericIndex.mixed_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_numeric.py]
    def mixed_index(self, dtype):
        return Index([1.5, 2, 3, 4, 5], dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::coerce_indexer_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def coerce_indexer_dtype(indexer: np.ndarray, categories: Index) -> np.ndarray:
    """coerce the indexer input array to the smallest dtype possible"""
    length = len(categories)
    if length < _int8_max:
        return ensure_int8(indexer)
    elif length < _int16_max:
        return ensure_int16(indexer)
    elif length < _int32_max:
        return ensure_int32(indexer)
    return ensure_int64(indexer)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tslibs/test_fields.py::dtindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tslibs/test_fields.py]
def dtindex():
    dtindex = np.arange(5, dtype=np.int64) * 10**9 * 3600 * 24 * 32
    dtindex.flags.writeable = False
    return dtindex

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        if not all(isinstance(x, IntervalDtype) for x in dtypes):
            return None

        closed = cast("IntervalDtype", dtypes[0]).closed
        if not all(cast("IntervalDtype", x).closed == closed for x in dtypes):
            return np.dtype(object)

        from pandas.core.dtypes.cast import find_common_type

        common = find_common_type([cast("IntervalDtype", x).subtype for x in dtypes])
        if common == object:
            return np.dtype(object)
        return IntervalDtype(common, closed=closed)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer(self, dtype, monotonic):
        self.data.get_indexer(self.indexer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py::dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py]
def dtype():
    return IntervalDtype()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py]
def _is_dt_or_td(dtype: DtypeObj) -> bool:
    # Note: the dtype here comes from an Index.dtype, so we know that any
    #  dt64/td64 dtype is of a supported unit.
    return isinstance(dtype, DatetimeTZDtype) or lib.is_np_dtype(dtype, "mM")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::FindValidIndex.time_first_valid_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_first_valid_index(self, dtype):
        self.df.first_valid_index()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py::numeric_indexing_engine_type_and_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py]
def numeric_indexing_engine_type_and_dtype(request):
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._dtype_to_subclass [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _dtype_to_subclass(cls, dtype: DtypeObj) -> type[Index]:
        # Delay import for perf. https://github.com/pandas-dev/pandas/pull/31423

        if isinstance(dtype, ExtensionDtype):
            return dtype.index_class

        if dtype.kind == "M":
            from pandas import DatetimeIndex

            return DatetimeIndex

        elif dtype.kind == "m":
            from pandas import TimedeltaIndex

            return TimedeltaIndex

        elif dtype.kind == "O":
            # NB: assuming away MultiIndex
            return Index

        elif issubclass(dtype.type, str) or is_numeric_dtype(dtype):
            return Index

        raise NotImplementedError(dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_numeric.py::TestNumericInt.simple_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/numeric/test_numeric.py]
    def simple_index(self, dtype):
        return Index(range(0, 20, 2), dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def dtype(self) -> IntervalDtype:
        return self._dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py::get_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/compat.py]
def get_dtype(obj) -> DtypeObj:
    if isinstance(obj, DataFrame):
        # Note: we are assuming only one column
        return obj.dtypes.iat[0]
    else:
        return obj.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        if all(isinstance(t, DatetimeTZDtype) and t.tz == self.tz for t in dtypes):
            np_dtype = np.max(
                [cast("DatetimeTZDtype", t).base for t in [self, *dtypes]]
            )
            unit = np.datetime_data(np_dtype)[0]
            unit = cast("TimeUnit", unit)
            return type(self)(unit=unit, tz=self.tz)
        return super()._get_common_dtype(dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::SparseDtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        # TODO for now only handle SparseDtypes and numpy dtypes => extend
        # with other compatible extension dtypes
        from pandas.core.dtypes.cast import np_find_common_type

        if any(
            isinstance(x, ExtensionDtype) and not isinstance(x, SparseDtype)
            for x in dtypes
        ):
            return None

        fill_values = [x.fill_value for x in dtypes if isinstance(x, SparseDtype)]
        fill_value = fill_values[0]

        from pandas import isna

        # np.nan isn't a singleton, so we may end up with multiple
        # NaNs here, so we ignore the all NA case too.
        if config["mode"]["performance_warnings"] and (
            not (len(set(fill_values)) == 1 or isna(fill_values).all())
        ):
            warnings.warn(
                "Concatenating sparse arrays with multiple fill "
                f"values: '{fill_values}'. Picking the first and "
                "converting the rest.",
                PerformanceWarning,
                stacklevel=find_stack_level(),
            )
        np_dtypes = (x.subtype if isinstance(x, SparseDtype) else x for x in dtypes)
        # error: Argument 1 to "np_find_common_type" has incompatible type
        # "*Generator[Any | dtype[Any] | ExtensionDtype, None, None]";
        # expected "dtype[Any]"  [arg-type]
        return SparseDtype(np_find_common_type(*np_dtypes), fill_value=fill_value)  # type: ignore [arg-type]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::index_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def index_indexing(index, idx):
    if isinstance(index, IndexType):

        def index_getitem(index, idx):
            return index._data[idx]

        return index_getitem

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/dim2.py::Dim2CompatTests.get_reduction_result_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/dim2.py]
        def get_reduction_result_dtype(dtype):
            # windows and 32bit builds will in some cases have int32/uint32
            #  where other builds will have int64/uint64.
            if dtype.itemsize == 8:
                return dtype
            elif dtype.kind in "ib":
                return NUMPY_INT_TO_DTYPE[np.dtype(int)]
            else:
                # i.e. dtype.kind == "u"
                return NUMPY_INT_TO_DTYPE[np.dtype("uint")]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py::typeof_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/extensions.py]
def typeof_index(val, c) -> IndexType:
    """
    This will assume that only strings are in object dtype
    index.
    (you should check this before this gets lowered down to numba)
    """
    # arrty = typeof_impl(val._data, c)
    arrty = typeof_impl(val._numba_data, c)
    assert arrty.ndim == 1
    return IndexType(arrty.dtype, arrty.layout, type(val))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::_get_na_rep [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
def _get_na_rep(dtype: DtypeObj) -> str:
    if isinstance(dtype, ExtensionDtype):
        return f"{dtype.na_value}"
    else:
        dtype_type = dtype.type

    return {np.datetime64: "NaT", np.timedelta64: "NaT"}.get(dtype_type, "NaN")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._left_indexer_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _left_indexer_unique(self, other: Self) -> npt.NDArray[np.intp]:
        # Caller is responsible for ensuring other.dtype == self.dtype
        sv = self._get_join_target()
        ov = other._get_join_target()
        # similar but not identical to ov.searchsorted(sv)
        return libjoin.left_join_indexer_unique(sv, ov)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._to_bool_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
        def _to_bool_indexer(indexer) -> npt.NDArray[np.bool_]:
            if isinstance(indexer, slice):
                new_indexer = np.zeros(n, dtype=np.bool_)
                new_indexer[indexer] = True
                return new_indexer
            return indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py::IntegerDtype._get_dtype_mapping [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py]
    def _get_dtype_mapping(cls) -> dict[np.dtype, IntegerDtype]:
        return NUMPY_INT_TO_DTYPE

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::get_datetime_metadata_from_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c]
PyArray_DatetimeMetaData
get_datetime_metadata_from_dtype(PyArray_Descr *dtype) {
#if NPY_ABI_VERSION < 0x02000000
#  define PyDataType_C_METADATA(dtype) ((dtype)->c_metadata)
#endif
  return ((PyArray_DatetimeDTypeMetaData *)PyDataType_C_METADATA(dtype))->meta;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/sorting.py::get_indexer_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/sorting.py]
def get_indexer_indexer(
    target: Index,
    level: Level | list[Level] | None,
    ascending: list[bool] | bool,
    kind: SortKind,
    na_position: NaPosition,
    sort_remaining: bool,
    key: IndexKeyFunc,
) -> npt.NDArray[np.intp] | None:
    """
    Helper method that return the indexer according to input parameters for
    the sort_index method of DataFrame and Series.

    Parameters
    ----------
    target : Index
    level : int or level name or list of ints or list of level names
    ascending : bool or list of bools, default True
    kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}
    na_position : {'first', 'last'}
    sort_remaining : bool
    key : callable, optional

    Returns
    -------
    Optional[ndarray[intp]]
        The indexer for the new index.
    """

    # error: Incompatible types in assignment (expression has type
    # "Union[ExtensionArray, ndarray[Any, Any], Index, Series]", variable has
    # type "Index")
    target = ensure_key_mapped(target, key, levels=level)  # type: ignore[assignment]
    target = target._sort_levels_monotonic()

    if level is not None:
        _, indexer = target.sortlevel(
            level,  # type: ignore[arg-type]
            ascending=ascending,
            sort_remaining=sort_remaining,
            na_position=na_position,
        )
    elif (np.all(ascending) and target.is_monotonic_increasing) or (
        not np.any(ascending) and target.is_monotonic_decreasing
    ):
        # Check monotonic-ness before sort an index (GH 11080)
        return None
    elif isinstance(target, ABCMultiIndex):
        codes = [lev.codes for lev in target._get_codes_for_sorting()]
        indexer = lexsort_indexer(
            codes, orders=ascending, na_position=na_position, codes_given=True
        )
    else:
        # ascending can only be a Sequence for MultiIndex
        indexer = nargsort(
            target,
            kind=kind,
            ascending=cast("bool", ascending),
            na_position=na_position,
        )
    return indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::data_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py]
def data_missing(dtype):
    if dtype.kind == "f":
        return pd.array([pd.NA, 0.1], dtype=dtype)
    elif dtype.kind == "b":
        return pd.array([np.nan, True], dtype=dtype)
    return pd.array([pd.NA, 1], dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py::empty_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_setops.py]
def empty_index(dtype="int64", closed="right"):
    return IntervalIndex(np.array([], dtype=dtype), closed=closed)
```
