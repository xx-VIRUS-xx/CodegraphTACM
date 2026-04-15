# pandas-47 :: tacm

query: BUG: assignment to multiple columns when some column do not exist (#29334)

## selected nodes

- rank=1 layer=FILE tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=2 layer=FILE tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=3 layer=FILE tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/api.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/api.py
- rank=4 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=5 layer=CLASS tokens=396 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/computation/test_eval.py::TestOperations file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/computation/test_eval.py
- rank=6 layer=CLASS tokens=261 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_chaining_and_caching.py::TestChaining file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_chaining_and_caching.py
- rank=7 layer=CLASS tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_insert.py::TestDataFrameInsert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_insert.py
- rank=8 layer=FUNCTION tokens=343 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._do_select_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=9 layer=FUNCTION tokens=410 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::stack_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=10 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._ensure_listlike_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=11 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.__setitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=12 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.get_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=13 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_stack_multi_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=14 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py::datetime_column_to_ndarray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=15 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::stack_v3 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=16 layer=FUNCTION tokens=276 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_reorder_for_extension_array_stack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=17 layer=FUNCTION tokens=355 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=18 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py::string_column_to_ndarray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=19 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.num_rows file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=20 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::HDFStore.append_to_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=21 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py::categorical_column_to_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/from_dataframe.py
- rank=22 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_convert_level_number file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=23 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=24 layer=FUNCTION tokens=255 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_stack_multi_column_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=25 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=26 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.get_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=27 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame.get_column_by_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=28 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.column_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py

## context

```text
file core/reshape/reshape.py
imports: __future__, itertools, typing, warnings, numpy, pandas
defines: _Unstacker, _unstack_multiple, unstack, unstack, unstack, _unstack_frame, _unstack_extension_series, stack, stack_factorize, stack_multiple, _stack_multi_column_index, _stack_multi_columns, _convert_level_number, _reorder_for_extension_array_stack, stack_v3, stack_reshape

file core/interchange/from_dataframe.py
imports: __future__, ctypes, re, typing, warnings, numpy, pandas
defines: from_dataframe, _from_dataframe, protocol_df_chunk_to_pandas, primitive_column_to_ndarray, categorical_column_to_series, string_column_to_ndarray, parse_datetime_format_str, datetime_column_to_ndarray, buffer_to_ndarray, set_nulls, set_nulls, set_nulls, set_nulls

file pandas/core/api.py
imports: pandas
defines: —

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class TestOperations:  [tests/computation/test_eval.py:1081]
methods: eval, local_func, local_func, test_4d_ndarray_fails
         test_assignment_column_invalid_assign
         test_assignment_column_invalid_assign_function_call
         test_assignment_column_multiple_raise
         test_assignment_explicit, test_assignment_fails
         test_assignment_in_query
         test_assignment_multiple_raises
         test_assignment_not_inplace
         test_assignment_single_assign_existing
         test_assignment_single_assign_local_overlap
         test_assignment_single_assign_name
         test_assignment_single_assign_new
         test_attr_expression
         test_basic_period_index_boolean_expression
         test_basic_period_index_subscript_expression
         test_bool_ops_with_constants
         test_cannot_copy_item, test_cannot_item_assign
         test_check_many_exprs, test_column_in
         test_constant, test_date_boolean
         test_failing_subscript_with_name_error
         test_fails_ampersand_pipe, test_fails_and_or_not
         test_inplace_no_assignment
         test_lhs_expression_subscript
         test_multi_line_expression
         test_multi_line_expression_callable_local_variable
         test_multi_line_expression_callable_local_variable_with_kwargs
         test_multi_line_expression_local_variable
         test_multi_line_expression_not_inplace
         test_nested_period_index_subscript_expression
         test_query_inplace, test_simple_arith_ops
         test_simple_bool_ops, test_simple_in_ops
         test_single_variable

class TestChaining:  [tests/indexing/test_chaining_and_caching.py:74]
methods: test_cache_updating, test_cache_updating2
         test_chained_getitem_with_lists
         test_detect_chained_assignment
         test_detect_chained_assignment_changing_dtype
         test_detect_chained_assignment_doc_example
         test_detect_chained_assignment_fails
         test_detect_chained_assignment_false_positives
         test_detect_chained_assignment_is_copy_pickle
         test_detect_chained_assignment_object_dtype
         test_detect_chained_assignment_raises
         test_detect_chained_assignment_sorting
         test_detect_chained_assignment_str
         test_detect_chained_assignment_undefined_column
         test_detect_chained_assignment_warning_stacklevel
         test_detect_chained_assignment_warnings_errors
         test_getitem_loc_assignment_slice_state
         test_iloc_setitem_chained_assignment
         test_setitem_chained_setfault
         test_setting_with_copy_bug
         test_setting_with_copy_bug_no_warning

class TestDataFrameInsert:  [frame/indexing/test_insert.py:20]
methods: test_insert, test_insert_EA_no_warning
         test_insert_column_bug_4032
         test_insert_delete_mixed_multiindex_columns
         test_insert_frame, test_insert_int64_loc
         test_insert_with_columns_dups

    def _do_select_columns(self, data: DataFrame, columns: Sequence[str]) -> DataFrame:
        if not self._column_selector_set:
            column_set = set(columns)
            if len(column_set) != len(columns):
                raise ValueError("columns contains duplicate entries")
            unmatched = column_set.difference(data.columns)
            if unmatched:
                joined = ", ".join(list(unmatched))
                raise ValueError(
                    "The following columns were not "
                    f"found in the Stata data set: {joined}"
                )
            # Copy information for retained columns for later processing
            dtyplist = []
            typlist = []
            fmtlist = []
            lbllist = []
            for col in columns:
                i = data.columns.get_loc(col)
                dtyplist.append(self._dtyplist[i])
                typlist.append(self._typlist[i])
                fmtlist.append(self._fmtlist[i])
                lbllist.append(self._lbllist[i])

            self._dtyplist = dtyplist  # type: ignore[assignment]
            self._typlist = typlist  # type: ignore[assignment]
            self._fmtlist = fmtlist  # type: ignore[assignment]
            self._lbllist = lbllist  # type: ignore[assignment]
            self._column_selector_set = True

        return data[columns]

def stack_multiple(frame: DataFrame, level, dropna: bool = True, sort: bool = True):
    # If all passed levels match up to column names, no
    # ambiguity about what to do
    if all(lev in frame.columns.names for lev in level):
        result = frame
        for lev in level:
            # error: Incompatible types in assignment (expression has type
            # "Series | DataFrame", variable has type "DataFrame")
            result = stack(result, lev, dropna=dropna, sort=sort)  # type: ignore[assignment]

    # Otherwise, level numbers may change as each successive level is stacked
    elif all(isinstance(lev, int) for lev in level):
        # As each stack is done, the level numbers decrease, so we need
        #  to account for that when level is a sequence of ints
        result = frame
        # _get_level_number() checks level numbers are in range and converts
        # negative numbers to positive
        level = [frame.columns._get_level_number(lev) for lev in level]

        while level:
            lev = level.pop(0)
            # error: Incompatible types in assignment (expression has type
            # "Series | DataFrame", variable has type "DataFrame")
            result = stack(result, lev, dropna=dropna, sort=sort)  # type: ignore[assignment]
            # Decrement all level numbers greater than current, as these
            # have now shifted down by one
            level = [v if v <= lev else v - 1 for v in level]

    else:
        raise ValueError(
            "level should contain all level names or all level "
            "numbers, not a mixture of the two."
        )

    return result

    def _ensure_listlike_indexer(self, key, axis=None) -> None:
        """
        Ensure that a list-like of column labels are all present by adding them if
        they do not already exist.

        Parameters
        ----------
        key : list-like of column labels
            Target labels.
        axis : key axis if known
        """
    # ... truncated

    def __setitem__(self, key, value) -> None:
        """
        Set item(s) in DataFrame by key.

        This method allows you to set the values of one or more columns in the
        DataFrame using a key. If the key does not exist, a new
        column will be created.

        Parameters
        ----------
        key : The object(s) in the index which are to be assigned to
            Column label(s) to set. Can be a single column name, list of column names,
    # ... truncated

    def get_columns(self) -> Iterable[Column]:
        """
        Return an iterator yielding the columns.
        """

def _stack_multi_columns(
    frame: DataFrame, level_num: int = -1, dropna: bool = True, sort: bool = True
) -> DataFrame:
    def _convert_level_number(level_num: int, columns: Index):
        """
    # ... truncated

def datetime_column_to_ndarray(col: Column) -> tuple[np.ndarray | pd.Series, Any]:
    """
    Convert a column holding DateTime data to a NumPy array.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of np.ndarray holding the data and the memory owner object
        that keeps the memory alive.
    """
    buffers = col.get_buffers()

    _, col_bit_width, format_str, _ = col.dtype
    dbuf, _ = buffers["data"]
    # Consider dtype being `uint` to get number of units passed since the 01.01.1970

    data = buffer_to_ndarray(
        dbuf,
        (
            DtypeKind.INT,
            col_bit_width,
            getattr(ArrowCTypes, f"INT{col_bit_width}"),
            Endianness.NATIVE,
        ),
        offset=col.offset,
        length=col.size(),
    )

    data = parse_datetime_format_str(format_str, data)  # type: ignore[assignment]
    data = set_nulls(data, col, buffers["validity"])
    return data, buffers

def stack_v3(frame: DataFrame, level: list[int]) -> Series | DataFrame:
    if frame.columns.nunique() != len(frame.columns):
        raise ValueError("Columns with duplicate values are not supported in stack")
    if not len(level):
        return frame
    set_levels = set(level)
    stack_cols = frame.columns._drop_level_numbers(
        [k for k in range(frame.columns.nlevels - 1, -1, -1) if k not in set_levels]
    )

    result: Series | DataFrame
    if not isinstance(frame.columns, MultiIndex):
    # ... truncated

def _reorder_for_extension_array_stack(
    arr: ExtensionArray, n_rows: int, n_columns: int
) -> ExtensionArray:
    """
    Re-orders the values when stacking multiple extension-arrays.

    The indirect stacking method used for EAs requires a followup
    take to get the order correct.

    Parameters
    ----------
    arr : ExtensionArray
    n_rows, n_columns : int
        The number of rows and columns in the original DataFrame.

    Returns
    -------
    taken : ExtensionArray
        The original `arr` with elements re-ordered appropriately

    Examples
    --------
    >>> arr = np.array(["a", "b", "c", "d", "e", "f"])
    >>> _reorder_for_extension_array_stack(arr, 2, 3)
    array(['a', 'c', 'e', 'b', 'd', 'f'], dtype='<U1')

    >>> _reorder_for_extension_array_stack(arr, 3, 2)
    array(['a', 'd', 'b', 'e', 'c', 'f'], dtype='<U1')
    """
    # final take to get the order correct.
    # idx is an indexer like
    # [c0r0, c1r0, c2r0, ...,
    #  c0r1, c1r1, c2r1, ...]
    idx = np.arange(n_rows * n_columns).reshape(n_columns, n_rows).T.reshape(-1)
    return arr.take(idx)

def unstack(
    obj: Series | DataFrame, level, fill_value=None, sort: bool = True
) -> Series | DataFrame:
    if isinstance(level, (tuple, list)):
        if len(level) != 1:
            # _unstack_multiple only handles MultiIndexes,
            # and isn't needed for a single level
            return _unstack_multiple(obj, level, fill_value=fill_value, sort=sort)
        else:
            level = level[0]

    if not is_integer(level) and not level == "__placeholder__":
        # check if level is valid in case of regular index
        obj.index._get_level_number(level)

    if isinstance(obj, DataFrame):
        if isinstance(obj.index, MultiIndex):
            return _unstack_frame(obj, level, fill_value=fill_value, sort=sort)
        else:
            return obj.T.stack()
    elif not isinstance(obj.index, MultiIndex):
        # GH 36113
        # Give nicer error messages when unstack a Series whose
        # Index is not a MultiIndex.
        raise ValueError(
            f"index must be a MultiIndex to unstack, {type(obj.index)} was passed"
        )
    else:
        if is_1d_only_ea_dtype(obj.dtype):
            return _unstack_extension_series(obj, level, fill_value, sort=sort)
        unstacker = _Unstacker(
            obj.index, level=level, constructor=obj._constructor_expanddim, sort=sort
        )
        return unstacker.get_result(obj, value_columns=None, fill_value=fill_value)

def string_column_to_ndarray(col: Column) -> tuple[np.ndarray, Any]:
    """
    Convert a column holding string data to a NumPy array.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of np.ndarray holding the data and the memory owner object
    # ... truncated

    def num_rows(self) -> int | None:
        # TODO: not happy with Optional, but need to flag it may be expensive
        #       why include it if it may be None - what do we expect consumers
        #       to do here?
        """
        Return the number of rows in the DataFrame, if available.
        """

    def append_to_multiple(
        self,
        d: dict,
        value,
        selector,
        data_columns=None,
        axes=None,
        dropna: bool | lib.NoDefault = lib.no_default,
        **kwargs,
    ) -> None:
        """
    # ... truncated

def categorical_column_to_series(col: Column) -> tuple[pd.Series, Any]:
    """
    Convert a column holding categorical data to a pandas Series.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of pd.Series holding the data and the memory owner object
    # ... truncated

    def _convert_level_number(level_num: int, columns: Index):
        """
        Logic for converting the level number to something we can safely pass
        to swaplevel.

        If `level_num` matches a column name return the name from
        position `level_num`, otherwise return `level_num`.
        """
        if level_num in columns.names:
            return columns.names[level_num]

        return level_num

def _unstack_multiple(
    data: Series | DataFrame, clocs, fill_value=None, sort: bool = True
):
    if len(clocs) == 0:
        return data

    # NOTE: This doesn't deal with hierarchical columns yet

    index = data.index
    index = cast("MultiIndex", index)  # caller is responsible for checking

    # GH 19966 Make sure if MultiIndexed index has tuple name, they will be
    # ... truncated

def _stack_multi_column_index(columns: MultiIndex) -> MultiIndex | Index:
    """Creates a MultiIndex from the first N-1 levels of this MultiIndex."""
    if len(columns.levels) <= 2:
        return columns.levels[0]._rename(name=columns.names[0])

    levs = (
        [lev[c] if c >= 0 else None for c in codes]
        for lev, codes in zip(columns.levels[:-1], columns.codes[:-1], strict=True)
    )

    # Remove duplicate tuples in the MultiIndex.
    tuples = zip(*levs, strict=True)
    unique_tuples = (key for key, _ in itertools.groupby(tuples))
    new_levs = zip(*unique_tuples, strict=True)

    # The dtype of each level must be explicitly set to avoid inferring the wrong type.
    # See GH-36991.
    return MultiIndex.from_arrays(
        [
            # Not all indices can accept None values.
            Index(new_lev, dtype=lev.dtype) if None not in new_lev else new_lev
            for new_lev, lev in zip(new_levs, columns.levels[:-1], strict=True)
        ],
        names=columns.names[:-1],
    )

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

    def get_column(self, i: int) -> Column:
        """
        Return the column at the indicated position.
        """

    def get_column_by_name(self, name: str) -> Column:
        """
        Return the column whose name is the indicated name.
        """

    def column_names(self) -> Index:
        return self._df.columns
```
