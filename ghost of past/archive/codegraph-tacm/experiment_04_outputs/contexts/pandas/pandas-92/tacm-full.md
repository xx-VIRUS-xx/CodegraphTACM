# pandas-92 :: tacm-full

query: BUG: PeriodIndex.searchsorted accepting invalid inputs (#30763)

## selected nodes

- rank=1 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py
- rank=2 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py
- rank=3 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.index_class file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=4 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::default_array_ufunc file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py
- rank=5 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__array_ufunc__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py
- rank=6 layer=FUNCTION tokens=353 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_monotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py
- rank=7 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py
- rank=8 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.__array_ufunc__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=9 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py
- rank=10 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=11 layer=FUNCTION tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.__array_ufunc__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=12 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.__array_ufunc__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=13 layer=FUNCTION tokens=380 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/array.py::DecimalArray.__array_ufunc__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/array.py
- rank=14 layer=FUNCTION tokens=248 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._searchsorted_monotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=15 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=16 layer=FUNCTION tokens=415 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.__array_ufunc__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=17 layer=FUNCTION tokens=263 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_indexing.py::TestSetitemValidation._check_setitem_invalid file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_indexing.py
- rank=18 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.searchsorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py
- rank=19 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=20 layer=FUNCTION tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_insert_nat_bin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py::BaseMethodsTests._test_searchsorted_bool_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/methods.py]
    def _test_searchsorted_bool_dtypes(self, data_for_sorting, as_series):
        # We call this from test_searchsorted in cases where we have a
        #  boolean-like dtype. The non-bool test assumes we have more than 2
        #  unique values.
        dtype = data_for_sorting.dtype
        data_for_sorting = pd.array([True, False], dtype=dtype)
        b, a = data_for_sorting
        arr = type(data_for_sorting)._from_sequence([a, b], dtype=dtype)

        if as_series:
            arr = pd.Series(arr)
        assert arr.searchsorted(a) == 0
        assert arr.searchsorted(a, side="right") == 1

        assert arr.searchsorted(b) == 1
        assert arr.searchsorted(b, side="right") == 2

        result = arr.searchsorted(arr.take([0, 1]))
        expected = np.array([0, 1], dtype=np.intp)

        tm.assert_numpy_array_equal(result, expected)

        # sorter
        sorter = np.array([1, 0])
        assert data_for_sorting.searchsorted(a, sorter=sorter) == 0

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py::SearchSorted.time_searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/series_methods.py]
    def time_searchsorted(self, dtype):
        key = "2" if dtype == "str" else 2
        self.s.searchsorted(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PeriodDtype.index_class [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def index_class(self) -> type_t[PeriodIndex]:
        from pandas import PeriodIndex

        return PeriodIndex

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py::default_array_ufunc [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arraylike.py]
def default_array_ufunc(self, ufunc: np.ufunc, method: str, *inputs, **kwargs):
    """
    Fallback to the behavior we would get if we did not define __array_ufunc__.

    Notes
    -----
    We are assuming that `self` is among `inputs`.
    """
    if not any(x is self for x in inputs):
        raise NotImplementedError

    new_inputs = [x if x is not self else np.asarray(x) for x in inputs]

    return getattr(ufunc, method)(*new_inputs, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py::Expression.__array_ufunc__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/col.py]
    def __array_ufunc__(
        self, ufunc: Callable[..., Any], method: str, *inputs: Any, **kwargs: Any
    ) -> Expression:
        def func(df: DataFrame) -> Any:
            parsed_inputs = _parse_args(df, *inputs)
            parsed_kwargs = _parse_kwargs(df, *kwargs)
            return ufunc(*parsed_inputs, **parsed_kwargs)

        args_str = _pretty_print_args_kwargs(*inputs, **kwargs)
        repr_str = f"{ufunc.__name__}({args_str})"

        return Expression(func, repr_str)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py::IntervalIndex._get_indexer_monotonic [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/interval.py]
    def _get_indexer_monotonic(self, target: Index) -> npt.NDArray[np.intp]:
        """
        Use searchsorted on endpoints for O(n*log(m)) scalar lookups on
        a monotonic non-overlapping IntervalIndex, instead of IntervalTree
        which scales poorly for large target arrays. See GH#47614.
        """
        # Caller is responsible for checking self.is_monotonic_increasing
        closed_right = self.closed in ("right", "both")
        closed_left = self.closed in ("left", "both")

        # searchsorted on right endpoints to find candidate bin
        side: Literal["left", "right"] = "left" if closed_right else "right"
        indexer = self.right.searchsorted(target, side=side)

        nbins = len(self)
        past_end = indexer >= nbins
        indexer = np.minimum(indexer, nbins - 1)

        # Verify values fall within the candidate bin's left bound
        left_values = self.left[indexer]
        if closed_left:
            left_miss = target < left_values
        else:
            left_miss = target <= left_values

        na_mask = isna(target)
        invalid = past_end | left_miss | na_mask
        indexer = np.where(invalid, -1, indexer)
        return ensure_platform_int(indexer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_indexing.py]
    def _check_setitem_invalid(self, ser, invalid, indexer):
        orig_ser = ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser[indexer] = invalid
            ser = orig_ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser.iloc[indexer] = invalid
            ser = orig_ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser.loc[indexer] = invalid
            ser = orig_ser.copy()

        with pytest.raises(TypeError, match="Invalid value"):
            ser[:] = invalid

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.__array_ufunc__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs):
        if any(
            isinstance(other, (ABCSeries, ABCIndex, ABCDataFrame)) for other in inputs
        ):
            return NotImplemented

        result = arraylike.maybe_dispatch_ufunc_to_dunder_op(
            self, ufunc, method, *inputs, **kwargs
        )
        if result is not NotImplemented:
            return result

        if "out" in kwargs:
            return arraylike.dispatch_ufunc_with_out(
                self, ufunc, method, *inputs, **kwargs
            )

        if method == "reduce":
            result = arraylike.dispatch_reduction_ufunc(
                self, ufunc, method, *inputs, **kwargs
            )
            if result is not NotImplemented:
                return result

        return arraylike.default_array_ufunc(self, ufunc, method, *inputs, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py::TestSetitemValidation._check_setitem_invalid [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_indexing.py]
    def _check_setitem_invalid(self, df, invalid, indexer):
        orig_df = df.copy()

        # iloc
        with pytest.raises(TypeError, match="Invalid value"):
            df.iloc[indexer, 0] = invalid
            df = orig_df.copy()

        # loc
        with pytest.raises(TypeError, match="Invalid value"):
            df.loc[indexer, "a"] = invalid
            df = orig_df.copy()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray.searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def searchsorted(
        self,
        v: ArrayLike | object,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        if config["mode"]["performance_warnings"]:
            msg = "searchsorted requires high memory usage."
            warnings.warn(msg, PerformanceWarning, stacklevel=find_stack_level())
        v = np.asarray(v)
        return np.asarray(self, dtype=self.dtype.subtype).searchsorted(v, side, sorter)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.__array_ufunc__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs):
        if (
            ufunc in [np.isnan, np.isinf, np.isfinite]
            and len(inputs) == 1
            and inputs[0] is self
        ):
            # numpy 1.18 changed isinf and isnan to not raise on dt64/td64
            return getattr(ufunc, method)(self._ndarray, **kwargs)

        return super().__array_ufunc__(ufunc, method, *inputs, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.__array_ufunc__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def __array_ufunc__(
        self, ufunc: np.ufunc, method: str, *inputs: Any, **kwargs: Any
    ):
        return arraylike.array_ufunc(self, ufunc, method, *inputs, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/array.py::DecimalArray.__array_ufunc__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/decimal/array.py]
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs):
        if not all(isinstance(t, (*self._HANDLED_TYPES, DecimalArray)) for t in inputs):
            return NotImplemented

        result = arraylike.maybe_dispatch_ufunc_to_dunder_op(
            self, ufunc, method, *inputs, **kwargs
        )
        if result is not NotImplemented:
            # e.g. test_array_ufunc_series_scalar_other
            return result

        if "out" in kwargs:
            return arraylike.dispatch_ufunc_with_out(
                self, ufunc, method, *inputs, **kwargs
            )

        inputs = tuple(x._data if isinstance(x, DecimalArray) else x for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if method == "reduce":
            result = arraylike.dispatch_reduction_ufunc(
                self, ufunc, method, *inputs, **kwargs
            )
            if result is not NotImplemented:
                return result

        def reconstruct(x):
            if isinstance(x, (decimal.Decimal, numbers.Number)):
                return x
            else:
                return type(self)._from_sequence(x, dtype=self.dtype)

        if ufunc.nout > 1:
            return tuple(reconstruct(x) for x in result)
        else:
            return reconstruct(result)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._searchsorted_monotonic [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _searchsorted_monotonic(
        self, label: Hashable, side: Literal["left", "right"] = "left"
    ) -> int:
        if self.is_monotonic_increasing:
            return self.searchsorted(label, side=side)  # type: ignore[call-overload]
        elif self.is_monotonic_decreasing:
            # np.searchsorted expects ascending sort order, have to reverse
            # everything for it to work (element ordering, search side and
            # resulting value).
            pos = self[::-1].searchsorted(  # type: ignore[call-overload]
                label,  # pyright: ignore[reportArgumentType]
                side="right" if side == "left" else "left",
            )
            return maybe_unbox_numpy_scalar(len(self) - pos)

        raise ValueError("index must be monotonic increasing or decreasing")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_contains(self):
        self.c.searchsorted(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.__array_ufunc__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def __array_ufunc__(
        self, ufunc: np.ufunc, method: str_t, *inputs: Any, **kwargs: Any
    ) -> Any:
        if any(isinstance(other, (ABCSeries, ABCDataFrame)) for other in inputs):
            return NotImplemented

        result = arraylike.maybe_dispatch_ufunc_to_dunder_op(
            self, ufunc, method, *inputs, **kwargs
        )
        if result is not NotImplemented:
            return result

        if "out" in kwargs:
            # e.g. test_dti_isub_tdi
            return arraylike.dispatch_ufunc_with_out(
                self, ufunc, method, *inputs, **kwargs
            )

        if method == "reduce":
            result = arraylike.dispatch_reduction_ufunc(
                self, ufunc, method, *inputs, **kwargs
            )
            if result is not NotImplemented:
                return result

        new_inputs = [x if x is not self else x._values for x in inputs]
        result = getattr(ufunc, method)(*new_inputs, **kwargs)
        if ufunc.nout == 2:
            # i.e. np.divmod, np.modf, np.frexp
            return tuple(self.__array_wrap__(x) for x in result)
        elif method == "reduce":
            result = lib.item_from_zerodim(result)
            return maybe_unbox_numpy_scalar(result)
        elif is_scalar(result):
            # e.g. matmul
            return maybe_unbox_numpy_scalar(result)

        if result.dtype == np.float16:
            result = result.astype(np.float32)

        return self.__array_wrap__(result)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_indexing.py::TestSetitemValidation._check_setitem_invalid [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/masked/test_indexing.py]
    def _check_setitem_invalid(self, arr, invalid):
        msg = f"Invalid value '{invalid!s}' for dtype '{arr.dtype}'"
        msg = re.escape(msg)
        with pytest.raises(TypeError, match=msg):
            arr[0] = invalid

        with pytest.raises(TypeError, match=msg):
            arr[:] = invalid

        with pytest.raises(TypeError, match=msg):
            arr[[0]] = invalid

        # FIXME: don't leave commented-out
        # with pytest.raises(TypeError):
        #    arr[[0]] = [invalid]

        # with pytest.raises(TypeError):
        #    arr[[0]] = np.array([invalid], dtype=object)

        # Series non-coercion, behavior subject to change
        ser = pd.Series(arr)
        with pytest.raises(TypeError, match=msg):
            ser[0] = invalid
            # TODO: so, so many other variants of this...

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.searchsorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py]
    def searchsorted(
        self,
        value: NumpyValueArrayLike | ExtensionArray,
        side: Literal["left", "right"] = "left",
        sorter: NumpySorter | None = None,
    ) -> npt.NDArray[np.intp] | np.intp:
        # Parent's searchsorted calls _validate_setitem_value, which is
        # too strict for search (e.g. rejects float into int). Delegate
        # directly to numpy which handles cross-dtype searches correctly.
        return self._ndarray.searchsorted(value, side=side, sorter=sorter)  # type: ignore[arg-type]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::SearchSorted.time_categorical_index_contains [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_categorical_index_contains(self):
        self.ci.searchsorted(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::_insert_nat_bin [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
def _insert_nat_bin(
    binner: PeriodIndex, bins: np.ndarray, labels: PeriodIndex, nat_count: int
) -> tuple[PeriodIndex, np.ndarray, PeriodIndex]:
    # NaT handling as in pandas._lib.lib.generate_bins_dt64()
    # shift bins by the number of NaT
    assert nat_count > 0
    bins += nat_count
    bins = np.insert(bins, 0, nat_count)

    # Incompatible types in assignment (expression has type "Index", variable
    # has type "PeriodIndex")
    binner = binner.insert(0, NaT)  # type: ignore[assignment]
    # Incompatible types in assignment (expression has type "Index", variable
    # has type "PeriodIndex")
    labels = labels.insert(0, NaT)  # type: ignore[assignment]
    return binner, bins, labels
```
