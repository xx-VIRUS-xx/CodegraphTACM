# pandas-18 :: hybrid

query: BUG: support skew function for custom BaseIndexer rolling windows (#33745)

## selected nodes

- rank=1 layer=FUNCTION tokens=392 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingGroupby._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=2 layer=FUNCTION tokens=367 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=3 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_zero_out_fperr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py
- rank=4 layer=FUNCTION tokens=1503 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=5 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=6 layer=FUNCTION tokens=371 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py
- rank=7 layer=FUNCTION tokens=414 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::GroupbyIndexer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=8 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=9 layer=FUNCTION tokens=613 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingGroupby._get_window_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def _get_window_indexer(self) -> GroupbyIndexer:
        """
        Return an indexer class that will compute the window start and end bounds

        Returns
        -------
        GroupbyIndexer
        """
        rolling_indexer: type[BaseIndexer]
        indexer_kwargs: dict[str, Any] | None = None
        index_array = self._index_array
        if isinstance(self.window, BaseIndexer):
            rolling_indexer = type(self.window)
            indexer_kwargs = self.window.__dict__.copy()
            assert isinstance(indexer_kwargs, dict)  # for mypy
            # We'll be using the index of each group later
            indexer_kwargs.pop("index_array", None)
            window = self.window
        elif self._win_freq_i8 is not None:
            rolling_indexer = VariableWindowIndexer
            # error: Incompatible types in assignment (expression has type
            # "int", variable has type "BaseIndexer")
            window = self._win_freq_i8  # type: ignore[assignment]
        else:
            rolling_indexer = FixedWindowIndexer
            window = self.window
        window_indexer = GroupbyIndexer(
            index_array=index_array,
            window_size=window,
            groupby_indices=self._grouper.indices,
            window_indexer=rolling_indexer,
            indexer_kwargs=indexer_kwargs,
        )
        return window_indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.skew [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def skew(self, numeric_only: bool = False):
        """
        Calculate the rolling unbiased skewness.

        This is equivalent to applying ``scipy.stats.skew`` over each rolling
        window. A minimum of three periods is required.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns.

        Returns
        -------
        Series or DataFrame
            Return type is the same as the original object with ``np.float64`` dtype.

        See Also
        --------
        scipy.stats.skew : Third moment of a probability density.
        Series.rolling : Calling rolling with Series data.
        DataFrame.rolling : Calling rolling with DataFrames.
        Series.skew : Aggregating skew for Series.
        DataFrame.skew : Aggregating skew for DataFrame.

        Notes
        -----

        A minimum of three periods is required for the rolling calculation.

        Examples
        --------
        >>> ser = pd.Series([1, 5, 2, 7, 15, 6])
        >>> ser.rolling(3).skew().round(6)
        0         NaN
        1         NaN
        2    1.293343
        3   -0.585583
        4    0.670284
        5    1.652317
        dtype: float64
        """
        return super().skew(numeric_only=numeric_only)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_zero_out_fperr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py]
def _zero_out_fperr(arg, tol: float | np.ndarray):
    # #18044 reference this behavior to fix rolling skew/kurt issue
    if isinstance(arg, np.ndarray):
        return np.where(np.abs(arg) < tol, 0, arg)
    else:
        return arg.dtype.type(0) if np.abs(arg) < tol else arg

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.rolling [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py]
    def rolling(
        self,
        window: int | datetime.timedelta | str | BaseOffset | BaseIndexer,
        min_periods: int | None = None,
        center: bool = False,
        win_type: str | None = None,
        on: str | None = None,
        closed: IntervalClosedType | None = None,
        method: str = "single",
    ) -> RollingGroupby:
        """
        Return a rolling grouper, providing rolling functionality per group.

        Allows the application of rolling window operations
        (e.g., moving averages) independently within each group defined
        by the groupby keys.

        Parameters
        ----------
        window : int, timedelta, str, offset, or BaseIndexer subclass
            Interval of the moving window.

            If an integer, the delta between the start and end of each window.
            The number of points in the window depends on the ``closed`` argument.

            If a timedelta, str, or offset, the time period of each window. Each
            window will be a variable sized based on the observations included in
            the time-period. This is only valid for datetimelike indexes.
            To learn more about the offsets & frequency strings, please see
            :ref:`this link<timeseries.offset_aliases>`.

            If a BaseIndexer subclass, the window boundaries
            based on the defined ``get_window_bounds`` method. Additional rolling
            keyword arguments, namely ``min_periods``, ``center``, ``closed`` and
            ``step`` will be passed to ``get_window_bounds``.

        min_periods : int, default None
            Minimum number of observations in window required to have a value;
            otherwise, result is ``np.nan``.

            For a window that is specified by an offset,
            ``min_periods`` will default to 1.

            For a window that is specified by an integer, ``min_periods`` will default
            to the size of the window.

        center : bool, default False
            If False, set the window labels as the right edge of the window index.

            If True, set the window labels as the center of the window index.

        win_type : str, default None
            If ``None``, all points are evenly weighted.

            If a string, it must be a valid `scipy.signal window function
            <https://docs.scipy.org/doc/scipy/reference/signal.windows.html#module-scipy.signal.windows>`__.

            Certain Scipy window types require additional parameters to be passed
            in the aggregation function. The additional parameters must match
            the keywords specified in the Scipy window type method signature.

        on : str, optional
            For a DataFrame, a column label or Index level on which
            to calculate the rolling window, rather than the DataFrame's index.

            Provided integer column is ignored and excluded from result since
            an integer index is not used to calculate the rolling window.

        closed : str, default None
            Determines the inclusivity of points in the window

            If ``'right'``, uses the window (first, last] meaning the last point
            is included in the calculations.

            If ``'left'``, uses the window [first, last) meaning the first point
            is included in the calculations.

            If ``'both'``, uses the window [first, last] meaning all points in
            the window are included in the calculations.

            If ``'neither'``, uses the window (first, last) meaning the first
            and last points in the window are excluded from calculations.

            () and [] are referencing open and closed set
            notation respetively.

            Default ``None`` (``'right'``).

        method : str {'single', 'table'}, default 'single'
            Execute the rolling operation per single column or row (``'single'``)
            or over the entire object (``'table'``).

            This argument is only implemented when specifying ``engine='numba'``
            in the method call.

        Returns
        -------
        pandas.api.typing.RollingGroupby
            Return a new grouper with our rolling appended.

        See Also
        --------
        Series.rolling : Calling object with Series data.
        DataFrame.rolling : Calling object with DataFrames.
        Series.groupby : Apply a function groupby to a Series.
        DataFrame.groupby : Apply a function groupby.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "A": [1, 1, 2, 2],
        ...         "B": [1, 2, 3, 4],
        ...         "C": [0.362, 0.227, 1.267, -0.562],
        ...     }
        ... )
        >>> df
              A  B      C
        0     1  1  0.362
        1     1  2  0.227
        2     2  3  1.267
        3     2  4 -0.562

        >>> df.groupby("A").rolling(2).sum()
            B      C
        A
        1 0  NaN    NaN
          1  3.0  0.589
        2 2  NaN    NaN
          3  7.0  0.705

        >>> df.groupby("A").rolling(2, min_periods=1).sum()
            B      C
        A
        1 0  1.0  0.362
          1  3.0  0.589
        2 2  3.0  1.267
          3  7.0  0.705

        >>> df.groupby("A").rolling(2, on="B").sum()
            B      C
        A
        1 0  1    NaN
          1  2  0.589
        2 2  3    NaN
          3  4  0.705
        """
        from pandas.core.window import RollingGroupby

        return RollingGroupby(
            self._selected_obj,
            window=window,
            min_periods=min_periods,
            center=center,
            win_type=win_type,
            on=on,
            closed=closed,
            method=method,
            _grouper=self._grouper,
            _as_index=self.as_index,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.skew [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def skew(
        self,
        *,
        axis: Axis | None = 0,
        skipna: bool = True,
        numeric_only: bool = False,
        **kwargs,
    ) -> Series | float:
        return self._stat_function(
            "skew", nanops.nanskew, axis, skipna, numeric_only, **kwargs
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding.skew [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py]
    def skew(self, numeric_only: bool = False):
        """
        Calculate the expanding unbiased skewness.

        Computes the third standardized moment over all data points seen
        so far, measuring the asymmetry of the distribution.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns.

        Returns
        -------
        Series or DataFrame
            Return type is the same as the original object with ``np.float64`` dtype.

        See Also
        --------
        scipy.stats.skew : Third moment of a probability density.
        Series.expanding : Calling expanding with Series data.
        DataFrame.expanding : Calling expanding with DataFrames.
        Series.skew : Aggregating skew for Series.
        DataFrame.skew : Aggregating skew for DataFrame.

        Notes
        -----
        A minimum of three periods is required for the rolling calculation.

        Examples
        --------
        >>> ser = pd.Series([-1, 0, 2, -1, 2], index=["a", "b", "c", "d", "e"])
        >>> ser.expanding().skew()
        a         NaN
        b         NaN
        c    0.935220
        d    1.414214
        e    0.315356
        dtype: float64
        """
        return super().skew(numeric_only=numeric_only)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::GroupbyIndexer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py]
    def __init__(
        self,
        index_array: np.ndarray | None = None,
        window_size: int | BaseIndexer = 0,
        groupby_indices: dict | None = None,
        window_indexer: type[BaseIndexer] = BaseIndexer,
        indexer_kwargs: dict | None = None,
        **kwargs,
    ) -> None:
        """
        Parameters
        ----------
        index_array : np.ndarray or None
            np.ndarray of the index of the original object that we are performing
            a chained groupby operation over. This index has been pre-sorted relative to
            the groups
        window_size : int or BaseIndexer
            window size during the windowing operation
        groupby_indices : dict or None
            dict of {group label: [positional index of rows belonging to the group]}
        window_indexer : BaseIndexer
            BaseIndexer class determining the start and end bounds of each group
        indexer_kwargs : dict or None
            Custom kwargs to be passed to window_indexer
        **kwargs :
            keyword arguments that will be available when get_window_bounds is called
        """
        self.groupby_indices = groupby_indices or {}
        self.window_indexer = window_indexer
        self.indexer_kwargs = indexer_kwargs.copy() if indexer_kwargs else {}
        super().__init__(
            index_array=index_array,
            window_size=self.indexer_kwargs.pop("window_size", window_size),
            **kwargs,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.skew [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def skew(self, numeric_only: bool = False):
        window_func = window_aggregations.roll_skew
        return self._apply(
            window_func,
            name="skew",
            numeric_only=numeric_only,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.skew [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py]
    def skew(
        self,
        axis: Axis | None = 0,
        skipna: bool = True,
        numeric_only: bool = False,
        **kwargs,
    ) -> Series | Any:
        """
        Return unbiased skew over requested axis.

        Normalized by N-1.

        Parameters
        ----------
        axis : {index (0), columns (1)}
            Axis for the function to be applied on.
            For `Series` this parameter is unused and defaults to 0.

            For DataFrames, specifying ``axis=None`` will apply the aggregation
            across both axes.

            .. versionadded:: 2.0.0

        skipna : bool, default True
            Exclude NA/null values when computing the result.
        numeric_only : bool, default False
            Include only float, int, boolean columns.

        **kwargs
            Additional keyword arguments to be passed to the function.

        Returns
        -------
        Series or scalar
            Unbiased skew over requested axis.

        See Also
        --------
        DataFrame.kurt : Returns unbiased kurtosis over requested axis.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> s.skew()
        0.0

        With a DataFrame

        >>> df = pd.DataFrame(
        ...     {"a": [1, 2, 3], "b": [2, 3, 4], "c": [1, 3, 5]},
        ...     index=["tiger", "zebra", "cow"],
        ... )
        >>> df
                a   b   c
        tiger   1   2   1
        zebra   2   3   3
        cow     3   4   5
        >>> df.skew()
        a   0.0
        b   0.0
        c   0.0
        dtype: float64

        Using axis=1

        >>> df.skew(axis=1)
        tiger   1.732051
        zebra  -1.732051
        cow     0.000000
        dtype: float64

        In this case, `numeric_only` should be set to `True` to avoid
        getting an error.

        >>> df = pd.DataFrame(
        ...     {"a": [1, 2, 3], "b": ["T", "Z", "X"]}, index=["tiger", "zebra", "cow"]
        ... )
        >>> df.skew(numeric_only=True)
        a   0.0
        dtype: float64
        """
        result = super().skew(
            axis=axis, skipna=skipna, numeric_only=numeric_only, **kwargs
        )
        if isinstance(result, Series):
            result = result.__finalize__(self, method="skew")
        return result
```
