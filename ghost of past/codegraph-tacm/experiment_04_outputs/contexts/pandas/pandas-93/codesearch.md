# pandas-93 :: codesearch

query: BUG: DTI/TDI/PI `where` accepting non-matching dtypes (#30791)

## selected nodes

- rank=1 layer=FUNCTION tokens=355 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._check_dtype_match file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=2 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=3 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Where.time_where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=4 layer=FUNCTION tokens=524 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._maybe_require_matching_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=5 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::_where_numexpr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py
- rank=6 layer=FUNCTION tokens=1881 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=7 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestWhereCoercion._assert_where_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py
- rank=8 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::_where_standard file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py
- rank=9 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray._where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py
- rank=10 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_require_matching_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=11 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py
- rank=12 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py
- rank=13 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py::dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py
- rank=14 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py::SelectDtypes.time_select_dtype_string_include file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._check_dtype_match [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
        def _check_dtype_match(left: ArrayLike, right: ArrayLike, i: int) -> None:
            if left.dtype != right.dtype:
                if isinstance(left.dtype, CategoricalDtype) and isinstance(
                    right.dtype, CategoricalDtype
                ):
                    # The generic error message is confusing for categoricals.
                    #
                    # In this function, the join keys include both the original
                    # ones of the merge_asof() call, and also the keys passed
                    # to its by= argument. Unordered but equal categories
                    # are not supported for the former, but will fail
                    # later with a ValueError, so we don't *need* to check
                    # for them here.
                    msg = (
                        f"incompatible merge keys [{i}] {left.dtype!r} and "
                        f"{right.dtype!r}, both sides category, but not equal ones"
                    )
                else:
                    msg = (
                        f"incompatible merge keys [{i}] {left.dtype!r} and "
                        f"{right.dtype!r}, must be the same type"
                    )
                raise MergeError(msg)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def _where(self, mask, value):
        # NB: may not preserve dtype, e.g. result may be Sparse[float64]
        #  while self is Sparse[int64]
        naive_implementation = np.where(mask, self, value)
        dtype = SparseDtype(naive_implementation.dtype, fill_value=self.fill_value)
        result = type(self)._from_sequence(naive_implementation, dtype=dtype)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Where.time_where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_where(self, inplace, dtype):
        self.df.where(self.mask, other=0.0, inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._maybe_require_matching_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _maybe_require_matching_dtypes(
        self, left_join_keys: list[ArrayLike], right_join_keys: list[ArrayLike]
    ) -> None:
        # TODO: why do we do this for AsOfMerge but not the others?

        def _check_dtype_match(left: ArrayLike, right: ArrayLike, i: int) -> None:
            if left.dtype != right.dtype:
                if isinstance(left.dtype, CategoricalDtype) and isinstance(
                    right.dtype, CategoricalDtype
                ):
                    # The generic error message is confusing for categoricals.
                    #
                    # In this function, the join keys include both the original
                    # ones of the merge_asof() call, and also the keys passed
                    # to its by= argument. Unordered but equal categories
                    # are not supported for the former, but will fail
                    # later with a ValueError, so we don't *need* to check
                    # for them here.
                    msg = (
                        f"incompatible merge keys [{i}] {left.dtype!r} and "
                        f"{right.dtype!r}, both sides category, but not equal ones"
                    )
                else:
                    msg = (
                        f"incompatible merge keys [{i}] {left.dtype!r} and "
                        f"{right.dtype!r}, must be the same type"
                    )
                raise MergeError(msg)

        # validate index types are the same
        for i, (lk, rk) in enumerate(zip(left_join_keys, right_join_keys, strict=True)):
            _check_dtype_match(lk, rk, i)

        if self.left_index:
            lt = self.left.index._values
        else:
            lt = left_join_keys[-1]

        if self.right_index:
            rt = self.right.index._values
        else:
            rt = right_join_keys[-1]

        _check_dtype_match(lt, rt, 0)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::_where_numexpr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py]
def _where_numexpr(cond, left_op, right_op):
    # Caller is responsible for extracting ndarray if necessary
    result = None

    if _can_use_numexpr(None, "where", left_op, right_op, "where"):
        result = ne.evaluate(
            "where(cond_value, a_value, b_value)",
            local_dict={"cond_value": cond, "a_value": left_op, "b_value": right_op},
            casting="safe",
        )

    if result is None:
        result = _where_standard(cond, left_op, right_op)

    return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame._where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def _where(
        self,
        cond,
        other=lib.no_default,
        *,
        inplace: bool = False,
        axis: Axis | None = None,
        level=None,
    ) -> Self:
        """
        Equivalent to public method `where`, except that `other` is not
        applied as a function even if callable. Used in __setitem__.
        """
        inplace = validate_bool_kwarg(inplace, "inplace")

        if axis is not None:
            axis = self._get_axis_number(axis)

        # align the cond to same shape as myself
        cond = common.apply_if_callable(cond, self)
        if isinstance(cond, NDFrame):
            # CoW: Make sure reference is not kept alive
            if cond.ndim == 1 and self.ndim == 2:
                if axis == 1:
                    # GH#58190 broadcast cond along columns
                    cond = cond._constructor_expanddim(
                        dict.fromkeys(range(len(self)), cond),
                        copy=False,
                    ).T
                    cond.index = self.index
                else:
                    cond = cond._constructor_expanddim(
                        dict.fromkeys(range(len(self.columns)), cond),
                        copy=False,
                    )
                    cond.columns = self.columns
            cond = cond.align(self, join="right")[0]
        else:
            if not hasattr(cond, "shape"):
                cond = np.asanyarray(cond)
            if cond.shape != self.shape:
                raise ValueError("Array conditional must be same shape as self")
            cond = self._constructor(cond, **self._construct_axes_dict(), copy=False)

        # make sure we are boolean
        fill_value = bool(inplace)
        cond = cond.fillna(fill_value)
        cond = cond.infer_objects()

        msg = "Boolean array expected for the condition, not {dtype}"

        if not cond.empty:
            if not isinstance(cond, ABCDataFrame):
                # This is a single-dimensional object.
                if not is_bool_dtype(cond):
                    raise TypeError(msg.format(dtype=cond.dtype))
            else:
                for block in cond._mgr.blocks:
                    if not is_bool_dtype(block.dtype):
                        raise TypeError(msg.format(dtype=block.dtype))
                if cond._mgr.any_extension_types:
                    # GH51574: avoid object ndarray conversion later on
                    cond = cond._constructor(
                        cond.to_numpy(dtype=bool, na_value=fill_value),
                        **cond._construct_axes_dict(),
                    )
        else:
            # GH#21947 we have an empty DataFrame/Series, could be object-dtype
            cond = cond.astype(bool)

        cond_for_ea = cond
        cond = -cond if inplace else cond
        cond = cond.reindex(self._info_axis, axis=self._info_axis_number)

        # try to align with other
        if isinstance(other, NDFrame):
            # align with me
            if other.ndim <= self.ndim:
                # CoW: Make sure reference is not kept alive
                other = self.align(
                    other,
                    join="left",
                    axis=axis,
                    level=level,
                    fill_value=None,
                )[1]

                # if we are NOT aligned, raise as we cannot where index
                if axis is None and not other._indexed_same(self):
                    raise InvalidIndexError

                if other.ndim < self.ndim:
                    other = other._values
                    if isinstance(other, np.ndarray):
                        # TODO(EA2D): could also do this for NDArrayBackedEA cases?
                        if axis == 0:
                            other = np.reshape(other, (-1, 1))
                        elif axis == 1:
                            other = np.reshape(other, (1, -1))

                        other = np.broadcast_to(other, self.shape)
                    else:
                        # GH#38729, GH#62038 avoid lossy casting or object-casting
                        if axis == 0:
                            res_cols = [
                                self.iloc[:, i]._where(
                                    cond_for_ea.iloc[:, i],
                                    other,
                                )
                                for i in range(self.shape[1])
                            ]
                        elif axis == 1:
                            # TODO: can we use a zero-copy alternative to "repeat"?
                            res_cols = [
                                self.iloc[:, i]._where(
                                    cond_for_ea.iloc[:, i],
                                    other[i : i + 1].repeat(len(self)),
                                )
                                for i in range(self.shape[1])
                            ]
                        res = self._constructor(dict(enumerate(res_cols)))
                        res.index = self.index
                        res.columns = self.columns
                        if inplace:
                            self._update_inplace(res)
                            return self
                        return res.__finalize__(self)

            # slice me out of the other
            else:
                raise NotImplementedError(
                    "cannot align with a higher dimensional NDFrame"
                )

        elif not isinstance(other, (MultiIndex, NDFrame)):
            # mainly just catching Index here
            other = extract_array(other, extract_numpy=True)

        if isinstance(other, (np.ndarray, ExtensionArray)):
            if other.shape != self.shape:
                if self.ndim != 1:
                    # In the ndim == 1 case we may have
                    #  other length 1, which we treat as scalar (GH#2745, GH#4192)
                    #  or len(other) == icond.sum(), which we treat like
                    #  __setitem__ (GH#3235)
                    raise ValueError(
                        "other must be the same shape as self when an ndarray"
                    )

            # we are the same shape, so create an actual object for alignment
            else:
                other = self._constructor(
                    other, **self._construct_axes_dict(), copy=False
                )

        if axis is None:
            axis = 0

        other_ndim = getattr(other, "ndim", 0)
        if self.ndim == other_ndim:
            align = True
        else:
            # GH#58190 scalar other (ndim=0) should never be aligned
            align = other_ndim >= 1 and self._get_axis_number(axis) == 1

        if inplace:
            # we may have different type blocks come out of putmask, so
            # reconstruct the block manager

            new_data = self._mgr.putmask(mask=cond, new=other, align=align)
            result = self._constructor_from_mgr(new_data, axes=new_data.axes)
            self._update_inplace(result)
            return self

        else:
            new_data = self._mgr.where(
                other=other,
                cond=cond,
                align=align,
            )
            result = self._constructor_from_mgr(new_data, axes=new_data.axes)
            return result.__finalize__(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestWhereCoercion._assert_where_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py]
    def _assert_where_conversion(
        self, original, cond, values, expected, expected_dtype
    ):
        """test coercion triggered by where"""
        target = original.copy()
        res = target.where(cond, values)
        tm.assert_equal(res, expected)
        assert res.dtype == expected_dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::_where_standard [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py]
def _where_standard(cond, left_op, right_op):
    # Caller is responsible for extracting ndarray if necessary
    return np.where(cond, left_op, right_op)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray._where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py]
    def _where(self, mask: npt.NDArray[np.bool_], value) -> Self:
        # the super() method NDArrayBackedExtensionArray._where uses
        # np.putmask which doesn't properly handle None/pd.NA, so using the
        # base class implementation that uses __setitem__
        return ExtensionArray._where(self, mask, value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_require_matching_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _maybe_require_matching_dtypes(
        self, left_join_keys: list[ArrayLike], right_join_keys: list[ArrayLike]
    ) -> None:
        # Overridden by AsOfMerge
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py::_is_dt_or_td [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/tile.py]
def _is_dt_or_td(dtype: DtypeObj) -> bool:
    # Note: the dtype here comes from an Index.dtype, so we know that any
    #  dt64/td64 dtype is of a supported unit.
    return isinstance(dtype, DatetimeTZDtype) or lib.is_np_dtype(dtype, "mM")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py]
def where(cond, left_op, right_op, use_numexpr: bool = True):
    """
    Evaluate the where condition cond on left_op and right_op.

    Parameters
    ----------
    cond : np.ndarray[bool]
    left_op : return if cond is True
    right_op : return if cond is False
    use_numexpr : bool, default True
        Whether to try to use numexpr.
    """
    assert _where is not None
    if use_numexpr:
        return _where(cond, left_op, right_op)
    else:
        return _where_standard(cond, left_op, right_op)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py::dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_interval.py]
def dtype():
    return IntervalDtype()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py::SelectDtypes.time_select_dtype_string_include [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/dtypes.py]
    def time_select_dtype_string_include(self, dtype):
        self.df_string.select_dtypes(include=dtype)
```
