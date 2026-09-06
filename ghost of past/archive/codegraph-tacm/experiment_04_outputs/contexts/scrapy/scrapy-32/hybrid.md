# scrapy-32 :: hybrid

query: fixed CrawlerProcess when settings are passed as dicts

## selected nodes

- rank=1 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcess.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=2 layer=FUNCTION tokens=333 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_reactor_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=3 layer=FUNCTION tokens=237 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=4 layer=FUNCTION tokens=668 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FeedExporter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py
- rank=5 layer=FUNCTION tokens=365 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py::AddonManager.load_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py
- rank=6 layer=FUNCTION tokens=261 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py::AddonManager.load_pre_crawler_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py
- rank=7 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=8 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::get_raw_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py
- rank=9 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._storage file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py
- rank=10 layer=FUNCTION tokens=429 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::configure_logging file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=11 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_reactorless_default_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=12 layer=FUNCTION tokens=200 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::Settings.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=13 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._middleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py
- rank=14 layer=FUNCTION tokens=220 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=15 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py::MiddlewareManager.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py
- rank=16 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py
- rank=17 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcess.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(
        self,
        settings: dict[str, Any] | Settings | None = None,
        install_root_handler: bool = True,
    ):
        super().__init__(settings, install_root_handler)
        self._initialized_reactor: bool = False
        logger.debug("Using CrawlerProcess")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_reactor_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py]
