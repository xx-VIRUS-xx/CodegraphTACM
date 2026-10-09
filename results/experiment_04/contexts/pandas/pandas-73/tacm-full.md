# pandas-73 :: tacm-full

query: BUG: DataFrame.floordiv(ser, axis=0) not matching column-wise bheavior (#31271)

## selected nodes

- rank=1 layer=FUNCTION tokens=868 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=2 layer=FUNCTION tokens=595 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=3 layer=FUNCTION tokens=324 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.nunique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._replace_columnwise file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=5 layer=FUNCTION tokens=204 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser._convert_axes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py
- rank=6 layer=FUNCTION tokens=1231 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.ne file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=7 layer=FUNCTION tokens=362 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::StructAccessor.explode file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=8 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::SeriesGroupBy.dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._replace_columnwise [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def _replace_columnwise(
        self, mapping: dict[Hashable, tuple[Any, Any]], inplace: bool, regex
    ) -> Self:
        """
        Dispatch to Series.replace column-wise.

        Parameters
        ----------
        mapping : dict
            of the form {col: (target, value)}
        inplace : bool
        regex : bool or same types as `to_replace` in DataFrame.replace

        Returns
        -------
        DataFrame
        """
        # Operate column-wise
        res = self if inplace else self.copy(deep=False)
        ax = self.columns

        for i, ax_value in enumerate(ax):
            if ax_value in mapping:
                ser = self.iloc[:, i]

                target, value = mapping[ax_value]
                newobj = ser.replace(target, value, regex=regex)

                res._iset_item(i, newobj, inplace=inplace)

        return res if inplace else res.__finalize__(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py::Parser._convert_axes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/json/_json.py]
    def _convert_axes(self, obj: DataFrame | Series) -> DataFrame | Series:
        """
        Try to convert axes.
        """
        for axis_name in obj._AXIS_ORDERS:
            ax = obj._get_axis(axis_name)
            ser = Series(ax, dtype=ax.dtype, copy=False)
            new_ser, result = self._try_convert_data(
                name=axis_name,
                data=ser,
                use_dtypes=False,
                convert_dates=True,
                is_axis=True,
            )
            if result:
                new_axis = Index(new_ser, dtype=new_ser.dtype, copy=False)
                setattr(obj, axis_name, new_axis)
        return obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.ne [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def ne(self, other, axis: Axis = "columns", level=None) -> DataFrame:
        """
        Get Not equal to of dataframe and other, element-wise (binary operator `ne`).

        Among flexible wrappers (`eq`, `ne`, `le`, `lt`, `ge`, `gt`) to comparison
        operators.

        Equivalent to `==`, `!=`, `<=`, `<`, `>=`, `>` with support to choose axis
        (rows or columns) and level for comparison.

        Parameters
        ----------
        other : scalar, sequence, Series, or DataFrame
            Any single or multiple element data structure, or list-like object.
        axis : {0 or 'index', 1 or 'columns'}, default 'columns'
            Whether to compare by the index (0 or 'index') or columns
            (1 or 'columns').
        level : int or label
            Broadcast across a level, matching Index values on the passed
            MultiIndex level.

        Returns
        -------
        DataFrame of bool
            Result of the comparison.

        See Also
        --------
        DataFrame.eq : Compare DataFrames for equality elementwise.
        DataFrame.ne : Compare DataFrames for inequality elementwise.
        DataFrame.le : Compare DataFrames for less than inequality
            or equality elementwise.
        DataFrame.lt : Compare DataFrames for strictly less than
            inequality elementwise.
        DataFrame.ge : Compare DataFrames for greater than inequality
            or equality elementwise.
        DataFrame.gt : Compare DataFrames for strictly greater than
            inequality elementwise.

        Notes
        -----
        Mismatched indices will be unioned together.
        `NaN` values are considered different (i.e. `NaN` != `NaN`).

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {"cost": [250, 150, 100], "revenue": [100, 250, 300]},
        ...     index=["A", "B", "C"],
        ... )
        >>> df
           cost  revenue
        A   250      100
        B   150      250
        C   100      300

        Comparison with a scalar, using either the operator or method:

        >>> df == 100
            cost  revenue
        A  False     True
        B  False    False
        C   True    False

        >>> df.eq(100)
            cost  revenue
        A  False     True
        B  False    False
        C   True    False

        When `other` is a :class:`Series`, the columns of a DataFrame are aligned
        with the index of `other` and broadcast:

        >>> df != pd.Series([100, 250], index=["cost", "revenue"])
            cost  revenue
        A   True     True
        B   True    False
        C  False     True

        Use the method to control the broadcast axis:

        >>> df.ne(pd.Series([100, 300], index=["A", "D"]), axis="index")
           cost  revenue
        A  True    False
        B  True     True
        C  True     True
        D  True     True

        When comparing to an arbitrary sequence, the number of columns must
        match the number elements in `other`:

        >>> df == [250, 100]
            cost  revenue
        A   True     True
        B  False    False
        C  False    False

        Use the method to control the axis:

        >>> df.eq([250, 250, 100], axis="index")
            cost  revenue
        A   True    False
        B  False     True
        C   True    False

        Compare to a DataFrame of different shape.

        >>> other = pd.DataFrame(
        ...     {"revenue": [300, 250, 100, 150]}, index=["A", "B", "C", "D"]
        ... )
        >>> other
           revenue
        A      300
        B      250
        C      100
        D      150

        >>> df.gt(other)
            cost  revenue
        A  False    False
        B  False    False
        C  False     True
        D  False    False

        Compare to a MultiIndex by level.

        >>> df_multindex = pd.DataFrame(
        ...     {
        ...         "cost": [250, 150, 100, 150, 300, 220],
        ...         "revenue": [100, 250, 300, 200, 175, 225],
        ...     },
        ...     index=[
        ...         ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2"],
        ...         ["A", "B", "C", "A", "B", "C"],
        ...     ],
        ... )
        >>> df_multindex
              cost  revenue
        Q1 A   250      100
           B   150      250
           C   100      300
        Q2 A   150      200
           B   300      175
           C   220      225

        >>> df.le(df_multindex, level=1)
               cost  revenue
        Q1 A   True     True
           B   True     True
           C   True     True
        Q2 A  False     True
           B   True    False
           C   True    False
        """
        return self._flex_cmp_method(other, operator.ne, axis=axis, level=level)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::StructAccessor.explode [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py]
    def explode(self) -> DataFrame:
        """
        Extract all child fields of a struct as a DataFrame.

        Each child field of the struct becomes a column in the resulting
        DataFrame, with column names matching the struct field names.

        Returns
        -------
        pandas.DataFrame
            The data corresponding to all child fields.

        See Also
        --------
        Series.struct.field : Return a single child field as a Series.

        Examples
        --------
        >>> import pyarrow as pa
        >>> s = pd.Series(
        ...     [
        ...         {"version": 1, "project": "pandas"},
        ...         {"version": 2, "project": "pandas"},
        ...         {"version": 1, "project": "numpy"},
        ...     ],
        ...     dtype=pd.ArrowDtype(
        ...         pa.struct([("version", pa.int64()), ("project", pa.string())])
        ...     ),
        ... )

        >>> s.struct.explode()
           version project
        0        1  pandas
        1        2  pandas
        2        1   numpy
        """
        from pandas import concat

        pa_type = self._pa_array.type
        return concat(
            [self.field(i) for i in range(pa_type.num_fields)], axis="columns"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::SeriesGroupBy.dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
    def dtype(self) -> Series:
        """
        Return the dtype object of the underlying data for each group.

        Mirrors :meth:`Series.dtype` applied group-wise.

        Returns
        -------
        Series
            Dtype of each group's values.
        """
        return self.apply(lambda ser: ser.dtype)
```
