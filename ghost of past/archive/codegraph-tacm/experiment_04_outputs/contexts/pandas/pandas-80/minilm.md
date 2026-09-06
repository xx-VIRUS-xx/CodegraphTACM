# pandas-80 :: minilm

query: BUG: Series/Frame invert dtypes (#31183)

## selected nodes

- rank=1 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsIn.time_isin_mismatched_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py
- rank=2 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py::TestGeneric.f file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py
- rank=3 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes.time_frame_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=4 layer=FUNCTION tokens=232 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/arrow_parser_wrapper.py::ArrowParserWrapper._finalize_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/arrow_parser_wrapper.py
- rank=5 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=6 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericDtype._get_dtype_mapping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py
- rank=7 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=8 layer=FUNCTION tokens=457 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::maybe_convert_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=9 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py::IndexOpsMixin.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py
- rank=10 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py
- rank=11 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=12 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_formats.py::ExtTypeStub.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_formats.py
- rank=13 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py
- rank=14 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py::Construction.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/strings.py
- rank=15 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._validate_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=16 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_na_ok_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py
- rank=17 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=18 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/array.py::DecimalArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/array.py
- rank=19 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py::DummyArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py
- rank=20 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.convert_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=21 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py::MockNumpyLikeArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py
- rank=22 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py
- rank=23 layer=FUNCTION tokens=222 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=24 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataWriter117._set_formats_and_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=25 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=26 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsinWithArangeSorted.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py
- rank=27 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_common.py::DummyArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_common.py
- rank=28 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py
- rank=29 layer=FUNCTION tokens=229 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=30 layer=FUNCTION tokens=289 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray._from_scalars file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=31 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py
- rank=32 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py::_BaseInfo.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py
- rank=33 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::assert_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=34 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_dtypes.py::TestPeriodDtype.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_dtypes.py
- rank=35 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::disallow.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py
- rank=36 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_boolean_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=37 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsIn.time_isin_mismatched_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py]
    def time_isin_mismatched_dtype(self, dtype):
        self.series.isin(self.mismatched)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py::TestGeneric.f [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/generic/test_generic.py]
        def f(dtype):
            return construct(frame_or_series, shape=3, value=1, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes.time_frame_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_frame_dtypes(self):
        self.df.dtypes

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/arrow_parser_wrapper.py::ArrowParserWrapper._finalize_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/arrow_parser_wrapper.py]
    def _finalize_dtype(self, frame: DataFrame) -> DataFrame:
        if self.dtype is not None:
            # Ignore non-existent columns from dtype mapping
            # like other parsers do
            if isinstance(self.dtype, dict):
                self.dtype = {
                    k: pandas_dtype(v)
                    for k, v in self.dtype.items()
                    if k in frame.columns
                }
            else:
                self.dtype = pandas_dtype(self.dtype)
            try:
                frame = frame.astype(self.dtype)
            except TypeError as err:
                # GH#44901 reraise to keep api consistent
                raise ValueError(str(err)) from err
        return frame

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def dtype(self) -> PeriodDtype:
        return self._dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericDtype._get_dtype_mapping [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py]
    def _get_dtype_mapping(cls) -> Mapping[np.dtype, NumericDtype]:
        raise AbstractMethodError(cls)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py::IndexOpsMixin.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py]
    def dtype(self) -> DtypeObj:
        # must be defined here as a property for mypy
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py]
    def dtype(self) -> NumericDtype:
        mapping = self._dtype_cls._get_dtype_mapping()
        return mapping[self._data.dtype]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py]
    def dtype(self) -> BaseMaskedDtype:
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_formats.py::ExtTypeStub.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/test_formats.py]
            def dtype(self):
                return DtypeStub()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py]
    def dtype(self) -> NumpyEADtype:
        return self._dtype

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._validate_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _validate_dtype(cls, values, dtype):
        raise AbstractMethodError(cls)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_na_ok_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py]
def _na_ok_dtype(dtype: DtypeObj) -> bool:
    if needs_i8_conversion(dtype):
        return False
    return not issubclass(dtype.type, np.integer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def dtype(self) -> DtypeObj:
        return self._block.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/array.py::DecimalArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/array.py]
    def dtype(self):
        return self._dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py::DummyArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_select_dtypes.py]
    def dtype(self):
        return self._dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BaseBlockManager.convert_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def convert_dtypes(self, **kwargs):
        return self.apply("convert_dtypes", **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py::MockNumpyLikeArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_inference.py]
    def dtype(self):
        return self._values.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py]
def data(dtype):
    return PeriodArray(np.arange(1970, 1980), dtype=dtype)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataWriter117._set_formats_and_types [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py]
    def _set_formats_and_types(self, dtypes: Series) -> None:
        self.typlist = []
        self.fmtlist = []
        for col, dtype in dtypes.items():
            force_strl = col in self._convert_strl
            fmt = _dtype_to_default_stata_fmt(
                dtype,
                self.data[col],
                dta_version=self._dta_version,
                force_strl=force_strl,
            )
            self.fmtlist.append(fmt)
            self.typlist.append(
                _dtype_to_stata_type_117(dtype, self.data[col], force_strl)
            )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def dtype(self) -> DtypeObj:
        return self.values.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py::IsinWithArangeSorted.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/algos/isin.py]
    def setup(self, dtype, size):
        self.series = Series(np.arange(size)).astype(dtype)
        self.values = np.arange(size).astype(dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_common.py::DummyArray.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_common.py]
    def dtype(self):
        return DummyDtype()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py::array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py]
    def array(self, dtype=None):
        raise ValueError("I cannot be converted.")

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray._from_scalars [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def _from_scalars(cls, scalars, *, dtype: DtypeObj) -> Self:
        """
        Strict analogue to _from_sequence, allowing only sequences of scalars
        that should be specifically inferred to the given dtype.

        Parameters
        ----------
        scalars : sequence
        dtype : ExtensionDtype

        Raises
        ------
        TypeError or ValueError

        Notes
        -----
        This is called in a try/except block when casting the result of a
        pointwise operation in ExtensionArray._cast_pointwise_result.
        """
        try:
            return cls._from_sequence(scalars, dtype=dtype, copy=False)
        except (ValueError, TypeError):
            raise
        except Exception:
            warnings.warn(
                "_from_scalars should only raise ValueError or TypeError. "
                "Consider overriding _from_scalars where appropriate.",
                stacklevel=find_stack_level(),
            )
            raise

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::data_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py]
def data_missing(dtype):
    return PeriodArray([iNaT, 2017], dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py::_BaseInfo.dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/info.py]
    def dtypes(self) -> Iterable[Dtype]:
        """
        Dtypes.

        Returns
        -------
        dtypes : sequence
            Dtype of each of the DataFrame's columns (or one series column).
        """

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::assert_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py]
def assert_dtype(obj, expected_dtype):
    """
    Helper to check the dtype for a Series, Index, or single-column DataFrame.
    """
    dtype = tm.get_dtype(obj)

    assert dtype == expected_dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_dtypes.py::TestPeriodDtype.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_dtypes.py]
    def dtype(self):
        """
        Class level fixture of dtype for TestPeriodDtype
        """
        return PeriodDtype("D")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::disallow.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py]
    def __init__(self, *dtypes: Dtype) -> None:
        super().__init__()
        self.dtypes = tuple(pandas_dtype(dtype).type for dtype in dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_boolean_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def time_boolean_series(self, dtype):
        self.idx[self.series_mask]

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
```