def get_reactor_settings() -> dict[str, Any]:
    """Return a settings dict that works with the installed reactor.

    ``Crawler._apply_settings()`` checks that the installed reactor matches the
    settings, so tests that run the crawler in the current process may need to
    pass a correct :setting:`TWISTED_REACTOR` setting value when creating it.
    """
    settings: dict[str, Any] = {}
    if is_reactor_installed():
        if not is_asyncio_reactor_installed():
            settings["TWISTED_REACTOR"] = None
    else:
        # We are either running Scrapy tests for the reactorless mode, or
        # running some 3rd-party library tests for the reactorless mode, or
        # running some 3rd-party library tests without initializing a reactor
        # properly. The first two cases are fine, but we cannot distinguish the
        # last one from them.
        settings["TWISTED_REACTOR_ENABLED"] = False
        settings["DOWNLOAD_HANDLERS"] = {
            "ftp": None,
            "http": "scrapy.core.downloader.handlers._httpx.HttpxDownloadHandler",
            "https": "scrapy.core.downloader.handlers._httpx.HttpxDownloadHandler",
        }
    return settings

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py]
def get_crawler(
    spidercls: type[Spider] | None = None,
    settings_dict: dict[str, Any] | None = None,
    prevent_warnings: bool = True,
) -> Crawler:
    """Return an unconfigured Crawler object. If settings_dict is given, it
    will be used to populate the crawler settings with a project level
    priority.
    """
    # When needed, useful settings can be added here, e.g. ones that prevent
    # deprecation warnings.
    settings: dict[str, Any] = {
        **get_reactor_settings(),
        **(settings_dict or {}),
    }
    runner: CrawlerRunnerBase
    if is_reactor_installed():
        runner = CrawlerRunner(settings)
    else:
        runner = AsyncCrawlerRunner(settings)
    crawler = runner.create_crawler(spidercls or DefaultSpider)
    crawler._apply_settings()
    return crawler

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FeedExporter.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py]
    def __init__(self, crawler: Crawler):
        self.crawler: Crawler = crawler
        self.settings: Settings = crawler.settings
        self.feeds = {}
        self.slots: list[FeedSlot] = []
        self.filters: dict[str, ItemFilter] = {}
        self._pending_close_coros: list[Coroutine[Any, Any, None]] = []

        if not self.settings["FEEDS"] and not self.settings["FEED_URI"]:
            raise NotConfigured

        # Begin: Backward compatibility for FEED_URI and FEED_FORMAT settings
        if self.settings["FEED_URI"]:
            warnings.warn(
                "The `FEED_URI` and `FEED_FORMAT` settings have been deprecated in favor of "
                "the `FEEDS` setting. Please see the `FEEDS` setting docs for more details",
                category=ScrapyDeprecationWarning,
                stacklevel=2,
            )
            uri = self.settings["FEED_URI"]
            # handle pathlib.Path objects
            uri = str(uri) if not isinstance(uri, Path) else uri.absolute().as_uri()
            feed_options = {"format": self.settings["FEED_FORMAT"]}
            self.feeds[uri] = feed_complete_default_values_from_settings(
                feed_options, self.settings
            )
            self.filters[uri] = self._load_filter(feed_options)
        # End: Backward compatibility for FEED_URI and FEED_FORMAT settings

        # 'FEEDS' setting takes precedence over 'FEED_URI'
        for settings_uri, feed_options in self.settings.getdict("FEEDS").items():
            # handle pathlib.Path objects
            uri = (
                str(settings_uri)
                if not isinstance(settings_uri, Path)
                else settings_uri.absolute().as_uri()
            )
            self.feeds[uri] = feed_complete_default_values_from_settings(
                feed_options, self.settings
            )
            self.filters[uri] = self._load_filter(feed_options)

        self.storages: dict[str, type[FeedStorageProtocol]] = self._load_components(
            "FEED_STORAGES"
        )
        self.exporters: dict[str, type[BaseItemExporter]] = self._load_components(
            "FEED_EXPORTERS"
        )
        for uri, feed_options in self.feeds.items():
            if not self._storage_supported(uri, feed_options):
                raise NotConfigured
            if not self._settings_are_valid():
                raise NotConfigured
            if not self._exporter_supported(feed_options["format"]):
                raise NotConfigured

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py::AddonManager.load_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py]
    def load_settings(self, settings: Settings) -> None:
        """Load add-ons and configurations from a settings object and apply them.

        This will load the add-on for every add-on path in the
        ``ADDONS`` setting and execute their ``update_settings`` methods.

        :param settings: The :class:`~scrapy.settings.Settings` object from \
            which to read the add-on configuration
        :type settings: :class:`~scrapy.settings.Settings`
        """
        for clspath in build_component_list(settings["ADDONS"]):
            try:
                addoncls = load_object(clspath)
                addon = build_from_crawler(addoncls, self.crawler)
                if hasattr(addon, "update_settings"):
                    addon.update_settings(settings)
                self.addons.append(addon)
            except NotConfigured as e:
                if e.args:
                    logger.warning(
                        "Disabled %(clspath)s: %(eargs)s",
                        {"clspath": clspath, "eargs": e.args[0]},
                        extra={"crawler": self.crawler},
                    )
        logger.info(
            "Enabled addons:\n%(addons)s",
            {
                "addons": self.addons,
            },
            extra={"crawler": self.crawler},
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py::AddonManager.load_pre_crawler_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py]
    def load_pre_crawler_settings(cls, settings: BaseSettings) -> None:
        """Update early settings that do not require a crawler instance, such as SPIDER_MODULES.

        Similar to the load_settings method, this loads each add-on configured in the
        ``ADDONS`` setting and calls their 'update_pre_crawler_settings' class method if present.
        This method doesn't have access to the crawler instance or the addons list.

        :param settings: The :class:`~scrapy.settings.BaseSettings` object from \
            which to read the early add-on configuration
        :type settings: :class:`~scrapy.settings.Settings`
        """
        for clspath in build_component_list(settings["ADDONS"]):
            addoncls = load_object(clspath)
            if hasattr(addoncls, "update_pre_crawler_settings"):
                addoncls.update_pre_crawler_settings(settings)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(self, settings: dict[str, Any] | Settings | None = None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        AddonManager.load_pre_crawler_settings(settings)
        self.settings: Settings = settings
        self.spider_loader: SpiderLoaderProtocol = get_spider_loader(settings)
        self._crawlers: set[Crawler] = set()
        self.bootstrap_failed = False

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::get_raw_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py]
def get_raw_crawler(spidercls=None, settings_dict=None):
    """get_crawler alternative that only calls the __init__ method of the
    crawler."""
    settings = Settings()
    settings.setdict(get_reactor_settings())
    settings.setdict(settings_dict or {})
    return Crawler(spidercls or DefaultSpider, settings)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._storage [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py]
    def _storage(self, **new_settings: Any):
        with self._middleware(**new_settings) as mw:
            yield mw.storage, mw.crawler

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::configure_logging [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py]
def configure_logging(
    settings: Settings | dict[_SettingsKey, Any] | None = None,
    install_root_handler: bool = True,
) -> None:
    """
    Initialize logging defaults for Scrapy.

    :param settings: settings used to create and configure a handler for the
        root logger (default: None).
    :type settings: dict, :class:`~scrapy.settings.Settings` object or ``None``

    :param install_root_handler: whether to install root logging handler
        (default: True)
    :type install_root_handler: bool

    This function does:

    - Route warnings and twisted logging through Python standard logging
    - Assign DEBUG and ERROR level to Scrapy and Twisted loggers respectively
    - Route stdout to log if LOG_STDOUT setting is True

    When ``install_root_handler`` is True (default), this function also
    creates a handler for the root logger according to given settings
    (see :ref:`topics-logging-settings`). You can override default options
    using ``settings`` argument. When ``settings`` is empty or None, defaults
    are used.
    """
    if not sys.warnoptions:
        # Route warnings through python logging
        logging.captureWarnings(True)

    observer = twisted_log.PythonLoggingObserver("twisted")
    observer.start()

    dictConfig(DEFAULT_LOGGING)

    if isinstance(settings, dict) or settings is None:
        settings = Settings(settings)

    if settings.getbool("LOG_STDOUT"):
        sys.stdout = StreamLogger(logging.getLogger("stdout"))

    if install_root_handler:
        install_scrapy_root_handler(settings)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_reactorless_default_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def _apply_reactorless_default_settings(self) -> None:
        """Change some setting defaults when not using a Twisted reactor.

        Some settings need different defaults when using and not using a
        reactor, but as we can't put this logic into default_settings.py we
        change them here when the reactor is not used.
        """
        self.settings.set("TELNETCONSOLE_ENABLED", False, priority="default")
        for scheme in ("http", "https"):
            self.settings["DOWNLOAD_HANDLERS_BASE"][scheme] = (
                "scrapy.core.downloader.handlers._httpx.HttpxDownloadHandler"
            )
        self.settings["DOWNLOAD_HANDLERS_BASE"]["ftp"] = None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::Settings.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
    def __init__(self, values: _SettingsInput = None, priority: int | str = "project"):
        # Do not pass kwarg values here. We don't want to promote user-defined
        # dicts, and we want to update, not replace, default dicts with the
        # values given by the user
        super().__init__()
        self.setmodule(default_settings, "default")
        # Promote default dictionaries to BaseSettings instances for per-key
        # priorities
        for name, val in self.items():
            if isinstance(val, dict):
                self.set(name, BaseSettings(val, "default"), "default")
        self.update(values, priority)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._middleware [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py]
    def _middleware(self, **new_settings: Any) -> Generator[HttpCacheMiddleware]:
        with self._get_crawler(**new_settings) as crawler:
            assert crawler.spider
            mw = HttpCacheMiddleware.from_crawler(crawler)
            mw.spider_opened(crawler.spider)
            try:
                yield mw
            finally:
                mw.spider_closed(crawler.spider)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py]
    def __init__(self, crawler: Crawler):
        if not crawler.settings.getbool("ROBOTSTXT_OBEY"):
            raise NotConfigured
        self._default_useragent: str = crawler.settings["USER_AGENT"]
        self._robotstxt_useragent: str | None = crawler.settings["ROBOTSTXT_USER_AGENT"]
        self.crawler: Crawler = crawler
        self._parsers: dict[str, RobotParser | Deferred[RobotParser | None] | None] = {}
        self._parserimpl: RobotParser = load_object(
            crawler.settings.get("ROBOTSTXT_PARSER")
        )

        # check if parser dependencies are met, this should throw an error otherwise.
        self._parserimpl.from_crawler(self.crawler, b"")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py::MiddlewareManager.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py]
    def from_crawler(cls, crawler: Crawler) -> Self:
        mwlist = cls._get_mwlist_from_settings(crawler.settings)
        middlewares = []
        enabled = []
        for clspath in mwlist:
            try:
                mwcls = load_object(clspath)
                mw = build_from_crawler(mwcls, crawler)
                middlewares.append(mw)
                enabled.append(clspath)
            except NotConfigured as e:
                if e.args:
                    logger.warning(
                        "Disabled %(clspath)s: %(eargs)s",
                        {"clspath": clspath, "eargs": e.args[0]},
                        extra={"crawler": crawler},
                    )

        logger.info(
            "Enabled %(componentname)ss:\n%(enabledlist)s",
            {
                "componentname": cls.component_name,
                "enabledlist": pprint.pformat(enabled),
            },
            extra={"crawler": crawler},
        )
        return cls(*middlewares, crawler=crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py]
            def update_pre_crawler_settings(cls, settings):
                settings.set(
                    "SPIDER_MODULES",
                    [module],
                    "project",
                )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py]
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
```
