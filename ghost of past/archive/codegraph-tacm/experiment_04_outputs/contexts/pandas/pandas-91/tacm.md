# pandas-91 :: tacm

query: BUG: TimedeltaIndex.searchsorted accepting invalid types/dtypes (#30831)

## selected nodes

- rank=1 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=2 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=3 layer=FILE tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/_util.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/_util.py
- rank=4 layer=FILE tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py
- rank=5 layer=FILE tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/api/types/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/api/types/__init__.py
- rank=6 layer=FILE tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/__init__.py
- rank=7 layer=FILE tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/api.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/api.py
- rank=8 layer=FILE tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py
- rank=9 layer=CLASS tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_timedeltas.py::TestTimedeltaArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_timedeltas.py
- rank=10 layer=CLASS tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_searchsorted.py::TestSeriesSearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_searchsorted.py
- rank=11 layer=CLASS tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/numpy_/test_indexing.py::TestSearchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/numpy_/test_indexing.py
- rank=12 layer=CLASS tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_searchsorted.py::TestSearchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_searchsorted.py
- rank=13 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_searchsorted.py::TestSearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_searchsorted.py
- rank=14 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py::DtypesInvalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py
- rank=15 layer=CLASS tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_getitem.py::TestSeriesGetitemSlices file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_getitem.py
- rank=16 layer=CLASS tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=17 layer=CLASS tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=18 layer=CLASS tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py::Dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py
- rank=19 layer=CLASS tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_dtypes.py::TestCategoricalDtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_dtypes.py
- rank=20 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_dtypes.py::Base file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_dtypes.py
- rank=21 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=22 layer=CLASS tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=23 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py::CheckDtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py
- rank=24 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.has_invalid_return_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=25 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=26 layer=FUNCTION tokens=245 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py
- rank=27 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::find_common_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=28 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=29 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py::listlike_box file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py
- rank=30 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::make_invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=31 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.inferred_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=32 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::timedelta_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=33 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex._engine_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=34 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py::DtypesInvalid.time_pandas_dtype_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py
- rank=35 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=36 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.select_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=37 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex._resolution_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=38 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::_cast_to_stata_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=39 layer=FUNCTION tokens=299 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_delta_bins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=40 layer=FUNCTION tokens=226 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::invalid_comparison file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=41 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=42 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=43 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=44 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::numeric_idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py
- rank=45 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py::IndexOpsMixin.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py
- rank=46 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.operand_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=47 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=48 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=49 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=50 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataWriter._set_formats_and_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=51 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py
- rank=52 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=53 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py
- rank=54 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=55 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py
- rank=56 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._needs_i8_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=57 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::timedelta_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=58 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=59 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex._is_comparable_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py

## context

```text
file core/ops/invalid.py
imports: __future__, operator, typing, numpy, collections, pandas
defines: invalid_comparison, make_invalid_op, invalid_op

file core/indexes/timedeltas.py
imports: __future__, typing, pandas
defines: TimedeltaIndex, timedelta_range

file pandas/io/_util.py
imports: __future__, typing, numpy, pandas, collections, pyarrow
defines: _arrow_dtype_mapping, _arrow_string_types_mapper, arrow_table_to_pandas, _post_convert_dtypes

file asv_bench/benchmarks/dtypes.py
imports: string, numpy, pandas, pandas_vb_common
defines: Dtypes, DtypesInvalid, SelectDtypes, CheckDtypes

file api/types/__init__.py
imports: pandas
defines: —

file core/dtypes/__init__.py
imports: —
defines: —

file core/dtypes/api.py
imports: pandas
defines: —

file io/sas/sas_constants.py
imports: __future__, typing
defines: SASIndex

class TestTimedeltaArray:  [tests/arrays/test_timedeltas.py:196]
methods: test_astype_int, test_searchsorted_invalid_types
         test_setitem_clears_freq, test_setitem_objects

class TestSeriesSearchSorted:  [series/methods/test_searchsorted.py:14]
methods: test_searchsorted, test_searchsorted_dataframe_fail
         test_searchsorted_datetime64_list
         test_searchsorted_datetime64_scalar
         test_searchsorted_datetime64_scalar_mixed_timezones
         test_searchsorted_numeric_dtypes_scalar
         test_searchsorted_numeric_dtypes_vector
         test_searchsorted_sorter

class TestSearchsorted:  [arrays/numpy_/test_indexing.py:9]
methods: test_searchsorted_numeric_dtypes_scalar
         test_searchsorted_numeric_dtypes_vector
         test_searchsorted_sorter, test_searchsorted_string

class TestSearchsorted:  [indexes/period/test_searchsorted.py:14]
methods: test_searchsorted
         test_searchsorted_different_argument_classes
         test_searchsorted_invalid

class TestSearchSorted:  [indexes/timedeltas/test_searchsorted.py:11]
methods: test_searchsorted_different_argument_classes
         test_searchsorted_invalid_argument_dtype

class DtypesInvalid:  [asv_bench/benchmarks/dtypes.py:37]
methods: time_pandas_dtype_invalid

class TestSeriesGetitemSlices:  [series/indexing/test_getitem.py:224]
methods: test_getitem_median_slice_bug
         test_getitem_partial_str_slice_high_reso_with_timedeltaindex
         test_getitem_partial_str_slice_with_datetimeindex
         test_getitem_partial_str_slice_with_timedeltaindex
         test_getitem_slice_2d, test_getitem_slice_bug
         test_getitem_slice_date
         test_getitem_slice_float_raises
         test_getitem_slice_integers
         test_getitem_slice_strings_with_datetimeindex

class TestMaybeCastSliceBound:  [indexes/timedeltas/test_indexing.py:288]
methods: monotonic, tdi, test_maybe_cast_slice_bound_invalid_str
         test_slice_invalid_str_with_timedeltaindex

class TimedeltaIndex(DatetimeTimedeltaMixin):  [core/indexes/timedeltas.py:75]
methods: _engine_type, _is_comparable_dtype, _parse_with_reso
         _parsed_string_to_bounds, _resolution_obj
         get_loc, inferred_type, __new__

class Dtypes:  [asv_bench/benchmarks/dtypes.py:29]
methods: time_pandas_dtype

class TestCategoricalDtypes:  [arrays/categorical/test_dtypes.py:19]
methods: test_categories_match_up_to_permutation, test_codes_dtypes
         test_interval_index_category
         test_iter_python_types
         test_iter_python_types_datetime
         test_set_dtype_many
         test_set_dtype_new_categories
         test_set_dtype_no_overlap, test_set_dtype_same

class Base:  [tests/dtypes/test_dtypes.py:45]
methods: test_equality_invalid, test_hash, test_numpy_informed
         test_pickle

class SearchSorted:  [asv_bench/benchmarks/series_methods.py:122]
methods: setup, time_searchsorted

class Op:  [core/computation/ops.py:213]
methods: has_invalid_return_type, is_datetime, is_scalar
         operand_types, return_type, __init__, __iter__
         __repr__

class CheckDtypes:  [asv_bench/benchmarks/dtypes.py:117]
methods: setup, time_is_extension_array_dtype_false
         time_is_extension_array_dtype_true

    def has_invalid_return_type(self) -> bool:
        types = self.operand_types
        obj_dtype_set = frozenset([np.dtype("object")])
        return self.return_type == object and types - obj_dtype_set

    def time_searchsorted(self, dtype):
        key = "2" if dtype == "str" else 2
        self.s.searchsorted(key)

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

def find_common_type(types: list[DtypeObj]) -> DtypeObj:  # type: ignore[misc]
    """
    Find a common data type among the given dtypes.

    Parameters
    ----------
    types : list of dtypes

    Returns
    -------
    pandas extension or numpy dtype

    # ... truncated

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

def listlike_box(request):
    """
    Types that may be passed as the indexer to searchsorted.
    """
    return request.param

def make_invalid_op(name: str) -> Callable[..., NoReturn]:
    """
    Return a binary method that always raises a TypeError.

    Parameters
    ----------
    name : str

    Returns
    -------
    invalid_op : function
    """

    def invalid_op(self: object, other: object = None) -> NoReturn:
        typ = type(self).__name__
        raise TypeError(f"cannot perform {name} with this index type: {typ}")

    invalid_op.__name__ = name
    return invalid_op

    def inferred_type(self) -> str:
        return "timedelta64"

def timedelta_range(
    start=None,
    end=None,
    periods: int | None = None,
    freq=None,
    name=None,
    closed=None,
    *,
    unit: TimeUnit | None = None,
) -> TimedeltaIndex:
    """
    # ... truncated

    def _engine_type(self) -> type[libindex.TimedeltaEngine]:
        return libindex.TimedeltaEngine

    def time_pandas_dtype_invalid(self, dtype):
        try:
            pandas_dtype(self.data_dict[dtype])
        except TypeError:
            pass

    def setup(self, dtype):
        N = 10**5
        data = np.array([1] * N + [2] * N + [3] * N).astype(dtype)
        self.s = Series(data)

    def select_dtypes(self, include=None, exclude=None) -> DataFrame:
        """
        Return a subset of the DataFrame's columns based on the column dtypes.

        This method allows for filtering columns based on their data types.
        It is useful when working with heterogeneous DataFrames where operations
        need to be performed on a specific subset of data types.

        Parameters
        ----------
        include, exclude : scalar or list-like
            A selection of dtypes or strings to be included/excluded. At least
    # ... truncated

    def _resolution_obj(self) -> Resolution | None:  # type: ignore[override]
        return self._data._resolution_obj

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
    # ... truncated

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

def invalid_comparison(
    left: ArrayLike,
    right: ArrayLike | list | range | Scalar,
    op: Callable[[Any, Any], bool],
) -> npt.NDArray[np.bool_]:
    """
    If a comparison has mismatched types and is not necessarily meaningful,
    follow python3 conventions by:

        - returning all-False for equality
        - returning all-True for inequality
        - raising TypeError otherwise

    Parameters
    ----------
    left : array-like
    right : scalar, array-like
    op : operator.{eq, ne, lt, le, gt}

    Raises
    ------
    TypeError : on inequality comparisons
    """
    if op is operator.eq:
        res_values = np.zeros(left.shape, dtype=bool)
    elif op is operator.ne:
        res_values = np.ones(left.shape, dtype=bool)
    else:
        typ = type(right).__name__
        raise TypeError(f"Invalid comparison between dtype={left.dtype} and {typ}")
    return res_values

    def __new__(
        cls,
        data=None,
        freq=lib.no_default,
        dtype=None,
        copy: bool | None = None,
        name=None,
    ):
        name = maybe_extract_name(name, data, cls)

        # GH#63388
        data, copy = cls._maybe_copy_array_input(data, copy, dtype)
    # ... truncated

    def time_categorical_contains(self):
        self.c.searchsorted(self.key)

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

def numeric_idx(request):
    """
    Several types of numeric-dtypes Index objects
    """
    return request.param

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def operand_types(self):
        return frozenset(term.type for term in com.flatten(self))

    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def _set_formats_and_types(self, dtypes: Series) -> None:
        self.fmtlist: list[str] = []
        self.typlist: list[int] = []
        for col, dtype in dtypes.items():
            self.fmtlist.append(_dtype_to_default_stata_fmt(dtype, self.data[col]))
            self.typlist.append(_dtype_to_stata_type(dtype, self.data[col]))

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def searchsorted(
        self,
        v: ArrayLike | object,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        if config["mode"]["performance_warnings"]:
            msg = "searchsorted requires high memory usage."
            warnings.warn(msg, PerformanceWarning, stacklevel=find_stack_level())
        v = np.asarray(v)
        return np.asarray(self, dtype=self.dtype.subtype).searchsorted(v, side, sorter)

    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

    def searchsorted(  # type: ignore[override]
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        """
    # ... truncated

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

def timedelta_index():
    """
    A fixture to provide TimedeltaIndex objects with different frequencies.
     Most TimedeltaArray behavior is already tested in TimedeltaIndex tests,
    so here we just test that the TimedeltaArray behavior matches
    the TimedeltaIndex behavior.
    """
    # TODO: flesh this out
    return TimedeltaIndex(["1 Day", "3 Hours", "NaT"])

    def invalid_op(self: object, other: object = None) -> NoReturn:
        typ = type(self).__name__
        raise TypeError(f"cannot perform {name} with this index type: {typ}")

    def _is_comparable_dtype(self, dtype: DtypeObj) -> bool:
        """
        Can we compare values of the given dtype to our own?
        """
        if isinstance(dtype, ArrowDtype):
            return dtype.kind == "m"
        return lib.is_np_dtype(dtype, "m")  # aka self._data._is_recognized_dtype
```
