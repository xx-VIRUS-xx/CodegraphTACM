# scrapy-26 :: tacm-full

query: Fix backwards-compatibility for users who explicitly set _BASE settings

## selected nodes

- rank=1 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._key_for_pipe file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=2 layer=FUNCTION tokens=668 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FeedExporter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py
- rank=3 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_reactorless_default_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=4 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py::TestFTP._get_factory file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py
- rank=5 layer=FUNCTION tokens=305 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlLinkExtractor.extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=6 layer=FUNCTION tokens=279 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::method_is_overridden file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=7 layer=FUNCTION tokens=399 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=8 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_logformatter.py::TestShowOrSkipMessages.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_logformatter.py
- rank=9 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::_get_project_only_cmds file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py
- rank=10 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=11 layer=FUNCTION tokens=423 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.update file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=12 layer=FUNCTION tokens=303 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/__init__.py::Downloader.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/__init__.py
- rank=13 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::AsyncCrawlerRunner.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=14 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py::pytest_configure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py
- rank=15 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=16 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py
- rank=17 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py
- rank=18 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._key_for_pipe [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _key_for_pipe(
        self,
        key: str,
        base_class_name: str | None = None,
        settings: Settings | None = None,
    ) -> str:
        class_name = self.__class__.__name__
        formatted_key = f"{class_name.upper()}_{key}"
        if (
            not base_class_name
            or class_name == base_class_name
            or (settings and not settings.get(formatted_key))
        ):
            return key
        return formatted_key

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py::TestFTP._get_factory [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py]
    def _get_factory(self, root):
        from twisted.protocols.ftp import FTPFactory, FTPRealm

        realm = FTPRealm(anonymousRoot=str(root), userHome=str(root))
        p = portal.Portal(realm)
        users_checker = checkers.InMemoryUsernamePasswordDatabaseDontUse()
        users_checker.addUser(self.username, self.password)
        p.registerChecker(users_checker, credentials.IUsernamePassword)
        return FTPFactory(portal=p)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlLinkExtractor.extract_links [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py]
    def extract_links(self, response: TextResponse) -> list[Link]:
        """Returns a list of :class:`~scrapy.link.Link` objects from the
        specified :class:`response <scrapy.http.Response>`.

        Only links that match the settings passed to the ``__init__`` method of
        the link extractor are returned.

        Duplicate links are omitted if the ``unique`` attribute is set to ``True``,
        otherwise they are returned.
        """
        base_url = get_base_url(response)
        if self.restrict_xpaths:
            docs = [
                subdoc for x in self.restrict_xpaths for subdoc in response.xpath(x)
            ]
        else:
            docs = [response.selector]
        all_links = []
        for doc in docs:
            links = self._extract_links(doc, response.url, response.encoding, base_url)
            all_links.extend(self._process_links(links))
        if self.link_extractor.unique:
            return unique_list(all_links, key=self.link_extractor.link_key)
        return all_links

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::method_is_overridden [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py]
def method_is_overridden(subclass: type, base_class: type, method_name: str) -> bool:
    """
    Return True if a method named ``method_name`` of a ``base_class``
    is overridden in a ``subclass``.

    >>> class Base:
    ...     def foo(self):
    ...         pass
    >>> class Sub1(Base):
    ...     pass
    >>> class Sub2(Base):
    ...     def foo(self):
    ...         pass
    >>> class Sub3(Sub1):
    ...     def foo(self):
    ...         pass
    >>> class Sub4(Sub2):
    ...     pass
    >>> method_is_overridden(Base, Base, 'foo')
    False
    >>> method_is_overridden(Sub1, Base, 'foo')
    False
    >>> method_is_overridden(Sub2, Base, 'foo')
    True
    >>> method_is_overridden(Sub3, Base, 'foo')
    True
    >>> method_is_overridden(Sub4, Base, 'foo')
    True
    """
    base_method = getattr(base_class, method_name)
    sub_method = getattr(subclass, method_name)
    return base_method.__code__ is not sub_method.__code__

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py]
    def _extract_links(
        self,
        selector: Selector,
        response_url: str,
        response_encoding: str,
        base_url: str,
    ) -> list[Link]:
        links: list[Link] = []
        # hacky way to get the underlying lxml parsed document
        for el, _, attr_val in self._iter_links(selector.root):
            # pseudo lxml.html.HtmlElement.make_links_absolute(base_url)
            try:
                if self.strip:
                    attr_val = strip_html5_whitespace(attr_val)  # noqa: PLW2901 this is intended
                attr_val = urljoin(base_url, attr_val)  # noqa: PLW2901
            except ValueError:
                continue  # skipping bogus links
            else:
                url = self.process_attr(attr_val)
                if url is None:
                    continue
            try:
                url = safe_url_string(url, encoding=response_encoding)
            except ValueError:
                logger.debug(f"Skipping extraction of link with bad URL {url!r}")
                continue

            # to fix relative links after process_value
            url = urljoin(response_url, url)
            link = Link(
                url,
                _collect_string_content(el) or "",
                nofollow=rel_has_nofollow(el.get("rel")),
            )
            links.append(link)
        return self._deduplicate_if_needed(links)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_logformatter.py::TestShowOrSkipMessages.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_logformatter.py]
    def setup_method(self):
        self.base_settings = {
            "LOG_LEVEL": "DEBUG",
            "ITEM_PIPELINES": {
                DropSomeItemsPipeline: 300,
            },
        }

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::_get_project_only_cmds [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py]
def _get_project_only_cmds(settings: BaseSettings) -> set[str]:
    return set(_get_commands_dict(settings, inproject=True)) - set(
        _get_commands_dict(settings, inproject=False)
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.update [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
    def update(self, values: _SettingsInput, priority: int | str = "project") -> None:  # type: ignore[override]
        """
        Store key/value pairs with a given priority.

        This is a helper function that calls
        :meth:`~scrapy.settings.BaseSettings.set` for every item of ``values``
        with the provided ``priority``.

        If ``values`` is a string, it is assumed to be JSON-encoded and parsed
        into a dict with ``json.loads()`` first. If it is a
        :class:`~scrapy.settings.BaseSettings` instance, the per-key priorities
        will be used and the ``priority`` parameter ignored. This allows
        inserting/updating settings with different priorities with a single
        command.

        :param values: the settings names and values
        :type values: dict or string or :class:`~scrapy.settings.BaseSettings`

        :param priority: the priority of the settings. Should be a key of
            :attr:`~scrapy.settings.SETTINGS_PRIORITIES` or an integer
        :type priority: str or int
        """
        self._assert_mutability()
        if isinstance(values, str):
            values = cast("dict[_SettingsKey, Any]", json.loads(values))
        if values is not None:
            if isinstance(values, BaseSettings):
                for name, value in values.items():
                    self.set(name, value, cast("int", values.getpriority(name)))
            else:
                for name, value in values.items():
                    self.set(name, value, priority)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/__init__.py::Downloader.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/__init__.py]
    def __init__(self, crawler: Crawler):
        self.crawler: Crawler = crawler
        self.settings: BaseSettings = crawler.settings
        self.signals: SignalManager = crawler.signals
        self.slots: dict[str, Slot] = {}
        self.active: set[Request] = set()
        self.handlers: DownloadHandlers = DownloadHandlers(crawler)
        self.total_concurrency: int = self.settings.getint("CONCURRENT_REQUESTS")
        self.domain_concurrency: int = self.settings.getint(
            "CONCURRENT_REQUESTS_PER_DOMAIN"
        )
        self.ip_concurrency: int = self.settings.getint("CONCURRENT_REQUESTS_PER_IP")
        self.randomize_delay: bool = self.settings.getbool("RANDOMIZE_DOWNLOAD_DELAY")
        self.middleware: DownloaderMiddlewareManager = (
            DownloaderMiddlewareManager.from_crawler(crawler)
        )
        self._slot_gc_loop: AsyncioLoopingCall | LoopingCall | None = None
        self.per_slot_settings: dict[str, dict[str, Any]] = self.settings.getdict(
            "DOWNLOAD_SLOTS"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::AsyncCrawlerRunner.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(self, settings: dict[str, Any] | Settings | None = None):
        super().__init__(settings)
        self._active: set[asyncio.Task[None]] = set()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py::pytest_configure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py]
def pytest_configure(config):
    if config.getoption("--reactor") == "asyncio":
        # Needed on Windows to switch from proactor to selector for Twisted reactor compatibility.
        # If we decide to run tests with both, we will need to add a new option and check it here.
        set_asyncio_event_loop_policy()
    elif config.getoption("--reactor") == "none":
        install_reactor_import_hook()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(self, settings: dict[str, Any] | Settings | None = None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        AddonManager.load_pre_crawler_settings(settings)
        self.settings: Settings = settings
        self.spider_loader: SpiderLoaderProtocol = get_spider_loader(settings)
        self._crawlers: set[Crawler] = set()
        self.bootstrap_failed = False

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py]
    def __init__(self, settings):
        settings.set("TEST1", f"{settings['TEST1']} + started")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py]
            def update_pre_crawler_settings(cls, settings):
                settings.set(
                    "SPIDER_MODULES",
                    [module],
                    "project",
                )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None
```
