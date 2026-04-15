# scrapy-15 :: tacm-full

query: Do not fail on canonicalizing URLs with wrong netlocs

## selected nodes

- rank=1 layer=FUNCTION tokens=407 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::HTTP11DownloadHandler.download_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=2 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._log_dataloss_warning file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=3 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::BaseHttpDownloadHandler.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py
- rank=4 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py::OffsiteMiddleware.should_follow file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py
- rank=5 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=6 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py::TestHeadersReceivedEngine._assert_visited_urls file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py
- rank=7 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=8 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=9 layer=FUNCTION tokens=212 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::defer_fail file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=10 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exporters.py::BaseItemExporter._configure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exporters.py
- rank=11 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_visited_urls file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py
- rank=12 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::FilesPipeline.get_media_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py
- rank=13 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py::ImagesPipeline.get_media_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py
- rank=14 layer=FUNCTION tokens=277 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=15 layer=FUNCTION tokens=284 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::_ResponseReader.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=16 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::RecoverySpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=17 layer=FUNCTION tokens=590 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py::RefererMiddleware.policy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py
- rank=18 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_files.py::_create_item_with_files file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_files.py
- rank=19 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.syntax file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py
- rank=20 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exporters.py::PythonItemExporter._configure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exporters.py
- rank=21 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_left.py::SignalCatcherSpider.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_left.py
- rank=22 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exceptions.py::StopDownload.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exceptions.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._log_dataloss_warning [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py]
    def _log_dataloss_warning(self, url: str) -> None:
        if self._fail_on_dataloss_warned:
            return
        logger.warning(get_dataloss_msg(url))
        self._fail_on_dataloss_warned = True

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::BaseHttpDownloadHandler.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py]
    def __init__(self, crawler: Crawler):
        super().__init__(crawler)
        self._default_maxsize: int = crawler.settings.getint("DOWNLOAD_MAXSIZE")
        self._default_warnsize: int = crawler.settings.getint("DOWNLOAD_WARNSIZE")
        self._fail_on_dataloss: bool = crawler.settings.getbool(
            "DOWNLOAD_FAIL_ON_DATALOSS"
        )
        self._tls_verbose_logging: bool = crawler.settings.getbool(
            "DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING"
        )
        self._fail_on_dataloss_warned: bool = False

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py::OffsiteMiddleware.should_follow [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py]
    def should_follow(self, request: Request, spider: Spider) -> bool:
        regex = self.host_regex
        # hostname can be None for wrong urls (like javascript links)
        host = urlparse_cached(request).hostname or ""
        return bool(regex.search(host))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
