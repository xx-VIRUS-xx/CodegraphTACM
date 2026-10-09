# pandas-53 :: tacm-full

query: BUG: using loc[int] with object index (#31905)

## selected nodes

- rank=1 layer=FUNCTION tokens=240 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_value file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=2 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=3 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=4 layer=FUNCTION tokens=831 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=5 layer=FUNCTION tokens=1585 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_level file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py
- rank=6 layer=FUNCTION tokens=374 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py::ExtensionArray.insert file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/base.py
- rank=7 layer=FUNCTION tokens=225 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_single_level_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series._set_value [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_level [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def _get_loc_level(self, key, level: int | list[int] = 0):
        """
        get_loc_level but with `level` known to be positional, not name-based.
        """

        # different name to distinguish from maybe_droplevels
        def maybe_mi_droplevels(indexer, levels):
            """
            If level does not exist or all levels were dropped, the exception
            has to be handled outside.
            """
            new_index = self[indexer]

            for i in sorted(levels, reverse=True):
                new_index = new_index._drop_level_numbers([i])

            return new_index

        if isinstance(level, (tuple, list)):
            if len(key) != len(level):
                raise AssertionError(
                    "Key for location must have same length as number of levels"
                )
            result = None
            for lev, k in zip(level, key, strict=True):
                loc, new_index = self._get_loc_level(k, level=lev)
                if isinstance(loc, slice):
                    mask = np.zeros(len(self), dtype=bool)
                    mask[loc] = True
                    loc = mask
                result = loc if result is None else result & loc

            try:
                # FIXME: we should be only dropping levels on which we are
                #  scalar-indexing
                mi = maybe_mi_droplevels(result, level)
            except ValueError:
                # droplevel failed because we tried to drop all levels,
                #  i.e. len(level) == self.nlevels
                mi = self[result]

            return result, mi

        # kludge for #1796
        if isinstance(key, list):
            key = tuple(key)

        if isinstance(key, tuple) and level == 0:
            try:
                # Check if this tuple is a single key in our first level
                if key in self.levels[0]:
                    indexer = self._get_level_indexer(key, level=level)
                    new_index = maybe_mi_droplevels(indexer, [0])
                    return indexer, new_index
            except (TypeError, InvalidIndexError):
                pass

            if not any(isinstance(k, slice) for k in key):
                if len(key) == self.nlevels and self.is_unique:
                    # Complete key in unique index -> standard get_loc
                    try:
                        return (self._engine.get_loc(key), None)
                    except KeyError as err:
                        raise KeyError(key) from err
                    except TypeError:
                        # e.g. partial string indexing
                        #  test_partial_string_timestamp_multiindex
                        pass

                # partial selection
                indexer = self.get_loc(key)
                ilevels = [i for i in range(len(key)) if key[i] != slice(None, None)]
                if len(ilevels) == self.nlevels:
                    if is_integer(indexer):
                        # we are dropping all levels
                        return indexer, None

                    # TODO: in some cases we still need to drop some levels,
                    #  e.g. test_multiindex_perf_warn
                    # test_partial_string_timestamp_multiindex
                    ilevels = [
                        i
                        for i in range(len(key))
                        if (
                            not isinstance(key[i], str)
                            or not self.levels[i]._supports_partial_string_indexing
                        )
                        and key[i] != slice(None, None)
                    ]
                    if len(ilevels) == self.nlevels:
                        # TODO: why?
                        ilevels = []
                return indexer, maybe_mi_droplevels(indexer, ilevels)

            else:
                indexer = None
                for i, k in enumerate(key):
                    if not isinstance(k, slice):
                        loc_level = self._get_level_indexer(k, level=i)
                        if isinstance(loc_level, slice):
                            if com.is_null_slice(loc_level) or com.is_full_slice(
                                loc_level, len(self)
                            ):
                                # everything
                                continue

                            # e.g. test_xs_IndexSlice_argument_not_implemented
                            k_index = np.zeros(len(self), dtype=bool)
                            k_index[loc_level] = True

                        else:
                            k_index = loc_level

                    elif com.is_null_slice(k):
                        # taking everything, does not affect `indexer` below
                        continue

                    else:
                        # FIXME: this message can be inaccurate, e.g.
                        #  test_series_varied_multiindex_alignment
                        raise TypeError(f"Expected label or tuple of labels, got {key}")

                    if indexer is None:
                        indexer = k_index
                    else:
                        indexer &= k_index
                if indexer is None:
                    indexer = slice(None, None)
                ilevels = [i for i in range(len(key)) if key[i] != slice(None, None)]
                return indexer, maybe_mi_droplevels(indexer, ilevels)
        else:
            indexer = self._get_level_indexer(key, level=level)
            if (
                isinstance(key, str)
                and self.levels[level]._supports_partial_string_indexing
            ):
                # check to see if we did an exact lookup vs sliced
                check = self.levels[level].get_loc(key)
                if not is_integer(check):
                    # e.g. test_partial_string_timestamp_multiindex
                    return indexer, self[indexer]

            try:
                result_index = maybe_mi_droplevels(indexer, [level])
            except ValueError:
                result_index = self[indexer]

            return indexer, result_index

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py::MultiIndex._get_loc_single_level_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/multi.py]
    def _get_loc_single_level_index(self, level_index: Index, key: Hashable) -> int:
        """
        If key is NA value, location of index unify as -1.

        Parameters
        ----------
        level_index: Index
        key : label

        Returns
        -------
        loc : int
            If key is NA value, loc is -1
            Else, location of key in index.

        See Also
        --------
        Index.get_loc : The get_loc method for (single-level) index.
        """
        if is_scalar(key) and isna(key):
            # TODO: need is_valid_na_for_dtype(key, level_index.dtype)
            return -1
        else:
            return level_index.get_loc(key)  # type: ignore[return-value]
```
