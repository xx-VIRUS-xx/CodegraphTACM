# pandas-43 :: minilm

query: BUG: arithmetic with reindex pow (#32734)

## selected nodes

- rank=1 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c::_next_pow2 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c
- rank=2 layer=FUNCTION tokens=282 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsondec.c::createDouble file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsondec.c
- rank=3 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__pow__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=4 layer=FUNCTION tokens=384 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._add_arithmetic_ops file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=5 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._create_arithmetic_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=6 layer=FUNCTION tokens=588 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.pow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=7 layer=FUNCTION tokens=869 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=8 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._reindex_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=9 layer=FUNCTION tokens=904 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py::ExponentialMovingWindow.sum file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py
- rank=10 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py::TestPivotTable.ret_sum file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py
- rank=11 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionScalarOpsMixin._create_arithmetic_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=12 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::scaleNanosecToUnit file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c
- rank=13 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._reindex_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=14 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py::TestPivotTable.ret_none file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py
- rank=15 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/hash_functions.py::UniqueAndFactorizeArange.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/hash_functions.py
- rank=16 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._needs_reindex_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=17 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py::arr_nan_1d file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c::_next_pow2 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c]
static size_t _next_pow2(size_t sz) {
  size_t result = 1;
  while (result < sz)
    result *= 2;
  return result;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsondec.c::createDouble [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsondec.c]
double createDouble(double intNeg, double intValue, double frcValue,
                    int frcDecimalCount) {
  static const double g_pow10[] = {1.0,
                                   0.1,
                                   0.01,
                                   0.001,
                                   0.0001,
                                   0.00001,
                                   0.000001,
                                   0.0000001,
                                   0.00000001,
                                   0.000000001,
                                   0.0000000001,
                                   0.00000000001,
                                   0.000000000001,
                                   0.0000000000001,
                                   0.00000000000001,
                                   0.000000000000001};
  return (intValue + (frcValue * g_pow10[frcDecimalCount])) * intNeg;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__pow__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py]
    def __pow__(self, other):
        return self._arith_method(other, operator.pow)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._create_arithmetic_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def _create_arithmetic_method(cls, op):
        raise AbstractMethodError(cls)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._reindex_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _reindex_indexer(
        self,
        new_index: Index | None,
        indexer: npt.NDArray[np.intp] | None,
    ) -> Series:
        # Note: new_index is None iff indexer is None
        # if not None, indexer is np.intp
        if indexer is None and (
            new_index is None or new_index.names == self.index.names
        ):
            return self.copy(deep=False)

        new_values = algorithms.take_nd(
            self._values, indexer, allow_fill=True, fill_value=None
        )
        return self._constructor(new_values, index=new_index, copy=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py::ExponentialMovingWindow.sum [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py]
    def sum(
        self,
        numeric_only: bool = False,
        engine=None,
        engine_kwargs=None,
    ):
        """
        Calculate the ewm (exponential weighted moment) sum.

        The weighting is controlled by the ``com``, ``span``, ``halflife``, or
        ``alpha`` parameter specified when calling :meth:`DataFrame.ewm` or
        :meth:`Series.ewm`.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns.
        engine : str, default None
            * ``'cython'`` : Runs the operation through C-extensions from cython.
            * ``'numba'`` : Runs the operation through JIT compiled code from numba.
            * ``None`` : Defaults to ``'cython'`` or globally setting
              ``compute.use_numba``
        engine_kwargs : dict, default None
            * For ``'cython'`` engine, there are no accepted ``engine_kwargs``
            * For ``'numba'`` engine, the engine can accept  ``nogil``
              and ``parallel`` dictionary keys. The values must either be ``True`` or
              ``False``. The default ``engine_kwargs`` for the ``'numba'`` engine is
              ``{'nogil': False, 'parallel': False}``

        Returns
        -------
        Series or DataFrame
            Return type is the same as the original object with ``np.float64`` dtype.

        See Also
        --------
        Series.ewm : Calling ewm with Series data.
        DataFrame.ewm : Calling ewm with DataFrames.
        Series.sum : Aggregating sum for Series.
        DataFrame.sum : Aggregating sum for DataFrame.

        Notes
        -----
        See :ref:`window.numba_engine` and :ref:`enhancingperf.numba` for extended
        documentation and performance considerations for the Numba engine.

        Examples
        --------
        >>> ser = pd.Series([1, 2, 3, 4])
        >>> ser.ewm(alpha=0.2).sum()
        0    1.000
        1    2.800
        2    5.240
        3    8.192
        dtype: float64
        """
        if not self.adjust:
            raise NotImplementedError("sum is not implemented with adjust=False")
        if self.times is not None:
            raise NotImplementedError("sum is not implemented with times")
        if maybe_use_numba(engine):
            if self.method == "single":
                func = generate_numba_ewm_func
            else:
                func = generate_numba_ewm_table_func
            ewm_func = func(
                **get_jit_arguments(engine_kwargs),
                com=self._com,
                adjust=self.adjust,
                ignore_na=self.ignore_na,
                deltas=tuple(self._deltas),
                normalize=False,
            )
            return self._apply(ewm_func, name="sum")
        elif engine in ("cython", None):
            if engine_kwargs is not None:
                raise ValueError("cython engine does not accept engine_kwargs")

            deltas = None if self.times is None else self._deltas
            window_func = partial(
                window_aggregations.ewm,
                com=self._com,
                adjust=self.adjust,
                ignore_na=self.ignore_na,
                deltas=deltas,
                normalize=False,
            )
            return self._apply(window_func, name="sum", numeric_only=numeric_only)
        else:
            raise ValueError("engine must be either 'numba' or 'cython'")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py::TestPivotTable.ret_sum [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py]
        def ret_sum(x):
            return sum(x)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionScalarOpsMixin._create_arithmetic_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def _create_arithmetic_method(cls, op):
        return cls._create_method(op)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c::scaleNanosecToUnit [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/datetime/date_conversions.c]
int scaleNanosecToUnit(int64_t *value, NPY_DATETIMEUNIT unit) {
  switch (unit) {
  case NPY_FR_ns:
    break;
  case NPY_FR_us:
    *value /= 1000LL;
    break;
  case NPY_FR_ms:
    *value /= 1000000LL;
    break;
  case NPY_FR_s:
    *value /= 1000000000LL;
    break;
  default:
    return -1;
  }

  return 0;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._reindex_multi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def _reindex_multi(self, axes, fill_value):
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py::TestPivotTable.ret_none [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/test_pivot.py]
        def ret_none(x):
            return np.nan

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/hash_functions.py::UniqueAndFactorizeArange.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/hash_functions.py]
    def setup(self, exponent):
        a = np.arange(10**4, dtype="float64")
        self.a2 = (a + 10**exponent).repeat(100)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._needs_reindex_multi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _needs_reindex_multi(self, axes, method, level) -> bool:
        """
        Check if we do need a multi reindex; this is for compat with
        higher dims.
        """
        return False

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py::arr_nan_1d [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py]
def arr_nan_1d(arr_nan):
    return arr_nan[:, 0]
```
