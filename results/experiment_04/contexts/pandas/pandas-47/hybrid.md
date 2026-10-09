# pandas-47 :: hybrid

query: BUG: assignment to multiple columns when some column do not exist (#29334)

## selected nodes

- rank=1 layer=FUNCTION tokens=440 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._set_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=2 layer=FUNCTION tokens=382 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py::StataReader._do_select_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/stata.py
- rank=3 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py::HTMLFormatter.row_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py
- rank=4 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py::ParserBase._validate_usecols_names file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/base_parser.py
- rank=5 layer=FUNCTION tokens=271 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py::PandasColumn.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/column.py
- rank=6 layer=FUNCTION tokens=584 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._setitem_with_indexer_frame_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=7 layer=FUNCTION tokens=505 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._handle_usecols file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py
- rank=8 layer=FUNCTION tokens=727 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._set_item_frame_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=9 layer=FUNCTION tokens=451 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::stack_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=10 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::float_frame_with_na file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._setitem_with_indexer_frame_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _setitem_with_indexer_frame_value(
        self, indexer, value: DataFrame, name: str
    ) -> None:
        ilocs = self._ensure_iterable_column_indexer(indexer[1])

        sub_indexer = list(indexer)
        pi = indexer[0]

        multiindex_indexer = isinstance(self.obj.columns, MultiIndex)

        unique_cols = value.columns.is_unique

        # We do not want to align the value in case of iloc GH#37728
        if name == "iloc":
            for i, loc in enumerate(ilocs):
                val = value.iloc[:, i]
                self._setitem_single_column(loc, val, pi)

        elif not unique_cols and value.columns.equals(self.obj.columns):
            # We assume we are already aligned, see
            # test_iloc_setitem_frame_duplicate_columns_multiple_blocks
            for loc in ilocs:
                item = self.obj.columns[loc]
                if item in value:
                    sub_indexer[1] = item
                    val = self._align_series(
                        tuple(sub_indexer),
                        value.iloc[:, loc],
                        multiindex_indexer,
                    )
                else:
                    val = np.nan

                self._setitem_single_column(loc, val, pi)

        elif not unique_cols:
            raise ValueError("Setting with non-unique columns is not allowed.")

        else:
            for loc in ilocs:
                item = self.obj.columns[loc]
                if item in value:
                    sub_indexer[1] = item
                    ser = value[item]
                    val = self._align_series(
                        tuple(sub_indexer),
                        ser,
                        multiindex_indexer,
                    )
                    # If _align_series did not need to reindex, pass the
                    # original Series so that _setitem_single_column can
                    # preserve CoW ref tracking through isetitem.
                    if val is ser._values:
                        val = ser
                else:
                    val = np.nan

                self._setitem_single_column(loc, val, pi)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._set_item_frame_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def _set_item_frame_value(self, key, value: DataFrame) -> None:
        self._ensure_valid_index(value)

        # align columns
        if key in self.columns:
            loc = self.columns.get_loc(key)
            cols = self.columns[loc]
            len_cols = 1 if is_scalar(cols) or isinstance(cols, tuple) else len(cols)
            if len_cols != len(value.columns):
                raise ValueError("Columns must be same length as key")

            # align right-hand-side columns if self.columns
            # is multi-index and self[key] is a sub-frame
            if isinstance(self.columns, MultiIndex) and isinstance(
                loc, (slice, Series, np.ndarray, Index)
            ):
                cols_droplevel = maybe_droplevels(cols, key)
                if (
                    not isinstance(cols_droplevel, MultiIndex)
                    and is_string_dtype(cols_droplevel.dtype)
                    and not cols_droplevel.any()
                ):
                    # if cols_droplevel contains only empty strings,
                    # value.reindex(cols_droplevel, axis=1) would be full of NaNs
                    # see GH#62518 and GH#61841
                    return
                if len(cols_droplevel) and not cols_droplevel.equals(value.columns):
                    value = value.reindex(cols_droplevel, axis=1)

                if not cols_droplevel.equals(cols):
                    # Levels were actually dropped, so we can safely use
                    # key-based indexing without re-entering this method.
                    for col, col_droplevel in zip(cols, cols_droplevel, strict=True):
                        self[col] = value[col_droplevel]
                    return
                # If cols_droplevel == cols (key matched all levels),
                # fall through to positional isetitem to avoid
                # infinite recursion (GH#53498).

            if is_scalar(cols):
                self[cols] = value[value.columns[0]]
                return

            locs: np.ndarray | list
            if isinstance(loc, slice):
                locs = np.arange(loc.start, loc.stop, loc.step)
            elif is_scalar(loc):
                locs = [loc]
            else:
                locs = loc.nonzero()[0]  # type: ignore[union-attr]

            return self.isetitem(locs, value)

        if len(value.columns) > 1:
            raise ValueError(
                "Cannot set a DataFrame with multiple columns to the single "
                f"column {key}"
            )
        elif len(value.columns) == 0:
            raise ValueError(
                f"Cannot set a DataFrame without columns to the column {key}"
            )

        self[key] = value[value.columns[0]]

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::float_frame_with_na [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py]
def float_frame_with_na():
    """
    Fixture for DataFrame of floats with index of unique strings

    Columns are ['A', 'B', 'C', 'D']; some entries are missing
    """
    df = DataFrame(
        np.random.default_rng(2).standard_normal((30, 4)),
        index=Index([f"foo_{i}" for i in range(30)], dtype=object),
        columns=Index(list("ABCD"), dtype=object),
    )
    # set some NAs
    df.iloc[5:10] = np.nan
    df.iloc[15:20, -2:] = np.nan
    return df
```
