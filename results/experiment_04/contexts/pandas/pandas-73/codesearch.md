# pandas-73 :: codesearch

query: BUG: DataFrame.floordiv(ser, axis=0) not matching column-wise bheavior (#31271)

## selected nodes

- rank=1 layer=FUNCTION tokens=868 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.floordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=2 layer=FUNCTION tokens=867 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.rfloordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FUNCTION tokens=1530 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.dropna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=FUNCTION tokens=309 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/executor.py::nb_looper file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/executor.py
- rank=5 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/roperator.py::rfloordiv file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/roperator.py
- rank=6 layer=FUNCTION tokens=229 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/tools.py::table file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/tools.py
- rank=7 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py::df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py
- rank=8 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newPosInf file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.dropna [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def dropna(
        self,
        *,
        axis: Axis = 0,
        how: AnyAll | lib.NoDefault = lib.no_default,
        thresh: int | lib.NoDefault = lib.no_default,
        subset: IndexLabel | AnyArrayLike | None = None,
        inplace: bool = False,
        ignore_index: bool = False,
    ) -> DataFrame | None:
        """
        Remove missing values.

        See the :ref:`User Guide <missing_data>` for more on which values are
        considered missing, and how to work with missing data.

        Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns'}, default 0
            Determine if rows or columns which contain missing values are
            removed.

            * 0, or 'index' : Drop rows which contain missing values.
            * 1, or 'columns' : Drop columns which contain missing value.

            Only a single axis is allowed.

        how : {'any', 'all'}, default 'any'
            Determine if row or column is removed from DataFrame, when we have
            at least one NA or all NA.

            * 'any' : If any NA values are present, drop that row or column.
            * 'all' : If all values are NA, drop that row or column.

        thresh : int, optional
            Require that many non-NA values. Cannot be combined with how.
        subset : column label or iterable of labels, optional
            Labels along other axis to consider, e.g. if you are dropping rows
            these would be a list of columns to include.
        inplace : bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        ignore_index : bool, default ``False``
            If ``True``, the resulting axis will be labeled 0, 1, …, n - 1.

            .. versionadded:: 2.0.0

        Returns
        -------
        DataFrame or None
            DataFrame with NA entries dropped from it or None if ``inplace=True``.

        See Also
        --------
        DataFrame.isna: Indicate missing values.
        DataFrame.notna : Indicate existing (non-missing) values.
        DataFrame.fillna : Replace missing values.
        Series.dropna : Drop missing values.
        Index.dropna : Drop missing indices.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "name": ["Alfred", "Batman", "Catwoman"],
        ...         "toy": [np.nan, "Batmobile", "Bullwhip"],
        ...         "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
        ...     }
        ... )
        >>> df
               name        toy       born
        0    Alfred        NaN        NaT
        1    Batman  Batmobile 1940-04-25
        2  Catwoman   Bullwhip        NaT

        Drop the rows where at least one element is missing.

        >>> df.dropna()
             name        toy       born
        1  Batman  Batmobile 1940-04-25

        Drop the columns where at least one element is missing.

        >>> df.dropna(axis="columns")
               name
        0    Alfred
        1    Batman
        2  Catwoman

        Drop the rows where all elements are missing.

        >>> df.dropna(how="all")
               name        toy       born
        0    Alfred        NaN        NaT
        1    Batman  Batmobile 1940-04-25
        2  Catwoman   Bullwhip        NaT

        Keep only the rows with at least 2 non-NA values.

        >>> df.dropna(thresh=2)
               name        toy       born
        1    Batman  Batmobile 1940-04-25
        2  Catwoman   Bullwhip        NaT

        Define in which columns to look for missing values.

        >>> df.dropna(subset=["name", "toy"])
               name        toy       born
        1    Batman  Batmobile 1940-04-25
        2  Catwoman   Bullwhip        NaT
        """
        if (how is not lib.no_default) and (thresh is not lib.no_default):
            raise TypeError(
                "You cannot set both the how and thresh arguments at the same time."
            )

        if how is lib.no_default:
            how = "any"

        inplace = validate_bool_kwarg(inplace, "inplace")
        if isinstance(axis, (tuple, list)):
            # GH20987
            raise TypeError("supplying multiple axes to axis is no longer supported.")

        axis = self._get_axis_number(axis)
        agg_axis = 1 - axis

        agg_obj = self
        if subset is not None:
            # subset needs to be list
            if not is_list_like(subset):
                subset = [cast("Hashable", subset)]
            ax = self._get_axis(agg_axis)
            indices = ax.get_indexer_for(subset)  # type: ignore[arg-type]
            check = indices == -1
            if check.any():
                raise KeyError(np.array(subset)[check].tolist())
            agg_obj = self.take(indices, axis=agg_axis)

        if thresh is not lib.no_default:
            count = agg_obj.count(axis=agg_axis)
            mask = count >= thresh
        elif how == "any":
            # faster equivalent to 'agg_obj.count(agg_axis) == self.shape[agg_axis]'
            notna_obj = notna(agg_obj)
            if agg_axis == 1:
                # Cast to bool to avoid slow EA groupby fallback (GH#60179)
                notna_obj = notna_obj.astype(bool)
            mask = notna_obj.all(axis=agg_axis, bool_only=False)
        elif how == "all":
            # faster equivalent to 'agg_obj.count(agg_axis) > 0'
            notna_obj = notna(agg_obj)
            if agg_axis == 1:
                notna_obj = notna_obj.astype(bool)
            mask = notna_obj.any(axis=agg_axis, bool_only=False)
        else:
            raise ValueError(f"invalid how option: {how}")

        if np.all(mask):
            result = self.copy(deep=False)
        else:
            result = self.loc(axis=axis)[mask]

        if ignore_index:
            result.index = default_index(len(result))

        if not inplace:
            return result
        self._update_inplace(result)
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/executor.py::nb_looper [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/executor.py]
    def nb_looper(values, axis, *args):
        # Operate on the first row/col in order to get
        # the output shape
        if axis == 0:
            first_elem = values[:, 0]
            dim0 = values.shape[1]
        else:
            first_elem = values[0]
            dim0 = values.shape[0]
        res0 = nb_compat_func(first_elem, *args)
        # Use np.asarray to get shape for
        # https://github.com/numba/numba/issues/4202#issuecomment-1185981507
        # Use tuple concatenation; numba doesn't support tuple unpacking syntax
        buf_shape = (dim0,) + np.atleast_1d(np.asarray(res0)).shape  # noqa: RUF005
        if axis == 0:
            buf_shape = buf_shape[::-1]
        buff = np.empty(buf_shape)

        if axis == 1:
            buff[0] = res0
            for i in numba.prange(1, values.shape[0]):
                buff[i] = nb_compat_func(values[i], *args)
        else:
            buff[:, 0] = res0
            for j in numba.prange(1, values.shape[1]):
                buff[:, j] = nb_compat_func(values[:, j], *args)
        return buff

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/roperator.py::rfloordiv [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/roperator.py]
def rfloordiv(left, right):
    return right // left

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/tools.py::table [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/tools.py]
def table(
    ax, data: DataFrame | Series, rowLabels=None, colLabels=None, **kwargs
) -> Table:
    if isinstance(data, ABCSeries):
        data = data.to_frame()
    elif isinstance(data, ABCDataFrame):
        pass
    else:
        raise ValueError("Input data must be DataFrame or Series")

    if rowLabels is None:
        rowLabels = data.index

    if colLabels is None:
        colLabels = data.columns

    cellText = data.values

    # error: Argument "cellText" to "table" has incompatible type "ndarray[Any,
    # Any]"; expected "Sequence[Sequence[str]] | None"
    return mpl.table.table(
        ax,
        cellText=cellText,  # type: ignore[arg-type]
        rowLabels=rowLabels,
        colLabels=colLabels,
        **kwargs,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py::df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py]
def df(vals, cols):
    return DataFrame(vals, columns=cols)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newPosInf [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newPosInf(void *Py_UNUSED(prv)) {
  return PyFloat_FromDouble(Py_HUGE_VAL);
}
```
