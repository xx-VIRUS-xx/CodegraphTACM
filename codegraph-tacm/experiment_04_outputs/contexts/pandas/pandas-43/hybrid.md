# pandas-43 :: hybrid

query: BUG: arithmetic with reindex pow (#32734)

## selected nodes

- rank=1 layer=FUNCTION tokens=384 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._add_arithmetic_ops file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=2 layer=FUNCTION tokens=869 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__pow__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=4 layer=FUNCTION tokens=588 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.pow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=5 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._inplace_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=6 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__pow__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py
- rank=7 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._needs_reindex_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=8 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._create_arithmetic_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=9 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionScalarOpsMixin._create_arithmetic_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=10 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::all_arithmetic_functions file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=11 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_with_cache file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=12 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py::reindex_helper file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py
- rank=13 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/sparse/test_arithmetics.py::TestSparseArrayArithmetics._check_numeric_ops file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
- rank=14 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._reindex_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=15 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._validate_can_reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=16 layer=FUNCTION tokens=704 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._arith_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=17 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._needs_reindex_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=18 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/conftest.py::arithmetic_win_operators file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/conftest.py
- rank=19 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py::TestPivotTable.ret_sum file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__pow__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py]
    def __pow__(self, other):
        return self._arith_method(other, operator.pow)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__pow__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py]
    def __pow__(self, other: Any) -> Expression:
        self_repr, other_repr = self._maybe_wrap_parentheses(other)
        return self._with_op("__pow__", other, f"{self_repr} ** {other_repr}")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._needs_reindex_multi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _needs_reindex_multi(self, axes, method, level) -> bool:
        """
        Check if we do need a multi reindex; this is for compat with
        higher dims.
        """
        return False

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._create_arithmetic_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def _create_arithmetic_method(cls, op):
        raise AbstractMethodError(cls)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionScalarOpsMixin._create_arithmetic_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def _create_arithmetic_method(cls, op):
        return cls._create_method(op)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_with_cache [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_reindex_multiindex_with_cache(self):
        # MultiIndex._values gets cached
        self.s.reindex(self.s_subset.index)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py::reindex_helper [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py]
    def reindex_helper(x):
        return x.reindex(np.arange(x.index.min(), x.index.max() + 1))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/sparse/test_arithmetics.py::TestSparseArrayArithmetics._check_numeric_ops [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/sparse/test_arithmetics.py]
    def _check_numeric_ops(self, a, b, a_dense, b_dense, mix: bool, op):
        # Check that arithmetic behavior matches non-Sparse Series arithmetic

        if isinstance(a_dense, np.ndarray):
            expected = op(pd.Series(a_dense), b_dense).values
        elif isinstance(b_dense, np.ndarray):
            expected = op(a_dense, pd.Series(b_dense)).values
        else:
            raise NotImplementedError

        with np.errstate(invalid="ignore", divide="ignore"):
            if mix:
                result = op(a, b_dense).to_dense()
            else:
                result = op(a, b).to_dense()

        self._assert(result, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._reindex_multi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def _reindex_multi(self, axes, fill_value):
        raise AbstractMethodError(self)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._arith_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py]
    def _arith_method(self, other: object, op: Callable) -> Index:
        """
        Parameters
        ----------
        other : Any
        op : callable that accepts 2 params
            perform the binary op
        """

        if isinstance(other, ABCTimedeltaIndex):
            # Defer to TimedeltaIndex implementation
            return NotImplemented
        elif isinstance(other, (timedelta, np.timedelta64)):
            # GH#19333 is_integer evaluated True on timedelta64,
            # so we need to catch these explicitly
            return super()._arith_method(other, op)
        elif lib.is_np_dtype(getattr(other, "dtype", None), "m"):
            # Must be an np.ndarray; GH#22390
            return super()._arith_method(other, op)

        if op in [
            operator.pow,
            ops.rpow,
            operator.mod,
            ops.rmod,
            operator.floordiv,
            ops.rfloordiv,
            divmod,
            ops.rdivmod,
        ]:
            return super()._arith_method(other, op)

        step: Callable | None = None
        if op in [operator.mul, ops.rmul, operator.truediv, ops.rtruediv]:
            step = op

        # TODO: if other is a RangeIndex we may have more efficient options
        right = extract_array(other, extract_numpy=True, extract_range=True)
        left = self

        try:
            # apply if we have an override
            if step:
                with np.errstate(all="ignore"):
                    rstep = step(left.step, right)

                # we don't have a representable op
                # so return a base index
                if not is_integer(rstep) or not rstep:
                    raise ValueError

            # GH#53255
            else:
                rstep = -left.step if op == ops.rsub else left.step

            with np.errstate(all="ignore"):
                rstart = op(left.start, right)
                rstop = op(left.stop, right)

            res_name = ops.get_op_result_name(self, other)  # type: ignore[no-untyped-call]
            result = type(self)(rstart, rstop, rstep, name=res_name)

            # for compat with numpy / Index with int64 dtype
            # even if we can represent as a RangeIndex, return
            # as a float64 Index if we have float-like descriptors
            if not all(is_integer(x) for x in [rstart, rstop, rstep]):
                result = result.astype("float64")  # type: ignore[assignment]

            return result

        except (ValueError, TypeError, ZeroDivisionError):
            # test_arithmetic_explicit_conversions
            return super()._arith_method(other, op)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._needs_reindex_multi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def _needs_reindex_multi(self, axes, method, level: Level | None) -> bool:
        """Check if we do need a multi reindex."""
        return (
            (common.count_not_none(*axes.values()) == self._AXIS_LEN)
            and method is None
            and level is None
            # reindex_multi calls self.values, so we only want to go
            #  down that path when doing so is cheap.
            and self._can_fast_transpose
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/conftest.py::arithmetic_win_operators [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/conftest.py]
def arithmetic_win_operators(request):
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py::TestPivotTable.ret_sum [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py]
        def ret_sum(x):
            return sum(x)
```
