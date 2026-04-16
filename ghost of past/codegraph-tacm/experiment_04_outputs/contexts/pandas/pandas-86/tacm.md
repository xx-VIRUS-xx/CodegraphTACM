# pandas-86 :: tacm

query: BUG: correct wrong error message in df.pivot when columns=None (#30925)

## selected nodes

- rank=1 layer=FILE tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/common.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/common.py
- rank=2 layer=FILE tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/fast_float_strtod.cpp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/fast_float_strtod.cpp
- rank=3 layer=CLASS tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py::TestPivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py
- rank=4 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=5 layer=CLASS tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_getitem.py::TestGetitemBooleanMask file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_getitem.py
- rank=6 layer=CLASS tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_arithmetic.py::TestFrameComparisons file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_arithmetic.py
- rank=7 layer=CLASS tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/period/test_period.py::TestPeriodDisallowedFreqs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/period/test_period.py
- rank=8 layer=CLASS tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_describe.py::TestDataFrameDescribe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_describe.py
- rank=9 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Pivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=10 layer=CLASS tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py::IOArgs file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py
- rank=11 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Pivot.time_reshape_pivot_time_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=12 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=13 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=14 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_agg file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=15 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins_only_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=16 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=17 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=18 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Pivot.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=19 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=20 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=21 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=22 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_categorical_observed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=23 layer=FUNCTION tokens=327 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_exceptions.py::rewrite_warning file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_exceptions.py
- rank=24 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::pivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=25 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._next_iter_line file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py
- rank=26 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=27 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_raises.py::func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_raises.py
- rank=28 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::__internal_pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=29 layer=FUNCTION tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_getitem.py::TestGetitemBooleanMask.df_dup_cols file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_getitem.py
- rank=30 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/common.py::is_local_in_caller_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/common.py
- rank=31 layer=FUNCTION tokens=318 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::cat_safe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=32 layer=FUNCTION tokens=194 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_warnings.py::_assert_raised_with_correct_stacklevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_warnings.py
- rank=33 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.num_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=34 layer=FUNCTION tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::raise_construction_error file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=35 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::external_error_raised file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py
- rank=36 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::ignore_doctest_warning file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=37 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::repr_class file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py
- rank=38 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate.py::new_func_wrong_docstring file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate.py
- rank=39 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::AppendableMultiFrameTable.read file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=40 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py::aggfun file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_groupby.py
- rank=41 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray._op_method_error_message file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py
- rank=42 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=43 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.get_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=44 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py

## context

```text
file pandas/core/common.py
imports: __future__, builtins, collections, contextlib, functools, inspect, sys, typing
defines: flatten, consensus_name_attr, is_bool_indexer, cast_scalar_indexer, not_none, any_none, all_none, any_not_none, all_not_none, count_not_none, asarray_tuplesafe, asarray_tuplesafe, asarray_tuplesafe, index_labels_to_array, maybe_make_list, maybe_iterable_to_list, is_null_slice, is_empty_slice, is_true_slices, is_full_slice, get_callable_name, apply_if_callable, standardize_mapping, random_state, random_state, random_state, pipe, pipe, pipe, get_rename_function, f, convert_to_list_like, temp_setattr, require_length_match, get_cython_func, fill_missing_names, is_local_in_caller_frame

file parser/fast_float_strtod.cpp
imports: fast_float, system_error
defines: fast_float_strtod

class TestPivot:  [tests/reshape/test_pivot.py:2734]
methods: test_pivot, test_pivot_columns_is_none
         test_pivot_columns_not_given
         test_pivot_duplicates, test_pivot_empty
         test_pivot_empty_dataframe_period_dtype
         test_pivot_empty_with_datetime
         test_pivot_index_is_none
         test_pivot_index_list_values_none_immutable_args
         test_pivot_index_none, test_pivot_integer_bug
         test_pivot_margins_with_none_index
         test_pivot_not_changing_index_name
         test_pivot_table_empty_dataframe_correct_index
         test_pivot_table_handles_explicit_datetime_types
         test_pivot_table_with_margins_and_numeric_column_names
         test_pivot_values_is_none
         test_pivot_with_pyarrow_categorical
         test_unstack_copy

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class TestGetitemBooleanMask:  [frame/indexing/test_getitem.py:338]
methods: df_dup_cols, test_getitem_bool_mask_categorical_index
         test_getitem_bool_mask_duplicate_columns_mixed_dtypes
         test_getitem_boolean_frame_unaligned_with_duplicate_columns
         test_getitem_boolean_frame_with_duplicate_columns
         test_getitem_boolean_series_with_duplicate_columns
         test_getitem_empty_frame_with_boolean
         test_getitem_frozenset_unique_in_column
         test_getitem_returns_view_when_column_is_unique_in_df

class TestFrameComparisons:  [tests/frame/test_arithmetic.py:86]
methods: test_comparison_invalid
         test_comparison_with_categorical_dtype
         test_df_boolean_comparison_error
         test_df_float_none_comparison
         test_df_string_comparison, test_frame_in_list
         test_mixed_comparison, test_timestamp_compare

class TestPeriodDisallowedFreqs:  [scalar/period/test_period.py:39]
methods: test_custom_business_day_freq_raises
         test_invalid_frequency_error_message
         test_invalid_frequency_period_error_message
         test_offsets_not_supported

class TestDataFrameDescribe:  [frame/methods/test_describe.py:15]
methods: test_datetime_is_numeric_includes_datetime
         test_describe_bool_frame
         test_describe_bool_in_mixed_frame
         test_describe_categorical
         test_describe_categorical_columns
         test_describe_datetime_columns
         test_describe_does_not_raise_error_for_dictlike_elements
         test_describe_empty_categorical_column
         test_describe_empty_object
         test_describe_exclude_pa_dtype
         test_describe_percentiles_integer_idx
         test_describe_timedelta_values
         test_describe_tz_values, test_describe_tz_values2
         test_describe_when_include_all_exclude_not_allowed
         test_describe_when_included_dtypes_not_present
         test_describe_with_duplicate_columns
         test_ea_with_na, test_refine_percentiles

class Pivot:  [asv_bench/benchmarks/reshape.py:32]
methods: setup, time_reshape_pivot_time_series

class IOArgs:  [pandas/io/common.py:92]
methods: —

    def time_reshape_pivot_time_series(self):
        self.df.pivot(index="date", columns="variable", values="value")

    def time_pivot_table(self):
        self.df.pivot_table(index="key1", columns=["key2", "key3"])

    def time_pivot_table_margins(self):
        self.df.pivot_table(index="key1", columns=["key2", "key3"], margins=True)

    def time_pivot_table_agg(self):
        self.df.pivot_table(
            index="key1", columns=["key2", "key3"], aggfunc=["sum", "mean"]
        )

    def time_pivot_table_margins_only_column(self):
        self.df.pivot_table(columns=["key1", "key2", "key3"], margins=True)

    def pivot_table(
        self,
        values=None,
        index=None,
        columns=None,
        aggfunc: AggFuncType = "mean",
        fill_value=None,
        margins: bool = False,
        dropna: bool = True,
        margins_name: Level = "All",
        observed: bool = True,
        sort: bool = True,
    # ... truncated

    def pivot(
        self, *, columns, index=lib.no_default, values=lib.no_default
    ) -> DataFrame:
        """
    # ... truncated

    def setup(self):
        N = 10000
        index = date_range("1/1/2000", periods=N, freq="h")
        data = {
            "value": np.random.randn(N * 50),
            "variable": np.arange(50).repeat(N),
            "date": np.tile(index.values, 50),
        }
        self.df = DataFrame(data)

    def time_pivot_table_categorical(self):
        self.df2.pivot_table(
            index="col1", values="col3", columns="col2", aggfunc="sum", fill_value=0
        )

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

    def time_pivot_table_categorical_observed(self):
        self.df2.pivot_table(
            index="col1",
            values="col3",
            columns="col2",
            aggfunc="sum",
            fill_value=0,
            observed=True,
        )

def rewrite_warning(
    target_message: str,
    target_category: type[Warning],
    new_message: str,
    new_category: type[Warning] | None = None,
) -> Generator[None]:
    """
    Rewrite the message of a warning.

    Parameters
    ----------
    target_message : str
        Warning message to match.
    target_category : Warning
        Warning type to match.
    new_message : str
        New warning message to emit.
    new_category : Warning or None, default None
        New warning type to emit. When None, will be the same as target_category.
    """
    if new_category is None:
        new_category = target_category
    with warnings.catch_warnings(record=True) as record:
        yield
    if len(record) > 0:
        match = re.compile(target_message)
        for warning in record:
            if warning.category is target_category and re.search(
                match, str(warning.message)
            ):
                category = new_category
                message: Warning | str = new_message
            else:
                category, message = warning.category, warning.message
            warnings.warn_explicit(
                message=message,
                category=category,
                filename=warning.filename,
                lineno=warning.lineno,
            )

def pivot(
    data: DataFrame,
    *,
    columns: IndexLabel,
    index: IndexLabel | lib.NoDefault = lib.no_default,
    values: IndexLabel | lib.NoDefault = lib.no_default,
) -> DataFrame:
    """
    # ... truncated

    def _next_iter_line(self, row_num: int) -> list[Scalar] | None:
        """
        Wrapper around iterating through `self.data` (CSV source).

        When a CSV error is raised, we check for specific
        error messages that allow us to customize the
        error message displayed to the user.

        Parameters
        ----------
        row_num: int
            The row number of the line being parsed.
    # ... truncated

def pivot_table(
    data: DataFrame,
    values=None,
    index=None,
    columns=None,
    aggfunc: AggFuncType = "mean",
    fill_value=None,
    margins: bool = False,
    dropna: bool = True,
    margins_name: Hashable = "All",
    observed: bool = True,
    sort: bool = True,
    # ... truncated

    def func(x):
        raise TypeError("Test error message")

def __internal_pivot_table(
    data: DataFrame,
    values,
    index,
    columns,
    aggfunc: AggFuncTypeBase | AggFuncTypeDict,
    fill_value,
    margins: bool,
    dropna: bool,
    margins_name: Hashable,
    observed: bool,
    sort: bool,
    # ... truncated

    def df_dup_cols(self):
        dups = ["A", "A", "C", "D"]
        df = DataFrame(np.arange(12).reshape(3, 4), columns=dups, dtype="float64")
        return df

def is_local_in_caller_frame(obj: NDFrame) -> bool:
    """
    Helper function used in detecting chained assignment.

    If the pandas object (DataFrame/Series) is a local variable
    in the caller's frame, it should not be a case of chained
    assignment or method call.

    For example:

    def test():
        df = pd.DataFrame(...)
        df["a"] = 1  # not chained assignment

    Inside ``df.__setitem__``, we call this function to check whether `df`
    (`self`) is a local variable in `test` frame (the frame calling setitem). If
    so, we know it is not a case of chained assignment (even when the refcount
    of `df` is below the threshold due to optimization of local variables).
    """
    frame = sys._getframe(2)
    for v in frame.f_locals.values():
        if v is obj:
            return True
    return False

def cat_safe(list_of_columns: list[npt.NDArray[np.object_]], sep: str):
    """
    Auxiliary function for :meth:`str.cat`.

    Same signature as cat_core, but handles TypeErrors in concatenation, which
    happen if the arrays in list_of columns have the wrong dtypes or content.

    Parameters
    ----------
    list_of_columns : list of numpy arrays
        List of arrays to be concatenated with sep;
        these arrays may not contain NaNs!
    sep : string
        The separator string for concatenating the columns.

    Returns
    -------
    nd.array
        The concatenation of list_of_columns with sep.
    """
    try:
        result = cat_core(list_of_columns, sep)
    except TypeError:
        # if there are any non-string values (wrong dtype or hidden behind
        # object dtype), np.sum will fail; catch and return with better message
        for column in list_of_columns:
            dtype = lib.infer_dtype(column, skipna=True)
            if dtype not in ["string", "empty"]:
                raise TypeError(
                    "Concatenation requires list-likes containing only "
                    "strings (or missing values). Offending values found in "
                    f"column {dtype}"
                ) from None
    return result

def _assert_raised_with_correct_stacklevel(
    actual_warning: warnings.WarningMessage,
) -> None:
    # https://stackoverflow.com/questions/17407119/python-inspect-stack-is-slow
    frame = inspect.currentframe()
    for _ in range(4):
        frame = frame.f_back  # type: ignore[union-attr]
    try:
        caller_filename = inspect.getfile(frame)  # type: ignore[arg-type]
    finally:
        # See note in
        # https://docs.python.org/3/library/inspect.html#inspect.Traceback
        del frame
    msg = (
        "Warning not set with correct stacklevel. "
        f"File where warning is raised: {actual_warning.filename} != "
        f"{caller_filename}. Warning message: {actual_warning.message}"
    )
    assert actual_warning.filename == caller_filename, msg

    def num_columns(self) -> int:
        """
        Return the number of columns in the DataFrame.
        """

def raise_construction_error(
    tot_items: int,
    block_shape: Shape,
    axes: list[Index],
    e: ValueError | None = None,
) -> NoReturn:
    """raise a helpful message about our construction"""
    passed = tuple(map(int, [tot_items, *block_shape]))
    # Correcting the user facing error message during dataframe construction
    if len(passed) <= 2:
        passed = passed[::-1]

    implied = tuple(len(ax) for ax in axes)
    # Correcting the user facing error message during dataframe construction
    if len(implied) <= 2:
        implied = implied[::-1]

    # We return the exception object instead of raising it so that we
    #  can raise it in the caller; mypy plays better with that
    if passed == implied and e is not None:
        raise e
    if block_shape[0] == 0:
        raise ValueError("Empty data passed with indices specified.")
    raise ValueError(f"Shape of passed values is {passed}, indices imply {implied}")

def external_error_raised(expected_exception: type[Exception]) -> ContextManager:
    """
    Helper function to mark pytest.raises that have an external error message.

    Parameters
    ----------
    expected_exception : Exception
        Expected error to raise.

    Returns
    -------
    Callable
        Regular `pytest.raises` function with `match` equal to `None`.
    """
    import pytest

    return pytest.raises(expected_exception, match=None)

def ignore_doctest_warning(item: pytest.Item, path: str, message: str) -> None:
    """Ignore doctest warning.

    Parameters
    ----------
    item : pytest.Item
        pytest test item.
    path : str
        Module path to Python object, e.g. "pandas.DataFrame.append". A
        warning will be filtered when item.name ends with in given path. So it is
        sufficient to specify e.g. "DataFrame.append".
    message : str
        Message to be filtered.
    """
    if item.name.endswith(path):
        item.add_marker(pytest.mark.filterwarnings(f"ignore:{message}"))

    def repr_class(x):
        if isinstance(x, Index):
            # return Index as it is to include values in the error message
            return x

        return type(x).__name__

def new_func_wrong_docstring():
    """Summary should be in the next line."""
    return "new_func_wrong_docstring called"

    def read(
        self,
        where=None,
        columns=None,
        start: int | None = None,
        stop: int | None = None,
    ) -> DataFrame:
        df = super().read(where=where, columns=columns, start=start, stop=stop)
        df = df.set_index(self.levels)

        # remove names for 'level_%d'
        df.index = df.index.set_names(
            [None if self._re_levels.search(name) else name for name in df.index.names]
        )

        return df

    def aggfun(ser):
        if ser.name == ("foo", "one"):
            raise TypeError("Test error message")
        return ser.sum()

    def _op_method_error_message(self, other, op) -> str:
        if hasattr(other, "dtype"):
            other_type = f"dtype '{other.dtype}'"
        else:
            other_type = f"object of type {type(other)}"
        return (
            f"operation '{op.__name__}' not supported for "
            f"dtype '{self.dtype}' with {other_type}"
        )

def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

    def get_columns(self) -> Iterable[Column]:
        """
        Return an iterator yielding the columns.
        """

    def len(self, text: str) -> int:
        return len(text)
```
