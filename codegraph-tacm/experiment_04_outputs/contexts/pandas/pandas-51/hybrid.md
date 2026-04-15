# pandas-51 :: hybrid

query: BUG: fix in categorical merges (#32079)

## selected nodes

- rank=1 layer=FUNCTION tokens=1647 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::union_categoricals file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py
- rank=2 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py::TestMergeCategorical.tests_merge_categorical_unordered_equal file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/reshape/merge/test_merge.py
- rank=3 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py::_maybe_unwrap file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/concat.py
- rank=4 layer=FUNCTION tokens=448 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._is_dtype_compat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py
- rank=5 layer=FUNCTION tokens=209 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical._encode_with_my_categories file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=6 layer=FUNCTION tokens=703 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py::recode_for_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py
- rank=7 layer=FUNCTION tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py::non_coercible_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py
- rank=8 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Constructor.time_existing_categorical file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py
- rank=9 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py::Categorical._categories_match_up_to_permutation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/categorical.py
- rank=10 layer=FUNCTION tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/sphinxext/announce.py::get_pull_requests file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/doc/sphinxext/announce.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py::CategoricalIndex._is_dtype_compat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/category.py]
    def _is_dtype_compat(self, other: Index) -> Categorical:
        """
        *this is an internal non-public method*

        provide a comparison between the dtype of self and other (coercing if
        needed)

        Parameters
        ----------
        other : Index

        Returns
        -------
        Categorical

        Raises
        ------
        TypeError if the dtypes are not compatible
        """
        if isinstance(other.dtype, CategoricalDtype):
            cat = extract_array(other)
            cat = cast("Categorical", cat)
            if not cat._categories_match_up_to_permutation(self._values):
                raise TypeError(
                    "categories must match existing categories when appending"
                )

        elif other._is_multi:
            # preempt raising NotImplementedError in isna call
            raise TypeError("MultiIndex is not dtype-compatible with CategoricalIndex")
        else:
            values = other

            codes = self.categories.get_indexer(values)
            if ((codes == -1) & ~values.isna()).any():
                # GH#37667 see test_equals_non_category
                raise TypeError(
                    "categories must match existing categories when appending"
                )
            cat = Categorical(other, dtype=self.dtype)
            other = CategoricalIndex(cat)
            if not other.isin(values).all():
                raise TypeError(
                    "cannot append a non-category item to a CategoricalIndex"
                )
            cat = other._values

        return cat

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py::recode_for_groupby [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/categorical.py]
def recode_for_groupby(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if sort:
        unique_notnan_codes = np.sort(unique_notnan_codes)
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py::non_coercible_categorical [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arrays/categorical/test_indexing.py]
def non_coercible_categorical(monkeypatch):
    """
    Monkeypatch Categorical.__array__ to ensure no implicit conversion.

    Raises
    ------
    ValueError
        When Categorical.__array__ is called.
    """

    # TODO(Categorical): identify other places where this may be
    # useful and move to a conftest.py
    def array(self, dtype=None):
        raise ValueError("I cannot be converted.")

    with monkeypatch.context() as m:
        m.setattr(Categorical, "__array__", array)
        yield

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py::Constructor.time_existing_categorical [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/categoricals.py]
    def time_existing_categorical(self):
        pd.Categorical(self.categorical)

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
```
