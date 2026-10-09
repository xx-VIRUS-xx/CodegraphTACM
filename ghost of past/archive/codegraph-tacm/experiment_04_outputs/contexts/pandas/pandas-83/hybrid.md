# pandas-83 :: hybrid

query: BUG: concat not copying index and columns when copy=True (#31119)

## selected nodes

- rank=1 layer=FUNCTION tokens=899 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::concatenate_managers file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py
- rank=2 layer=FUNCTION tokens=432 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._wrap_applied_output_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=3 layer=FUNCTION tokens=487 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._concat_same_type file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py
- rank=4 layer=FUNCTION tokens=606 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py::Styler._copy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py
- rank=5 layer=FUNCTION tokens=490 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._reindex_and_concat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py
- rank=6 layer=FUNCTION tokens=570 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._concat_objects file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=7 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._concat file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=8 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_get_concat_axis_dataframe file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=9 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_concat_indexes file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py
- rank=10 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.res_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py::concatenate_managers [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/internals/concat.py]
def concatenate_managers(
    mgrs_indexers, axes: list[Index], concat_axis: AxisInt, copy: bool
) -> BlockManager:
    """
    Concatenate block managers into one.

    Parameters
    ----------
    mgrs_indexers : list of (BlockManager, {axis: indexer,...}) tuples
    axes : list of Index
    concat_axis : int
    copy : bool

    Returns
    -------
    BlockManager
    """

    needs_copy = copy and concat_axis == 0

    # Assertions disabled for performance
    # for tup in mgrs_indexers:
    #    # caller is responsible for ensuring this
    #    indexers = tup[1]
    #    assert concat_axis not in indexers

    if concat_axis == 0:
        mgrs = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers, needs_copy)
        return mgrs[0].concat_horizontal(mgrs, axes)

    if len(mgrs_indexers) > 0 and mgrs_indexers[0][0].nblocks > 0:
        first_dtype = mgrs_indexers[0][0].blocks[0].dtype
        if first_dtype in [np.float64, np.float32]:
            # TODO: support more dtypes here.  This will be simpler once
            #  JoinUnit.is_na behavior is deprecated.
            #  (update 2024-04-13 that deprecation has been enforced)
            if (
                all(_is_homogeneous_mgr(mgr, first_dtype) for mgr, _ in mgrs_indexers)
                and len(mgrs_indexers) > 1
            ):
                # Fastpath!
                # Length restriction is just to avoid having to worry about 'copy'
                shape = tuple(len(x) for x in axes)
                nb = _concat_homogeneous_fastpath(mgrs_indexers, shape, first_dtype)
                return BlockManager((nb,), axes)

    mgrs = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers, needs_copy)

    if len(mgrs) == 1:
        mgr = mgrs[0]
        out = mgr.copy(deep=False)
        out.axes = axes
        return out

    blocks = []
    values: ArrayLike

    for placement, join_units in _get_combined_plan(mgrs):
        unit = join_units[0]
        blk = unit.block

        if _is_uniform_join_units(join_units):
            vals = [ju.block.values for ju in join_units]

            if not blk.is_extension:
                # _is_uniform_join_units ensures a single dtype, so
                #  we can use np.concatenate, which is more performant
                #  than concat_compat
                # error: Argument 1 to "concatenate" has incompatible type
                # "List[Union[ndarray[Any, Any], ExtensionArray]]";
                # expected "Union[_SupportsArray[dtype[Any]],
                # _NestedSequence[_SupportsArray[dtype[Any]]]]"
                values = np.concatenate(vals, axis=1)  # type: ignore[arg-type]
            elif is_1d_only_ea_dtype(blk.dtype):
                # TODO(EA2D): special-casing not needed with 2D EAs
                values = concat_compat(vals, axis=0, ea_compat_axis=True)
                values = ensure_block_shape(values, ndim=2)
            else:
                values = concat_compat(vals, axis=1)

            values = ensure_wrapped_if_datetimelike(values)

            fastpath = blk.values.dtype == values.dtype
        else:
            values = _concatenate_join_units(join_units, copy=copy)
            fastpath = False

        if fastpath:
            b = blk.make_block_same_class(values, placement=placement)
        else:
            b = new_block_2d(values, placement=placement)

        blocks.append(b)

    return BlockManager(tuple(blocks), axes)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._wrap_applied_output_series [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
    def _wrap_applied_output_series(
        self,
        values: list[Series],
        not_indexed_same: bool,
        first_not_none,
        key_index: Index | None,
        is_transform: bool,
    ) -> DataFrame | Series:
        kwargs = first_not_none._construct_axes_dict()
        backup = Series(**kwargs)
        values = [x if (x is not None) else backup for x in values]

        all_indexed_same = all_indexes_same(x.index for x in values)

        if not all_indexed_same:
            # GH 8467
            return self._concat_objects(
                values,
                not_indexed_same=True,
                is_transform=is_transform,
            )

        # Combine values
        # vstack+constructor is faster than concat and handles MI-columns
        stacked_values = np.vstack([np.asarray(v) for v in values])

        index = key_index
        columns = first_not_none.index.copy()
        if columns.name is None:
            # GH6124 - propagate name of Series when it's consistent
            names = {v.name for v in values}
            if len(names) == 1:
                columns.name = next(iter(names))

        if stacked_values.dtype == object:
            # We'll have the DataFrame constructor do inference
            stacked_values = stacked_values.tolist()
        result = self.obj._constructor(stacked_values, index=index, columns=columns)

        if not self.as_index:
            result = self._insert_inaxis_grouper(result)

        return result.__finalize__(self.obj, method="groupby")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py::SparseArray._concat_same_type [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/sparse/array.py]
    def _concat_same_type(cls, to_concat: Sequence[Self]) -> Self:
        fill_value = to_concat[0].fill_value

        values = []
        length = 0

        if to_concat:
            sp_kind = to_concat[0].kind
        else:
            sp_kind = "integer"

        sp_index: SparseIndex
        if sp_kind == "integer":
            indices = []

            for arr in to_concat:
                int_idx = arr.sp_index.indices.copy()
                int_idx += length  # TODO: wraparound
                length += arr.sp_index.length

                values.append(arr.sp_values)
                indices.append(int_idx)

            data = np.concatenate(values)
            indices_arr = np.concatenate(indices)
            sp_index = IntIndex(length, indices_arr)

        else:
            # when concatenating block indices, we don't claim that you'll
            # get an identical index as concatenating the values and then
            # creating a new index. We don't want to spend the time trying
            # to merge blocks across arrays in `to_concat`, so the resulting
            # BlockIndex may have more blocks.
            blengths = []
            blocs = []

            for arr in to_concat:
                block_idx = arr.sp_index.to_block_index()

                values.append(arr.sp_values)
                blocs.append(block_idx.blocs.copy() + length)
                blengths.append(block_idx.blengths)
                length += arr.sp_index.length

            data = np.concatenate(values)
            blocs_arr = np.concatenate(blocs)
            blengths_arr = np.concatenate(blengths)

            sp_index = BlockIndex(length, blocs_arr, blengths_arr)

        return cls(data, sparse_index=sp_index, fill_value=fill_value)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py::Styler._copy [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/style.py]
    def _copy(self, deepcopy: bool = False) -> Styler:
        """
        Copies a Styler, allowing for deepcopy or shallow copy

        Copying a Styler aims to recreate a new Styler object which contains the same
        data and styles as the original.

        Data dependent attributes [copied and NOT exported]:
          - formatting (._display_funcs)
          - hidden index values or column values (.hidden_rows, .hidden_columns)
          - tooltips
          - cell_context (cell css classes)
          - ctx (cell css styles)
          - caption
          - concatenated stylers

        Non-data dependent attributes [copied and exported]:
          - css
          - hidden index state and hidden columns state (.hide_index_, .hide_columns_)
          - table_attributes
          - table_styles
          - applied styles (_todo)

        """
        # GH 40675, 52728
        styler = type(self)(
            self.data,  # populates attributes 'data', 'columns', 'index' as shallow
        )
        shallow = [  # simple string or boolean immutables
            "hide_index_",
            "hide_columns_",
            "hide_column_names",
            "hide_index_names",
            "table_attributes",
            "cell_ids",
            "caption",
            "uuid",
            "uuid_len",
            "template_latex",  # also copy templates if these have been customised
            "template_html_style",
            "template_html_table",
            "template_html",
        ]
        deep = [  # nested lists or dicts
            "css",
            "concatenated",
            "_display_funcs",
            "_display_funcs_index",
            "_display_funcs_columns",
            "_display_funcs_index_names",
            "_display_funcs_column_names",
            "hidden_rows",
            "hidden_columns",
            "ctx",
            "ctx_index",
            "ctx_columns",
            "cell_context",
            "_todo",
            "table_styles",
            "tooltips",
        ]

        for attr in shallow:
            setattr(styler, attr, getattr(self, attr))

        for attr in deep:
            val = getattr(self, attr)
            setattr(styler, attr, copy.deepcopy(val) if deepcopy else val)

        return styler

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py::_MergeOperation._reindex_and_concat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/merge.py]
    def _reindex_and_concat(
        self,
        join_index: Index,
        left_indexer: npt.NDArray[np.intp] | None,
        right_indexer: npt.NDArray[np.intp] | None,
    ) -> DataFrame:
        """
        reindex along index and concat along columns.
        """
        # Take views so we do not alter the originals
        left = self.left[:]
        right = self.right[:]

        llabels, rlabels = _items_overlap_with_suffix(
            self.left._info_axis, self.right._info_axis, self.suffixes
        )

        if left_indexer is not None and not is_range_indexer(left_indexer, len(left)):
            # Pinning the index here (and in the right code just below) is not
            #  necessary, but makes the `.take` more performant if we have e.g.
            #  a MultiIndex for left.index.
            lmgr = left._mgr.reindex_indexer(
                join_index,
                left_indexer,
                axis=1,
                only_slice=True,
                allow_dups=True,
                use_na_proxy=True,
            )
            left = left._constructor_from_mgr(lmgr, axes=lmgr.axes)
        left.index = join_index

        if right_indexer is not None and not is_range_indexer(
            right_indexer, len(right)
        ):
            rmgr = right._mgr.reindex_indexer(
                join_index,
                right_indexer,
                axis=1,
                only_slice=True,
                allow_dups=True,
                use_na_proxy=True,
            )
            right = right._constructor_from_mgr(rmgr, axes=rmgr.axes)
        right.index = join_index

        from pandas import concat

        left.columns = llabels
        right.columns = rlabels
        result = concat([left, right], axis=1)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy._concat_objects [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py]
    def _concat_objects(
        self,
        values,
        not_indexed_same: bool = False,
        is_transform: bool = False,
    ):
        from pandas.core.reshape.concat import concat

        if self.group_keys and not is_transform:
            if self.as_index:
                # possible MI return case
                group_keys = self._grouper.result_index
                group_levels = self._grouper.levels
                group_names = self._grouper.names

                result = concat(
                    values,
                    axis=0,
                    keys=group_keys,
                    levels=group_levels,
                    names=group_names,
                    sort=False,
                )
            else:
                result = concat(values, axis=0)

        elif not not_indexed_same:
            result = concat(values, axis=0)

            ax = self._selected_obj.index
            if self.dropna:
                labels = self._grouper.ids
                mask = labels != -1
                ax = ax[mask]

            # this is a very unfortunate situation
            # we can't use reindex to restore the original order
            # when the ax has duplicates
            # so we resort to this
            # GH 14776, 30667
            # TODO: can we reuse e.g. _reindex_non_unique?
            if ax.has_duplicates and not result.axes[0].equals(ax):
                # e.g. test_category_order_transformer
                target = algorithms.unique1d(ax._values)
                indexer, _ = result.index.get_indexer_non_unique(target)
                result = result.take(indexer, axis=0)
            else:
                result = result.reindex(ax, axis=0)

        else:
            result = concat(values, axis=0)

        if self.obj.ndim == 1:
            name = self.obj.name
        elif is_hashable(self._selection):
            name = self._selection
        else:
            name = None

        if isinstance(result, Series) and name is not None:
            result.name = name

        return result.__finalize__(self.obj, method="groupby")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::Index._concat [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
    def _concat(self, to_concat: list[Index], name: Hashable) -> Index:
        """
        Concatenate multiple Index objects.
        """
        to_concat_vals = [x._values for x in to_concat]

        result = concat_compat(to_concat_vals)

        return Index._with_infer(result, name=name, copy=False)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_get_concat_axis_dataframe [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py]
def _get_concat_axis_dataframe(
    objs: list[Series | DataFrame],
    axis: AxisInt,
    ignore_index: bool,
    keys: Iterable[Hashable] | None,
    names: list[HashableT] | None,
    levels,
    verify_integrity: bool,
) -> Index:
    """Return result concat axis when concatenating DataFrame objects."""
    indexes_gen = (x.axes[axis] for x in objs)

    if ignore_index:
        return default_index(sum(len(i) for i in indexes_gen))
    else:
        indexes = list(indexes_gen)

    if keys is None:
        if levels is not None:
            raise ValueError("levels supported only when keys is not None")
        concat_axis = _concat_indexes(indexes)
    else:
        concat_axis = _make_concat_multiindex(indexes, keys, levels, names)

    if verify_integrity and not concat_axis.is_unique:
        overlap = concat_axis[concat_axis.duplicated()].unique()
        raise ValueError(f"Indexes have overlapping values: {overlap}")

    return concat_axis

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py::_concat_indexes [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/reshape/concat.py]
def _concat_indexes(indexes) -> Index:
    return indexes[0].append(indexes[1:])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.res_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def res_columns(self) -> Index:
        return self.result_columns
```
