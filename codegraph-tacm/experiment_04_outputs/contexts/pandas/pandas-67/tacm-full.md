# pandas-67 :: tacm-full

query: BUG: Block.iget not wrapping timedelta64/datetime64 (#31666)

## selected nodes

- rank=1 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=2 layer=FUNCTION tokens=161 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=3 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py::_classes_and_not_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py
- rank=4 layer=FUNCTION tokens=461 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=5 layer=FUNCTION tokens=224 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py::_parse_latex_table_wrapping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py
- rank=6 layer=FUNCTION tokens=346 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py::_make_block file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py
- rank=7 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_mask_datetimelike_result file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py
- rank=8 layer=FUNCTION tokens=482 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unwrap_setitem_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=9 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py::is_ea_or_datetimelike_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py
- rank=10 layer=FUNCTION tokens=493 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py::is_valid_na_for_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py
- rank=11 layer=FUNCTION tokens=287 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Fillna.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py
- rank=12 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._unbox_scalar file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=13 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._sub_nat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=14 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_maybe_unbox_datetimelike file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py
- rank=15 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::_get_na_rep file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=16 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._formatter file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=17 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_sparse.py::dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_sparse.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def iget(self, i: int, track_ref: bool = True) -> SingleBlockManager:
        """
        Return the data as a SingleBlockManager.
        """
        block = self.blocks[self.blknos[i]]
        values = block.iget(self.blklocs[i])

        # shortcut for select a single-dim from a 2-dim BM
        bp = BlockPlacement(slice(0, len(values)))
        nb = type(block)(
            values, placement=bp, ndim=1, refs=block.refs if track_ref else None
        )
        return SingleBlockManager(nb, self.axes[1].view())

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::BlockManager.iget_values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py]
    def iget_values(self, i: int) -> ArrayLike:
        """
        Return the data for column i as the values (ndarray or ExtensionArray).

        Warning! The returned array is a view but doesn't handle Copy-on-Write,
        so this should be used with caution.
        """
        # TODO(CoW) making the arrays read-only might make this safer to use?
        block = self.blocks[self.blknos[i]]
        values = block.iget(self.blklocs[i])
        return values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py::_classes_and_not_datetimelike [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py]
