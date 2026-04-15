# pandas-17 :: hybrid

query: BUG: DTI/TDI.insert doing invalid casting (#33703)

## selected nodes

- rank=1 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=2 layer=FUNCTION tokens=316 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._maybe_cast_slice_bound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=3 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=4 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py::TestMaybeCastSliceBound.tdi file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_indexing.py
- rank=5 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestInsertIndexCoercion._assert_insert_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py
- rank=6 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py::IntegerDtype._safe_cast file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py
- rank=7 layer=FUNCTION tokens=374 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=8 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::_test_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py
- rank=9 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericDtype._safe_cast file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py
- rank=10 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py
- rank=11 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=12 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=13 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/floating.py::FloatingDtype._safe_cast file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/floating.py
- rank=14 layer=FUNCTION tokens=756 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.coerce_to_target_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=15 layer=FUNCTION tokens=429 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLTable.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=16 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py::ArrowStringArray.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py
- rank=17 layer=FUNCTION tokens=137 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::BaseEngine.insert_records file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=18 layer=FUNCTION tokens=263 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._validate_fill_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=19 layer=FUNCTION tokens=159 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta_dti file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=20 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray._validate_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py
- rank=21 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py]
    def dta(self, dta_dti):
        dta, dti = dta_dti
        return dta

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_add_dti_offset(self, offset):
        with warnings.catch_warnings(record=True):
            self.rng + offset

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestInsertIndexCoercion._assert_insert_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py]
    def _assert_insert_conversion(self, original, value, expected, expected_dtype):
        """test coercion triggered by insert"""
        target = original.copy()
        res = target.insert(1, value)
        tm.assert_index_equal(res, expected)
        assert res.dtype == expected_dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py::IntegerDtype._safe_cast [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/integer.py]
    def _safe_cast(cls, values: np.ndarray, dtype: np.dtype, copy: bool) -> np.ndarray:
        """
        Safely cast the values to the given dtype.

        "safe" in this context means the casting is lossless. e.g. if 'values'
        has a floating dtype, each value must be an integer.
        """
        try:
            return values.astype(dtype, casting="safe", copy=copy)
        except TypeError as err:
            casted = values.astype(dtype, copy=copy)
            if (casted == values).all():
                return casted

            raise TypeError(
                f"cannot safely cast non-equivalent {values.dtype} to {np.dtype(dtype)}"
            ) from err

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py]
    def insert(self, loc: int, item) -> Self:
        """
        Insert an item at the given position.

        This method creates a new ExtensionArray with the specified item
        inserted at the given index. The original array is not modified.

        Parameters
        ----------
        loc : int
            Index where the `item` needs to be inserted.
        item : scalar-like
            Value to be inserted.

        Returns
        -------
        ExtensionArray
            With `item` inserted at `loc`.

        See Also
        --------
        Index.insert: Make new Index inserting new item at location.

        Notes
        -----
        This method should be both type and dtype-preserving.  If the item
        cannot be held in an array of this type/dtype, either ValueError or
        TypeError should be raised.

        The default implementation relies on _from_sequence to raise on invalid
        items.

        Examples
        --------
        >>> arr = pd.array([1, 2, 3])
        >>> arr.insert(2, -1)
        <IntegerArray>
        [1, 2, -1, 3]
        Length: 4, dtype: Int64
        """
        loc = validate_insert_loc(loc, len(self))

        item_arr = type(self)._from_sequence([item], dtype=self.dtype)

        return type(self)._concat_same_type([self[:loc], item_arr, self[loc:]])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py::_test_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_resample_api.py]
