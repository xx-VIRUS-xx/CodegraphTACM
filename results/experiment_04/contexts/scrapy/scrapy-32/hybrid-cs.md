# scrapy-32 :: hybrid-cs

query: fixed CrawlerProcess when settings are passed as dicts

## selected nodes

- rank=1 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcess.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=2 layer=FUNCTION tokens=429 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::configure_logging file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=3 layer=FUNCTION tokens=261 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py::AddonManager.load_pre_crawler_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/addons.py
- rank=4 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=5 layer=FUNCTION tokens=200 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::Settings.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=6 layer=FUNCTION tokens=333 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_reactor_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=7 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_reactorless_default_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=8 layer=FUNCTION tokens=680 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=9 layer=FUNCTION tokens=668 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FeedExporter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py
- rank=10 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py
- rank=11 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_misc/test_return_with_argument_inside_generator.py::MockSettings.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_misc/test_return_with_argument_inside_generator.py
- rank=12 layer=FUNCTION tokens=159 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._get_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py
- rank=13 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._storage file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py
- rank=14 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::AddonWithFallback.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py
- rank=15 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::TrackingAddon.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py
- rank=16 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::LoggedAddon.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py
- rank=17 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcessBase.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=18 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::SimpleAddon.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py
- rank=19 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpWithCrawlerBase.settings_dict file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py
- rank=20 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_middleware.py::MOff.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_middleware.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py]
            def update_pre_crawler_settings(cls, settings):
                settings.set(
                    "SPIDER_MODULES",
                    [module],
                    "project",
                )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_misc/test_return_with_argument_inside_generator.py::MockSettings.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_misc/test_return_with_argument_inside_generator.py]
            def __init__(self, settings_dict=None):
                self.settings_dict = settings_dict or {}

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._get_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py]
    def _get_settings(self, **new_settings: Any) -> dict[str, Any]:
        settings = {
            "HTTPCACHE_ENABLED": True,
            "HTTPCACHE_DIR": self.tmpdir,
            "HTTPCACHE_EXPIRATION_SECS": 1,
            "HTTPCACHE_IGNORE_HTTP_CODES": [],
            "HTTPCACHE_POLICY": self.policy_class,
            "HTTPCACHE_STORAGE": self.storage_class,
        }
        settings.update(new_settings)
        return settings

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._storage [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py]
    def _storage(self, **new_settings: Any):
        with self._middleware(**new_settings) as mw:
            yield mw.storage, mw.crawler

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::AddonWithFallback.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py]
            def update_settings(self, settings):
                if not settings.get(FALLBACK_SETTING):
                    settings.set(
                        FALLBACK_SETTING,
                        settings.get("SCHEDULER"),
                        "addon",
                    )
                settings["SCHEDULER"] = "AddonScheduler"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::TrackingAddon.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py]
            def update_settings(self, settings):
                pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::LoggedAddon.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py]
            def update_settings(self, settings):
                pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcessBase.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(
        self,
        settings: dict[str, Any] | Settings | None = None,
        install_root_handler: bool = True,
    ):
        super().__init__(settings)
        configure_logging(self.settings, install_root_handler)
        log_scrapy_info(self.settings)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::SimpleAddon.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py]
    def update_settings(self, settings):
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py::TestHttpWithCrawlerBase.settings_dict [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers_http_base.py]
    def settings_dict(self) -> dict[str, Any] | None:
        raise NotImplementedError

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_middleware.py::MOff.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_middleware.py]
    def __init__(self):
        raise NotConfigured("foo")
```
