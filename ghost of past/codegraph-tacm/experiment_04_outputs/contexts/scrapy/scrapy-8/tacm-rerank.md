# scrapy-8 :: tacm-rerank

query: BUG: Fix __classcell__ propagation.

## selected nodes

- rank=1 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::ItemMeta.__new__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py
- rank=2 layer=FUNCTION tokens=422 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py::PeriodicLog.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py
- rank=3 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=4 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._create_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=5 layer=FUNCTION tokens=1342 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=6 layer=FUNCTION tokens=680 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=7 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=8 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=9 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=10 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.items file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=11 layer=FUNCTION tokens=350 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.run file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py
- rank=12 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py::SignalManager.connect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::ItemMeta.__new__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py]
    def __new__(
        mcs, class_name: str, bases: tuple[type, ...], attrs: dict[str, Any]
    ) -> ItemMeta:
        classcell = attrs.pop("__classcell__", None)
        new_bases = tuple(base._class for base in bases if hasattr(base, "_class"))
        _class = super().__new__(mcs, "x_" + class_name, new_bases, attrs)

        fields = getattr(_class, "fields", {})
        new_attrs = {}
        for n in dir(_class):
            v = getattr(_class, n)
            if isinstance(v, Field):
                fields[n] = v
            elif n in attrs:
                new_attrs[n] = attrs[n]

        new_attrs["fields"] = fields
        new_attrs["_class"] = _class
        if classcell is not None:
            new_attrs["__classcell__"] = classcell
        return super().__new__(mcs, class_name, bases, new_attrs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py::PeriodicLog.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py]
    def from_crawler(cls, crawler: Crawler) -> Self:
        interval: float = crawler.settings.getfloat("LOGSTATS_INTERVAL")
        if not interval:
            raise NotConfigured
        try:
            ext_stats: dict[str, Any] | None = crawler.settings.getdict(
                "PERIODIC_LOG_STATS"
            )
        except (TypeError, ValueError):
            ext_stats = (
                {"enabled": True}
                if crawler.settings.getbool("PERIODIC_LOG_STATS")
                else None
            )
        try:
            ext_delta: dict[str, Any] | None = crawler.settings.getdict(
                "PERIODIC_LOG_DELTA"
            )
        except (TypeError, ValueError):
            ext_delta = (
                {"enabled": True}
                if crawler.settings.getbool("PERIODIC_LOG_DELTA")
                else None
            )

        ext_timing_enabled: bool = crawler.settings.getbool(
            "PERIODIC_LOG_TIMING_ENABLED"
        )
        if not (ext_stats or ext_delta or ext_timing_enabled):
            raise NotConfigured
        assert crawler.stats
        assert ext_stats is not None
        assert ext_delta is not None
        o = cls(
            crawler.stats,
            interval,
            ext_stats,
            ext_delta,
            ext_timing_enabled,
        )
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        return o

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py]
            def __init__(self, *args, **kwargs):  # pylint: disable=useless-parent-delegation
                # This call to super() trigger the __classcell__ propagation
                # requirement. When not done properly raises an error:
                # TypeError: __class__ set to <class '__main__.MyItem'>
                # defining 'MyItem' as <class '__main__.MyItem'>
                super().__init__(*args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._create_spider [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def _create_spider(self, *args: Any, **kwargs: Any) -> Spider:
        return self.spidercls.from_crawler(self, *args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py]
    def __init__(
        self,
        url: str,
        callback: CallbackT | None = None,
        method: str = "GET",
        headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        body: bytes | str | None = None,
        cookies: CookiesT | None = None,
        meta: dict[str, Any] | None = None,
        encoding: str = "utf-8",
        priority: int = 0,
        dont_filter: bool = False,
        errback: Callable[[Failure], Any] | None = None,
        flags: list[str] | None = None,
        cb_kwargs: dict[str, Any] | None = None,
    ) -> None:
        self._encoding: str = encoding  # this one has to be set first
        self.method: str = str(method).upper()
        self._set_url(url)
        self._set_body(body)
        if not isinstance(priority, int):
            raise TypeError(f"Request priority not an integer: {priority!r}")

        #: Default: ``0``
        #:
        #: Value that the :ref:`scheduler <topics-scheduler>` may use for
        #: request prioritization.
        #:
        #: Built-in schedulers prioritize requests with a higher priority
        #: value.
        #:
        #: Negative values are allowed.
        self.priority: int = priority

        if not (callable(callback) or callback is None):
            raise TypeError(
                f"callback must be a callable, got {type(callback).__name__}"
            )
        if not (callable(errback) or errback is None):
            raise TypeError(f"errback must be a callable, got {type(errback).__name__}")

        #: :class:`~collections.abc.Callable` to parse the
        #: :class:`~scrapy.http.Response` to this request once received.
        #:
        #: The callable must expect the response as its first parameter, and
        #: support any additional keyword arguments set through
        #: :attr:`cb_kwargs`.
        #:
        #: In addition to an arbitrary callable, the following values are also
        #: supported:
        #:
        #: -   ``None`` (default), which indicates that the
        #:     :meth:`~scrapy.Spider.parse` method of the spider must be used.
        #:
        #: -   :func:`~scrapy.http.request.NO_CALLBACK`.
        #:
        #: If an unhandled exception is raised during request or response
        #: processing, i.e. by a :ref:`spider middleware
        #: <topics-spider-middleware>`, :ref:`downloader middleware
        #: <topics-downloader-middleware>` or download handler
        #: (:setting:`DOWNLOAD_HANDLERS`), :attr:`errback` is called instead.
        #:
        #: .. tip::
        #:     :class:`~scrapy.spidermiddlewares.httperror.HttpErrorMiddleware`
        #:     raises exceptions for non-2xx responses by default, sending them
        #:     to the :attr:`errback` instead.
        #:
        #: .. seealso::
        #:     :ref:`topics-request-response-ref-request-callback-arguments`
        self.callback: CallbackT | None = callback

        #: :class:`~collections.abc.Callable` to handle exceptions raised
        #: during request or response processing.
        #:
        #: The callable must expect a :exc:`~twisted.python.failure.Failure` as
        #: its first parameter.
        #:
        #: .. seealso:: :ref:`topics-request-response-ref-errbacks`
        self.errback: Callable[[Failure], Any] | None = errback

        self._cookies: CookiesT | None = cookies or None
        self._headers: Headers | None = (
            Headers(headers, encoding=encoding) if headers else None
        )

        #: Whether this request may be filtered out by :ref:`components
        #: <topics-components>` that support filtering out requests (``False``,
        #: default), or those components should not filter out this request
        #: (``True``).
        #:
        #: The following built-in components check this attribute:
        #:
        #: -   The :ref:`scheduler <topics-scheduler>` uses it to skip
        #:     duplicate request filtering (see
        #:     :setting:`DUPEFILTER_CLASS`). When set to ``True``, the
        #:     request is not checked against the duplicate filter,
        #:     allowing requests that would otherwise be considered duplicates
        #:     to be scheduled multiple times.
        #: -   :class:`~scrapy.downloadermiddlewares.offsite.OffsiteMiddleware`
        #:     uses it to allow requests to domains not in
        #:     :attr:`~scrapy.Spider.allowed_domains`. To skip only the offsite
        #:     filter without affecting other components, consider using the
        #:     :reqmeta:`allow_offsite` request meta key instead.
        #:
        #: Third-party components may also use this attribute to decide whether
        #: to filter out a request.
        #:
        #: When defining the start URLs of a spider through
        #: :attr:`~scrapy.Spider.start_urls`, this attribute is enabled by
        #: default. See :meth:`~scrapy.Spider.start`.
        self.dont_filter: bool = dont_filter

        self._meta: dict[str, Any] | None = dict(meta) if meta else None
        self._cb_kwargs: dict[str, Any] | None = dict(cb_kwargs) if cb_kwargs else None
        self._flags: list[str] | None = list(flags) if flags else None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def _apply_settings(self) -> None:
        if self.settings.frozen:
            return

        self.addons.load_settings(self.settings)
        self.stats = load_object(self.settings["STATS_CLASS"])(self)

        lf_cls: type[LogFormatter] = load_object(self.settings["LOG_FORMATTER"])
        self.logformatter = lf_cls.from_crawler(self)

        self.request_fingerprinter = build_from_crawler(
            load_object(self.settings["REQUEST_FINGERPRINTER_CLASS"]),
            self,
        )

        use_reactor = self.settings.getbool("TWISTED_REACTOR_ENABLED")
        if use_reactor:
            # We either install a reactor or expect one to be installed.
            reactor_class: str = self.settings["TWISTED_REACTOR"]
            event_loop: str = self.settings["ASYNCIO_EVENT_LOOP"]
            if self._init_reactor:
                # We need to install a reactor.
                # This needs to be done after the spider settings are merged,
                # but before something imports twisted.internet.reactor.
                if reactor_class:
                    # Install a specific reactor.
                    install_reactor(reactor_class, event_loop)
                else:
                    # Install the default one.
                    from twisted.internet import reactor  # noqa: F401
            elif not is_reactor_installed():
                # We need a reactor to be already installed.
                raise RuntimeError(
                    "We expected a Twisted reactor to be installed but it isn't."
                )
            if reactor_class:
                # We need to check that the correct reactor is installed.
                verify_installed_reactor(reactor_class)
                if is_asyncio_reactor_installed() and event_loop:
                    verify_installed_asyncio_event_loop(event_loop)

            if self._init_reactor or reactor_class:
                log_reactor_info()
        else:
            # We expect a reactor to not be installed.
            if is_reactor_installed():
                raise RuntimeError(
                    "TWISTED_REACTOR_ENABLED is False but a Twisted reactor is installed."
                )
            logger.debug("Not using a Twisted reactor")
            self._apply_reactorless_default_settings()

        self.extensions = ExtensionManager.from_crawler(self)
        self.settings.freeze()

        d = dict(overridden_settings(self.settings))
        logger.info(
            "Overridden settings:\n%(settings)s", {"settings": pprint.pformat(d)}
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.items [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def items(self) -> Iterable[tuple[bytes, list[bytes]]]:  # type: ignore[override]
        return ((k, self.getlist(k)) for k in self.keys())

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.run [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py]
    def run(self, args: list[str], opts: Namespace) -> None:
        url = args[0] if args else None
        if url:
            # first argument may be a local file
            url = guess_scheme(url)

        assert self.crawler_process
        spider_loader = self.crawler_process.spider_loader

        spidercls: type[Spider] = DefaultSpider
        if opts.spider:
            spidercls = spider_loader.load(opts.spider)
        elif url:
            spidercls = spidercls_for_request(
                spider_loader, Request(url), spidercls, log_multiple=True
            )

        # The crawler is created this way since the Shell manually handles the
        # crawling engine, so the set up in the crawl method won't work
        crawler = self.crawler_process._create_crawler(spidercls)
        crawler._apply_settings()
        loop: asyncio.AbstractEventLoop | None = None
        if crawler.settings.getbool("TWISTED_REACTOR_ENABLED"):
            self._init_with_reactor(crawler)
        else:
            self._init_without_reactor(crawler)
            loop = self._get_reactorless_loop()
        shell = Shell(crawler, update_vars=self.update_vars, code=opts.code, loop=loop)
        shell.start(url=url, redirect=not opts.no_redirect)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py::SignalManager.connect [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py]
    def connect(self, receiver: Any, signal: Any, **kwargs: Any) -> None:
        """
        Connect a receiver function to a signal.

        The signal can be any object, although Scrapy comes with some
        predefined signals that are documented in the :ref:`topics-signals`
        section.

        :param receiver: the function to be connected
        :type receiver: collections.abc.Callable

        :param signal: the signal to connect to
        :type signal: object
        """
        kwargs.setdefault("sender", self.sender)
        dispatcher.connect(receiver, signal, **kwargs)
```