def _wrong_credentials(proxy_url):
    bad_auth_proxy = list(urlsplit(proxy_url))
    bad_auth_proxy[1] = bad_auth_proxy[1].replace("scrapy:scrapy@", "wrong:wronger@")
    return urlunsplit(bad_auth_proxy)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py::TestHeadersReceivedEngine._assert_visited_urls [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py]
    def _assert_visited_urls(run: CrawlerRun) -> None:
        must_be_visited = ["/static/", "/redirect", "/redirected"]
        urls_visited = {rp[0].url for rp in run.respplug}
        urls_expected = {run.geturl(p) for p in must_be_visited}
        assert urls_expected <= urls_visited, (
            f"URLs not visited: {list(urls_expected - urls_visited)}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
    async def start(self):
        for url in self.start_urls:
            yield Request(url, self.parse, errback=self.on_error)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
    def get(self, name: _SettingsKey, default: Any = None) -> Any:
        """
        Get a setting value without affecting its original type.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
        if name == "CONCURRENT_REQUESTS_PER_IP" and (
            isinstance(self[name], int) and self[name] != 0
        ):
            warnings.warn(
                "The CONCURRENT_REQUESTS_PER_IP setting is deprecated, use CONCURRENT_REQUESTS_PER_DOMAIN instead.",
                ScrapyDeprecationWarning,
                stacklevel=2,
            )

        if name == "DNS_RESOLVER":
            warnings.warn(
                "The DNS_RESOLVER setting is deprecated, please use "
                "TWISTED_DNS_RESOLVER instead.",
                ScrapyDeprecationWarning,
                stacklevel=2,
            )

        return self[name] if self[name] is not None else default

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::defer_fail [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py]
def defer_fail(_failure: Failure) -> Deferred[Any]:  # pragma: no cover
    """Same as twisted.internet.defer.fail but delay calling errback until
    next reactor loop

    It delays by 100ms so reactor has a chance to go through readers and writers
    before attending pending delayed calls, so do not set delay to zero.
    """
    warnings.warn(
        "scrapy.utils.defer.defer_fail() is deprecated, use"
        " twisted.internet.defer.fail(), plus an explicit sleep if needed.",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )

    from twisted.internet import reactor

    d: Deferred[Any] = Deferred()
    reactor.callLater(_DEFER_DELAY, d.errback, _failure)
    return d

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exporters.py::BaseItemExporter._configure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exporters.py]
    def _configure(self, options: dict[str, Any], dont_fail: bool = False) -> None:
        """Configure the exporter by popping options from the ``options`` dict.
        If dont_fail is set, it won't raise an exception on unexpected options
        (useful for using with keyword arguments in subclasses ``__init__`` methods)
        """
        self.encoding: str | None = options.pop("encoding", None)
        self.fields_to_export: Mapping[str, str] | Iterable[str] | None = options.pop(
            "fields_to_export", None
        )
        self.export_empty_fields: bool = options.pop("export_empty_fields", False)
        self.indent: int | None = options.pop("indent", None)
        if not dont_fail and options:
            raise TypeError(f"Unexpected options: {', '.join(options.keys())}")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_visited_urls [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py]
    def _assert_visited_urls(run: CrawlerRun) -> None:
        must_be_visited = [
            "/static/",
            "/redirect",
            "/redirected",
            "/static/item1.html",
            "/static/item2.html",
            "/static/item999.html",
        ]
        urls_visited = {rp[0].url for rp in run.respplug}
        urls_expected = {run.geturl(p) for p in must_be_visited}
        assert urls_expected <= urls_visited, (
            f"URLs not visited: {list(urls_expected - urls_visited)}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::FilesPipeline.get_media_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py]
    def get_media_requests(
        self, item: Any, info: MediaPipeline.SpiderInfo
    ) -> list[Request]:
        urls = ItemAdapter(item).get(self.files_urls_field, [])
        if not isinstance(urls, list):
            raise TypeError(
                f"{self.files_urls_field} must be a list of URLs, got {type(urls).__name__}. "
            )
        return [Request(u, callback=NO_CALLBACK) for u in urls]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py::ImagesPipeline.get_media_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py]
    def get_media_requests(
        self, item: Any, info: MediaPipeline.SpiderInfo
    ) -> list[Request]:
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        if not isinstance(urls, list):
            raise TypeError(
                f"{self.images_urls_field} must be a list of URLs, got {type(urls).__name__}. "
            )
        return [Request(u, callback=NO_CALLBACK) for u in urls]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def __init__(
        self,
        *,
        contextFactory: IPolicyForHTTPS,
        connectTimeout: float = 10,
        bindAddress: str | tuple[str, int] | None = None,
        pool: HTTPConnectionPool | None = None,
        maxsize: int = 0,
        warnsize: int = 0,
        fail_on_dataloss: bool = True,
        crawler: Crawler,
        tls_verbose_logging: bool = False,
    ):
        self._contextFactory: IPolicyForHTTPS = contextFactory
        self._connectTimeout: float = connectTimeout
        self._bindAddress: str | tuple[str, int] | None = bindAddress
        self._pool: HTTPConnectionPool | None = pool
        self._maxsize: int = maxsize
        self._warnsize: int = warnsize
        self._fail_on_dataloss: bool = fail_on_dataloss
        self._txresponse: TxResponse | None = None
        self._crawler: Crawler = crawler
        self._tls_verbose_logging: bool = tls_verbose_logging

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::_ResponseReader.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def __init__(
        self,
        finished: Deferred[_ResultT],
        txresponse: TxResponse,
        request: Request,
        maxsize: int,
        warnsize: int,
        fail_on_dataloss: bool,
        crawler: Crawler,
        *,
        tls_verbose_logging: bool = False,
    ):
        self._finished: Deferred[_ResultT] = finished
        self._txresponse: TxResponse = txresponse
        self._request: Request = request
        self._bodybuf: BytesIO = BytesIO()
        self._maxsize: int = maxsize
        self._warnsize: int = warnsize
        self._fail_on_dataloss: bool = fail_on_dataloss
        self._reached_warnsize: bool = False
        self._bytes_received: int = 0
        self._certificate: ssl.Certificate | None = None
        self._ip_address: ipaddress.IPv4Address | ipaddress.IPv6Address | None = None
        self._crawler: Crawler = crawler
        self._tls_verbose_logging: bool = tls_verbose_logging

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::RecoverySpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py]
    def parse(self, response):
        yield {"test": 1}
        self.logger.info("DONT_FAIL: %s", response.meta.get("dont_fail"))
        if not response.meta.get("dont_fail"):
            raise TabError

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py::RefererMiddleware.policy [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py]
    def policy(
        self,
        response: Response | str | None = None,
        request: Request | None = None,
        **kwargs: Unpack[_PolicyKwargs],
    ) -> ReferrerPolicy:
        """Return the referrer policy to use for *request* based on *request*
        meta, *response* and settings.

        - if a valid policy is set in Request meta, it is used.
        - if the policy is set in meta but is wrong (e.g. a typo error), the
          policy from settings is used
        - if the policy is not set in Request meta, but there is a
          Referrer-Policy header in the parent response, it is used if valid
        - otherwise, the policy from settings is used.
        """
        if "resp_or_url" in kwargs:
            if response is not None:
                raise TypeError("Cannot pass both 'response' and 'resp_or_url'")
            response = kwargs.pop("resp_or_url")
            warn(
                "Passing 'resp_or_url' is deprecated, use 'response' instead.",
                DeprecationWarning,
                stacklevel=2,
            )
        if response is None:
            raise TypeError("Missing required argument: 'response'")
        if request is None:
            raise TypeError("Missing required argument: 'request'")
        if isinstance(response, str):
            warn(
                "Passing a response URL to RefererMiddleware.policy() instead "
                "of a Response object is deprecated.",
                DeprecationWarning,
                stacklevel=2,
            )
        allow_import_path = True
        policy_name = request.meta.get("referrer_policy")
        if policy_name is None and isinstance(response, Response):
            policy_header = response.headers.get("Referrer-Policy")
            if policy_header is not None:
                policy_name = to_unicode(policy_header.decode("latin1"))
                allow_import_path = False
        if policy_name is None:
            return self.default_policy()
        cls = self._load_policy_class(
            policy_name, warning_only=True, allow_import_path=allow_import_path
        )
        return cls() if cls else self.default_policy()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_files.py::_create_item_with_files [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_files.py]
def _create_item_with_files(*files: str) -> ItemWithFiles:
    item = ItemWithFiles()
    item["file_urls"] = files
    return item

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.syntax [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py]
    def syntax(self) -> str:
        """
        Command syntax (preferably one-line). Do not include command name.
        """
        return ""

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exporters.py::PythonItemExporter._configure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exporters.py]
    def _configure(self, options: dict[str, Any], dont_fail: bool = False) -> None:
        super()._configure(options, dont_fail)
        if not self.encoding:
            self.encoding = "utf-8"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_left.py::SignalCatcherSpider.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_left.py]
    def __init__(self, crawler, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        crawler.signals.connect(self.on_request_left, signal=request_left_downloader)
        self.caught_times = 0
        self.start_urls = [url]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exceptions.py::StopDownload.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/exceptions.py]
    def __init__(self, *, fail: bool = True):
        super().__init__()
        self.fail = fail
```
