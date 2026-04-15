# pandas-83 :: codesearch

query: BUG: concat not copying index and columns when copy=True (#31119)

## selected nodes

- rank=1 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._maybe_make_multi_index_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=2 layer=FUNCTION tokens=490 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._reindex_and_concat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=3 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_concat_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=4 layer=FUNCTION tokens=347 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._make_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=5 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.get_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py
- rank=6 layer=FUNCTION tokens=362 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_left_join_on_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=7 layer=FUNCTION tokens=214 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::psql_insert_copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=8 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=9 layer=FUNCTION tokens=382 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._do_select_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=10 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::tupleobject_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=11 layer=FUNCTION tokens=258 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py::is_potential_multi_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py
- rank=12 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::is_index_col file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=13 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::DataCol.__eq__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=14 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::IndexCol.__eq__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=15 layer=FUNCTION tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py::SparseFrameAccessor._prep_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py
- rank=16 layer=FUNCTION tokens=896 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._rows_to_cols file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py
- rank=17 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameRowApply.result_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py
- rank=18 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_store.py::col file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_store.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._maybe_make_multi_index_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py]
    def _maybe_make_multi_index_columns(
        self,
        columns: SequenceT,
        col_names: Sequence[Hashable] | None = None,
    ) -> SequenceT | MultiIndex:
        # possibly create a column mi here
        if is_potential_multi_index(columns):
            columns_mi = cast("Sequence[tuple[Hashable, ...]]", columns)
            return MultiIndex.from_tuples(columns_mi, names=col_names)
        return columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._reindex_and_concat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _reindex_and_concat(
        self,
        join_index: Index,
        left_indexer: npt.NDArray[np.intp] | None,
        right_indexer: npt.NDArray[np.intp] | None,
    ) -> DataFrame:
        """
        reindex along index and concat along columns.
        """
        # Take views so we do not alter the originals
        left = self.left[:]
        right = self.right[:]

        llabels, rlabels = _items_overlap_with_suffix(
            self.left._info_axis, self.right._info_axis, self.suffixes
        )

        if left_indexer is not None and not is_range_indexer(left_indexer, len(left)):
            # Pinning the index here (and in the right code just below) is not
            #  necessary, but makes the `.take` more performant if we have e.g.
            #  a MultiIndex for left.index.
            lmgr = left._mgr.reindex_indexer(
                join_index,
                left_indexer,
                axis=1,
                only_slice=True,
                allow_dups=True,
                use_na_proxy=True,
            )
            left = left._constructor_from_mgr(lmgr, axes=lmgr.axes)
        left.index = join_index

        if right_indexer is not None and not is_range_indexer(
            right_indexer, len(right)
        ):
            rmgr = right._mgr.reindex_indexer(
                join_index,
                right_indexer,
                axis=1,
                only_slice=True,
                allow_dups=True,
                use_na_proxy=True,
            )
            right = right._constructor_from_mgr(rmgr, axes=rmgr.axes)
        right.index = join_index

        from pandas import concat

        left.columns = llabels
        right.columns = rlabels
        result = concat([left, right], axis=1)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_concat_indexes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py]
