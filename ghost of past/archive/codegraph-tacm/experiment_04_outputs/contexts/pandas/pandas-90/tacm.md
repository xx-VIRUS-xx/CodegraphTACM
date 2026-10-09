# pandas-90 :: tacm

query: BUG: func 'to_pickle' and 'read_pickle' where not accepting URL GH#30163 (#30301)

## selected nodes

- rank=1 layer=FILE tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=2 layer=FILE tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=3 layer=FILE tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=4 layer=FILE tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=5 layer=FILE tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py
- rank=6 layer=FILE tokens=20 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/iceberg.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/iceberg.py
- rank=7 layer=FILE tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sas/sas_constants.py
- rank=8 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=9 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::Unpickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=10 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/datetimes/test_pickle.py
- rank=11 layer=CLASS tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py::TestCustomBusinessDay file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
- rank=12 layer=CLASS tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::TestProtocol file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=13 layer=CLASS tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/period/test_pickle.py
- rank=14 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/interval/test_pickle.py
- rank=15 layer=CLASS tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_pickle.py::TestPickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/timedeltas/test_pickle.py
- rank=16 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_any_index.py::TestRoundTrips file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/indexes/test_any_index.py
- rank=17 layer=CLASS tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::TestCompression file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=18 layer=CLASS tokens=273 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=19 layer=CLASS tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::MyTz file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=20 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py::DataFrame file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/interchange/dataframe_protocol.py
- rank=21 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_dtypes.py::Base file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/dtypes/test_dtypes.py
- rank=22 layer=CLASS tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::TestCommonCBM file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
- rank=23 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py::round_trip_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py
- rank=24 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=25 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=26 layer=FUNCTION tokens=18 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=27 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=28 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::patch_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=29 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::to_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=30 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=31 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=32 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py::TestCustomBusinessDay._check_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
- rank=33 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::TestCommonCBM._check_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
- rank=34 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.to_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=35 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::loads file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=36 layer=FUNCTION tokens=26 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py
- rank=37 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::write_legacy_pickles file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=38 layer=FUNCTION tokens=274 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::HDFStore.select_as_coordinates file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=39 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py::round_trip_pathlib file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py
- rank=40 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py::StringMethods.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/strings/accessor.py
- rank=41 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py::ListAccessor.len file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/arrays/arrow/accessors.py
- rank=42 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype.__setstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=43 layer=FUNCTION tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_set file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=44 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::Unpickler.load_reduce file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=45 layer=FUNCTION tokens=321 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::HDFStore.get file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=46 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PandasExtensionDtype.__getstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=47 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::CategoricalDtype.__setstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=48 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype.__setstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=49 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::create_pickle_data file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=50 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py::is_fsspec_url file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/common.py
- rank=51 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::get_random_path file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=52 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py::HDFStore.func file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pytables.py
- rank=53 layer=FUNCTION tokens=272 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py::TestDataFrameIndexingWhere._check_align file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/frame/indexing/test_where.py
- rank=54 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_unpickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py

## context

