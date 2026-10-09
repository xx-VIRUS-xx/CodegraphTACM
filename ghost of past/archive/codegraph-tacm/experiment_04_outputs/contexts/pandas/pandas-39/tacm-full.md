# pandas-39 :: tacm-full

query: BUG: Fixed strange behaviour of pd.DataFrame.drop() with inplace argu… (#30501)

## selected nodes

- rank=1 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=2 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=3 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_string file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=4 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_int file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=5 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_bool file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=6 layer=FUNCTION tokens=2156 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.set_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=7 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_na file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py
- rank=8 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=9 layer=FUNCTION tokens=890 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.drop_duplicates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=10 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py::ReplaceList.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py
- rank=11 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Iteration.time_items file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_int [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_series_drop_dups_int(self, inplace):
        self.s.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups(self, inplace):
        self.df.drop_duplicates(["key1", "key2"], inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_series_drop_dups_string [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_series_drop_dups_string(self, inplace):
        self.s_str.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_int [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups_int(self, inplace):
        self.df_int.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_bool [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups_bool(self, inplace):
        self.df_bool.drop_duplicates(inplace=inplace)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.set_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
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
        Set the DataFrame index using existing columns.

        Set the DataFrame index (row labels) using one or more existing
        columns or arrays (of the correct length). The index can replace the
        existing index or expand on it.

        Parameters
        ----------
        keys : label or array-like or list of labels/arrays
            This parameter can be either a single column key, a single array of
            the same length as the calling DataFrame, or a list containing an
            arbitrary combination of column keys and arrays. Here, "array"
            encompasses :class:`Series`, :class:`Index`, ``np.ndarray``, and
            instances of :class:`~collections.abc.Iterator`.
        drop : bool, default True
            Delete columns to be used as the new index.
        append : bool, default False
            Whether to append columns to existing index.
            Setting to True will add the new columns to existing index.
            When set to False, the current index will be dropped from the DataFrame.
        inplace : bool, default False
            Whether to modify the DataFrame rather than creating a new one.
        verify_integrity : bool, default False
            Check the new index for duplicates. Otherwise defer the check until
            necessary. Setting to False will improve the performance of this
            method.

            .. deprecated:: 3.0.0

        Returns
        -------
        DataFrame or None
            Changed row labels or None if ``inplace=True``.

        See Also
        --------
        DataFrame.reset_index : Opposite of set_index.
        DataFrame.reindex : Change to new indices or expand indices.
        DataFrame.reindex_like : Change to same indices as other DataFrame.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "month": [1, 4, 7, 10],
        ...         "year": [2012, 2014, 2013, 2014],
        ...         "sale": [55, 40, 84, 31],
        ...     }
        ... )
        >>> df
           month  year  sale
        0      1  2012    55
        1      4  2014    40
        2      7  2013    84
        3     10  2014    31

        Set the index to become the 'month' column:

        >>> df.set_index("month")
               year  sale
        month
        1      2012    55
        4      2014    40
        7      2013    84
        10     2014    31

        Create a MultiIndex using columns 'year' and 'month':

        >>> df.set_index(["year", "month"])
                    sale
        year  month
        2012  1     55
        2014  4     40
        2013  7     84
        2014  10    31

        Create a MultiIndex using an Index and a column:

        >>> df.set_index([pd.Index([1, 2, 3, 4]), "year"])
                 month  sale
           year
        1  2012  1      55
        2  2014  4      40
        3  2013  7      84
        4  2014  10     31

        Create a MultiIndex using two Series:

        >>> s = pd.Series([1, 2, 3, 4])
        >>> df.set_index([s, s**2])
              month  year  sale
        1 1       1  2012    55
        2 4       4  2014    40
        3 9       7  2013    84
        4 16     10  2014    31

        Append a column to the existing index:

        >>> df = df.set_index("month")
        >>> df.set_index("year", append=True)
                      sale
        month  year
        1      2012    55
        4      2014    40
        7      2013    84
        10     2014    31

        >>> df.set_index("year", append=False)
               sale
        year
        2012    55
        2014    40
        2013    84
        2014    31
        """
        if verify_integrity is not lib.no_default:
            # GH#62919
            warnings.warn(
                "The 'verify_integrity' keyword in DataFrame.set_index is "
                "deprecated and will be removed in a future version. "
                "Directly check the result.index.is_unique instead.",
                Pandas4Warning,
                stacklevel=find_stack_level(),
            )
        else:
            verify_integrity = False

        inplace = validate_bool_kwarg(inplace, "inplace")
        self._check_inplace_and_allows_duplicate_labels(inplace)
        if not isinstance(keys, list):
            keys = [keys]

        err_msg = (
            'The parameter "keys" may be a column key, one-dimensional '
            "array, or a list containing only valid column keys and "
            "one-dimensional arrays."
        )

        missing: list[Hashable] = []
        for col in keys:
            if isinstance(col, (Index, Series, np.ndarray, list, abc.Iterator)):
                # arrays are fine as long as they are one-dimensional
                # iterators get converted to list below
                if getattr(col, "ndim", 1) != 1:
                    raise ValueError(err_msg)
            else:
                # everything else gets tried as a key; see GH 24969
                try:
                    found = col in self.columns
                except TypeError as err:
                    raise TypeError(
                        f"{err_msg}. Received column of type {type(col)}"
                    ) from err
                else:
                    if not found:
                        missing.append(col)

        if missing:
            raise KeyError(f"None of {missing} are in the columns")

        if inplace:
            frame = self
        else:
            frame = self.copy(deep=False)

        arrays: list[Index] = []
        names: list[Hashable] = []
        if append:
            names = list(self.index.names)
            if isinstance(self.index, MultiIndex):
                arrays.extend(
                    self.index._get_level_values(i) for i in range(self.index.nlevels)
                )
            else:
                arrays.append(self.index)

        to_remove: set[Hashable] = set()
        for col in keys:
            if isinstance(col, MultiIndex):
                arrays.extend(col._get_level_values(n) for n in range(col.nlevels))
                names.extend(col.names)
            elif isinstance(col, (Index, Series)):
                # if Index then not MultiIndex (treated above)

                # error: Argument 1 to "append" of "list" has incompatible type
                #  "Union[Index, Series]"; expected "Index"
                arrays.append(col)  # type: ignore[arg-type]
                names.append(col.name)
            elif isinstance(col, (list, np.ndarray)):
                # error: Argument 1 to "append" of "list" has incompatible type
                # "Union[List[Any], ndarray]"; expected "Index"
                arrays.append(col)  # type: ignore[arg-type]
                names.append(None)
            elif isinstance(col, abc.Iterator):
                # error: Argument 1 to "append" of "list" has incompatible type
                # "List[Any]"; expected "Index"
                arrays.append(list(col))  # type: ignore[arg-type]
                names.append(None)
            # from here, col can only be a column label
            else:
                arrays.append(frame[col])
                names.append(col)
                if drop:
                    to_remove.add(col)

            if len(arrays[-1]) != len(self):
                # check newest element against length of calling frame, since
                # ensure_index_from_sequences would not raise for append=False.
                raise ValueError(
                    f"Length mismatch: Expected {len(self)} rows, "
                    f"received array of length {len(arrays[-1])}"
                )

        index = ensure_index_from_sequences(arrays, names)

        if verify_integrity and not index.is_unique:
            duplicates = index[index.duplicated()].unique()
            raise ValueError(f"Index has duplicate keys: {duplicates}")

        # use set to handle duplicate column names gracefully in case of drop
        for c in to_remove:
            del frame[c]

        # clear up memory usage
        index._cleanup()

        frame.index = index

        if not inplace:
            return frame
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py::DropDuplicates.time_frame_drop_dups_na [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/reindex.py]
    def time_frame_drop_dups_na(self, inplace):
        self.df_nan.drop_duplicates(["key1", "key2"], inplace=inplace)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.drop_duplicates [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def drop_duplicates(
        self,
        subset: Hashable | Iterable[Hashable] | None = None,
        *,
        keep: DropKeep = "first",
        inplace: bool = False,
        ignore_index: bool = False,
    ) -> DataFrame | None:
        """
        Return DataFrame with duplicate rows removed.

        Considering certain columns is optional. Indexes, including time indexes
        are ignored.

        Parameters
        ----------
        subset : column label or iterable of labels, optional
            Only consider certain columns for identifying duplicates, by
            default use all of the columns.
        keep : {'first', 'last', ``False``}, default 'first'
            Determines which duplicates (if any) to keep.

            - 'first' : Drop duplicates except for the first occurrence.
            - 'last' : Drop duplicates except for the last occurrence.
            - ``False`` : Drop all duplicates.

        inplace : bool, default ``False``
            Whether to modify the DataFrame rather than creating a new one.
        ignore_index : bool, default ``False``
            If ``True``, the resulting axis will be labeled 0, 1, …, n - 1.

        Returns
        -------
        DataFrame or None
            DataFrame with duplicates removed or None if ``inplace=True``.

        See Also
        --------
        DataFrame.value_counts: Count unique combinations of columns.

        Notes
        -----
        This method requires columns specified by ``subset`` to be of hashable type.
        Passing unhashable columns will raise a ``TypeError``.

        Examples
        --------
        Consider dataset containing ramen rating.

        >>> df = pd.DataFrame(
        ...     {
        ...         "brand": ["Yum Yum", "Yum Yum", "Indomie", "Indomie", "Indomie"],
        ...         "style": ["cup", "cup", "cup", "pack", "pack"],
        ...         "rating": [4, 4, 3.5, 15, 5],
        ...     }
        ... )
        >>> df
            brand style  rating
        0  Yum Yum   cup     4.0
        1  Yum Yum   cup     4.0
        2  Indomie   cup     3.5
        3  Indomie  pack    15.0
        4  Indomie  pack     5.0

        By default, it removes duplicate rows based on all columns.

        >>> df.drop_duplicates()
            brand style  rating
        0  Yum Yum   cup     4.0
        2  Indomie   cup     3.5
        3  Indomie  pack    15.0
        4  Indomie  pack     5.0

        To remove duplicates on specific column(s), use ``subset``.

        >>> df.drop_duplicates(subset=["brand"])
            brand style  rating
        0  Yum Yum   cup     4.0
        2  Indomie   cup     3.5

        To remove duplicates and keep last occurrences, use ``keep``.

        >>> df.drop_duplicates(subset=["brand", "style"], keep="last")
            brand style  rating
        1  Yum Yum   cup     4.0
        2  Indomie   cup     3.5
        4  Indomie  pack     5.0
        """
        if self.empty:
            return self.copy(deep=False)

        inplace = validate_bool_kwarg(inplace, "inplace")
        ignore_index = validate_bool_kwarg(ignore_index, "ignore_index")

        result = self[-self.duplicated(subset, keep=keep)]
        if ignore_index:
            result.index = default_index(len(result))

        if inplace:
            self._update_inplace(result)
            return None
        else:
            return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py::ReplaceList.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/replace.py]
    def setup(self, inplace):
        self.df = pd.DataFrame({"A": 0, "B": 0}, index=range(10**7))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py::Iteration.time_items [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/frame_methods.py]
    def time_items(self):
        # (monitor no-copying behaviour)
        for name, col in self.df.items():
            pass
```
