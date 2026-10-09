# pandas-5 :: hybrid-cs

query: BUG: DataFrameGroupby std/sem modify grouped column when as_index=False (#33630)

## selected nodes

- rank=1 layer=FUNCTION tokens=927 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py::boxplot_frame_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_core.py
- rank=2 layer=FUNCTION tokens=511 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py::boxplot_frame_groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py
- rank=3 layer=FUNCTION tokens=2277 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.groupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=4 layer=FUNCTION tokens=278 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py::DataFrameGroupBy._apply_to_column_groupbys file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/generic.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py::boxplot_frame_groupby [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/boxplot.py]
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
    **kwds,
):
    if subplots is True:
        naxes = len(grouped)
        fig, axes = create_subplots(
            naxes=naxes,
            squeeze=False,
            ax=ax,
            sharex=sharex,
            sharey=sharey,
            figsize=figsize,
            layout=layout,
        )
        data = {}
        for (key, group), ax in zip(grouped, flatten_axes(axes), strict=False):
            d = group.boxplot(
                ax=ax, column=column, fontsize=fontsize, rot=rot, grid=grid, **kwds
            )
            ax.set_title(pprint_thing(key))
            data[key] = d
        ret = pd.Series(data)
        maybe_adjust_figure(fig, bottom=0.15, top=0.9, left=0.1, right=0.9, wspace=0.2)
    else:
        keys, frames = zip(*grouped, strict=True)
        df = pd.concat(frames, keys=keys, axis=1)

        # GH 16748, DataFrameGroupby fails when subplots=False and `column` argument
        # is assigned, and in this case, since `df` here becomes MI after groupby,
        # so we need to couple the keys (grouped values) and column (original df
        # column) together to search for subset to plot
        if column is not None:
            column = com.convert_to_list_like(column)
            multi_key = pd.MultiIndex.from_product([keys, column])
            column = list(multi_key.values)
        ret = df.boxplot(
            column=column,
            fontsize=fontsize,
            rot=rot,
            grid=grid,
            ax=ax,
            figsize=figsize,
            layout=layout,
            **kwds,
        )
    return ret

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.groupby [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def groupby(
        self,
        by=None,
        level: IndexLabel | None = None,
        as_index: bool = True,
        sort: bool = True,
        group_keys: bool = True,
        observed: bool = True,
        dropna: bool = True,
    ) -> DataFrameGroupBy:
        """
        Group DataFrame using a mapper or by a Series of columns.

        A groupby operation involves some combination of splitting the
        object, applying a function, and combining the results. This can be
        used to group large amounts of data and compute operations on these
        groups.

        Parameters
        ----------
        by : mapping, function, label, pd.Grouper or list of such
            Used to determine the groups for the groupby.
            If ``by`` is a function, it's called on each value of the object's
            index. If a dict or Series is passed, the Series or dict VALUES
            will be used to determine the groups (the Series' values are first
            aligned; see ``.align()`` method). If a list or ndarray of length
            equal to the number of rows is passed (see the `groupby user guide
            <https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#splitting-an-object-into-groups>`_),
            the values are used as-is to determine the groups. A label or list
            of labels may be passed to group by the columns in ``self``.
            Notice that a tuple is interpreted as a (single) key.
        level : int, level name, or sequence of such, default None
            If the axis is a MultiIndex (hierarchical), group by a particular
            level or levels. Do not specify both ``by`` and ``level``.
        as_index : bool, default True
            Return object with group labels as the
            index. Only relevant for DataFrame input. as_index=False is
            effectively "SQL-style" grouped output. This argument has no effect
            on filtrations (see the `filtrations in the user guide
            <https://pandas.pydata.org/docs/dev/user_guide/groupby.html#filtration>`_),
            such as ``head()``, ``tail()``, ``nth()`` and in transformations
            (see the `transformations in the user guide
            <https://pandas.pydata.org/docs/dev/user_guide/groupby.html#transformation>`_).
        sort : bool, default True
            Sort group keys. Get better performance by turning this off.
            Note this does not influence the order of observations within each
            group. Groupby preserves the order of rows within each group. If False,
            the groups will appear in the same order as they did in the original
            DataFrame.
            This argument has no effect on filtrations (see the `filtrations
            in the user guide
            <https://pandas.pydata.org/docs/dev/user_guide/groupby.html#filtration>`_),
            such as ``head()``, ``tail()``, ``nth()`` and in transformations
            (see the `transformations in the user guide
            <https://pandas.pydata.org/docs/dev/user_guide/groupby.html#transformation>`_).

            .. versionchanged:: 2.0.0

                Specifying ``sort=False`` with an ordered categorical grouper will no
                longer sort the values.

        group_keys : bool, default True
            When calling apply and the ``by`` argument produces a like-indexed
            (i.e. :ref:`a transform <groupby.transform>`) result, add group keys to
            index to identify pieces. By default group keys are not included
            when the result's index (and column) labels match the inputs, and
            are included otherwise.

            .. versionchanged:: 2.0.0

               ``group_keys`` now defaults to ``True``.

        observed : bool, default True
            This only applies if any of the groupers are Categoricals.
            If True: only show observed values for categorical groupers.
            If False: show all values for categorical groupers.

            .. versionchanged:: 3.0.0

                The default value is now ``True``.

        dropna : bool, default True
            If True, and if group keys contain NA values, NA values together
            with row/column will be dropped.
            If False, NA values will also be treated as the key in groups.

        Returns
        -------
        pandas.api.typing.DataFrameGroupBy
            Returns a groupby object that contains information about the groups.

        See Also
        --------
        resample : Convenience method for frequency conversion and resampling
            of time series.

        Notes
        -----
        See the `user guide
        <https://pandas.pydata.org/pandas-docs/stable/groupby.html>`__ for more
        detailed usage and examples, including splitting an object into groups,
        iterating through groups, selecting a group, aggregation, and more.

        The implementation of groupby is hash-based, meaning in particular that
        objects that compare as equal will be considered to be in the same group.
        An exception to this is that pandas has special handling of NA values:
        any NA values will be collapsed to a single group, regardless of how
        they compare. See the user guide linked above for more details.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "Animal": ["Falcon", "Falcon", "Parrot", "Parrot"],
        ...         "Max Speed": [380.0, 370.0, 24.0, 26.0],
        ...     }
        ... )
        >>> df
           Animal  Max Speed
        0  Falcon      380.0
        1  Falcon      370.0
        2  Parrot       24.0
        3  Parrot       26.0
        >>> df.groupby(["Animal"]).mean()
                Max Speed
        Animal
        Falcon      375.0
        Parrot       25.0

        **Hierarchical Indexes**

        We can groupby different levels of a hierarchical index
        using the `level` parameter:

        >>> arrays = [
        ...     ["Falcon", "Falcon", "Parrot", "Parrot"],
        ...     ["Captive", "Wild", "Captive", "Wild"],
        ... ]
        >>> index = pd.MultiIndex.from_arrays(arrays, names=("Animal", "Type"))
        >>> df = pd.DataFrame({"Max Speed": [390.0, 350.0, 30.0, 20.0]}, index=index)
        >>> df
                        Max Speed
        Animal Type
        Falcon Captive      390.0
               Wild         350.0
        Parrot Captive       30.0
               Wild          20.0
        >>> df.groupby(level=0).mean()
                Max Speed
        Animal
        Falcon      370.0
        Parrot       25.0
        >>> df.groupby(level="Type").mean()
                 Max Speed
        Type
        Captive      210.0
        Wild         185.0

        We can also choose to include NA in group keys or not by setting
        `dropna` parameter, the default setting is `True`.

        >>> arr = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
        >>> df = pd.DataFrame(arr, columns=["a", "b", "c"])

        >>> df.groupby(by=["b"]).sum()
            a   c
        b
        1.0 2   3
        2.0 2   5

        >>> df.groupby(by=["b"], dropna=False).sum()
            a   c
        b
        1.0 2   3
        2.0 2   5
        NaN 1   4

        >>> arr = [["a", 12, 12], [None, 12.3, 33.0], ["b", 12.3, 123], ["a", 1, 1]]
        >>> df = pd.DataFrame(arr, columns=["a", "b", "c"])

        >>> df.groupby(by="a").sum()
            b     c
        a
        a   13.0   13.0
        b   12.3  123.0

        >>> df.groupby(by="a", dropna=False).sum()
            b     c
        a
        a   13.0   13.0
        b   12.3  123.0
        NaN 12.3   33.0

        When using ``.apply()``, use ``group_keys`` to include or exclude the
        group keys. The ``group_keys`` argument defaults to ``True`` (include).

        >>> df = pd.DataFrame(
        ...     {
        ...         "Animal": ["Falcon", "Falcon", "Parrot", "Parrot"],
        ...         "Max Speed": [380.0, 370.0, 24.0, 26.0],
        ...     }
        ... )
        >>> df.groupby("Animal", group_keys=True)[["Max Speed"]].apply(lambda x: x)
                  Max Speed
        Animal
        Falcon 0      380.0
               1      370.0
        Parrot 2       24.0
               3       26.0

        >>> df.groupby("Animal", group_keys=False)[["Max Speed"]].apply(lambda x: x)
           Max Speed
        0      380.0
        1      370.0
        2       24.0
        3       26.0
        """
        from pandas.core.groupby.generic import DataFrameGroupBy

        if level is None and by is None:
            raise TypeError("You have to supply one of 'by' and 'level'")

        return DataFrameGroupBy(
            obj=self,
            keys=by,
            level=level,
            as_index=as_index,
            sort=sort,
            group_keys=group_keys,
            observed=observed,
            dropna=dropna,
        )

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
```
