# pandas-70 :: codesearch

query: BUG: regression when applying groupby aggregation on categorical columns (#31359)

## selected nodes

- rank=1 layer=FUNCTION tokens=278 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._apply_to_column_groupbys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py
- rank=2 layer=FUNCTION tokens=465 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py::_grouped_plot_by_column file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py
- rank=3 layer=FUNCTION tokens=189 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/numba_.py::group_agg file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/numba_.py
- rank=4 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_for_grouping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py
- rank=5 layer=FUNCTION tokens=477 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._groupby_and_aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py
- rank=6 layer=FUNCTION tokens=367 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py::assert_categorical_single_grouper file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/groupby/methods/test_value_counts.py
- rank=7 layer=FUNCTION tokens=506 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py::_grouped_hist file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py
- rank=8 layer=FUNCTION tokens=197 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/numba_.py::group_transform file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/numba_.py
- rank=9 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/conftest.py::data_for_grouping file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/conftest.py
- rank=10 layer=FUNCTION tokens=349 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py::_grouped_plot file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py
- rank=11 layer=FUNCTION tokens=927 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py::boxplot_frame_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py
- rank=12 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.result_columns file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._apply_to_column_groupbys [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py::_grouped_plot_by_column [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py]
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
):
    grouped = data.groupby(by, observed=False)
    if columns is None:
        if not isinstance(by, (list, tuple)):
            by = [by]
        columns = data._get_numeric_data().columns.difference(by)
    naxes = len(columns)
    fig, axes = create_subplots(
        naxes=naxes,
        sharex=kwargs.pop("sharex", True),
        sharey=kwargs.pop("sharey", True),
        figsize=figsize,
        ax=ax,
        layout=layout,
    )

    # GH 45465: move the "by" label based on "vert"
    xlabel, ylabel = kwargs.pop("xlabel", None), kwargs.pop("ylabel", None)
    if kwargs.get("vert", True):
        xlabel = xlabel or by
    else:
        ylabel = ylabel or by

    ax_values = []

    for ax, col in zip(flatten_axes(axes), columns, strict=False):
        gp_col = grouped[col]
        keys, values = zip(*gp_col, strict=True)
        re_plotf = plotf(keys, values, ax, xlabel=xlabel, ylabel=ylabel, **kwargs)
        ax.set_title(col)
        ax_values.append(re_plotf)
        ax.grid(grid)

    result = pd.Series(ax_values, index=columns, copy=False)

    # Return axes in multiplot case, maybe revisit later # 985
    if return_type is None:
        result = axes

    byline = by[0] if len(by) == 1 else by  # pyright: ignore[reportOptionalSubscript]
    fig.suptitle(f"Boxplot grouped by {byline}")
    maybe_adjust_figure(fig, bottom=0.15, top=0.9, left=0.1, right=0.9, wspace=0.2)

    return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/numba_.py::group_agg [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/numba_.py]
    def group_agg(
        values: np.ndarray,
        index: np.ndarray,
        begin: np.ndarray,
        end: np.ndarray,
        num_columns: int,
        *args: Any,
    ) -> np.ndarray:
        assert len(begin) == len(end)
        num_groups = len(begin)

        result = np.empty((num_groups, num_columns))
        for i in numba.prange(num_groups):
            group_index = index[begin[i] : end[i]]
            for j in numba.prange(num_columns):
                group = values[begin[i] : end[i], j]
                result[i, j] = numba_func(group, group_index, *args)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py::data_for_grouping [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/test_categorical.py]
def data_for_grouping():
    return Categorical(["a", "a", None, None, "b", "b", "a", "c"])

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py::Resampler._groupby_and_aggregate [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/resample.py]
    def _groupby_and_aggregate(self, how, *args, **kwargs):
        """
        Re-evaluate the obj with a groupby aggregation.
        """
        grouper = self._grouper

        # Excludes `on` column when provided
        obj = self._obj_with_exclusions

        grouped = get_groupby(obj, by=None, grouper=grouper, group_keys=self.group_keys)

        try:
            if callable(how):
                # TODO: test_resample_apply_with_additional_args fails if we go
                #  through the non-lambda path, not clear that it should.
                func = lambda x: how(x, *args, **kwargs)
                result = grouped.aggregate(func)
            else:
                result = grouped.aggregate(how, *args, **kwargs)
        except (AttributeError, KeyError):
            # we have a non-reducing function; try to evaluate
            # alternatively we want to evaluate only a column of the input

            # test_apply_to_one_column_of_df the function being applied references
            #  a DataFrame column, but aggregate_item_by_item operates column-wise
            #  on Series, raising AttributeError or KeyError
            #  (depending on whether the column lookup uses getattr/__getitem__)
            result = grouped.apply(how, *args, **kwargs)

        except ValueError as err:
            if "Must produce aggregated value" in str(err):
                # raised in _aggregate_named
                # see test_apply_without_aggregation, test_apply_with_mutated_index
                pass
            else:
                raise

            # we have a non-reducing function
            # try to evaluate
            result = grouped.apply(how, *args, **kwargs)

        return self._wrap_result(result)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py::_grouped_hist [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py]
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
    xlabelsize: int | None = None,
    xrot=None,
    ylabelsize: int | None = None,
    yrot=None,
    legend: bool = False,
    **kwargs,
):
    """
    Grouped histogram

    Parameters
    ----------
    data : Series/DataFrame
    column : object, optional
    by : object, optional
    ax : axes, optional
    bins : int, default 50
    figsize : tuple, optional
    layout : optional
    sharex : bool, default False
    sharey : bool, default False
    rot : float, default 90
    grid : bool, default True
    legend: : bool, default False
    kwargs : dict, keyword arguments passed to matplotlib.Axes.hist

    Returns
    -------
    collection of Matplotlib Axes
    """
    if legend:
        assert "label" not in kwargs
        if data.ndim == 1:
            kwargs["label"] = data.name
        elif column is None:
            kwargs["label"] = data.columns
        else:
            kwargs["label"] = column

    def plot_group(group, ax) -> None:
        ax.hist(group.dropna().values, bins=bins, **kwargs)
        if legend:
            ax.legend()

    if xrot is None:
        xrot = rot

    fig, axes = _grouped_plot(
        plot_group,
        data,
        column=column,
        by=by,
        sharex=sharex,
        sharey=sharey,
        ax=ax,
        figsize=figsize,
        layout=layout,
        rot=rot,
    )

    set_ticks_props(
        axes, xlabelsize=xlabelsize, xrot=xrot, ylabelsize=ylabelsize, yrot=yrot
    )

    maybe_adjust_figure(
        fig, bottom=0.15, top=0.9, left=0.1, right=0.9, hspace=0.5, wspace=0.3
    )
    return axes

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/numba_.py::group_transform [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/numba_.py]
    def group_transform(
        values: np.ndarray,
        index: np.ndarray,
        begin: np.ndarray,
        end: np.ndarray,
        num_columns: int,
        *args: Any,
    ) -> np.ndarray:
        assert len(begin) == len(end)
        num_groups = len(begin)

        result = np.empty((len(values), num_columns))
        for i in numba.prange(num_groups):
            group_index = index[begin[i] : end[i]]
            for j in numba.prange(num_columns):
                group = values[begin[i] : end[i], j]
                result[begin[i] : end[i], j] = numba_func(group, group_index, *args)
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/conftest.py::data_for_grouping [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/extension/conftest.py]
def data_for_grouping():
    """
    Data for factorization, grouping, and unique tests.

    Expected to be like [B, B, NA, NA, A, A, B, C]

    Where A < B < C and NA is missing.

    If a dtype has _is_boolean = True, i.e. only 2 unique non-NA entries,
    then set C=B.
    """
    raise NotImplementedError

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py::_grouped_plot [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/hist.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py::boxplot_frame_groupby [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py]
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
    backend=None,
    **kwargs,
):
    """
    Make box plots from DataFrameGroupBy data.

    Creates one or more box-and-whisker plots based on data that has been
    grouped using :meth:`DataFrame.groupby`. Each group can be rendered as
    a separate subplot or combined into a single figure.

    Parameters
    ----------
    grouped : DataFrameGroupBy
        The grouped DataFrame object over which to create the box plots.
    subplots : bool
        * ``False`` - no subplots will be used
        * ``True`` - create a subplot for each group.
    column : column name or list of names, or vector
        Can be any valid input to groupby.
    fontsize : float or str
        Font size for the labels.
    rot : float
        Rotation angle of labels (in degrees) on the x-axis.
    grid : bool
        Whether to show grid lines on the plot.
    ax : Matplotlib axis object, default None
        The axes on which to draw the plots. If None, uses the current axes.
    figsize : tuple of (float, float)
        The figure size in inches (width, height).
    layout : tuple (optional)
        The layout of the plot: (rows, columns).
    sharex : bool, default False
        Whether x-axes will be shared among subplots.
    sharey : bool, default True
        Whether y-axes will be shared among subplots.
    backend : str, default None
        Backend to use instead of the backend specified in the option
        ``plotting.backend``. For instance, 'matplotlib'. Alternatively, to
        specify the ``plotting.backend`` for the whole session, set
        ``pd.options.plotting.backend``.
    **kwargs
        All other plotting keyword arguments to be passed to
        matplotlib's boxplot function.

    Returns
    -------
    dict or DataFrame.boxplot return value
        If ``subplots=True``, returns a dictionary of group keys to the boxplot
        return values. If ``subplots=False``, returns the boxplot return value
        of a single DataFrame.

    See Also
    --------
    DataFrame.boxplot : Create a box plot from a DataFrame.
    Series.plot : Plot a Series.

    Examples
    --------
    You can create boxplots for grouped data and show them as separate subplots:

    .. plot::
        :context: close-figs

        >>> import itertools
        >>> tuples = [t for t in itertools.product(range(1000), range(4))]
        >>> index = pd.MultiIndex.from_tuples(tuples, names=["lvl0", "lvl1"])
        >>> data = np.random.randn(len(index), 4)
        >>> df = pd.DataFrame(data, columns=list("ABCD"), index=index)
        >>> grouped = df.groupby(level="lvl1")
        >>> grouped.boxplot(rot=45, fontsize=12, figsize=(8, 10))  # doctest: +SKIP

    The ``subplots=False`` option shows the boxplots in a single figure.

    .. plot::
        :context: close-figs

        >>> grouped.boxplot(subplots=False, rot=45, fontsize=12)  # doctest: +SKIP
    """
    plot_backend = _get_plot_backend(backend)
    return plot_backend.boxplot_frame_groupby(
        grouped,
        subplots=subplots,
        column=column,
        fontsize=fontsize,
        rot=rot,
        grid=grid,
        ax=ax,
        figsize=figsize,
        layout=layout,
        sharex=sharex,
        sharey=sharey,
        **kwargs,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py::FrameApply.result_columns [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/apply.py]
    def result_columns(self) -> Index:
        pass
```
