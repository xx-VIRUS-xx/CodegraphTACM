# pandas-73 :: hybrid-cs

query: BUG: DataFrame.floordiv(ser, axis=0) not matching column-wise bheavior (#31271)

## selected nodes

- rank=1 layer=FUNCTION tokens=868 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=2 layer=FUNCTION tokens=867 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.rfloordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FUNCTION tokens=875 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.rtruediv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=FUNCTION tokens=1051 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.truediv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FUNCTION tokens=324 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.nunique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.rtruediv [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def rtruediv(
        self, other, axis: Axis = "columns", level=None, fill_value=None
    ) -> DataFrame:
        """
        Get Floating division of dataframe and other, \
        element-wise (binary operator `rtruediv`).

        Equivalent to ``other / dataframe``, but with support to substitute a
        fill_value for missing data in one of the inputs. With reverse version,
        `truediv`.

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

        >>> 1 / df
                     angles   degrees
        circle          inf  0.002778
        triangle   0.333333  0.005556
        rectangle  0.250000  0.002778

        >>> df.rtruediv(1)
                     angles   degrees
        circle          inf  0.002778
        triangle   0.333333  0.005556
        rectangle  0.250000  0.002778

        Divide a list.

        >>> [1, 2] / df
                     angles   degrees
        circle          inf  0.005556
        triangle   0.333333  0.011111
        rectangle  0.250000  0.005556

        >>> df.rtruediv([1, 2], axis='columns')
                     angles   degrees
        circle          inf  0.005556
        triangle   0.333333  0.011111
        rectangle  0.250000  0.005556
        """
        return self._flex_arith_method(
            other, roperator.rtruediv, level=level, fill_value=fill_value, axis=axis
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.truediv [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def truediv(
        self, other, axis: Axis = "columns", level=None, fill_value=None
    ) -> DataFrame:
        """
        Get Floating division of dataframe and other, \
        element-wise (binary operator `truediv`).

        Equivalent to ``dataframe / other``, but with support to substitute a
        fill_value for missing data in one of the inputs. With reverse version,
        `rtruediv`.

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

        >>> df / 2
                   angles  degrees
        circle        0.0    180.0
        triangle      1.5     90.0
        rectangle     2.0    180.0

        >>> df.truediv(2)
                   angles  degrees
        circle        0.0    180.0
        triangle      1.5     90.0
        rectangle     2.0    180.0

        Divide by a list and Series.

        >>> df / [1, 2]
                   angles  degrees
        circle        0.0    180.0
        triangle      3.0     90.0
        rectangle     4.0    180.0

        >>> df.truediv([1, 2], axis='columns')
                   angles  degrees
        circle        0.0    180.0
        triangle      3.0     90.0
        rectangle     4.0    180.0

        >>> df.truediv(pd.Series([1, 2, 3], index=['circle', 'triangle', 'rectangle']),
        ...            axis='index')
                     angles  degrees
        circle     0.000000    360.0
        triangle   1.500000     90.0
        rectangle  1.333333    120.0

        Divide by a dictionary by axis.

        >>> df.truediv({'angles': 2, 'degrees': 3})
                   angles  degrees
        circle        0.0    120.0
        triangle      1.5     60.0
        rectangle     2.0    120.0

        >>> df.truediv({'circle': 1, 'triangle': 2, 'rectangle': 3}, axis='index')
                     angles  degrees
        circle     0.000000    360.0
        triangle   1.500000     90.0
        rectangle  1.333333    120.0
        """
        return self._flex_arith_method(
            other, operator.truediv, level=level, fill_value=fill_value, axis=axis
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.nunique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def nunique(self, axis: Axis = 0, dropna: bool = True) -> Series:
        """
        Count number of distinct elements in specified axis.

        Return Series with number of distinct elements. Can ignore NaN
        values.

        Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns'}, default 0
            The axis to use. 0 or 'index' for row-wise, 1 or 'columns' for
            column-wise.
        dropna : bool, default True
            Don't include NaN in the counts.

        Returns
        -------
        Series
            Series with counts of unique values per row or column, depending on `axis`.

        See Also
        --------
        Series.nunique: Method nunique for Series.
        DataFrame.count: Count non-NA cells for each column or row.

        Examples
        --------
        >>> df = pd.DataFrame({"A": [4, 5, 6], "B": [4, 1, 1]})
        >>> df.nunique()
        A    3
        B    2
        dtype: int64

        >>> df.nunique(axis=1)
        0    1
        1    2
        2    2
        dtype: int64
        """
        return self.apply(Series.nunique, axis=axis, dropna=dropna)
```
