# scrapy-2 :: hybrid

query: Fix scrapy.utils.datatypes.LocalCache limit issue

## selected nodes

- rank=1 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py::scrapy_components_versions file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/versions.py
- rank=2 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Slot.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=3 layer=FUNCTION tokens=372 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py::MemoryUsage._check_limit file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py
- rank=4 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py::__getattr__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/default_settings.py
- rank=5 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::LocalWeakReferencedCache.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=6 layer=FUNCTION tokens=226 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::AjaxCrawlMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
- rank=7 layer=FUNCTION tokens=177 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=8 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::walk_modules_iter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py
- rank=9 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::get_scrapy_root_handler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=10 layer=FUNCTION tokens=345 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.to_dict file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=11 layer=FUNCTION tokens=266 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py::Shell.get_help file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py
- rank=12 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py::ResponseTypes.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/responsetypes.py
- rank=13 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py
- rank=14 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py
- rank=15 layer=FUNCTION tokens=254 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/dupefilters.py::RFPDupeFilter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/dupefilters.py
- rank=16 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py
- rank=17 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py
- rank=18 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py
- rank=19 layer=FUNCTION tokens=216 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/resolver.py::CachingThreadedResolver.getHostByName file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/resolver.py
- rank=20 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::install_scrapy_root_handler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=21 layer=FUNCTION tokens=508 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.processProxyResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=22 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.logger file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Slot.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py]
    def __init__(self, max_active_size: int = 5000000):
        self.max_active_size: int = max_active_size
        self.queue: deque[QueueTuple] = deque()
        self.active: set[Request] = set()
        self.active_size: int = 0
        self.itemproc_size: int = 0  # just for scrapy.utils.engine.get_engine_status()
        self.closing: Deferred[Spider] | None = None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py::MemoryUsage._check_limit [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/memusage.py]
    def _check_limit(self) -> None:
        assert self.crawler.engine
        assert self.crawler.stats
        peak_mem_usage = self.get_virtual_size()
        if peak_mem_usage > self.limit:
            self.crawler.stats.set_value("memusage/limit_reached", 1)
            mem = self.limit / 1024 / 1024
            logger.error(
                "Memory usage exceeded %(memusage)dMiB. Shutting down Scrapy...",
                {"memusage": mem},
                extra={"crawler": self.crawler},
            )
            if self.notify_mails:
                subj = (
                    f"{self.crawler.settings['BOT_NAME']} terminated: "
                    f"memory usage exceeded {mem}MiB at {socket.gethostname()}"
                )
                self._send_report(self.notify_mails, subj)
                self.crawler.stats.set_value("memusage/limit_notified", 1)

            if self.crawler.engine.spider is not None:
                _schedule_coro(
                    self.crawler.engine.close_spider_async(reason="memusage_exceeded")
                )
            else:
                _schedule_coro(self.crawler.stop_async())
        else:
            logger.info(
                "Peak memory usage is %(virtualsize)dMiB",
                {"virtualsize": peak_mem_usage / 1024 / 1024},
            )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::LocalWeakReferencedCache.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def __init__(self, limit: int | None = None):
        super().__init__()
        self.data: LocalCache = LocalCache(limit=limit)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.__new__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        # circular import
        from scrapy.http.headers import Headers  # noqa: PLC0415

        if issubclass(cls, CaselessDict) and not issubclass(cls, Headers):
            warnings.warn(
                "scrapy.utils.datatypes.CaselessDict is deprecated,"
                " please use scrapy.utils.datatypes.CaseInsensitiveDict instead",
                category=ScrapyDeprecationWarning,
                stacklevel=2,
            )
        return super().__new__(cls, *args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::walk_modules_iter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py]
def walk_modules_iter(path: str) -> Iterable[ModuleType]:
    """Loads a module and all its submodules from the given module path and
    returns them. If *any* module throws an exception while importing, that
    exception is thrown back.

    For example:
    >>> list(walk_modules_iter('scrapy.utils'))
    [<module 'scrapy.utils' from '...'>, ...]
    >>> gen = walk_modules_iter('scrapy.utils.nonexistent') # error not raised until the generator is consumed
    >>> list(gen)
    Traceback (most recent call last):
        ...
    ModuleNotFoundError: No module named 'scrapy.utils.nonexistent'
    """

    mod = import_module(path)
    yield mod
    if hasattr(mod, "__path__"):
        for _, subpath, ispkg in iter_modules(mod.__path__):
            fullpath = path + "." + subpath
            if ispkg:
                yield from walk_modules_iter(fullpath)
            else:
                yield import_module(fullpath)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::get_scrapy_root_handler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py]
