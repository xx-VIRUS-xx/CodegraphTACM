# pandas-14 :: hybrid-cs

query: BUG: DataFrame[object] + Series[dt64], test parametrization (#33824)

## selected nodes

- rank=1 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_string.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_string.py
- rank=2 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_typst.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_typst.py
- rank=3 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py
- rank=4 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py::unpack_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py
- rank=5 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_join.py::TestJoin.df2 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_join.py
- rank=6 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMerge.df2 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=7 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterBegin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=8 layer=FUNCTION tokens=304 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_numeric_only.py::TestNumericOnly.df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_numeric_only.py
- rank=9 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::tsframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py
- rank=10 layer=FUNCTION tokens=219 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/transform/test_transform.py::frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/transform/test_transform.py
- rank=11 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py::series_via_frame_from_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py
- rank=12 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/excel.py::_generate_dataframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/excel.py
- rank=13 layer=FUNCTION tokens=255 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::_check_where_equivalences file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=14 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py::skip_if_installed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py
- rank=15 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_fsspec.py::df1 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_fsspec.py
- rank=16 layer=FUNCTION tokens=418 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py::skip_if_no file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py
- rank=17 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py::_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py
- rank=18 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Concat.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=19 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/moments/conftest.py::create_dataframes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/moments/conftest.py
- rank=20 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::dtype_backend_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=21 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py::_frame2 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py
- rank=22 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::downsample_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py
- rank=23 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
- rank=24 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterEnd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=25 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::resample_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py
- rank=26 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=27 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.time_add_np_dt64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py
- rank=28 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.__dataframe__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py
- rank=29 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py::FromScalar.time_frame_from_scalar_ea_float64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py
- rank=30 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py::ParallelReadCSV.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py
- rank=31 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser._parse file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_string.py::df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_string.py]
def df():
    return DataFrame(
        {"A": [0, 1], "B": [-0.61, -1.22], "C": Series(["ab", "cd"], dtype=object)}
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_typst.py::df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_typst.py]
def df():
    return DataFrame(
        {"A": [0, 1], "B": [-0.61, -1.22], "C": Series(["ab", "cd"], dtype=object)}
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py::df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py]
def df():
    return DataFrame(
        {"A": [0, 1], "B": [-0.61, -1.22], "C": Series(["ab", "cd"], dtype=object)}
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_join.py::TestJoin.df2 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_join.py]
    def df2(self):
        return DataFrame(
            {
                "key1": get_test_data(n=10),
                "key2": get_test_data(ngroups=4, n=10),
                "value": np.random.default_rng(2).standard_normal(10),
            }
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMerge.df2 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py]
    def df2(self):
        return DataFrame(
            {
                "key1": get_test_data(n=10),
                "key2": get_test_data(ngroups=4, n=10),
                "value": np.random.default_rng(2).standard_normal(10),
            }
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterBegin [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void DataFrame_iterBegin(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  PyObjectEncoder *enc = (PyObjectEncoder *)tc->encoder;
  GET_TC(tc)->index = 0;
  enc->outputFormat = VALUES; // for contained series & index
  GET_TC(tc)->cStr = PyObject_Malloc(CSTR_SIZE);
  if (!GET_TC(tc)->cStr) {
    PyErr_NoMemory();
  }
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_numeric_only.py::TestNumericOnly.df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_numeric_only.py]
    def df(self):
        # GH3668
        # GH5724
        df = DataFrame(
            {
                "group": [1, 1, 2],
                "int": [1, 2, 3],
                "float": [4.0, 5.0, 6.0],
                "string": Series(["a", "b", "c"], dtype="str"),
                "object": Series(["a", "b", "c"], dtype=object),
                "category_string": Series(list("abc")).astype("category"),
                "category_int": [7, 8, 9],
                "datetime": date_range("20130101", periods=3),
                "datetimetz": date_range("20130101", periods=3, tz="US/Eastern"),
                "timedelta": pd.timedelta_range("1 s", periods=3, freq="s"),
            },
            columns=[
                "group",
                "int",
                "float",
                "string",
                "object",
                "category_string",
                "category_int",
                "datetime",
                "datetimetz",
                "timedelta",
            ],
        )
        return df

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::tsframe [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py]
def tsframe():
    return DataFrame(
        np.random.default_rng(2).standard_normal((30, 4)),
        columns=Index(list("ABCD"), dtype=object),
        index=date_range("2000-01-01", periods=30, freq="B"),
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/transform/test_transform.py::frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/transform/test_transform.py]
def frame():
    floating = Series(np.random.default_rng(2).standard_normal(10))
    floating_missing = floating.copy()
    floating_missing.iloc[2:7] = np.nan
    strings = list("abcde") * 2
    strings_missing = strings[:]
    strings_missing[5] = np.nan

    df = DataFrame(
        {
            "float": floating,
            "float_missing": floating_missing,
            "int": [1, 1, 1, 1, 2] * 2,
            "datetime": date_range("1990-1-1", periods=10),
            "timedelta": pd.timedelta_range(1, freq="s", periods=10),
            "string": strings,
            "string_missing": strings_missing,
            "cat": Categorical(strings),
        },
    )
    return df

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py::series_via_frame_from_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/base/test_constructors.py]
def series_via_frame_from_scalar(x, **kwargs):
    return DataFrame(x, **kwargs)[0]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/excel.py::_generate_dataframe [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/excel.py]
def _generate_dataframe():
    N = 2000
    C = 5
    df = DataFrame(
        np.random.randn(N, C),
        columns=[f"float{i}" for i in range(C)],
        index=date_range("20000101", periods=N, freq="h"),
    )
    df["object"] = Index([f"i-{i}" for i in range(N)], dtype=object)
    return df

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py::skip_if_installed [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py]
def skip_if_installed(package: str) -> pytest.MarkDecorator:
    """
    Skip a test if a package is installed.

    Parameters
    ----------
    package : str
        The name of the package.

    Returns
    -------
    pytest.MarkDecorator
        a pytest.mark.skipif to use as either a test decorator or a
        parametrization mark.
    """
    return pytest.mark.skipif(
        bool(import_optional_dependency(package, errors="ignore")),
        reason=f"Skipping because {package} is installed.",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_fsspec.py::df1 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_fsspec.py]
def df1():
    return DataFrame(
        {
            "int": [1, 3],
            "float": [2.0, np.nan],
            "str": ["t", "s"],
            "dt": date_range("2018-06-18", periods=2),
        }
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py::skip_if_no [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py]
def skip_if_no(package: str, min_version: str | None = None) -> pytest.MarkDecorator:
    """
    Generic function to help skip tests when required packages are not
    present on the testing system.

    This function returns a pytest mark with a skip condition that will be
    evaluated during test collection. An attempt will be made to import the
    specified ``package`` and optionally ensure it meets the ``min_version``

    The mark can be used as either a decorator for a test class or to be
    applied to parameters in pytest.mark.parametrize calls or parametrized
    fixtures. Use pytest.importorskip if an imported module is later needed
    or for test functions.

    If the import and version check are unsuccessful, then the test function
    (or test case when used in conjunction with parametrization) will be
    skipped.

    Parameters
    ----------
    package: str
        The name of the required package.
    min_version: str or None, default None
        Optional minimum version of the package.

    Returns
    -------
    pytest.MarkDecorator
        a pytest.mark.skipif to use as either a test decorator or a
        parametrization mark.
    """
    msg = f"Could not import '{package}'"
    if min_version:
        msg += f" satisfying a min_version of {min_version}"
    return pytest.mark.skipif(
        not bool(
            import_optional_dependency(
                package, errors="ignore", min_version=min_version
            )
        ),
        reason=msg,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py::_frame [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py]
def _frame():
    return DataFrame(
        np.random.default_rng(2).standard_normal((10001, 4)),
        columns=list("ABCD"),
        dtype="float64",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Concat.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def setup(self, axis):
        N = 1000
        s = Series(N, index=Index([f"i-{i}" for i in range(N)], dtype=object))
        self.series = [s[i:-i] for i in range(1, 10)] * 50
        self.small_frames = [DataFrame(np.random.randn(5, 4))] * 1000
        df = DataFrame(
            {"A": range(N)}, index=date_range("20130101", periods=N, freq="s")
        )
        self.empty_left = [DataFrame(), df]
        self.empty_right = [df, DataFrame()]
        self.mixed_ndims = [df, df.head(N // 2)]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/moments/conftest.py::create_dataframes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/moments/conftest.py]
def create_dataframes():
    return [
        DataFrame(columns=["a", "a"]),
        DataFrame(np.arange(15).reshape((5, 3)), columns=["a", "a", 99]),
    ] + [DataFrame(s) for s in create_series()]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::dtype_backend_data [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py]
def dtype_backend_data() -> DataFrame:
    return DataFrame(
        {
            "a": Series([1, pd.NA, 3], dtype="Int64"),
            "b": Series([1, 2, 3], dtype="Int64"),
            "c": Series([1.5, pd.NA, 2.5], dtype="Float64"),
            "d": Series([1.5, 2.0, 2.5], dtype="Float64"),
            "e": [True, False, None],
            "f": [True, False, True],
            "g": ["a", "b", "c"],
            "h": ["a", "b", None],
        }
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py::_frame2 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_expressions.py]
def _frame2():
    return DataFrame(
        np.random.default_rng(2).standard_normal((100, 4)),
        columns=list("ABCD"),
        dtype="float64",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::downsample_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py]
def downsample_method(request):
    """Fixture for parametrization of Grouper downsample methods."""
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py]
    def ts(self, dt64):
        return Timestamp._from_dt64(dt64)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::DataFrame_iterEnd [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void DataFrame_iterEnd(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  PyObjectEncoder *enc = (PyObjectEncoder *)tc->encoder;
  enc->outputFormat = enc->originalOutputFormat;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::resample_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py]
def resample_method(request):
    """Fixture for parametrization of Grouper resample methods."""
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.time_add_np_dt64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py]
    def time_add_np_dt64(self, offset):
        offset + self.dt64

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.__dataframe__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py]
    def __dataframe__(
        self, nan_as_null: bool = False, allow_copy: bool = True
    ) -> PandasDataFrameXchg:
        # `nan_as_null` can be removed here once it's removed from
        # Dataframe.__dataframe__
        return PandasDataFrameXchg(self._df, allow_copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py::FromScalar.time_frame_from_scalar_ea_float64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_ctor.py]
    def time_frame_from_scalar_ea_float64(self):
        DataFrame(
            1.0,
            index=range(self.nrows),
            columns=list("abc"),
            dtype=Float64Dtype(),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py::ParallelReadCSV.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py]
    def setup(self, dtype):
        rows = 10000
        cols = 50
        if dtype == "float":
            df = DataFrame(np.random.randn(rows, cols))
        elif dtype == "datetime":
            df = DataFrame(
                np.random.randn(rows, cols), index=date_range("1/1/2000", periods=rows)
            )
        elif dtype == "object":
            df = DataFrame(
                "foo", index=range(rows), columns=["object%03d" for _ in range(5)]
            )
        else:
            raise NotImplementedError

        self.fname = f"__test_{dtype}__.csv"
        df.to_csv(self.fname)

        @run_parallel(num_threads=2)
        def parallel_read_csv():
            read_csv(self.fname)

        self.parallel_read_csv = parallel_read_csv

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser._parse [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py]
    def _parse(self) -> DataFrame | Series:
        raise AbstractMethodError(self)
```
