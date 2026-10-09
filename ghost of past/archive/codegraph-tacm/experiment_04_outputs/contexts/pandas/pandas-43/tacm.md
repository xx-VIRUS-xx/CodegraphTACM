# pandas-43 :: tacm

query: BUG: arithmetic with reindex pow (#32734)

## selected nodes

- rank=1 layer=FILE tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=2 layer=FILE tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=3 layer=FILE tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/numpy/function.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/numpy/function.py
- rank=4 layer=FILE tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/scripts/eval_performance.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/scripts/eval_performance.py
- rank=5 layer=CLASS tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::TestNumericArithmeticUnsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py
- rank=6 layer=CLASS tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=7 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=8 layer=CLASS tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py::TestTimedelta64ArrayLikeArithmetic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_timedelta64.py
- rank=9 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::ReindexMethod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=10 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::LevelAlign file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=11 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_with_cache file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=12 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.pow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=13 layer=FUNCTION tokens=339 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._add_arithmetic_ops file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=14 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._needs_reindex_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=15 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_dates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=16 layer=FUNCTION tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=17 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_no_cache file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=18 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::Reindex.time_reindex_multiindex_no_cache_dates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=19 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__pow__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py
- rank=20 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::LevelAlign.time_reindex_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=21 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::ReindexMethod.time_reindex_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=22 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=23 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::_reindex_for_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=24 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::OpsMixin.__pow__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=25 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=26 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.pow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=27 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._arith_method_with_reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=28 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._validate_can_reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=29 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=30 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._reindex_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=31 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._inplace_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=32 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionOpsMixin._create_arithmetic_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=33 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::all_arithmetic_functions file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=34 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Reindex.time_reindex_axis0 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=35 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py::compare_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_numeric.py
- rank=36 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Reindex.time_reindex_axis1 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=37 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionScalarOpsMixin._create_arithmetic_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=38 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Reindex.time_reindex_upcast file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=39 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Reindex.time_reindex_axis1_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=40 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/array_ops.py::arithmetic_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/array_ops.py
- rank=41 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::all_arithmetic_operators file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=42 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex.reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=43 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Reindex.time_reindex_both_axes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=44 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=45 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=46 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/test_decimal.py::DecimalArrayWithoutCoercion._create_arithmetic_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/test_decimal.py
- rank=47 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Indexing.time_reindex_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=48 layer=FUNCTION tokens=201 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._reindex_axes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=49 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.reindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=50 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._should_reindex_frame_op file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=51 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py::reindex_helper file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/test_apply.py
- rank=52 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._reindex_multi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=53 layer=FUNCTION tokens=10 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/date/array.py::DateDtype.type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/date/array.py

## context

```text
file asv_bench/benchmarks/reindex.py
imports: numpy, pandas
defines: Reindex, ReindexMethod, LevelAlign, DropDuplicates, Align

file pandas/core/frame.py
imports: __future__, collections, functools, io, itertools, operator, sys, typing
defines: DataFrame, _from_nested_dict, _reindex_for_setitem

file compat/numpy/function.py
imports: __future__, typing, numpy, pandas
defines: CompatValidator, process_skipna, validate_argmin_with_skipna, validate_argmax_with_skipna, validate_argsort_with_ascending, validate_clip_with_axis, validate_clip_with_axis, validate_clip_with_axis, validate_cum_func_with_skipna, validate_groupby_func, validate_minmax_axis, validate_func

file doc/scripts/eval_performance.py
imports: timeit, numpy, seaborn, pandas, matplotlib
defines: bench_with, bench_subset, bench, plot_perf

class TestNumericArithmeticUnsorted:  [tests/arithmetic/test_numeric.py:1276]
methods: test_addsub_arithmetic
         test_arithmetic_with_frame_or_series
         test_binops_index, test_binops_index_pow
         test_binops_index_scalar
         test_binops_index_scalar_pow
         test_numeric_compat2
         test_numeric_compat2_floordiv
         test_pow_nan_with_zero

class Reindex:  [asv_bench/benchmarks/reindex.py:13]
methods: setup, time_reindex_columns, time_reindex_dates
         time_reindex_multiindex_no_cache
         time_reindex_multiindex_no_cache_dates
         time_reindex_multiindex_with_cache

class Series(base.IndexOpsMixin, NDFrame):  # type: ignore[misc]  [pandas/core/series.py:211]
methods: _align_for_op, _append_internal, _arith_method, _binop
         _can_hold_na, _cmp_method, _construct_result
         _construct_result, _construct_result
         _constructor, _constructor_expanddim
         _constructor_expanddim_from_mgr
         _constructor_from_mgr, _flex_method
         _get_rows_with_mask, _get_value
         _get_values_tuple, _get_with, _gotitem
         _init_dict, _ixs, _logical_method
         _needs_reindex_multi, _reduce, _references
         _reindex_indexer, _set_labels, _set_name
         _set_value, _set_values, _set_with
         _set_with_engine, _slice, _values, add, aggregate
         all, any, apply, argsort, array, autocorr, axes
         between, case_when, combine, combine_first
         compare, corr, count, cov, cummax, cummin
         cumprod, cumsum, diff, divmod, dot, drop, drop
         drop, drop, drop_duplicates, drop_duplicates
         drop_duplicates, drop_duplicates, dropna, dropna
         dropna, dtype, dtypes, duplicated, eq, explode
         floordiv, from_arrow, ge, groupby, gt, idxmax
         idxmin, info, isin, isna, isnull, items, keys
         kurt, le, lt, map, max, mean, median
         memory_usage, min, mod, mode, mul, name, name, ne
         nlargest, notna, notnull, nsmallest, pop, pow
         prod, quantile, quantile, quantile, quantile
         radd, rdivmod, reindex, rename, rename, rename
         rename_axis, rename_axis, rename_axis
         rename_axis, reorder_levels, repeat, reset_index
         reset_index, reset_index, reset_index, rfloordiv
         rmod, rmul, round, rpow, rsub, rtruediv
         searchsorted, sem, set_axis, skew, sort_index
         sort_index, sort_index, sort_index, sort_values
         sort_values, sort_values, sort_values, std, sub
         sum, swaplevel, to_dict, to_dict, to_dict
         to_frame, to_markdown, to_markdown, to_markdown
         to_markdown, to_period, to_string, to_string
         to_string, to_timestamp, transform, truediv
         unique, unstack, update, values, var, __array__
         __arrow_c_stream__, __getitem__, __init__
         __len__, __matmul__, __repr__, __rmatmul__
         __setitem__

class TestTimedelta64ArrayLikeArithmetic:  [tests/arithmetic/test_timedelta64.py:2293]
methods: test_td64arr_pow_invalid

class ReindexMethod:  [asv_bench/benchmarks/reindex.py:54]
methods: setup, time_reindex_method

class LevelAlign:  [asv_bench/benchmarks/reindex.py:67]
methods: setup, time_align_level, time_reindex_level

    def time_reindex_multiindex_with_cache(self):
        # MultiIndex._values gets cached
        self.s.reindex(self.s_subset.index)

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
    # ... truncated

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

    def _needs_reindex_multi(self, axes, method, level) -> bool:
        """
        Check if we do need a multi reindex; this is for compat with
        higher dims.
        """
        return False

    def time_reindex_dates(self):
        self.df.reindex(self.rng_subset)

    def time_reindex_columns(self):
        self.df2.reindex(columns=self.df.columns[1:5])

    def time_reindex_multiindex_no_cache(self):
        # Copy to avoid MultiIndex._values getting cached
        self.s.reindex(self.s_subset_no_cache.index.copy())

    def time_reindex_multiindex_no_cache_dates(self):
        # Copy to avoid MultiIndex._values getting cached
        self.s2_subset.reindex(self.s2.index.copy())

    def __pow__(self, other: Any) -> Expression:
        self_repr, other_repr = self._maybe_wrap_parentheses(other)
        return self._with_op("__pow__", other, f"{self_repr} ** {other_repr}")

    def time_reindex_level(self):
        self.df_level.reindex(self.index, level=1)

    def time_reindex_method(self, method, constructor):
        self.ts.reindex(self.idx, method=method)

    def reindex(  # type: ignore[override]
        self,
        index=None,
        *,
        axis: Axis | None = None,
        method: ReindexMethod | None = None,
        copy: bool | lib.NoDefault = lib.no_default,
        level: Level | None = None,
        fill_value: Scalar | None = None,
        limit: int | None = None,
        tolerance=None,
    ) -> Series:
    # ... truncated

def _reindex_for_setitem(
    value: DataFrame | Series, index: Index
) -> tuple[ArrayLike, BlockValuesRefs | None]:
    # reindex if necessary

    if value.index.equals(index) or not len(index):
        if isinstance(value, Series):
            return value._values, value._references
        return value._values.copy(), None

    # GH#4107
    try:
        reindexed_value = value.reindex(index)._values
    except ValueError as err:
        # raised in MultiIndex.from_tuples, see test_insert_error_msmgs
        if not value.index.is_unique:
            # duplicate axis
            raise err

        raise TypeError(
            "incompatible index of inserted column with frame index"
        ) from err
    return reindexed_value, None

    def __pow__(self, other):
        return self._arith_method(other, operator.pow)

    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

    # ... truncated

    def pow(
        self, other, axis: Axis = "columns", level=None, fill_value=None
    ) -> DataFrame:
        """
    # ... truncated

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
    # ... truncated

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
    # ... truncated

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

    def _inplace_method(self, other, op) -> Self:
        """
        Wrap arithmetic method to operate inplace.
        """
        result = op(self, other)

        # this makes sure that we are aligned like the input
        # we are updating inplace
        self._update_inplace(result.reindex_like(self))
        return self

    def _create_arithmetic_method(cls, op):
        raise AbstractMethodError(cls)

def all_arithmetic_functions(request):
    """
    Fixture for operator and roperator arithmetic functions.

    Notes
    -----
    This includes divmod and rdivmod, whereas all_arithmetic_operators
    does not.
    """
    return request.param

    def time_reindex_axis0(self):
        self.df.reindex(self.idx)

def compare_op(series, other, op):
    left = np.abs(series) if op in (ops.rpow, operator.pow) else series
    right = np.abs(other) if op in (ops.rpow, operator.pow) else other

    cython_or_numpy = op(left, right)
    python = left.combine(right, op)
    if isinstance(other, Series) and not other.index.equals(series.index):
        python.index = python.index._with_freq(None)
    tm.assert_series_equal(cython_or_numpy, python)

    def time_reindex_axis1(self):
        self.df.reindex(columns=self.idx_cols)

    def _create_arithmetic_method(cls, op):
        return cls._create_method(op)

    def time_reindex_upcast(self):
        self.df2.reindex(np.random.permutation(range(1200)))

    def time_reindex_axis1_missing(self):
        self.df.reindex(columns=self.idx)

def arithmetic_op(left: ArrayLike, right: Any, op):
    """
    Evaluate an arithmetic operation `+`, `-`, `*`, `/`, `//`, `%`, `**`, ...

    Note: the caller is responsible for ensuring that numpy warnings are
    suppressed (with np.errstate(all="ignore")) if needed.

    Parameters
    ----------
    left : np.ndarray or ExtensionArray
    right : object
        Cannot be a DataFrame or Index.  Series is *not* excluded.
    # ... truncated

def all_arithmetic_operators(request):
    """
    Fixture for dunder names for common arithmetic operations.
    """
    return request.param

    def reindex(
        self, target, method=None, level=None, limit: int | None = None, tolerance=None
    ) -> tuple[Index, npt.NDArray[np.intp] | None]:
        """
        Create index with target's values (move/add/delete values as necessary)

        Returns
        -------
        new_index : pd.Index
            Resulting index
        indexer : np.ndarray[np.intp] or None
            Indices of output values in original index

        """
        if method is not None:
            raise NotImplementedError(
                "argument method is not implemented for CategoricalIndex.reindex"
            )
        if level is not None:
            raise NotImplementedError(
                "argument level is not implemented for CategoricalIndex.reindex"
            )
        if limit is not None:
            raise NotImplementedError(
                "argument limit is not implemented for CategoricalIndex.reindex"
            )
        return super().reindex(target)

    def time_reindex_both_axes(self):
        self.df.reindex(index=self.idx, columns=self.idx_cols)

    def reindex(
        self,
        labels=None,
        *,
        index=None,
        columns=None,
        axis: Axis | None = None,
        method: ReindexMethod | None = None,
        copy: bool | lib.NoDefault = lib.no_default,
        level: Level | None = None,
        fill_value: Scalar | None = np.nan,
        limit: int | None = None,
    # ... truncated

    def time_reindex(self):
        self.index.reindex(self.index[:500])

    def _create_arithmetic_method(cls, op):
        return cls._create_method(op, coerce_to_dtype=False)

    def time_reindex_missing(self):
        self.index.reindex(["a", "b", "c", "d"])

    def _reindex_axes(
        self,
        axes,
        level: Level | None,
        limit: int | None,
        tolerance,
        method,
        fill_value: Scalar | None,
    ) -> Self:
        """Perform the reindex for all the axes."""
        obj = self
        for a in self._AXIS_ORDERS:
            labels = axes[a]
            if labels is None:
                continue

            ax = self._get_axis(a)
            new_index, indexer = ax.reindex(
                labels, level=level, limit=limit, tolerance=tolerance, method=method
            )

            axis = self._get_axis_number(a)
            obj = obj._reindex_with_indexers(
                {axis: [new_index, indexer]},
                fill_value=fill_value,
                allow_dups=False,
            )

        return obj

    def reindex(
        self,
        labels=None,
        *,
        index=None,
        columns=None,
        axis: Axis | None = None,
        method: ReindexMethod | None = None,
        copy: bool | lib.NoDefault = lib.no_default,
        level: Level | None = None,
        fill_value: Scalar | None = np.nan,
        limit: int | None = None,
    # ... truncated

    def _should_reindex_frame_op(self, right, op, axis: int, fill_value, level) -> bool:
        """
        Check if this is an operation between DataFrames that will need to reindex.
        """
    # ... truncated

    def reindex_helper(x):
        return x.reindex(np.arange(x.index.min(), x.index.max() + 1))

    def _reindex_multi(self, axes, fill_value):
        raise AbstractMethodError(self)

    def type(self):
        return dt.date
```
