# pandas-91 :: tacm-full

query: BUG: TimedeltaIndex.searchsorted accepting invalid types/dtypes (#30831)

## selected nodes

- rank=1 layer=FUNCTION tokens=447 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::find_common_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=2 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=3 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py
- rank=4 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py::listlike_box file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py
- rank=5 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.has_invalid_return_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=6 layer=FUNCTION tokens=341 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_delta_bins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=7 layer=FUNCTION tokens=1375 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::_cast_to_stata_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=8 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::numeric_idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py
- rank=9 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=10 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::timedelta_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=11 layer=FUNCTION tokens=266 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._needs_i8_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=12 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py
- rank=13 layer=FUNCTION tokens=353 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_monotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=14 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=15 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_sparse.py::dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_sparse.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::find_common_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def find_common_type(types: list[DtypeObj]) -> DtypeObj:  # type: ignore[misc]
    """
    Find a common data type among the given dtypes.

    Parameters
    ----------
    types : list of dtypes

    Returns
    -------
    pandas extension or numpy dtype

    See Also
    --------
    numpy.find_common_type

    """
    if not types:
        raise ValueError("no types given")

    first = types[0]

    # workaround for find_common_type([np.dtype('datetime64[ns]')] * 2)
    # => object
    if lib.dtypes_all_equal(list(types)):
        return first

    # get unique types (dict.fromkeys is used as order-preserving set())
    types = list(dict.fromkeys(types).keys())

    if any(isinstance(t, ExtensionDtype) for t in types):
        for t in types:
            if isinstance(t, ExtensionDtype):
                res = t._get_common_dtype(types)
                if res is not None:
                    return res
        return np.dtype("object")

    # At this point, all types are np.dtype (ExtensionDtype was handled above)
    np_types = cast("list[np.dtype]", types)

    # take lowest unit
    if all(lib.is_np_dtype(t, "M") for t in np_types):
        return np.dtype(max(np_types))
    if all(lib.is_np_dtype(t, "m") for t in np_types):
        return np.dtype(max(np_types))

    # don't mix bool / int or float or complex
    # this is different from numpy, which casts bool with float/int as int
    has_bools = any(t.kind == "b" for t in np_types)
    if has_bools:
        for t in np_types:
            if t.kind in "iufc":
                return np.dtype("object")

    return np_find_common_type(*np_types)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py]
