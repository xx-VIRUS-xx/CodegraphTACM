# pandas-73 :: hybrid

query: BUG: DataFrame.floordiv(ser, axis=0) not matching column-wise bheavior (#31271)

## selected nodes

- rank=1 layer=FUNCTION tokens=868 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=2 layer=FUNCTION tokens=595 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=3 layer=FUNCTION tokens=866 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.rmod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=FUNCTION tokens=867 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.rfloordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FUNCTION tokens=368 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::FrameWithFrameWide.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=6 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py::HTMLFormatter.row_levels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/html.py
- rank=7 layer=FUNCTION tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.axes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=8 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__floordiv__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.rmod [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def rmod(
        self, other, axis: Axis = "columns", level=None, fill_value=None
    ) -> DataFrame:
        """
        Get Modulo of dataframe and other, \
        element-wise (binary operator `rmod`).

        Equivalent to ``other % dataframe``, but with support to substitute a
        fill_value for missing data in one of the inputs. With reverse version,
        `mod`.

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

        Calculate modulo with a scalar.

        >>> 1000 % df
                   angles  degrees
        circle        NaN    280.0
        triangle      1.0    100.0
        rectangle     0.0    280.0

        >>> df.rmod(1000)
                   angles  degrees
        circle        NaN    280.0
        triangle      1.0    100.0
        rectangle     0.0    280.0

        Calculate modulo with a list.

        >>> [1000, 2000] % df
                   angles  degrees
        circle        NaN    200.0
        triangle      1.0     20.0
        rectangle     0.0    200.0

        >>> df.rmod([1000, 2000], axis='columns')
                   angles  degrees
        circle        NaN    200.0
        triangle      1.0     20.0
        rectangle     0.0    200.0
        """
        return self._flex_arith_method(
            other, roperator.rmod, level=level, fill_value=fill_value, axis=axis
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.rfloordiv [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def rfloordiv(
        self, other, axis: Axis = "columns", level=None, fill_value=None
    ) -> DataFrame:
        """
        Get Integer division of dataframe and other, \
        element-wise (binary operator `rfloordiv`).

        Equivalent to ``other // dataframe``, but with support to substitute a
        fill_value for missing data in one of the inputs. With reverse version,
        `floordiv`.

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

        Divide a scalar.

        >>> 10 // df
                   angles  degrees
        circle        inf      0.0
        triangle      3.0      0.0
        rectangle     2.0      0.0

        >>> df.rfloordiv(10)
                   angles  degrees
        circle        inf      0.0
        triangle      3.0      0.0
        rectangle     2.0      0.0

        Divide a list.

        >>> [10, 20] // df
                   angles  degrees
        circle        inf      0.0
        triangle      3.0      0.0
        rectangle     2.0      0.0

        >>> df.rfloordiv([10, 20], axis='columns')
                   angles  degrees
        circle        inf      0.0
        triangle      3.0      0.0
        rectangle     2.0      0.0
        """
        return self._flex_arith_method(
            other, roperator.rfloordiv, level=level, fill_value=fill_value, axis=axis
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.axes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def axes(self) -> list[Index]:
        """
        Return a list representing the axes of the DataFrame.

        It has the row axis labels and column axis labels as the only members.
        They are returned in that order.

        See Also
        --------
        DataFrame.index: The index (row labels) of the DataFrame.
        DataFrame.columns: The column labels of the DataFrame.

        Examples
        --------
        >>> df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        >>> df.axes
        [RangeIndex(start=0, stop=2, step=1), Index(['col1', 'col2'], dtype='str')]
        """
        return [self.index, self.columns]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__floordiv__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py]
    def __floordiv__(self, other):
        return self._arith_method(other, operator.floordiv)
```
