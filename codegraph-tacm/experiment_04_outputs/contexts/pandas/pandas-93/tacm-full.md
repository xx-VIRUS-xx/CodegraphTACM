# pandas-93 :: tacm-full

query: BUG: DTI/TDI/PI `where` accepting non-matching dtypes (#30791)

## selected nodes

- rank=1 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=2 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=3 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=4 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=5 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex._parsed_string_to_bounds file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py
- rank=6 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_get file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=7 layer=FUNCTION tokens=316 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._maybe_cast_slice_bound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=8 layer=FUNCTION tokens=343 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=9 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/common.py::result_type_many file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/common.py
- rank=10 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=11 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_require_matching_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=12 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::_test_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py
- rank=13 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=14 layer=FUNCTION tokens=222 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::invalidate_string_dtypes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=15 layer=FUNCTION tokens=1031 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._get_join_indexers file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=16 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::DatetimeIndexConstructor.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py]
    def tdi(self, monotonic):
        tdi = timedelta_range("1 Day", periods=10)
        if monotonic == "decreasing":
            tdi = tdi[::-1]
        elif monotonic is None:
            taker = np.arange(10, dtype=np.intp)
            np.random.default_rng(2).shuffle(taker)
            tdi = tdi.take(taker)
        return tdi

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py::TimedeltaIndex._parsed_string_to_bounds [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/timedeltas.py]
    def _parsed_string_to_bounds(self, reso: Resolution, parsed: Timedelta):
        # reso is unused, included to match signature of DTI/PI
        lbound = parsed.round(parsed.resolution_string)
        rbound = (
            lbound
            + to_offset(parsed.resolution_string)
            - Timedelta(1, unit=self.unit).as_unit(self.unit)
        )
        return lbound, rbound

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._maybe_cast_slice_bound [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _maybe_cast_slice_bound(self, label, side: str):
        """
        If label is a string, cast it to scalar type according to resolution.

        Parameters
        ----------
        label : object
        side : {'left', 'right'}

        Returns
        -------
        label : object

        Notes
        -----
        Value of `side` parameter should be validated in caller.
        """
        if isinstance(label, str):
            try:
                parsed, reso = self._parse_with_reso(label)
            except ValueError as err:
                # DTI -> parsing.DateParseError
                # TDI -> 'unit abbreviation w/o a number'
                # PI -> string cannot be parsed as datetime-like
                self._raise_invalid_indexer("slice", label, err)

            lower, upper = self._parsed_string_to_bounds(reso, parsed)
            return lower if side == "left" else upper
        elif not isinstance(label, self._data._recognized_scalars):
            self._raise_invalid_indexer("slice", label)

        return label

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/common.py::result_type_many [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/common.py]
def result_type_many(*arrays_and_dtypes):
    """
    Wrapper around numpy.result_type which overcomes the NPY_MAXARGS (32)
    argument limit.
    """
    try:
        return np.result_type(*arrays_and_dtypes)
    except ValueError:
        # we have > NPY_MAXARGS terms in our expression
        return reduce(np.result_type, arrays_and_dtypes)
    except TypeError:
        from pandas.core.dtypes.cast import find_common_type
        from pandas.core.dtypes.common import is_extension_array_dtype

        arr_and_dtypes = list(arrays_and_dtypes)
        ea_dtypes, non_ea_dtypes = [], []
        for arr_or_dtype in arr_and_dtypes:
            if is_extension_array_dtype(arr_or_dtype):
                ea_dtypes.append(arr_or_dtype)
            else:
                non_ea_dtypes.append(arr_or_dtype)

        if non_ea_dtypes:
            try:
                np_dtype = np.result_type(*non_ea_dtypes)
            except ValueError:
                np_dtype = reduce(np.result_type, arrays_and_dtypes)
            return find_common_type([*ea_dtypes, np_dtype])

        return find_common_type(ea_dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py]
    def dta(self, dta_dti):
        dta, dti = dta_dti
        return dta

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._maybe_require_matching_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _maybe_require_matching_dtypes(
        self, left_join_keys: list[ArrayLike], right_join_keys: list[ArrayLike]
    ) -> None:
        # Overridden by AsOfMerge
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::_test_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py]
def _test_series(dti):
    return Series(np.random.default_rng(2).random(len(dti)), dti)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def setup(self):
        dti = date_range("2016-01-01", periods=10000, tz="US/Pacific")
        dti2 = dti.tz_convert("UTC")
        self.dti = dti
        self.dti2 = dti2

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::invalidate_string_dtypes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def invalidate_string_dtypes(dtype_set: set[DtypeObj]) -> None:
    """
    Change string like dtypes to object for
    ``DataFrame.select_dtypes()``.
    """
    # error: Argument 1 to <set> has incompatible type "Type[generic]"; expected
    # "Union[dtype[Any], ExtensionDtype, None]"
    # error: Argument 2 to <set> has incompatible type "Type[generic]"; expected
    # "Union[dtype[Any], ExtensionDtype, None]"
    non_string_dtypes = dtype_set - {
        np.dtype("S").type,  # type: ignore[arg-type]
        np.dtype("<U").type,  # type: ignore[arg-type]
    }
    if non_string_dtypes != dtype_set:
        raise TypeError(
            "numpy string dtypes are not allowed, use 'str' or 'object' instead"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_AsOfMerge._get_join_indexers [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _get_join_indexers(self) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """return the join indexers"""

        # values to compare
        left_values = (
            self.left.index._values if self.left_index else self.left_join_keys[-1]
        )
        right_values = (
            self.right.index._values if self.right_index else self.right_join_keys[-1]
        )

        # _maybe_require_matching_dtypes already checked for dtype matching
        assert left_values.dtype == right_values.dtype

        tolerance = self.tolerance
        if tolerance is not None:
            # TODO: can we reuse a tolerance-conversion function from
            #  e.g. TimedeltaIndex?
            if needs_i8_conversion(left_values.dtype) or (
                isinstance(left_values, ArrowExtensionArray)
                and left_values.dtype.kind in "mM"
            ):
                tolerance = Timedelta(tolerance)
                # TODO: we have no test cases with PeriodDtype here; probably
                #  need to adjust tolerance for that case.
                if left_values.dtype.kind in "mM":
                    # Make sure the i8 representation for tolerance
                    #  matches that for left_values/right_values.
                    if isinstance(left_values, ArrowExtensionArray):
                        unit = left_values.dtype.pyarrow_dtype.unit
                    else:
                        unit = ensure_wrapped_if_datetimelike(left_values).unit
                    tolerance = tolerance.as_unit(unit)

                tolerance = tolerance._value

        # initial type conversion as needed
        left_values = self._convert_values_for_libjoin(left_values, "left")
        right_values = self._convert_values_for_libjoin(right_values, "right")

        # a "by" parameter requires special handling
        if self.left_by is not None:
            # remove 'on' parameter from values if one existed
            if self.left_index and self.right_index:
                left_join_keys = self.left_join_keys
                right_join_keys = self.right_join_keys
            else:
                left_join_keys = self.left_join_keys[0:-1]
                right_join_keys = self.right_join_keys[0:-1]

            mapped = [
                _factorize_keys(
                    left_join_keys[n],
                    right_join_keys[n],
                    sort=False,
                )
                for n in range(len(left_join_keys))
            ]

            if len(left_join_keys) == 1:
                left_by_values = mapped[0][0]
                right_by_values = mapped[0][1]
            else:
                arrs = [np.concatenate(m[:2]) for m in mapped]
                shape = tuple(m[2] for m in mapped)
                group_index = get_group_index(
                    arrs, shape=shape, sort=False, xnull=False
                )
                left_len = len(left_join_keys[0])
                left_by_values = group_index[:left_len]
                right_by_values = group_index[left_len:]

            left_by_values = ensure_int64(left_by_values)
            right_by_values = ensure_int64(right_by_values)

            # choose appropriate function by type
            func = _asof_by_function(self.direction)
            return func(  # pyright: ignore[reportOptionalCall]
                left_values,
                right_values,
                left_by_values,
                right_by_values,
                self.allow_exact_matches,
                tolerance,
            )
        else:
            # choose appropriate function by type
            func = _asof_by_function(self.direction)
            return func(  # pyright: ignore[reportOptionalCall]
                left_values,
                right_values,
                None,
                None,
                self.allow_exact_matches,
                tolerance,
                False,
            )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py::DatetimeIndexConstructor.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/ctors.py]
    def setup(self):
        N = 20_000
        dti = date_range("1900-01-01", periods=N)

        self.list_of_timestamps = dti.tolist()
        self.list_of_dates = dti.date.tolist()
        self.list_of_datetimes = dti.to_pydatetime().tolist()
        self.list_of_str = dti.strftime("%Y-%m-%d").tolist()
```