def types_data_frame(types_data):
    dtypes = {
        "TextCol": "str",
        "DateCol": "str",
        "IntDateCol": "int64",
        "IntDateOnlyCol": "int64",
        "FloatCol": "float",
        "IntCol": "int64",
        "BoolCol": "int64",
        "IntColWithNull": "float",
        "BoolColWithNull": "float",
    }
    df = DataFrame(types_data)
    return df[dtypes.keys()].astype(dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py]
    def _test_searchsorted_bool_dtypes(self, data_for_sorting, as_series):
        # We call this from test_searchsorted in cases where we have a
        #  boolean-like dtype. The non-bool test assumes we have more than 2
        #  unique values.
        dtype = data_for_sorting.dtype
        data_for_sorting = pd.array([True, False], dtype=dtype)
        b, a = data_for_sorting
        arr = type(data_for_sorting)._from_sequence([a, b], dtype=dtype)

        if as_series:
            arr = pd.Series(arr)
        assert arr.searchsorted(a) == 0
        assert arr.searchsorted(a, side="right") == 1

        assert arr.searchsorted(b) == 1
        assert arr.searchsorted(b, side="right") == 2

        result = arr.searchsorted(arr.take([0, 1]))
        expected = np.array([0, 1], dtype=np.intp)

        tm.assert_numpy_array_equal(result, expected)

        # sorter
        sorter = np.array([1, 0])
        assert data_for_sorting.searchsorted(a, sorter=sorter) == 0

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py::listlike_box [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py]
def listlike_box(request):
    """
    Types that may be passed as the indexer to searchsorted.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.has_invalid_return_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py]
    def has_invalid_return_type(self) -> bool:
        types = self.operand_types
        obj_dtype_set = frozenset([np.dtype("object")])
        return self.return_type == object and types - obj_dtype_set

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_delta_bins [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _get_time_delta_bins(self, ax: TimedeltaIndex):
        if not isinstance(ax, TimedeltaIndex):
            raise TypeError(
                "axis must be a TimedeltaIndex, but got "
                f"an instance of {type(ax).__name__}"
            )

        if not isinstance(self.freq, (Tick, Day)):
            # GH#51896
            raise ValueError(
                "Resampling on a TimedeltaIndex requires fixed-duration `freq`, "
                f"e.g. '24h' or '3D', not {self.freq}"
            )

        if not len(ax):
            binner = labels = TimedeltaIndex(data=[], freq=self.freq, name=ax.name)
            return binner, [], labels

        start, end = ax.min(), ax.max()

        if self.closed == "right":
            end += self.freq  # type: ignore[operator]

        labels = binner = timedelta_range(
            start=start, end=end, freq=self.freq, name=ax.name
        )

        end_stamps = labels
        if self.closed == "left":
            end_stamps += self.freq

        bins = ax.searchsorted(end_stamps, side=self.closed)

        if self.offset:
            # GH 10530 & 31809
            labels += self.offset

        return binner, bins, labels

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::_cast_to_stata_types [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py]
def _cast_to_stata_types(data: DataFrame) -> DataFrame:
    """
    Checks the dtypes of the columns of a pandas DataFrame for
    compatibility with the data types and ranges supported by Stata, and
    converts if necessary.

    Parameters
    ----------
    data : DataFrame
        The DataFrame to check and convert

    Notes
    -----
    Numeric columns in Stata must be one of int8, int16, int32, float32 or
    float64, with some additional value restrictions.  int8 and int16 columns
    are checked for violations of the value restrictions and upcast if needed.
    int64 data is not usable in Stata, and so it is downcast to int32 whenever
    the value are in the int32 range, and sidecast to float64 when larger than
    this range.  If the int64 values are outside of the range of those
    perfectly representable as float64 values, a warning is raised.

    bool columns are cast to int8.  uint columns are converted to int of the
    same size if there is no loss in precision, otherwise are upcast to a
    larger type.  uint64 is currently not supported since it is concerted to
    object in a DataFrame.
    """
    ws = ""
    # original, if small, if large
    conversion_data: tuple[
        tuple[type, type, type],
        tuple[type, type, type],
        tuple[type, type, type],
        tuple[type, type, type],
        tuple[type, type, type],
    ] = (
        (np.bool_, np.int8, np.int8),
        (np.uint8, np.int8, np.int16),
        (np.uint16, np.int16, np.int32),
        (np.uint32, np.int32, np.int64),
        (np.uint64, np.int64, np.float64),
    )

    float32_max = struct.unpack("<f", b"\xff\xff\xff\x7e")[0]
    float64_max = struct.unpack("<d", b"\xff\xff\xff\xff\xff\xff\xdf\x7f")[0]

    for col in data:
        # Cast from unsupported types to supported types
        is_nullable_int = (
            isinstance(data[col].dtype, ExtensionDtype)
            and data[col].dtype.kind in "iub"
        )
        # We need to find orig_missing before altering data below
        orig_missing = data[col].isna()
        if is_nullable_int:
            fv = 0 if data[col].dtype.kind in "iu" else False
            # Replace with NumPy-compatible column
            data[col] = data[col].fillna(fv).astype(data[col].dtype.numpy_dtype)
        elif isinstance(data[col].dtype, ExtensionDtype):
            if getattr(data[col].dtype, "numpy_dtype", None) is not None:
                data[col] = data[col].astype(data[col].dtype.numpy_dtype)
            elif is_string_dtype(data[col].dtype):
                # TODO could avoid converting string dtype to object here,
                # but handle string dtype in _encode_strings
                data[col] = data[col].astype("object")
                # generate_table checks for None values
                data.loc[data[col].isna(), col] = None

        dtype = data[col].dtype
        empty_df = data.shape[0] == 0
        for c_data in conversion_data:
            if dtype == c_data[0]:
                if empty_df or data[col].max() <= np.iinfo(c_data[1]).max:
                    dtype = c_data[1]
                else:
                    dtype = c_data[2]
                if c_data[2] == np.int64:  # Warn if necessary
                    if data[col].max() >= 2**53:
                        ws = precision_loss_doc.format("uint64", "float64")

                data[col] = data[col].astype(dtype)

        # Check values and upcast if necessary

        if dtype == np.int8 and not empty_df:
            if data[col].max() > 100 or data[col].min() < -127:
                data[col] = data[col].astype(np.int16)
        elif dtype == np.int16 and not empty_df:
            if data[col].max() > 32740 or data[col].min() < -32767:
                data[col] = data[col].astype(np.int32)
        elif dtype == np.int64:
            if empty_df or (
                data[col].max() <= 2147483620 and data[col].min() >= -2147483647
            ):
                data[col] = data[col].astype(np.int32)
            else:
                data[col] = data[col].astype(np.float64)
                if data[col].max() >= 2**53 or data[col].min() <= -(2**53):
                    ws = precision_loss_doc.format("int64", "float64")
        elif dtype in (np.float32, np.float64):
            if np.isinf(data[col]).any():
                raise ValueError(
                    f"Column {col} contains infinity or -infinity"
                    "which is outside the range supported by Stata."
                )
            value = data[col].max()
            if dtype == np.float32 and value > float32_max:
                data[col] = data[col].astype(np.float64)
            elif dtype == np.float64:
                if value > float64_max:
                    raise ValueError(
                        f"Column {col} has a maximum value ({value}) outside the range "
                        f"supported by Stata ({float64_max})"
                    )
        if is_nullable_int:
            if orig_missing.any():
                # Replace missing by Stata sentinel value
                sentinel = StataMissingValue.BASE_MISSING_VALUES[data[col].dtype.name]
                data.loc[orig_missing, col] = sentinel
    if ws:
        warnings.warn(
            ws,
            PossiblePrecisionLoss,
            stacklevel=find_stack_level(),
        )

    return data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::numeric_idx [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py]
def numeric_idx(request):
    """
    Several types of numeric-dtypes Index objects
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py]
    def time_searchsorted(self, dtype):
        key = "2" if dtype == "str" else 2
        self.s.searchsorted(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::timedelta_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py]
