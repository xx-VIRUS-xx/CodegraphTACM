# scrapy-32 :: tacm-rerank

query: fixed CrawlerProcess when settings are passed as dicts

## selected nodes

- rank=1 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcess.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=2 layer=FUNCTION tokens=680 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=3 layer=FUNCTION tokens=200 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::Settings.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=4 layer=FUNCTION tokens=304 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.getbool file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=5 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=6 layer=FUNCTION tokens=213 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_reactorless_default_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=7 layer=FUNCTION tokens=138 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::log_scrapy_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=8 layer=FUNCTION tokens=333 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_reactor_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=9 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py::TestCrawlerProcessSubprocess.script_dir file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py
- rank=10 layer=FUNCTION tokens=237 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=11 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/reactorless.py::is_reactorless file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/reactorless.py
- rank=12 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/closespider.py::CloseSpider.spider_opened_no_item file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/closespider.py
- rank=13 layer=FUNCTION tokens=299 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/json_request.py::JsonRequest.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/json_request.py
- rank=14 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/json_request.py::JsonRequest.replace file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/json_request.py
- rank=15 layer=FUNCTION tokens=137 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py::SignalManager.send_catch_log file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py
- rank=16 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::deferred_f_from_coro_f file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=17 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py::H2ClientProtocol.settings_acknowledged file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py
- rank=18 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._storage file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.getbool [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
    def getbool(self, name: _SettingsKey, default: bool = False) -> bool:
        """
        Get a setting value as a boolean.

        ``1``, ``'1'``, `True`` and ``'True'`` return ``True``,
        while ``0``, ``'0'``, ``False``, ``'False'`` and ``None`` return ``False``.

        For example, settings populated through environment variables set to
        ``'0'`` will return ``False`` when using this method.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
        got = self.get(name, default)
        try:
            return bool(int(got))
        except ValueError:
            if got in {"True", "true"}:
                return True
            if got in {"False", "false"}:
                return False
            raise ValueError(
                "Supported values for boolean settings "
                "are 0/1, True/False, '0'/'1', "
                "'True'/'False' and 'true'/'false'"
            ) from None

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::log_scrapy_info [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py]
def log_scrapy_info(settings: Settings) -> None:
    logger.info(
        "Scrapy %(version)s started (bot: %(bot)s)",
        {"version": scrapy.__version__, "bot": settings["BOT_NAME"]},
    )
    software: list[str] = settings.getlist("LOG_VERSIONS")
    if not software:
        return
    versions = pprint.pformat(dict(get_versions(software)), sort_dicts=False)
    logger.info(f"Versions:\n{versions}")

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py::TestCrawlerProcessSubprocess.script_dir [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler_subprocess.py]
    def script_dir(self) -> Path:
        return self.get_script_dir("CrawlerProcess")

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/reactorless.py::is_reactorless [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/reactorless.py]
def is_reactorless() -> bool:
    """Check if we are running in the reactorless mode, i.e. with
    :setting:`TWISTED_REACTOR_ENABLED` set to ``False``.

    As this checks the runtime state and not the setting itself, it can be
    wrong when executed very early, before the reactor and/or the asyncio event
    loop are initialized.

    .. note:: As this function uses
        :func:`scrapy.utils.asyncio.is_asyncio_available()`, it has the same
        limitations for detecting a running asyncio event loop as that one.

    .. versionadded:: VERSION
    """
    return is_asyncio_available() and not is_reactor_installed()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/closespider.py::CloseSpider.spider_opened_no_item [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/closespider.py]
    def spider_opened_no_item(self, spider: Spider) -> None:
        self.task_no_item = create_looping_call(self._count_items_produced)
        self.task_no_item.start(self.timeout_no_item, now=False)

        logger.info(
            f"Spider will stop when no items are produced after "
            f"{self.timeout_no_item} seconds."
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/json_request.py::JsonRequest.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/json_request.py]
    def __init__(
        self, *args: Any, dumps_kwargs: dict[str, Any] | None = None, **kwargs: Any
    ) -> None:
        dumps_kwargs = copy.deepcopy(dumps_kwargs) if dumps_kwargs is not None else {}
        dumps_kwargs.setdefault("sort_keys", True)
        self._dumps_kwargs: dict[str, Any] = dumps_kwargs

        body_passed = kwargs.get("body") is not None
        data: Any = kwargs.pop("data", None)
        data_passed: bool = data is not None

        if body_passed and data_passed:
            warnings.warn(
                "Both body and data passed. data will be ignored", stacklevel=2
            )
        elif not body_passed and data_passed:
            kwargs["body"] = self._dumps(data)
            if "method" not in kwargs:
                kwargs["method"] = "POST"

        super().__init__(*args, **kwargs)
        self.headers.setdefault("Content-Type", "application/json")
        self.headers.setdefault(
            "Accept", "application/json, text/javascript, */*; q=0.01"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/json_request.py::JsonRequest.replace [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/json_request.py]
    def replace(
        self, *args: Any, cls: type[Request] | None = None, **kwargs: Any
    ) -> Request:
        body_passed = kwargs.get("body") is not None
        data: Any = kwargs.pop("data", None)
        data_passed: bool = data is not None

        if body_passed and data_passed:
            warnings.warn(
                "Both body and data passed. data will be ignored", stacklevel=2
            )
        elif not body_passed and data_passed:
            kwargs["body"] = self._dumps(data)

        return super().replace(*args, cls=cls, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py::SignalManager.send_catch_log [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py]
    def send_catch_log(self, signal: Any, **kwargs: Any) -> list[tuple[Any, Any]]:
        """
        Send a signal, catch exceptions and log them.

        The keyword arguments are passed to the signal handlers (connected
        through the :meth:`connect` method).
        """
        kwargs.setdefault("sender", self.sender)
        return _signal.send_catch_log(signal, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::deferred_f_from_coro_f [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py]
def deferred_f_from_coro_f(
    coro_f: Callable[_P, Awaitable[_T]],
) -> Callable[_P, Deferred[_T]]:
    """Convert a coroutine function into a function that returns a Deferred.

    The coroutine function will be called at the time when the wrapper is called. Wrapper args will be passed to it.
    This is useful for callback chains, as callback functions are called with the previous callback result.
    """

    @wraps(coro_f)
    def f(*coro_args: _P.args, **coro_kwargs: _P.kwargs) -> Deferred[_T]:
        return deferred_from_coro(coro_f(*coro_args, **coro_kwargs))

    return f

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py::H2ClientProtocol.settings_acknowledged [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/protocol.py]
    def settings_acknowledged(self, event: SettingsAcknowledged) -> None:
        self.metadata["settings_acknowledged"] = True

        # Send off all the pending requests as now we have
        # established a proper HTTP/2 connection
        self._send_pending_requests()

        # Update certificate when our HTTP/2 connection is established
        assert self.transport is not None  # typing
        self.metadata["certificate"] = Certificate(self.transport.getPeerCertificate())

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase._storage [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py]
    def _storage(self, **new_settings: Any):
        with self._middleware(**new_settings) as mw:
            yield mw.storage, mw.crawler
```