```text
file pandas/io/pickle.py
imports: __future__, pickle, typing, warnings, pandas
defines: to_pickle, read_pickle

file pandas/compat/pickle_compat.py
imports: __future__, contextlib, io, pickle, typing, numpy, pandas, collections
defines: Unpickler, loads, patch_pickle

file pandas/core/generic.py
imports: __future__, collections, copy, datetime, functools, json, operator, pickle
defines: NDFrame

file benchmarks/io/pickle.py
imports: numpy, pandas, pandas_vb_common
defines: Pickle

file pandas/_testing/_io.py
imports: __future__, gzip, io, tarfile, typing, zipfile, pandas, collections
defines: round_trip_pickle, round_trip_pathlib, write_to_compressed

file pandas/io/iceberg.py
imports: typing, pandas
defines: read_iceberg, to_iceberg

file io/sas/sas_constants.py
imports: __future__, typing
defines: SASIndex

class Pickle(BaseIO):  [benchmarks/io/pickle.py:13]
methods: peakmem_read_pickle, peakmem_write_pickle, setup
         time_read_pickle, time_write_pickle

class Unpickler(pickle._Unpickler):  [pandas/compat/pickle_compat.py:66]
methods: find_class, load_newobj, load_reduce

class TestPickle:  [indexes/datetimes/test_pickle.py:11]
methods: test_pickle, test_pickle_after_set_freq
         test_pickle_dont_infer_freq, test_pickle_unpickle
         test_roundtrip_pickle_with_tz

class TestCustomBusinessDay:  [tseries/offsets/test_custom_business_day.py:34]
methods: _check_roundtrip, test_calendar
         test_cbd_raises_if_calendar_not_busdaycalendar
         test_holidays, test_pickle_compat_0_14_1
         test_repr, test_roundtrip_pickle, test_weekmask
         test_weekmask_and_holidays

class TestProtocol:  [tests/io/test_pickle.py:420]
methods: test_read

class TestPickle:  [indexes/period/test_pickle.py:14]
methods: test_pickle_freq, test_pickle_round_trip

class TestPickle:  [indexes/interval/test_pickle.py:5]
methods: test_pickle_round_trip_closed

class TestPickle:  [indexes/timedeltas/test_pickle.py:5]
methods: test_pickle_after_set_freq

class TestRoundTrips:  [tests/indexes/test_any_index.py:104]
methods: test_pickle_preserves_name, test_pickle_roundtrip

class TestCompression:  [tests/io/test_pickle.py:284]
methods: compress_file, test_read_explicit, test_read_infer
         test_write_explicit, test_write_explicit_bad
         test_write_infer

class TestDataFrameIndexingWhere:  [frame/indexing/test_where.py:48]
methods: _check_align, _check_get, _check_set, create
         test_df_where_change_dtype
         test_df_where_with_category, test_where_align
         test_where_alignment, test_where_array_like
         test_where_axis, test_where_axis_multiple_dtypes
         test_where_axis_with_upcast, test_where_bug
         test_where_bug_mixed
         test_where_bug_transposition, test_where_callable
         test_where_categorical_filtering
         test_where_complex
         test_where_dataframe_col_match
         test_where_datetime, test_where_datetimelike_noop
         test_where_ea_other
         test_where_empty_df_and_empty_cond_having_non_bool_dtypes
         test_where_get
         test_where_interval_fullop_downcast
         test_where_interval_noop, test_where_invalid
         test_where_invalid_input_multiple
         test_where_invalid_input_single
         test_where_ndframe_align, test_where_none
         test_where_series_slicing, test_where_set
         test_where_tz_values, test_where_upcasting

class MyTz(datetime.tzinfo):  [tests/io/test_pickle.py:462]
methods: __init__

class DataFrame(ABC):  [core/interchange/dataframe_protocol.py:368]
methods: column_names, get_chunks, get_column, get_column_by_name
         get_columns, metadata, num_chunks, num_columns
         num_rows, select_columns, select_columns_by_name
         __dataframe__

class Base:  [tests/dtypes/test_dtypes.py:45]
methods: test_equality_invalid, test_hash, test_numpy_informed
         test_pickle

class TestCommonCBM:  [tseries/offsets/test_custom_business_month.py:39]
methods: _check_roundtrip, test_copy, test_eq, test_hash
         test_roundtrip_pickle

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

    def peakmem_read_pickle(self):
        read_pickle(self.fname)

    def time_read_pickle(self):
        read_pickle(self.fname)

    def peakmem_write_pickle(self):
        self.df.to_pickle(self.fname)

    def time_write_pickle(self):
        self.df.to_pickle(self.fname)

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

def to_pickle(
    obj: Any,
    filepath_or_buffer: FilePath | WriteBuffer[bytes],
    compression: CompressionOptions = "infer",
    protocol: int = pickle.HIGHEST_PROTOCOL,
    storage_options: StorageOptions | None = None,
) -> None:
    """
    # ... truncated

def read_pickle(
    filepath_or_buffer: FilePath | ReadPickleBuffer,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,
) -> DataFrame | Series:
    """
    # ... truncated

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

        def _check_roundtrip(obj):
            unpickled = tm.round_trip_pickle(obj, temp_file)
            assert unpickled == obj

        def _check_roundtrip(obj):
            unpickled = tm.round_trip_pickle(obj, temp_file)
            assert unpickled == obj

    def to_pickle(
        self,
        path: FilePath | WriteBuffer[bytes],
        *,
        compression: CompressionOptions = "infer",
        protocol: int = pickle.HIGHEST_PROTOCOL,
        storage_options: StorageOptions | None = None,
    ) -> None:
        """
    # ... truncated

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

def pickle_respnder(df):
    with BytesIO() as bio:
        df.to_pickle(bio)
        return bio.getvalue()

def write_legacy_pickles(output_dir):
    pth = f"{platform_name()}.pickle"

    with open(os.path.join(output_dir, pth), "wb") as fh:
        pickle.dump(create_pickle_data(test=False), fh, pickle.DEFAULT_PROTOCOL)

    print(f"created pickle file: {pth}")

    def select_as_coordinates(
        self,
        key: str,
        where=None,
        start: int | None = None,
        stop: int | None = None,
    ):
        """
        return the selection as an Index

        .. warning::

           Pandas uses PyTables for reading and writing HDF5 files, which allows
           serializing object-dtype data with pickle when using the "fixed" format.
           Loading pickled data received from untrusted sources can be unsafe.

           See: https://docs.python.org/3/library/pickle.html for more.


        Parameters
        ----------
        key : str
        where : list of Term (or convertible) objects, optional
        start : integer (defaults to None), row number to start selection
        stop  : integer (defaults to None), row number to stop selection
        """
        where = _ensure_term(where, scope_level=1)
        tbl = self.get_storer(key)
        if not isinstance(tbl, Table):
            raise TypeError("can only read_coordinates with a table")
        return tbl.read_coordinates(where=where, start=start, stop=stop)

def round_trip_pathlib(writer, reader, tmp_path: Path):
    """
    Write an object to file specified by a pathlib.Path and read it back

    Parameters
    ----------
    writer : callable bound to pandas object
        IO writing function (e.g. DataFrame.to_csv )
    reader : callable
        IO reading function (e.g. pd.read_csv )
    path : str, default None
        The path where the object is written and then read.

    Returns
    -------
    pandas object
        The original object that was serialized and then re-read.
    """
    writer(tmp_path)
    obj = reader(tmp_path)
    return obj

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

    def __setstate__(self, state) -> None:
        # for pickle compat. __get_state__ is defined in the
        # PandasExtensionDtype superclass and uses the public properties to
        # pickle -> need to set the settable private ones here (see GH26067)
        self._tz = state["tz"]
        self._unit = state["unit"]

        def _check_set(df, cond, check_dtypes=True):
            dfi = df.copy()
            econd = cond.reindex_like(df).fillna(True).infer_objects()
            expected = dfi.mask(~econd)

            result = dfi.where(cond, np.nan, inplace=True)
            assert result is dfi
            tm.assert_frame_equal(dfi, expected)

            # dtypes (and confirm upcasts)x
            if check_dtypes:
                for k, v in df.dtypes.items():
                    if issubclass(v.type, np.integer) and not cond[k].all():
                        v = np.dtype("float64")
                    assert dfi[k].dtype == v

    def load_reduce(self) -> None:
        stack = self.stack  # type: ignore[attr-defined]
        args = stack.pop()
        func = stack[-1]

        try:
            stack[-1] = func(*args)
        except TypeError:
            # If we have a deprecated function,
            # try to replace and try again.
            if args and isinstance(args[0], type) and issubclass(args[0], BaseOffset):
                # TypeError: object.__new__(Day) is not safe, use Day.__new__()
                cls = args[0]
                stack[-1] = cls.__new__(*args)
                return
            elif args and issubclass(args[0], PeriodArray):
                cls = args[0]
                stack[-1] = NDArrayBacked.__new__(*args)
                return
            raise

    def get(self, key: str):
        """
        Retrieve pandas object stored in file.

        The object is read from the HDF5 file and returned as the
        same type that was stored (e.g., DataFrame, Series).

        Parameters
        ----------
        key : str
            Object to retrieve from file. Raises KeyError if not found.

        Returns
        -------
        object
            Same type as object stored in file.

        See Also
        --------
        HDFStore.get_node : Returns the node with the key.
        HDFStore.get_storer : Returns the storer object for a key.

        Examples
        --------
        >>> df = pd.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])
        >>> store = pd.HDFStore("store.h5", "w")  # doctest: +SKIP
        >>> store.put("data", df)  # doctest: +SKIP
        >>> store.get("data")  # doctest: +SKIP
        >>> store.close()  # doctest: +SKIP
        """
        with patch_pickle():
            # GH#31167 Without this patch, pickle doesn't know how to unpickle
            #  old DateOffset objects now that they are cdef classes.
            group = self.get_node(key)
            if group is None:
                raise KeyError(f"No object named {key} in the file")
            return self._read_group(group)

    def __getstate__(self) -> dict[str_type, Any]:
        # pickle support; we don't want to pickle the cache
        return {k: getattr(self, k, None) for k in self._metadata}

    def __setstate__(self, state: MutableMapping[str_type, Any]) -> None:
        # for pickle compat. __get_state__ is defined in the
        # PandasExtensionDtype superclass and uses the public properties to
        # pickle -> need to set the settable private ones here (see GH26067)
        self._categories = state.pop("categories", None)
        self._ordered = state.pop("ordered", False)

    def __setstate__(self, state) -> None:
        # for pickle compat. __get_state__ is defined in the
        # PandasExtensionDtype superclass and uses the public properties to
        # pickle -> need to set the settable private ones here (see GH26067)
        self._subtype = state["subtype"]

        # backward-compat older pickles won't have "closed" key
        self._closed = state.pop("closed", None)

def create_pickle_data(test: bool = True):
    """create the pickle data"""
    data = {
        "A": [0.0, 1.0, 2.0, 3.0, np.nan],
        "B": [0, 1, 0, 1, 0],
        "C": ["foo1", "foo2", "foo3", "foo4", "foo5"],
        "D": date_range("1/1/2009", periods=5),
        "E": [0.0, 1, Timestamp("20100101"), "foo", 2.0],
    }

    scalars = {"timestamp": Timestamp("20130101"), "period": Period("2012", "M")}

    # ... truncated

def is_fsspec_url(url: FilePath | BaseBuffer) -> bool:
    """
    Returns true if the given URL looks like
    something fsspec can handle
    """
    return (
        isinstance(url, str)
        and bool(_FSSPEC_URL_PATTERN.match(url))
        and not url.startswith(("http://", "https://"))
    )

def get_random_path():
    return f"__{uuid.uuid4()}__.pickle"

        def func(_start, _stop, _where):
            # retrieve the objs, _where is always passed as a set of
            # coordinates here
            objs = [
                t.read(where=_where, columns=columns, start=_start, stop=_stop)
                for t in tbls
            ]

            # concat and return
            return concat(objs, axis=axis, verify_integrity=False)._consolidate()

        def _check_align(df, cond, other, check_dtypes=True):
            rs = df.where(cond, other)
            for i, k in enumerate(rs.columns):
                result = rs[k]
                d = df[k].values
                c = cond[k].reindex(df[k].index).fillna(False).values

                if is_scalar(other):
                    o = other
                elif isinstance(other, np.ndarray):
                    o = Series(other[:, i], index=result.index).values
                else:
                    o = other[k].values

                new_values = d if c.all() else np.where(c, d, o)
                expected = Series(new_values, index=result.index, name=k)

                # since we can't always have the correct numpy dtype
                # as numpy doesn't know how to downcast, don't check
                tm.assert_series_equal(result, expected, check_dtype=False)

            # dtypes
            # can't check dtype when other is an ndarray

            if check_dtypes and not isinstance(other, np.ndarray):
                assert (rs.dtypes == df.dtypes).all()

def python_unpickler(path):
    with open(path, "rb") as fh:
        fh.seek(0)
        return pickle.load(fh)
```
