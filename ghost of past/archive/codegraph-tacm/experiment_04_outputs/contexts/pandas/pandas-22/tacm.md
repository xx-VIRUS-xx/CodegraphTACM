# pandas-22 :: tacm

query: BUG: support count function for custom BaseIndexer rolling windows (#33605)

## selected nodes

- rank=1 layer=FILE tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=2 layer=FILE tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py
- rank=3 layer=FILE tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=4 layer=FILE tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/tools/numeric.py
- rank=5 layer=CLASS tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=6 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::CustomIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=7 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::PrescribedWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=8 layer=CLASS tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=9 layer=CLASS tokens=459 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py::TestRolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py
- rank=10 layer=CLASS tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingGroupby file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=11 layer=CLASS tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::FixedForwardWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=12 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::BaseIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=13 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::VariableWindowIndexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=14 layer=CLASS tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/errors/__init__.py::MergeError file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/errors/__init__.py
- rank=15 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=16 layer=FUNCTION tokens=347 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingGroupby._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=17 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.aggregate file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=18 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.sem file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=19 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=20 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py::is_platform_windows file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/__init__.py
- rank=21 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling._validate_datetimelike_monotonic file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=22 layer=FUNCTION tokens=135 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py::tests_empty_df_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_rolling.py
- rank=23 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::BaseIndexer.get_window_bounds file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=24 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py::GroupBy.rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/groupby/groupby.py
- rank=25 layer=FUNCTION tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::Apply.time_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=26 layer=FUNCTION tokens=283 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.first file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=27 layer=FUNCTION tokens=283 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.last file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=28 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomSeries.custom_series_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py
- rank=29 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py::CustomDataFrame.custom_frame_function file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_subclass.py
- rank=30 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=31 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.kurt file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=32 layer=FUNCTION tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py::rolling_aggregation file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_cython_aggregations.py
- rank=33 layer=FUNCTION tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::BaseIndexer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=34 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.nunique file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=35 layer=FUNCTION tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py::TestRolling.func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/window/test_groupby.py
- rank=36 layer=FUNCTION tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.quantile file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=37 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=38 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.corr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=39 layer=FUNCTION tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.sum file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=40 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=41 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.max file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=42 layer=FUNCTION tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.count file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=43 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.rank file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=44 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/core.py::BarhPlot._get_custom_index_name file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/plotting/_matplotlib/core.py
- rank=45 layer=FUNCTION tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py::ParallelRolling.parallel_rolling file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/gil.py

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

class TestRolling:  [tests/window/test_groupby.py:52]
methods: func, func, isnumpyarray, test_as_index_false
         test_by_column_not_in_values
         test_datelike_on_monotonic_within_each_group
         test_datelike_on_not_monotonic_within_each_group
         test_getitem, test_getitem_multiple
         test_groupby_level, test_groupby_monotonic
         test_groupby_rolling
         test_groupby_rolling_agg_namedagg
         test_groupby_rolling_center_center
         test_groupby_rolling_center_min_periods
         test_groupby_rolling_center_on
         test_groupby_rolling_count_closed_on
         test_groupby_rolling_custom_indexer
         test_groupby_rolling_empty_frame
         test_groupby_rolling_group_keys
         test_groupby_rolling_index_changed
         test_groupby_rolling_index_level_and_column_label
         test_groupby_rolling_nans_in_index
         test_groupby_rolling_no_sort
         test_groupby_rolling_non_monotonic
         test_groupby_rolling_object_doesnt_affect_groupby_apply
         test_groupby_rolling_resulting_multiindex
         test_groupby_rolling_resulting_multiindex2
         test_groupby_rolling_resulting_multiindex3
         test_groupby_rolling_sem
         test_groupby_rolling_string_index
         test_groupby_rolling_subset_with_closed
         test_groupby_rolling_var
         test_groupby_subselect_rolling
         test_groupby_subset_rolling_subset_with_closed
         test_groupby_unsupported_argument
         test_nan_and_zero_endpoints, test_rolling
         test_rolling_apply, test_rolling_apply_mutability
         test_rolling_corr_cov_other_diff_size_as_groups
         test_rolling_corr_cov_other_same_size_as_groups
         test_rolling_corr_cov_pairwise
         test_rolling_corr_cov_unordered
         test_rolling_ddof, test_rolling_quantile

class RollingGroupby(BaseWindowGroupby, Rolling):  [core/window/rolling.py:3533]
methods: _get_window_indexer, _validate_datetimelike_monotonic

class FixedForwardWindowIndexer(BaseIndexer):  [core/indexers/objects.py:429]
methods: get_window_bounds

class BaseIndexer:  [core/indexers/objects.py:21]
methods: get_window_bounds, __init__

class VariableWindowIndexer(BaseIndexer):  [core/indexers/objects.py:158]
methods: get_window_bounds

class MergeError(ValueError):  [pandas/errors/__init__.py:456]
methods: —

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

    def sem(self, ddof: int = 1, numeric_only: bool = False):
        """
        Calculate the rolling standard error of mean.

        This is computed as the rolling standard deviation divided by the
        square root of the rolling count. A minimum of one period is required.

        Parameters
        ----------
        ddof : int, default 1
            Delta Degrees of Freedom.  The divisor used in calculations
            is ``N - ddof``, where ``N`` represents the number of elements.
    # ... truncated

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

    def time_rolling(self, constructor, window, dtype, function, raw):
        self.roll.apply(function, raw=raw)

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

            def custom_series_function(self):
                return "OK"

            def custom_frame_function(self):
                return "OK"

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

    def kurt(self, numeric_only: bool = False):
        """
        Calculate the rolling Fisher's definition of kurtosis without bias.

        This is equivalent to applying ``scipy.stats.kurtosis`` (with
        ``bias=False``) over each rolling window. A minimum of four periods
        is required.

        Parameters
        ----------
        numeric_only : bool, default False
            Include only float, int, boolean columns.
    # ... truncated

def rolling_aggregation(request):
    """Make a rolling aggregation function as fixture."""
    return request.param

    def __init__(
        self, index_array: np.ndarray | None = None, window_size: int = 0, **kwargs
    ) -> None:
        self.index_array = index_array
        self.window_size = window_size
        # Set user defined kwargs as attributes that can be used in get_window_bounds
        for key, value in kwargs.items():
            setattr(self, key, value)

    def nunique(
        self,
        numeric_only: bool = False,
    ):
        """
    # ... truncated

        def func(x):
            return getattr(x.B.rolling(4), f)(pairwise=True)

    def quantile(
        self,
        q: float,
        interpolation: QuantileInterpolation = "linear",
        numeric_only: bool = False,
    ):
        """
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

    def corr(
        self,
        other: DataFrame | Series | None = None,
        pairwise: bool | None = None,
        ddof: int = 1,
        numeric_only: bool = False,
    ):
        """
    # ... truncated

    def sum(
        self,
        numeric_only: bool = False,
        engine: Literal["cython", "numba"] | None = None,
        engine_kwargs: dict[str, bool] | None = None,
    ):
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

    def max(
        self,
        numeric_only: bool = False,
        *args,
        engine: Literal["cython", "numba"] | None = None,
        engine_kwargs: dict[str, bool] | None = None,
        **kwargs,
    ):
        """
    # ... truncated

    def count(self, numeric_only: bool = False):
        window_func = window_aggregations.roll_sum
        return self._apply(window_func, name="count", numeric_only=numeric_only)

    def rank(
        self,
        method: WindowingRankType = "average",
        ascending: bool = True,
        pct: bool = False,
        numeric_only: bool = False,
    ):
        """
    # ... truncated

    def _get_custom_index_name(self):
        return self.ylabel

            def parallel_rolling():
                rolling[method](arr, win)
```
