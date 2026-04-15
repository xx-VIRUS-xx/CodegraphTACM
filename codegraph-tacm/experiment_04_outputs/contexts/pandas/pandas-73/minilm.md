# pandas-73 :: minilm

query: BUG: DataFrame.floordiv(ser, axis=0) not matching column-wise bheavior (#31271)

## selected nodes

- rank=1 layer=FUNCTION tokens=868 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=2 layer=FUNCTION tokens=595 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=3 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Ops2.time_frame_float_floor_by_zero file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=4 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py::HTMLFormatter.row_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py
- rank=5 layer=FUNCTION tokens=727 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._set_item_frame_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=6 layer=FUNCTION tokens=630 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Table._get_blocks_and_items file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=7 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::BlockManagerFixed.read file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=8 layer=FUNCTION tokens=368 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::FrameWithFrameWide.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=9 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::df_col file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py
- rank=10 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py::DataFrameFormatter._initialize_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.floordiv [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def floordiv(
        self, other, axis: Axis = "columns", level=None, fill_value=None
    ) -> DataFrame:
        """
        Get Integer division of dataframe and other, \
        element-wise (binary operator `floordiv`).

        Equivalent to ``dataframe // other``, but with support to substitute a
        fill_value for missing data in one of the inputs. With reverse version,
        `rfloordiv`.

        Among flexible wrappers (`add`, `sub`, `mul`, `div`, `floordiv`, `mod`, `pow`)
        to arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`.

        Parameters
        ----------
        other : scalar, sequence, Series, dict or DataFrame
            Any single or multiple element data structure, or list-like object.
        axis : {0 or 'index', 1 or 'columns'}
            Whether to compare by the index (0 or 'index') or columns.
            (1 or 'columns'). For Series input, axis to match Series index on.
        level : int or label
            Broadcast across a level, matching Index values on the
            passed MultiIndex level.
        fill_value : float or None, default None
            Fill existing missing (NaN) values, and any new element needed for
            successful DataFrame alignment, with this value before computation.
            If data in both corresponding DataFrame locations is missing
            the result will be missing.

        Returns
        -------
        DataFrame
            Result of the arithmetic operation.

        See Also
        --------
        DataFrame.add : Add DataFrames.
        DataFrame.sub : Subtract DataFrames.
        DataFrame.mul : Multiply DataFrames.
        DataFrame.div : Divide DataFrames (float division).
        DataFrame.truediv : Divide DataFrames (float division).
        DataFrame.floordiv : Divide DataFrames (integer division).
        DataFrame.mod : Calculate modulo (remainder after division).
        DataFrame.pow : Calculate exponential power.

        Notes
        -----
        Mismatched indices will be unioned together.

        Examples
        --------
        >>> df = pd.DataFrame({'angles': [0, 3, 4],
        ...                    'degrees': [360, 180, 360]},
        ...                   index=['circle', 'triangle', 'rectangle'])
        >>> df
                   angles  degrees
        circle          0      360
        triangle        3      180
        rectangle       4      360

        Divide by a scalar.

        >>> df // 2
                   angles  degrees
        circle          0      180
        triangle        1       90
        rectangle       2      180

        >>> df.floordiv(2)
                   angles  degrees
        circle          0      180
        triangle        1       90
        rectangle       2      180

        Divide by a list and Series.

        >>> df // [1, 2]
                   angles  degrees
        circle          0      180
        triangle        3       90
        rectangle       4      180

        >>> df.floordiv([1, 2], axis='columns')
                   angles  degrees
        circle          0      180
        triangle        3       90
        rectangle       4      180
        """
        return self._flex_arith_method(
            other, operator.floordiv, level=level, fill_value=fill_value, axis=axis
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.floordiv [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def floordiv(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Integer division of series and other, \
        element-wise (binary operator `floordiv`).

        Equivalent to ``series // other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
            will behave the same as ``//`` but with possibly different results due
            to the other arguments.
        level : int or name
            Broadcast across a level, matching Index values on the
            passed MultiIndex level.
        fill_value : None or float value, default None (NaN)
            Fill existing missing (NaN) values, and any new element needed for
            successful Series alignment, with this value before computation.
            If data in both corresponding Series locations is missing
            the result of filling (at that location) will be missing.
        axis : {0 or 'index'}
            Unused. Parameter needed for compatibility with DataFrame.

        Returns
        -------
        Series
            The result of the operation.

        See Also
        --------
        Series.rfloordiv : Reverse of the Integer division operator, see
            `Python documentation
            <https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types>`_
            for more details.

        Examples
        --------
        >>> a = pd.Series([1, 1, 1, np.nan], index=["a", "b", "c", "d"])
        >>> a
        a    1.0
        b    1.0
        c    1.0
        d    NaN
        dtype: float64
        >>> b = pd.Series([1, np.nan, 1, np.nan], index=["a", "b", "d", "e"])
        >>> b
        a    1.0
        b    NaN
        d    1.0
        e    NaN
        dtype: float64
        >>> a.floordiv(b, fill_value=0)
        a    1.0
        b    inf
        c    inf
        d    0.0
        e    NaN
        dtype: float64
        """
        return self._flex_method(
            other, operator.floordiv, level=level, fill_value=fill_value, axis=axis
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::Ops2.time_frame_float_floor_by_zero [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_frame_float_floor_by_zero(self):
        self.df // 0

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::Table._get_blocks_and_items [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def _get_blocks_and_items(
        frame: DataFrame,
        table_exists: bool,
        new_non_index_axes,
        values_axes,
        data_columns,
    ):
        # Helper to clarify non-state-altering parts of _create_axes
        def get_blk_items(mgr):
            return [mgr.items.take(blk.mgr_locs) for blk in mgr.blocks]

        mgr = frame._mgr
        blocks: list[Block] = list(mgr.blocks)
        blk_items: list[Index] = get_blk_items(mgr)

        if len(data_columns):
            # TODO: prove that we only get here with axis == 1?
            #  It is the case in all extant tests, but NOT the case
            #  outside this `if len(data_columns)` check.

            axis, axis_labels = new_non_index_axes[0]
            new_labels = Index(axis_labels).difference(Index(data_columns))
            mgr = frame.reindex(new_labels, axis=axis)._mgr

            blocks = list(mgr.blocks)
            blk_items = get_blk_items(mgr)
            for c in data_columns:
                # This reindex would raise ValueError if we had a duplicate
                #  index, so we can infer that (as long as axis==1) we
                #  get a single column back, so a single block.
                mgr = frame.reindex([c], axis=axis)._mgr
                blocks.extend(mgr.blocks)
                blk_items.extend(get_blk_items(mgr))

        # reorder the blocks in the same order as the existing table if we can
        if table_exists:
            by_items = {
                tuple(b_items.tolist()): (b, b_items)
                for b, b_items in zip(blocks, blk_items, strict=True)
            }
            new_blocks: list[Block] = []
            new_blk_items = []
            for ea in values_axes:
                items = tuple(ea.values)
                try:
                    b, b_items = by_items.pop(items)
                    new_blocks.append(b)
                    new_blk_items.append(b_items)
                except (IndexError, KeyError) as err:
                    jitems = ",".join([pprint_thing(item) for item in items])
                    raise ValueError(
                        f"cannot match existing table structure for [{jitems}] "
                        "on appending data"
                    ) from err
            blocks = new_blocks
            blk_items = new_blk_items

        return blocks, blk_items

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::BlockManagerFixed.read [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py]
    def read(
        self,
        where=None,
        columns=None,
        start: int | None = None,
        stop: int | None = None,
    ) -> DataFrame:
        # start, stop applied to rows, so 0th axis only
        self.validate_read(columns, where)
        select_axis = self.obj_type()._get_block_manager_axis(0)

        axes = []
        for i in range(self.ndim):
            _start, _stop = (start, stop) if i == select_axis else (None, None)
            ax = self.read_index(f"axis{i}", start=_start, stop=_stop)
            axes.append(ax)

        items = axes[0]
        dfs = []

        for i in range(self.nblocks):
            blk_items = self.read_index(f"block{i}_items")
            values = self.read_array(f"block{i}_values", start=_start, stop=_stop)

            columns = items[items.get_indexer(blk_items)]
            df = DataFrame(values.T, columns=columns, index=axes[1], copy=False)
            if (
                using_string_dtype()
                and isinstance(values, np.ndarray)
                and is_string_array(values, skipna=True)
            ):
                df = df.astype(StringDtype(na_value=np.nan))
            dfs.append(df)

        if len(dfs) > 0:
            out = concat(dfs, axis=1).copy()
            return out.reindex(columns=items)

        return DataFrame(columns=axes[0], index=axes[1])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::FrameWithFrameWide.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def setup(self, op, shape):
        # we choose dtypes so as to make the blocks
        #  a) not perfectly match between right and left
        #  b) appreciably bigger than single columns
        n_rows, n_cols = shape

        if op is operator.floordiv:
            # floordiv is much slower than the other operations -> use less data
            n_rows = n_rows // 10

        # construct dataframe with 2 blocks
        arr1 = np.random.randn(n_rows, n_cols // 2).astype("f8")
        arr2 = np.random.randn(n_rows, n_cols // 2).astype("f4")
        df = pd.concat([DataFrame(arr1), DataFrame(arr2)], axis=1, ignore_index=True)
        # should already be the case, but just to be sure
        df._consolidate_inplace()

        # TODO: GH#33198 the setting here shouldn't need two steps
        arr1 = np.random.randn(n_rows, max(n_cols // 4, 3)).astype("f8")
        arr2 = np.random.randn(n_rows, n_cols // 2).astype("i8")
        arr3 = np.random.randn(n_rows, n_cols // 4).astype("f8")
        df2 = pd.concat(
            [DataFrame(arr1), DataFrame(arr2), DataFrame(arr3)],
            axis=1,
            ignore_index=True,
        )
        # should already be the case, but just to be sure
        df2._consolidate_inplace()

        self.left = df
        self.right = df2

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::df_col [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py]
def df_col(df):
    return df.reset_index()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py::DataFrameFormatter._initialize_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py]
    def _initialize_columns(self, columns: Axes | None) -> Index:
        if columns is not None:
            cols = ensure_index(columns)
            self.frame = self.frame[cols]
            return cols
        else:
            return self.frame.columns
```
