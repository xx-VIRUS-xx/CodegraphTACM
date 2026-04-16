# pandas-86 :: tacm-dyn

query: BUG: correct wrong error message in df.pivot when columns=None (#30925)

## selected nodes

- rank=1 layer=FILE tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/common.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/common.py
- rank=2 layer=CLASS tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py::TestPivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py
- rank=3 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::Pivot.time_reshape_pivot_time_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=4 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=5 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=6 layer=FILE tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=7 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::pivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=8 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=9 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py::__internal_pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/pivot.py
- rank=10 layer=CLASS tokens=884 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=11 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pivot_table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=12 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pivot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=13 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_agg file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=14 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=15 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=16 layer=FUNCTION tokens=327 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_exceptions.py::rewrite_warning file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_exceptions.py
- rank=17 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._next_iter_line file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py
- rank=18 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/validate_unwanted_patterns.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/validate_unwanted_patterns.py
- rank=19 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/validate_unwanted_patterns.py::strings_with_wrong_placed_whitespace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/scripts/validate_unwanted_patterns.py
- rank=20 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_raises.py::func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_raises.py
- rank=21 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/console.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/console.py
- rank=22 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/common.py::is_local_in_caller_frame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/common.py
- rank=23 layer=FUNCTION tokens=318 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::cat_safe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=24 layer=FILE tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py
- rank=25 layer=FUNCTION tokens=194 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_warnings.py::_assert_raised_with_correct_stacklevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_warnings.py
- rank=26 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=27 layer=FILE tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=28 layer=FILE tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/grouper.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/grouper.py
- rank=29 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.num_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=30 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._getitem_multilevel file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=31 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py::PivotTable.time_pivot_table_margins_only_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reshape.py
- rank=32 layer=FUNCTION tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::raise_construction_error file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py

## context

```text
file pandas/core/common.py
imports: __future__, builtins, collections, contextlib, functools, inspect, sys, typing
defines: flatten, consensus_name_attr, is_bool_indexer, cast_scalar_indexer, not_none, any_none, all_none, any_not_none, all_not_none, count_not_none, asarray_tuplesafe, asarray_tuplesafe, asarray_tuplesafe, index_labels_to_array, maybe_make_list, maybe_iterable_to_list, is_null_slice, is_empty_slice, is_true_slices, is_full_slice, get_callable_name, apply_if_callable, standardize_mapping, random_state, random_state, random_state, pipe, pipe, pipe, get_rename_function, f, convert_to_list_like, temp_setattr, require_length_match, get_cython_func, fill_missing_names, is_local_in_caller_frame

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

    def time_reshape_pivot_time_series(self):
        self.df.pivot(index="date", columns="variable", values="value")

    def time_pivot_table(self):
        self.df.pivot_table(index="key1", columns=["key2", "key3"])

    def time_pivot_table_margins(self):
        self.df.pivot_table(index="key1", columns=["key2", "key3"], margins=True)

file core/reshape/pivot.py
imports: __future__, itertools, typing, numpy, pandas, collections
defines: pivot_table, __internal_pivot_table, _add_margins, _compute_grand_margin, _generate_marginal_results, _all_key, _generate_marginal_results_without_values, _all_key, _convert_by, pivot, crosstab, _normalize, _get_names, _build_names_mapper

def pivot(
    data: DataFrame,
    *,
    columns: IndexLabel,
    index: IndexLabel | lib.NoDefault = lib.no_default,
    values: IndexLabel | lib.NoDefault = lib.no_default,
) -> DataFrame:
    """
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

    def time_pivot_table_agg(self):
        self.df.pivot_table(
            index="key1", columns=["key2", "key3"], aggfunc=["sum", "mean"]
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

file pandas/scripts/validate_unwanted_patterns.py
imports: argparse, ast, collections, re, sys, token, tokenize, typing
defines: _get_literal_string_prefix_len, private_function_across_module, private_import_across_module, strings_with_wrong_placed_whitespace, has_wrong_whitespace, nodefault_used_not_only_for_typing, doesnt_use_pandas_warnings, main

def strings_with_wrong_placed_whitespace(
    file_obj: IO[str],
) -> Iterable[tuple[int, str]]:
    """
    # ... truncated

    def func(x):
        raise TypeError("Test error message")

file io/formats/console.py
imports: __future__, shutil, pandas, __main__
defines: get_console_size, in_interactive_session, check_main, in_ipython_frontend

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

file asv_bench/benchmarks/ctors.py
imports: numpy, pandas
defines: SeriesConstructors, SeriesDtypesConstructors, MultiIndexConstructor, DatetimeIndexConstructor, no_change, list_of_str, gen_of_str, arr_dict, list_of_tuples, gen_of_tuples, list_of_lists, list_of_tuples_with_none, list_of_lists_with_none

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

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

file core/computation/ops.py
imports: __future__, datetime, functools, operator, typing, numpy, pandas, collections
defines: Term, Constant, Op, BinOp, UnaryOp, MathCall, FuncNode, _in, _not_in, is_term

file core/groupby/grouper.py
imports: __future__, itertools, typing, warnings, numpy, pandas, collections
defines: Grouper, Grouping, get_grouper, is_in_axis, is_in_obj, _is_label_like, _convert_grouper

    def num_columns(self) -> int:
        """
        Return the number of columns in the DataFrame.
        """

    def _getitem_multilevel(self, key):
        # self.columns is a MultiIndex
        assert isinstance(self.columns, MultiIndex)
        if isinstance(key, tuple) and any(
            isinstance(k, (slice, list, np.ndarray)) for k in key
        ):
            # Tuple key contains slices or lists, e.g. df[:, "t1"] which gives
            # key=(slice(None), "t1"), or df[["A", "B"], "t1"] which gives
            # key=(["A", "B"], "t1"). Use get_locs which handles
            # per-level slicing and list selection (GH#26511)
            loc = self.columns.get_locs(key)
            new_columns = self.columns[loc]
    # ... truncated

    def time_pivot_table_margins_only_column(self):
        self.df.pivot_table(columns=["key1", "key2", "key3"], margins=True)

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
```
