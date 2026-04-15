# pandas-84 :: hybrid-cs

query: BUG: Fix MutliIndexed unstack failures at tuple names (#30943)

## selected nodes

- rank=1 layer=FUNCTION tokens=896 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_multiple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=2 layer=FUNCTION tokens=394 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::unstack file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py
- rank=3 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py::TestDataFrameReshape.unstack_and_compare file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py
- rank=4 layer=FUNCTION tokens=341 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_get_multiindex_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=5 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._exclude_implicit_index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py
- rank=6 layer=FUNCTION tokens=187 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_copy.py::assert_multiindex_copied file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_copy.py
- rank=7 layer=FUNCTION tokens=1022 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_make_concat_multiindex file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=8 layer=FUNCTION tokens=684 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._getitem_nested_tuple file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py
- rank=9 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterGetName file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c
- rank=10 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::at file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::_unstack_multiple [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
def _unstack_multiple(
    data: Series | DataFrame, clocs, fill_value=None, sort: bool = True
):
    if len(clocs) == 0:
        return data

    # NOTE: This doesn't deal with hierarchical columns yet

    index = data.index
    index = cast("MultiIndex", index)  # caller is responsible for checking

    # GH 19966 Make sure if MultiIndexed index has tuple name, they will be
    # recognised as a whole
    if clocs in index.names:
        clocs = [clocs]
    clocs = [index._get_level_number(i) for i in clocs]

    rlocs = [i for i in range(index.nlevels) if i not in clocs]

    clevels = [index.levels[i] for i in clocs]
    ccodes = [index.codes[i] for i in clocs]
    cnames = [index.names[i] for i in clocs]
    rlevels = [index.levels[i] for i in rlocs]
    rcodes = [index.codes[i] for i in rlocs]
    rnames = [index.names[i] for i in rlocs]

    shape = tuple(len(x) for x in clevels)
    group_index = get_group_index(ccodes, shape, sort=False, xnull=False)

    comp_ids, obs_ids = compress_group_index(group_index, sort=False)
    recons_codes = decons_obs_group_ids(comp_ids, obs_ids, shape, ccodes, xnull=False)

    if not rlocs:
        # Everything is in clocs, so the dummy df has a regular index
        dummy_index = Index(obs_ids, name="__placeholder__", copy=False)
    else:
        dummy_index = MultiIndex(
            levels=[*rlevels, obs_ids],
            codes=[*rcodes, comp_ids],
            names=[*rnames, "__placeholder__"],
            verify_integrity=False,
        )

    if isinstance(data, Series):
        dummy = data.copy(deep=False)
        dummy.index = dummy_index

        unstacked = dummy.unstack("__placeholder__", fill_value=fill_value, sort=sort)
        new_levels = clevels
        new_names = cnames
        new_codes = recons_codes
    else:
        if isinstance(data.columns, MultiIndex):
            result = data
            while clocs:
                val = clocs.pop(0)
                # error: Incompatible types in assignment (expression has type
                # "DataFrame | Series", variable has type "DataFrame")
                result = result.unstack(  # type: ignore[assignment]
                    val, fill_value=fill_value, sort=sort
                )
                clocs = [v if v < val else v - 1 for v in clocs]

            return result

        # GH#42579 deep=False to avoid consolidating
        dummy_df = data.copy(deep=False)
        dummy_df.index = dummy_index

        # error: Incompatible types in assignment (expression has type "DataFrame |
        # Series", variable has type "DataFrame")
        unstacked = dummy_df.unstack(  # type: ignore[assignment]
            "__placeholder__", fill_value=fill_value, sort=sort
        )
        if isinstance(unstacked, Series):
            unstcols = unstacked.index
        else:
            unstcols = unstacked.columns
        assert isinstance(unstcols, MultiIndex)  # for mypy
        new_levels = [unstcols.levels[0], *clevels]
        new_names = [data.columns.name, *cnames]

        new_codes = [unstcols.codes[0]]
        new_codes.extend(rec.take(unstcols.codes[-1]) for rec in recons_codes)

    new_columns = MultiIndex(
        levels=new_levels, codes=new_codes, names=new_names, verify_integrity=False
    )

    if isinstance(unstacked, Series):
        unstacked.index = new_columns
    else:
        unstacked.columns = new_columns

    return unstacked

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py::unstack [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/reshape.py]
def unstack(
    obj: Series | DataFrame, level, fill_value=None, sort: bool = True
) -> Series | DataFrame:
    if isinstance(level, (tuple, list)):
        if len(level) != 1:
            # _unstack_multiple only handles MultiIndexes,
            # and isn't needed for a single level
            return _unstack_multiple(obj, level, fill_value=fill_value, sort=sort)
        else:
            level = level[0]

    if not is_integer(level) and not level == "__placeholder__":
        # check if level is valid in case of regular index
        obj.index._get_level_number(level)

    if isinstance(obj, DataFrame):
        if isinstance(obj.index, MultiIndex):
            return _unstack_frame(obj, level, fill_value=fill_value, sort=sort)
        else:
            return obj.T.stack()
    elif not isinstance(obj.index, MultiIndex):
        # GH 36113
        # Give nicer error messages when unstack a Series whose
        # Index is not a MultiIndex.
        raise ValueError(
            f"index must be a MultiIndex to unstack, {type(obj.index)} was passed"
        )
    else:
        if is_1d_only_ea_dtype(obj.dtype):
            return _unstack_extension_series(obj, level, fill_value, sort=sort)
        unstacker = _Unstacker(
            obj.index, level=level, constructor=obj._constructor_expanddim, sort=sort
        )
        return unstacker.get_result(obj, value_columns=None, fill_value=fill_value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py::TestDataFrameReshape.unstack_and_compare [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_stack_unstack.py]
        def unstack_and_compare(df, column_name):
            unstacked1 = df.unstack([column_name])
            unstacked2 = df.unstack(column_name)
            tm.assert_frame_equal(unstacked1, unstacked2)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_get_multiindex_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
def _get_multiindex_indexer(
    join_keys: list[ArrayLike], index: MultiIndex, sort: bool
) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]:
    # left & right join labels and num. of levels at each location
    mapped = (
        _factorize_keys(index.levels[n]._values, join_keys[n], sort=sort)
        for n in range(index.nlevels)
    )
    zipped = zip(*mapped, strict=True)
    rcodes, lcodes, shape = (list(x) for x in zipped)
    if sort:
        rcodes = list(map(np.take, rcodes, index.codes))
    else:
        i8copy = lambda a: a.astype("i8", subok=False)
        rcodes = list(map(i8copy, index.codes))

    # fix right labels if there were any nulls
    for i, join_key in enumerate(join_keys):
        mask = index.codes[i] == -1
        if mask.any():
            # check if there already was any nulls at this location
            # if there was, it is factorized to `shape[i] - 1`
            a = join_key[lcodes[i] == shape[i] - 1]
            if a.size == 0 or not a[0] != a[0]:
                shape[i] += 1

            rcodes[i][mask] = shape[i] - 1

    # get flat i8 join keys
    lkey, rkey = _get_join_keys(lcodes, rcodes, tuple(shape), sort)
    return lkey, rkey

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py::PythonParser._exclude_implicit_index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/parsers/python_parser.py]
    def _exclude_implicit_index(
        self,
        alldata: list[np.ndarray],
    ) -> tuple[Mapping[Hashable, np.ndarray], Sequence[Hashable]]:
        # error: Cannot determine type of 'index_col'
        names = dedup_names(
            self.orig_names,
            is_potential_multi_index(
                self.orig_names,
                self.index_col,
            ),
        )

        offset = 0
        if self._implicit_index:
            offset = len(self.index_col)

        len_alldata = len(alldata)
        self._check_data_length(names, alldata)

        return {
            name: alldata[i + offset] for i, name in enumerate(names) if i < len_alldata
        }, names

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_copy.py::assert_multiindex_copied [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/multi/test_copy.py]
def assert_multiindex_copied(copy, original):
    # Levels should be (at least, shallow copied)
    tm.assert_copy(copy.levels, original.levels)
    tm.assert_almost_equal(copy.codes, original.codes)

    # Labels doesn't matter which way copied
    tm.assert_almost_equal(copy.codes, original.codes)
    assert copy.codes is not original.codes

    # Names doesn't matter which way copied
    assert copy.names == original.names
    assert copy.names is not original.names

    # Sort order should be copied
    assert copy.sortorder == original.sortorder

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_make_concat_multiindex [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py]
def _make_concat_multiindex(indexes, keys, levels=None, names=None) -> MultiIndex:
    if (levels is None and isinstance(keys[0], tuple)) or (
        levels is not None and len(levels) > 1
    ):
        zipped = list(zip(*keys, strict=True))
        if names is None:
            names = [None] * len(zipped)

        if levels is None:
            _, levels = factorize_from_iterables(zipped)
        else:
            levels = [ensure_index(x) for x in levels]
            validate_unique_levels(levels)
    else:
        zipped = [keys]
        if names is None:
            names = [None]

        if levels is None:
            levels = [ensure_index(keys).unique()]
        else:
            levels = [ensure_index(x) for x in levels]
            validate_unique_levels(levels)

    if not all_indexes_same(indexes):
        codes_list = []

        # things are potentially different sizes, so compute the exact codes
        # for each level and pass those to MultiIndex.from_arrays

        for hlevel, level in zip(zipped, levels, strict=True):
            to_concat = []
            if isinstance(hlevel, Index) and hlevel.equals(level):
                lens = [len(idx) for idx in indexes]
                codes_list.append(np.repeat(np.arange(len(hlevel)), lens))
            else:
                for key, index in zip(hlevel, indexes, strict=True):
                    # Find matching codes, include matching nan values as equal.
                    mask = (isna(level) & isna(key)) | (level == key)
                    if not mask.any():
                        raise ValueError(f"Key {key} not in level {level}")
                    i = np.nonzero(mask)[0][0]

                    to_concat.append(np.repeat(i, len(index)))
                codes_list.append(np.concatenate(to_concat))

        concat_index = _concat_indexes(indexes)

        # these go at the end
        if isinstance(concat_index, MultiIndex):
            levels.extend(concat_index.levels)
            codes_list.extend(concat_index.codes)
        else:
            codes, categories = factorize_from_iterable(concat_index)
            levels.append(categories)
            codes_list.append(codes)

        if len(names) == len(levels):
            names = list(names)
        else:
            # make sure that all of the passed indices have the same nlevels
            if not len({idx.nlevels for idx in indexes}) == 1:
                raise AssertionError(
                    "Cannot concat indices that do not have the same number of levels"
                )

            # also copies
            names = list(names) + list(get_unanimous_names(*indexes))

        return MultiIndex(
            levels=levels, codes=codes_list, names=names, verify_integrity=False
        )

    new_index = indexes[0]
    n = len(new_index)
    kpieces = len(indexes)

    # also copies
    new_names = list(names)
    new_levels = list(levels)

    # construct codes
    new_codes = []

    # do something a bit more speedy

    for hlevel, level in zip(zipped, levels, strict=True):
        hlevel_index = ensure_index(hlevel)
        mapped = level.get_indexer(hlevel_index)

        mask = mapped == -1
        if mask.any():
            raise ValueError(
                f"Values not found in passed level: {hlevel_index[mask]!s}"
            )

        new_codes.append(np.repeat(mapped, n))

    if isinstance(new_index, MultiIndex):
        new_levels.extend(new_index.levels)
        new_codes.extend(np.tile(lab, kpieces) for lab in new_index.codes)
    else:
        new_levels.append(new_index.unique())
        single_codes = new_index.unique().get_indexer(new_index)
        new_codes.append(np.tile(single_codes, kpieces))

    if len(new_names) < len(new_levels):
        new_names.extend(new_index.names)

    return MultiIndex(
        levels=new_levels, codes=new_codes, names=new_names, verify_integrity=False
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._getitem_nested_tuple [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _getitem_nested_tuple(self, tup: tuple):
        # we have a nested tuple so have at least 1 multi-index level
        # we should be able to match up the dimensionality here

        for key in tup:
            check_dict_or_set_indexers(key)

        # we have too many indexers for our dim, but have at least 1
        # multi-index dimension, try to see if we have something like
        # a tuple passed to a series with a multi-index
        if len(tup) > self.ndim:
            if self.name != "loc":
                # This should never be reached, but let's be explicit about it
                raise ValueError("Too many indices")  # pragma: no cover
            if all(
                is_hashable(x, allow_slice=False) or com.is_null_slice(x) for x in tup
            ):
                # GH#10521 Series should reduce MultiIndex dimensions instead of
                #  DataFrame, IndexingError is not raised when slice(None,None,None)
                #  with one row.
                with suppress(IndexingError):
                    return cast("_LocIndexer", self)._handle_lowerdim_multi_index_axis0(
                        tup
                    )
            elif isinstance(self.obj, ABCSeries) and any(
                isinstance(k, tuple) for k in tup
            ):
                # GH#35349 Raise if tuple in tuple for series
                # Do this after the all-hashable-or-null-slice check so that
                #  we are only getting non-hashable tuples, in particular ones
                #  that themselves contain a slice entry
                # See test_loc_series_getitem_too_many_dimensions
                raise IndexingError("Too many indexers")

            # this is a series with a multi-index specified a tuple of
            # selectors
            axis = self.axis or 0
            return self._getitem_axis(tup, axis=axis)

        # handle the multi-axis by taking sections and reducing
        # this is iterative
        obj = self.obj
        # GH#41369 Loop in reverse order ensures indexing along columns before rows
        # which selects only necessary blocks which avoids dtype conversion if possible
        axis = len(tup) - 1
        for key in reversed(tup):
            if com.is_null_slice(key):
                axis -= 1
                continue

            obj = getattr(obj, self.name)._getitem_axis(key, axis=axis)
            axis -= 1

            # if we have a scalar, we are done
            if is_scalar(obj) or not hasattr(obj, "ndim"):
                break

        return obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c::Tuple_iterGetName [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/src/vendored/ujson/python/objToJSON.c]
static const char *Tuple_iterGetName(JSOBJ Py_UNUSED(obj),
                                     JSONTypeContext *Py_UNUSED(tc),
                                     size_t *Py_UNUSED(outLen)) {
  return NULL;
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py::at [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/__init__.py]
def at(x):
    return x.at
```