def _test_series(dti):
    return Series(np.random.default_rng(2).random(len(dti)), dti)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py::NumericDtype._safe_cast [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numeric.py]
    def _safe_cast(cls, values: np.ndarray, dtype: np.dtype, copy: bool) -> np.ndarray:
        """
        Safely cast the values to the given dtype.

        "safe" in this context means the casting is lossless.
        """
        raise AbstractMethodError(cls)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py::BaseMaskedArray.insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/masked.py]
    def insert(self, loc: int, item) -> Self:
        if not is_valid_na_for_dtype(item, self.dtype):
            self._validate_setitem_value(item)
        return super().insert(loc, item)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_mismatched_tz(self):
        # reached via e.g.
        #  ser = Series(range(len(dti)), index=dti)
        #  ser[dti2]
        self.dti.get_indexer(self.dti2)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def setup(self):
        dti = date_range("2016-01-01", periods=10000, tz="US/Pacific")
        dti2 = dti.tz_convert("UTC")
        self.dti = dti
        self.dti2 = dti2

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/floating.py::FloatingDtype._safe_cast [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/floating.py]
    def _safe_cast(cls, values: np.ndarray, dtype: np.dtype, copy: bool) -> np.ndarray:
        """
        Safely cast the values to the given dtype.

        "safe" in this context means the casting is lossless.
        """
        # This is really only here for compatibility with IntegerDtype
        # Here for compat with IntegerDtype
        return values.astype(dtype, copy=copy)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.coerce_to_target_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def coerce_to_target_dtype(self, other, raise_on_upcast: bool) -> Block:
        """
        coerce the current block to a dtype compat for other
        we will return a block, possibly object, and not raise

        we can also safely try to coerce to the same dtype
        and will receive the same block
        """
        new_dtype = find_result_type(self.values.dtype, other)
        if new_dtype == self.dtype:
            if lib.is_np_dtype(new_dtype, "mM"):
                # GH#61671 e.g. datetime64[ns] column and a replacement value
                # outside ns range. find_common_type picked the highest
                # resolution which can't represent the value.
                raise OutOfBoundsDatetime(
                    f"Incompatible (high-resolution) value for "
                    f"dtype='{self.dtype}'. "
                    "Explicitly cast before operating."
                )
            # GH#52927 avoid RecursionError
            raise AssertionError(
                "Something has gone wrong, please report a bug at "
                "https://github.com/pandas-dev/pandas/issues"
            )

        # In a future version of pandas, the default will be that
        # setting `nan` into an integer series won't raise.
        if (
            is_scalar(other)
            and is_integer_dtype(self.values.dtype)
            and isna(other)
            and other is not NaT
            and not (
                isinstance(other, (np.datetime64, np.timedelta64)) and np.isnat(other)
            )
        ):
            raise_on_upcast = False
        elif (
            isinstance(other, np.ndarray)
            and other.ndim == 1
            and is_integer_dtype(self.values.dtype)
            and is_float_dtype(other.dtype)
            and lib.has_only_ints_or_nan(other)
        ):
            raise_on_upcast = False

        if raise_on_upcast:
            raise TypeError(f"Invalid value '{other}' for dtype '{self.values.dtype}'")
        if self.values.dtype == new_dtype:
            raise AssertionError(
                f"Did not expect new dtype {new_dtype} to equal self.dtype "
                f"{self.values.dtype}. Please report a bug at "
                "https://github.com/pandas-dev/pandas/issues."
            )
        try:
            return self.astype(new_dtype)
        except OutOfBoundsDatetime as err:
            # e.g. GH#56419 if self.dtype is a low-resolution dt64 and we try to
            #  upcast to a higher-resolution dt64, we may have entries that are
            #  out of bounds for the higher resolution.
            #  Re-raise with a more informative message.
            raise OutOfBoundsDatetime(
                f"Incompatible (high-resolution) value for dtype='{self.dtype}'. "
                "Explicitly cast before operating."
            ) from err

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLTable.insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py]
    def insert(
        self,
        chunksize: int | None = None,
        method: Literal["multi"] | Callable | None = None,
    ) -> int | None:
        # set insert method
        if method is None:
            exec_insert = self._execute_insert
        elif method == "multi":
            exec_insert = self._execute_insert_multi
        elif callable(method):
            exec_insert = partial(method, self)
        else:
            raise ValueError(f"Invalid parameter `method`: {method}")

        keys, data_list = self.insert_data()

        nrows = len(self.frame)

        if nrows == 0:
            return 0

        if chunksize is None:
            chunksize = nrows
        elif chunksize == 0:
            raise ValueError("chunksize argument should be non-zero")

        chunks = (nrows // chunksize) + 1
        total_inserted = None
        with self.pd_sql.run_transaction() as conn:
            for i in range(chunks):
                start_i = i * chunksize
                end_i = min((i + 1) * chunksize, nrows)
                if start_i >= end_i:
                    break

                chunk_iter = zip(
                    *(arr[start_i:end_i] for arr in data_list), strict=True
                )
                num_inserted = exec_insert(conn, keys, chunk_iter)
                # GH 46891
                if num_inserted is not None:
                    if total_inserted is None:
                        total_inserted = num_inserted
                    else:
                        total_inserted += num_inserted
        return total_inserted

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py::ArrowStringArray.insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py]
    def insert(self, loc: int, item) -> ArrowStringArray:
        if self.dtype.na_value is np.nan and item is np.nan:
            item = libmissing.NA
        if not isinstance(item, str) and item is not libmissing.NA:
            raise TypeError(
                f"Invalid value '{item}' for dtype 'str'. Value should be a "
                f"string or missing value, got '{type(item).__name__}' instead."
            )
        return super().insert(loc, item)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::BaseEngine.insert_records [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py]
    def insert_records(
        self,
        table: SQLTable,
        con,
        frame,
        name: str,
        index: bool | str | list[str] | None = True,
        schema=None,
        chunksize: int | None = None,
        method=None,
        **engine_kwargs,
    ) -> int | None:
        """
        Inserts data into already-prepared table
        """
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._validate_fill_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _validate_fill_value(self, value: object) -> object:
        """
        Check if the value can be inserted into our array without casting,
        and convert it to an appropriate native type if necessary.

        Raises
        ------
        TypeError
            If the value cannot be inserted into an array of this dtype.
        """
        dtype = self.dtype
        if isinstance(dtype, np.dtype) and dtype.kind not in "mM":
            if isinstance(value, tuple) and dtype != object:
                # GH#54385
                raise TypeError
            try:
                return np_can_hold_element(dtype, value)
            except LossySetitemError as err:
                # re-raise as TypeError for consistency
                raise TypeError from err
        elif not can_hold_element(self._values, value):
            raise TypeError
        return value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta_dti [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py]
    def dta_dti(self, unit, dtype):
        tz = getattr(dtype, "tz", None)

        dti = pd.date_range("2016-01-01", periods=55, freq="D", tz=tz, unit="ns")
        if tz is None:
            arr = np.asarray(dti).astype(f"M8[{unit}]")
        else:
            arr = np.asarray(dti.tz_convert("UTC").tz_localize(None)).astype(
                f"M8[{unit}]"
            )

        dta = DatetimeArray._simple_new(arr, dtype=dtype)
        return dta, dti

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray._validate_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py]
    def _validate_scalar(self, value):
        # used by NDArrayBackedExtensionIndex.insert
        if isna(value):
            return self.dtype.na_value
        elif not isinstance(value, str):
            raise TypeError(
                f"Invalid value '{value}' for dtype '{self.dtype}'. Value should be a "
                f"string or missing value, got '{type(value).__name__}' instead."
            )
        return value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::iat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def iat(x):
    return x.iat
```
