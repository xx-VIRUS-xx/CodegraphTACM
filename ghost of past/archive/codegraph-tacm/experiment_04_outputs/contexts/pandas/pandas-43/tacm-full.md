# pandas-43 :: tacm-full

query: BUG: arithmetic with reindex pow (#32734)

## selected nodes

- rank=1 layer=FUNCTION tokens=384 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._add_arithmetic_ops file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=2 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__pow__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py
- rank=3 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=4 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__pow__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=5 layer=FUNCTION tokens=514 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._arith_method_with_reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=6 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=7 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_with_cache file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=8 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._inplace_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=9 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._validate_can_reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=10 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::all_arithmetic_functions file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=11 layer=FUNCTION tokens=588 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.pow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=12 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._needs_reindex_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=13 layer=FUNCTION tokens=869 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=14 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::all_arithmetic_operators file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=15 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py::reindex_helper file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py
- rank=16 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._add_arithmetic_ops [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def _add_arithmetic_ops(cls) -> None:
        setattr(cls, "__add__", cls._create_arithmetic_method(operator.add))
        setattr(cls, "__radd__", cls._create_arithmetic_method(roperator.radd))
        setattr(cls, "__sub__", cls._create_arithmetic_method(operator.sub))
        setattr(cls, "__rsub__", cls._create_arithmetic_method(roperator.rsub))
        setattr(cls, "__mul__", cls._create_arithmetic_method(operator.mul))
        setattr(cls, "__rmul__", cls._create_arithmetic_method(roperator.rmul))
        setattr(cls, "__pow__", cls._create_arithmetic_method(operator.pow))
        setattr(cls, "__rpow__", cls._create_arithmetic_method(roperator.rpow))
        setattr(cls, "__mod__", cls._create_arithmetic_method(operator.mod))
        setattr(cls, "__rmod__", cls._create_arithmetic_method(roperator.rmod))
        setattr(cls, "__floordiv__", cls._create_arithmetic_method(operator.floordiv))
        setattr(
            cls, "__rfloordiv__", cls._create_arithmetic_method(roperator.rfloordiv)
        )
        setattr(cls, "__truediv__", cls._create_arithmetic_method(operator.truediv))
        setattr(cls, "__rtruediv__", cls._create_arithmetic_method(roperator.rtruediv))
        setattr(cls, "__divmod__", cls._create_arithmetic_method(divmod))
        setattr(cls, "__rdivmod__", cls._create_arithmetic_method(roperator.rdivmod))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__pow__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py]
    def __pow__(self, other: Any) -> Expression:
        self_repr, other_repr = self._maybe_wrap_parentheses(other)
        return self._with_op("__pow__", other, f"{self_repr} ** {other_repr}")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py]
    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.
        StringMethods.len : Compute the length of each element in the Series/Index.

        Examples
        --------
        >>> import pyarrow as pa
        >>> s = pd.Series(
        ...     [
        ...         [1, 2, 3],
        ...         [3],
        ...     ],
        ...     dtype=pd.ArrowDtype(pa.list_(pa.int64())),
        ... )
        >>> s.list.len()
        0    3
        1    1
        dtype: int32[pyarrow]
        """
        from pandas import Series

        value_lengths = pc.list_value_length(self._pa_array)
        return Series(
            value_lengths,
            dtype=ArrowDtype(value_lengths.type),
            index=self._data.index,
            name=self._data.name,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__pow__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py]
    def __pow__(self, other):
        return self._arith_method(other, operator.pow)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._arith_method_with_reindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def _arith_method_with_reindex(self, right: DataFrame, op) -> DataFrame:
        """
        For DataFrame-with-DataFrame operations that require reindexing,
        operate only on shared columns, then reindex.

        Parameters
        ----------
        right : DataFrame
        op : binary operator

        Returns
        -------
        DataFrame
        """
        left = self

        # GH#31623, only operate on shared columns
        cols, lcol_indexer, rcol_indexer = left.columns.join(
            right.columns, how="inner", return_indexers=True
        )

        new_left = left if lcol_indexer is None else left.iloc[:, lcol_indexer]
        new_right = right if rcol_indexer is None else right.iloc[:, rcol_indexer]

        # GH#60498 For MultiIndex column alignment
        if isinstance(cols, MultiIndex):
            # When overwriting column names, make a shallow copy so as to not modify
            # the input DFs
            new_left = new_left.copy(deep=False)
            new_right = new_right.copy(deep=False)
            new_left.columns = cols
            new_right.columns = cols

        result = op(new_left, new_right)

        # Do the join on the columns instead of using left._align_for_op
        #  to avoid constructing two potentially large/sparse DataFrames
        join_columns = left.columns.join(right.columns, how="outer")

        if result.columns.has_duplicates:
            # Avoid reindexing with a duplicate axis.
            # https://github.com/pandas-dev/pandas/issues/35194
            indexer, _ = result.columns.get_indexer_non_unique(join_columns)
            indexer = algorithms.unique1d(indexer)
            result = result._reindex_with_indexers(
                {1: [join_columns, indexer]}, allow_dups=True
            )
        else:
            result = result.reindex(join_columns, axis=1)

        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py]
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

        See Also
        --------
        str.len : Python built-in function returning the length of an object.
        Series.size : Returns the length of the Series.

        Examples
        --------
        Returns the length (number of characters) in a string. Returns the
        number of entries for dictionaries, lists or tuples.

        >>> s = pd.Series(
        ...     ["dog", "", 5, {"foo": "bar"}, [2, 3, 5, 7], ("one", "two", "three")]
        ... )
        >>> s
        0                  dog
        1
        2                    5
        3       {'foo': 'bar'}
        4         [2, 3, 5, 7]
        5    (one, two, three)
        dtype: object
        >>> s.str.len()
        0    3.0
        1    0.0
        2    NaN
        3    1.0
        4    4.0
        5    3.0
        dtype: float64
        """
        result = self._data.array._str_len()
        return self._wrap_result(result, returns_string=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_with_cache [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_reindex_multiindex_with_cache(self):
        # MultiIndex._values gets cached
        self.s.reindex(self.s_subset.index)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._inplace_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def _inplace_method(self, other, op) -> Self:
        """
        Wrap arithmetic method to operate inplace.
        """
        result = op(self, other)

        # this makes sure that we are aligned like the input
        # we are updating inplace
        self._update_inplace(result.reindex_like(self))
        return self

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._validate_can_reindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _validate_can_reindex(self, indexer: np.ndarray) -> None:
        """
        Check if we are allowing reindexing with this particular indexer.

        Parameters
        ----------
        indexer : an integer ndarray

        Raises
        ------
        ValueError if its a duplicate axis
        """
        # trying to reindex on an axis with duplicates
        if not self._index_as_unique and len(indexer):
            raise ValueError("cannot reindex on an axis with duplicate labels")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::all_arithmetic_functions [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def all_arithmetic_functions(request):
    """
    Fixture for operator and roperator arithmetic functions.

    Notes
    -----
    This includes divmod and rdivmod, whereas all_arithmetic_operators
    does not.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.pow [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def pow(self, other, level=None, fill_value=None, axis: Axis = 0) -> Series:
        """
        Return Exponential power of series and other, \
        element-wise (binary operator `pow`).

        Equivalent to ``series ** other``, but with support to substitute a
        fill_value for missing data in either one of the inputs.

        Parameters
        ----------
        other : object
            When a Series is provided, will align on indexes. For all other types,
            will behave the same as ``**`` but with possibly different results due
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
        Series.rpow : Reverse of the Exponential power operator, see
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
        >>> a.pow(b, fill_value=0)
        a    1.0
        b    1.0
        c    1.0
        d    0.0
        e    NaN
        dtype: float64
        """
        return self._flex_method(
            other, operator.pow, level=level, fill_value=fill_value, axis=axis
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._needs_reindex_multi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _needs_reindex_multi(self, axes, method, level) -> bool:
        """
        Check if we do need a multi reindex; this is for compat with
        higher dims.
        """
        return False

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pow [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def pow(
        self, other, axis: Axis = "columns", level=None, fill_value=None
    ) -> DataFrame:
        """
        Get Exponential power of dataframe and other, \
        element-wise (binary operator `pow`).

        Equivalent to ``dataframe ** other``, but with support to substitute a
        fill_value for missing data in one of the inputs. With reverse version,
        `rpow`.

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

        Calculate exponential power with a scalar.

        >>> df ** 2
                   angles  degrees
        circle          0   129600
        triangle        9    32400
        rectangle      16   129600

        >>> df.pow(2)
                   angles  degrees
        circle          0   129600
        triangle        9    32400
        rectangle      16   129600

        Calculate exponential power with a list.

        >>> df ** [1, 2]
                   angles  degrees
        circle          0   129600
        triangle        3    32400
        rectangle       4   129600

        >>> df.pow([1, 2], axis='columns')
                   angles  degrees
        circle          0   129600
        triangle        3    32400
        rectangle       4   129600
        """
        return self._flex_arith_method(
            other, operator.pow, level=level, fill_value=fill_value, axis=axis
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::all_arithmetic_operators [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def all_arithmetic_operators(request):
    """
    Fixture for dunder names for common arithmetic operations.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py::reindex_helper [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py]
    def reindex_helper(x):
        return x.reindex(np.arange(x.index.min(), x.index.max() + 1))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_reindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_reindex(self):
        self.index.reindex(self.index[:500])
```