def _classes_and_not_datetimelike(*klasses) -> Callable:
    """
    Evaluate if the tipo is a subclass of the klasses
    and not a datetimelike.
    """
    return lambda tipo: (
        issubclass(tipo, klasses)
        and not issubclass(tipo, (np.datetime64, np.timedelta64))
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._values [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def _values(self):
        """
        Return the internal repr of this data (defined by Block.interval_values).
        This are the values as stored in the Block (ndarray or ExtensionArray
        depending on the Block class), with datetime64[ns] and timedelta64[ns]
        wrapped in ExtensionArrays to match Index._values behavior.

        Differs from the public ``.values`` for certain data types, because of
        historical backwards compatibility of the public attribute (e.g. period
        returns object ndarray and datetimetz a datetime64[ns] ndarray for
        ``.values`` while it returns an ExtensionArray for ``._values`` in those
        cases).

        Differs from ``.array`` in that this still returns the numpy array if
        the Block is backed by a numpy array (except for datetime64 and
        timedelta64 dtypes), while ``.array`` ensures to always return an
        ExtensionArray.

        Overview:

        dtype       | values        | _values       | array                 |
        ----------- | ------------- | ------------- | --------------------- |
        Numeric     | ndarray       | ndarray       | NumpyExtensionArray   |
        Category    | Categorical   | Categorical   | Categorical           |
        dt64[ns]    | ndarray[M8ns] | DatetimeArray | DatetimeArray         |
        dt64[ns tz] | ndarray[M8ns] | DatetimeArray | DatetimeArray         |
        td64[ns]    | ndarray[m8ns] | TimedeltaArray| TimedeltaArray        |
        Period      | ndarray[obj]  | PeriodArray   | PeriodArray           |
        Nullable    | EA            | EA            | EA                    |

        """
        return self._mgr.internal_values()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py::_parse_latex_table_wrapping [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style_render.py]
def _parse_latex_table_wrapping(table_styles: CSSStyles, caption: str | None) -> bool:
    """
    Indicate whether LaTeX {tabular} should be wrapped with a {table} environment.

    Parses the `table_styles` and detects any selectors which must be included outside
    of {tabular}, i.e. indicating that wrapping must occur, and therefore return True,
    or if a caption exists and requires similar.
    """
    IGNORED_WRAPPERS = ["toprule", "midrule", "bottomrule", "column_format"]
    # ignored selectors are included with {tabular} so do not need wrapping
    return (
        table_styles is not None
        and any(d["selector"] not in IGNORED_WRAPPERS for d in table_styles)
    ) or caption is not None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py::_make_block [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/api.py]
def _make_block(values: ArrayLike, placement: np.ndarray) -> Block:
    """
    This is an analogue to blocks.new_block(_2d) that ensures:
    1) correct dimension for EAs that support 2D (`ensure_block_shape`), and
    2) correct EA class for datetime64/timedelta64 (`maybe_coerce_values`).

    The input `values` is assumed to be either numpy array or ExtensionArray:
    - In case of a numpy array, it is assumed to already be in the expected
      shape for Blocks (2D, (cols, rows)).
    - In case of an ExtensionArray the input can be 1D, also for EAs that are
      internally stored as 2D.

    For the rest no preprocessing or validation is done, except for those dtypes
    that are internally stored as EAs but have an exact numpy equivalent (and at
    the moment use that numpy dtype), i.e. datetime64/timedelta64.
    """
    dtype = values.dtype
    klass = get_block_type(dtype)
    placement_obj = BlockPlacement(placement)

    if (isinstance(dtype, ExtensionDtype) and dtype._supports_2d) or isinstance(
        values, (DatetimeArray, TimedeltaArray)
    ):
        values = ensure_block_shape(values, ndim=2)

    values = maybe_coerce_values(values)
    return klass(values, ndim=2, placement=placement_obj)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_mask_datetimelike_result [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py]
def _mask_datetimelike_result(
    result: np.ndarray | np.datetime64 | np.timedelta64,
    axis: AxisInt | None,
    mask: npt.NDArray[np.bool_],
    orig_values: np.ndarray,
) -> np.ndarray | np.datetime64 | np.timedelta64 | NaTType:
    if isinstance(result, np.ndarray):
        # we need to apply the mask
        result = result.astype("i8").view(orig_values.dtype)
        axis_mask = mask.any(axis=axis)
        result[axis_mask] = iNaT
    elif mask.any():
        return np.int64(iNaT).view(orig_values.dtype)
    return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unwrap_setitem_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py]
    def _unwrap_setitem_indexer(self, indexer):
        """
        Adapt a 2D-indexer to our 1D values.

        This is intended for 'setitem', not 'iget' or '_slice'.
        """
        # TODO: ATM this doesn't work for iget/_slice, can we change that?

        if isinstance(indexer, tuple) and len(indexer) == 2:
            # TODO(EA2D): not needed with 2D EAs
            #  Should never have length > 2.  Caller is responsible for checking.
            #  Length 1 is reached vis setitem_single_block and setitem_single_column
            #  each of which pass indexer=(pi,)
            if all(isinstance(x, np.ndarray) and x.ndim == 2 for x in indexer):
                # GH#44703 went through indexing.maybe_convert_ix
                first, second = indexer
                if not (
                    second.size == 1 and (second == 0).all() and first.shape[1] == 1
                ):
                    raise NotImplementedError(
                        "This should not be reached. Please report a bug at "
                        "github.com/pandas-dev/pandas/"
                    )
                indexer = first[:, 0]

            elif lib.is_integer(indexer[1]) and indexer[1] == 0:
                # reached via setitem_single_block passing the whole indexer
                indexer = indexer[0]

            elif com.is_null_slice(indexer[1]):
                indexer = indexer[0]

            elif is_list_like(indexer[1]) and indexer[1][0] == 0:
                indexer = indexer[0]

            else:
                raise NotImplementedError(
                    "This should not be reached. Please report a bug at "
                    "github.com/pandas-dev/pandas/"
                )
        return indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py::is_ea_or_datetimelike_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/common.py]
def is_ea_or_datetimelike_dtype(dtype: DtypeObj | None) -> bool:
    """
    Check for ExtensionDtype, datetime64 dtype, or timedelta64 dtype.

    Notes
    -----
    Checks only for dtype objects, not dtype-castable strings or types.
    """
    return isinstance(dtype, ExtensionDtype) or (lib.is_np_dtype(dtype, "mM"))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py::is_valid_na_for_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/missing.py]
