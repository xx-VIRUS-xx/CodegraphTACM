# scrapy-32 :: minilm

query: fixed CrawlerProcess when settings are passed as dicts

## selected nodes

- rank=1 layer=FUNCTION tokens=333 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_reactor_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=2 layer=FUNCTION tokens=237 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=3 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcess.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=4 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::get_raw_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py
- rank=5 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=6 layer=FUNCTION tokens=365 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py::AddonManager.load_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py
- rank=7 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py
- rank=8 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py::DownloadHandlers.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py
- rank=9 layer=FUNCTION tokens=293 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py::MiddlewareManager.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py
- rank=10 layer=FUNCTION tokens=668 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FeedExporter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py
- rank=11 layer=FUNCTION tokens=313 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.set file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=12 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpBase.get_dh file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py
- rank=13 layer=FUNCTION tokens=261 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py::AddonManager.load_pre_crawler_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py
- rank=14 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py
- rank=15 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_http11.py::TestHttp11WithCrawler.settings_dict file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_http11.py
- rank=16 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::MySpider.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py
- rank=17 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_httpx.py::TestHttp11WithCrawler.settings_dict file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_httpx.py
- rank=18 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_extension_periodic_log.py::extension file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_extension_periodic_log.py
- rank=19 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::AjaxCrawlMiddleware.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcess.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(
        self,
        settings: dict[str, Any] | Settings | None = None,
        install_root_handler: bool = True,
    ):
        super().__init__(settings, install_root_handler)
        self._initialized_reactor: bool = False
        logger.debug("Using CrawlerProcess")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::get_raw_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py]
def get_raw_crawler(spidercls=None, settings_dict=None):
    """get_crawler alternative that only calls the __init__ method of the
    crawler."""
    settings = Settings()
    settings.setdict(get_reactor_settings())
    settings.setdict(settings_dict or {})
    return Crawler(spidercls or DefaultSpider, settings)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(self, settings: dict[str, Any] | Settings | None = None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        AddonManager.load_pre_crawler_settings(settings)
        self.settings: Settings = settings
        self.spider_loader: SpiderLoaderProtocol = get_spider_loader(settings)
        self._crawlers: set[Crawler] = set()
        self.bootstrap_failed = False

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py]
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py::DownloadHandlers.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py]
    def __init__(self, crawler: Crawler):
        self._crawler: Crawler = crawler
        # stores acceptable schemes on instancing
        self._schemes: dict[str, str | Callable[..., Any]] = {}
        # stores instanced handlers for schemes
        self._handlers: dict[str, DownloadHandlerProtocol] = {}
        # remembers failed handlers
        self._notconfigured: dict[str, str] = {}
        # remembers handlers with Deferred-based download_request()
        self._old_style_handlers: set[str] = set()
        handlers: dict[str, str | Callable[..., Any]] = without_none_values(
            cast(
                "dict[str, str | Callable[..., Any]]",
                crawler.settings.getwithbase("DOWNLOAD_HANDLERS"),
            )
        )
        for scheme, clspath in handlers.items():
            self._schemes[scheme] = clspath
            self._load_handler(scheme, skip_lazy=True)

        crawler.signals.connect(self._close, signals.engine_stopped)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.set [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
    def set(
        self, name: _SettingsKey, value: Any, priority: int | str = "project"
    ) -> None:
        """
        Store a key/value attribute with a given priority.

        Settings should be populated *before* configuring the Crawler object
        (through the :meth:`~scrapy.crawler.Crawler.configure` method),
        otherwise they won't have any effect.

        :param name: the setting name
        :type name: str

        :param value: the value to associate with the setting
        :type value: object

        :param priority: the priority of the setting. Should be a key of
            :attr:`~scrapy.settings.SETTINGS_PRIORITIES` or an integer
        :type priority: str or int
        """
        self._assert_mutability()
        priority = get_settings_priority(priority)
        if name not in self:
            if isinstance(value, SettingsAttribute):
                self.attributes[name] = value
            else:
                self.attributes[name] = SettingsAttribute(value, priority)
        else:
            self.attributes[name].set(value, priority)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpBase.get_dh [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py]
    async def get_dh(
        self, settings_dict: dict[str, Any] | None = None
    ) -> AsyncGenerator[DownloadHandlerProtocol]:
        crawler = get_crawler(DefaultSpider, settings_dict)
        crawler.spider = crawler._create_spider()
        dh = build_from_crawler(self.download_handler_cls, crawler)
        try:
            yield dh
        finally:
            await dh.close()

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py]
            def update_pre_crawler_settings(cls, settings):
                settings.set(
                    "SPIDER_MODULES",
                    [module],
                    "project",
                )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_http11.py::TestHttp11WithCrawler.settings_dict [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_http11.py]
    def settings_dict(self) -> dict[str, Any] | None:
        return {
            "DOWNLOAD_HANDLERS": {
                "http": "scrapy.core.downloader.handlers.http11.HTTP11DownloadHandler",
                "https": "scrapy.core.downloader.handlers.http11.HTTP11DownloadHandler",
            }
        }

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::MySpider.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py]
            def from_crawler(cls, crawler, *args, **kwargs):
                spider = super().from_crawler(crawler, *args, **kwargs)
                addon_config = {"KEY": "addon"}
                addon_cls = get_addon_cls(addon_config)
                spider.settings.set("ADDONS", {addon_cls: 1}, priority="spider")
                return spider

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_httpx.py::TestHttp11WithCrawler.settings_dict [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_httpx.py]
    def settings_dict(self) -> dict[str, Any] | None:
        return {
            "DOWNLOAD_HANDLERS": {
                "http": "scrapy.core.downloader.handlers._httpx.HttpxDownloadHandler",
                "https": "scrapy.core.downloader.handlers._httpx.HttpxDownloadHandler",
            }
        }

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_extension_periodic_log.py::extension [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_extension_periodic_log.py]
def extension(settings: dict[str, Any] | None = None) -> CustomPeriodicLog:
    crawler = get_crawler(MetaSpider, settings)
    return CustomPeriodicLog.from_crawler(crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::AjaxCrawlMiddleware.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py]
    def from_crawler(cls, crawler: Crawler) -> Self:
        return cls(crawler.settings)
```
