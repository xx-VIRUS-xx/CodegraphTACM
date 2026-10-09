# pandas-91 :: tacm-dyn-l4

query: BUG: TimedeltaIndex.searchsorted accepting invalid types/dtypes (#30831)

## selected nodes

- rank=1 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=2 layer=CLASS tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_timedeltas.py::TestTimedeltaArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_timedeltas.py
- rank=3 layer=FUNCTION tokens=245 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py
- rank=4 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.has_invalid_return_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=5 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::find_common_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=6 layer=CLASS tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_searchsorted.py::TestSeriesSearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/methods/test_searchsorted.py
- rank=7 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::types_data_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=8 layer=CLASS tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/numpy_/test_indexing.py::TestSearchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/numpy_/test_indexing.py
- rank=9 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py::listlike_box file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py
- rank=10 layer=CLASS tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_searchsorted.py::TestSearchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_searchsorted.py
- rank=11 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::make_invalid_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=12 layer=CLASS tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_searchsorted.py::TestSearchSorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_searchsorted.py
- rank=13 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=14 layer=CLASS tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_getitem.py::TestSeriesGetitemSlices file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_getitem.py
- rank=15 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.select_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=16 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::_cast_to_stata_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=17 layer=CLASS tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=18 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=19 layer=FUNCTION tokens=206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.check_int_infer_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=20 layer=FUNCTION tokens=299 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::TimeGrouper._get_time_delta_bins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=21 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=22 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::timedelta_range file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=23 layer=FUNCTION tokens=226 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py::invalid_comparison file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/invalid.py
- rank=24 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=25 layer=CLASS tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=26 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex.inferred_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=27 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=28 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::numeric_idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py
- rank=29 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py::IndexOpsMixin.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/base.py
- rank=30 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=31 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex._engine_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=32 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=33 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=34 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataWriter._set_formats_and_types file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=35 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py
- rank=36 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=37 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py
- rank=38 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=39 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py::timedelta_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimelike.py
- rank=40 layer=FUNCTION tokens=13 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Dtypes.time_frame_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py

## context

```text
file core/ops/invalid.py
imports: __future__, operator, typing, numpy, collections, pandas
defines: invalid_comparison, make_invalid_op, invalid_op

class TestTimedeltaArray:  [tests/arrays/test_timedeltas.py:196]
methods: test_astype_int, test_searchsorted_invalid_types
         test_setitem_clears_freq, test_setitem_objects

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

    def has_invalid_return_type(self) -> bool:
        types = self.operand_types
        obj_dtype_set = frozenset([np.dtype("object")])
        return self.return_type == object and types - obj_dtype_set

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

class TestSeriesSearchSorted:  [series/methods/test_searchsorted.py:14]
methods: test_searchsorted, test_searchsorted_dataframe_fail
         test_searchsorted_datetime64_list
         test_searchsorted_datetime64_scalar
         test_searchsorted_datetime64_scalar_mixed_timezones
         test_searchsorted_numeric_dtypes_scalar
         test_searchsorted_numeric_dtypes_vector
         test_searchsorted_sorter

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

class TestSearchsorted:  [arrays/numpy_/test_indexing.py:9]
methods: test_searchsorted_numeric_dtypes_scalar
         test_searchsorted_numeric_dtypes_vector
         test_searchsorted_sorter, test_searchsorted_string

def listlike_box(request):
    """
    Types that may be passed as the indexer to searchsorted.
    """
    return request.param

class TestSearchsorted:  [indexes/period/test_searchsorted.py:14]
methods: test_searchsorted
         test_searchsorted_different_argument_classes
         test_searchsorted_invalid

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

class TestSearchSorted:  [indexes/timedeltas/test_searchsorted.py:11]
methods: test_searchsorted_different_argument_classes
         test_searchsorted_invalid_argument_dtype

    def time_searchsorted(self, dtype):
        key = "2" if dtype == "str" else 2
        self.s.searchsorted(key)

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

class TestMaybeCastSliceBound:  [indexes/timedeltas/test_indexing.py:288]
methods: monotonic, tdi, test_maybe_cast_slice_bound_invalid_str
         test_slice_invalid_str_with_timedeltaindex

class DataFrame(NDFrame, OpsMixin):  [pandas/core/frame.py:269]
methods: T, _align_for_op, _append_internal, _arith_method
         _arith_method_with_reindex, _arith_op
         _box_col_values, _can_fast_transpose, _cmp_method
         _combine_frame, _construct_result, _constructor
         _constructor_from_mgr
         _constructor_sliced_from_mgr, _dict_round
         _dispatch_frame_op, _ensure_valid_index
         _flex_arith_method, _flex_cmp_method
         _from_arrays, _get_agg_axis, _get_column_array
         _get_data, _get_item, _get_value
         _get_values_for_csv, _getitem_bool_array
         _getitem_multilevel, _gotitem, _info_repr
         _is_homogeneous_type, _iset_item, _iset_item_mgr
         _iset_not_inplace, _iter_column_arrays, _ixs
         _maybe_align_series_as_frame, _reduce
         _reduce_axis1, _reindex_multi
         _replace_columnwise, _repr_fits_horizontal_
         _repr_fits_vertical_, _repr_html_
         _sanitize_column, _series, _series_round
         _set_item, _set_item_frame_value, _set_item_mgr
         _set_value, _setitem_array, _setitem_frame
         _setitem_slice, _should_reindex_frame_op
         _to_dict_of_blocks, _values, add, aggregate, all
         all, all, all, any, any, any, any, apply, assign
         axes, blk_func, c, check_int_infer_dtype, combine
         combine_first, combiner, compare, corr, corrwith
         count, cov, create_index, cummax, cummin, cumprod
         cumsum, diff, dot, dot, dot, drop, drop, drop
         drop, drop_duplicates, drop_duplicates
         drop_duplicates, drop_duplicates, dropna, dropna
         dropna, dtype_predicate, duplicated, eq, eval
         eval, eval, explode, f, f, floordiv, from_arrow
         from_dict, from_records, func, ge, groupby, gt
         idxmax, idxmin, igetitem, infer, info, insert
         isetitem, isin, isin_, isna, isnull, items
         iterrows, itertuples, join, kurt, kurt, kurt
         kurt, le, lt, map, max, max, max, max
         maybe_reorder, mean, mean, mean, mean, median
         median, median, median, melt, memory_usage, merge
         min, min, min, min, mod, mode, mul, ne, nlargest
         notna, notnull, nsmallest, nunique, pivot
         pivot_table, pop, pow, predicate, prod, quantile
         quantile, quantile, quantile, query, query, query
         query, radd, reindex, rename, rename, rename
         rename, reorder_levels, reset_index, reset_index
         reset_index, reset_index, rfloordiv, rmod, rmul
         round, rpow, rsub, rtruediv, select_dtypes, sem
         sem, sem, sem, set_axis, set_index, set_index
         set_index, shape, shift, skew, skew, skew, skew
         sort_index, sort_index, sort_index, sort_index
         sort_values, sort_values, sort_values, stack, std
         std, std, std, style, sub, sum, swaplevel
         to_dict, to_dict, to_dict, to_dict, to_dict
         to_feather, to_html, to_html, to_html, to_iceberg
         to_markdown, to_markdown, to_markdown
         to_markdown, to_numpy, to_orc, to_orc, to_orc
         to_orc, to_parquet, to_parquet, to_parquet
         to_period, to_records, to_series, to_stata
         to_string, to_string, to_string, to_timestamp
         to_xml, to_xml, to_xml, transform, transpose
         truediv, unstack, update, value_counts, values
         var, var, var, var, __arrow_c_stream__
         __dataframe__, __divmod__, __getitem__, __init__
         __len__, __matmul__, __matmul__, __matmul__
         __rdivmod__, __repr__, __rmatmul__, __setitem__

        def check_int_infer_dtype(dtypes):
            converted_dtypes: list[type] = []
            for dtype in dtypes:
                # Numpy maps int to different types (int32, in64) on Windows and Linux
                # see https://github.com/numpy/numpy/issues/9464
                if (isinstance(dtype, str) and dtype == "int") or (dtype is int):
                    converted_dtypes.append(np.int32)
                    converted_dtypes.append(np.int64)
                elif dtype == "float" or dtype is float:
                    # GH#42452 : np.dtype("float") coerces to np.float64 from Numpy 1.20
                    converted_dtypes.extend([np.float64, np.float32])
                else:
                    converted_dtypes.append(infer_dtype_from_object(dtype))
            return frozenset(converted_dtypes)

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

file core/indexes/timedeltas.py
imports: __future__, typing, pandas
defines: TimedeltaIndex, timedelta_range

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

    def time_categorical_contains(self):
        self.c.searchsorted(self.key)

class TimedeltaIndex(DatetimeTimedeltaMixin):  [core/indexes/timedeltas.py:75]
methods: _engine_type, _is_comparable_dtype, _parse_with_reso
         _parsed_string_to_bounds, _resolution_obj
         get_loc, inferred_type, __new__

    def inferred_type(self) -> str:
        return "timedelta64"

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

    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

    def _engine_type(self) -> type[libindex.TimedeltaEngine]:
        return libindex.TimedeltaEngine

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

class SearchSorted:  [asv_bench/benchmarks/series_methods.py:122]
methods: setup, time_searchsorted

# --- Layer 04: Variable context ---
# call-chain context
  called by: add_categories [categorical.py]
  called by: to_coo [accessor.py]

# call-chain context
  called by: _make_unpacked_invalid_op [datetimelike.py]

# call-chain context
  called by: time_select_dtype_int_include [dtypes.py]
  called by: time_select_dtype_int_exclude [dtypes.py]

# call-chain context
  called by: _prepare_pandas [stata.py]

# call-chain context
  called by: select_dtypes [frame.py]

# call-chain context
  called by: _get_binner_for_time [resample.py]

# call-chain context
  called by: setup_cache [algorithms.py]
  called by: setup [frame_methods.py]

# call-chain context
  called by: _cmp_method [array.py]
  called by: func [categorical.py]

# call-chain context
  called by: time_categorical_index_contains [categoricals.py]
  called by: time_categorical_contains [categoricals.py]

# call-chain context
  called by: time_categorical_index_contains [categoricals.py]
  called by: time_categorical_contains [categoricals.py]

# call-chain context
  called by: time_categorical_index_contains [categoricals.py]
  called by: time_categorical_contains [categoricals.py]

# call-chain context
  called by: time_categorical_index_contains [categoricals.py]
  called by: time_categorical_contains [categoricals.py]

# call-chain context
  called by: _prepare_pandas [stata.py]

```
