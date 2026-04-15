# pandas-22 :: hybrid-cs

query: BUG: support count function for custom BaseIndexer rolling windows (#33605)

## selected nodes

- rank=1 layer=FUNCTION tokens=392 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingGroupby._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=2 layer=FUNCTION tokens=367 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=3 layer=FUNCTION tokens=1503 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=4 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindow._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=5 layer=FUNCTION tokens=414 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::GroupbyIndexer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=6 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py::ExponentialMovingWindow._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py
- rank=7 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::tests_empty_df_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=8 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py
- rank=9 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=10 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py
- rank=11 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_maybe_add_count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py
- rank=12 layer=FUNCTION tokens=411 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::FixedForwardWindowIndexer.get_window_bounds file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=13 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::Apply.time_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=14 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.count [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def count(self, numeric_only: bool = False):
        """
        Calculate the rolling count of non NaN observations.

        This is useful for identifying windows with missing data, as it counts
        only non-NaN entries within each window.

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
        Series.rolling : Calling rolling with Series data.
        DataFrame.rolling : Calling rolling with DataFrames.
        Series.count : Aggregating count for Series.
        DataFrame.count : Aggregating count for DataFrame.

        Examples
        --------
        >>> s = pd.Series([2, 3, np.nan, 10])
        >>> s.rolling(2).count()
        0    NaN
        1    2.0
        2    1.0
        3    1.0
        dtype: float64
        >>> s.rolling(3).count()
        0    NaN
        1    NaN
        2    2.0
        3    2.0
        dtype: float64
        >>> s.rolling(4).count()
        0    NaN
        1    NaN
        2    NaN
        3    3.0
        dtype: float64
        """
        return super().count(numeric_only)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindow._get_window_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def _get_window_indexer(self) -> BaseIndexer:
        """
        Return an indexer class that will compute the window start and end bounds
        """
        if isinstance(self.window, BaseIndexer):
            return self.window
        if self._win_freq_i8 is not None:
            return VariableWindowIndexer(
                index_array=self._index_array,
                window_size=self._win_freq_i8,
                center=self.center,
            )
        return FixedWindowIndexer(window_size=self.window)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py::ExponentialMovingWindow._get_window_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py]
    def _get_window_indexer(self) -> BaseIndexer:
        """
        Return an indexer class that will compute the window start and end bounds
        """
        return ExponentialMovingWindowIndexer()

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding._get_window_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py]
    def _get_window_indexer(self) -> BaseIndexer:
        """
        Return an indexer class that will compute the window start and end bounds
        """
        return ExpandingIndexer()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.count [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def count(self, numeric_only: bool = False):
        window_func = window_aggregations.roll_sum
        return self._apply(window_func, name="count", numeric_only=numeric_only)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.count [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py]
    def count(self, value: Any, /) -> int: ...

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py::_maybe_add_count [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tseries/frequencies.py]
def _maybe_add_count(base: str, count: float) -> str:
    if count != 1:
        assert count == int(count)
        count = int(count)
        return f"{count}{base}"
    else:
        return base

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::FixedForwardWindowIndexer.get_window_bounds [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py]
    def get_window_bounds(
        self,
        num_values: int = 0,
        min_periods: int | None = None,
        center: bool | None = None,
        closed: str | None = None,
        step: int | None = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Computes the bounds of a window.

        Parameters
        ----------
        num_values : int, default 0
            number of values that will be aggregated over
        min_periods : int, default None
            min_periods passed from the top level rolling API
        center : bool, default None
            center passed from the top level rolling API
        closed : str, default None
            closed passed from the top level rolling API
        step : int, default None
            step passed from the top level rolling API

        Returns
        -------
        A tuple of ndarray[int64]s, indicating the boundaries of each
        window
        """
        if center:
            raise ValueError("Forward-looking windows can't have center=True")
        if closed is not None:
            raise ValueError(
                "Forward-looking windows don't support setting the closed argument"
            )
        if step is None:
            step = 1

        start = np.arange(0, num_values, step, dtype="int64")
        end = start + self.window_size
        if self.window_size:
            end = np.clip(end, 0, num_values)

        return start, end

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::Apply.time_rolling [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py]
    def time_rolling(self, constructor, window, dtype, function, raw):
        self.roll.apply(function, raw=raw)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py::ArrowExtensionArray.count [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/array.py]
    def count(self) -> int:
        return len(self) - self._pa_array.null_count
```
