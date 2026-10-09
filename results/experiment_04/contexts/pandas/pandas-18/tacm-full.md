# pandas-18 :: tacm-full

query: BUG: support skew function for custom BaseIndexer rolling windows (#33745)

## selected nodes

- rank=1 layer=FUNCTION tokens=276 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py::ParallelRolling.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py
- rank=2 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::tests_empty_df_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=3 layer=FUNCTION tokens=2358 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=4 layer=FUNCTION tokens=392 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingGroupby._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=5 layer=FUNCTION tokens=367 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=6 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomSeries.custom_series_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py
- rank=7 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomDataFrame.custom_frame_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py
- rank=8 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py::rolling_aggregation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py
- rank=9 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::Apply.time_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=10 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py::ParallelRolling.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py]
    def setup(self, method):
        win = 100
        arr = np.random.rand(100000)
        if hasattr(DataFrame, "rolling"):
            df = DataFrame(arr).rolling(win)

            @run_parallel(num_threads=2)
            def parallel_rolling():
                getattr(df, method)()

            self.parallel_rolling = parallel_rolling
        elif have_rolling_methods:
            rolling = {
                "median": rolling_median,
                "mean": rolling_mean,
                "min": rolling_min,
                "max": rolling_max,
                "var": rolling_var,
                "skew": rolling_skew,
                "kurt": rolling_kurt,
                "std": rolling_std,
            }

            @run_parallel(num_threads=2)
            def parallel_rolling():
                rolling[method](arr, win)

            self.parallel_rolling = parallel_rolling
        else:
            raise NotImplementedError

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::tests_empty_df_rolling [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py]
def tests_empty_df_rolling(roller):
    # GH 15819 Verifies that datetime and integer rolling windows can be
    # applied to empty DataFrames
    expected = DataFrame()
    result = DataFrame().rolling(roller).sum()
    tm.assert_frame_equal(result, expected)

    # Verifies that datetime and integer rolling windows can be applied to
    # empty DataFrames with datetime index
    expected = DataFrame(index=DatetimeIndex([]))
    result = DataFrame(index=DatetimeIndex([])).rolling(roller).sum()
    tm.assert_frame_equal(result, expected)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.rolling [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def rolling(
        self,
        window: int | dt.timedelta | str | BaseOffset | BaseIndexer,
        min_periods: int | None = None,
        center: bool = False,
        win_type: str | None = None,
        on: str | None = None,
        closed: IntervalClosedType | None = None,
        step: int | None = None,
        method: str = "single",
    ) -> Window | Rolling:
        """
        Provide rolling window calculations.

        This method returns a rolling window object, enabling aggregation,
        transformation, and other operations over a sliding window of a
        specified size.

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

            For a window that is specified by an offset, ``min_periods`` will default
            to 1.

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

        step : int, default None
            Evaluate the window at every ``step`` result, equivalent to slicing as
            ``[::step]``. ``window`` must be an integer. Using a step argument other
            than None or 1 will produce a result with a different shape than the input.

        method : str {'single', 'table'}, default 'single'

            Execute the rolling operation per single column or row (``'single'``)
            or over the entire object (``'table'``).

            This argument is only implemented when specifying ``engine='numba'``
            in the method call.

        Returns
        -------
        pandas.api.typing.Window or pandas.api.typing.Rolling
            An instance of Window is returned if ``win_type`` is passed. Otherwise,
            an instance of Rolling is returned.

        See Also
        --------
        expanding : Provides expanding transformations.
        ewm : Provides exponential weighted functions.

        Notes
        -----
        See :ref:`Windowing Operations <window.generic>` for further usage details
        and examples.

        Examples
        --------
        >>> df = pd.DataFrame({"B": [0, 1, 2, np.nan, 4]})
        >>> df
             B
        0  0.0
        1  1.0
        2  2.0
        3  NaN
        4  4.0

        **window**

        Rolling sum with a window length of 2 observations.

        >>> df.rolling(2).sum()
             B
        0  NaN
        1  1.0
        2  3.0
        3  NaN
        4  NaN

        Rolling sum with a window span of 2 seconds.

        >>> df_time = pd.DataFrame(
        ...     {"B": [0, 1, 2, np.nan, 4]},
        ...     index=[
        ...         pd.Timestamp("20130101 09:00:00"),
        ...         pd.Timestamp("20130101 09:00:02"),
        ...         pd.Timestamp("20130101 09:00:03"),
        ...         pd.Timestamp("20130101 09:00:05"),
        ...         pd.Timestamp("20130101 09:00:06"),
        ...     ],
        ... )

        >>> df_time
                               B
        2013-01-01 09:00:00  0.0
        2013-01-01 09:00:02  1.0
        2013-01-01 09:00:03  2.0
        2013-01-01 09:00:05  NaN
        2013-01-01 09:00:06  4.0

        >>> df_time.rolling("2s").sum()
                               B
        2013-01-01 09:00:00  0.0
        2013-01-01 09:00:02  1.0
        2013-01-01 09:00:03  3.0
        2013-01-01 09:00:05  NaN
        2013-01-01 09:00:06  4.0

        Rolling sum with forward looking windows with 2 observations.

        >>> indexer = pd.api.indexers.FixedForwardWindowIndexer(window_size=2)
        >>> df.rolling(window=indexer, min_periods=1).sum()
             B
        0  1.0
        1  3.0
        2  2.0
        3  4.0
        4  4.0

        **min_periods**

        Rolling sum with a window length of 2 observations, but only needs a minimum
        of 1 observation to calculate a value.

        >>> df.rolling(2, min_periods=1).sum()
             B
        0  0.0
        1  1.0
        2  3.0
        3  2.0
        4  4.0

        **center**

        Rolling sum with the result assigned to the center of the window index.

        >>> df.rolling(3, min_periods=1, center=True).sum()
             B
        0  1.0
        1  3.0
        2  3.0
        3  6.0
        4  4.0

        >>> df.rolling(3, min_periods=1, center=False).sum()
             B
        0  0.0
        1  1.0
        2  3.0
        3  3.0
        4  6.0

        **step**

        Rolling sum with a window length of 2 observations, minimum of 1 observation to
        calculate a value, and a step of 2.

        >>> df.rolling(2, min_periods=1, step=2).sum()
             B
        0  0.0
        2  3.0
        4  4.0

        **win_type**

        Rolling sum with a window length of 2, using the Scipy ``'gaussian'``
        window type. ``std`` is required in the aggregation function.

        >>> df.rolling(2, win_type="gaussian").sum(std=3)
                  B
        0        NaN
        1   0.986207
        2   2.958621
        3        NaN
        4        NaN

        **on**

        Rolling sum with a window length of 2 days.

        >>> df = pd.DataFrame(
        ...     {
        ...         "A": [
        ...             pd.to_datetime("2020-01-01"),
        ...             pd.to_datetime("2020-01-01"),
        ...             pd.to_datetime("2020-01-02"),
        ...         ],
        ...         "B": [1, 2, 3],
        ...     },
        ...     index=pd.date_range("2020", periods=3),
        ... )

        >>> df
                            A  B
        2020-01-01 2020-01-01  1
        2020-01-02 2020-01-01  2
        2020-01-03 2020-01-02  3

        >>> df.rolling("2D", on="A").sum()
                            A    B
        2020-01-01 2020-01-01  1.0
        2020-01-02 2020-01-01  3.0
        2020-01-03 2020-01-02  6.0
        """
        if win_type is not None:
            return Window(
                self,
                window=window,
                min_periods=min_periods,
                center=center,
                win_type=win_type,
                on=on,
                closed=closed,
                step=step,
                method=method,
            )

        return Rolling(
            self,
            window=window,
            min_periods=min_periods,
            center=center,
            win_type=win_type,
            on=on,
            closed=closed,
            step=step,
            method=method,
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomSeries.custom_series_function [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py]
            def custom_series_function(self):
                return "OK"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomDataFrame.custom_frame_function [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py]
            def custom_frame_function(self):
                return "OK"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py::rolling_aggregation [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py]
def rolling_aggregation(request):
    """Make a rolling aggregation function as fixture."""
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::Apply.time_rolling [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py]
    def time_rolling(self, constructor, window, dtype, function, raw):
        self.roll.apply(function, raw=raw)

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
```
