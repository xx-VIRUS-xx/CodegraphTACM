# pandas-93 :: hybrid-cs

query: BUG: DTI/TDI/PI `where` accepting non-matching dtypes (#30791)

## selected nodes

- rank=1 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_get file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=2 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_require_matching_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=3 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray._where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py
- rank=4 layer=FUNCTION tokens=434 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::_get_result_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py
- rank=5 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Where.time_where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=6 layer=FUNCTION tokens=343 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=7 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::_where_numexpr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py
- rank=8 layer=FUNCTION tokens=325 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_align file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=9 layer=FUNCTION tokens=1389 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=10 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestWhereCoercion._assert_where_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py
- rank=11 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=12 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray._where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py
- rank=13 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::_where_standard file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py
- rank=14 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::where file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py
- rank=15 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_get [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py]
        def _check_get(df, cond, check_dtypes=True):
            other1 = _safe_add(df)
            rs = df.where(cond, other1)
            rs2 = df.where(cond.values, other1)
            for k, v in rs.items():
                exp = Series(np.where(cond[k], df[k], other1[k]), index=v.index, name=k)
                tm.assert_series_equal(v, exp)
            tm.assert_frame_equal(rs, rs2)

            # dtypes
            if check_dtypes:
                assert (rs.dtypes == df.dtypes).all()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_require_matching_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _maybe_require_matching_dtypes(
        self, left_join_keys: list[ArrayLike], right_join_keys: list[ArrayLike]
    ) -> None:
        # Overridden by AsOfMerge
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray._where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py]
    def _where(self: Self, mask: npt.NDArray[np.bool_], value) -> Self:
        """
        Analogue to np.where(mask, self, value)

        Parameters
        ----------
        mask : np.ndarray[bool]
        value : scalar or listlike

        Raises
        ------
        TypeError
            If value cannot be cast to self.dtype.
        """
        value = self._validate_setitem_value(value)

        res_values = np.where(mask, self._ndarray, value)
        if res_values.dtype != self._ndarray.dtype:
            raise AssertionError(
                # GH#56410
                "Something has gone wrong, please report a bug at "
                "github.com/pandas-dev/pandas/"
            )
        return self._from_backing_data(res_values)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::_get_result_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py]
