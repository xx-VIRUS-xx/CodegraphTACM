# pandas-51 :: minilm

query: BUG: fix in categorical merges (#32079)

## selected nodes

- rank=1 layer=FUNCTION tokens=355 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._check_dtype_match file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=2 layer=FUNCTION tokens=524 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._maybe_require_matching_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=3 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical.tests_merge_categorical_unordered_equal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=4 layer=FUNCTION tokens=2326 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_coerce_merge_keys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=5 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_idx file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=6 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_cat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=7 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_col file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py
- rank=8 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_cross_merge file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=9 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_2intkey file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical.tests_merge_categorical_unordered_equal [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py]
    def tests_merge_categorical_unordered_equal(self):
        # GH-19551
        df1 = DataFrame(
            {
                "Foo": Categorical(["A", "B", "C"], categories=["A", "B", "C"]),
                "Left": ["A0", "B0", "C0"],
            }
        )

        df2 = DataFrame(
            {
                "Foo": Categorical(["C", "B", "A"], categories=["C", "B", "A"]),
                "Right": ["C1", "B1", "A1"],
            }
        )
        result = merge(df1, df2, on=["Foo"])
        expected = DataFrame(
            {
                "Foo": Categorical(["A", "B", "C"]),
                "Left": ["A0", "B0", "C0"],
                "Right": ["A1", "B1", "C1"],
            }
        )
        tm.assert_frame_equal(result, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_coerce_merge_keys [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _maybe_coerce_merge_keys(self) -> None:
        # we have valid merges but we may have to further
        # coerce these if they are originally incompatible types
        #
        # for example if these are categorical, but are not dtype_equal
        # or if we have object and integer dtypes

        for lk, rk, name in zip(
            self.left_join_keys, self.right_join_keys, self.join_names, strict=True
        ):
            if (len(lk) and not len(rk)) or (not len(lk) and len(rk)):
                continue

            lk = extract_array(lk, extract_numpy=True)
            rk = extract_array(rk, extract_numpy=True)

            lk_is_cat = isinstance(lk.dtype, CategoricalDtype)
            rk_is_cat = isinstance(rk.dtype, CategoricalDtype)
            lk_is_object_or_string = is_object_dtype(lk.dtype) or is_string_dtype(
                lk.dtype
            )
            rk_is_object_or_string = is_object_dtype(rk.dtype) or is_string_dtype(
                rk.dtype
            )

            # if either left or right is a categorical
            # then the must match exactly in categories & ordered
            if lk_is_cat and rk_is_cat:
                lk = cast("Categorical", lk)
                rk = cast("Categorical", rk)
                if lk._categories_match_up_to_permutation(rk):
                    continue

            elif lk_is_cat or rk_is_cat:
                pass

            elif lk.dtype == rk.dtype:
                continue

            msg = (
                f"You are trying to merge on {lk.dtype} and {rk.dtype} columns "
                f"for key '{name}'. If you wish to proceed you should use pd.concat"
            )

            # if we are numeric, then allow differing
            # kinds to proceed, eg. int64 and int8, int and float
            # further if we are object, but we infer to
            # the same, then proceed
            if is_numeric_dtype(lk.dtype) and is_numeric_dtype(rk.dtype):
                if lk.dtype.kind == rk.dtype.kind:
                    continue

                if isinstance(lk.dtype, ExtensionDtype) and not isinstance(
                    rk.dtype, ExtensionDtype
                ):
                    ct = find_common_type([lk.dtype, rk.dtype])
                    if isinstance(ct, ExtensionDtype):
                        com_cls = ct.construct_array_type()
                        rk = com_cls._from_sequence(rk, dtype=ct, copy=False)
                    else:
                        rk = rk.astype(ct, copy=False)
                elif isinstance(rk.dtype, ExtensionDtype):
                    ct = find_common_type([lk.dtype, rk.dtype])
                    if isinstance(ct, ExtensionDtype):
                        com_cls = ct.construct_array_type()
                        lk = com_cls._from_sequence(lk, dtype=ct, copy=False)
                    else:
                        lk = lk.astype(ct, copy=False)

                # check whether ints and floats
                if is_integer_dtype(rk.dtype) and is_float_dtype(lk.dtype):
                    # GH 47391 numpy > 1.24 will raise a RuntimeError for nan -> int
                    with np.errstate(invalid="ignore"):
                        # error: Argument 1 to "astype" of "ndarray" has incompatible
                        # type "Union[ExtensionDtype, Any, dtype[Any]]"; expected
                        # "Union[dtype[Any], Type[Any], _SupportsDType[dtype[Any]]]"
                        casted = lk.astype(rk.dtype)  # type: ignore[arg-type]

                    mask = ~np.isnan(lk)
                    match = lk == casted
                    # error: Item "ExtensionArray" of
                    # "ExtensionArray | Any" has no attribute "all"
                    if not match[mask].all():  # type: ignore[union-attr]
                        warnings.warn(
                            "You are merging on int and float "
                            "columns where the float values "
                            "are not equal to their int representation.",
                            UserWarning,
                            stacklevel=find_stack_level(),
                        )
                    continue

                if is_float_dtype(rk.dtype) and is_integer_dtype(lk.dtype):
                    # GH 47391 numpy > 1.24 will raise a RuntimeError for nan -> int
                    with np.errstate(invalid="ignore"):
                        # error: Argument 1 to "astype" of "ndarray" has incompatible
                        # type "Union[ExtensionDtype, Any, dtype[Any]]"; expected
                        # "Union[dtype[Any], Type[Any], _SupportsDType[dtype[Any]]]"
                        casted = rk.astype(lk.dtype)  # type: ignore[arg-type]

                    mask = ~np.isnan(rk)
                    match = rk == casted
                    # error: Item "ExtensionArray" of
                    # "ExtensionArray | Any" has no attribute "all"
                    if not match[mask].all():  # type: ignore[union-attr]
                        warnings.warn(
                            "You are merging on int and float "
                            "columns where the float values "
                            "are not equal to their int representation.",
                            UserWarning,
                            stacklevel=find_stack_level(),
                        )
                    continue

                # let's infer and see if we are ok
                if lib.infer_dtype(lk, skipna=False) == lib.infer_dtype(
                    rk, skipna=False
                ):
                    continue

            # Check if we are trying to merge on obviously
            # incompatible dtypes GH 9780, GH 15800

            # bool values are coerced to object
            elif (lk_is_object_or_string and is_bool_dtype(rk.dtype)) or (
                is_bool_dtype(lk.dtype) and rk_is_object_or_string
            ):
                pass

            # object values are allowed to be merged
            elif (lk_is_object_or_string and is_numeric_dtype(rk.dtype)) or (
                is_numeric_dtype(lk.dtype) and rk_is_object_or_string
            ):
                inferred_left = lib.infer_dtype(lk, skipna=False)
                inferred_right = lib.infer_dtype(rk, skipna=False)
                bool_types = ["integer", "mixed-integer", "boolean", "empty"]
                string_types = ["string", "unicode", "mixed", "bytes", "empty"]

                # inferred bool
                if inferred_left in bool_types and inferred_right in bool_types:
                    pass

                # unless we are merging non-string-like with string-like
                elif (
                    inferred_left in string_types and inferred_right not in string_types
                ) or (
                    inferred_right in string_types and inferred_left not in string_types
                ):
                    raise ValueError(msg)

            # datetimelikes must match exactly
            elif needs_i8_conversion(lk.dtype) and not needs_i8_conversion(rk.dtype):
                raise ValueError(msg)
            elif not needs_i8_conversion(lk.dtype) and needs_i8_conversion(rk.dtype):
                raise ValueError(msg)
            elif isinstance(lk.dtype, DatetimeTZDtype) and not isinstance(
                rk.dtype, DatetimeTZDtype
            ):
                raise ValueError(msg)
            elif not isinstance(lk.dtype, DatetimeTZDtype) and isinstance(
                rk.dtype, DatetimeTZDtype
            ):
                raise ValueError(msg)
            elif (
                isinstance(lk.dtype, DatetimeTZDtype)
                and isinstance(rk.dtype, DatetimeTZDtype)
            ) or (lk.dtype.kind == "M" and rk.dtype.kind == "M"):
                # allows datetime with different resolutions
                continue
            # datetime and timedelta not allowed
            elif lk.dtype.kind == "M" and rk.dtype.kind == "m":
                raise ValueError(msg)
            elif lk.dtype.kind == "m" and rk.dtype.kind == "M":
                raise ValueError(msg)

            elif is_object_dtype(lk.dtype) and is_object_dtype(rk.dtype):
                continue

            # Houston, we have a problem!
            # let's coerce to object if the dtypes aren't
            # categorical, otherwise coerce to the category
            # dtype. If we coerced categories to object,
            # then we would lose type information on some
            # columns, and end up trying to merge
            # incompatible dtypes. See GH 16900.
            if name in self.left.columns:
                typ = cast("Categorical", lk).categories.dtype if lk_is_cat else object
                self.left = self.left.copy(deep=False)
                self.left[name] = self.left[name].astype(typ)
            if name in self.right.columns:
                typ = cast("Categorical", rk).categories.dtype if rk_is_cat else object
                self.right = self.right.copy(deep=False)
                self.right[name] = self.right[name].astype(typ)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_idx [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_on_cat_idx(self):
        merge(self.left_cat_idx, self.right_cat_idx, on="X")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_cat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_cat(self):
        merge(self.left_cat, self.right_cat, on="X")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::MergeCategoricals.time_merge_on_cat_col [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_on_cat_col(self):
        merge(self.left_cat_col, self.right_cat_col, on="X")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_cross_merge [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
def _cross_merge(
    left: DataFrame,
    right: DataFrame,
    on: IndexLabel | AnyArrayLike | None = None,
    left_on: IndexLabel | AnyArrayLike | None = None,
    right_on: IndexLabel | AnyArrayLike | None = None,
    left_index: bool = False,
    right_index: bool = False,
    sort: bool = False,
    suffixes: Suffixes = ("_x", "_y"),
    indicator: str | bool = False,
    validate: str | None = None,
) -> DataFrame:
    """
    See merge.__doc__ with how='cross'
    """

    if (
        left_index
        or right_index
        or right_on is not None
        or left_on is not None
        or on is not None
    ):
        raise MergeError(
            "Can not pass on, right_on, left_on or set right_index=True or "
            "left_index=True"
        )

    return _CrossMergeOperation(
        left,
        right,
        suffixes=suffixes,
        indicator=indicator,
    ).get_result()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py::Merge.time_merge_2intkey [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/join_merge.py]
    def time_merge_2intkey(self, sort):
        merge(self.left, self.right, sort=sort)
```
