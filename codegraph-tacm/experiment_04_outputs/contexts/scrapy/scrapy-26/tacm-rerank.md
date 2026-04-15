# scrapy-26 :: tacm-rerank

query: Fix backwards-compatibility for users who explicitly set _BASE settings

## selected nodes

- rank=1 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_reactorless_default_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=2 layer=FUNCTION tokens=680 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=3 layer=FUNCTION tokens=423 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.update file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=4 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=5 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::AsyncCrawlerRunner.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=6 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._key_for_pipe file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=7 layer=FUNCTION tokens=303 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/__init__.py::Downloader.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/__init__.py
- rank=8 layer=FUNCTION tokens=445 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::execute file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py
- rank=9 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::_get_project_only_cmds file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py
- rank=10 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=11 layer=FUNCTION tokens=668 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FeedExporter.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py
- rank=12 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.process_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py
- rank=13 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py::TestFTP._get_factory file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::AsyncCrawlerRunner.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(self, settings: dict[str, Any] | Settings | None = None):
        super().__init__(settings)
        self._active: set[asyncio.Task[None]] = set()

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::execute [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py]
def execute(argv: list[str] | None = None, settings: Settings | None = None) -> None:
    if argv is None:
        argv = sys.argv

    if settings is None:
        settings = get_project_settings()
        # set EDITOR from environment if available
        try:
            editor = os.environ["EDITOR"]
        except KeyError:
            pass
        else:
            settings["EDITOR"] = editor

    inproject = inside_project()
    cmds = _get_commands_dict(settings, inproject)
    cmdname = _pop_command_name(argv)
    if not cmdname:
        _print_commands(settings, inproject)
        sys.exit(0)
    elif cmdname not in cmds:
        _print_unknown_command(settings, cmdname, inproject)
        sys.exit(2)

    cmd = cmds[cmdname]
    parser = ScrapyArgumentParser(
        formatter_class=ScrapyHelpFormatter,
        usage=f"scrapy {cmdname} {cmd.syntax()}",
        conflict_handler="resolve",
        description=cmd.long_desc(),
    )
    settings.setdict(cmd.default_settings, priority="command")
    cmd.settings = settings
    cmd.add_options(parser)
    opts, args = parser.parse_known_args(args=argv[1:])
    _run_print_help(parser, cmd.process_options, args, opts)

    if cmd.requires_crawler_process:
        if (
            settings["TWISTED_REACTOR"] == _asyncio_reactor_path
            and not settings.getbool("FORCE_CRAWLER_PROCESS")
        ) or not settings.getbool("TWISTED_REACTOR_ENABLED"):
            cmd.crawler_process = AsyncCrawlerProcess(settings)
        else:
            cmd.crawler_process = CrawlerProcess(settings)
    _run_print_help(parser, _run_command, cmd, args, opts)
    sys.exit(cmd.exitcode)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::_get_project_only_cmds [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py]
def _get_project_only_cmds(settings: BaseSettings) -> set[str]:
    return set(_get_commands_dict(settings, inproject=True)) - set(
        _get_commands_dict(settings, inproject=False)
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(self, settings: dict[str, Any] | Settings | None = None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        AddonManager.load_pre_crawler_settings(settings)
        self.settings: Settings = settings
        self.spider_loader: SpiderLoaderProtocol = get_spider_loader(settings)
        self._crawlers: set[Crawler] = set()
        self.bootstrap_failed = False

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.process_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py]
    def process_options(self, args: list[str], opts: argparse.Namespace) -> None:
        assert self.settings is not None
        try:
            self.settings.setdict(arglist_to_dict(opts.set), priority="cmdline")
        except ValueError:
            raise UsageError(
                "Invalid -s value, use -s NAME=VALUE", print_help=False
            ) from None

        if opts.logfile:
            self.settings.set("LOG_ENABLED", True, priority="cmdline")
            self.settings.set("LOG_FILE", opts.logfile, priority="cmdline")

        if opts.loglevel:
            self.settings.set("LOG_ENABLED", True, priority="cmdline")
            self.settings.set("LOG_LEVEL", opts.loglevel, priority="cmdline")

        if opts.nolog:
            self.settings.set("LOG_ENABLED", False, priority="cmdline")

        if opts.pidfile:
            Path(opts.pidfile).write_text(
                str(os.getpid()) + os.linesep, encoding="utf-8"
            )

        if opts.pdb:
            failure.startDebugMode()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py::TestFTP._get_factory [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py]
    def _get_factory(self, root):
        from twisted.protocols.ftp import FTPFactory, FTPRealm

        realm = FTPRealm(anonymousRoot=str(root), userHome=str(root))
        p = portal.Portal(realm)
        users_checker = checkers.InMemoryUsernamePasswordDatabaseDontUse()
        users_checker.addUser(self.username, self.password)
        p.registerChecker(users_checker, credentials.IUsernamePassword)
        return FTPFactory(portal=p)
```
