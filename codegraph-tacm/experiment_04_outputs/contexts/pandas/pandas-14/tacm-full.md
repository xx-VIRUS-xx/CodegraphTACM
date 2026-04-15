# pandas-14 :: tacm-full

query: BUG: DataFrame[object] + Series[dt64], test parametrization (#33824)

## selected nodes

- rank=1 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py::unpack_obj file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py
- rank=2 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=3 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
- rank=4 layer=FUNCTION tokens=377 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=5 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py::skip_if_installed file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py
- rank=6 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::downsample_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py
- rank=7 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::resample_method file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py
- rank=8 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=9 layer=FUNCTION tokens=255 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::_check_where_equivalences file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=10 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.time_add_np_dt64 file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py
- rank=11 layer=FUNCTION tokens=953 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby._apply_pairwise file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=12 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::box_with_array file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py
- rank=13 layer=FUNCTION tokens=1206 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/hashing.py::hash_pandas_object file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/hashing.py
- rank=14 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/indexing.py::GroupByNthSelector.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/indexing.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py::unpack_obj [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/apply/test_frame_transform.py]
def unpack_obj(obj, klass, axis):
    """
    Helper to ensure we have the right type of object for a test parametrized
    over frame_or_series.
    """
    if klass is not DataFrame:
        obj = obj["A"]
        if axis != 0:
            pytest.skip(f"Test is only for DataFrame with axis={axis}")
    return obj

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py::TestNonNano.ts [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/scalar/timestamp/test_timestamp.py]
    def ts(self, dt64):
        return Timestamp._from_dt64(dt64)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py::skip_if_installed [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/util/_test_decorators.py]
def skip_if_installed(package: str) -> pytest.MarkDecorator:
    """
    Skip a test if a package is installed.

    Parameters
    ----------
    package : str
        The name of the package.

    Returns
    -------
    pytest.MarkDecorator
        a pytest.mark.skipif to use as either a test decorator or a
        parametrization mark.
    """
    return pytest.mark.skipif(
        bool(import_optional_dependency(package, errors="ignore")),
        reason=f"Skipping because {package} is installed.",
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::downsample_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py]
def downsample_method(request):
    """Fixture for parametrization of Grouper downsample methods."""
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py::resample_method [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/resample/conftest.py]
def resample_method(request):
    """Fixture for parametrization of Grouper resample methods."""
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::index_or_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def index_or_series(request):
    """
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::_check_where_equivalences [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py]
def _check_where_equivalences(df, mask, other, expected):
    # similar to tests.series.indexing.test_setitem.SetitemCastingEquivalences
    #  but with DataFrame in mind and less fleshed-out
    res = df.where(mask, other)
    tm.assert_frame_equal(res, expected)

    res = df.mask(~mask, other)
    tm.assert_frame_equal(res, expected)

    # Note: frame.mask(~mask, other, inplace=True) takes some more work bc
    #  Block.putmask does *not* downcast.  The change to 'expected' here
    #  is specific to the cases in test_where_dt64_2d.
    df = df.copy()
    df.mask(~mask, other, inplace=True)
    if not mask.all():
        # with mask.all(), Block.putmask is a no-op, so does not downcast
        expected = expected.copy()
        expected["A"] = expected["A"].astype(object)
    tm.assert_frame_equal(df, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py::OffestDatetimeArithmetic.time_add_np_dt64 [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/tslibs/offsets.py]
    def time_add_np_dt64(self, offset):
        offset + self.dt64

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby._apply_pairwise [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def _apply_pairwise(
        self,
        target: DataFrame | Series,
        other: DataFrame | Series | None,
        pairwise: bool | None,
        func: Callable[[DataFrame | Series, DataFrame | Series], DataFrame | Series],
        numeric_only: bool,
    ) -> DataFrame | Series:
        """
        Apply the given pairwise function given 2 pandas objects (DataFrame/Series)
        """
        # Manually drop the grouping column first
        target = target.drop(columns=self._grouper.names, errors="ignore")
        result = super()._apply_pairwise(target, other, pairwise, func, numeric_only)
        # 1) Determine the levels + codes of the groupby levels
        if other is not None and not all(
            len(group) == len(other) for group in self._grouper.indices.values()
        ):
            # GH 42915
            # len(other) != len(any group), so must reindex (expand) the result
            # from flex_binary_moment to a "transform"-like result
            # per groupby combination
            old_result_len = len(result)
            result = concat(
                [
                    result.take(gb_indices).reindex(result.index)
                    for gb_indices in self._grouper.indices.values()
                ]
            )

            gb_pairs = (
                com.maybe_make_list(pair) for pair in self._grouper.indices.keys()
            )
            groupby_codes = []
            groupby_levels = []
            # e.g. [[1, 2], [4, 5]] as [[1, 4], [2, 5]]
            for gb_level_pair in map(list, zip(*gb_pairs, strict=True)):
                labels = np.repeat(np.array(gb_level_pair), old_result_len)
                codes, levels = factorize(labels)
                groupby_codes.append(codes)
                groupby_levels.append(levels)
        else:
            # pairwise=True or len(other) == len(each group), so repeat
            # the groupby labels by the number of columns in the original object
            groupby_codes = self._grouper.codes
            # error: Incompatible types in assignment (expression has type
            # "List[Index]", variable has type "List[Union[ndarray, Index]]")
            groupby_levels = self._grouper.levels  # type: ignore[assignment]

            group_indices = self._grouper.indices.values()
            if group_indices:
                indexer = np.concatenate(list(group_indices))
            else:
                indexer = np.array([], dtype=np.intp)

            if target.ndim == 1:
                repeat_by = 1
            else:
                repeat_by = len(target.columns)
            groupby_codes = [
                np.repeat(c.take(indexer), repeat_by) for c in groupby_codes
            ]
        # 2) Determine the levels + codes of the result from super()._apply_pairwise
        if isinstance(result.index, MultiIndex):
            result_codes = list(result.index.codes)
            result_levels = list(result.index.levels)
            result_names = list(result.index.names)
        else:
            idx_codes, idx_levels = factorize(result.index)
            result_codes = [idx_codes]
            result_levels = [idx_levels]
            result_names = [result.index.name]

            # 3) Create the resulting index by combining 1) + 2)
        result_codes = groupby_codes + result_codes
        result_levels = groupby_levels + result_levels
        result_names = self._grouper.names + result_names

        result_index = MultiIndex(
            result_levels, result_codes, names=result_names, verify_integrity=False
        )
        result.index = result_index
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py::box_with_array [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/conftest.py]
def box_with_array(request):
    """
    Fixture to test behavior for Index, Series, DataFrame, and pandas Array
    classes
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/hashing.py::hash_pandas_object [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/util/hashing.py]
def hash_pandas_object(
    obj: Index | DataFrame | Series,
    index: bool = True,
    encoding: str = "utf8",
    hash_key: str | None = _default_hash_key,
    categorize: bool = True,
) -> Series:
    """
    Return a data hash of the Index/Series/DataFrame.

    The hash is computed element-wise using the underlying data values,
    and optionally includes the index when hashing a Series or DataFrame.

    Parameters
    ----------
    obj : Index, Series, or DataFrame
        The pandas object to hash.
    index : bool, default True
        Include the index in the hash (if Series/DataFrame). When True,
        the hash for each row depends on both the value and the index label,
        so the same value at a different index position will produce a
        different hash.
    encoding : str, default 'utf8'
        Encoding for data & key when strings.
    hash_key : str, default _default_hash_key
        Hash_key for string key to encode.
    categorize : bool, default True
        Whether to first categorize object arrays before hashing. This is more
        efficient when the array contains duplicate values.

    Returns
    -------
    Series of uint64
        Same length as the object.

    See Also
    --------
    util.hash_array : Return a hash of the given array.
    util.hash_tuples : Hash a MultiIndex or listlike-of-tuples efficiently.

    Examples
    --------
    >>> pd.util.hash_pandas_object(pd.Series([1, 2, 3]))
    0    14639053686158035780
    1     3869563279212530728
    2      393322362522515241
    dtype: uint64

    By default, the hash includes the index, so the same value at a
    different index position will produce a different hash:

    >>> df1 = pd.DataFrame({"a": ["a", "b", "c"]})
    >>> df2 = pd.DataFrame({"a": ["b", "a", "c"]})
    >>> pd.util.hash_pandas_object(df1)
    0     4578374827886788867
    1    17338122309987883691
    2     5473791562133574857
    dtype: uint64
    >>> pd.util.hash_pandas_object(df2)
    0     8168238220198793318
    1    14044658390916132862
    2     5473791562133574857
    dtype: uint64

    Set ``index=False`` to hash only the values. In this case, the same
    value always produces the same hash regardless of its position:

    >>> pd.util.hash_pandas_object(df1, index=False)
    0     5694802365760992243
    1     2797248057711234736
    2    18202460376300699891
    dtype: uint64
    >>> pd.util.hash_pandas_object(df2, index=False)
    0     2797248057711234736
    1     5694802365760992243
    2    18202460376300699891
    dtype: uint64
    """
    from pandas import Series

    if hash_key is None:
        hash_key = _default_hash_key

    if isinstance(obj, ABCMultiIndex):
        return Series(hash_tuples(obj, encoding, hash_key), dtype="uint64", copy=False)

    elif isinstance(obj, ABCIndex):
        h = hash_array(obj._values, encoding, hash_key, categorize).astype(
            "uint64", copy=False
        )
        ser = Series(h, index=obj, dtype="uint64", copy=False)

    elif isinstance(obj, ABCSeries):
        h = hash_array(obj._values, encoding, hash_key, categorize).astype(
            "uint64", copy=False
        )
        if index:
            index_iter = (
                hash_pandas_object(
                    obj.index,
                    index=False,
                    encoding=encoding,
                    hash_key=hash_key,
                    categorize=categorize,
                )._values
                for _ in [None]
            )
            arrays = itertools.chain([h], index_iter)
            h = combine_hash_arrays(arrays, 2)

        ser = Series(h, index=obj.index, dtype="uint64", copy=False)

    elif isinstance(obj, ABCDataFrame):
        hashes = (
            hash_array(series._values, encoding, hash_key, categorize)
            for _, series in obj.items()
        )
        num_items = len(obj.columns)
        if index:
            index_hash_generator = (
                hash_pandas_object(
                    obj.index,
                    index=False,
                    encoding=encoding,
                    hash_key=hash_key,
                    categorize=categorize,
                )._values
                for _ in [None]
            )
            num_items += 1

            # keep `hashes` specifically a generator to keep mypy happy
            _hashes = itertools.chain(hashes, index_hash_generator)
            hashes = (x for x in _hashes)
        h = combine_hash_arrays(hashes, num_items)

        ser = Series(h, index=obj.index, dtype="uint64", copy=False)
    else:
        raise TypeError(f"Unexpected type for hashing {type(obj)}")

    return ser

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/indexing.py::GroupByNthSelector.__getitem__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/indexing.py]
    def __getitem__(self, n: PositionalIndexer | tuple) -> DataFrame | Series:
        return self.groupby_object._nth(n)
```