def is_valid_na_for_dtype(obj, dtype: DtypeObj) -> bool:
    """
    isna check that excludes incompatible dtypes

    Parameters
    ----------
    obj : object
    dtype : np.datetime64, np.timedelta64, DatetimeTZDtype, or PeriodDtype

    Returns
    -------
    bool
    """
    if not lib.is_scalar(obj) or not isna(obj):
        return False
    elif dtype.kind == "M":
        if isinstance(dtype, np.dtype):
            # i.e. not tzaware
            return not isinstance(obj, (np.timedelta64, Decimal))
        # we have to rule out tznaive dt64("NaT")
        return not isinstance(obj, (np.timedelta64, np.datetime64, Decimal))
    elif dtype.kind == "m":
        return not isinstance(obj, (np.datetime64, Decimal))
    elif dtype.kind in "iufc":
        # Numeric
        return obj is not NaT and not isinstance(obj, (np.datetime64, np.timedelta64))
    elif dtype.kind == "b":
        # We allow pd.NA, None, np.nan in BooleanArray (same as IntervalDtype)
        return lib.is_float(obj) or obj is None or obj is libmissing.NA

    elif dtype == _dtype_str:
        # numpy string dtypes to avoid float np.nan
        return not isinstance(obj, (np.datetime64, np.timedelta64, Decimal, float))

    elif dtype == _dtype_object:
        # This is needed for Categorical, but is kind of weird
        return True

    elif isinstance(dtype, PeriodDtype):
        return not isinstance(obj, (np.datetime64, np.timedelta64, Decimal))

    elif isinstance(dtype, IntervalDtype):
        return lib.is_float(obj) or obj is None or obj is libmissing.NA

    elif isinstance(dtype, CategoricalDtype):
        return is_valid_na_for_dtype(obj, dtype.categories.dtype)

    # fallback, default to allowing NaN, None, NA, NaT
    return not isinstance(obj, (np.datetime64, np.timedelta64, Decimal))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Fillna.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def setup(self, inplace, dtype):
        N, M = 10000, 100
        if dtype in ("datetime64[ns]", "datetime64[ns, tz]", "timedelta64[ns]"):
            data = {
                "datetime64[ns]": date_range("2011-01-01", freq="h", periods=N),
                "datetime64[ns, tz]": date_range(
                    "2011-01-01", freq="h", periods=N, tz="Asia/Tokyo"
                ),
                "timedelta64[ns]": timedelta_range(start="1 day", periods=N, freq="1D"),
            }
            self.df = DataFrame({f"col_{i}": data[dtype] for i in range(M)})
            self.df[::2] = None
        else:
            values = np.random.randn(N, M)
            values[::2] = np.nan
            if dtype == "Int64":
                values = values.round()
                values = values.astype(object)
                values[::2] = NA
            self.df = DataFrame(values, dtype=dtype)
        self.fill_values = self.df.iloc[self.df.first_valid_index()].to_dict()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._unbox_scalar [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _unbox_scalar(
        self, value: DTScalarOrNaT
    ) -> np.int64 | np.datetime64 | np.timedelta64:
        """
        Unbox the integer value of a scalar `value`.

        Parameters
        ----------
        value : Period, Timestamp, Timedelta, or NaT
            Depending on subclass.

        Returns
        -------
        int

        Examples
        --------
        >>> arr = pd.array(np.array(["1970-01-01"], "datetime64[ns]"))
        >>> arr._unbox_scalar(arr[0])
        np.datetime64('1970-01-01T00:00:00.000000000')
        """
        raise AbstractMethodError(self)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::DatetimeLikeArrayMixin._sub_nat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _sub_nat(self) -> np.ndarray:
        """
        Subtract pd.NaT from self
        """
        # GH#19124 Timedelta - datetime is not in general well-defined.
        # We make an exception for pd.NaT, which in this case quacks
        # like a timedelta.
        # For datetime64 dtypes by convention we treat NaT as a datetime, so
        # this subtraction returns a timedelta64 dtype.
        # For period dtype, timedelta64 is a close-enough return dtype.
        result = np.empty(self.shape, dtype=np.int64)
        result.fill(iNaT)
        if self.dtype.kind in "mM":
            # We can retain unit in dtype
            self = cast("DatetimeArray| TimedeltaArray", self)
            return result.view(f"timedelta64[{self.unit}]")
        else:
            return result.view("timedelta64[ns]")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py::_maybe_unbox_datetimelike [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/cast.py]
def _maybe_unbox_datetimelike(value: Scalar, dtype: DtypeObj) -> Scalar:
    """
    Convert a Timedelta or Timestamp to timedelta64 or datetime64 for setting
    into a numpy array.  Failing to unbox would risk dropping nanoseconds.

    Notes
    -----
    Caller is responsible for checking dtype.kind in "mM"
    """
    if is_valid_na_for_dtype(value, dtype):
        # GH#36541: can't fill array directly with pd.NaT
        # > np.empty(10, dtype="datetime64[ns]").fill(pd.NaT)
        # ValueError: cannot convert float NaN to integer
        value = dtype.type("NaT", "ns")
    elif isinstance(value, Timestamp):
        if value.tz is None:
            value = value.to_datetime64()
        elif not isinstance(dtype, DatetimeTZDtype):
            raise TypeError("Cannot unbox tzaware Timestamp to tznaive dtype")
    elif isinstance(value, Timedelta):
        value = value.to_timedelta64()

    _disallow_mismatched_datetimelike(value, dtype)
    return value

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::_get_na_rep [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
def _get_na_rep(dtype: DtypeObj) -> str:
    if isinstance(dtype, ExtensionDtype):
        return f"{dtype.na_value}"
    else:
        dtype_type = dtype.type

    return {np.datetime64: "NaT", np.timedelta64: "NaT"}.get(dtype_type, "NaN")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._formatter [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def _formatter(self, boxed: bool = False) -> Callable:
        # Use str to avoid np.int64(...) wrapping in repr output.
        return str

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_sparse.py::dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_sparse.py]
def dtype():
    return SparseDtype()
```
