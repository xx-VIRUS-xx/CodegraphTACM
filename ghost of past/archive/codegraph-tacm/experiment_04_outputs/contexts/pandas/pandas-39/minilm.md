# pandas-39 :: minilm

query: BUG: Fixed strange behaviour of pd.DataFrame.drop() with inplace argu… (#30501)

## selected nodes

- rank=1 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_na file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=2 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/reduce.py::BaseReduceTests._get_expected_reduction_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/reduce.py
- rank=3 layer=FUNCTION tokens=876 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::diff file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py
- rank=4 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=5 layer=FUNCTION tokens=692 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dropna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=6 layer=FUNCTION tokens=339 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/reduce.py::BaseReduceTests.check_reduce_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/reduce.py
- rank=7 layer=FUNCTION tokens=528 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.infer_objects file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=8 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_bool file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=9 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/conftest.py::na_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/conftest.py
- rank=10 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py
- rank=11 layer=FUNCTION tokens=457 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::maybe_convert_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=12 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/integer/conftest.py::data_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/integer/conftest.py
- rank=13 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.__dataframe__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py
- rank=14 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dropna.time_dropna_axis_mixed_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=15 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_numpy.py::data_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_numpy.py
- rank=16 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_col.py::XYZAccessor.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_col.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_na [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups_na(self, inplace):
        self.df_nan.drop_duplicates(["key1", "key2"], inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/reduce.py::BaseReduceTests._get_expected_reduction_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/reduce.py]
    def _get_expected_reduction_dtype(self, arr, op_name: str, skipna: bool):
        # Find the expected dtype when the given reduction is done on a DataFrame
        # column with this array.  The default assumes float64-like behavior,
        # i.e. retains the dtype.
        return arr.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py::diff [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/algorithms.py]
def diff(arr, n: int | float | np.integer | np.floating, axis: AxisInt = 0):
    """
    difference of n between self,
    analogous to s-s.shift(n)

    Parameters
    ----------
    arr : ndarray or ExtensionArray
    n : int
        number of periods
    axis : {0, 1}
        axis to shift on
    stacklevel : int, default 3
        The stacklevel for the lost dtype warning.

    Returns
    -------
    shifted
    """

    # added a check on the integer value of period
    # see https://github.com/pandas-dev/pandas/issues/56607
    if not lib.is_integer(n):
        if not (is_float(n) and n.is_integer()):
            raise ValueError("periods must be an integer")
        n = int(n)
    na = np.nan
    dtype = arr.dtype

    is_bool = is_bool_dtype(dtype)
    if is_bool:
        op = operator.xor
    else:
        op = operator.sub

    if isinstance(dtype, NumpyEADtype):
        # NumpyExtensionArray cannot necessarily hold shifted versions of itself.
        arr = arr.to_numpy()
        dtype = arr.dtype

    if not isinstance(arr, np.ndarray):
        # i.e ExtensionArray
        if hasattr(arr, f"__{op.__name__}__"):
            if axis >= arr.ndim:
                raise ValueError(f"cannot diff {type(arr).__name__} on axis={axis}")
            return op(arr, arr.shift(n))
        else:
            raise TypeError(
                f"{type(arr).__name__} has no 'diff' method. "
                "Convert to a suitable dtype prior to calling 'diff'."
            )

    is_timedelta = False
    if arr.dtype.kind in "mM":
        dtype = np.int64
        arr = arr.view("i8")
        na = iNaT
        is_timedelta = True

    elif is_bool:
        # We have to cast in order to be able to hold np.nan
        dtype = np.object_

    elif dtype.kind in "iu":
        # We have to cast in order to be able to hold np.nan

        # int8, int16 are incompatible with float64,
        # see https://github.com/cython/cython/issues/2646
        if arr.dtype.name in ["int8", "int16"]:
            dtype = np.float32
        else:
            dtype = np.float64

    orig_ndim = arr.ndim
    if orig_ndim == 1:
        # reshape so we can always use algos.diff_2d
        arr = arr.reshape(-1, 1)
        # TODO: require axis == 0

    dtype = np.dtype(dtype)
    out_arr = np.empty(arr.shape, dtype=dtype)

    na_indexer = [slice(None)] * 2
    na_indexer[axis] = slice(None, n) if n >= 0 else slice(n, None)
    out_arr[tuple(na_indexer)] = na

    if arr.dtype.name in _diff_special:
        # TODO: can diff_2d dtype specialization troubles be fixed by defining
        #  out_arr inside diff_2d?
        algos.diff_2d(arr, out_arr, int(n), axis, datetimelike=is_timedelta)
    else:
        # To keep mypy happy, _res_indexer is a list while res_indexer is
        #  a tuple, ditto for lag_indexer.
        _res_indexer = [slice(None)] * 2
        _res_indexer[axis] = slice(n, None) if n >= 0 else slice(None, n)
        res_indexer = tuple(_res_indexer)

        _lag_indexer = [slice(None)] * 2
        _lag_indexer[axis] = slice(None, -n) if n > 0 else slice(-n, None)
        lag_indexer = tuple(_lag_indexer)

        out_arr[res_indexer] = op(arr[res_indexer], arr[lag_indexer])

    if is_timedelta:
        out_arr = out_arr.view("timedelta64[ns]")

    if orig_ndim == 1:
        out_arr = out_arr[:, 0]
    return out_arr

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_int [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups_int(self, inplace):
        self.df_int.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dropna [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def dropna(
        self,
        *,
        axis: Axis = 0,
        inplace: bool = False,
        how: AnyAll | None = None,
        ignore_index: bool = False,
    ) -> Series | None:
        """
        Return a new Series with missing values removed.

        See the :ref:`User Guide <missing_data>` for more on which values are
        considered missing, and how to work with missing data.

        Parameters
        ----------
        axis : {0 or 'index'}
            Unused. Parameter needed for compatibility with DataFrame.
        inplace : bool, default False
            If True, do operation inplace and return None.
        how : str, optional
            Not in use. Kept for compatibility.
        ignore_index : bool, default ``False``
            If ``True``, the resulting axis will be labeled 0, 1, …, n - 1.

            .. versionadded:: 2.0.0

        Returns
        -------
        Series or None
            Series with NA entries dropped from it or None if ``inplace=True``.

        See Also
        --------
        Series.isna: Indicate missing values.
        Series.notna : Indicate existing (non-missing) values.
        Series.fillna : Replace missing values.
        DataFrame.dropna : Drop rows or columns which contain NA values.
        Index.dropna : Drop missing indices.

        Examples
        --------
        >>> ser = pd.Series([1.0, 2.0, np.nan])
        >>> ser
        0    1.0
        1    2.0
        2    NaN
        dtype: float64

        Drop NA values from a Series.

        >>> ser.dropna()
        0    1.0
        1    2.0
        dtype: float64

        Empty strings are not considered NA values. ``None`` is considered an
        NA value.

        >>> ser = pd.Series([np.nan, 2, pd.NaT, "", None, "I stay"])
        >>> ser
        0       NaN
        1         2
        2       NaT
        3
        4      None
        5    I stay
        dtype: object
        >>> ser.dropna()
        1         2
        3
        5    I stay
        dtype: object
        """
        inplace = validate_bool_kwarg(inplace, "inplace")
        ignore_index = validate_bool_kwarg(ignore_index, "ignore_index")
        # Validate the axis parameter
        self._get_axis_number(axis or 0)

        if self._can_hold_na:
            result = remove_na_arraylike(self)
        elif not inplace:
            result = self.copy(deep=False)
        else:
            result = self

        if ignore_index:
            result.index = default_index(len(result))

        if inplace:
            return self._update_inplace(result)
        else:
            return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/reduce.py::BaseReduceTests.check_reduce_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/reduce.py]
    def check_reduce_frame(self, ser: pd.Series, op_name: str, skipna: bool):
        # Check that the 2D reduction done in a DataFrame reduction "looks like"
        # a wrapped version of the 1D reduction done by Series.
        arr = ser.array
        df = pd.DataFrame({"a": arr})

        kwargs = {"ddof": 1} if op_name in ["var", "std", "sem"] else {}

        cmp_dtype = self._get_expected_reduction_dtype(arr, op_name, skipna)

        # The DataFrame method just calls arr._reduce with keepdims=True,
        #  so this first check is perfunctory.
        result1 = arr._reduce(op_name, skipna=skipna, keepdims=True, **kwargs)
        result2 = getattr(df, op_name)(skipna=skipna, **kwargs).array
        tm.assert_extension_array_equal(result1, result2)

        # Check that the 2D reduction looks like a wrapped version of the
        #  1D reduction
        if not skipna and ser.isna().any():
            expected = pd.array([pd.NA], dtype=cmp_dtype)
        else:
            exp_value = getattr(ser.dropna(), op_name)()
            expected = pd.array([exp_value], dtype=cmp_dtype)

        tm.assert_extension_array_equal(result1, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.infer_objects [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def infer_objects(self, copy: bool | lib.NoDefault = lib.no_default) -> Self:
        """
        Attempt to infer better dtypes for object columns.

        Attempts soft conversion of object-dtyped
        columns, leaving non-object and unconvertible
        columns unchanged. The inference rules are the
        same as during normal Series/DataFrame construction.

        Parameters
        ----------
        copy : bool, default False
            This keyword is now ignored; changing its value will have no
            impact on the method.

            .. deprecated:: 3.0.0

                This keyword is ignored and will be removed in pandas 4.0. Since
                pandas 3.0, this method always returns a new object using a lazy
                copy mechanism that defers copies until necessary
                (Copy-on-Write). See the `user guide on Copy-on-Write
                <https://pandas.pydata.org/docs/dev/user_guide/copy_on_write.html>`__
                for more details.

        Returns
        -------
        same type as input object
            Returns an object of the same type as the input object.

        See Also
        --------
        to_datetime : Convert argument to datetime.
        to_timedelta : Convert argument to timedelta.
        to_numeric : Convert argument to numeric type.
        convert_dtypes : Convert argument to best possible dtype.

        Examples
        --------
        >>> df = pd.DataFrame({"A": ["a", 1, 2, 3]})
        >>> df = df.iloc[1:]
        >>> df
           A
        1  1
        2  2
        3  3

        >>> df.dtypes
        A    object
        dtype: object

        >>> df.infer_objects().dtypes
        A    int64
        dtype: object
        """
        self._check_copy_deprecation(copy)
        new_mgr = self._mgr.convert()
        res = self._constructor_from_mgr(new_mgr, axes=new_mgr.axes)
        return res.__finalize__(self, method="infer_objects")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_bool [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups_bool(self, inplace):
        self.df_bool.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/conftest.py::na_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/conftest.py]
def na_value(dtype):
    """
    The scalar missing value for this type. Default dtype.na_value.

    TODO: can be removed in 3.x (see https://github.com/pandas-dev/pandas/pull/54930)
    """
    return dtype.na_value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py]
    def __init__(self, df: DataFrame, allow_copy: bool = True) -> None:
        """
        Constructor - an instance of this (private) class is returned from
        `pd.DataFrame.__dataframe__`.
        """
        self._df = df.rename(columns=str)
        self._allow_copy = allow_copy
        for i, _col in enumerate(self._df.columns):
            rechunked = maybe_rechunk(self._df.iloc[:, i], allow_copy=allow_copy)
            if rechunked is not None:
                self._df.isetitem(i, rechunked)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/integer/conftest.py::data_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/integer/conftest.py]
def data_missing(dtype):
    """
    Fixture returning array with exactly one NaN and one valid integer,
    according to parametrized integer 'dtype'.

    Used to test dtype conversion with and without missing values.
    """
    return pd.array([pd.NA, 1], dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.__dataframe__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py]
    def __dataframe__(
        self, nan_as_null: bool = False, allow_copy: bool = True
    ) -> PandasDataFrameXchg:
        # `nan_as_null` can be removed here once it's removed from
        # Dataframe.__dataframe__
        return PandasDataFrameXchg(self._df, allow_copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dropna.time_dropna_axis_mixed_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_dropna_axis_mixed_dtypes(self, how, axis):
        self.df_mixed.dropna(how=how, axis=axis)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_numpy.py::data_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_numpy.py]
def data_missing(allow_in_pandas, dtype):
    if dtype.numpy_dtype == "object":
        return NumpyExtensionArray(np.array([np.nan, (1,)], dtype=object))
    return NumpyExtensionArray(np.array([np.nan, 1.0]))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_col.py::XYZAccessor.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_col.py]
        def __init__(self, pandas_obj):
            self._obj = pandas_obj
```
