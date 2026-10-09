# pandas-18 :: minilm

query: BUG: support skew function for custom BaseIndexer rolling windows (#33745)

## selected nodes

- rank=1 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=2 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py::TestNanskewFixedValues.actual_skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py
- rank=3 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::BaseWindow._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=4 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_zero_out_fperr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py
- rank=5 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py
- rank=6 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py::ExponentialMovingWindow._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py
- rank=7 layer=FUNCTION tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py
- rank=8 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py::TestnanopsDataFrame._skew_kurt_wrap file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py
- rank=9 layer=FUNCTION tokens=110 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=10 layer=FUNCTION tokens=392 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingGroupby._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=11 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::ForwardWindowMethods.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py
- rank=12 layer=FUNCTION tokens=314 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py
- rank=13 layer=FUNCTION tokens=613 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py::DataFrame.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/frame.py
- rank=14 layer=FUNCTION tokens=367 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Rolling.skew file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=15 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::ExpandingGroupby._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py
- rank=16 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Window._center_window file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py
- rank=17 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::VariableOffsetWindowIndexer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=18 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py::ExponentialMovingWindowGroupby._get_window_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py
- rank=19 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::TestDataFrameAnalytics.skewness file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py
- rank=20 layer=FUNCTION tokens=414 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::GroupbyIndexer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py
- rank=21 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._convert_to_indexer file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::RollingAndExpandingMixin.skew [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def skew(self, numeric_only: bool = False):
        window_func = window_aggregations.roll_skew
        return self._apply(
            window_func,
            name="skew",
            numeric_only=numeric_only,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py::TestNanskewFixedValues.actual_skew [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py]
    def actual_skew(self):
        return -0.1875895205961754

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py::_zero_out_fperr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/nanops.py]
def _zero_out_fperr(arg, tol: float | np.ndarray):
    # #18044 reference this behavior to fix rolling skew/kurt issue
    if isinstance(arg, np.ndarray):
        return np.where(np.abs(arg) < tol, 0, arg)
    else:
        return arg.dtype.type(0) if np.abs(arg) < tol else arg

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::Expanding._get_window_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py]
    def _get_window_indexer(self) -> BaseIndexer:
        """
        Return an indexer class that will compute the window start and end bounds
        """
        return ExpandingIndexer()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py::ExponentialMovingWindow._get_window_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py]
    def _get_window_indexer(self) -> BaseIndexer:
        """
        Return an indexer class that will compute the window start and end bounds
        """
        return ExponentialMovingWindowIndexer()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py::NumpyExtensionArray.skew [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/numpy_.py]
    def skew(
        self,
        *,
        axis: AxisInt | None = None,
        dtype: NpDtype | None = None,
        out=None,
        keepdims: bool = False,
        skipna: bool = True,
    ):
        nv.validate_stat_ddof_func(
            (), {"dtype": dtype, "out": out, "keepdims": keepdims}, fname="skew"
        )
        result = nanops.nanskew(self._ndarray, axis=axis, skipna=skipna)
        return self._wrap_reduction_result(axis, result)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py::TestnanopsDataFrame._skew_kurt_wrap [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/test_nanops.py]
    def _skew_kurt_wrap(self, values, axis=None, func=None):
        if not isinstance(values.dtype.type, np.floating):
            values = values.astype("f8")
        result = func(values, axis=axis, bias=False)
        return result

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py::ForwardWindowMethods.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/rolling.py]
    def setup(self, constructor, window_size, dtype, method):
        N = 10**5
        arr = np.random.random(N).astype(dtype)
        indexer = pd.api.indexers.FixedForwardWindowIndexer(window_size=window_size)
        self.roll = getattr(pd, constructor)(arr).rolling(window=indexer)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py::Series.skew [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/series.py]
    def skew(
        self,
        axis: Axis | None = 0,
        skipna: bool = True,
        numeric_only: bool = False,
        **kwargs,
    ):
        """
        Return unbiased skew over requested axis.

        Normalized by N-1.

        Parameters
        ----------
        axis : {index (0)}
            This parameter is unused and defaults to 0.
        skipna : bool, default True
            Exclude NA/null values when computing the result.
        numeric_only : bool, default False
            Unused.
        **kwargs
            Additional keyword arguments to be passed to the function.

        Returns
        -------
        scalar
            Unbiased skew of the Series.

        See Also
        --------

        Series.var : Return unbiased variance over requested axis.
        Series.std : Return unbiased standard deviation over requested axis.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3])
        >>> s.skew()
        0.0
        """
        return NDFrame.skew(
            self, axis=axis, skipna=skipna, numeric_only=numeric_only, **kwargs
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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py::ExpandingGroupby._get_window_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/expanding.py]
    def _get_window_indexer(self) -> GroupbyIndexer:
        """
        Return an indexer class that will compute the window start and end bounds

        Returns
        -------
        GroupbyIndexer
        """
        window_indexer = GroupbyIndexer(
            groupby_indices=self._grouper.indices,
            window_indexer=ExpandingIndexer,
        )
        return window_indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py::Window._center_window [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/rolling.py]
    def _center_window(self, result: np.ndarray, offset: int) -> np.ndarray:
        """
        Center the result in the window for weighted rolling aggregations.
        """
        if offset > 0:
            lead_indexer = [slice(offset, None)]
            result = np.copy(result[tuple(lead_indexer)])
        return result

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py::VariableOffsetWindowIndexer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexers/objects.py]
    def __init__(
        self,
        index_array: np.ndarray | None = None,
        window_size: int = 0,
        index: DatetimeIndex | None = None,
        offset: BaseOffset | None = None,
        **kwargs,
    ) -> None:
        super().__init__(index_array, window_size, **kwargs)
        if not isinstance(index, DatetimeIndex):
            raise ValueError("index must be a DatetimeIndex.")
        self.index = index
        if not isinstance(offset, BaseOffset):
            raise ValueError("offset must be a DateOffset-like object.")
        self.offset = offset

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py::ExponentialMovingWindowGroupby._get_window_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/window/ewm.py]
    def _get_window_indexer(self) -> GroupbyIndexer:
        """
        Return an indexer class that will compute the window start and end bounds

        Returns
        -------
        GroupbyIndexer
        """
        window_indexer = GroupbyIndexer(
            groupby_indices=self._grouper.indices,
            window_indexer=ExponentialMovingWindowIndexer,
        )
        return window_indexer

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py::TestDataFrameAnalytics.skewness [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/test_reductions.py]
        def skewness(x):
            if len(x) < 3:
                return np.nan
            return sp_stats.skew(x, bias=False)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py::_LocationIndexer._convert_to_indexer [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexing.py]
    def _convert_to_indexer(self, key, axis: AxisInt):
        raise AbstractMethodError(self)
```
