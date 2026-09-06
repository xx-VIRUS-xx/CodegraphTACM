# pandas-5 :: tacm

query: BUG: DataFrameGroupby std/sem modify grouped column when as_index=False (#33630)

## selected nodes

- rank=1 layer=FILE tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py
- rank=2 layer=FILE tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=3 layer=FILE tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/kernels/sum_.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/_numba/kernels/sum_.py
- rank=4 layer=FILE tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py
- rank=5 layer=CLASS tokens=301 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/plotting/test_boxplot_method.py::TestDataFrameGroupByPlots file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/plotting/test_boxplot_method.py
- rank=6 layer=CLASS tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=7 layer=CLASS tokens=219 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/plotting/test_hist_method.py::TestDataFrameGroupByPlots file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/plotting/test_hist_method.py
- rank=8 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=9 layer=CLASS tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py
- rank=10 layer=CLASS tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas7bdat.py::_Column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas7bdat.py
- rank=11 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py
- rank=12 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=13 layer=FUNCTION tokens=305 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py::_grouped_plot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py
- rank=14 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.hist file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=15 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py::_grouped_hist file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py
- rank=16 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=17 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py::_grouped_plot_by_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py
- rank=18 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py::boxplot_frame_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py
- rank=19 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::TestDataFrameAnalytics.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py
- rank=20 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py::boxplot_frame_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py
- rank=21 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._wrap_applied_output file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=22 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding.std file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py
- rank=23 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._apply_to_column_groupbys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=24 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.idxmax file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=25 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.idxmin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=26 layer=FUNCTION tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.kurt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=27 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.corrwith file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=28 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=29 layer=FUNCTION tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=30 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.value_counts file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=31 layer=FUNCTION tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.cov file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=32 layer=FUNCTION tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py::slice_test_grouped file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/conftest.py
- rank=33 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.corr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=34 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=35 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.take file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=36 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._python_agg_general file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=37 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.nunique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=38 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._wrap_applied_output_series file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=39 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.filter file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=40 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.__getitem__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=41 layer=FUNCTION tokens=118 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy.transform file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=42 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas7bdat.py::_Column.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas7bdat.py
- rank=43 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=44 layer=FUNCTION tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=45 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._get_data_to_aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=46 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::TestDataFrameAnalytics.std file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py

## context

```text
file plotting/_matplotlib/boxplot.py
imports: __future__, typing, warnings, matplotlib, numpy, pandas, collections
defines: BoxPlot, BP, _set_ticklabels, maybe_color_bp, _grouped_plot_by_column, boxplot, _get_colors, plot_group, boxplot_frame, boxplot_frame_groupby

file core/groupby/generic.py
imports: __future__, collections, dataclasses, functools, typing, warnings, numpy, pandas
defines: NamedAgg, SeriesGroupBy, DataFrameGroupBy, _wrap_transform_general_frame

file _numba/kernels/sum_.py
imports: __future__, typing, numba, numpy, pandas
defines: add_sum, remove_sum, sliding_sum, grouped_kahan_sum, grouped_sum

file plotting/_matplotlib/hist.py
imports: __future__, typing, numpy, pandas, matplotlib
defines: HistPlot, KdePlot, _grouped_plot, _grouped_hist, plot_group, hist_series, hist_frame

class TestDataFrameGroupByPlots:  [tests/plotting/test_boxplot_method.py:412]
methods: test_boxplot_legacy1, test_boxplot_legacy1_return_type
         test_boxplot_legacy2
         test_boxplot_legacy2_return_type
         test_boxplot_multi_groupby_groups
         test_boxplot_multiindex_column, test_fontsize
         test_groupby_boxplot_object
         test_groupby_boxplot_subplots_false
         test_grouped_box_layout_axes_shape_cols_groupby
         test_grouped_box_layout_axes_shape_rows
         test_grouped_box_layout_needs_by
         test_grouped_box_layout_positive_layout
         test_grouped_box_layout_positive_layout_axes
         test_grouped_box_layout_shape
         test_grouped_box_layout_too_small
         test_grouped_box_layout_visible
         test_grouped_box_layout_works
         test_grouped_box_multiple_axes
         test_grouped_box_multiple_axes_ax_error
         test_grouped_box_multiple_axes_on_fig
         test_grouped_box_return_type
         test_grouped_box_return_type_arg
         test_grouped_box_return_type_arg_duplcate_cats
         test_grouped_box_return_type_groupby
         test_grouped_plot_fignums
         test_grouped_plot_fignums_excluded_col

class DataFrameGroupBy(GroupBy[DataFrame]):  [core/groupby/generic.py:2138]
methods: _apply_to_column_groupbys, _choose_path, _cython_transform
         _define_paths, _get_data_to_aggregate, _gotitem
         _python_agg_general, _transform_general
         _wrap_agged_manager, _wrap_applied_output
         _wrap_applied_output_series, aggregate, alt
         arr_func, corr, corrwith, cov, filter, hist
         idxmax, idxmin, kurt, nunique, plot, skew, take
         transform, value_counts, __getitem__

class TestDataFrameGroupByPlots:  [tests/plotting/test_hist_method.py:646]
methods: test_axis_share_x, test_axis_share_xy, test_axis_share_y
         test_grouped_hist_layout_axes
         test_grouped_hist_layout_by_warning
         test_grouped_hist_layout_error
         test_grouped_hist_layout_figsize
         test_grouped_hist_layout_warning
         test_grouped_hist_legacy
         test_grouped_hist_legacy2
         test_grouped_hist_legacy_axes_shape_no_col
         test_grouped_hist_legacy_external_err
         test_grouped_hist_legacy_figsize_err
         test_grouped_hist_legacy_grouped_hist
         test_grouped_hist_legacy_grouped_hist_kwargs
         test_grouped_hist_legacy_single_key
         test_grouped_hist_multiple_axes
         test_grouped_hist_multiple_axes_error
         test_grouped_hist_multiple_axes_no_cols
         test_histtype_argument

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class Expanding(RollingAndExpandingMixin):  [core/window/expanding.py:43]
methods: _get_window_indexer, aggregate, apply, corr, count, cov
         first, kurt, last, max, mean, median, min
         nunique, pipe, pipe, pipe, quantile, rank, sem
         skew, std, sum, var, __init__

class _Column:  [io/sas/sas7bdat.py:121]
methods: __init__

    def sem(self, ddof: int = 1, numeric_only: bool = False):
        """
        Calculate the expanding standard error of mean.

        The standard error is computed as ``std / sqrt(N)`` over all data
        points seen so far, where ``N`` is the number of observations.

        Parameters
        ----------
        ddof : int, default 1
            Delta Degrees of Freedom.  The divisor used in calculations
            is ``N - ddof``, where ``N`` represents the number of elements.
    # ... truncated

    def sem(self, ddof: int = 1, numeric_only: bool = False):
        # Raise here so error message says sem instead of std
        self._validate_numeric_only("sem", numeric_only)
        return self.std(numeric_only=numeric_only, ddof=ddof) / (
            self.count(numeric_only=numeric_only)
        ).pow(0.5)

def _grouped_plot(
    plotf,
    data: Series | DataFrame,
    column=None,
    by=None,
    numeric_only: bool = True,
    figsize: tuple[float, float] | None = None,
    sharex: bool = True,
    sharey: bool = True,
    layout=None,
    rot: float = 0,
    ax=None,
    **kwargs,
):
    # error: Non-overlapping equality check (left operand type: "Optional[Tuple[float,
    # float]]", right operand type: "Literal['default']")
    if figsize == "default":  # type: ignore[comparison-overlap]
        # allowed to specify mpl default with 'default'
        raise ValueError(
            "figsize='default' is no longer supported. "
            "Specify figure size by tuple instead"
        )

    grouped = data.groupby(by)
    if column is not None:
        grouped = grouped[column]

    naxes = len(grouped)
    fig, axes = create_subplots(
        naxes=naxes, figsize=figsize, sharex=sharex, sharey=sharey, ax=ax, layout=layout
    )

    for ax, (key, group) in zip(flatten_axes(axes), grouped, strict=False):
        if numeric_only and isinstance(group, ABCDataFrame):
            group = group._get_numeric_data()
        plotf(group, ax, **kwargs)
        ax.set_title(pprint_thing(key))

    return fig, axes

    def hist(
        self,
        column: IndexLabel | None = None,
        by=None,
        grid: bool = True,
        xlabelsize: int | None = None,
        xrot: float | None = None,
        ylabelsize: int | None = None,
        yrot: float | None = None,
        ax=None,
        sharex: bool = False,
        sharey: bool = False,
    # ... truncated

def _grouped_hist(
    data: Series | DataFrame,
    column=None,
    by=None,
    ax=None,
    bins: int = 50,
    figsize: tuple[float, float] | None = None,
    layout=None,
    sharex: bool = False,
    sharey: bool = False,
    rot: float = 90,
    grid: bool = True,
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

def _grouped_plot_by_column(
    plotf,
    data,
    columns=None,
    by=None,
    numeric_only: bool = True,
    grid: bool = False,
    figsize: tuple[float, float] | None = None,
    ax=None,
    layout=None,
    return_type=None,
    **kwargs,
    # ... truncated

def boxplot_frame_groupby(
    grouped,
    subplots: bool = True,
    column=None,
    fontsize: int | None = None,
    rot: int = 0,
    grid: bool = True,
    ax=None,
    figsize: tuple[float, float] | None = None,
    layout=None,
    sharex: bool = False,
    sharey: bool = True,
    # ... truncated

        def sem(x):
            return np.std(x, ddof=1) / np.sqrt(len(x))

def boxplot_frame_groupby(
    grouped: DataFrameGroupBy,
    subplots: bool = True,
    column=None,
    fontsize: int | None = None,
    rot: int = 0,
    grid: bool = True,
    ax=None,
    figsize: tuple[float, float] | None = None,
    layout=None,
    sharex: bool = False,
    sharey: bool = True,
    # ... truncated

    def _wrap_applied_output(
        self,
        data: DataFrame,
        values: list,
        not_indexed_same: bool = False,
        is_transform: bool = False,
    ):
        if len(values) == 0:
            if is_transform:
                # GH#47787 see test_group_on_empty_multiindex
                res_index = data.index
            elif not self.group_keys:
    # ... truncated

    def std(
        self,
        ddof: int = 1,
        numeric_only: bool = False,
        engine: Literal["cython", "numba"] | None = None,
        engine_kwargs: dict[str, bool] | None = None,
    ):
        """
    # ... truncated

    def _apply_to_column_groupbys(self, func) -> DataFrame:
        from pandas.core.reshape.concat import concat

        obj = self._obj_with_exclusions
        columns = obj.columns
        sgbs = (
            SeriesGroupBy(
                obj.iloc[:, i],
                selection=colname,
                grouper=self._grouper,
                exclusions=self.exclusions,
                observed=self.observed,
            )
            for i, colname in enumerate(obj.columns)
        )
        results = [func(sgb) for sgb in sgbs]

        if not results:
            # concat would raise
            res_df = DataFrame([], columns=columns, index=self._grouper.result_index)
        else:
            res_df = concat(results, keys=columns, axis=1)

        if not self.as_index:
            res_df.index = default_index(len(res_df))
            res_df = self._insert_inaxis_grouper(res_df)
        return res_df

    def idxmax(
        self,
        skipna: bool = True,
        numeric_only: bool = False,
    ) -> DataFrame:
        """
    # ... truncated

    def idxmin(
        self,
        skipna: bool = True,
        numeric_only: bool = False,
    ) -> DataFrame:
        """
    # ... truncated

    def kurt(
        self,
        skipna: bool = True,
        numeric_only: bool = False,
        **kwargs,
    ) -> DataFrame:
        """
    # ... truncated

    def corrwith(
        self,
        other: DataFrame | Series,
        drop: bool = False,
        method: CorrelationMethod = "pearson",
        numeric_only: bool = False,
    ) -> DataFrame:
        """
    # ... truncated

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

    def skew(
        self,
        skipna: bool = True,
        numeric_only: bool = False,
        **kwargs,
    ) -> DataFrame:
        """
    # ... truncated

    def value_counts(
        self,
        subset: Sequence[Hashable] | None = None,
        normalize: bool = False,
        sort: bool = True,
        ascending: bool = False,
        dropna: bool = True,
    ) -> DataFrame | Series:
        """
    # ... truncated

    def cov(
        self,
        min_periods: int | None = None,
        ddof: int | None = 1,
        numeric_only: bool = False,
    ) -> DataFrame:
        """
    # ... truncated

def slice_test_grouped(slice_test_df):
    return slice_test_df.groupby("Group", as_index=False)

    def corr(
        self,
        method: str | Callable[[np.ndarray, np.ndarray], float] = "pearson",
        min_periods: int = 1,
        numeric_only: bool = False,
    ) -> DataFrame:
        """
    # ... truncated

    def aggregate(
        self, func=None, *args, engine=None, engine_kwargs=None, **kwargs
    ) -> DataFrame:
        """
    # ... truncated

    def take(
        self,
        indices: TakeIndexer,
        **kwargs,
    ) -> DataFrame:
        """
    # ... truncated

    def _python_agg_general(self, func, *args, **kwargs):
        f = lambda x: func(x, *args, **kwargs)

        obj = self._obj_with_exclusions

        if self.ngroups == 0 or len(obj.columns) == 0:
            res_index = self._grouper.result_index
            res = self.obj._constructor(index=res_index, columns=obj.columns).astype(
                obj.dtypes
            )
        else:
            output: dict[int, ArrayLike] = {
                idx: self._grouper.agg_series(ser, f)
                for idx, (name, ser) in enumerate(obj.items())
            }
            res = self.obj._constructor(output)
            res.columns = obj.columns.copy(deep=False)
        return self._wrap_aggregated_output(res)

    def nunique(self, dropna: bool = True) -> DataFrame:
        """
        Return DataFrame with counts of unique elements in each position.

        This method counts the number of distinct values for each column
        within each group, optionally excluding NaN values.

        Parameters
        ----------
        dropna : bool, default True
            Don't include NaN in the counts.

    # ... truncated

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

    # ... truncated

    def filter(self, func, dropna: bool = True, *args, **kwargs) -> DataFrame:
        """
        Filter elements from groups that don't satisfy a criterion.

        Elements from groups are filtered if they do not satisfy the
        boolean criterion specified by func.

        Parameters
        ----------
        func : function
            Criterion to apply to each group. Should return True or False.
        dropna : bool
    # ... truncated

    def __getitem__(self, key):
        check_dict_or_set_indexers(key)
        key = lib.item_from_zerodim(key)
        key = com.apply_if_callable(key, self)

        if is_hashable(key, allow_slice=False) and not is_iterator(key):
            # is_iterator to exclude generator e.g. test_getitem_listlike
            # As of Python 3.12, slice is hashable which breaks MultiIndex (GH#57500)

            # Shortcut: return single column as Series when key refers to one column.
            # Previously we used "key in self.columns.drop_duplicates(keep=False)",
            # which built a new Index on every access when columns had duplicates.
    # ... truncated

    def transform(self, func, *args, engine=None, engine_kwargs=None, **kwargs):
        """
        Call function producing a same-indexed DataFrame on each group.

        Returns a DataFrame having the same indexes as the original object
        filled with the transformed values.

        Parameters
        ----------
        func : function, str
            Function to apply to each group.
            See the Notes section below for requirements.
    # ... truncated

    def __init__(
        self,
        col_id: int,
        # These can be bytes when convert_header_text is False
        name: str | bytes,
        label: str | bytes,
        format: str | bytes,
        ctype: bytes,
        length: int,
    ) -> None:
        self.col_id = col_id
        self.name = name
        self.label = label
        self.format = format
        self.ctype = ctype
        self.length = length

    def sem(
        self, ddof: int = 1, numeric_only: bool = False, skipna: bool = True
    ) -> NDFrameT:
        """
    # ... truncated

    def sem(
        self,
        ddof: int = 1,
        numeric_only: bool = False,
    ):
        """
    # ... truncated

    def _get_data_to_aggregate(
        self, *, numeric_only: bool = False, name: str | None = None
    ) -> BlockManager:
        obj = self._obj_with_exclusions
        mgr = obj._mgr
        if numeric_only:
            mgr = mgr.get_numeric_data()
        return mgr

        def std(x):
            return np.std(x, ddof=1)
```