def get_scrapy_root_handler() -> logging.Handler | None:
    return _scrapy_root_handler

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.to_dict [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py]
    def to_dict(self, *, spider: scrapy.Spider | None = None) -> dict[str, Any]:
        """Return a dictionary containing the Request's data.

        Use :func:`~scrapy.utils.request.request_from_dict` to convert back into a :class:`~scrapy.Request` object.

        If a spider is given, this method will try to find out the name of the spider methods used as callback
        and errback and include them in the output dict, raising an exception if they cannot be found.
        """
        d = {
            "url": self.url,  # urls are safe (safe_string_url)
            "callback": (
                _find_method(spider, self.callback)
                if callable(self.callback)
                else self.callback
            ),
            "errback": (
                _find_method(spider, self.errback)
                if callable(self.errback)
                else self.errback
            ),
            "headers": dict(self.headers),
        }
        for attr in self.attributes:
            d.setdefault(attr, getattr(self, attr))
        if type(self) is not Request:  # pylint: disable=unidiomatic-typecheck
            d["_class"] = self.__module__ + "." + self.__class__.__name__
        return d

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py::Shell.get_help [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py]
    def get_help(self) -> str:
        b = []
        b.append("Available Scrapy objects:")
        b.append(
            "  scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)"
        )
        for k, v in sorted(self.vars.items()):
            if self._is_relevant(v):
                b.append(f"  {k:<10} {v}")
        b.append("Useful shortcuts:")
        if self.fetch_available:
            b.append(
                "  fetch(url[, redirect=True]) "
                "Fetch URL and update local objects (by default, redirects are followed)"
            )
            b.append(
                "  fetch(req)                  "
                "Fetch a scrapy.Request and update local objects "
            )
        b.append("  shelp()           Shell help (print this help)")
        b.append("  view(response)    View response in a browser")

        return "\n".join(f"[s] {line}" for line in b) + "\n"

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py]
    def parse(self, response):
        for _ in range(10):
            yield scrapy.Request(
                response.url, dont_filter=True, callback=self.ignore_response
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py]
    def __init__(self) -> None:
        self.settings: Settings | None = None  # set in scrapy.cmdline

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py]
    def parse(self, response):
        for _ in range(10):
            yield scrapy.Request(
                response.url, dont_filter=True, callback=self.ignore_response
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py]
    async def start(self):
        yield scrapy.Request(self.url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py]
    async def start(self):
        yield scrapy.Request(self.url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/resolver.py::CachingThreadedResolver.getHostByName [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/resolver.py]
    def getHostByName(self, name: str, timeout: Sequence[int] = ()) -> Deferred[str]:
        if name in dnscache:
            return defer.succeed(dnscache[name])
        # in Twisted<=16.6, getHostByName() is always called with
        # a default timeout of 60s (actually passed as (1, 3, 11, 45) tuple),
        # so the input argument above is simply overridden
        # to enforce Scrapy's DNS_TIMEOUT setting's value
        # The timeout arg is typed as Sequence[int] but supports floats.
        timeout = (self.timeout,)  # type: ignore[assignment]
        d = super().getHostByName(name, timeout)
        if dnscache.limit:
            d.addCallback(self._cache_result, name)
        return d

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::install_scrapy_root_handler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py]
def install_scrapy_root_handler(settings: Settings) -> None:
    global _scrapy_root_handler  # noqa: PLW0603

    _uninstall_scrapy_root_handler()
    logging.root.setLevel(logging.NOTSET)
    _scrapy_root_handler = _get_handler(settings)
    logging.root.addHandler(_scrapy_root_handler)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.logger [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py]
    def logger(self) -> SpiderLoggerAdapter:
        # circular import
        from scrapy.utils.log import SpiderLoggerAdapter  # noqa: PLC0415

        logger = logging.getLogger(self.name)
        return SpiderLoggerAdapter(logger, {"spider": self})
```
