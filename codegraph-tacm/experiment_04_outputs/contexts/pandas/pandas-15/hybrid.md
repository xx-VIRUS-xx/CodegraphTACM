# pandas-15 :: hybrid

query: BUG: pickle after _with_freq (#33811)

## selected nodes

- rank=1 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py
- rank=2 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py::patch_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/compat/pickle_compat.py
- rank=3 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=4 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=5 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_pickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=6 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::write_legacy_pickles file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py
- rank=7 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=8 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_write_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=9 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py::round_trip_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/_testing/_io.py
- rank=10 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PandasExtensionDtype.__getstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=11 layer=FUNCTION tokens=140 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.setup file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py
- rank=12 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype.__setstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=13 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::get_random_path file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=14 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype.__setstate__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py
- rank=15 layer=FUNCTION tokens=1233 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::read_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py
- rank=16 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_unpickler file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py
- rank=17 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py::TestCustomBusinessDay._check_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
- rank=18 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::TestCommonCBM._check_roundtrip file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
- rank=19 layer=FUNCTION tokens=1056 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.to_pickle file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py
- rank=20 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py
- rank=21 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::PandasSQL.__exit__ file=/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py::pickle_respnder [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_http_headers.py]
def pickle_respnder(df):
    with BytesIO() as bio:
        df.to_pickle(bio)
        return bio.getvalue()

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_read_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def peakmem_read_pickle(self):
        read_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.time_read_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def time_read_pickle(self):
        read_pickle(self.fname)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_pickler [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py]
def python_pickler(obj, path):
    with open(path, "wb") as fh:
        pickle.dump(obj, fh, protocol=-1)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py::write_legacy_pickles [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/generate_legacy_storage_files.py]
def write_legacy_pickles(output_dir):
    pth = f"{platform_name()}.pickle"

    with open(os.path.join(output_dir, pth), "wb") as fh:
        pickle.dump(create_pickle_data(test=False), fh, pickle.DEFAULT_PROTOCOL)

    print(f"created pickle file: {pth}")

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py::Pickle.peakmem_write_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/asv_bench/benchmarks/io/pickle.py]
    def peakmem_write_pickle(self):
        self.df.to_pickle(self.fname)

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::PandasExtensionDtype.__getstate__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def __getstate__(self) -> dict[str_type, Any]:
        # pickle support; we don't want to pickle the cache
        return {k: getattr(self, k, None) for k in self._metadata}

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

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::IntervalDtype.__setstate__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def __setstate__(self, state) -> None:
        # for pickle compat. __get_state__ is defined in the
        # PandasExtensionDtype superclass and uses the public properties to
        # pickle -> need to set the settable private ones here (see GH26067)
        self._subtype = state["subtype"]

        # backward-compat older pickles won't have "closed" key
        self._closed = state.pop("closed", None)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::get_random_path [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py]
