# pandas-47 :: hybrid-cs

query: BUG: assignment to multiple columns when some column do not exist (#29334)

## selected nodes

- rank=1 layer=FUNCTION tokens=382 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._do_select_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=2 layer=FUNCTION tokens=541 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py::_validate_or_indexify_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py
- rank=3 layer=FUNCTION tokens=286 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py::DataFrameDescriber._select_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py
- rank=4 layer=FUNCTION tokens=1502 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py::HTMLFormatter._write_col_header file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py
- rank=5 layer=FUNCTION tokens=451 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::stack_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=6 layer=FUNCTION tokens=835 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Table.create_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py::_validate_or_indexify_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/construction.py]
def _validate_or_indexify_columns(
    content: list[np.ndarray], columns: Index | None
) -> Index:
    """
    If columns is None, make numbers as column names; Otherwise, validate that
    columns have valid length.

    Parameters
    ----------
    content : list of np.ndarrays
    columns : Index or None

    Returns
    -------
    Index
        If columns is None, assign positional column index value as columns.

    Raises
    ------
    1. AssertionError when content is not composed of list of lists, and if
        length of columns is not equal to length of content.
    2. ValueError when content is list of lists, but length of each sub-list
        is not equal
    3. ValueError when content is list of lists, but length of sub-list is
        not equal to length of content
    """
    if columns is None:
        columns = default_index(len(content))
    else:
        # Add mask for data which is composed of list of lists
        is_mi_list = isinstance(columns, list) and all(
            isinstance(col, list) for col in columns
        )

        if not is_mi_list and len(columns) != len(content):  # pragma: no cover
            # caller's responsibility to check for this...
            raise AssertionError(
                f"{len(columns)} columns passed, passed data had {len(content)} columns"
            )
        if is_mi_list:
            # check if nested list column, length of each sub-list should be equal
            if len({len(col) for col in columns}) > 1:
                raise ValueError(
                    "Length of columns passed for MultiIndex columns is different"
                )

            # if columns is not empty and length of sublist is not equal to content
            if columns and len(columns[0]) != len(content):
                raise ValueError(
                    f"{len(columns[0])} columns passed, passed data had "
                    f"{len(content)} columns"
                )
    return columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py::DataFrameDescriber._select_data [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/methods/describe.py]
    def _select_data(self) -> DataFrame:
        """Select columns to be described."""
        if (self.include is None) and (self.exclude is None):
            # when some numerics are found, keep only numerics
            default_include: list[npt.DTypeLike] = [np.number, "datetime"]
            data = self.obj.select_dtypes(include=default_include)
            if len(data.columns) == 0:
                data = self.obj
        elif self.include == "all":
            if self.exclude is not None:
                msg = "exclude must be None when include is 'all'"
                raise ValueError(msg)
            data = self.obj
        else:
            data = self.obj.select_dtypes(
                include=self.include,
                exclude=self.exclude,
            )
            if len(data.columns) == 0:
                msg = "No columns match the specified include or exclude data types"
                raise ValueError(msg)
        return data

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py::HTMLFormatter._write_col_header [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py]
    def _write_col_header(self, indent: int) -> None:
        row: list[Hashable]
        is_truncated_horizontally = self.fmt.is_truncated_horizontally
        if isinstance(self.columns, MultiIndex):
            template = 'colspan="{span:d}" halign="left"'

            sentinel: lib.NoDefault | bool
            if self.fmt.sparsify:
                # GH3547
                sentinel = lib.no_default
            else:
                sentinel = False
            levels = self.columns._format_multi(sparsify=sentinel, include_names=False)
            level_lengths = get_level_lengths(levels, sentinel)
            inner_lvl = len(level_lengths) - 1
            for lnum, (records, values) in enumerate(
                zip(level_lengths, levels, strict=True)
            ):
                if is_truncated_horizontally:
                    # modify the header lines
                    ins_col = self.fmt.tr_col_num
                    if self.fmt.sparsify:
                        recs_new = {}
                        # Increment tags after ... col.
                        for tag, span in list(records.items()):
                            if tag >= ins_col:
                                recs_new[tag + 1] = span
                            elif tag + span > ins_col:
                                recs_new[tag] = span + 1
                                if lnum == inner_lvl:
                                    values = (
                                        *values[:ins_col],
                                        "...",
                                        *values[ins_col:],
                                    )
                                else:
                                    # sparse col headers do not receive a ...
                                    values = (
                                        *values[:ins_col],
                                        values[ins_col - 1],
                                        *values[ins_col:],
                                    )
                            else:
                                recs_new[tag] = span
                            # if ins_col lies between tags, all col headers
                            # get ...
                            if tag + span == ins_col:
                                recs_new[ins_col] = 1
                                values = (*values[:ins_col], "...", *values[ins_col:])
                        records = recs_new
                        inner_lvl = len(level_lengths) - 1
                        if lnum == inner_lvl:
                            records[ins_col] = 1
                    else:
                        recs_new = {}
                        for tag, span in list(records.items()):
                            if tag >= ins_col:
                                recs_new[tag + 1] = span
                            else:
                                recs_new[tag] = span
                        recs_new[ins_col] = 1
                        records = recs_new
                        values = [*values[:ins_col], "...", *values[ins_col:]]

                # see gh-22579
                # Column Offset Bug with to_html(index=False) with
                # MultiIndex Columns and Index.
                # Initially fill row with blank cells before column names.
                # TODO: Refactor to remove code duplication with code
                # block below for standard columns index.
                row = [""] * (self.row_levels - 1)
                if self.fmt.index or self.show_col_idx_names:
                    # see gh-22747
                    # If to_html(index_names=False) do not show columns
                    # index names.
                    # TODO: Refactor to use _get_column_name_list from
                    # DataFrameFormatter class and create a
                    # _get_formatted_column_labels function for code
                    # parity with DataFrameFormatter class.
                    if self.fmt.show_index_names:
                        name = self.columns.names[lnum]
                        row.append(pprint_thing(name or ""))
                    else:
                        row.append("")

                tags = {}
                j = len(row)
                for i, v in enumerate(values):
                    if i in records:
                        if records[i] > 1:
                            tags[j] = template.format(span=records[i])
                    else:
                        continue
                    j += 1
                    row.append(v)
                self.write_tr(row, indent, self.indent_delta, tags=tags, header=True)
        else:
            # see gh-22579
            # Column misalignment also occurs for
            # a standard index when the columns index is named.
            # Initially fill row with blank cells before column names.
            # TODO: Refactor to remove code duplication with code block
            # above for columns MultiIndex.
            row = [""] * (self.row_levels - 1)
            if self.fmt.index or self.show_col_idx_names:
                # see gh-22747
                # If to_html(index_names=False) do not show columns
                # index names.
                # TODO: Refactor to use _get_column_name_list from
                # DataFrameFormatter class.
                if self.fmt.show_index_names:
                    row.append(self.columns.name or "")
                else:
                    row.append("")
            row.extend(self._get_columns_formatted_values())
            align = self.fmt.justify

            if is_truncated_horizontally:
                ins_col = self.row_levels + self.fmt.tr_col_num
                row.insert(ins_col, "...")

            self.write_tr(row, indent, self.indent_delta, header=True, align=align)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::stack_multiple [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Table.create_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def create_index(
        self, columns=None, optlevel=None, kind: str | None = None
    ) -> None:
        """
        Create a pytables index on the specified columns.

        Parameters
        ----------
        columns : None, bool, or listlike[str]
            Indicate which columns to create an index on.

            * False : Do not create any indexes.
            * True : Create indexes on all columns.
            * None : Create indexes on all columns.
            * listlike : Create indexes on the given columns.

        optlevel : int or None, default None
            Optimization level, if None, pytables defaults to 6.
        kind : str or None, default None
            Kind of index, if None, pytables defaults to "medium".

        Raises
        ------
        TypeError if trying to create an index on a complex-type column.

        Notes
        -----
        Cannot index Time64Col or ComplexCol.
        Pytables must be >= 3.0.
        """
        if not self.infer_axes():
            return
        if columns is False:
            return

        # index all indexables and data_columns
        if columns is None or columns is True:
            columns = [a.cname for a in self.axes if a.is_data_indexable]
        if not isinstance(columns, (tuple, list)):
            columns = [columns]

        kw = {}
        if optlevel is not None:
            kw["optlevel"] = optlevel
        if kind is not None:
            kw["kind"] = kind

        table = self.table
        for c in columns:
            v = getattr(table.cols, c, None)
            if v is not None:
                # remove the index if the kind/optlevel have changed
                if v.is_indexed:
                    index = v.index
                    cur_optlevel = index.optlevel
                    cur_kind = index.kind

                    if kind is not None and cur_kind != kind:
                        v.remove_index()
                    else:
                        kw["kind"] = cur_kind

                    if optlevel is not None and cur_optlevel != optlevel:
                        v.remove_index()
                    else:
                        kw["optlevel"] = cur_optlevel

                # create the index
                if not v.is_indexed:
                    if v.type.startswith("complex"):
                        raise TypeError(
                            "Columns containing complex values can be stored but "
                            "cannot be indexed when using table format. Either use "
                            "fixed format, set index=False, or do not include "
                            "the columns containing complex values to "
                            "data_columns when initializing the table."
                        )
                    v.create_index(**kw)
            elif c in self.non_index_axes[0][1]:
                # GH 28156
                raise AttributeError(
                    f"column {c} is not a data_column.\n"
                    f"In order to read column {c} you must reload the dataframe \n"
                    f"into HDFStore and include {c} with the data_columns argument."
                )
```
