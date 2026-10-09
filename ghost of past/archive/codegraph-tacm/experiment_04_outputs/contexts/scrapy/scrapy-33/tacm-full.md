# scrapy-33 :: tacm-full

query: Replace FailureFormatter with direct exc_info conversions in log calls

## selected nodes

- rank=1 layer=FUNCTION tokens=417 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::_send_catch_log_deferred file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=2 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::logerror file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=3 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py
- rank=4 layer=FUNCTION tokens=200 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_request_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=5 layer=FUNCTION tokens=212 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_spider_attr file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=6 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline.item_completed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=7 layer=FUNCTION tokens=207 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_setting file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=8 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_invalid_netloc file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=9 layer=FUNCTION tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::logformatter_adapter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=10 layer=FUNCTION tokens=359 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=11 layer=FUNCTION tokens=408 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::send_catch_log file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=12 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.handle_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=13 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=14 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=15 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::MySpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py
- rank=16 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_commands.py::TestCommandCrawlerProcess._replace_custom_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_commands.py
- rank=17 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::sanitize_module_name file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py
- rank=18 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::failure_to_exc_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=19 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::StreamLogger.write file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=20 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=21 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=22 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedResponse.info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::_send_catch_log_deferred [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py]
def _send_catch_log_deferred(
    signal: TypingAny,
    sender: TypingAny,
    *arguments: TypingAny,
    **named: TypingAny,
) -> Generator[Deferred[TypingAny], TypingAny, list[tuple[TypingAny, TypingAny]]]:
    def logerror(failure: Failure, recv: TypingAny) -> Failure:
        if dont_log is None or not isinstance(failure.value, dont_log):
            logger.error(
                "Error caught on signal handler: %(receiver)s",
                {"receiver": recv},
                exc_info=failure_to_exc_info(failure),
                extra={"spider": spider},
            )
        return failure

    dont_log = named.pop("dont_log", None)
    spider = named.get("spider")
    dfds: list[Deferred[tuple[TypingAny, TypingAny]]] = []
    for receiver in liveReceivers(getAllReceivers(sender, signal)):
        d: Deferred[TypingAny] = _maybeDeferred_coro(
            robustApply,
            True,
            receiver,
            *arguments,
            signal=signal,
            sender=sender,
            **named,
        )
        d.addErrback(logerror, receiver)
        # TODO https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/cell-var-from-loop.html
        d2: Deferred[tuple[TypingAny, TypingAny]] = d.addBoth(
            lambda result: (
                receiver,  # pylint: disable=cell-var-from-loop  # noqa: B023
                result,
            )
        )
        dfds.append(d2)

    results = yield DeferredList(dfds)
    return [result[1] for result in results]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::logerror [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py]
    def logerror(failure: Failure, recv: TypingAny) -> Failure:
        if dont_log is None or not isinstance(failure.value, dont_log):
            logger.error(
                "Error caught on signal handler: %(receiver)s",
                {"receiver": recv},
                exc_info=failure_to_exc_info(failure),
                extra={"spider": spider},
            )
        return failure

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py]
        def log_failure(msg: str) -> None:
            logger.error(msg, exc_info=True, extra={"spider": spider})  # noqa: LOG014

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_request_meta [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py]
    def _test_compression_bomb_request_meta(self, compression_id):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider("scrapytest.org")
        mw = HttpCompressionMiddleware.from_crawler(crawler)
        mw.open_spider(spider)

        response = self._getresponse(f"bomb-{compression_id}")
        response.meta["download_maxsize"] = 1_000_000
        with pytest.raises(IgnoreRequest) as exc_info:
            mw.process_response(response.request, response)
        assert exc_info.value.__cause__.decompressed_size < 1_100_000

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_spider_attr [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py]
    def _test_compression_bomb_spider_attr(self, compression_id):
        class DownloadMaxSizeSpider(Spider):
            download_maxsize = 1_000_000

        crawler = get_crawler(DownloadMaxSizeSpider)
        spider = crawler._create_spider("scrapytest.org")
        mw = HttpCompressionMiddleware.from_crawler(crawler)
        mw.open_spider(spider)

        response = self._getresponse(f"bomb-{compression_id}")
        with pytest.raises(IgnoreRequest) as exc_info:
            mw.process_response(response.request, response)
        assert exc_info.value.__cause__.decompressed_size < 1_100_000

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline.item_completed [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def item_completed(
        self, results: list[FileInfoOrError], item: Any, info: SpiderInfo
    ) -> Any:
        """Called per item when all media requests has been processed"""
        if self.LOG_FAILED_RESULTS:
            for ok, value in results:
                if not ok:
                    assert isinstance(value, Failure)
                    logger.error(
                        "%(class)s found errors processing %(item)s",
                        {"class": self.__class__.__name__, "item": item},
                        exc_info=failure_to_exc_info(value),
                        extra={"spider": info.spider},
                    )
        return item

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_setting [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py]
    def _test_compression_bomb_setting(self, compression_id):
        settings = {"DOWNLOAD_MAXSIZE": 1_000_000}
        crawler = get_crawler(Spider, settings_dict=settings)
        spider = crawler._create_spider("scrapytest.org")
        mw = HttpCompressionMiddleware.from_crawler(crawler)
        mw.open_spider(spider)

        response = self._getresponse(f"bomb-{compression_id}")  # 11_511_612 B
        with pytest.raises(IgnoreRequest) as exc_info:
            mw.process_response(response.request, response)
        assert exc_info.value.__cause__.decompressed_size < 1_100_000

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_invalid_netloc [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
    async def _check_invalid_netloc(client: H2ClientProtocol, url: str) -> None:
        from scrapy.core.http2.stream import InvalidHostname  # noqa: PLC0415

        request = Request(url)
        with pytest.raises(InvalidHostname) as exc_info:
            await make_request(client, request)
        error_msg = str(exc_info.value)
        assert "localhost" in error_msg
        assert "127.0.0.1" in error_msg
        assert str(request) in error_msg

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::logformatter_adapter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py]
def logformatter_adapter(
    logkws: LogFormatterResult,
) -> tuple[int, str, dict[str, Any] | tuple[Any, ...]]:
    """
    Helper that takes the dictionary output from the methods in LogFormatter
    and adapts it into a tuple of positional arguments for logger.log calls,
    handling backward compatibility as well.
    """

    level = logkws.get("level", logging.INFO)
    message = logkws.get("msg") or ""
    # NOTE: This also handles 'args' being an empty dict, that case doesn't
    # play well in logger.log calls
    args = cast("dict[str, Any]", logkws) if not logkws.get("args") else logkws["args"]

    return (level, message, args)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py]
    def handle_spider_error(
        self,
        _failure: Failure,
        request: Request,
        response: Response | Failure,
        spider: Spider | None = None,
    ) -> None:
        """Handle an exception raised by a spider callback or errback."""
        assert self.crawler.spider
        exc = _failure.value
        if isinstance(exc, CloseSpider):
            assert self.crawler.engine is not None  # typing
            _schedule_coro(
                self.crawler.engine.close_spider_async(reason=exc.reason or "cancelled")
            )
            return
        logkws = self.logformatter.spider_error(
            _failure, request, response, self.crawler.spider
        )
        logger.log(
            *logformatter_adapter(logkws),
            exc_info=failure_to_exc_info(_failure),
            extra={"spider": self.crawler.spider},
        )
        self.signals.send_catch_log(
            signal=signals.spider_error,
            failure=_failure,
            response=response,
            spider=self.crawler.spider,
        )
        assert self.crawler.stats
        self.crawler.stats.inc_value("spider_exceptions/count")
        self.crawler.stats.inc_value(
            f"spider_exceptions/{_failure.value.__class__.__name__}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::send_catch_log [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py]
def send_catch_log(
    signal: TypingAny = Any,
    sender: TypingAny = Anonymous,
    *arguments: TypingAny,
    **named: TypingAny,
) -> list[tuple[TypingAny, TypingAny]]:
    """Like ``pydispatcher.robust.sendRobust()`` but it also logs errors and returns
    Failures instead of exceptions.
    """
    dont_log = named.pop("dont_log", ())
    dont_log = tuple(dont_log) if isinstance(dont_log, Sequence) else (dont_log,)
    dont_log += (StopDownload,)
    spider = named.get("spider")
    responses: list[tuple[TypingAny, TypingAny]] = []
    for receiver in liveReceivers(getAllReceivers(sender, signal)):
        result: TypingAny
        try:
            response = robustApply(
                receiver, *arguments, signal=signal, sender=sender, **named
            )
            if isinstance(response, Deferred):
                logger.error(
                    "Cannot return deferreds from signal handler: %(receiver)s",
                    {"receiver": receiver},
                    extra={"spider": spider},
                )
        except dont_log:
            result = Failure()
        except Exception:
            result = Failure()
            logger.error(
                "Error caught on signal handler: %(receiver)s",
                {"receiver": receiver},
                exc_info=True,
                extra={"spider": spider},
            )
        else:
            result = response
        responses.append((receiver, result))
    return responses

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.handle_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def handle_exception(self, _failure: Failure) -> None:
        logger.error(
            "An error is caught while iterating the async iterable",
            exc_info=failure_to_exc_info(_failure),
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py]
        def eb_wrapper(failure: Failure) -> None:
            case = _create_testcase(method, "errback")
            exc_info = failure.type, failure.value, failure.getTracebackObject()
            results.addError(case, exc_info)  # type: ignore[arg-type]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::MySpider.start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py]
            async def start(self):
                info_count_start = crawler.stats.get_value("log_count/INFO")
                logging.debug("debug message")  # noqa: LOG015
                logging.info("info message")  # noqa: LOG015
                logging.warning("warning message")  # noqa: LOG015
                logging.error("error message")  # noqa: LOG015
                nonlocal info_count
                info_count = (
                    crawler.stats.get_value("log_count/INFO") - info_count_start
                )
                return
                yield

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_commands.py::TestCommandCrawlerProcess._replace_custom_settings [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_commands.py]
    def _replace_custom_settings(
        proj_mod_path: Path, spider_name: str, text: str
    ) -> None:
        """Replace custom_settings in the given spider file with the given text."""
        spider_path = proj_mod_path / "spiders" / f"{spider_name}.py"
        with spider_path.open("r+", encoding="utf-8") as f:
            content = f.read()
            content = content.replace(
                "custom_settings = {}", f"custom_settings = {text}"
            )
            f.seek(0)
            f.write(content)
            f.truncate()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::sanitize_module_name [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py]
def sanitize_module_name(module_name: str) -> str:
    """Sanitize the given module name, by replacing dashes and points
    with underscores and prefixing it with a letter if it doesn't start
    with one
    """
    module_name = module_name.replace("-", "_").replace(".", "_")
    if module_name[0] not in string.ascii_letters:
        module_name = "a" + module_name
    return module_name

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::failure_to_exc_info [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py]
def failure_to_exc_info(
    failure: Failure,
) -> tuple[type[BaseException], BaseException, TracebackType | None] | None:
    """Extract exc_info from Failure instances"""
    if isinstance(failure, Failure):
        assert failure.type
        assert failure.value
        return (
            failure.type,
            failure.value,
            cast("TracebackType | None", failure.getTracebackObject()),
        )
    return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::StreamLogger.write [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py]
    def write(self, buf: str) -> None:
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedResponse.info [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def info(self) -> Self:
        return self
```
