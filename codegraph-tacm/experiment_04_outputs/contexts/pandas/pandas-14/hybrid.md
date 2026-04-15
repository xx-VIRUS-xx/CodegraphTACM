# pandas-14 :: hybrid

query: BUG: DataFrame[object] + Series[dt64], test parametrization (#33824)

## selected nodes

- rank=1 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=2 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=3 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py::data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py
- rank=4 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._convert_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=5 layer=FUNCTION tokens=307 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding.nunique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py
- rank=6 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py::unpack_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py
- rank=7 layer=FUNCTION tokens=222 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=8 layer=FUNCTION tokens=420 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._maybe_align_series_as_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=9 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::frame_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=10 layer=FUNCTION tokens=315 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py::backend file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/copy_view/test_indexing.py
- rank=11 layer=FUNCTION tokens=314 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.nunique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=12 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::Apply.apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=13 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::box_with_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=14 layer=FUNCTION tokens=348 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=15 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser._parse file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py
- rank=16 layer=FUNCTION tokens=506 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::create_dataframe_all_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=17 layer=FUNCTION tokens=245 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.wrap_results file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=18 layer=FUNCTION tokens=255 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::_check_where_equivalences file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=19 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::_test_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py
- rank=20 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py::data [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py]
def data(request):
    """Fixture returning parametrized (array, scalar) tuple.

    Used to test equivalence of scalars, numpy arrays with array ops, and the
    equivalence of DataFrame and Series ops.
    """
    return request.param

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py::unpack_obj [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py]
def unpack_obj(obj, klass, axis):
    """
    Helper to ensure we have the right type of object for a test parametrized
    over frame_or_series.
    """
    if klass is not DataFrame:
        obj = obj["A"]
        if axis != 0:
            pytest.skip(f"Test is only for DataFrame with axis={axis}")
    return obj

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._maybe_align_series_as_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def _maybe_align_series_as_frame(self, series: Series, axis: AxisInt):
        """
        If the Series operand is not EA-dtype, we can broadcast to 2D and operate
        blockwise.
        """
        rvalues = series._values
        if lib.is_np_dtype(rvalues.dtype):
            # We can losslessly+cheaply cast to ndarray
            # i.e. ndarray or dt64[naive], td64
            # TODO(EA2D): no need to special case with 2D EAs
            rvalues = np.asarray(rvalues)

            if axis == 0:
                rvalues = rvalues.reshape(-1, 1)
            else:
                rvalues = rvalues.reshape(1, -1)

            rvalues = np.broadcast_to(rvalues, self.shape)
            # pass dtype to avoid doing inference
            # copy=False is safe because this is a temporary DataFrame used only
            # as the right operand in blockwise arithmetic.
            df = self._constructor(
                rvalues,
                index=self.index,
                columns=self.columns,
                dtype=rvalues.dtype,
                copy=False,
            )
        # GH#61581
        elif axis == 0:
            df = DataFrame(dict.fromkeys(range(self.shape[1]), rvalues))
        else:
            nrows = self.shape[0]
            df = DataFrame(
                {i: rvalues[[i]].repeat(nrows) for i in range(self.shape[1])},
                dtype=rvalues.dtype,
            )
        df.index = self.index
        df.columns = self.columns
        return df.__finalize__(series)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::frame_or_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def frame_or_series(request):
    """
    Fixture to parametrize over DataFrame and Series.
    """
    return request.param

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.nunique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def nunique(
        self,
        numeric_only: bool = False,
    ):
        """
        Calculate the rolling nunique.

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
        Series.rolling : Calling rolling with Series data.
        DataFrame.rolling : Calling rolling with DataFrames.
        Series.nunique : Aggregating nunique for Series.
        DataFrame.nunique : Aggregating nunique for DataFrame.

        Examples
        --------
        >>> s = pd.Series([1, 4, 2, np.nan, 3, 3, 4, 5])
        >>> s.rolling(3).nunique()
        0    NaN
        1    NaN
        2    3.0
        3    NaN
        4    NaN
        5    NaN
        6    2.0
        7    3.0
        dtype: float64
        """
        return super().nunique(
            numeric_only=numeric_only,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::Apply.apply [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def apply(self) -> DataFrame | Series:
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::box_with_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def box_with_array(request):
    """
    Fixture to test behavior for Index, Series, DataFrame, and pandas Array
    classes
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def dtypes(self):
        """
        Return the dtypes in the DataFrame.

        This returns a Series with the data type of each column.
        The result's index is the original DataFrame's columns. Columns
        with mixed types are stored with the ``object`` dtype. See
        :ref:`the User Guide <basics.dtypes>` for more.

        Returns
        -------
        pandas.Series
            The data type of each column.

        See Also
        --------
        Series.dtypes : Return the dtype object of the underlying data.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "float": [1.0],
        ...         "int": [1],
        ...         "datetime": [pd.Timestamp("20180310")],
        ...         "string": ["foo"],
        ...     }
        ... )
        >>> df.dtypes
        float              float64
        int                  int64
        datetime    datetime64[us]
        string              str
        dtype: object
        """
        data = self._mgr.get_dtypes()
        # copy=False is safe because get_dtypes() returns a new array
        return self._constructor_sliced(
            data, index=self._info_axis, dtype=np.object_, copy=False
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser._parse [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py]
    def _parse(self) -> DataFrame | Series:
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::create_dataframe_all_types [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py]
def create_dataframe_all_types():
    timestamps = Series(
        [
            Timestamp("2013-01-01"),
            NaT,
            Timestamp("2013-01-03"),
            Timestamp("2013-01-04"),
            Timestamp("2013-01-05"),
        ]
    )
    timedeltas = timestamps - timestamps[0]

    data = {
        # "string": Series(
        #     ["a", "b", "c", None, "e"], dtype=StringDtype(na_value=np.nan)
        # ),
        # "object": Series(["a", "b", "c", None, "e"], dtype=object),
        # "object_nan": Series(["a", "b", "c", np.nan, "e"], dtype=object),
        "int": list(range(1, 6)),
        "uint64": np.arange(3, 8).astype("uint64"),
        "float": [0.1, 0.2, 0.3, 0.4, np.nan],
        "float32": Series([0.1, 0.2, 0.3, 0.4, np.nan], dtype="float32"),
        "bool": [True, False, True, False, True],
        "datetime_ns": timestamps.dt.as_unit("ns"),
        "datetime_us": timestamps.dt.as_unit("us"),
        "datetime_ms": timestamps.dt.as_unit("ms"),
        "datetime_s": timestamps.dt.as_unit("s"),
        "datetimetz_ns": timestamps.dt.tz_localize("US/Eastern").dt.as_unit("ns"),
        "datetimetz_us": timestamps.dt.tz_localize("US/Eastern").dt.as_unit("us"),
        "timedelta_ns": timedeltas.dt.as_unit("ns"),
        "timedelta_us": timedeltas.dt.as_unit("us"),
        "timedelta_ms": timedeltas.dt.as_unit("ms"),
        "timedelta_s": timedeltas.dt.as_unit("s"),
        # "categorical": Categorical(
        #     Series(
        #         ["foo", "bar", "baz",np.nan,"foo"],dtype=StringDtype(na_value=np.nan)
        #     )
        # ),
        # "categorical_object": Categorical(
        #     Series(["foo", "bar", "baz", np.nan, "foo"], dtype=object)
        # ),
        "categorical_int": Categorical([1, 2, 3, np.nan, 1]),
    }
    return DataFrame(data)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::_check_where_equivalences [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py]
def _check_where_equivalences(df, mask, other, expected):
    # similar to tests.series.indexing.test_setitem.SetitemCastingEquivalences
    #  but with DataFrame in mind and less fleshed-out
    res = df.where(mask, other)
    tm.assert_frame_equal(res, expected)

    res = df.mask(~mask, other)
    tm.assert_frame_equal(res, expected)

    # Note: frame.mask(~mask, other, inplace=True) takes some more work bc
    #  Block.putmask does *not* downcast.  The change to 'expected' here
    #  is specific to the cases in test_where_dt64_2d.
    df = df.copy()
    df.mask(~mask, other, inplace=True)
    if not mask.all():
        # with mask.all(), Block.putmask is a no-op, so does not downcast
        expected = expected.copy()
        expected["A"] = expected["A"].astype(object)
    tm.assert_frame_equal(df, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::_test_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py]
def _test_series(dti):
    return Series(np.random.default_rng(2).random(len(dti)), dti)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py::df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py]
def df():
    return DataFrame(
        {"A": [0, 1], "B": [-0.61, -1.22], "C": Series(["ab", "cd"], dtype=object)}
    )
```
