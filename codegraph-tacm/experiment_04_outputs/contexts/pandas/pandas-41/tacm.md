# pandas-41 :: tacm

query: BUG: ExtensionBlock.set not setting values inplace (#32831)

## selected nodes

- rank=1 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=2 layer=FILE tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/putmask.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/putmask.py
- rank=3 layer=FILE tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/localization.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/localization.py
- rank=4 layer=FILE tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py
- rank=5 layer=CLASS tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=6 layer=CLASS tokens=566 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=7 layer=CLASS tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_partial.py::TestPartialSetting file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexing/test_partial.py
- rank=8 layer=CLASS tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_set_index.py::TestSetIndexCustomLabelType.Thing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/methods/test_set_index.py
- rank=9 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=10 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=11 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock._unwrap_setitem_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=12 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.fillna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=13 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_with_engine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=14 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.is_numeric file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=15 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.shape file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=16 layer=FUNCTION tokens=149 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents._check_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=17 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.sort_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=18 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=19 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py::SetitemCastingEquivalents.is_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/series/indexing/test_setitem.py
- rank=20 layer=FUNCTION tokens=300 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/localization.py::set_locale file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_config/localization.py
- rank=21 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_labels file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=22 layer=FUNCTION tokens=202 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=23 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.slice_block_rows file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=24 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=25 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/putmask.py::setitem_datetimelike_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/putmask.py
- rank=26 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::ExtensionBlock.is_view file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=27 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/putmask.py::putmask_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/array_algos/putmask.py
- rank=28 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py::TestCanHoldElement.check_series_setitem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/internals/test_internals.py
- rank=29 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=30 layer=FUNCTION tokens=153 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py::Block.set_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/blocks.py
- rank=31 layer=FUNCTION tokens=167 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame._iset_not_inplace file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=32 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.set_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=33 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py::SingleBlockManager.set_values file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/managers.py
- rank=34 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.reset_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=35 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.dropna file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=36 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.drop_duplicates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=37 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py::_TextAdjustment.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/printing.py

## context

```text
file core/internals/blocks.py
imports: __future__, inspect, re, typing, warnings, numpy, pandas
defines: Block, EABackedBlock, ExtensionBlock, NumpyBlock, NDArrayBackedExtensionBlock, DatetimeLikeBlock, maybe_coerce_values, get_block_type, new_block_2d, new_block, check_ndim, extract_pandas_array, extend_blocks, ensure_block_shape, external_values

file core/array_algos/putmask.py
imports: __future__, typing, numpy, pandas
defines: putmask_inplace, putmask_without_repeat, validate_putmask, extract_bool_array, setitem_datetimelike_compat

file pandas/_config/localization.py
imports: __future__, contextlib, locale, platform, re, subprocess, typing, pandas
defines: set_locale, can_set_locale, _valid_locales, get_locales

file io/sas/sas_constants.py
imports: __future__, typing
defines: SASIndex

class ExtensionBlock(EABackedBlock):  [core/internals/blocks.py:1905]
methods: _maybe_squeeze_arg, _slice, _unstack
         _unwrap_setitem_indexer, fillna, iget, is_numeric
         is_view, set_inplace, shape, slice_block_rows

class Series(base.IndexOpsMixin, NDFrame):  # type: ignore[misc]  [pandas/core/series.py:211]
methods: _align_for_op, _append_internal, _arith_method, _binop
         _can_hold_na, _cmp_method, _construct_result
         _construct_result, _construct_result
         _constructor, _constructor_expanddim
         _constructor_expanddim_from_mgr
         _constructor_from_mgr, _flex_method
         _get_rows_with_mask, _get_value
         _get_values_tuple, _get_with, _gotitem
         _init_dict, _ixs, _logical_method
         _needs_reindex_multi, _reduce, _references
         _reindex_indexer, _set_labels, _set_name
         _set_value, _set_values, _set_with
         _set_with_engine, _slice, _values, add, aggregate
         all, any, apply, argsort, array, autocorr, axes
         between, case_when, combine, combine_first
         compare, corr, count, cov, cummax, cummin
         cumprod, cumsum, diff, divmod, dot, drop, drop
         drop, drop, drop_duplicates, drop_duplicates
         drop_duplicates, drop_duplicates, dropna, dropna
         dropna, dtype, dtypes, duplicated, eq, explode
         floordiv, from_arrow, ge, groupby, gt, idxmax
         idxmin, info, isin, isna, isnull, items, keys
         kurt, le, lt, map, max, mean, median
         memory_usage, min, mod, mode, mul, name, name, ne
         nlargest, notna, notnull, nsmallest, pop, pow
         prod, quantile, quantile, quantile, quantile
         radd, rdivmod, reindex, rename, rename, rename
         rename_axis, rename_axis, rename_axis
         rename_axis, reorder_levels, repeat, reset_index
         reset_index, reset_index, reset_index, rfloordiv
         rmod, rmul, round, rpow, rsub, rtruediv
         searchsorted, sem, set_axis, skew, sort_index
         sort_index, sort_index, sort_index, sort_values
         sort_values, sort_values, sort_values, std, sub
         sum, swaplevel, to_dict, to_dict, to_dict
         to_frame, to_markdown, to_markdown, to_markdown
         to_markdown, to_period, to_string, to_string
         to_string, to_timestamp, transform, truediv
         unique, unstack, update, values, var, __array__
         __arrow_c_stream__, __getitem__, __init__
         __len__, __matmul__, __repr__, __rmatmul__
         __setitem__

class TestPartialSetting:  [tests/indexing/test_partial.py:239]
methods: test_cannot_expand_with_iloc_iat
         test_loc_with_list_of_strings_representing_datetimes
         test_loc_with_list_of_strings_representing_datetimes_missing_value
         test_loc_with_list_of_strings_representing_datetimes_not_matched_type
         test_partial_set_invalid, test_partial_setting
         test_partial_setting2, test_partial_setting_frame
         test_partial_setting_mixed_dtype
         test_series_partial_set
         test_series_partial_set_with_name
         test_setitem_with_expansion_numeric_into_datetimeindex

class Thing(set):  [frame/methods/test_set_index.py:709]
methods: —

    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None:
        # When an ndarray, we should have locs.tolist() == [0]
        # When a BlockPlacement we should have list(locs) == [0]
        if copy:
            self.values = self.values.copy()
        self.values[:] = values

    def _set_name(self, name, inplace: bool = False) -> Series:
        """
        Set the Series name.

        Parameters
        ----------
        name : str
        inplace : bool
            Whether to modify `self` directly or return a copy.
        """
        inplace = validate_bool_kwarg(inplace, "inplace")
        ser = self if inplace else self.copy(deep=False)
        ser.name = name
        return ser

    def _unwrap_setitem_indexer(self, indexer):
        """
        Adapt a 2D-indexer to our 1D values.

        This is intended for 'setitem', not 'iget' or '_slice'.
        """
    # ... truncated

    def fillna(
        self,
        value,
        limit: int | None = None,
        inplace: bool = False,
    ) -> list[Block]:
        if isinstance(self.dtype, (IntervalDtype, StringDtype)):
            # Block.fillna handles coercion (test_fillna_interval)
            if isinstance(self.dtype, IntervalDtype) and limit is not None:
                raise ValueError("limit must be None")
            return super().fillna(
                value=value,
    # ... truncated

    def _set_with_engine(self, key, value) -> None:
        loc = self.index.get_loc(key)

        # this is equivalent to self._values[key] = value
        self._mgr.setitem_inplace(loc, value)

    def is_numeric(self) -> bool:  # type: ignore[override]
        return self.values.dtype._is_numeric

    def shape(self) -> Shape:
        # TODO(EA2D): override unnecessary with 2D EAs
        if self.ndim == 1:
            return (len(self.values),)
        return len(self._mgr_locs), len(self.values)

    def _check_inplace(self, is_inplace, orig, arr, obj):
        if is_inplace is None:
            # We are not (yet) checking whether setting is inplace or not
            pass
        elif is_inplace:
            if arr.dtype.kind in ["m", "M"]:
                # We may not have the same DTA/TDA, but will have the same
                #  underlying data
                assert arr._ndarray is obj._values._ndarray
            else:
                assert obj._values is arr
        else:
            # otherwise original array should be unchanged
            tm.assert_equal(arr, orig._values)

    def sort_values(
        self,
        *,
        axis: Axis = 0,
        ascending: bool | Sequence[bool] = True,
        inplace: bool = False,
        kind: SortKind = "quicksort",
        na_position: NaPosition = "last",
        ignore_index: bool = False,
        key: ValueKeyFunc | None = None,
    ) -> Series | None:
        """
    # ... truncated

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
    # ... truncated

    def is_inplace(self, obj, expected):
        """
        Whether we expect the setting to be in-place or not.
        """
        return expected.dtype == obj.dtype

def set_locale(
    new_locale: str | tuple[str, str], lc_var: int = locale.LC_ALL
) -> Generator[str | tuple[str, str]]:
    """
    Context manager for temporarily setting a locale.

    Parameters
    ----------
    new_locale : str or tuple
        A string of the form <language_country>.<encoding>. For example to set
        the current locale to US English with a UTF8 encoding, you would pass
        "en_US.UTF-8".
    lc_var : int, default `locale.LC_ALL`
        The category of the locale being set.

    Notes
    -----
    This is useful when you want to run a particular block of code under a
    particular locale, without globally setting the locale. This probably isn't
    thread-safe.
    """
    # getlocale is not always compliant with setlocale, use setlocale. GH#46595
    current_locale = locale.setlocale(lc_var)

    try:
        locale.setlocale(lc_var, new_locale)
        normalized_code, normalized_encoding = locale.getlocale()
        if normalized_code is not None and normalized_encoding is not None:
            yield f"{normalized_code}.{normalized_encoding}"
        else:
            yield new_locale
    finally:
        locale.setlocale(lc_var, current_locale)

    def _set_labels(self, key, value) -> None:
        key = com.asarray_tuplesafe(key)
        indexer: np.ndarray = self.index.get_indexer(key)
        mask = indexer == -1
        if mask.any():
            raise KeyError(f"{key[mask]} not in index")
        self._set_values(indexer, value)

    def _set_value(self, label, value, takeable: bool = False) -> None:
        """
        Quickly set single value at passed label.

        If label is not contained, a new object is created with the label
        placed at the end of the result index.

        Parameters
        ----------
        label : object
            Partial indexing with MultiIndex not allowed.
        value : object
            Scalar value.
        takeable : interpret the index as indexers, default False
        """
        if not takeable:
            try:
                loc = self.index.get_loc(label)
            except KeyError:
                # set using a non-recursive method
                self.loc[label] = value
                return
        else:
            loc = label

        self._set_values(loc, value)

    def slice_block_rows(self, slicer: slice) -> Self:
        """
        Perform __getitem__-like specialized to slicing along index.
        """
        # GH#42787 in principle this is equivalent to values[..., slicer], but we don't
        # require subclasses of ExtensionArray to support that form (for now).
        new_values = self.values[slicer]
        return type(self)(new_values, self._mgr_locs, ndim=self.ndim, refs=self.refs)

    def _set_values(self, key, value) -> None:
        if isinstance(key, (Index, Series)):
            key = key._values

        self._mgr = self._mgr.setitem(indexer=key, value=value)

def setitem_datetimelike_compat(values: np.ndarray, num_set: int, other: Any) -> Any:
    """
    Parameters
    ----------
    values : np.ndarray
    num_set : int
        For putmask, this is mask.sum()
    other : Any
    """
    if values.dtype == object:
        dtype, _ = infer_dtype_from(other)

        if lib.is_np_dtype(dtype, "mM"):
            # https://github.com/numpy/numpy/issues/12550
            #  timedelta64 will incorrectly cast to int
            if not is_list_like(other):
                other = [other] * num_set
            else:
                other = list(other)

    return other

    def is_view(self) -> bool:
        """Extension arrays are never treated as views."""
        return False

def putmask_inplace(values: ArrayLike, mask: npt.NDArray[np.bool_], value: Any) -> None:
    """
    ExtensionArray-compatible implementation of np.putmask.  The main
    difference is we do not handle repeating or truncating like numpy.

    Parameters
    ----------
    values: np.ndarray or ExtensionArray
    mask : np.ndarray[bool]
        We assume extract_bool_array has already been called.
    value : Any
    """

    if (
        not isinstance(values, np.ndarray)
        or (values.dtype == object and not lib.is_scalar(value))
        # GH#43424: np.putmask raises TypeError if we cannot cast between types with
        # rule = "safe", a stricter guarantee we may not have here
        or (
            isinstance(value, np.ndarray) and not np.can_cast(value.dtype, values.dtype)
        )
    ):
        # GH#19266 using np.putmask gives unexpected results with listlike value
        #  along with object dtype
        if is_list_like(value) and len(value) == len(values):
            values[mask] = value[mask]
        else:
            values[mask] = value
    else:
        # GH#37833 np.putmask is more performant than __setitem__
        np.putmask(values, mask, value)

    def check_series_setitem(self, elem, index: Index, inplace: bool):
        arr = index._data.copy()
        ser = Series(arr, copy=False)

        self.check_can_hold_element(ser, elem, inplace)

        if is_scalar(elem):
            ser[0] = elem
        else:
            ser[: len(elem)] = elem

        if inplace:
            assert ser._values is arr  # i.e. setting was done inplace
        else:
            assert ser.dtype == object

    def len(self) -> Series:
        """
        Return the length of each list in the Series.

        Computes the number of elements in each list entry. The result is a
        Series of integers with the same index as the original Series.

        Returns
        -------
        pandas.Series
            The length of each list.

    # ... truncated

    def set_inplace(self, locs, values: ArrayLike, copy: bool = False) -> None:
        """
        Modify block values in-place with new item value.

        If copy=True, first copy the underlying values in place before modifying
        (for Copy-on-Write).

        Notes
        -----
        `set_inplace` never creates a new array or new Block, whereas `setitem`
        _may_ create a new array and always creates a new Block.

        Caller is responsible for checking values.dtype == self.dtype.
        """
        if copy:
            self.values = self.values.copy()
        self.values[locs] = values

    def _iset_not_inplace(self, key, value) -> None:
        # GH#39510 when setting with df[key] = obj with a list-like key and
        #  list-like value, we iterate over those listlikes and set columns
        #  one at a time.  This is different from dispatching to
        #  `self.loc[:, key]= value`  because loc.__setitem__ may overwrite
        #  data inplace, whereas this will insert new arrays.

        def igetitem(obj, i: int):
            # Note: we catch DataFrame obj before getting here, but
            #  hypothetically would return obj.iloc[:, i]
            if isinstance(obj, np.ndarray):
                return obj[..., i]
    # ... truncated

    def set_index(
        self,
        keys,
        *,
        drop: bool = True,
        append: bool = False,
        inplace: bool = False,
        verify_integrity: bool | lib.NoDefault = lib.no_default,
    ) -> DataFrame | None:
        """
    # ... truncated

    def set_values(self, values: ArrayLike) -> None:
        """
        Set the values of the single block in place.

        Use at your own risk! This does not check if the passed values are
        valid for the current Block/SingleBlockManager (length, dtype, etc),
        and this does not properly keep track of references.
        """
        # NOTE(CoW) Currently this is only used for FrameColumnApply.series_generator
        # which handles CoW by setting the refs manually if necessary
        self.blocks[0].values = values
        self.blocks[0]._mgr_locs = BlockPlacement(slice(len(values)))

    def reset_index(
        self,
        level: IndexLabel | None = None,
        *,
        drop: bool = False,
        name: Level = lib.no_default,
        inplace: bool = False,
        allow_duplicates: bool = False,
    ) -> DataFrame | Series | None:
        """
    # ... truncated

    def dropna(
        self,
        *,
        axis: Axis = 0,
        inplace: bool = False,
        how: AnyAll | None = None,
        ignore_index: bool = False,
    ) -> Series | None:
        """
    # ... truncated

    def drop_duplicates(
        self,
        *,
        keep: DropKeep = "first",
        inplace: bool = False,
        ignore_index: bool = False,
    ) -> Series | None:
        """
    # ... truncated

    def len(self, text: str) -> int:
        return len(text)
```
