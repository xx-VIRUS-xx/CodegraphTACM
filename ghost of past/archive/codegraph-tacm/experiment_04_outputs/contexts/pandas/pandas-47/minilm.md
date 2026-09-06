# pandas-47 :: minilm

query: BUG: assignment to multiple columns when some column do not exist (#29334)

## selected nodes

- rank=1 layer=FUNCTION tokens=311 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._set_no_thousand_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py
- rank=2 layer=FUNCTION tokens=440 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._set_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FUNCTION tokens=390 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.get_new_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=4 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py::HTMLFormatter.row_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py
- rank=5 layer=FUNCTION tokens=505 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._handle_usecols file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py
- rank=6 layer=FUNCTION tokens=382 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._do_select_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=7 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._validate_usecols_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=8 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::bool_frame_with_na file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py
- rank=9 layer=FUNCTION tokens=271 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py::PandasColumn.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py
- rank=10 layer=FUNCTION tokens=914 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py::StylerRenderer._generate_col_header_row file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py
- rank=11 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter.has_mi_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py
- rank=12 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.result_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._set_no_thousand_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py]
    def _set_no_thousand_columns(self) -> set[int]:
        no_thousands_columns: set[int] = set()
        if self.columns and self.parse_dates:
            assert self._col_indices is not None
            no_thousands_columns = self._set_noconvert_dtype_columns(
                self._col_indices, self.columns
            )
        if self.columns and self.dtype:
            assert self._col_indices is not None
            for i, col in zip(self._col_indices, self.columns, strict=True):
                if not isinstance(self.dtype, dict) and not is_numeric_dtype(
                    self.dtype
                ):
                    no_thousands_columns.add(i)
                if (
                    isinstance(self.dtype, dict)
                    and col in self.dtype
                    and (
                        not is_numeric_dtype(self.dtype[col])
                        or is_bool_dtype(self.dtype[col])
                    )
                ):
                    no_thousands_columns.add(i)
        return no_thousands_columns

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._set_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def _set_value(
        self, index: IndexLabel, col, value: Scalar, takeable: bool = False
    ) -> None:
        """
        Put single value at passed column and index.

        Parameters
        ----------
        index : Label
            row label
        col : Label
            column label
        value : scalar
        takeable : bool, default False
            Sets whether or not index/col interpreted as indexers
        """
        try:
            if takeable:
                icol = col
                iindex = cast("int", index)
            else:
                icol = self.columns.get_loc(col)
                iindex = self.index.get_loc(index)  # type: ignore[assignment]
            self._mgr.column_setitem(icol, iindex, value, inplace_only=True)

        except (KeyError, TypeError, ValueError, LossySetitemError):
            # get_loc might raise a KeyError for missing labels (falling back
            #  to (i)loc will do expansion of the index)
            # column_setitem will do validation that may raise TypeError,
            #  ValueError, or LossySetitemError
            # set using a non-recursive method & reset the cache
            if takeable:
                self.iloc[index, col] = value
            else:
                self.loc[index, col] = value

        except InvalidIndexError as ii_err:
            # GH48729: Seems like you are trying to assign a value to a
            # row when only scalar options are permitted
            raise InvalidIndexError(
                f"You can only assign a scalar value not a {type(value)}"
            ) from ii_err

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_Unstacker.get_new_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
    def get_new_columns(self, value_columns: Index | None):
        if value_columns is None:
            if not self.has_nan:
                return self.removed_level._rename(name=self.removed_name)

            lev = self.removed_level.insert(0, item=self.removed_level._na_value)
            return lev.rename(self.removed_name)

        stride = len(self.removed_level) + self.has_nan
        width = len(value_columns)
        propagator = np.repeat(np.arange(width), stride)

        new_levels: FrozenList | list[Index]

        if isinstance(value_columns, MultiIndex):
            new_levels = value_columns.levels + (self.removed_level_full,)  # pyright: ignore[reportOperatorIssue] # noqa: RUF005
            new_names = value_columns.names + (self.removed_name,)  # noqa: RUF005

            new_codes = [lab.take(propagator) for lab in value_columns.codes]
        else:
            new_levels = [
                value_columns,
                self.removed_level_full,
            ]
            new_names = [value_columns.name, self.removed_name]
            new_codes = [propagator]

        repeater = self._repeater

        # The entire level is then just a repetition of the single chunk:
        new_codes.append(np.tile(repeater, width))
        return MultiIndex(
            levels=new_levels, codes=new_codes, names=new_names, verify_integrity=False
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py::HTMLFormatter.row_levels [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py]
    def row_levels(self) -> int:
        if self.fmt.index:
            # showing (row) index
            return self.frame.index.nlevels
        elif self.show_col_idx_names:
            # see gh-22579
            # Column misalignment also occurs for
            # a standard index when the columns index is named.
            # If the row index is not displayed a column of
            # blank cells need to be included before the DataFrame values.
            return 1
        # not showing (row) index
        return 0

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._handle_usecols [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py]
    def _handle_usecols(
        self,
        columns: list[list[Scalar | None]],
        usecols_key: list[Scalar | None],
        num_original_columns: int,
    ) -> list[list[Scalar | None]]:
        """
        Sets self._col_indices

        usecols_key is used if there are string usecols.
        """
        col_indices: set[int] | list[int]
        if self.usecols is not None:
            if callable(self.usecols):
                col_indices = evaluate_callable_usecols(self.usecols, usecols_key)
            elif any(isinstance(u, str) for u in self.usecols):
                if len(columns) > 1:
                    raise ValueError(
                        "If using multiple headers, usecols must be integers."
                    )
                col_indices = []

                for col in self.usecols:
                    if isinstance(col, str):
                        try:
                            col_indices.append(usecols_key.index(col))
                        except ValueError:
                            self._validate_usecols_names(self.usecols, usecols_key)
                    else:
                        col_indices.append(col)
            else:
                missing_usecols = [
                    col for col in self.usecols if col >= num_original_columns
                ]
                if missing_usecols:
                    raise ParserError(
                        "Defining usecols with out-of-bounds indices is not allowed. "
                        f"{missing_usecols} are out-of-bounds.",
                    )
                col_indices = self.usecols

            columns = [
                [n for i, n in enumerate(column) if i in col_indices]
                for column in columns
            ]
            self._col_indices = sorted(col_indices)
        return columns

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._validate_usecols_names [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py]
    def _validate_usecols_names(self, usecols: SequenceT, names: Sequence) -> SequenceT:
        """
        Validates that all usecols are present in a given
        list of names. If not, raise a ValueError that
        shows what usecols are missing.

        Parameters
        ----------
        usecols : iterable of usecols
            The columns to validate are present in names.
        names : iterable of names
            The column names to check against.

        Returns
        -------
        usecols : iterable of usecols
            The `usecols` parameter if the validation succeeds.

        Raises
        ------
        ValueError : Columns were missing. Error message will list them.
        """
        missing = [c for c in usecols if c not in names]
        if len(missing) > 0:
            raise ValueError(
                f"Usecols do not match columns, columns expected but not found: "
                f"{missing}"
            )

        return usecols

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::bool_frame_with_na [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py]
def bool_frame_with_na():
    """
    Fixture for DataFrame of booleans with index of unique strings

    Columns are ['A', 'B', 'C', 'D']; some entries are missing
    """
    df = DataFrame(
        np.concatenate(
            [np.ones((15, 4), dtype=bool), np.zeros((15, 4), dtype=bool)], axis=0
        ),
        index=Index([f"foo_{i}" for i in range(30)], dtype=object),
        columns=Index(list("ABCD"), dtype=object),
        dtype=object,
    )
    # set some NAs
    df.iloc[5:10] = np.nan
    df.iloc[15:20, -2:] = np.nan
    return df

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py::PandasColumn.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py]
    def __init__(self, column: pd.Series, allow_copy: bool = True) -> None:
        """
        Note: doesn't deal with extension arrays yet, just assume a regular
        Series/ndarray for now.
        """
        if isinstance(column, pd.DataFrame):
            raise TypeError(
                "Expected a Series, got a DataFrame. This likely happened "
                "because you called __dataframe__ on a DataFrame which, "
                "after converting column names to string, resulted in duplicated "
                f"names: {column.columns}. Please rename these columns before "
                "using the interchange protocol."
            )
        if not isinstance(column, pd.Series):
            raise NotImplementedError(f"Columns of type {type(column)} not handled yet")

        # Store the column as a private attribute
        self._col = column
        self._allow_copy = allow_copy

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py::StylerRenderer._generate_col_header_row [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py]
    def _generate_col_header_row(
        self, iter: Sequence, max_cols: int, col_lengths: dict
    ):
        """
        Generate the row containing column headers:

         +----------------------------+---------------+---------------------------+
         |  index_blanks ...          | column_name_i |  column_headers (level_i) |
         +----------------------------+---------------+---------------------------+

        Parameters
        ----------
        iter : tuple
            Looping variables from outer scope
        max_cols : int
            Permissible number of columns
        col_lengths :
            c

        Returns
        -------
        list of elements
        """

        r, clabels = iter

        # number of index blanks is governed by number of hidden index levels
        index_blanks = [
            _element("th", self.css["blank"], self.css["blank_value"], True)
        ] * (self.index.nlevels - sum(self.hide_index_) - 1)

        name = self.data.columns.names[r]

        is_display = name is not None and not self.hide_column_names
        value = name if is_display else self.css["blank_value"]
        display_value = (
            self._display_funcs_column_names[r](value) if is_display else None
        )
        column_name = [
            _element(
                "th",
                (
                    f"{self.css['blank']} {self.css['level']}{r}"
                    if name is None
                    else f"{self.css['index_name']} {self.css['level']}{r}"
                ),
                value,
                not all(self.hide_index_),
                display_value=display_value,
            )
        ]

        column_headers: list = []
        visible_col_count: int = 0
        for c, value in enumerate(clabels[r]):
            header_element_visible = _is_visible(c, r, col_lengths)
            if header_element_visible:
                visible_col_count += col_lengths.get((r, c), 0)
            if self._check_trim(
                visible_col_count,
                max_cols,
                column_headers,
                "th",
                f"{self.css['col_heading']} {self.css['level']}{r} "
                f"{self.css['col_trim']}",
            ):
                break

            header_element = _element(
                "th",
                (
                    f"{self.css['col_heading']} {self.css['level']}{r} "
                    f"{self.css['col']}{c}"
                ),
                value,
                header_element_visible,
                display_value=self._display_funcs_columns[(r, c)](value),
                attributes=(
                    f'colspan="{col_lengths.get((r, c), 0)}"'
                    if col_lengths.get((r, c), 0) > 1
                    else ""
                ),
            )

            if self.cell_ids:
                header_element["id"] = f"{self.css['level']}{r}_{self.css['col']}{c}"
            if (
                header_element_visible
                and (r, c) in self.ctx_columns
                and self.ctx_columns[r, c]
            ):
                header_element["id"] = f"{self.css['level']}{r}_{self.css['col']}{c}"
                self.cellstyle_map_columns[tuple(self.ctx_columns[r, c])].append(
                    f"{self.css['level']}{r}_{self.css['col']}{c}"
                )

            column_headers.append(header_element)

        return index_blanks + column_name + column_headers

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py::CSVFormatter.has_mi_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/csvs.py]
    def has_mi_columns(self) -> bool:
        return bool(isinstance(self.obj.columns, ABCMultiIndex))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.result_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def result_columns(self) -> Index:
        pass
```