def _concat_indexes(indexes) -> Index:
    return indexes[0].append(indexes[1:])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._make_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py]
    def _make_index(
        self, alldata, columns, indexnamerow: list[Scalar] | None = None
    ) -> tuple[Index | None, Sequence[Hashable] | MultiIndex]:
        index: Index | None
        if isinstance(self.index_col, list) and len(self.index_col):
            to_remove = []
            indexes = []
            for idx in self.index_col:
                if isinstance(idx, str):
                    raise ValueError(f"Index {idx} invalid")
                to_remove.append(idx)
                indexes.append(alldata[idx])
            # remove index items from content and columns, don't pop in
            # loop
            for i in sorted(to_remove, reverse=True):
                alldata.pop(i)
                if not self._implicit_index:
                    columns.pop(i)
            index = self._agg_index(indexes)

            # add names for the index
            if indexnamerow:
                coffset = len(indexnamerow) - len(columns)
                index = index.set_names(indexnamerow[:coffset])
        else:
            index = None

        # maybe create a mi on the columns
        columns = self._maybe_make_multi_index_columns(columns, self.col_names)

        return index, columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py::PandasDataFrameXchg.get_column [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe.py]
    def get_column(self, i: int) -> PandasColumn:
        return PandasColumn(self._df.iloc[:, i], allow_copy=self._allow_copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_left_join_on_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
def _left_join_on_index(
    left_ax: Index, right_ax: Index, join_keys: list[ArrayLike], sort: bool = False
) -> tuple[Index, npt.NDArray[np.intp] | None, npt.NDArray[np.intp]]:
    if isinstance(right_ax, MultiIndex):
        lkey, rkey = _get_multiindex_indexer(join_keys, right_ax, sort=sort)
    else:
        # error: Incompatible types in assignment (expression has type
        # "Union[Union[ExtensionArray, ndarray[Any, Any]], Index, Series]",
        # variable has type "ndarray[Any, dtype[signedinteger[Any]]]")
        lkey = join_keys[0]  # type: ignore[assignment]
        # error: Incompatible types in assignment (expression has type "Index",
        # variable has type "ndarray[Any, dtype[signedinteger[Any]]]")
        rkey = right_ax._values  # type: ignore[assignment]

    left_key, right_key, count = _factorize_keys(lkey, rkey, sort=sort)
    left_indexer, right_indexer = libjoin.left_outer_join(
        left_key, right_key, count, sort=sort
    )

    if sort or len(left_ax) != len(left_indexer):
        # if asked to sort or there are 1-to-many matches
        join_index = left_ax.take(left_indexer)
        return join_index, left_indexer, right_indexer

    # left frame preserves order & length of its index
    return left_ax, None, right_indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::psql_insert_copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py]
    def psql_insert_copy(table, conn, keys, data_iter):
        # gets a DBAPI connection that can provide a cursor
        dbapi_conn = conn.connection
        with dbapi_conn.cursor() as cur:
            s_buf = StringIO()
            writer = csv.writer(s_buf)
            writer.writerows(data_iter)
            s_buf.seek(0)

            columns = ", ".join([f'"{k}"' for k in keys])
            if table.schema:
                table_name = f"{table.schema}.{table.name}"
            else:
                table_name = table.name

            sql_query = f"COPY {table_name} ({columns}) FROM STDIN WITH CSV"
            cur.copy_expert(sql=sql_query, file=s_buf)
        return expected_count

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def columns(self) -> Index:
        return self.obj.columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._do_select_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::tupleobject_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h]
static inline int tupleobject_cmp(PyTupleObject *a, PyTupleObject *b) {
  Py_ssize_t i;

  if (Py_SIZE(a) != Py_SIZE(b)) {
    return 0;
  }

  for (i = 0; i < Py_SIZE(a); ++i) {
    if (!pyobject_cmp(PyTuple_GET_ITEM(a, i), PyTuple_GET_ITEM(b, i))) {
      return 0;
    }
  }
  return 1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py::is_potential_multi_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py]
