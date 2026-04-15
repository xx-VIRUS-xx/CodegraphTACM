# scrapy-2 :: minilm

query: Fix scrapy.utils.datatypes.LocalCache limit issue

## selected nodes

- rank=1 layer=FUNCTION tokens=226 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::AjaxCrawlMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
- rank=2 layer=FUNCTION tokens=508 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=3 layer=FUNCTION tokens=254 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/dupefilters.py::RFPDupeFilter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/dupefilters.py
- rank=4 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Slot.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=5 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py::__getattr__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py
- rank=6 layer=FUNCTION tokens=498 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::FilesPipeline.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py
- rank=7 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py::scrapy_components_versions file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py
- rank=8 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=9 layer=FUNCTION tokens=407 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::HTTP11DownloadHandler.download_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=10 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py
- rank=11 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py
- rank=12 layer=FUNCTION tokens=385 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.start_async file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py
- rank=13 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py
- rank=14 layer=FUNCTION tokens=305 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_download_warnsize_request_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=15 layer=FUNCTION tokens=542 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::AjaxCrawlMiddleware.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py]
    def __init__(self, settings: BaseSettings):
        if not settings.getbool("AJAXCRAWL_ENABLED"):
            raise NotConfigured

        warn(
            "scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware is deprecated"
            " and will be removed in a future Scrapy version.",
            ScrapyDeprecationWarning,
            stacklevel=2,
        )

        # XXX: Google parses at least first 100k bytes; scrapy's redirect
        # middleware parses first 4k. 4k turns out to be insufficient
        # for this middleware, and parsing 100k could be slow.
        # We use something in between (32K) by default.
        self.lookup_bytes: int = settings.getint("AJAXCRAWL_MAXSIZE")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def processProxyResponse(self, data: bytes) -> None:
        """Processes the response from the proxy. If the tunnel is successfully
        created, notifies the client that we are ready to send requests. If not
        raises a TunnelError.
        """
        assert self._protocol.transport
        self._connectBuffer += data
        # make sure that enough (all) bytes are consumed
        # and that we've got all HTTP headers (ending with a blank line)
        # from the proxy so that we don't send those bytes to the TLS layer
        #
        # see https://github.com/scrapy/scrapy/issues/2491
        if b"\r\n\r\n" not in self._connectBuffer:
            return
        self._protocol.dataReceived = self._protocolDataReceived  # type: ignore[method-assign]
        respm = TunnelingTCP4ClientEndpoint._responseMatcher.match(self._connectBuffer)
        if respm and int(respm.group("status")) == 200:
            # set proper Server Name Indication extension
            sslOptions = self._contextFactory.creatorForNetloc(  # type: ignore[call-arg,misc]
                self._tunneledHost, self._tunneledPort
            )
            self._protocol.transport.startTLS(sslOptions, self._protocolFactory)
            self._tunnelReadyDeferred.callback(self._protocol)
        else:
            extra: Any
            if respm:
                extra = {
                    "status": int(respm.group("status")),
                    "reason": respm.group("reason").strip(),
                }
            else:
                extra = data[: self._truncatedLength]
            self._tunnelReadyDeferred.errback(
                TunnelError(
                    "Could not open CONNECT tunnel with proxy "
                    f"{self._host}:{self._port} [{extra!r}]"
                )
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/dupefilters.py::RFPDupeFilter.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/dupefilters.py]
    def __init__(
        self,
        path: str | None = None,
        debug: bool = False,
        *,
        fingerprinter: RequestFingerprinterProtocol | None = None,
    ) -> None:
        self.file = None
        self.fingerprinter: RequestFingerprinterProtocol = (
            fingerprinter or RequestFingerprinter()
        )
        self.fingerprints: set[str] = set()
        self.logdupes = True
        self.debug = debug
        self.logger = logging.getLogger(__name__)
        if path:
            # line-by-line writing, see: https://github.com/scrapy/scrapy/issues/6019
            self.file = Path(path, "requests.seen").open(
                "a+", buffering=1, encoding="utf-8"
            )
            self.file.reconfigure(write_through=True)
            self.file.seek(0)
            self.fingerprints.update(x.rstrip() for x in self.file)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Slot.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py]
    def __init__(self, max_active_size: int = 5000000):
        self.max_active_size: int = max_active_size
        self.queue: deque[QueueTuple] = deque()
        self.active: set[Request] = set()
        self.active_size: int = 0
        self.itemproc_size: int = 0  # just for scrapy.utils.engine.get_engine_status()
        self.closing: Deferred[Spider] | None = None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py::__getattr__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py]
