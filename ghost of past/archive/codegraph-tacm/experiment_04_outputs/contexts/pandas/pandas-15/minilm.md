# pandas-15 :: minilm

query: BUG: pickle after _with_freq (#33811)

## selected nodes

- rank=1 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=2 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=3 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::patch_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=4 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py
- rank=5 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_pickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=6 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py
- rank=7 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=8 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_clear_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=9 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py::TimedeltaProperties.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py
- rank=10 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=11 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py::round_trip_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py
- rank=12 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::write_legacy_pickles file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=13 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::mismatched_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py
- rank=14 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype.__setstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=15 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::loads file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=16 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::get_random_path file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=17 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PandasExtensionDtype.__getstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=18 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py::TestCustomBusinessDay._check_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
- rank=19 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::TestCommonCBM._check_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
- rank=20 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype.__setstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=21 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=22 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py
- rank=23 layer=FUNCTION tokens=315 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::_new_Index file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py
- rank=24 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.freqstr file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py
- rank=25 layer=FUNCTION tokens=768 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_pin_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py
- rank=26 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=27 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::InferFreq.time_infer_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py
- rank=28 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py::freq_sample file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py
- rank=29 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/errors/__init__.py::UndefinedVariableError.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/errors/__init__.py
- rank=30 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py::FloatArrayFormatter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py
- rank=31 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::_test_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=32 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLiteTable.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py
- rank=33 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=34 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::sqlite_conn_iris file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py
- rank=35 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.__len__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def peakmem_read_pickle(self):
        read_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def time_read_pickle(self):
        read_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::patch_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py]
def patch_pickle() -> Generator[None]:
    """
    Temporarily patch pickle to use our unpickler.
    """
    orig_loads = pickle.loads
    try:
        setattr(pickle, "loads", loads)
        yield
    finally:
        setattr(pickle, "loads", orig_loads)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py]
def pickle_respnder(df):
    with BytesIO() as bio:
        df.to_pickle(bio)
        return bio.getvalue()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_pickler [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py]
def python_pickler(obj, path):
    with open(path, "wb") as fh:
        pickle.dump(obj, fh, protocol=-1)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py]
    def freq(self):
        return self._freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def peakmem_write_pickle(self):
        self.df.to_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_clear_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _maybe_clear_freq(self) -> None:
        self._freq = None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py::TimedeltaProperties.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/accessors.py]
    def freq(self):
        return self._get_values().inferred_freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_write_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def time_write_pickle(self):
        self.df.to_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py::round_trip_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py]
def round_trip_pickle(obj: Any, tmp_path: Path) -> DataFrame | Series:
    """
    Pickle an object and then read it again.

    Parameters
    ----------
    obj : any object
        The object to pickle and then re-read.
    path : str, path object or file-like object, default None
        The path where the pickled object is written and then read.

    Returns
    -------
    pandas object
        The original object that was pickled and then re-read.
    """
    pd.to_pickle(obj, tmp_path)
    return pd.read_pickle(tmp_path)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::write_legacy_pickles [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py]
def write_legacy_pickles(output_dir):
    pth = f"{platform_name()}.pickle"

    with open(os.path.join(output_dir, pth), "wb") as fh:
        pickle.dump(create_pickle_data(test=False), fh, pickle.DEFAULT_PROTOCOL)

    print(f"created pickle file: {pth}")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py::mismatched_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/arithmetic/test_period.py]
