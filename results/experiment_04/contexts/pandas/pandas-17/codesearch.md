# pandas-17 :: codesearch

query: BUG: DTI/TDI.insert doing invalid casting (#33703)

## selected nodes

- rank=1 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=2 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newTrue file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=3 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newFalse file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=4 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNegInf file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=5 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newInteger file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=6 layer=FUNCTION tokens=1709 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c::precise_xstrtod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/tokenizer.c
- rank=7 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=8 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::node_decref file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h
- rank=9 layer=FUNCTION tokens=137 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyTimeDeltaToIsoCallback file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=10 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newPosInf file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=11 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dict_iterBegin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=12 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::node_incref file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h
- rank=13 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_getLongValue file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=14 layer=FUNCTION tokens=376 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::skiplist_insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h
- rank=15 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=16 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newDouble file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=17 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newLong file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=18 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newObject file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=19 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/fast_float_strtod.cpp::fast_float_strtod file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/fast_float_strtod.cpp
- rank=20 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendIndentUnchecked file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c
- rank=21 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newString file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=22 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_iterGetValue file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=23 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endObject file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c
- rank=24 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endArray file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNull [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newNull(void *Py_UNUSED(prv)) { Py_RETURN_NONE; }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newTrue [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newTrue(void *Py_UNUSED(prv)) { Py_RETURN_TRUE; }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newFalse [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newFalse(void *Py_UNUSED(prv)) { Py_RETURN_FALSE; }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newNegInf [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newNegInf(void *Py_UNUSED(prv)) {
  return PyFloat_FromDouble(-Py_HUGE_VAL);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newInteger [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newInteger(void *Py_UNUSED(prv), JSINT32 value) {
  return PyLong_FromLong(value);
}

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Set_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Set_iterGetName(JSOBJ Py_UNUSED(obj),
                                   JSONTypeContext *Py_UNUSED(tc),
                                   size_t *Py_UNUSED(outLen)) {
  return NULL;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::node_decref [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h]
static inline void node_decref(node_t *node) { --(node->ref_count); }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::NpyTimeDeltaToIsoCallback [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *NpyTimeDeltaToIsoCallback(JSOBJ Py_UNUSED(unused),
                                             JSONTypeContext *tc, size_t *len) {
  NPY_DATETIMEUNIT valueUnit = ((PyObjectEncoder *)tc->encoder)->valueUnit;
  GET_TC(tc)->cStr = int64ToIsoDuration(GET_TC(tc)->longValue, valueUnit, len);
  return GET_TC(tc)->cStr;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newPosInf [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newPosInf(void *Py_UNUSED(prv)) {
  return PyFloat_FromDouble(Py_HUGE_VAL);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Dict_iterBegin [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static void Dict_iterBegin(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  GET_TC(tc)->index = 0;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::node_incref [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h]
static inline void node_incref(node_t *node) { ++(node->ref_count); }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_getLongValue [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static JSINT64 Object_getLongValue(JSOBJ Py_UNUSED(obj), JSONTypeContext *tc) {
  return GET_TC(tc)->longValue;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::skiplist_insert [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h]
static inline int skiplist_insert(skiplist_t *skp, double value) {
  node_t *node, *prevnode, *newnode, *next_at_level;
  int *steps_at_level;
  int size, steps, level, rank = 0;
  node_t **chain;

  chain = skp->tmp_chain;

  steps_at_level = skp->tmp_steps;
  memset(steps_at_level, 0, skp->maxlevels * sizeof(int));

  node = skp->head;

  for (level = skp->maxlevels - 1; level >= 0; --level) {
    next_at_level = node->next[level];
    while (_node_cmp(next_at_level, value) >= 0) {
      steps_at_level[level] += node->width[level];
      rank += node->width[level];
      node = next_at_level;
      next_at_level = node->next[level];
    }
    chain[level] = node;
  }

  size = int_min(skp->maxlevels, 1 - ((int)log2(urand())));

  newnode = node_init(value, size);
  if (!newnode) {
    return -1;
  }
  steps = 0;

  for (level = 0; level < size; ++level) {
    prevnode = chain[level];
    newnode->next[level] = prevnode->next[level];

    prevnode->next[level] = newnode;
    node_incref(newnode); // increment the reference count

    newnode->width[level] = prevnode->width[level] - steps;
    prevnode->width[level] = steps + 1;

    steps += steps_at_level[level];
  }

  for (level = size; level < skp->maxlevels; ++level) {
    chain[level]->width[level] += 1;
  }

  ++(skp->size);

  return rank + 1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Tuple_iterGetName(JSOBJ Py_UNUSED(obj),
                                     JSONTypeContext *Py_UNUSED(tc),
                                     size_t *Py_UNUSED(outLen)) {
  return NULL;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newDouble [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newDouble(void *Py_UNUSED(prv), double value) {
  return PyFloat_FromDouble(value);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newLong [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newLong(void *Py_UNUSED(prv), JSINT64 value) {
  return PyLong_FromLongLong(value);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newObject [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newObject(void *Py_UNUSED(prv), void *Py_UNUSED(decoder)) {
  return PyDict_New();
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/fast_float_strtod.cpp::fast_float_strtod [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/parser/fast_float_strtod.cpp]
int fast_float_strtod(const char *start, const char *end, double *value,
                      const char **endptr, char decimal) {
  fast_float::parse_options options{fast_float::chars_format::general, decimal};
  auto result = fast_float::from_chars_advanced(start, end, *value, options);
  // No error or overflow/underflow are valid
  if (result.ec == std::errc() || result.ec == std::errc::result_out_of_range) {
    *endptr = result.ptr;
    return 0;
  }
  return -1;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c::Buffer_AppendIndentUnchecked [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/lib/ultrajsonenc.c]
void Buffer_AppendIndentUnchecked(JSONObjectEncoder *enc, JSINT32 value) {
  int i;
  if (enc->indent > 0) {
    while (value-- > 0)
      for (i = 0; i < enc->indent; i++)
        Buffer_AppendCharUnchecked(enc, ' ');
  }
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_newString [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_newString(void *Py_UNUSED(prv), wchar_t *start,
                              wchar_t *end) {
  return PyUnicode_FromWideChar(start, (end - start));
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Object_iterGetValue [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static JSOBJ Object_iterGetValue(JSOBJ obj, JSONTypeContext *tc) {
  return GET_TC(tc)->iterGetValue(obj, tc);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endObject [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_endObject(void *Py_UNUSED(prv), JSOBJ obj) { return obj; }

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c::Object_endArray [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/JSONtoObj.c]
static JSOBJ Object_endArray(void *Py_UNUSED(prv), JSOBJ obj) { return obj; }
```
