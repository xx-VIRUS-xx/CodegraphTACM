# scrapy-8 :: tacm-full

query: BUG: Fix __classcell__ propagation.

## selected nodes

- rank=1 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=2 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=3 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=4 layer=FUNCTION tokens=680 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=5 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.items file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=6 layer=FUNCTION tokens=1253 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._process_spider_output file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=7 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py
- rank=8 layer=FUNCTION tokens=237 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=9 layer=FUNCTION tokens=988 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream.close file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=10 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._create_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=11 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedResponse.info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=12 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.type file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.items [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def items(self) -> Iterable[tuple[bytes, list[bytes]]]:  # type: ignore[override]
        return ((k, self.getlist(k)) for k in self.keys())

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._process_spider_output [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py]
    def _process_spider_output(  # noqa: PLR0912
        self,
        response: Response,
        result: Iterable[_T] | AsyncIterator[_T],
        start_index: int = 0,
    ) -> Generator[Deferred[Any], Any, MutableChain[_T] | MutableAsyncChain[_T]]:
        # items in this iterable do not need to go through the process_spider_output
        # chain, they went through it already from the process_spider_exception method
        recovered: MutableChain[_T] | MutableAsyncChain[_T]
        last_result_is_async = isinstance(result, AsyncIterator)
        recovered = MutableAsyncChain() if last_result_is_async else MutableChain()

        # There are three cases for the middleware: def foo, async def foo, def foo + async def foo_async.
        # 1. def foo. Sync iterables are passed as is, async ones are downgraded.
        # 2. async def foo. Sync iterables are upgraded, async ones are passed as is.
        # 3. def foo + async def foo_async. Iterables are passed to the respective method.
        # Storing methods and method tuples in the same list is weird but we should be able to roll this back
        # when we drop this compatibility feature.

        method_list = islice(self.methods["process_spider_output"], start_index, None)
        for method_index, method_pair in enumerate(method_list, start=start_index):
            if method_pair is None:
                continue
            need_upgrade = need_downgrade = False
            if isinstance(method_pair, tuple):
                # This tuple handling is only needed until _async compatibility methods are removed.
                method_sync, method_async = method_pair
                method = method_async if last_result_is_async else method_sync
            else:
                method = method_pair
                if not last_result_is_async and isasyncgenfunction(method):
                    need_upgrade = True
                elif last_result_is_async and not isasyncgenfunction(method):
                    need_downgrade = True
            try:
                if need_upgrade:
                    # Iterable -> AsyncIterator
                    result = as_async_generator(result)
                elif need_downgrade:
                    logger.warning(
                        f"Async iterable passed to {global_object_name(method)} was"
                        f" downgraded to a non-async one. This is deprecated and will"
                        f" stop working in a future version of Scrapy. Please see"
                        f" https://docs.scrapy.org/en/latest/topics/coroutines.html#for-middleware-users"
                        f" for more information."
                    )
                    assert isinstance(result, AsyncIterator)
                    # AsyncIterator -> Iterable
                    result = yield deferred_from_coro(collect_asyncgen(result))
                    if isinstance(recovered, AsyncIterator):
                        recovered_collected = yield deferred_from_coro(
                            collect_asyncgen(recovered)
                        )
                        recovered = MutableChain(recovered_collected)
                # might fail directly if the output value is not a generator
                if method in self._mw_methods_requiring_spider:
                    result = method(
                        response=response, result=result, spider=self._spider
                    )
                else:
                    result = method(response=response, result=result)
            except Exception as ex:
                exception_result: Failure | MutableChain[_T] | MutableAsyncChain[_T] = (
                    self._process_spider_exception(response, ex, method_index + 1)
                )
                if isinstance(exception_result, Failure):
                    raise
                return exception_result
            if _isiterable(result):
                result = self._evaluate_iterable(
                    response, result, method_index + 1, recovered
                )
            else:
                if iscoroutine(result):
                    result.close()  # Silence warning about not awaiting
                    msg = (
                        f"{global_object_name(method)} must be an asynchronous "
                        f"generator (i.e. use yield)"
                    )
                else:
                    msg = (
                        f"{global_object_name(method)} must return an iterable, got "
                        f"{type(result)}"
                    )
                raise _InvalidOutput(msg)
            last_result_is_async = isinstance(result, AsyncIterator)

        if last_result_is_async:
            return MutableAsyncChain(result, recovered)
        return MutableChain(result, recovered)  # type: ignore[arg-type]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py::MyItem.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_item.py]
            def __init__(self, *args, **kwargs):  # pylint: disable=useless-parent-delegation
                # This call to super() trigger the __classcell__ propagation
                # requirement. When not done properly raises an error:
                # TypeError: __class__ set to <class '__main__.MyItem'>
                # defining 'MyItem' as <class '__main__.MyItem'>
                super().__init__(*args, **kwargs)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream.close [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py]
    def close(
        self,
        reason: StreamCloseReason,
        errors: Sequence[BaseException] | None = None,
        from_protocol: bool = False,
    ) -> None:
        """Based on the reason sent we will handle each case."""
        if self.metadata["stream_closed_server"]:
            raise StreamClosedError(self.stream_id)

        if not isinstance(reason, StreamCloseReason):
            raise TypeError(
                f"Expected StreamCloseReason, received {reason.__class__.__qualname__}"
            )

        # Have default value of errors as an empty list as
        # some cases can add a list of exceptions
        errors = errors or ()

        if not from_protocol:
            self._protocol.pop_stream(self.stream_id)

        self.metadata["stream_closed_server"] = True

        # We do not check for Content-Length or Transfer-Encoding in response headers
        # and add `partial` flag as in HTTP/1.1 as 'A request or response that includes
        # a payload body can include a content-length header field' (RFC 7540 - Section 8.1.2.6)

        # NOTE: Order of handling the events is important here
        # As we immediately cancel the request when maxsize is exceeded while
        # receiving DATA_FRAME's when we have received the headers (not
        # having Content-Length)
        if reason in {
            StreamCloseReason.MAXSIZE_EXCEEDED,
            StreamCloseReason.MAXSIZE_EXCEEDED_ACTUAL,
        }:
            expected_size = int(
                self._response["headers"].get(
                    b"Content-Length", self._response["flow_controlled_size"]
                )
            )
            error_msg = get_maxsize_msg(
                expected_size,
                self._download_maxsize,
                self._request,
                expected=reason == StreamCloseReason.MAXSIZE_EXCEEDED,
            )
            logger.error(error_msg)
            self._deferred_response.errback(DownloadCancelledError(error_msg))

        elif reason is StreamCloseReason.ENDED:
            self._fire_response_deferred()

        # Stream was abruptly ended here
        elif reason is StreamCloseReason.CANCELLED:
            # Client has cancelled the request. Remove all the data
            # received and fire the response deferred with no flags set

            # NOTE: The data is already flushed in Stream.reset_stream() called
            # immediately when the stream needs to be cancelled

            # There maybe no :status in headers, we make
            # HTTP Status Code: 499 - Client Closed Request
            self._response["headers"][":status"] = "499"
            self._fire_response_deferred()

        elif reason is StreamCloseReason.RESET:
            self._deferred_response.errback(
                ResponseFailed(
                    [
                        Failure(
                            f"Remote peer {self._protocol.metadata['ip_address']} sent RST_STREAM",
                            ProtocolError,
                        )
                    ]
                )
            )

        elif reason is StreamCloseReason.CONNECTION_LOST:
            self._deferred_response.errback(ResponseFailed(errors))

        elif reason is StreamCloseReason.INACTIVE:
            errors = (InactiveStreamClosed(self._request), *errors)
            self._deferred_response.errback(ResponseFailed(errors))

        else:
            assert reason is StreamCloseReason.INVALID_HOSTNAME
            self._deferred_response.errback(
                InvalidHostname(
                    self._request,
                    str(self._protocol.metadata["uri"].host, "utf-8"),
                    f"{self._protocol.metadata['ip_address']}:{self._protocol.metadata['uri'].port}",
                )
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._create_spider [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def _create_spider(self, *args: Any, **kwargs: Any) -> Spider:
        return self.spidercls.from_crawler(self, *args, **kwargs)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedResponse.info [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def info(self) -> Self:
        return self

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.type [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def type(self) -> str:
        return self.get_type()
```
