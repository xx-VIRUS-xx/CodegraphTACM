# pandas-55 :: codesearch

query: BUG: Fix incorrect _is_scalar_access check in iloc (#32085)

## selected nodes

- rank=1 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=2 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Term.is_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=3 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=4 layer=FUNCTION tokens=275 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocIndexer._is_scalar_access file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=5 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._check_indexing_error file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=6 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.is_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=7 layer=FUNCTION tokens=560 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::TestMaskedArrays.check_accumulate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py
- rank=8 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray._validate_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py
- rank=9 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_arrow_string_mixins.py::ArrowStringArrayMixin._str_isascii file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_arrow_string_mixins.py
- rank=10 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::using_python_scalars file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=11 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::extract_utc_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c
- rank=12 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray._validate_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py
- rank=13 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=14 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c::uint64_conflict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c
- rank=15 layer=FUNCTION tokens=254 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/common.py::check_indexing_smoketest_or_raises file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/common.py
- rank=16 layer=FUNCTION tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_arrow.py::TestArrowArray.check_accumulate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_arrow.py
- rank=17 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::TestPeriodArray._supports_accumulation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py
- rank=18 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py::TestDatetimeArray._supports_accumulation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py
- rank=19 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::BinOp._disallow_scalar_only_bool_ops file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py
- rank=20 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_round_trip.py::_check_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_round_trip.py
- rank=21 layer=FUNCTION tokens=226 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::BinOp._disallow_scalar_only_bool_ops file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py
- rank=22 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/libs.py::ScalarListLike.time_is_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/libs.py
- rank=23 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/ops.py::BaseOpsUtil.check_opname file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/ops.py
- rank=24 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/accumulate.py::BaseAccumulateTests.check_accumulate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/accumulate.py
- rank=25 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::TestMaskedArrays._supports_accumulation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py
- rank=26 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::assert_indexing_slices_equivalent file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py
- rank=27 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._raise_scalar_data_error file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=28 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_arrow_string_mixins.py::ArrowStringArrayMixin._str_isalpha file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_arrow_string_mixins.py
- rank=29 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/__init__.py::using_python_scalars file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/__init__.py
- rank=30 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/common.py::has_castable_attr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/common.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._is_scalar_access [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _is_scalar_access(self, key: tuple):
        raise NotImplementedError

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Term.is_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py]
    def is_scalar(self) -> bool:
        return is_scalar(self._value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_iLocIndexer._is_scalar_access [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _is_scalar_access(self, key: tuple) -> bool:
        """
        Returns
        -------
        bool
        """
        # this is a shortcut accessor to both .loc and .iloc
        # that provide the equivalent access of .at and .iat
        # a) avoid getting things via sections and (to minimize dtype changes)
        # b) provide a performant path
        if len(key) != self.ndim:
            return False

        return all(is_integer(k) for k in key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocIndexer._is_scalar_access [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _is_scalar_access(self, key: tuple) -> bool:
        """
        Returns
        -------
        bool
        """
        # this is a shortcut accessor to both .loc and .iloc
        # that provide the equivalent access of .at and .iat
        # a) avoid getting things via sections and (to minimize dtype changes)
        # b) provide a performant path
        if len(key) != self.ndim:
            return False

        for i, k in enumerate(key):
            if not is_scalar(k):
                return False

            ax = self.obj.axes[i]
            if isinstance(ax, MultiIndex):
                return False

            if isinstance(k, str) and ax._supports_partial_string_indexing:
                # partial string indexing, df.loc['2000', 'A']
                # should not be considered scalar
                return False

            if not ax._index_as_unique:
                return False

        return True

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._check_indexing_error [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _check_indexing_error(self, key: object) -> None:
        if not is_scalar(key):
            # if key is not a scalar, directly raise an error (the code below
            # would convert to numpy arrays and raise later any way) - GH29926
            raise InvalidIndexError(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::Op.is_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py]
    def is_scalar(self) -> bool:
        return all(operand.is_scalar for operand in self.operands)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::TestMaskedArrays.check_accumulate [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py]
    def check_accumulate(self, ser: pd.Series, op_name: str, skipna: bool):
        # overwrite to ensure pd.NA is tested instead of np.nan
        # https://github.com/pandas-dev/pandas/issues/30958
        length = 64
        if is_windows_or_32bit:
            # Item "ExtensionDtype" of "Union[dtype[Any], ExtensionDtype]" has
            # no attribute "itemsize"
            if not ser.dtype.itemsize == 8:  # type: ignore[union-attr]
                length = 32

        if ser.dtype.name.startswith("U"):
            expected_dtype = f"UInt{length}"
        elif ser.dtype.name.startswith("I"):
            expected_dtype = f"Int{length}"
        elif ser.dtype.name.startswith("F"):
            # Incompatible types in assignment (expression has type
            # "Union[dtype[Any], ExtensionDtype]", variable has type "str")
            expected_dtype = ser.dtype  # type: ignore[assignment]
        elif ser.dtype.kind == "b":
            if op_name in ("cummin", "cummax"):
                expected_dtype = "boolean"
            else:
                expected_dtype = f"Int{length}"

        if expected_dtype == "Float32" and op_name == "cumprod" and skipna:
            # TODO: xfail?
            pytest.skip(
                f"Float32 precision lead to large differences with op {op_name} "
                f"and skipna={skipna}"
            )

        if op_name == "cumsum":
            pass
        elif op_name in ["cummax", "cummin"]:
            expected_dtype = ser.dtype  # type: ignore[assignment]
        elif op_name == "cumprod":
            ser = ser[:12]
        else:
            raise NotImplementedError(f"{op_name} not supported")

        result = getattr(ser, op_name)(skipna=skipna)
        expected = pd.Series(
            pd.array(
                getattr(ser.astype("float64"), op_name)(skipna=skipna),
                dtype="Float64",
            )
        )
        expected[np.isnan(expected)] = pd.NA
        expected = expected.astype(expected_dtype)
        tm.assert_series_equal(result, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py::NDArrayBackedExtensionArray._validate_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_mixins.py]
    def _validate_scalar(self, value):
        # used by NDArrayBackedExtensionIndex.insert
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_arrow_string_mixins.py::ArrowStringArrayMixin._str_isascii [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_arrow_string_mixins.py]
    def _str_isascii(self):
        result = pc.string_is_ascii(self._pa_array)
        return self._convert_bool_result(result)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::using_python_scalars [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def using_python_scalars() -> bool:
    return pd.options.future.python_scalars is True

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c::extract_utc_offset [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/numpy/datetime/np_datetime.c]
PyObject *extract_utc_offset(PyObject *obj) {
  PyObject *tmp = PyObject_GetAttrString(obj, "tzinfo");
  if (tmp == NULL) {
    return NULL;
  }
  if (tmp != Py_None) {
    PyObject *offset = PyObject_CallMethod(tmp, "utcoffset", "O", obj);
    if (offset == NULL) {
      Py_DECREF(tmp);
      return NULL;
    }
    return offset;
  }
  return tmp;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py::IntervalArray._validate_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/interval.py]
    def _validate_scalar(self, value):
        if isinstance(value, Interval):
            self._check_closed_matches(value, name="value")
            left, right = value.left, value.right
            # TODO: check subdtype match like _validate_setitem_value?
        elif is_valid_na_for_dtype(value, self.left.dtype):
            # GH#18295
            left = right = self.left._na_value
        else:
            raise TypeError(
                "can only insert Interval objects and NA into an IntervalArray"
            )
        return left, right

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericSeriesIndexing.time_iloc_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_iloc_scalar(self, index, index_structure):
        self.data.iloc[800000]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c::uint64_conflict [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c]
int uint64_conflict(uint_state *self) {
  return self->seen_uint && (self->seen_sint || self->seen_null);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/common.py::check_indexing_smoketest_or_raises [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/common.py]
def check_indexing_smoketest_or_raises(
    obj,
    method: Literal["iloc", "loc"],
    key: Any,
    axes: Literal[0, 1] | None = None,
    fails=None,
) -> None:
    if axes is None:
        axes_list = [0, 1]
    else:
        assert axes in [0, 1]
        axes_list = [axes]

    for ax in axes_list:
        if ax < obj.ndim:
            # create a tuple accessor
            new_axes = [slice(None)] * obj.ndim
            new_axes[ax] = key
            axified = tuple(new_axes)
            try:
                getattr(obj, method).__getitem__(axified)
            except (IndexError, TypeError, KeyError) as detail:
                # if we are in fails, the ok, otherwise raise it
                if fails is not None:
                    if isinstance(detail, fails):
                        return
                raise

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_arrow.py::TestArrowArray.check_accumulate [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_arrow.py]
    def check_accumulate(self, ser, op_name, skipna):
        result = getattr(ser, op_name)(skipna=skipna)

        pa_type = ser.dtype.pyarrow_dtype
        if pa.types.is_temporal(pa_type):
            # Just check that we match the integer behavior.
            if pa_type.bit_width == 32:
                int_type = "int32[pyarrow]"
            else:
                int_type = "int64[pyarrow]"
            ser = ser.astype(int_type)
            result = result.astype(int_type)

        result = result.astype("Float64")
        expected = getattr(ser.astype("Float64"), op_name)(skipna=skipna)
        tm.assert_series_equal(result, expected, check_dtype=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py::TestPeriodArray._supports_accumulation [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_period.py]
    def _supports_accumulation(self, ser, op_name: str) -> bool:
        return op_name in ["cummin", "cummax"]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py::TestDatetimeArray._supports_accumulation [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_datetime.py]
    def _supports_accumulation(self, ser, op_name: str) -> bool:
        return op_name in ["cummin", "cummax"]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py::BinOp._disallow_scalar_only_bool_ops [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/pytables.py]
    def _disallow_scalar_only_bool_ops(self) -> None:
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_round_trip.py::_check_roundtrip [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/pytables/test_round_trip.py]
def _check_roundtrip(obj, comparator, path, compression=False, **kwargs):
    options = {}
    if compression:
        options["complib"] = "blosc"

    with HDFStore(path, "w", **options) as store:
        store["obj"] = obj
        retrieved = store["obj"]
        comparator(retrieved, obj, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py::BinOp._disallow_scalar_only_bool_ops [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/ops.py]
    def _disallow_scalar_only_bool_ops(self) -> None:
        rhs = self.rhs
        lhs = self.lhs

        # GH#24883 unwrap dtype if necessary to ensure we have a type object
        rhs_rt = rhs.return_type
        rhs_rt = getattr(rhs_rt, "type", rhs_rt)
        lhs_rt = lhs.return_type
        lhs_rt = getattr(lhs_rt, "type", lhs_rt)
        if (
            (lhs.is_scalar or rhs.is_scalar)
            and self.op in _bool_ops_dict
            and (
                not (
                    issubclass(rhs_rt, (bool, np.bool_))
                    and issubclass(lhs_rt, (bool, np.bool_))
                )
            )
        ):
            raise NotImplementedError("cannot evaluate scalar only bool ops")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/libs.py::ScalarListLike.time_is_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/libs.py]
    def time_is_scalar(self, param):
        is_scalar(param)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/ops.py::BaseOpsUtil.check_opname [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/ops.py]
    def check_opname(self, ser: pd.Series, op_name: str, other):
        exc = self._get_expected_exception(op_name, ser, other)
        op = self.get_op_from_name(op_name)

        self._check_op(ser, op, other, op_name, exc)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/accumulate.py::BaseAccumulateTests.check_accumulate [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/base/accumulate.py]
    def check_accumulate(self, ser: pd.Series, op_name: str, skipna: bool):
        try:
            alt = ser.astype("float64")
        except (TypeError, ValueError):
            # e.g. Period can't be cast to float64 (TypeError)
            #      String can't be cast to float64 (ValueError)
            alt = ser.astype(object)

        result = getattr(ser, op_name)(skipna=skipna)
        expected = getattr(alt, op_name)(skipna=skipna)
        tm.assert_series_equal(result, expected, check_dtype=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py::TestMaskedArrays._supports_accumulation [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_masked.py]
    def _supports_accumulation(self, ser: pd.Series, op_name: str) -> bool:
        return True

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py::assert_indexing_slices_equivalent [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/asserters.py]
def assert_indexing_slices_equivalent(ser: Series, l_slc: slice, i_slc: slice) -> None:
    """
    Check that ser.iloc[i_slc] matches ser.loc[l_slc] and, if applicable,
    ser[l_slc].
    """
    expected = ser.iloc[i_slc]

    assert_series_equal(ser.loc[l_slc], expected)

    if not is_integer_dtype(ser.index):
        # For integer indices, .loc and plain getitem are position-based.
        assert_series_equal(ser[l_slc], expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._raise_scalar_data_error [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _raise_scalar_data_error(cls, data: object) -> NoReturn:
        # We return the TypeError so that we can raise it from the constructor
        #  in order to keep mypy happy
        raise TypeError(
            f"{cls.__name__}(...) must be called with a collection of some "
            f"kind, {repr(data) if not isinstance(data, np.generic) else str(data)} "
            "was passed"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_arrow_string_mixins.py::ArrowStringArrayMixin._str_isalpha [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/_arrow_string_mixins.py]
    def _str_isalpha(self):
        result = pc.utf8_is_alpha(self._pa_array)
        return self._convert_bool_result(result)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/__init__.py::using_python_scalars [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/__init__.py]
def using_python_scalars() -> bool:
    from pandas._config.config import _global_config as config

    _mode_options = config["future"]
    return _mode_options["python_scalars"]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/common.py::has_castable_attr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/ops/common.py]
def has_castable_attr(obj) -> bool:
    attrs = ["__array__", "__dlpack__", "__arrow_c_array__", "__arrow_c_stream__"]
    return any(hasattr(obj, name) for name in attrs)
```
