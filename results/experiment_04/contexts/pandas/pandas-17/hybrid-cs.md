# pandas-17 :: hybrid-cs

query: BUG: DTI/TDI.insert doing invalid casting (#33703)

## selected nodes

- rank=1 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestInsertIndexCoercion._assert_insert_conversion file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py
- rank=2 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py::ArrowStringArray.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_arrow.py
- rank=3 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=4 layer=FUNCTION tokens=429 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLTable.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=5 layer=FUNCTION tokens=831 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=6 layer=FUNCTION tokens=1709 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c::precise_xstrtod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c
- rank=7 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=8 layer=FUNCTION tokens=316 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._maybe_cast_slice_bound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=9 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newTrue file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=10 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py::StringArray._validate_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/string_.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py::TestInsertIndexCoercion._assert_insert_conversion [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_coercion.py]
    def _assert_insert_conversion(self, original, value, expected, expected_dtype):
        """test coercion triggered by insert"""
        target = original.copy()
        res = target.insert(1, value)
        tm.assert_index_equal(res, expected)
        assert res.dtype == expected_dtype

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def insert(self, loc: int, item: Hashable) -> Index:
        """
        Make new Index inserting new item at location.

        Follows Python numpy.insert semantics for negative values.

        Parameters
        ----------
        loc : int
            The integer location where the new item will be inserted.
        item : object
            The new item to be inserted into the Index.

        Returns
        -------
        Index
            Returns a new Index object resulting from inserting the specified item at
            the specified location within the original Index.

        See Also
        --------
        Index.append : Append a collection of Indexes together.

        Examples
        --------
        >>> idx = pd.Index(["a", "b", "c"])
        >>> idx.insert(1, "x")
        Index(['a', 'x', 'b', 'c'], dtype='str')
        """
        item = lib.item_from_zerodim(item)
        if is_valid_na_for_dtype(item, self.dtype) and self.dtype != object:
            item = self._na_value

        arr = self._values

        if using_string_dtype() and len(self) == 0 and self.dtype == np.object_:
            # special case: if we are an empty object-dtype Index, also
            # take into account the inserted item for the resulting dtype
            # (https://github.com/pandas-dev/pandas/pull/60797)
            dtype = self._find_common_type_compat(item)
            if dtype != self.dtype:
                return self.astype(dtype).insert(loc, item)

        try:
            if isinstance(arr, ExtensionArray):
                res_values = arr.insert(loc, item)
                return type(self)._simple_new(res_values, name=self.name)
            else:
                item = self._validate_fill_value(item)
        except (TypeError, ValueError, LossySetitemError):
            # e.g. trying to insert an integer into a DatetimeIndex
            #  We cannot keep the same dtype, so cast to the (often object)
            #  minimal shared dtype before doing the insert.
            dtype = self._find_common_type_compat(item)
            if dtype == self.dtype:
                # EA's might run into recursion errors if loc is invalid
                raise
            return self.astype(dtype).insert(loc, item)

        if arr.dtype != object or not isinstance(
            item, (tuple, np.datetime64, np.timedelta64)
        ):
            # with object-dtype we need to worry about numpy incorrectly casting
            # dt64/td64 to integer, also about treating tuples as sequences
            # special-casing dt64/td64 https://github.com/numpy/numpy/issues/12550
            casted = arr.dtype.type(item)
            new_values = np.insert(arr, loc, casted)

        else:
            # error: No overload variant of "insert" matches argument types
            # "ndarray[Any, Any]", "int", "None"
            new_values = np.insert(arr, loc, None)  # type: ignore[call-overload]
            loc = loc if loc >= 0 else loc - 1
            new_values[loc] = item

        # GH#51363 stopped doing dtype inference here
        out = Index(new_values, dtype=new_values.dtype, name=self.name, copy=False)
        return out

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c::precise_xstrtod [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c]
double precise_xstrtod(const char *str, char **endptr, char decimal, char sci,
                       char tsep, int skip_trailing, int *error,
                       int *maybe_int) {
  // Use fast_float for standard format (no tsep, sci='e'/'E').
  // fast_float provides IEEE 754 correctly-rounded parsing.
  if (tsep == '\0' && (sci == 'e' || sci == 'E')) {
    const char *p = str;
    while (isspace_ascii(*p))
      p++;

    // Only try fast_float for numeric-looking input (digit, sign+digit,
    // or decimal point). This avoids fast_float parsing "nan"/"inf" which
    // the original precise_xstrtod did not handle.
    const char *q = p;
    if (*q == '-' || *q == '+')
      q++;
    if (!isdigit_ascii(*q) && !(*q == decimal && isdigit_ascii(*(q + 1))))
      goto fallback;

    // Find end of token (next whitespace or NUL).
    const char *end = p;
    while (*end && !isspace_ascii(*end))
      end++;

    double value;
    const char *parsed_end;
    if (fast_float_strtod(p, end, &value, &parsed_end, decimal) == 0) {
      // Determine maybe_int by checking if we saw decimal or 'e'/'E'.
      if (maybe_int != NULL) {
        *maybe_int = 1;
        for (const char *c = p; c < parsed_end; c++) {
          if (*c == decimal || *c == 'e' || *c == 'E') {
            *maybe_int = 0;
            break;
          }
        }
      }
      if (skip_trailing)
        while (isspace_ascii(*parsed_end))
          parsed_end++;
      if (endptr)
        *endptr = (char *)parsed_end;
      return value;
    }
  }

fallback:
    // Fallback for non-standard formats (custom tsep, or sci char).
    ;
  const char *p = str;
  const int max_digits = 17;

  if (maybe_int != NULL)
    *maybe_int = 1;
  // Cache powers of 10 in memory.
  static double e[] = {
      1.,    1e1,   1e2,   1e3,   1e4,   1e5,   1e6,   1e7,   1e8,   1e9,
      1e10,  1e11,  1e12,  1e13,  1e14,  1e15,  1e16,  1e17,  1e18,  1e19,
      1e20,  1e21,  1e22,  1e23,  1e24,  1e25,  1e26,  1e27,  1e28,  1e29,
      1e30,  1e31,  1e32,  1e33,  1e34,  1e35,  1e36,  1e37,  1e38,  1e39,
      1e40,  1e41,  1e42,  1e43,  1e44,  1e45,  1e46,  1e47,  1e48,  1e49,
      1e50,  1e51,  1e52,  1e53,  1e54,  1e55,  1e56,  1e57,  1e58,  1e59,
      1e60,  1e61,  1e62,  1e63,  1e64,  1e65,  1e66,  1e67,  1e68,  1e69,
      1e70,  1e71,  1e72,  1e73,  1e74,  1e75,  1e76,  1e77,  1e78,  1e79,
      1e80,  1e81,  1e82,  1e83,  1e84,  1e85,  1e86,  1e87,  1e88,  1e89,
      1e90,  1e91,  1e92,  1e93,  1e94,  1e95,  1e96,  1e97,  1e98,  1e99,
      1e100, 1e101, 1e102, 1e103, 1e104, 1e105, 1e106, 1e107, 1e108, 1e109,
      1e110, 1e111, 1e112, 1e113, 1e114, 1e115, 1e116, 1e117, 1e118, 1e119,
      1e120, 1e121, 1e122, 1e123, 1e124, 1e125, 1e126, 1e127, 1e128, 1e129,
      1e130, 1e131, 1e132, 1e133, 1e134, 1e135, 1e136, 1e137, 1e138, 1e139,
      1e140, 1e141, 1e142, 1e143, 1e144, 1e145, 1e146, 1e147, 1e148, 1e149,
      1e150, 1e151, 1e152, 1e153, 1e154, 1e155, 1e156, 1e157, 1e158, 1e159,
      1e160, 1e161, 1e162, 1e163, 1e164, 1e165, 1e166, 1e167, 1e168, 1e169,
      1e170, 1e171, 1e172, 1e173, 1e174, 1e175, 1e176, 1e177, 1e178, 1e179,
      1e180, 1e181, 1e182, 1e183, 1e184, 1e185, 1e186, 1e187, 1e188, 1e189,
      1e190, 1e191, 1e192, 1e193, 1e194, 1e195, 1e196, 1e197, 1e198, 1e199,
      1e200, 1e201, 1e202, 1e203, 1e204, 1e205, 1e206, 1e207, 1e208, 1e209,
      1e210, 1e211, 1e212, 1e213, 1e214, 1e215, 1e216, 1e217, 1e218, 1e219,
      1e220, 1e221, 1e222, 1e223, 1e224, 1e225, 1e226, 1e227, 1e228, 1e229,
      1e230, 1e231, 1e232, 1e233, 1e234, 1e235, 1e236, 1e237, 1e238, 1e239,
      1e240, 1e241, 1e242, 1e243, 1e244, 1e245, 1e246, 1e247, 1e248, 1e249,
      1e250, 1e251, 1e252, 1e253, 1e254, 1e255, 1e256, 1e257, 1e258, 1e259,
      1e260, 1e261, 1e262, 1e263, 1e264, 1e265, 1e266, 1e267, 1e268, 1e269,
      1e270, 1e271, 1e272, 1e273, 1e274, 1e275, 1e276, 1e277, 1e278, 1e279,
      1e280, 1e281, 1e282, 1e283, 1e284, 1e285, 1e286, 1e287, 1e288, 1e289,
      1e290, 1e291, 1e292, 1e293, 1e294, 1e295, 1e296, 1e297, 1e298, 1e299,
      1e300, 1e301, 1e302, 1e303, 1e304, 1e305, 1e306, 1e307, 1e308};

  // Skip leading whitespace.
  while (isspace_ascii(*p))
    p++;

  // Handle optional sign.
  int negative = 0;
  switch (*p) {
  case '-':
    negative = 1;
    PD_FALLTHROUGH; // Fall through to increment position.
  case '+':
    p++;
    break;
  }

  long int exponent = 0;
  long int num_digits = 0;
  long int num_decimals = 0;

  // Accumulate mantissa digits as an integer to avoid per-digit FP rounding.
  // max_digits=17 decimal digits fit safely in uint64_t (max ~9.9e17 < 2^64).
  uint64_t mantissa = 0;

  // Process string of digits.
  while (isdigit_ascii(*p)) {
    if (num_digits < max_digits) {
      mantissa = mantissa * 10 + (*p - '0');
      num_digits++;
    } else {
      ++exponent;
    }

    p++;
    p += (tsep != '\0' && *p == tsep);
  }

  // Process decimal part
  if (*p == decimal) {
    if (maybe_int != NULL)
      *maybe_int = 0;
    p++;

    while (num_digits < max_digits && isdigit_ascii(*p)) {
      mantissa = mantissa * 10 + (*p - '0');
      p++;
      num_digits++;
      num_decimals++;
    }

    if (num_digits >= max_digits) // Consume extra decimal digits.
      while (isdigit_ascii(*p))
        ++p;

    exponent -= num_decimals;
  }

  if (num_digits == 0) {
    *error = ERANGE;
    return 0.0;
  }

  // Single conversion from integer mantissa to double: at most one rounding,
  // compared to up to max_digits roundings in the old FP accumulation loop.
  double number = (double)mantissa;

  // Correct for sign.
  if (negative)
    number = -number;

  // Process an exponent string.
  if (toupper_ascii(*p) == toupper_ascii(sci)) {
    if (maybe_int != NULL)
      *maybe_int = 0;

    // move past scientific notation
    p++;

    char *tmp_ptr;
    long int n = strtol(p, &tmp_ptr, 10);

    if (errno == ERANGE || checked_add(exponent, n, &exponent)) {
      errno = 0;
      exponent = n;
    }

    // If no digits after the 'e'/'E', un-consume it.
    if (tmp_ptr == p)
      p--;
    else
      p = tmp_ptr;
  }

  if (exponent > 308) {
    number = number == 0 ? 0 : number < 0 ? -HUGE_VAL : HUGE_VAL;
  } else if (exponent > 0) {
    number *= e[exponent];
  } else if (exponent < -308) { // Subnormal
    if (exponent < -616) {      // Prevent invalid array access.
      number = 0.;
    } else {
      number /= e[-308 - exponent];
      number /= e[308];
    }

  } else {
    number /= e[-exponent];
  }

  if (skip_trailing) {
    // Skip trailing whitespace.
    while (isspace_ascii(*p))
      p++;
  }

  if (endptr)
    *endptr = (char *)p;
  return number;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newNull(void *Py_UNUSED(prv)) { Py_RETURN_NONE; }

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newTrue [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newTrue(void *Py_UNUSED(prv)) { Py_RETURN_TRUE; }

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
```
