# pandas-51 :: hybrid-cs

query: BUG: fix in categorical merges (#32079)

## selected nodes

- rank=1 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical.tests_merge_categorical_unordered_equal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=2 layer=FUNCTION tokens=1647 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::union_categoricals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py
- rank=3 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::_maybe_unwrap file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py
- rank=4 layer=FUNCTION tokens=367 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py::assert_categorical_single_grouper file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py
- rank=5 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical._categories_match_up_to_permutation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=6 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical._encode_with_my_categories file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=7 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::create_categorical_intervals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py
- rank=8 layer=FUNCTION tokens=343 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype._get_common_dtype file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=9 layer=FUNCTION tokens=268 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._should_compare file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=10 layer=FUNCTION tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/sphinxext/announce.py::get_pull_requests file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/sphinxext/announce.py
- rank=11 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_for_grouping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py
- rank=12 layer=FUNCTION tokens=170 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::complexobject_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h
- rank=13 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::_node_cmp file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical.tests_merge_categorical_unordered_equal [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py]
    def tests_merge_categorical_unordered_equal(self):
        # GH-19551
        df1 = DataFrame(
            {
                "Foo": Categorical(["A", "B", "C"], categories=["A", "B", "C"]),
                "Left": ["A0", "B0", "C0"],
            }
        )

        df2 = DataFrame(
            {
                "Foo": Categorical(["C", "B", "A"], categories=["C", "B", "A"]),
                "Right": ["C1", "B1", "A1"],
            }
        )
        result = merge(df1, df2, on=["Foo"])
        expected = DataFrame(
            {
                "Foo": Categorical(["A", "B", "C"]),
                "Left": ["A0", "B0", "C0"],
                "Right": ["A1", "B1", "C1"],
            }
        )
        tm.assert_frame_equal(result, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::union_categoricals [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py]
def union_categoricals(
    to_union: Sequence[CategoricalIndex | Series | Categorical],
    sort_categories: bool = False,
    ignore_order: bool = False,
) -> Categorical:
    """
    Combine list-like of Categorical-like, unioning categories.

    All categories must have the same dtype.

    Parameters
    ----------
    to_union : list-like
        Categorical, CategoricalIndex, or Series with dtype='category'.
    sort_categories : bool, default False
        If true, resulting categories will be lexsorted, otherwise
        they will be ordered as they appear in the data.
    ignore_order : bool, default False
        If true, the ordered attribute of the Categoricals will be ignored.
        Results in an unordered categorical.

    Returns
    -------
    Categorical
        The union of categories being combined.

    Raises
    ------
    TypeError
        - all inputs do not have the same dtype
        - all inputs do not have the same ordered property
        - all inputs are ordered and their categories are not identical
        - sort_categories=True and Categoricals are ordered
    ValueError
        Empty list of categoricals passed

    See Also
    --------
    CategoricalDtype : Type for categorical data with the categories and orderedness.
    Categorical : Represent a categorical variable in classic R / S-plus fashion.

    Notes
    -----
    To learn more about categories, see `link
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#unioning>`__

    Examples
    --------
    If you want to combine categoricals that do not necessarily have
    the same categories, `union_categoricals` will combine a list-like
    of categoricals. The new categories will be the union of the
    categories being combined.

    >>> a = pd.Categorical(["b", "c"])
    >>> b = pd.Categorical(["a", "b"])
    >>> pd.api.types.union_categoricals([a, b])
    ['b', 'c', 'a', 'b']
    Categories (3, str): ['b', 'c', 'a']

    By default, the resulting categories will be ordered as they appear
    in the `categories` of the data. If you want the categories to be
    lexsorted, use `sort_categories=True` argument.

    >>> pd.api.types.union_categoricals([a, b], sort_categories=True)
    ['b', 'c', 'a', 'b']
    Categories (3, str): ['a', 'b', 'c']

    `union_categoricals` also works with the case of combining two
    categoricals of the same categories and order information (e.g. what
    you could also `append` for).

    >>> a = pd.Categorical(["a", "b"], ordered=True)
    >>> b = pd.Categorical(["a", "b", "a"], ordered=True)
    >>> pd.api.types.union_categoricals([a, b])
    ['a', 'b', 'a', 'b', 'a']
    Categories (2, str): ['a' < 'b']

    Raises `TypeError` because the categories are ordered and not identical.

    >>> a = pd.Categorical(["a", "b"], ordered=True)
    >>> b = pd.Categorical(["a", "b", "c"], ordered=True)
    >>> pd.api.types.union_categoricals([a, b])
    Traceback (most recent call last):
        ...
    TypeError: to union ordered Categoricals, all categories must be the same

    Ordered categoricals with different categories or orderings can be
    combined by using the `ignore_order=True` argument.

    >>> a = pd.Categorical(["a", "b", "c"], ordered=True)
    >>> b = pd.Categorical(["c", "b", "a"], ordered=True)
    >>> pd.api.types.union_categoricals([a, b], ignore_order=True)
    ['a', 'b', 'c', 'c', 'b', 'a']
    Categories (3, str): ['a', 'b', 'c']

    `union_categoricals` also works with a `CategoricalIndex`, or `Series`
    containing categorical data, but note that the resulting array will
    always be a plain `Categorical`

    >>> a = pd.Series(["b", "c"], dtype="category")
    >>> b = pd.Series(["a", "b"], dtype="category")
    >>> pd.api.types.union_categoricals([a, b])
    ['b', 'c', 'a', 'b']
    Categories (3, str): ['b', 'c', 'a']
    """
    from pandas import Categorical
    from pandas.core.arrays.categorical import recode_for_categories

    if len(to_union) == 0:
        raise ValueError("No Categoricals to union")

    def _maybe_unwrap(
        x: CategoricalIndex | Series | Categorical,
    ) -> Categorical:
        if isinstance(x, (ABCCategoricalIndex, ABCSeries)):
            return x._values
        elif isinstance(x, Categorical):
            return x
        else:
            raise TypeError("all components to combine must be Categorical")

    to_union = cast("list[Categorical]", [_maybe_unwrap(x) for x in to_union])
    first = to_union[0]

    if not lib.dtypes_all_equal([obj.categories.dtype for obj in to_union]):
        raise TypeError("dtype of categories must be the same")

    ordered: bool | None = False
    if all(first._categories_match_up_to_permutation(other) for other in to_union[1:]):
        # identical categories - fastpath
        categories = first.categories
        ordered = first.ordered

        all_codes = [first._encode_with_my_categories(x)._codes for x in to_union]
        new_codes = np.concatenate(all_codes)

        if sort_categories and not ignore_order and ordered:
            raise TypeError("Cannot use sort_categories=True with ordered Categoricals")

        if sort_categories and not categories.is_monotonic_increasing:
            categories = categories.sort_values()
            indexer = categories.get_indexer(first.categories)

            from pandas.core.algorithms import take_nd

            new_codes = take_nd(indexer, new_codes, fill_value=-1)
    elif ignore_order or all(not c.ordered for c in to_union):
        # different categories - union and recode
        cats = first.categories.append([c.categories for c in to_union[1:]])
        categories = cats.unique()
        if sort_categories:
            categories = categories.sort_values()

        all_codes = [
            recode_for_categories(c.codes, c.categories, categories, copy=False)
            for c in to_union
        ]
        new_codes = np.concatenate(all_codes)
    else:
        # ordered - to show a proper error message
        if all(c.ordered for c in to_union):
            msg = "to union ordered Categoricals, all categories must be the same"
            raise TypeError(msg)
        raise TypeError("Categorical.ordered must be the same")

    if ignore_order:
        ordered = False

    dtype = CategoricalDtype(categories=categories, ordered=ordered)
    return Categorical._simple_new(new_codes, dtype=dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::_maybe_unwrap [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py]
    def _maybe_unwrap(
        x: CategoricalIndex | Series | Categorical,
    ) -> Categorical:
        if isinstance(x, (ABCCategoricalIndex, ABCSeries)):
            return x._values
        elif isinstance(x, Categorical):
            return x
        else:
            raise TypeError("all components to combine must be Categorical")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py::assert_categorical_single_grouper [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py]
def assert_categorical_single_grouper(
    education_df, as_index, observed, expected_index, normalize, name, expected_data
):
    # Test single categorical grouper when non-groupers are also categorical
    education_df = education_df.copy().astype("category")

    # Add non-observed grouping categories
    education_df["country"] = education_df["country"].cat.add_categories(["ASIA"])

    gp = education_df.groupby("country", as_index=as_index, observed=observed)
    result = gp.value_counts(normalize=normalize)

    expected_series = Series(
        data=expected_data,
        index=MultiIndex.from_tuples(
            expected_index,
            names=["country", "gender", "education"],
        ),
        name=name,
    )
    for i in range(3):
        index_level = CategoricalIndex(expected_series.index.levels[i])
        if i == 0:
            index_level = index_level.set_categories(
                education_df["country"].cat.categories
            )
        expected_series.index = expected_series.index.set_levels(index_level, level=i)

    if as_index:
        tm.assert_series_equal(result, expected_series)
    else:
        expected = expected_series.reset_index(name=name)
        tm.assert_frame_equal(result, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical._categories_match_up_to_permutation [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py]
    def _categories_match_up_to_permutation(self, other: Categorical) -> bool:
        """
        Returns True if categoricals are the same dtype
          same categories, and same ordered

        Parameters
        ----------
        other : Categorical

        Returns
        -------
        bool
        """
        return hash(self.dtype) == hash(other.dtype)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical._encode_with_my_categories [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py]
    def _encode_with_my_categories(self, other: Categorical) -> Categorical:
        """
        Re-encode another categorical using this Categorical's categories.

        Notes
        -----
        This assumes we have already checked
        self._categories_match_up_to_permutation(other).
        """
        # Indexing on codes is more efficient if categories are the same,
        #  so we can apply some optimizations based on the degree of
        #  dtype-matching.
        codes = recode_for_categories(
            other.codes, other.categories, self.categories, copy=False
        )
        return self._from_backing_data(codes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py::create_categorical_intervals [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_interval.py]
def create_categorical_intervals(left, right, closed="right"):
    return Categorical(IntervalIndex.from_arrays(left, right, closed))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype._get_common_dtype [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def _get_common_dtype(self, dtypes: list[DtypeObj]) -> DtypeObj | None:
        # check if we have all categorical dtype with identical categories
        if all(isinstance(x, CategoricalDtype) for x in dtypes):
            first = dtypes[0]
            if all(first == other for other in dtypes[1:]):
                return first

        # special case non-initialized categorical
        # TODO we should figure out the expected return value in general
        non_init_cats = [
            isinstance(x, CategoricalDtype) and x.categories is None for x in dtypes
        ]
        if all(non_init_cats):
            return self
        elif any(non_init_cats):
            return None

        # categorical is aware of Sparse -> extract sparse subdtypes
        subtypes = (x.subtype if isinstance(x, SparseDtype) else x for x in dtypes)
        # extract the categories' dtype
        non_cat_dtypes = [
            x.categories.dtype if isinstance(x, CategoricalDtype) else x
            for x in subtypes
        ]
        # TODO should categorical always give an answer?
        from pandas.core.dtypes.cast import find_common_type

        return find_common_type(non_cat_dtypes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._should_compare [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _should_compare(self, other: Index) -> bool:
        """
        Check if `self == other` can ever have non-False entries.
        """

        # NB: we use inferred_type rather than is_bool_dtype to catch
        #  object_dtype_of_bool and categorical[object_dtype_of_bool] cases
        if (
            other.inferred_type == "boolean" and is_any_real_numeric_dtype(self.dtype)
        ) or (
            self.inferred_type == "boolean" and is_any_real_numeric_dtype(other.dtype)
        ):
            # GH#16877 Treat boolean labels passed to a numeric index as not
            #  found. Without this fix False and True would be treated as 0 and 1
            #  respectively.
            return False

        dtype = _unpack_nested_dtype(other)
        return (
            self._is_comparable_dtype(dtype)
            or is_object_dtype(dtype)
            or is_string_dtype(dtype)
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/sphinxext/announce.py::get_pull_requests [/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/sphinxext/announce.py]
def get_pull_requests(repo, revision_range):
    prnums = []

    # From regular merges
    merges = this_repo.git.log("--oneline", "--merges", revision_range)
    issues = re.findall("Merge pull request \\#(\\d*)", merges)
    prnums.extend(int(s) for s in issues)

    # From Homu merges (Auto merges)
    issues = re.findall("Auto merge of \\#(\\d*)", merges)
    prnums.extend(int(s) for s in issues)

    # From fast forward squash-merges
    commits = this_repo.git.log(
        "--oneline", "--no-merges", "--first-parent", revision_range
    )
    issues = re.findall("^.*\\(\\#(\\d+)\\)$", commits, re.M)
    prnums.extend(int(s) for s in issues)

    # get PR data from GitHub repo
    prnums.sort()
    prs = [repo.get_pull(n) for n in prnums]
    return prs

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_for_grouping [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py]
def data_for_grouping():
    return Categorical(["a", "a", None, None, "b", "b", "a", "c"])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h::complexobject_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/vendored/klib/khash_python.h]
static inline int complexobject_cmp(PyComplexObject *a, PyComplexObject *b) {
  return (isnan(a->cval.real) && isnan(b->cval.real) && isnan(a->cval.imag) &&
          isnan(b->cval.imag)) ||
         (isnan(a->cval.real) && isnan(b->cval.real) &&
          a->cval.imag == b->cval.imag) ||
         (a->cval.real == b->cval.real && isnan(a->cval.imag) &&
          isnan(b->cval.imag)) ||
         (a->cval.real == b->cval.real && a->cval.imag == b->cval.imag);
}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h::_node_cmp [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_libs/include/pandas/skiplist.h]
static inline int _node_cmp(node_t *node, double value) {
  if (node->is_nil || node->value > value) {
    return -1;
  } else if (node->value < value) {
    return 1;
  } else {
    return 0;
  }
}
```