def mismatched_freq(request):
    """
    Several timedelta-like and DateOffset instances that are _not_
    compatible with Monthly or Annual frequencies.
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype.__setstate__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def __setstate__(self, state) -> None:
        # for pickle compat. __get_state__ is defined in the
        # PandasExtensionDtype superclass and uses the public properties to
        # pickle -> need to set the settable private ones here (see GH26067)
        self._subtype = state["subtype"]

        # backward-compat older pickles won't have "closed" key
        self._closed = state.pop("closed", None)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::loads [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py]
def loads(
    bytes_object: bytes,
    *,
    fix_imports: bool = True,
    encoding: str = "ASCII",
    errors: str = "strict",
) -> Any:
    """
    Analogous to pickle._loads.
    """
    fd = io.BytesIO(bytes_object)
    return Unpickler(
        fd, fix_imports=fix_imports, encoding=encoding, errors=errors
    ).load()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::get_random_path [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py]
def get_random_path():
    return f"__{uuid.uuid4()}__.pickle"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PandasExtensionDtype.__getstate__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def __getstate__(self) -> dict[str_type, Any]:
        # pickle support; we don't want to pickle the cache
        return {k: getattr(self, k, None) for k in self._metadata}

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py::TestCustomBusinessDay._check_roundtrip [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py]
        def _check_roundtrip(obj):
            unpickled = tm.round_trip_pickle(obj, temp_file)
            assert unpickled == obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::TestCommonCBM._check_roundtrip [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py]
        def _check_roundtrip(obj):
            unpickled = tm.round_trip_pickle(obj, temp_file)
            assert unpickled == obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype.__setstate__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def __setstate__(self, state) -> None:
        # for pickle compat. __get_state__ is defined in the
        # PandasExtensionDtype superclass and uses the public properties to
        # pickle -> need to set the settable private ones here (see GH26067)
        self._tz = state["tz"]
        self._unit = state["unit"]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.setup [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def setup(self):
        self.fname = "__test__.pkl"
        N = 100000
        C = 5
        self.df = DataFrame(
            np.random.randn(N, C),
            columns=[f"float{i}" for i in range(C)],
            index=date_range("20000101", periods=N, freq="h"),
        )
        self.df["object"] = Index([f"i-{i}" for i in range(N)], dtype=object)
        self.df.to_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py::ArrowPeriodType.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/extension_types.py]
    def __init__(self, freq) -> None:
        # attributes need to be set first before calling
        # super init (as that calls serialize)
        self._freq = freq
        pyarrow.ExtensionType.__init__(self, pyarrow.int64(), "pandas.period")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py::_new_Index [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/base.py]
def _new_Index(cls: type[Index], d: dict) -> Index:
    """
    This is called upon unpickling, rather than the default which doesn't
    have arguments and breaks __new__.
    """
    # required for backward compat, because PI can't be instantiated with
    # ordinals through __new__ GH #13277
    d["copy"] = False
    if issubclass(cls, ABCPeriodIndex):
        from pandas.core.indexes.period import _new_PeriodIndex

        return _new_PeriodIndex(cls, **d)  # type: ignore[no-untyped-call]

    if issubclass(cls, ABCMultiIndex):
        if "labels" in d and "codes" not in d:
            # GH#23752 "labels" kwarg has been replaced with "codes"
            d["codes"] = d.pop("labels")

        # Since this was a valid MultiIndex at pickle-time, we don't need to
        #  check validty at un-pickle time.
        d["verify_integrity"] = False

    elif "dtype" not in d and "data" in d:
        # Prevent Index.__new__ from conducting inference;
        #  "data" key not in RangeIndex
        d["dtype"] = d["data"].dtype
    return cls.__new__(cls, **d)  # pyright: ignore[reportArgumentType]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py::PeriodArray.freqstr [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/period.py]
    def freqstr(self) -> str:
        return PeriodDtype(self.freq)._freqstr

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py::TimelikeOps._maybe_pin_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/datetimelike.py]
    def _maybe_pin_freq(self, freq, validate_kwds: dict) -> None:
        """
        Constructor helper to pin the appropriate `freq` attribute.  Assumes
        that self._freq is currently set to any freq inferred in
        _from_sequence_not_strict.
        """
        if freq is None:
            # user explicitly passed None -> override any inferred_freq
            self._freq = None
        elif freq == "infer":
            # if self._freq is *not* None then we already inferred a freq
            #  and there is nothing left to do
            if self._freq is None:
                # Set _freq directly to bypass duplicative _validate_frequency
                # check.
                self._freq = to_offset(self.inferred_freq)  # type: ignore[assignment]
        elif freq is lib.no_default:
            # user did not specify anything, keep inferred freq if the original
            #  data had one, otherwise do nothing
            pass
        elif self._freq is None:
            # We cannot inherit a freq from the data, so we need to validate
            #  the user-passed freq
            freq = to_offset(freq)
            type(self)._validate_frequency(self, freq, **validate_kwds)
            self._freq = freq
        else:
            # Otherwise we just need to check that the user-passed freq
            #  doesn't conflict with the one we already have.
            freq = to_offset(freq)
            if freq != self._freq:
                # GH#61086 freq may be equivalent but not equal (e.g.
                # QS-FEB vs QS-MAY), so validate against the actual data.
                if len(self) == 0:
                    pass
                elif len(self) == 1:
                    if not freq.is_on_offset(self[0]):
                        raise ValueError(
                            f"Inferred frequency {self._freq} from passed "
                            "values does not conform to passed frequency "
                            f"{freq.freqstr}"
                        )
                elif self[0] + freq == self[1]:
                    # For standard offsets, the step is a deterministic
                    # function of the date, so agreement on one step proves
                    # equivalence. For Custom/FY5253 offsets, external
                    # state (holidays, 52/53-week patterns) could cause
                    # later steps to diverge, so we validate fully.
                    if hasattr(freq, "_holidays") or isinstance(freq, FY5253Mixin):
                        type(self)._validate_frequency(self, freq, **validate_kwds)
                else:
                    raise ValueError(
                        f"Inferred frequency {self._freq} from passed "
                        "values does not conform to passed frequency "
                        f"{freq.freqstr}"
                    )
            self._freq = freq

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeIndexOpsMixin.freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def freq(self, value) -> None:
        # error: Property "freq" defined in "PeriodArray" is read-only  [misc]
        self._data.freq = value  # type: ignore[misc]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py::InferFreq.time_infer_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/timeseries.py]
    def time_infer_freq(self, freq):
        infer_freq(self.idx)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py::freq_sample [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/conftest.py]
def freq_sample(request):
    """
    Valid values for 'freq' parameter used to create date_range and
    timedelta_range..
    """
    return request.param

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/errors/__init__.py::UndefinedVariableError.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/errors/__init__.py]
    def __init__(self, name: str, is_local: bool | None = None) -> None:
        base_msg = f"{name!r} is not defined"
        if is_local:
            msg = f"local variable {base_msg}"
        else:
            msg = f"name {base_msg}"
        super().__init__(msg)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py::FloatArrayFormatter.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/formats/format.py]
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # float_format is expected to be a string
        # formatter should be used to pass a function
        if self.float_format is not None and self.formatter is None:
            # GH21625, GH22270
            self.fixed_width = False
            if callable(self.float_format):
                self.formatter = self.float_format
                self.float_format = None

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::_test_roundtrip [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py]
    def _test_roundtrip(frame, temp_file):
        unpickled = tm.round_trip_pickle(frame, temp_file)
        tm.assert_frame_equal(frame, unpickled)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::SQLiteTable.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py]
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._register_date_adapters()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _with_freq(self, freq):
        arr = self._data._with_freq(freq)
        return type(self)._simple_new(arr, name=self._name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py::sqlite_conn_iris [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_sql.py]
def sqlite_conn_iris(sqlite_engine_iris):
    with sqlite_engine_iris.connect() as conn:
        yield conn

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py::SequenceNotStr.__len__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_typing.py]
    def __len__(self) -> int: ...
```
