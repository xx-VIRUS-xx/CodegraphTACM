# scrapy-26 :: hybrid

query: Fix backwards-compatibility for users who explicitly set _BASE settings

## selected nodes

- rank=1 layer=FUNCTION tokens=84 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::_get_project_only_cmds file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py
- rank=2 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_reactorless_default_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=3 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::AddonWithFallback.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py
- rank=4 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py::SpiderLoaderProtocol.from_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py
- rank=5 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_logformatter.py::TestShowOrSkipMessages.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_logformatter.py
- rank=6 layer=FUNCTION tokens=158 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._key_for_pipe file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=7 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunner.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=8 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.setmodule file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=9 layer=FUNCTION tokens=298 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py::ScrapyCommand.process_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/__init__.py
- rank=10 layer=FUNCTION tokens=436 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.getwithbase file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=11 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/interfaces.py::ISpiderLoader.from_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/interfaces.py
- rank=12 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py::SpiderLoader.from_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py
- rank=13 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::overridden_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=14 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::AsyncCrawlerRunner.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=15 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py
- rank=16 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py
- rank=17 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py
- rank=18 layer=FUNCTION tokens=423 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.update file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=19 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=20 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=21 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::AddonWithConfig.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py
- rank=22 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py::DummySpiderLoader.from_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py
- rank=23 layer=FUNCTION tokens=200 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::Settings.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=24 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::NotConfiguredAddon.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py
- rank=25 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::TrackingAddon.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py
- rank=26 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::SimpleAddon.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py
- rank=27 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py::pytest_configure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py
- rank=28 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::LoggedAddon.update_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py
- rank=29 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py::TestFTP._get_factory file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handler_twisted_ftp.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py::_get_project_only_cmds [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/cmdline.py]
def _get_project_only_cmds(settings: BaseSettings) -> set[str]:
    return set(_get_commands_dict(settings, inproject=True)) - set(
        _get_commands_dict(settings, inproject=False)
    )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::AddonWithFallback.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py]
            def update_settings(self, settings):
                if not settings.get(FALLBACK_SETTING):
                    settings.set(
                        FALLBACK_SETTING,
                        settings.get("SCHEDULER"),
                        "addon",
                    )
                settings["SCHEDULER"] = "AddonScheduler"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py::SpiderLoaderProtocol.from_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py]
    def from_settings(cls, settings: BaseSettings) -> Self:
        """Return an instance of the class for the given settings"""

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_logformatter.py::TestShowOrSkipMessages.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_logformatter.py]
    def setup_method(self):
        self.base_settings = {
            "LOG_LEVEL": "DEBUG",
            "ITEM_PIPELINES": {
                DropSomeItemsPipeline: 300,
            },
        }

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunner.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(self, settings: dict[str, Any] | Settings | None = None):
        super().__init__(settings)
        if not self.settings.getbool("TWISTED_REACTOR_ENABLED"):
            raise RuntimeError(
                f"{type(self).__name__} doesn't support TWISTED_REACTOR_ENABLED=False."
            )
        self._active: set[Deferred[None]] = set()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.setmodule [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
    def setmodule(
        self, module: ModuleType | str, priority: int | str = "project"
    ) -> None:
        """
        Store settings from a module with a given priority.

        This is a helper function that calls
        :meth:`~scrapy.settings.BaseSettings.set` for every globally declared
        uppercase variable of ``module`` with the provided ``priority``.

        :param module: the module or the path of the module
        :type module: types.ModuleType or str

        :param priority: the priority of the settings. Should be a key of
            :attr:`~scrapy.settings.SETTINGS_PRIORITIES` or an integer
        :type priority: str or int
        """
        self._assert_mutability()
        if isinstance(module, str):
            module = import_module(module)
        for key in dir(module):
            if key.isupper():
                self.set(key, getattr(module, key), priority)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.getwithbase [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
    def getwithbase(self, name: _SettingsKey) -> BaseSettings:
        """Get a composition of a dictionary-like setting and its `_BASE`
        counterpart.

        :param name: name of the dictionary-like setting
        :type name: str
        """
        if not isinstance(name, str):
            raise ValueError(f"Base setting key must be a string, got {name}")

        normalized_keys = {}
        obj_keys = set()

        def track_loaded_key(k: Any) -> None:
            if k not in obj_keys:
                obj_keys.add(k)
                return
            logger.warning(
                f"Setting {name} contains multiple keys that refer to the "
                f"same object: {global_object_name(k)}. Only the last one will "
                f"be kept."
            )

        def normalize_key(key: Any) -> str:
            try:
                loaded_key = load_object(key)
            except (AttributeError, TypeError, ValueError):
                loaded_key = key
            else:
                import_path = global_object_name(loaded_key)
                normalized_keys[import_path] = key
                key = import_path
            track_loaded_key(loaded_key)
            return key

        def restore_key(k: str) -> Any:
            return normalized_keys.get(k, k)

        result = dict(self[name + "_BASE"] or {})
        override = {normalize_key(k): v for k, v in (self[name] or {}).items()}
        result.update(override)
        return BaseSettings(
            {restore_key(k): v for k, v in result.items() if v is not None}
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/interfaces.py::ISpiderLoader.from_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/interfaces.py]
    def from_settings(settings):
        """Return an instance of the class for the given settings"""

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py::SpiderLoader.from_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py]
    def from_settings(cls, settings: BaseSettings) -> Self:
        return cls(settings)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::overridden_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
def overridden_settings(
    settings: Mapping[_SettingsKey, Any],
) -> Iterable[tuple[str, Any]]:
    """Return an iterable of the settings that have been overridden"""
    for name, defvalue in iter_default_settings():
        value = settings[name]
        if not isinstance(defvalue, dict) and value != defvalue:
            yield name, value

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::AsyncCrawlerRunner.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(self, settings: dict[str, Any] | Settings | None = None):
        super().__init__(settings)
        self._active: set[asyncio.Task[None]] = set()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py]
    def __init__(self, settings):
        settings.set("TEST1", f"{settings['TEST1']} + started")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py]
    def update_settings(cls, settings: BaseSettings) -> None:
        settings.setdict(cls.custom_settings or {}, priority="spider")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py::SpiderModuleAddon.update_pre_crawler_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/__init__.py]
            def update_pre_crawler_settings(cls, settings):
                settings.set(
                    "SPIDER_MODULES",
                    [module],
                    "project",
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py]
    def __init__(self, settings: BaseSettings):
        self.ignore_schemes: list[str] = settings.getlist("HTTPCACHE_IGNORE_SCHEMES")
        self.ignore_http_codes: list[int] = [
            int(x) for x in settings.getlist("HTTPCACHE_IGNORE_HTTP_CODES")
        ]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerRunnerBase.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def __init__(self, settings: dict[str, Any] | Settings | None = None):
        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)
        AddonManager.load_pre_crawler_settings(settings)
        self.settings: Settings = settings
        self.spider_loader: SpiderLoaderProtocol = get_spider_loader(settings)
        self._crawlers: set[Crawler] = set()
        self.bootstrap_failed = False

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::AddonWithConfig.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py]
        def update_settings(self, settings: BaseSettings):
            settings.update(config, priority="addon")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py::DummySpiderLoader.from_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiderloader.py]
    def from_settings(cls, settings: BaseSettings) -> Self:
        return cls()

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::NotConfiguredAddon.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py]
            def update_settings(self, settings):
                raise NotConfigured

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::TrackingAddon.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py]
            def update_settings(self, settings):
                pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::SimpleAddon.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py]
    def update_settings(self, settings):
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py::pytest_configure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py]
def pytest_configure(config):
    if config.getoption("--reactor") == "asyncio":
        # Needed on Windows to switch from proactor to selector for Twisted reactor compatibility.
        # If we decide to run tests with both, we will need to add a new option and check it here.
        set_asyncio_event_loop_policy()
    elif config.getoption("--reactor") == "none":
        install_reactor_import_hook()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py::LoggedAddon.update_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_addons.py]
            def update_settings(self, settings):
                pass

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