def __getattr__(name: str):
    if name == "CONCURRENT_REQUESTS_PER_IP":
        import warnings  # noqa: PLC0415

        from scrapy.exceptions import ScrapyDeprecationWarning  # noqa: PLC0415

        warnings.warn(
            "The scrapy.settings.default_settings.CONCURRENT_REQUESTS_PER_IP attribute is deprecated, use scrapy.settings.default_settings.CONCURRENT_REQUESTS_PER_DOMAIN instead.",
            ScrapyDeprecationWarning,
            stacklevel=2,
        )
        return 0

    raise AttributeError

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::FilesPipeline.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py]
    def __init__(
        self,
        store_uri: str | PathLike[str],
        download_func: None = None,
        *,
        crawler: Crawler,
    ):
        if download_func is not None:  # pragma: no cover
            warnings.warn(
                "The download_func argument of FilesPipeline.__init__() is ignored"
                " and will be removed in a future Scrapy version.",
                category=ScrapyDeprecationWarning,
                stacklevel=2,
            )

        if not (store_uri and (store_uri := _to_string(store_uri))):
            from scrapy.pipelines.images import ImagesPipeline  # noqa: PLC0415

            setting_name = (
                "IMAGES_STORE" if isinstance(self, ImagesPipeline) else "FILES_STORE"
            )
            raise NotConfigured(
                f"{setting_name} setting must be set to a valid path (not empty) "
                f"to enable {self.__class__.__name__}."
            )

        settings = crawler.settings
        cls_name = "FilesPipeline"
        self.store: FilesStoreProtocol = self._get_store(store_uri)
        resolve = functools.partial(
            self._key_for_pipe, base_class_name=cls_name, settings=settings
        )
        self.expires: int = settings.getint(resolve("FILES_EXPIRES"), self.EXPIRES)
        if not hasattr(self, "FILES_URLS_FIELD"):
            self.FILES_URLS_FIELD = self.DEFAULT_FILES_URLS_FIELD
        if not hasattr(self, "FILES_RESULT_FIELD"):
            self.FILES_RESULT_FIELD = self.DEFAULT_FILES_RESULT_FIELD
        self.files_urls_field: str = settings.get(
            resolve("FILES_URLS_FIELD"), self.FILES_URLS_FIELD
        )
        self.files_result_field: str = settings.get(
            resolve("FILES_RESULT_FIELD"), self.FILES_RESULT_FIELD
        )

        super().__init__(crawler=crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py::scrapy_components_versions [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py]
def scrapy_components_versions() -> list[tuple[str, str]]:  # pragma: no cover
    warn(
        (
            "scrapy.utils.versions.scrapy_components_versions() is deprecated, "
            "use scrapy.utils.versions.get_versions() instead."
        ),
        ScrapyDeprecationWarning,
        stacklevel=2,
    )
    return get_versions()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py]
    def __init__(self) -> None:
        self.classes: dict[str, type[Response]] = {}
        self.mimetypes: MimeTypes = MimeTypes()
        mimedata = get_data("scrapy", "mime.types")
        if not mimedata:
            raise ValueError(
                "The mime.types file is not found in the Scrapy installation"
            )
        self.mimetypes.readfp(StringIO(mimedata.decode("utf8")))
        for mimetype, cls in self.CLASSES.items():
            self.classes[mimetype] = load_object(cls)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::HTTP11DownloadHandler.download_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    async def download_request(self, request: Request) -> Response:
        """Return a deferred for the HTTP download"""
        if hasattr(self._crawler.spider, "download_maxsize"):  # pragma: no cover
            warn_on_deprecated_spider_attribute("download_maxsize", "DOWNLOAD_MAXSIZE")
        if hasattr(self._crawler.spider, "download_warnsize"):  # pragma: no cover
            warn_on_deprecated_spider_attribute(
                "download_warnsize", "DOWNLOAD_WARNSIZE"
            )

        agent = ScrapyAgent(
            contextFactory=self._contextFactory,
            bindAddress=self._bind_address,
            pool=self._pool,
            maxsize=getattr(
                self._crawler.spider, "download_maxsize", self._default_maxsize
            ),
            warnsize=getattr(
                self._crawler.spider, "download_warnsize", self._default_warnsize
            ),
            fail_on_dataloss=self._fail_on_dataloss,
            crawler=self._crawler,
            tls_verbose_logging=self._tls_verbose_logging,
        )
        try:
            with wrap_twisted_exceptions():
                return await maybe_deferred_to_future(agent.download_request(request))
        except ResponseDataLossError:
            if not self._fail_on_dataloss_warned:
                logger.warning(get_dataloss_msg(request.url))
                self._fail_on_dataloss_warned = True
            raise

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py]
    def parse(self, response):
        for _ in range(10):
            yield scrapy.Request(
                response.url, dont_filter=True, callback=self.ignore_response
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py]
    def parse(self, response):
        for _ in range(10):
            yield scrapy.Request(
                response.url, dont_filter=True, callback=self.ignore_response
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.start_async [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py]
    async def start_async(self, *, _start_request_processing: bool = True) -> None:
        """Start the execution engine.

        .. versionadded:: 2.14
        """
        if self._starting:
            raise RuntimeError("Engine already running")
        self.start_time = time()
        self._starting = True
        await self.signals.send_catch_log_async(signal=signals.engine_started)
        if self._stopping:
            # band-aid until https://github.com/scrapy/scrapy/issues/6916
            return
        if _start_request_processing and self.spider is None:
            # require an opened spider when not run in scrapy shell
            return
        self.running = True
        self._closewait = Deferred()
        if _start_request_processing:
            coro = self._start_request_processing()
            if is_asyncio_available():
                # not wrapping in a Deferred here to avoid https://github.com/twisted/twisted/issues/12470
                # (can happen when this is cancelled, e.g. in test_close_during_start_iteration())
                self._start_request_processing_awaitable = asyncio.ensure_future(coro)
            else:
                self._start_request_processing_awaitable = Deferred.fromCoroutine(coro)
        with contextlib.suppress(asyncio.exceptions.CancelledError):
            await maybe_deferred_to_future(self._closewait)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py]
    def __init__(self) -> None:
        self.settings: Settings | None = None  # set in scrapy.cmdline

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_download_warnsize_request_meta [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py]
    def _test_download_warnsize_request_meta(self, compression_id):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider("scrapytest.org")
        mw = HttpCompressionMiddleware.from_crawler(crawler)
        mw.open_spider(spider)
        response = self._getresponse(f"bomb-{compression_id}")
        response.meta["download_warnsize"] = 10_000_000

        with LogCapture(
            "scrapy.downloadermiddlewares.httpcompression",
            propagate=False,
            level=WARNING,
        ) as log:
            mw.process_response(response.request, response)
        log.check(
            (
                "scrapy.downloadermiddlewares.httpcompression",
                "WARNING",
                (
                    "<200 http://scrapytest.org/> body size after "
                    "decompression (11511612 B) is larger than the download "
                    "warning size (10000000 B)."
                ),
            ),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py]
    def __init__(self, request: Request, timeout: float = 180):
        warnings.warn(
            "ScrapyHTTPClientFactory is deprecated and will be removed in a future Scrapy version.",
            category=ScrapyDeprecationWarning,
            stacklevel=2,
        )

        self._url: str = urldefrag(request.url)[0]
        # converting to bytes to comply to Twisted interface
        self.url: bytes = to_bytes(self._url, encoding="ascii")
        self.method: bytes = to_bytes(request.method, encoding="ascii")
        self.body: bytes | None = request.body or None
        self.headers: Headers = Headers(request.headers)
        self.response_headers: Headers | None = None
        self.timeout: float = request.meta.get("download_timeout") or timeout
        self.start_time: float = time()
        self.deferred: defer.Deferred[Response] = defer.Deferred().addCallback(
            self._build_response, request
        )

        # Fixes Twisted 11.1.0+ support as HTTPClientFactory is expected
        # to have _disconnectedDeferred. See Twisted r32329.
        # As Scrapy implements it's own logic to handle redirects is not
        # needed to add the callback _waitForDisconnect.
        # Specifically this avoids the AttributeError exception when
        # clientConnectionFailed method is called.
        self._disconnectedDeferred: defer.Deferred[None] = defer.Deferred()

        self._set_connection_attributes(request)

        # set Host header based on url
        self.headers.setdefault("Host", self.netloc)

        # set Content-Length based len of body
        if self.body is not None:
            self.headers["Content-Length"] = len(self.body)
            # just in case a broken http/1.1 decides to keep connection alive
            self.headers.setdefault("Connection", "close")
        # Content-Length must be specified in POST method even with no body
        elif self.method == b"POST":
            self.headers["Content-Length"] = 0
```
