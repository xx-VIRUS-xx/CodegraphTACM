# pandas-18 :: tacm

query: BUG: support skew function for custom BaseIndexer rolling windows (#33745)

## selected nodes

- rank=1 layer=FILE tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=2 layer=FILE tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py
- rank=3 layer=FILE tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=4 layer=FILE tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py
- rank=5 layer=CLASS tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=6 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::CustomIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=7 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::PrescribedWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=8 layer=CLASS tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=9 layer=CLASS tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingGroupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=10 layer=CLASS tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::FixedForwardWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=11 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::BaseIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=12 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::VariableWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=13 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::FixedWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=14 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::ExpandingIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=15 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::ExponentialMovingWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=16 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::GroupbyIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=17 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::VariableOffsetWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=18 layer=CLASS tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindow file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=19 layer=CLASS tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::AggEngine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=20 layer=CLASS tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::TransformEngine file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=21 layer=CLASS tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindowGroupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=22 layer=CLASS tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py::Apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/groupby.py
- rank=23 layer=CLASS tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::Apply file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=24 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=25 layer=FUNCTION tokens=347 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingGroupby._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=26 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::Apply.time_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=27 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=28 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=29 layer=FUNCTION tokens=371 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::GroupbyIndexer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=30 layer=FUNCTION tokens=234 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py::ParallelRolling.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py
- rank=31 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=32 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=33 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::tests_empty_df_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=34 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py::is_platform_windows file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py
- rank=35 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling._validate_datetimelike_monotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=36 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::BaseIndexer.get_window_bounds file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=37 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=38 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::Apply.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=39 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomSeries.custom_series_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py
- rank=40 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomDataFrame.custom_frame_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py
- rank=41 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=42 layer=FUNCTION tokens=283 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.first file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=43 layer=FUNCTION tokens=283 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.last file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=44 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindow._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=45 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py::rolling_aggregation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py

## context

```text
file core/window/rolling.py
imports: __future__, copy, datetime, functools, inspect, typing, numpy, pandas
defines: BaseWindow, BaseWindowGroupby, Window, RollingAndExpandingMixin, Rolling, RollingGroupby

file pandas/compat/__init__.py
imports: __future__, platform, sys, typing, pandas
defines: set_function_name, is_platform_little_endian, is_platform_windows, is_platform_linux, is_platform_mac, is_platform_arm, is_platform_power, is_platform_riscv64

file core/indexers/objects.py
imports: __future__, datetime, numpy, pandas
defines: BaseIndexer, FixedWindowIndexer, VariableWindowIndexer, VariableOffsetWindowIndexer, ExpandingIndexer, FixedForwardWindowIndexer, GroupbyIndexer, ExponentialMovingWindowIndexer

file core/tools/numeric.py
imports: __future__, typing, numpy, pandas
defines: to_numeric

class Rolling(RollingAndExpandingMixin):  [core/window/rolling.py:1979]
methods: _raise_monotonic_error, _validate
         _validate_datetimelike_monotonic, aggregate
         apply, corr, count, cov, first, kurt, last, max
         mean, median, min, nunique, pipe, pipe, pipe
         quantile, rank, sem, skew, std, sum, var

class CustomIndexer(BaseIndexer):  [tests/window/test_rolling.py:1354]
methods: get_window_bounds

class PrescribedWindowIndexer(BaseIndexer):  [tests/window/test_rolling.py:2055]
methods: get_window_bounds, __init__

class RollingAndExpandingMixin(BaseWindow):  [core/window/rolling.py:1537]
methods: _generate_cython_apply_func, apply, apply_func, corr
         corr_func, count, cov, cov_func, first, kurt
         last, max, mean, median, min, nunique, pipe, pipe
         pipe, quantile, rank, sem, skew, std, sum, var
         zsqrt_func

class RollingGroupby(BaseWindowGroupby, Rolling):  [core/window/rolling.py:3533]
methods: _get_window_indexer, _validate_datetimelike_monotonic

class FixedForwardWindowIndexer(BaseIndexer):  [core/indexers/objects.py:429]
methods: get_window_bounds

class BaseIndexer:  [core/indexers/objects.py:21]
methods: get_window_bounds, __init__

class VariableWindowIndexer(BaseIndexer):  [core/indexers/objects.py:158]
methods: get_window_bounds

class FixedWindowIndexer(BaseIndexer):  [core/indexers/objects.py:108]
methods: get_window_bounds

class ExpandingIndexer(BaseIndexer):  [core/indexers/objects.py:390]
methods: get_window_bounds

class ExponentialMovingWindowIndexer(BaseIndexer):  [core/indexers/objects.py:637]
methods: get_window_bounds

class GroupbyIndexer(BaseIndexer):  [core/indexers/objects.py:524]
methods: get_window_bounds, __init__

class VariableOffsetWindowIndexer(BaseIndexer):  [core/indexers/objects.py:211]
methods: get_window_bounds, __init__

class BaseWindow(SelectionMixin):  [core/window/rolling.py:116]
methods: _apply, _apply_columnwise, _apply_pairwise, _apply_series
         _apply_tablewise, _check_window_bounds
         _create_data, _dir_additions, _get_window_indexer
         _gotitem, _index_array, _insert_on_column
         _make_numeric_only, _numba_apply, _prep_values
         _resolve_output, _slice_axis_for_step, _validate
         _validate_numeric_only, aggregate, calc
         homogeneous_func, __getattr__, __init__, __iter__
         __repr__

class AggEngine:  [asv_bench/benchmarks/groupby.py:1048]
methods: function, function, function, function, setup
         time_dataframe_cython, time_dataframe_numba
         time_series_cython, time_series_numba

class TransformEngine:  [asv_bench/benchmarks/groupby.py:1006]
methods: function, function, function, function, setup
         time_dataframe_cython, time_dataframe_numba
         time_series_cython, time_series_numba

class BaseWindowGroupby(BaseWindow):  [core/window/rolling.py:660]
methods: _apply, _apply_pairwise, _create_data, _gotitem, __init__

class Apply:  [asv_bench/benchmarks/groupby.py:104]
methods: df_copy_function, setup, time_copy_function_multi_col
         time_copy_overhead_single_col
         time_scalar_function_multi_col
         time_scalar_function_single_col

class Apply:  [asv_bench/benchmarks/rolling.py:43]
methods: setup, time_rolling

    def skew(self, numeric_only: bool = False):
        """
        Calculate the rolling unbiased skewness.

        This is equivalent to applying ``scipy.stats.skew`` over each rolling
        window. A minimum of three periods is required.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns.

    # ... truncated

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

    def time_rolling(self, constructor, window, dtype, function, raw):
        self.roll.apply(function, raw=raw)

    def count(self, numeric_only: bool = False):
        """
        Calculate the rolling count of non NaN observations.

        This is useful for identifying windows with missing data, as it counts
        only non-NaN entries within each window.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns.

    # ... truncated

    def aggregate(self, func=None, *args, **kwargs):
        """
        Aggregate using one or more operations over the specified axis.

        This method allows combining multiple aggregation functions (e.g.
        ``'sum'``, ``'mean'``) in a single call, returning a result for each
        function applied to each rolling window.

        Parameters
        ----------
        func : function, str, list or dict
            Function to use for aggregating the data. If a function, must either
    # ... truncated

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
    # ... truncated

    def skew(self, numeric_only: bool = False):
        window_func = window_aggregations.roll_skew
        return self._apply(
            window_func,
            name="skew",
            numeric_only=numeric_only,
        )

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

def is_platform_windows() -> bool:
    """
    Checking if the running platform is windows.

    Returns
    -------
    bool
        True if the running platform is windows.
    """
    return sys.platform in ["win32", "cygwin"]

    def _validate_datetimelike_monotonic(self) -> None:
        """
        Validate self._on is monotonic (increasing or decreasing) and has
        no NaT values for frequency windows.
        """
        if self._on.hasnans:
            self._raise_monotonic_error("values must not have NaT")
        if not (self._on.is_monotonic_increasing or self._on.is_monotonic_decreasing):
            self._raise_monotonic_error("values must be monotonic")

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
        raise NotImplementedError

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
    # ... truncated

    def setup(self, constructor, window, dtype, function, raw):
        N = 10**3
        arr = (100 * np.random.random(N)).astype(dtype)
        self.roll = getattr(pd, constructor)(arr).rolling(window)

            def custom_series_function(self):
                return "OK"

            def custom_frame_function(self):
                return "OK"

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

    def first(self, numeric_only: bool = False):
        """
        Calculate the rolling First (left-most) element of the window.

        Return the first observed value in each rolling window. This is useful
        for tracking the starting value of a window as it slides forward.

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
        GroupBy.first : Similar method for GroupBy objects.
        Rolling.last : Method to get the last element in each window.

        Examples
        --------
        The example below will show a rolling calculation with a window size of
        three.

        >>> s = pd.Series(range(5))
        >>> s.rolling(3).first()
        0         NaN
        1         NaN
        2         0.0
        3         1.0
        4         2.0
        dtype: float64
        """
        return super().first(numeric_only=numeric_only)

    def last(self, numeric_only: bool = False):
        """
        Calculate the rolling Last (right-most) element of the window.

        Return the last observed value in each rolling window. This is useful
        for tracking the most recent value of a window as it slides forward.

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
        GroupBy.last : Similar method for GroupBy objects.
        Rolling.first : Method to get the first element in each window.

        Examples
        --------
        The example below will show a rolling calculation with a window size of
        three.

        >>> s = pd.Series(range(5))
        >>> s.rolling(3).last()
        0         NaN
        1         NaN
        2         2.0
        3         3.0
        4         4.0
        dtype: float64
        """
        return super().last(numeric_only=numeric_only)

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

def rolling_aggregation(request):
    """Make a rolling aggregation function as fixture."""
    return request.param
```
