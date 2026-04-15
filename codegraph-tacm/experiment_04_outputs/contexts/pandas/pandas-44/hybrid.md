# pandas-44 :: hybrid

query: BUG: DTI/TDI/PI get_indexer_non_unique with incompatible dtype (#32650)

## selected nodes

- rank=1 layer=FUNCTION tokens=412 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=2 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=3 layer=FUNCTION tokens=354 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._intersection file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=4 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=5 layer=FUNCTION tokens=419 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_strict file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=6 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique_sorted file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py
- rank=7 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._index_as_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=8 layer=FUNCTION tokens=696 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._reindex_non_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=9 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py::TestNonNano.dta file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/test_datetimes.py
- rank=10 layer=FUNCTION tokens=316 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._maybe_cast_slice_bound file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=11 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._left_indexer_unique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=12 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer_dups file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=13 layer=FUNCTION tokens=299 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_for file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=14 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=15 layer=FUNCTION tokens=348 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_FrequencyInferer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py
- rank=16 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py
- rank=17 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py::any_dtype_for_small_pos_integer_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py
- rank=18 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._disallow_mismatched_indexing file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py
- rank=19 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py
- rank=20 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py::numeric_indexing_engine_type_and_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_non_comparable [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _get_indexer_non_comparable(
        self, target: Index, method: str_t | None, unique: bool = True
    ) -> npt.NDArray[np.intp] | tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
        """
        Called from get_indexer or get_indexer_non_unique when the target
        is of a non-comparable dtype.

        For get_indexer lookups with method=None, get_indexer is an _equality_
        check, so non-comparable dtypes mean we will always have no matches.

        For get_indexer lookups with a method, get_indexer is an _inequality_
        check, so non-comparable dtypes mean we will always raise TypeError.

        Parameters
        ----------
        target : Index
        method : str or None
        unique : bool, default True
            * True if called from get_indexer.
            * False if called from get_indexer_non_unique.

        Raises
        ------
        TypeError
            If doing an inequality check, i.e. method is not None.
        """
        if method is not None:
            other_dtype = _unpack_nested_dtype(target)
            raise TypeError(f"Cannot compare dtypes {self.dtype} and {other_dtype}")

        no_matches = -1 * np.ones(target.shape, dtype=np.intp)
        if unique:
            # This is for get_indexer
            return no_matches
        else:
            # This is for get_indexer_non_unique
            missing = np.arange(len(target), dtype=np.intp)
            return no_matches, missing

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::DatetimeIndexIndexing.time_get_indexer_mismatched_tz [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_mismatched_tz(self):
        # reached via e.g.
        #  ser = Series(range(len(dti)), index=dti)
        #  ser[dti2]
        self.dti.get_indexer(self.dti2)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._intersection [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _intersection(
        self, other: Index, sort: bool = False
    ) -> Index | ArrayLike | MultiIndex:
        """
        intersection specialized to the case with matching dtypes.
        """
        if self._can_use_libjoin and other._can_use_libjoin:
            try:
                res_indexer, indexer, _ = self._inner_indexer(other)  # pyright: ignore[reportArgumentType]
            except TypeError:
                # non-comparable; should only be for object dtype
                pass
            else:
                # TODO: algos.unique1d should preserve DTA/TDA
                if is_numeric_dtype(self.dtype):
                    # This is faster, because Index.unique() checks for uniqueness
                    # before calculating the unique values.
                    res = algos.unique1d(res_indexer)
                else:
                    result = self.take(indexer)
                    res = result.drop_duplicates()  # type: ignore[assignment]
                return ensure_wrapped_if_datetimelike(res)  # type: ignore[no-untyped-call]

        res_values = self._intersection_via_get_indexer(other, sort=sort)
        res_values = _maybe_try_sort(res_values, sort)  # type: ignore[assignment]
        return res_values

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def time_get_loc_non_unique(self, dtype):
        self.non_unique.get_loc(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._get_indexer_strict [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _get_indexer_strict(
        self, key: Axes, axis_name: str_t
    ) -> tuple[Index, np.ndarray]:
        """
        Analogue to get_indexer that raises if any elements are missing.
        """
        keyarr = key
        if not isinstance(keyarr, Index):
            keyarr = com.asarray_tuplesafe(keyarr)

        if self._index_as_unique:
            indexer = self.get_indexer_for(keyarr)  # pyright: ignore[reportArgumentType]
            keyarr = self.reindex(keyarr)[0]  # pyright: ignore[reportArgumentType]
        else:
            keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

        self._raise_if_missing(keyarr, indexer, axis_name)

        keyarr = self.take(indexer)
        if isinstance(key, Index):
            # GH 42790 - Preserve name from an Index
            keyarr.name = key.name
        if lib.is_np_dtype(keyarr.dtype, "mM") or isinstance(
            keyarr.dtype, DatetimeTZDtype
        ):
            # DTI/TDI.take can infer a freq in some cases when we dont want one
            if isinstance(key, list) or (
                isinstance(key, type(self))
                # "Index" has no attribute "freq"
                and key.freq is None  # type: ignore[attr-defined]
            ):
                # error: "Index" has no attribute "_with_freq"; maybe "_with_infer"?
                keyarr = keyarr._with_freq(None)  # type: ignore[attr-defined]

        return keyarr, indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py::Indexing.time_get_loc_non_unique_sorted [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/index_object.py]
    def time_get_loc_non_unique_sorted(self, dtype):
        self.non_unique_sorted.get_loc(self.key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._index_as_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _index_as_unique(self) -> bool:
        """
        Whether we should treat this as unique for the sake of
        get_indexer vs get_indexer_non_unique.

        For IntervalIndex compat.
        """
        return self.is_unique

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._reindex_non_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _reindex_non_unique(
        self, target: Index
    ) -> tuple[Index, npt.NDArray[np.intp], npt.NDArray[np.intp] | None]:
        """
        Create a new index with target's values (move/add/delete values as
        necessary) use with non-unique Index and a possibly non-unique target.

        Parameters
        ----------
        target : an iterable

        Returns
        -------
        new_index : pd.Index
            Resulting index.
        indexer : np.ndarray[np.intp]
            Indices of output values in original index.
        new_indexer : np.ndarray[np.intp] or None

        """
        target = ensure_index(target)
        if len(target) == 0:
            # GH#13691
            return self[:0], np.array([], dtype=np.intp), None

        indexer, missing = self.get_indexer_non_unique(target)
        check = indexer != -1
        new_labels: Index | np.ndarray = self.take(indexer[check])
        new_indexer = None

        if len(missing):
            length = np.arange(len(indexer), dtype=np.intp)

            missing = ensure_platform_int(missing)
            missing_labels = target.take(missing)
            missing_indexer = length[~check]
            cur_labels = self.take(indexer[check]).values
            cur_indexer = length[check]

            # Index constructor below will do inference
            new_labels = np.empty((len(indexer),), dtype=object)
            new_labels[cur_indexer] = cur_labels
            new_labels[missing_indexer] = missing_labels

            # GH#38906
            if not len(self):
                new_indexer = np.arange(0, dtype=np.intp)

            # a unique indexer
            elif target.is_unique:
                # see GH5553, make sure we use the right indexer
                new_indexer = np.arange(len(indexer), dtype=np.intp)
                new_indexer[cur_indexer] = np.arange(len(cur_labels))
                new_indexer[missing_indexer] = -1

            # we have a non_unique selector, need to use the original
            # indexer here
            else:
                # need to retake to have the same size as the indexer
                indexer[~check] = -1

                # reset the new indexer to account for the new size
                new_indexer = np.arange(len(self.take(indexer)), dtype=np.intp)
                new_indexer[~check] = -1

        if not isinstance(self, ABCMultiIndex):
            new_index = Index(new_labels, name=self.name, copy=False)
        else:
            new_index = type(self).from_tuples(new_labels, names=self.names)
        return new_index, indexer, new_indexer

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._left_indexer_unique [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _left_indexer_unique(self, other: Self) -> npt.NDArray[np.intp]:
        # Caller is responsible for ensuring other.dtype == self.dtype
        sv = self._get_join_target()
        ov = other._get_join_target()
        # similar but not identical to ov.searchsorted(sv)
        return libjoin.left_join_indexer_unique(sv, ov)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer_dups [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer_dups(self, dtype, monotonic):
        self.data.get_indexer_for(self.indexer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.get_indexer_for [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def get_indexer_for(self, target: Axes) -> npt.NDArray[np.intp]:
        """
        Guaranteed return of an indexer even when non-unique.

        This dispatches to get_indexer or get_indexer_non_unique
        as appropriate.

        Parameters
        ----------
        target : Index
            An iterable containing the values to be used for computing indexer.

        Returns
        -------
        np.ndarray[np.intp]
            List of indices.

        See Also
        --------
        Index.get_indexer : Computes indexer and mask for new index given
            the current index.
        Index.get_non_unique : Returns indexer and masks for new index given
            the current index.

        Examples
        --------
        >>> idx = pd.Index([np.nan, "var1", np.nan])
        >>> idx.get_indexer_for([np.nan])
        array([0, 2])
        """
        if self._index_as_unique:
            return self.get_indexer(target)
        indexer, _ = self.get_indexer_non_unique(target)
        return indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin._can_partial_date_slice [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _can_partial_date_slice(self, reso: Resolution) -> bool:
        # e.g. test_getitem_setitem_periodindex
        # History of conversation GH#3452, GH#3931, GH#2369, GH#14826
        return reso > self._resolution_obj
        # NB: for DTI/PI, not TDI

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_FrequencyInferer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py]
    def __init__(self, index) -> None:
        self.index = index
        self.i8values = index.asi8

        # For get_unit_from_dtype we need the dtype to the underlying ndarray,
        #  which for tz-aware is not the same as index.dtype
        if isinstance(index, ABCIndex):
            # error: Item "ndarray[Any, Any]" of "Union[ExtensionArray,
            # ndarray[Any, Any]]" has no attribute "_ndarray"
            self._creso = get_unit_from_dtype(
                index._data._ndarray.dtype  # type: ignore[union-attr]
            )
        else:
            # otherwise we have DTA/TDA
            self._creso = get_unit_from_dtype(index._ndarray.dtype)

        # This moves the values, which are implicitly in UTC, to the
        # the timezone so they are in local time
        if hasattr(index, "tz"):
            if index.tz is not None:
                self.i8values = tz_convert_from_utc(
                    self.i8values, index.tz, reso=self._creso
                )

        if len(index) < 3:
            raise ValueError("Need at least 3 dates to infer frequency")

        self.is_monotonic = (
            self.index._is_monotonic_increasing or self.index._is_monotonic_decreasing
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py::NumericMaskedIndexing.time_get_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/indexing.py]
    def time_get_indexer(self, dtype, monotonic):
        self.data.get_indexer(self.indexer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py::any_dtype_for_small_pos_integer_indexes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_setops.py]
def any_dtype_for_small_pos_integer_indexes(request):
    """
    Dtypes that can be given to an Index with small positive integers.

    This means that for any dtype `x` in the params list, `Index([1, 2, 3], dtype=x)` is
    valid and gives the correct Index (sub-)class.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py::PeriodIndex._disallow_mismatched_indexing [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/period.py]
    def _disallow_mismatched_indexing(self, key: Period) -> None:
        if key._dtype != self.dtype:
            raise KeyError(key)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py::OffsetArrayArithmetic.time_add_dti_offset [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/arithmetic.py]
    def time_add_dti_offset(self, offset):
        with warnings.catch_warnings(record=True):
            self.rng + offset

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py::numeric_indexing_engine_type_and_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_engines.py]
def numeric_indexing_engine_type_and_dtype(request):
    return request.param
```