def timedelta_index():
    """
    A fixture to provide TimedeltaIndex objects with different frequencies.
     Most TimedeltaArray behavior is already tested in TimedeltaIndex tests,
    so here we just test that the TimedeltaArray behavior matches
    the TimedeltaIndex behavior.
    """
    # TODO: flesh this out
    return TimedeltaIndex(["1 Day", "3 Hours", "NaT"])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._needs_i8_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
    def _needs_i8_conversion(self, key) -> bool:
        """
        Check if a given key needs i8 conversion. Conversion is necessary for
        Timestamp, Timedelta, DatetimeIndex, and TimedeltaIndex keys. An
        Interval-like requires conversion if its endpoints are one of the
        aforementioned types.

        Assumes that any list-like data has already been cast to an Index.

        Parameters
        ----------
        key : scalar or Index-like
            The key that should be checked for i8 conversion

        Returns
        -------
        bool
        """
        key_dtype = getattr(key, "dtype", None)
        if isinstance(key_dtype, IntervalDtype) or isinstance(key, Interval):
            return self._needs_i8_conversion(key.left)

        i8_types = (Timestamp, Timedelta, DatetimeIndex, TimedeltaIndex)
        return isinstance(key, i8_types)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py]
    def _check_setitem_invalid(self, ser, invalid, indexer):
        orig_ser = ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser[indexer] = invalid
            ser = orig_ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser.iloc[indexer] = invalid
            ser = orig_ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser.loc[indexer] = invalid
            ser = orig_ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser[:] = invalid

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_monotonic [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
    def _get_indexer_monotonic(self, target: Index) -> npt.NDArray[np.intp]:
        """
        Use searchsorted on endpoints for O(n*log(m)) scalar lookups on
        a monotonic non-overlapping IntervalIndex, instead of IntervalTree
        which scales poorly for large target arrays. See GH#47614.
        """
        # Caller is responsible for checking self.is_monotonic_increasing
        closed_right = self.closed in ("right", "both")
        closed_left = self.closed in ("left", "both")

        # searchsorted on right endpoints to find candidate bin
        side: Literal["left", "right"] = "left" if closed_right else "right"
        indexer = self.right.searchsorted(target, side=side)

        nbins = len(self)
        past_end = indexer >= nbins
        indexer = np.minimum(indexer, nbins - 1)

        # Verify values fall within the candidate bin's left bound
        left_values = self.left[indexer]
        if closed_left:
            left_miss = target < left_values
        else:
            left_miss = target <= left_values

        na_mask = isna(target)
        invalid = past_end | left_miss | na_mask
        indexer = np.where(invalid, -1, indexer)
        return ensure_platform_int(indexer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_contains(self):
        self.c.searchsorted(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_sparse.py::dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_sparse.py]
def dtype():
    return SparseDtype()
```