def get_random_path():
    return f"__{uuid.uuid4()}__.pickle"

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py::DatetimeTZDtype.__setstate__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/dtypes/dtypes.py]
    def __setstate__(self, state) -> None:
        # for pickle compat. __get_state__ is defined in the
        # PandasExtensionDtype superclass and uses the public properties to
        # pickle -> need to set the settable private ones here (see GH26067)
        self._tz = state["tz"]
        self._unit = state["unit"]

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py::read_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/pickle.py]
def read_pickle(
    filepath_or_buffer: FilePath | ReadPickleBuffer,
    compression: CompressionOptions = "infer",
    storage_options: StorageOptions | None = None,
) -> DataFrame | Series:
    """
    Load pickled pandas object (or any object) from file and return unpickled object.

    .. warning::

       Loading pickled data received from untrusted sources can be
       unsafe. See `here <https://docs.python.org/3/library/pickle.html>`__.

    Parameters
    ----------
    filepath_or_buffer : str, path object, or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``readlines()`` function.
        Also accepts URL. URL is not limited to S3 and GCS.

        Certain URL schemes may require additional packages. For example, S3
        URLs require the ``s3fs`` library. See
        :ref:`install.optional_dependencies` for a full list.
    compression : str or dict, default 'infer'
        For on-the-fly decompression of on-disk data. If 'infer' and
        'filepath_or_buffer' is path-like, then detect compression from the
        following extensions: '.gz', '.bz2', '.zip', '.xz', '.zst', '.tar',
        '.tar.gz', '.tar.xz' or '.tar.bz2' (otherwise no compression).
        If using 'zip' or 'tar', the ZIP file must contain only one data file
        to be read in.
        Set to ``None`` for no decompression.
        Can also be a dict with key ``'method'`` set
        to one of {``'zip'``, ``'gzip'``, ``'bz2'``, ``'zstd'``, ``'xz'``,
        ``'tar'``} and other key-value pairs are forwarded to
        ``zipfile.ZipFile``, ``gzip.GzipFile``,
        ``bz2.BZ2File``, ``zstandard.ZstdDecompressor``, ``lzma.LZMAFile`` or
        ``tarfile.TarFile``, respectively.
        As an example, the following could be passed for Zstandard decompression
        using a custom compression dictionary:
        ``compression={'method': 'zstd', 'dict_data': my_compression_dict}``.
    storage_options : dict, optional
        Extra options that make sense for a particular storage connection, e.g.
        host, port, username, password, etc. For HTTP(S) URLs the key-value pairs
        are forwarded to ``urllib.request.Request`` as header options. For other
        URLs (e.g. starting with "s3://", and "gcs://") the key-value pairs are
        forwarded to ``fsspec.open``. Please see ``fsspec`` and ``urllib`` for more
        details, and for more examples on storage options refer `here
        <https://pandas.pydata.org/docs/user_guide/io.html?
        highlight=storage_options#reading-writing-remote-files>`_.

    Returns
    -------
    object
        The unpickled pandas object (or any object) that was stored in file.

    See Also
    --------
    DataFrame.to_pickle : Pickle (serialize) DataFrame object to file.
    Series.to_pickle : Pickle (serialize) Series object to file.
    read_hdf : Read HDF5 file into a DataFrame.
    read_sql : Read SQL query or database table into a DataFrame.
    read_parquet : Load a parquet object, returning a DataFrame.

    Notes
    -----
    read_pickle is only guaranteed to be backwards compatible to pandas 1.0
    provided the object was serialized with to_pickle.

    Examples
    --------
    >>> original_df = pd.DataFrame(
    ...     {"foo": range(5), "bar": range(5, 10)}
    ... )  # doctest: +SKIP
    >>> original_df  # doctest: +SKIP
       foo  bar
    0    0    5
    1    1    6
    2    2    7
    3    3    8
    4    4    9
    >>> pd.to_pickle(original_df, "./dummy.pkl")  # doctest: +SKIP

    >>> unpickled_df = pd.read_pickle("./dummy.pkl")  # doctest: +SKIP
    >>> unpickled_df  # doctest: +SKIP
       foo  bar
    0    0    5
    1    1    6
    2    2    7
    3    3    8
    4    4    9
    """
    # TypeError for Cython complaints about object.__new__ vs Tick.__new__
    excs_to_catch = (AttributeError, ImportError, ModuleNotFoundError, TypeError)
    with get_handle(
        filepath_or_buffer,
        "rb",
        compression=compression,
        is_text=False,
        storage_options=storage_options,
    ) as handles:
        # 1) try standard library Pickle
        # 2) try pickle_compat (older pandas version) to handle subclass changes
        try:
            with warnings.catch_warnings(record=True):
                # We want to silence any warnings about, e.g. moved modules.
                warnings.simplefilter("ignore", Warning)
                return pickle.load(handles.handle)
        except excs_to_catch:
            # e.g.
            #  "No module named 'pandas.core.sparse.series'"
            #  "Can't get attribute '_nat_unpickle' on <module 'pandas._libs.tslib"
            handles.handle.seek(0)
            return pickle_compat.Unpickler(handles.handle).load()

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py::python_unpickler [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/io/test_pickle.py]
def python_unpickler(path):
    with open(path, "rb") as fh:
        fh.seek(0)
        return pickle.load(fh)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py::TestCustomBusinessDay._check_roundtrip [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py]
        def _check_roundtrip(obj):
            unpickled = tm.round_trip_pickle(obj, temp_file)
            assert unpickled == obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py::TestCommonCBM._check_roundtrip [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py]
        def _check_roundtrip(obj):
            unpickled = tm.round_trip_pickle(obj, temp_file)
            assert unpickled == obj

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py::NDFrame.to_pickle [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/generic.py]
    def to_pickle(
        self,
        path: FilePath | WriteBuffer[bytes],
        *,
        compression: CompressionOptions = "infer",
        protocol: int = pickle.HIGHEST_PROTOCOL,
        storage_options: StorageOptions | None = None,
    ) -> None:
        """
        Pickle (serialize) object to file.

        Uses Python's ``pickle`` module to serialize the object and write
        it to the specified file path. The resulting file can be loaded
        back using :func:`pandas.read_pickle`.

        Parameters
        ----------
        path : str, path object, or file-like object
            String, path object (implementing ``os.PathLike[str]``), or file-like
            object implementing a binary ``write()`` function. File path where
            the pickled object will be stored.

        compression : str or dict, default 'infer'
            For on-the-fly compression of the output data. If 'infer' and
            'path_or_buf' is path-like, then detect compression from the following
            extensions: '.gz',
            '.bz2', '.zip', '.xz', '.zst', '.tar', '.tar.gz', '.tar.xz' or '.tar.bz2'
            (otherwise no compression).
            Set to ``None`` for no compression.
            Can also be a dict with key ``'method'`` set to one of
            {``'zip'``, ``'gzip'``, ``'bz2'``, ``'zstd'``, ``'xz'``, ``'tar'``} and
            other key-value pairs are forwarded to
            ``zipfile.ZipFile``, ``gzip.GzipFile``,
            ``bz2.BZ2File``, ``zstandard.ZstdCompressor``, ``lzma.LZMAFile`` or
            ``tarfile.TarFile``, respectively.
            As an example, the following could be passed for faster compression and
            to create a reproducible gzip archive:
            ``compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1}``.

        protocol : int
            Int which indicates which protocol should be used by the pickler,
            default HIGHEST_PROTOCOL (see [1]_ paragraph 12.1.2). The possible
            values are 0, 1, 2, 3, 4, 5. A negative value for the protocol
            parameter is equivalent to setting its value to HIGHEST_PROTOCOL.

            .. [1] https://docs.python.org/3/library/pickle.html.

        storage_options : dict, optional
            Extra options that make sense for a particular storage connection, e.g.
            host, port, username, password, etc. For HTTP(S) URLs the key-value pairs
            are forwarded to ``urllib.request.Request`` as header options. For other
            URLs (e.g. starting with "s3://", and "gcs://") the key-value pairs are
            forwarded to ``fsspec.open``. Please see ``fsspec`` and ``urllib`` for more
            details, and for more examples on storage options refer `here
            <https://pandas.pydata.org/docs/user_guide/io.html?
            highlight=storage_options#reading-writing-remote-files>`_.

        See Also
        --------
        read_pickle : Load pickled pandas object (or any object) from file.
        DataFrame.to_hdf : Write DataFrame to an HDF5 file.
        DataFrame.to_sql : Write DataFrame to a SQL database.
        DataFrame.to_parquet : Write a DataFrame to the binary parquet format.

        Examples
        --------
        >>> original_df = pd.DataFrame(
        ...     {"foo": range(5), "bar": range(5, 10)}
        ... )  # doctest: +SKIP
        >>> original_df  # doctest: +SKIP
           foo  bar
        0    0    5
        1    1    6
        2    2    7
        3    3    8
        4    4    9
        >>> original_df.to_pickle("./dummy.pkl")  # doctest: +SKIP

        >>> unpickled_df = pd.read_pickle("./dummy.pkl")  # doctest: +SKIP
        >>> unpickled_df  # doctest: +SKIP
           foo  bar
        0    0    5
        1    1    6
        2    2    7
        3    3    8
        4    4    9
        """
        from pandas.io.pickle import to_pickle

        to_pickle(
            self,
            path,
            compression=compression,
            protocol=protocol,
            storage_options=storage_options,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py::DatetimeTimedeltaMixin._with_freq [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/core/indexes/datetimelike.py]
    def _with_freq(self, freq):
        arr = self._data._with_freq(freq)
        return type(self)._simple_new(arr, name=self._name)

# /Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py::PandasSQL.__exit__ [/Users/xxvirusxx/PY/CodegraphTACM/pandas/pandas/io/sql.py]
    def __exit__(self, *args) -> None:
        pass
```
