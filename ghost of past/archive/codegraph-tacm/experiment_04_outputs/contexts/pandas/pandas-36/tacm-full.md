# pandas-36 :: tacm-full

query: BUG: isna_old with td64, dt64tz, period (#33158)

## selected nodes

- rank=1 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::TestSetitemNADatetimeLikeDtype.is_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=2 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.any file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=3 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.all file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=4 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=5 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._extended_gcd file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py
- rank=6 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::_make_2d_ea_df file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py
- rank=7 layer=FUNCTION tokens=227 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/scope.py::Scope.swapkey file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/scope.py
- rank=8 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=9 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_misc.py::_Options.use file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_misc.py
- rank=10 layer=FUNCTION tokens=219 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::simple_period_range_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py
- rank=11 layer=FUNCTION tokens=216 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_with_missing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=12 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py::_f4 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py
- rank=13 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py::EWMMeanState.run_ewm file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py
- rank=14 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::_simple_period_range_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py
- rank=15 layer=FUNCTION tokens=515 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::get_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=16 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestBlockManager._compare file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py
- rank=17 layer=FUNCTION tokens=533 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py::online_ewma file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py
- rank=18 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::TestSetitemNADatetimeLikeDtype.is_inplace [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py]
    def is_inplace(self, val, obj):
        # td64   -> cast to object iff val is datetime64("NaT")
        # dt64   -> cast to object iff val is timedelta64("NaT")
        # dt64tz -> cast to object with anything _but_ NaT
        return val is NaT or val is None or val is np.nan or obj.dtype == val.dtype

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.any [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def any(self, *, axis: AxisInt | None = None, skipna: bool = True) -> bool:
        # GH#34479 the nanops call will raise a TypeError for non-td64 dtype
        return nanops.nanany(self._ndarray, axis=axis, skipna=skipna, mask=self.isna())

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps.all [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def all(self, *, axis: AxisInt | None = None, skipna: bool = True) -> bool:
        # GH#34479 the nanops call will raise a TypeError for non-td64 dtype

        return nanops.nanall(self._ndarray, axis=axis, skipna=skipna, mask=self.isna())

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py::RangeIndex._extended_gcd [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/range.py]
    def _extended_gcd(self, a: int, b: int) -> tuple[int, int, int]:
        """
        Extended Euclidean algorithms to solve Bezout's identity:
           a*x + b*y = gcd(x, y)
        Finds one particular solution for x, y: s, t
        Returns: gcd, s, t
        """
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = b, a
        while r:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        return old_r, old_s, old_t

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::_make_2d_ea_df [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py]
def _make_2d_ea_df(col_arrays, col_names):
    """
    Construct a DataFrame with a single 2D ExtensionArray block.

    Used for dt64tz and period types which support 2D blocks but don't
    consolidate automatically.
    """
    ea_type = type(col_arrays[0])
    ea_2d = ea_type._simple_new(
        np.stack([arr._ndarray for arr in col_arrays]),
        dtype=col_arrays[0].dtype,
    )
    return DataFrame(ea_2d.T, columns=col_names)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/scope.py::Scope.swapkey [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/computation/scope.py]
    def swapkey(self, old_key: str, new_key: str, new_value=None) -> None:
        """
        Replace a variable name, with a potentially new value.

        Parameters
        ----------
        old_key : str
            Current variable name to replace
        new_key : str
            New variable name to replace `old_key` with
        new_value : object
            Value to be replaced along with the possible renaming
        """
        if self.has_resolvers:
            maps = self.resolvers.maps + self.scope.maps
        else:
            maps = self.scope.maps

        maps.append(self.temps)

        for mapping in maps:
            if old_key in mapping:
                mapping[new_key] = new_value
                return

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::_create_mi_with_dt64tz_level [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def _create_mi_with_dt64tz_level():
    """
    MultiIndex with a level that is a tzaware DatetimeIndex.
    """
    # GH#8367 round trip with pickle
    return MultiIndex.from_product(
        [[1, 2], ["a", "b"], date_range("20130101", periods=3, tz="US/Eastern")],
        names=["one", "two", "three"],
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_misc.py::_Options.use [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_misc.py]
    def use(self, key, value) -> Generator[_Options]:
        """
        Temporarily set a parameter value using the with statement.
        Aliasing allowed.
        """
        old_value = self[key]
        try:
            self[key] = value
            yield self
        finally:
            self[key] = old_value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::simple_period_range_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py]
def simple_period_range_series():
    """
    Series with period range index and random data for test purposes.
    """

    def _simple_period_range_series(start, end, freq="D"):
        with warnings.catch_warnings():
            # suppress Period[B] deprecation warning
            msg = "|".join(["Period with BDay freq", r"PeriodDtype\[B\] is deprecated"])
            warnings.filterwarnings(
                "ignore",
                msg,
                category=FutureWarning,
            )
            rng = period_range(start, end, freq=freq)
        return Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)

    return _simple_period_range_series

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_with_missing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def index_with_missing(request):
    """
    Fixture for indices with missing values.

    Integer-dtype and empty cases are excluded because they cannot hold missing
    values.

    MultiIndex is excluded because isna() is not defined for MultiIndex.
    """
    ind = indices_dict[request.param]
    if request.param in ["tuples", "mi-with-dt64tz-level", "multi"]:
        # For setting missing values in the top level of MultiIndex
        vals = ind.tolist()
        vals[0] = (None, *vals[0][1:])
        vals[-1] = (None, *vals[-1][1:])
        return MultiIndex.from_tuples(vals)
    else:
        vals = ind.values.copy()
        vals[0] = None
        vals[-1] = None
        return type(ind)(vals, copy=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py::_f4 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/util/test_deprecate_kwarg.py]
def _f4(old=True, unchanged=True):
    return old, unchanged

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py::EWMMeanState.run_ewm [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py]
    def run_ewm(self, weighted_avg, deltas, min_periods, ewm_func):
        result, old_wt = ewm_func(
            weighted_avg,
            deltas,
            min_periods,
            self.old_wt_factor,
            self.new_wt,
            self.old_wt,
            self.adjust,
            self.ignore_na,
        )
        self.old_wt = old_wt
        self.last_ewm = result[-1]
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py::_simple_period_range_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/test_period_index.py]
    def _simple_period_range_series(start, end, freq="D"):
        with warnings.catch_warnings():
            # suppress Period[B] deprecation warning
            msg = "|".join(["Period with BDay freq", r"PeriodDtype\[B\] is deprecated"])
            warnings.filterwarnings(
                "ignore",
                msg,
                category=FutureWarning,
            )
            rng = period_range(start, end, freq=freq)
        return Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::get_values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static PyObject *get_values(PyObject *obj) {
  PyObject *values = NULL;

  if (object_is_index_type(obj) || object_is_series_type(obj)) {
    // The special cases to worry about are dt64tz and category[dt64tz].
    //  In both cases we want the UTC-localized datetime64 ndarray,
    //  without going through and object array of Timestamps.
    if (PyObject_HasAttrString(obj, "tz")) {
      PyObject *tz = PyObject_GetAttrString(obj, "tz");
      if (tz != Py_None) {
        // Go through object array if we have dt64tz, since tz info will
        // be lost if values is used directly.
        Py_DECREF(tz);
        values = PyObject_CallMethod(obj, "__array__", NULL);
        return values;
      }
      Py_DECREF(tz);
    }
    values = PyObject_GetAttrString(obj, "values");
    if (values == NULL) {
      // Clear so we can subsequently try another method
      PyErr_Clear();
    } else if (PyObject_HasAttrString(values, "__array__")) {
      // We may have gotten a Categorical or Sparse array so call np.array
      PyObject *array_values = PyObject_CallMethod(values, "__array__", NULL);
      Py_DECREF(values);
      values = array_values;
    } else if (!PyArray_CheckExact(values)) {
      // Didn't get a numpy array, so keep trying
      Py_DECREF(values);
      values = NULL;
    }
  }

  if (values == NULL) {
    PyObject *typeRepr = PyObject_Repr((PyObject *)Py_TYPE(obj));
    PyObject *repr;
    if (PyObject_HasAttrString(obj, "dtype")) {
      PyObject *dtype = PyObject_GetAttrString(obj, "dtype");
      repr = PyObject_Repr(dtype);
      Py_DECREF(dtype);
    } else {
      repr = PyUnicode_FromString("<unknown dtype>");
    }

    PyErr_Format(PyExc_ValueError, "%R or %R are not JSON serializable yet",
                 repr, typeRepr);
    Py_DECREF(repr);
    Py_DECREF(typeRepr);

    return NULL;
  }

  return values;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestBlockManager._compare [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py]
        def _compare(old_mgr, new_mgr):
            """compare the blocks, numeric compare ==, object don't"""
            old_blocks = set(old_mgr.blocks)
            new_blocks = set(new_mgr.blocks)
            assert len(old_blocks) == len(new_blocks)

            # compare non-numeric
            for b in old_blocks:
                found = False
                for nb in new_blocks:
                    if (b.values == nb.values).all():
                        found = True
                        break
                assert found

            for b in new_blocks:
                found = False
                for ob in old_blocks:
                    if (b.values == ob.values).all():
                        found = True
                        break
                assert found

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py::online_ewma [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/online.py]
    def online_ewma(
        values: np.ndarray,
        deltas: np.ndarray,
        minimum_periods: int,
        old_wt_factor: float,
        new_wt: float,
        old_wt: np.ndarray,
        adjust: bool,
        ignore_na: bool,
    ):
        """
        Compute online exponentially weighted mean per column over 2D values.

        Takes the first observation as is, then computes the subsequent
        exponentially weighted mean accounting minimum periods.
        """
        result = np.empty(values.shape)
        weighted_avg = values[0].copy()
        nobs = (~np.isnan(weighted_avg)).astype(np.int64)
        result[0] = np.where(nobs >= minimum_periods, weighted_avg, np.nan)

        for i in range(1, len(values)):
            cur = values[i]
            is_observations = ~np.isnan(cur)
            nobs += is_observations.astype(np.int64)
            for j in numba.prange(len(cur)):
                if not np.isnan(weighted_avg[j]):
                    if is_observations[j] or not ignore_na:
                        # note that len(deltas) = len(vals) - 1 and deltas[i] is to be
                        # used in conjunction with vals[i+1]
                        old_wt[j] *= old_wt_factor ** deltas[j - 1]
                        if is_observations[j]:
                            # avoid numerical errors on constant series
                            if weighted_avg[j] != cur[j]:
                                weighted_avg[j] = (
                                    (old_wt[j] * weighted_avg[j]) + (new_wt * cur[j])
                                ) / (old_wt[j] + new_wt)
                            if adjust:
                                old_wt[j] += new_wt
                            else:
                                old_wt[j] = 1.0
                elif is_observations[j]:
                    weighted_avg[j] = cur[j]

            result[i] = np.where(nobs >= minimum_periods, weighted_avg, np.nan)

        return result, old_wt

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
```