def _get_result_dtype(
    to_concat: Sequence[ArrayLike], non_empties: Sequence[ArrayLike]
) -> tuple[bool, set[str], DtypeObj | None]:
    target_dtype = None

    dtypes = {obj.dtype for obj in to_concat}
    kinds = {obj.dtype.kind for obj in to_concat}

    any_ea = any(not isinstance(x, np.ndarray) for x in to_concat)
    if any_ea:
        # i.e. any ExtensionArrays

        # we ignore axis here, as internally concatting with EAs is always
        # for axis=0
        if len(dtypes) != 1:
            target_dtype = find_common_type([x.dtype for x in to_concat])
            target_dtype = common_dtype_categorical_compat(to_concat, target_dtype)

    elif not len(non_empties):
        # we have all empties, but may need to coerce the result dtype to
        # object if we have non-numeric type operands (numpy would otherwise
        # cast this to float)
        if len(kinds) != 1:
            if not len(kinds - {"i", "u", "f"}) or not len(kinds - {"b", "i", "u"}):
                # let numpy coerce
                pass
            else:
                # coerce to object
                target_dtype = np.dtype(object)
                kinds = {"o"}
    elif "b" in kinds and len(kinds) > 1:
        # GH#21108, GH#45101
        target_dtype = np.dtype(object)
        kinds = {"o"}
    else:
        # error: Argument 1 to "np_find_common_type" has incompatible type
        # "*Set[Union[ExtensionDtype, Any]]"; expected "dtype[Any]"
        target_dtype = np_find_common_type(*dtypes)  # type: ignore[arg-type]

    return any_ea, kinds, target_dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Where.time_where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_where(self, inplace, dtype):
        self.df.where(self.mask, other=0.0, inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        # check if we have all categorical dtype with identical categories
        if all(isinstance(x, CategoricalDtype) for x in dtypes):
            first = dtypes[0]
            if all(first == other for other in dtypes[1:]):
                return first

        # special case non-initialized categorical
        # TODO we should figure out the expected return value in general
        non_init_cats = [
            isinstance(x, CategoricalDtype) and x.categories is None for x in dtypes
        ]
        if all(non_init_cats):
            return self
        elif any(non_init_cats):
            return None

        # categorical is aware of Sparse -> extract sparse subdtypes
        subtypes = (x.subtype if isinstance(x, SparseDtype) else x for x in dtypes)
        # extract the categories' dtype
        non_cat_dtypes = [
            x.categories.dtype if isinstance(x, CategoricalDtype) else x
            for x in subtypes
        ]
        # TODO should categorical always give an answer?
        from pandas.core.dtypes.cast import find_common_type

        return find_common_type(non_cat_dtypes)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_align [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py]
        def _check_align(df, cond, other, check_dtypes=True):
            rs = df.where(cond, other)
            for i, k in enumerate(rs.columns):
                result = rs[k]
                d = df[k].values
                c = cond[k].reindex(df[k].index).fillna(False).values

                if is_scalar(other):
                    o = other
                elif isinstance(other, np.ndarray):
                    o = Series(other[:, i], index=result.index).values
                else:
                    o = other[k].values

                new_values = d if c.all() else np.where(c, d, o)
                expected = Series(new_values, index=result.index, name=k)

                # since we can't always have the correct numpy dtype
                # as numpy doesn't know how to downcast, don't check
                tm.assert_series_equal(result, expected, check_dtype=False)

            # dtypes
            # can't check dtype when other is an ndarray

            if check_dtypes and not isinstance(other, np.ndarray):
                assert (rs.dtypes == df.dtypes).all()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def where(
        self,
        cond,
        other=lib.no_default,
        *,
        inplace: bool = False,
        axis: Axis | None = None,
        level: Level | None = None,
    ) -> Self:
        """
        Replace values where the condition is False.

        This method allows conditional replacement of values. Where the
        condition evaluates to True, the original values are retained; where
        it evaluates to False, values are replaced with corresponding entries
        from ``other``.

        Parameters
        ----------
        cond : bool Series/DataFrame, array-like, or callable
            Where `cond` is True, keep the original value. Where
            False, replace with corresponding value from `other`.
            If `cond` is callable, it is computed on the Series/DataFrame and
            should return boolean Series/DataFrame or array. The callable must
            not change input Series/DataFrame (though pandas doesn't check it).
        other : scalar, Series/DataFrame, or callable
            Entries where `cond` is False are replaced with
            corresponding value from `other`.
            If other is callable, it is computed on the Series/DataFrame and
            should return scalar or Series/DataFrame. The callable must not
            change input Series/DataFrame (though pandas doesn't check it).
            If not specified, entries will be filled with the corresponding
            NULL value (``np.nan`` for numpy dtypes, ``pd.NA`` for extension
            dtypes).
        inplace : bool, default False
            Whether to perform the operation in place on the data.
        axis : int, default None
            Alignment axis if needed. For `Series` this parameter is
            unused and defaults to 0.
        level : int, default None
            Alignment level if needed.

        Returns
        -------
        Series or DataFrame
            When applied to a Series, the function will return a Series,
            and when applied to a DataFrame, it will return a DataFrame.

        See Also
        --------
        :func:`DataFrame.mask` : Return an object of same shape as caller.
        :func:`Series.mask` : Return an object of same shape as caller.

        Notes
        -----
        The where method is an application of the if-then idiom. For each
        element in the caller, if ``cond`` is ``True`` the
        element is used; otherwise the corresponding element from
        ``other`` is used. If the axis of ``other`` does not align with axis of
        ``cond`` Series/DataFrame, the values of ``cond`` on misaligned index positions
        will be filled with False.

        The signature for :func:`Series.where` or
        :func:`DataFrame.where` differs from :func:`numpy.where`.
        Roughly ``df1.where(m, df2)`` is equivalent to ``np.where(m, df1, df2)``.

        For further details and examples see the ``where`` documentation in
        :ref:`indexing <indexing.where_mask>`.

        The dtype of the object takes precedence. The fill value is casted to
        the object's dtype, if this can be done losslessly.

        Examples
        --------
        >>> s = pd.Series(range(5))
        >>> s.where(s > 0)
        0    NaN
        1    1.0
        2    2.0
        3    3.0
        4    4.0
        dtype: float64
        >>> s.mask(s > 0)
        0    0.0
        1    NaN
        2    NaN
        3    NaN
        4    NaN
        dtype: float64

        >>> s = pd.Series(range(5))
        >>> t = pd.Series([True, False])
        >>> s.where(t, 99)
        0     0
        1    99
        2    99
        3    99
        4    99
        dtype: int64
        >>> s.mask(t, 99)
        0    99
        1     1
        2    99
        3    99
        4    99
        dtype: int64

        >>> s.where(s > 1, 10)
        0    10
        1    10
        2    2
        3    3
        4    4
        dtype: int64
        >>> s.mask(s > 1, 10)
        0     0
        1     1
        2    10
        3    10
        4    10
        dtype: int64

        >>> df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=["A", "B"])
        >>> df
           A  B
        0  0  1
        1  2  3
        2  4  5
        3  6  7
        4  8  9
        >>> m = df % 3 == 0
        >>> df.where(m, -df)
           A  B
        0  0 -1
        1 -2  3
        2 -4 -5
        3  6 -7
        4 -8  9
        >>> df.where(m, -df) == np.where(m, df, -df)
              A     B
        0  True  True
        1  True  True
        2  True  True
        3  True  True
        4  True  True
        >>> df.where(m, -df) == df.mask(~m, -df)
              A     B
        0  True  True
        1  True  True
        2  True  True
        3  True  True
        4  True  True
        """
        inplace = validate_bool_kwarg(inplace, "inplace")
        if inplace:
            if not CHAINED_WARNING_DISABLED:
                if sys.getrefcount(
                    self
                ) <= REF_COUNT_METHOD and not common.is_local_in_caller_frame(self):
                    warnings.warn(
                        _chained_assignment_method_msg,
                        ChainedAssignmentError,
                        stacklevel=2,
                    )

        other = common.apply_if_callable(other, self)
        return self._where(cond, other, inplace=inplace, axis=axis, level=level)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestWhereCoercion._assert_where_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py]
    def _assert_where_conversion(
        self, original, cond, values, expected, expected_dtype
    ):
        """test coercion triggered by where"""
        target = original.copy()
        res = target.where(cond, values)
        tm.assert_equal(res, expected)
        assert res.dtype == expected_dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def _where(self, mask, value):
        # NB: may not preserve dtype, e.g. result may be Sparse[float64]
        #  while self is Sparse[int64]
        naive_implementation = np.where(mask, self, value)
        dtype = SparseDtype(naive_implementation.dtype, fill_value=self.fill_value)
        result = type(self)._from_sequence(naive_implementation, dtype=dtype)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray._where [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py]
    def _where(self, mask: npt.NDArray[np.bool_], value) -> Self:
        # the super() method NDArrayBackedExtensionArray._where uses
        # np.putmask which doesn't properly handle None/pd.NA, so using the
        # base class implementation that uses __setitem__
        return ExtensionArray._where(self, mask, value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py::_where_standard [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/expressions.py]
def _where_standard(cond, left_op, right_op):
    # Caller is responsible for extracting ndarray if necessary
    return np.where(cond, left_op, right_op)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI
```
