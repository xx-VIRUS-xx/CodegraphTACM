# pandas-14 :: tacm

query: BUG: DataFrame[object] + Series[dt64], test parametrization (#33824)

## selected nodes

- rank=1 layer=FILE tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=2 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FILE tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=4 layer=FILE tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_tester.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_tester.py
- rank=5 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=6 layer=CLASS tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_astype.py::TestAstype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_astype.py
- rank=7 layer=CLASS tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_diff.py::TestSeriesDiff file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_diff.py
- rank=8 layer=CLASS tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/casting.py::BaseCastingTests file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/casting.py
- rank=9 layer=CLASS tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_empty.py::TestEmptyConcat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/concat/test_empty.py
- rank=10 layer=CLASS tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_comparisons.py::TestTimestampComparison file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
- rank=11 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py::unpack_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py
- rank=12 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=13 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=14 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py::skip_if_installed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py
- rank=15 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
- rank=16 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.time_add_np_dt64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py
- rank=17 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::downsample_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py
- rank=18 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::resample_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py
- rank=19 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=20 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::_check_where_equivalences file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=21 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::_reindex_for_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=22 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::box_with_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=23 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.__dataframe__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=24 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby._apply_pairwise file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=25 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.items file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=26 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/hashing.py::hash_pandas_object file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/hashing.py
- rank=27 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=28 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c::object_is_dataframe_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=29 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/test_format.py::gen_series_formatting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/test_format.py
- rank=30 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.combine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=31 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c::object_is_series_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/ujson.c
- rank=32 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.join file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=33 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py::_validate_dt64_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimes.py
- rank=34 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.dt64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
- rank=35 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._gotitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=36 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py::data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_arithmetic.py
- rank=37 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::_test_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py
- rank=38 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py::bday_to_datetime file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/converter.py
- rank=39 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/moments/conftest.py::all_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/moments/conftest.py
- rank=40 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__add__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=41 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._convert_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=42 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.to_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=43 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/indexing.py::GroupByNthSelector.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/indexing.py
- rank=44 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::TestSetitemNADatetimeLikeDtype.is_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=45 layer=FUNCTION tokens=39 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py::array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/construction.py
- rank=46 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._constructor_sliced_from_mgr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=47 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/formats/style/test_to_latex.py
- rank=48 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py::SparseSeriesToFrame.time_series_to_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/sparse.py

## context

```text
file vendored/ujson/python/ujson.c
imports: Python, numpy
defines: modulestate, PyModuleDef, object_is_decimal_type, object_is_dataframe_type, object_is_series_type, object_is_index_type, object_is_nat_type, object_is_na_type, object_is_decimal_type, object_is_dataframe_type, object_is_series_type, object_is_index_type, object_is_nat_type, object_is_na_type, module_traverse, module_clear, module_free, PyInit__ujson

file pandas/core/frame.py
imports: __future__, collections, functools, io, itertools, operator, sys, typing
defines: DataFrame, _from_nested_dict, _reindex_for_setitem

file pandas/core/series.py
imports: __future__, collections, functools, operator, sys, typing, warnings, numpy
defines: Series

file pandas/util/_tester.py
imports: __future__, os, sys, pandas
defines: test

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class TestAstype:  [series/methods/test_astype.py:111]
methods: test_astype, test_astype_bytes
         test_astype_cast_nan_inf_int
         test_astype_cast_object_int
         test_astype_cast_object_int_fail
         test_astype_datetime, test_astype_datetime64tz
         test_astype_dt64_to_str
         test_astype_dt64tz_to_str
         test_astype_ea_to_datetimetzdtype
         test_astype_empty_constructor_equality
         test_astype_float_to_period
         test_astype_float_to_uint_negatives_raise
         test_astype_from_float_to_str
         test_astype_generic_timestamp_no_frequency
         test_astype_ignores_errors_for_extension_dtypes
         test_astype_mixed_object_to_dt64tz
         test_astype_nan_to_bool
         test_astype_no_pandas_dtype
         test_astype_object_to_dt64_non_nano
         test_astype_retain_attrs
         test_astype_str_cast_dt64
         test_astype_str_cast_td64, test_astype_str_map
         test_astype_to_str_preserves_na
         test_astype_unicode
         test_dt64_series_astype_object
         test_td64_series_astype_object

class TestSeriesDiff:  [series/methods/test_diff.py:12]
methods: test_diff_bool, test_diff_dt64, test_diff_dt64tz
         test_diff_int, test_diff_np
         test_diff_object_dtype
         test_diff_series_requires_integer, test_diff_tz

class BaseCastingTests:  [extension/base/casting.py:11]
methods: as_str, test_astype_empty_dataframe
         test_astype_object_frame
         test_astype_object_series, test_astype_own_type
         test_astype_str, test_astype_string
         test_to_numpy, test_tolist

class TestEmptyConcat:  [reshape/concat/test_empty.py:15]
methods: float_result_type, get_result_type, int_result_type
         test_concat_empty_dataframe
         test_concat_empty_dataframe_different_dtypes
         test_concat_empty_dataframe_dtypes
         test_concat_empty_df_object_dtype
         test_concat_empty_series
         test_concat_empty_series_dtype_category_with_array
         test_concat_empty_series_dtypes
         test_concat_empty_series_dtypes_match_roundtrips
         test_concat_empty_series_dtypes_roundtrips
         test_concat_empty_series_dtypes_sparse
         test_concat_empty_series_dtypes_triple
         test_concat_empty_series_timelike
         test_concat_inner_join_empty
         test_concat_to_empty_ea, test_empty_dtype_coerce
         test_handle_empty_objects

class TestTimestampComparison:  [scalar/timestamp/test_comparisons.py:14]
methods: test_cant_compare_tz_naive_w_aware, test_compare_date
         test_compare_invalid, test_compare_non_nano_dt64
         test_compare_zerodim_array, test_comparison
         test_comparison_dt64_ndarray
         test_comparison_dt64_ndarray_tzaware
         test_comparison_object_array
         test_timestamp_compare_oob_dt64
         test_timestamp_compare_scalars
         test_timestamp_compare_with_early_datetime

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

    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

    # ... truncated

    def len(self):
        """
        Compute the length of each element in the Series/Index.

        The element may be a sequence (such as a string, tuple or list) or a collection
        (such as a dictionary).

        Returns
        -------
        Series or Index of int
            A Series or Index of integer values indicating the length of each
            element in the Series or Index.
    # ... truncated

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

    def ts(self, dt64):
        return Timestamp._from_dt64(dt64)

    def time_add_np_dt64(self, offset):
        offset + self.dt64

def downsample_method(request):
    """Fixture for parametrization of Grouper downsample methods."""
    return request.param

def resample_method(request):
    """Fixture for parametrization of Grouper resample methods."""
    return request.param

def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

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

def _reindex_for_setitem(
    value: DataFrame | Series, index: Index
) -> tuple[ArrayLike, BlockValuesRefs | None]:
    # reindex if necessary

    if value.index.equals(index) or not len(index):
        if isinstance(value, Series):
            return value._values, value._references
        return value._values.copy(), None

    # GH#4107
    try:
        reindexed_value = value.reindex(index)._values
    except ValueError as err:
        # raised in MultiIndex.from_tuples, see test_insert_error_msmgs
        if not value.index.is_unique:
            # duplicate axis
            raise err

        raise TypeError(
            "incompatible index of inserted column with frame index"
        ) from err
    return reindexed_value, None

def box_with_array(request):
    """
    Fixture to test behavior for Index, Series, DataFrame, and pandas Array
    classes
    """
    return request.param

    def __dataframe__(self, nan_as_null: bool = False, allow_copy: bool = True):
        """Construct a new interchange object, potentially changing the parameters."""

    def _apply_pairwise(
        self,
        target: DataFrame | Series,
        other: DataFrame | Series | None,
        pairwise: bool | None,
        func: Callable[[DataFrame | Series, DataFrame | Series], DataFrame | Series],
        numeric_only: bool,
    ) -> DataFrame | Series:
        """
    # ... truncated

    def items(self) -> Iterable[tuple[Hashable, Series]]:
        r"""
        Iterate over (column name, Series) pairs.

        Iterates over the DataFrame columns, returning a tuple with
        the column name and the content as a Series.

        Yields
        ------
        label : object
            The column names for the DataFrame being iterated over.
        content : Series
    # ... truncated

def hash_pandas_object(
    obj: Index | DataFrame | Series,
    index: bool = True,
    encoding: str = "utf8",
    hash_key: str | None = _default_hash_key,
    categorize: bool = True,
) -> Series:
    """
    # ... truncated

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

int object_is_dataframe_type(PyObject *obj) {
  PyObject *module = PyImport_ImportModule("pandas");
  if (module == NULL) {
    PyErr_Clear();
    return 0;
  }
  PyObject *type_dataframe = PyObject_GetAttrString(module, "DataFrame");
  if (type_dataframe == NULL) {
    Py_DECREF(module);
    PyErr_Clear();
    return 0;
  }
  int result = PyObject_IsInstance(obj, type_dataframe);
  if (result == -1) {
    Py_DECREF(module);
    Py_DECREF(type_dataframe);
    PyErr_Clear();
    return 0;
  }
  return result;
}

def gen_series_formatting():
    s1 = Series(["a"] * 100)
    s2 = Series(["ab"] * 100)
    s3 = Series(["a", "ab", "abc", "abcd", "abcde", "abcdef"])
    s4 = s3[::-1]
    test_sers = {"onel": s1, "twol": s2, "asc": s3, "desc": s4}
    return test_sers

    def combine(
        self,
        other: DataFrame,
        func: Callable[[Series, Series], Series | Hashable],
        fill_value=None,
        overwrite: bool = True,
    ) -> DataFrame:
        """
    # ... truncated

int object_is_series_type(PyObject *obj) {
  PyObject *module = PyImport_ImportModule("pandas");
  if (module == NULL) {
    PyErr_Clear();
    return 0;
  }
  PyObject *type_series = PyObject_GetAttrString(module, "Series");
  if (type_series == NULL) {
    Py_DECREF(module);
    PyErr_Clear();
    return 0;
  }
  int result = PyObject_IsInstance(obj, type_series);
  if (result == -1) {
    Py_DECREF(module);
    Py_DECREF(type_series);
    PyErr_Clear();
    return 0;
  }
  return result;
}

    def join(
        self,
        other: DataFrame | Series | Iterable[DataFrame | Series],
        on: IndexLabel | None = None,
        how: MergeHow = "left",
        lsuffix: str = "",
        rsuffix: str = "",
        sort: bool = False,
        validate: JoinValidate | None = None,
    ) -> DataFrame:
        """
    # ... truncated

def _validate_dt64_dtype(dtype):
    """
    Check that a dtype, if passed, represents either a numpy datetime64[ns]
    dtype or a pandas DatetimeTZDtype.

    Parameters
    ----------
    dtype : object

    Returns
    -------
    dtype : None, numpy.dtype, or DatetimeTZDtype
    # ... truncated

    def dt64(self, reso):
        # cases that are in-bounds for nanosecond, so we can compare against
        #  the existing implementation.
        return np.datetime64("2016-01-01", reso)

    def _gotitem(
        self,
        key: IndexLabel,
        ndim: int,
        subset: DataFrame | Series | None = None,
    ) -> DataFrame | Series:
        """
        Sub-classes to define. Return a sliced object.

        Parameters
        ----------
        key : string / list of selections
        ndim : {1, 2}
            requested ndim of result
        subset : object, default None
            subset to act on
        """
        if subset is None:
            subset = self
        elif subset.ndim == 1:  # is Series
            return subset

        return subset[key]

def data(request):
    """Fixture returning parametrized (array, scalar) tuple.

    Used to test equivalence of scalars, numpy arrays with array ops, and the
    equivalence of DataFrame and Series ops.
    """
    return request.param

def _test_series(dti):
    return Series(np.random.default_rng(2).random(len(dti)), dti)

def bday_to_datetime(ordinal: int) -> datetime:
    """Inverse of bday_count (replaces Period(ordinal=N, freq='B'))."""
    dt64 = np.busday_offset(np.datetime64("1970-01-01", "D"), ordinal)
    return dt64.astype("datetime64[us]").item()

def all_data(request):
    """
    Test:
        - Empty Series / DataFrame
        - All NaN
        - All consistent value
        - Monotonically decreasing
        - Monotonically increasing
        - Monotonically consistent with NaNs
        - Monotonically increasing with NaNs
        - Monotonically decreasing with NaNs
    """
    return request.param

    def __add__(self, other):
        """
        Get Addition of DataFrame and other, column-wise.

        Equivalent to ``DataFrame.add(other)``.

        Parameters
        ----------
        other : scalar, sequence, Series, dict or DataFrame
            Object to be added to the DataFrame.

        Returns
    # ... truncated

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

    def to_frame(self, name: Hashable = lib.no_default) -> DataFrame:
        """
        Convert Series to DataFrame.

        The resulting DataFrame contains a single column. The name of the
        column can be set using the ``name`` parameter; otherwise it
        defaults to the Series' name.

        Parameters
        ----------
        name : object, optional
            The passed name should substitute for the series name (if it has
    # ... truncated

    def __getitem__(self, n: PositionalIndexer | tuple) -> DataFrame | Series:
        return self.groupby_object._nth(n)

    def is_inplace(self, val, obj):
        # td64   -> cast to object iff val is datetime64("NaT")
        # dt64   -> cast to object iff val is timedelta64("NaT")
        # dt64tz -> cast to object with anything _but_ NaT
        return val is NaT or val is None or val is np.nan or obj.dtype == val.dtype

def array(
    data: Sequence[object] | AnyArrayLike,
    dtype: Dtype | None = None,
    copy: bool = True,
) -> ExtensionArray:
    """
    # ... truncated

    def _constructor_sliced_from_mgr(self, mgr, axes) -> Series:
        ser = Series._from_mgr(mgr, axes)
        # Use object.__setattr__ to bypass NDFrame.__setattr__ overhead
        object.__setattr__(ser, "_name", None)  # caller sets real name

        if type(self) is DataFrame:
            # This would also work `if self._constructor_sliced is Series`, but
            #  this check is slightly faster, benefiting the most-common case.
            return ser

        # We assume that the subclass __init__ knows how to handle a
        #  pd.Series object.
        return self._constructor_sliced(ser)

def df():
    return DataFrame(
        {"A": [0, 1], "B": [-0.61, -1.22], "C": Series(["ab", "cd"], dtype=object)}
    )

    def time_series_to_frame(self):
        pd.DataFrame(self.series)
```