def is_potential_multi_index(
    columns: Sequence[Hashable] | MultiIndex,
    index_col: bool | Sequence[int] | None = None,
) -> bool:
    """
    Check whether or not the `columns` parameter
    could be converted into a MultiIndex.

    Parameters
    ----------
    columns : array-like
        Object which may or may not be convertible into a MultiIndex
    index_col : None, bool or list, optional
        Column or columns to use as the (possibly hierarchical) index

    Returns
    -------
    bool : Whether or not columns could become a MultiIndex
    """
    if index_col is None or isinstance(index_col, bool):
        index_columns = set()
    else:
        index_columns = set(index_col)

    return bool(
        len(columns)
        and not isinstance(columns, ABCMultiIndex)
        and all(isinstance(c, tuple) for c in columns if c not in index_columns)
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::is_index_col [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py]
def is_index_col(col) -> bool:
    return col is not None and col is not False

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::DataCol.__eq__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def __eq__(self, other: object) -> bool:
        """compare 2 col items"""
        return all(
            getattr(self, a, None) == getattr(other, a, None)
            for a in ["name", "cname", "dtype", "pos"]
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::IndexCol.__eq__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def __eq__(self, other: object) -> bool:
        """compare 2 col items"""
        return all(
            getattr(self, a, None) == getattr(other, a, None)
            for a in ["name", "cname", "axis", "pos"]
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py::SparseFrameAccessor._prep_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/accessor.py]
    def _prep_index(data, index, columns):
        from pandas.core.indexes.api import (
            default_index,
            ensure_index,
        )

        N, K = data.shape
        if index is None:
            index = default_index(N)
        else:
            index = ensure_index(index)
        if columns is None:
            columns = default_index(K)
        else:
            columns = ensure_index(columns)

        if len(columns) != K:
            raise ValueError(f"Column length mismatch: {len(columns)} vs. {K}")
        if len(index) != N:
            raise ValueError(f"Index length mismatch: {len(index)} vs. {N}")
        return index, columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._rows_to_cols [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py]
    def _rows_to_cols(self, content: list[list[Scalar]]) -> list[np.ndarray]:
        col_len = self.num_original_columns

        if self._implicit_index:
            col_len += len(self.index_col)

        max_len = max(len(row) for row in content)

        # Check that there are no rows with too many
        # elements in their row (rows with too few
        # elements are padded with NaN).
        if max_len > col_len and self.index_col is not False and self.usecols is None:
            footers = self.skipfooter if self.skipfooter else 0
            bad_lines = []

            iter_content = enumerate(content)
            content_len = len(content)
            content = []

            for i, _content in iter_content:
                actual_len = len(_content)
                if actual_len > col_len:
                    if callable(self.on_bad_lines):
                        new_l = self.on_bad_lines(_content)
                        if new_l is not None:
                            new_l = cast("list[Scalar]", new_l)
                            if len(new_l) > col_len:
                                row_num = self.pos - (content_len - i + footers)
                                bad_lines.append((row_num, len(new_l), "callable"))
                                new_l = new_l[:col_len]
                            content.append(new_l)

                    elif self.on_bad_lines in (
                        self.BadLineHandleMethod.ERROR,
                        self.BadLineHandleMethod.WARN,
                    ):
                        row_num = self.pos - (content_len - i + footers)
                        bad_lines.append((row_num, actual_len, "normal"))
                        if self.on_bad_lines == self.BadLineHandleMethod.ERROR:
                            break
                else:
                    content.append(_content)

            for row_num, actual_len, source in bad_lines:
                msg = (
                    f"Expected {col_len} fields in line {row_num + 1}, saw {actual_len}"
                )
                if source == "callable":
                    msg += " from bad_lines callable"
                elif (
                    self.delimiter
                    and len(self.delimiter) > 1
                    and self.quoting != csv.QUOTE_NONE
                ):
                    # see gh-13374
                    reason = (
                        "Error could possibly be due to quotes being "
                        "ignored when a multi-char delimiter is used."
                    )
                    msg += ". " + reason

                self._alert_malformed(msg, row_num + 1)

        # see gh-13320
        zipped_content = list(lib.to_object_array(content, min_width=col_len).T)

        if self.usecols:
            assert self._col_indices is not None
            col_indices = self._col_indices

            if self._implicit_index:
                zipped_content = [
                    a
                    for i, a in enumerate(zipped_content)
                    if (
                        i < len(self.index_col)
                        or i - len(self.index_col) in col_indices
                    )
                ]
            else:
                zipped_content = [
                    a for i, a in enumerate(zipped_content) if i in col_indices
                ]
        return zipped_content

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameRowApply.result_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def result_index(self) -> Index:
        return self.columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_store.py::col [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_store.py]
    def col(t, column):
        return getattr(store.get_storer(t).table.cols, column)
```
