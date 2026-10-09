# pandas-14 :: minilm

query: BUG: DataFrame[object] + Series[dt64], test parametrization (#33824)

## selected nodes

- rank=1 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=2 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::frame_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=3 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::Apply.apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=4 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser._parse file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py
- rank=5 layer=FUNCTION tokens=315 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py::backend file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py
- rank=6 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=7 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::assert_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=8 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._convert_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=9 layer=FUNCTION tokens=245 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.wrap_results file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=10 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Construction.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py
- rank=11 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._constructor_expanddim file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=12 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py::data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py
- rank=13 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::_get_data_and_dtype_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=14 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py::func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py
- rank=15 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.__dataframe__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=16 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::SparseSeriesToFrame.time_series_to_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py
- rank=17 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::Apply.transform_str_or_callable file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=18 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding.nunique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py
- rank=19 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::_wrap_transform_general_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=20 layer=FUNCTION tokens=222 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=21 layer=FUNCTION tokens=229 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=22 layer=FUNCTION tokens=511 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py::_validate_apply_axis_arg file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py
- rank=23 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py::NDFrameDescriberAbstract.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py
- rank=24 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser.parse file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def dtypes(self) -> DtypeObj:
        """
        Return the dtype object of the underlying data.

        Unlike ``DataFrame.dtypes``, which returns a Series of dtypes for each
        column, ``Series.dtypes`` returns a single dtype object representing
        the type of all elements in the Series.

        See Also
        --------
        DataFrame.dtypes :  Return the dtypes in the DataFrame.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> s.dtypes
        dtype('int64')
        """
        # DataFrame compatibility
        return self.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::frame_or_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def frame_or_series(request):
    """
    Fixture to parametrize over DataFrame and Series.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::Apply.apply [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def apply(self) -> DataFrame | Series:
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser._parse [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py]
    def _parse(self) -> DataFrame | Series:
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py::backend [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py]
def backend(request):
    if request.param == "numpy":

        def make_dataframe(*args, **kwargs):
            return DataFrame(*args, **kwargs)

        def make_series(*args, **kwargs):
            return Series(*args, **kwargs)

    elif request.param == "nullable":

        def make_dataframe(*args, **kwargs):
            df = DataFrame(*args, **kwargs)
            df_nullable = df.convert_dtypes()
            # convert_dtypes will try to cast float to int if there is no loss in
            # precision -> undo that change
            for col in df.columns:
                if is_float_dtype(df[col].dtype) and not is_float_dtype(
                    df_nullable[col].dtype
                ):
                    df_nullable[col] = df_nullable[col].astype("Float64")
            # copy final result to ensure we start with a fully self-owning DataFrame
            return df_nullable.copy()

        def make_series(*args, **kwargs):
            ser = Series(*args, **kwargs)
            return ser.convert_dtypes().copy()

    return request.param, make_dataframe, make_series

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::assert_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py]
def assert_dtype(obj, expected_dtype):
    """
    Helper to check the dtype for a Series, Index, or single-column DataFrame.
    """
    dtype = tm.get_dtype(obj)

    assert dtype == expected_dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._convert_obj [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _convert_obj(self, obj: NDFrameT) -> NDFrameT:
        """
        Provide any conversions for the object in order to correctly handle.

        Parameters
        ----------
        obj : Series or DataFrame

        Returns
        -------
        Series or DataFrame
        """
        return obj._consolidate()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.wrap_results [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def wrap_results(self, results: ResType, res_index: Index) -> DataFrame | Series:
        from pandas import Series

        # see if we can infer the results
        if len(results) > 0 and 0 in results and is_sequence(results[0]):
            return self.wrap_results_for_axis(results, res_index)

        # dict of scalars

        # the default dtype of an empty Series is `object`, but this
        # code can be hit by df.mean() where the result should have dtype
        # float64 even if it's an empty Series.
        constructor_sliced = self.obj._constructor_sliced
        if len(results) == 0 and constructor_sliced is Series:
            result = constructor_sliced(results, dtype=np.float64)
        else:
            result = constructor_sliced(results)
        result.index = res_index

        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Construction.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py]
    def setup(self, pd_type, dtype):
        series_arr = np.array(
            [str(i) * 10 for i in range(100_000)], dtype=self.dtype_mapping[dtype]
        )
        if pd_type == "series":
            self.arr = series_arr
        elif pd_type == "frame":
            self.arr = series_arr.reshape((50_000, 2)).copy()
        elif pd_type == "categorical_series":
            # GH37371. Testing construction of string series/frames from ExtensionArrays
            self.arr = Categorical(series_arr)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._constructor_expanddim [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _constructor_expanddim(self) -> Callable[..., DataFrame]:
        """
        Used when a manipulation result has one higher dimension as the
        original, such as Series.to_frame()
        """
        from pandas.core.frame import DataFrame

        return DataFrame

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py::data [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py]
def data(request):
    """Fixture returning parametrized (array, scalar) tuple.

    Used to test equivalence of scalars, numpy arrays with array ops, and the
    equivalence of DataFrame and Series ops.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::_get_data_and_dtype_name [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
def _get_data_and_dtype_name(data: ArrayLike):
    """
    Convert the passed data into a storable form and a dtype string.
    """
    if isinstance(data, Categorical):
        data = data.codes

    if isinstance(data.dtype, DatetimeTZDtype):
        # For datetime64tz we need to drop the TZ in tests TODO: why?
        dtype_name = f"datetime64[{data.dtype.unit}]"
    else:
        dtype_name = data.dtype.name

    if data.dtype.kind in "mM":
        data = np.asarray(data.view("i8"))
        # TODO: we used to reshape for the dt64tz case, but no longer
        #  doing that doesn't seem to break anything.  why?

    elif isinstance(data, PeriodIndex):
        data = data.asi8

    data = np.asarray(data)
    return data, dtype_name

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py::func [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py]
    def func(x):
        # transform is using apply iff x is not a DataFrame
        if use_apply == isinstance(x, frame_or_series):
            # Force transform to fallback
            raise ValueError
        return x + 1

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.__dataframe__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py]
    def __dataframe__(self, nan_as_null: bool = False, allow_copy: bool = True):
        """Construct a new interchange object, potentially changing the parameters."""

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::SparseSeriesToFrame.time_series_to_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py]
    def time_series_to_frame(self):
        pd.DataFrame(self.series)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::Apply.transform_str_or_callable [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def transform_str_or_callable(self, func) -> DataFrame | Series:
        """
        Compute transform in the case of a string or callable func
        """
        obj = self.obj
        args = self.args
        kwargs = self.kwargs

        if isinstance(func, str):
            return self._apply_str(obj, func, *args, **kwargs)

        # Two possible ways to use a UDF - apply or call directly
        try:
            return obj.apply(func, args=args, **kwargs)
        except Exception:
            return func(obj, *args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding.nunique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py]
    def nunique(
        self,
        numeric_only: bool = False,
    ):
        """
        Calculate the expanding nunique.

        .. versionadded:: 3.0.0

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns.

        Returns
        -------
        Series or DataFrame
            Return type is the same as the original object with ``np.float64`` dtype.

        See Also
        --------
        Series.expanding : Calling expanding with Series data.
        DataFrame.expanding : Calling expanding with DataFrames.
        Series.nunique : Aggregating nunique for Series.
        DataFrame.nunique : Aggregating nunique for DataFrame.

        Examples
        --------
        >>> s = pd.Series([1, 4, 2, 3, 5, 3])
        >>> s.expanding().nunique()
        0    1.0
        1    2.0
        2    3.0
        3    4.0
        4    5.0
        5    5.0
        dtype: float64
        """
        return super().nunique(
            numeric_only=numeric_only,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::_wrap_transform_general_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
def _wrap_transform_general_frame(
    obj: DataFrame, group: DataFrame, res: DataFrame | Series
) -> DataFrame:
    from pandas import concat

    if isinstance(res, Series):
        # we need to broadcast across the
        # other dimension; this will preserve dtypes
        # GH14457
        if res.index.is_(obj.index):
            res_frame = concat([res] * len(group.columns), axis=1, ignore_index=True)
            res_frame.columns = group.columns
            res_frame.index = group.index
        else:
            res_frame = obj._constructor(
                np.tile(res.values, (len(group.index), 1)),
                columns=group.columns,
                index=group.index,
            )
        assert isinstance(res_frame, DataFrame)
        return res_frame
    elif isinstance(res, DataFrame) and not res.index.is_(group.index):
        return res._align_frame(group)[0]
    else:
        return res

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def dtype(self) -> DtypeObj:
        """
        Return the dtype object of the underlying data.

        This is the dtype of the array backing the Series (or the single dtype
        for a DataFrame column). For extension types, it returns the
        corresponding extension dtype.

        See Also
        --------
        Series.dtypes : Return the dtype object of the underlying data.
        Series.astype : Cast a pandas object to a specified dtype dtype.
        Series.convert_dtypes : Convert columns to the best possible dtypes using dtypes
            supporting pd.NA.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> s.dtype
        dtype('int64')
        """
        return self._mgr.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def dtype(self) -> ExtensionDtype:
        """
        An instance of ExtensionDtype.

        This property returns the dtype object associated with this
        ExtensionArray. The dtype describes the type of data stored
        in the array.

        See Also
        --------
        api.extensions.ExtensionDtype : Base class for extension dtypes.
        api.extensions.ExtensionArray : Base class for extension array types.
        api.extensions.ExtensionArray.dtype : The dtype of an ExtensionArray.
        Series.dtype : The dtype of a Series.
        DataFrame.dtype : The dtype of a DataFrame.

        Examples
        --------
        >>> pd.array([1, 2, 3]).dtype
        Int64Dtype()
        """
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py::_validate_apply_axis_arg [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py]
def _validate_apply_axis_arg(
    arg: NDFrame | Sequence | np.ndarray,
    arg_name: str,
    dtype: Any | None,
    data: NDFrame,
) -> np.ndarray:
    """
    For the apply-type methods, ``axis=None`` creates ``data`` as DataFrame, and for
    ``axis=[1,0]`` it creates a Series. Where ``arg`` is expected as an element
    of some operator with ``data`` we must make sure that the two are compatible shapes,
    or raise.

    Parameters
    ----------
    arg : sequence, Series or DataFrame
        the user input arg
    arg_name : string
        name of the arg for use in error messages
    dtype : numpy dtype, optional
        forced numpy dtype if given
    data : Series or DataFrame
        underling subset of Styler data on which operations are performed

    Returns
    -------
    ndarray
    """
    dtype = {"dtype": dtype} if dtype else {}
    # raise if input is wrong for axis:
    if isinstance(arg, Series) and isinstance(data, DataFrame):
        raise ValueError(
            f"'{arg_name}' is a Series but underlying data for operations "
            f"is a DataFrame since 'axis=None'"
        )
    if isinstance(arg, DataFrame) and isinstance(data, Series):
        raise ValueError(
            f"'{arg_name}' is a DataFrame but underlying data for "
            f"operations is a Series with 'axis in [0,1]'"
        )
    if isinstance(arg, (Series, DataFrame)):  # align indx / cols to data
        arg = arg.reindex_like(data).to_numpy(**dtype)
    else:
        arg = np.asarray(arg, **dtype)
        assert isinstance(arg, np.ndarray)  # mypy requirement
        if arg.shape != data.shape:  # check valid input
            raise ValueError(
                f"supplied '{arg_name}' is not correct shape for data over "
                f"selected 'axis': got {arg.shape}, "
                f"expected {data.shape}"
            )
    return arg

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py::NDFrameDescriberAbstract.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py]
    def __init__(self, obj: DataFrame | Series) -> None:
        self.obj = obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser.parse [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py]
    def parse(self) -> DataFrame | Series:
        obj = self._parse()

        if self.convert_axes:
            obj = self._convert_axes(obj)
        obj = self._try_convert_types(obj)
        return obj
```
