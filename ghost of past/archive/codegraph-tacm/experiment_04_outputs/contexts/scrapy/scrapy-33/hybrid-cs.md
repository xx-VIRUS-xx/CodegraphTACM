# scrapy-33 :: hybrid-cs

query: Replace FailureFormatter with direct exc_info conversions in log calls

## selected nodes

- rank=1 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::logerror file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=2 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py
- rank=3 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=4 layer=FUNCTION tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::logformatter_adapter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=5 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::failure_to_exc_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=6 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.handle_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=7 layer=FUNCTION tokens=417 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::_send_catch_log_deferred file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=8 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=9 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::ResponseMiddleware.process_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py
- rank=10 layer=FUNCTION tokens=408 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::send_catch_log file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=11 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect._assert_got_tunnel_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=12 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware._robots_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=13 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=14 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py::MockFTPServer.__exit__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py
- rank=15 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py::MockDNSServer.__exit__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py
- rank=16 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline.item_completed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=17 layer=FUNCTION tokens=359 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=18 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__exit__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py
- rank=19 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_critical file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=20 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py::TestLoggingWithExtra.logger file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py
- rank=21 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::StreamLogger.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=22 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._log_tls_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=23 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_invalid_netloc file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=24 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::MySpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py
- rank=25 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py::PeriodicLog.log file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py
- rank=26 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py::ItemPipelineManager.eb file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py
- rank=27 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::private_handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py
- rank=28 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/twisted_reactor_custom_settings_select.py::log_task_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/twisted_reactor_custom_settings_select.py
- rank=29 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport.py::printf_escape file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py]
        def eb_wrapper(failure: Failure) -> None:
            case = _create_testcase(method, "errback")
            exc_info = failure.type, failure.value, failure.getTracebackObject()
            results.addError(case, exc_info)  # type: ignore[arg-type]

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.handle_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def handle_exception(self, _failure: Failure) -> None:
        logger.error(
            "An error is caught while iterating the async iterable",
            exc_info=failure_to_exc_info(_failure),
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_info [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_info(self, message: str, extra: dict | None = None):
        self.logger.info(message, extra=extra)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::ResponseMiddleware.process_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py]
            def process_exception(self, request, exception):
                calls.append("process_exception")
                return resp

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect._assert_got_tunnel_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
    def _assert_got_tunnel_error(self, log):
        assert "TunnelError" in str(log)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware._robots_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py]
    def _robots_error(self, exc: Exception, netloc: str) -> None:
        if not isinstance(exc, IgnoreRequest):
            key = f"robotstxt/exception_count/{type(exc)}"
            assert self.crawler.stats
            self.crawler.stats.inc_value(key)
        rp_dfd = self._parsers[netloc]
        assert isinstance(rp_dfd, Deferred)
        self._parsers[netloc] = None
        rp_dfd.callback(None)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_error(self, message: str, extra: dict | None = None):
        self.logger.error(message, extra=extra)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py::MockFTPServer.__exit__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py]
    def __exit__(self, exc_type, exc_value, traceback):
        rmtree(str(self.path))
        self.proc.kill()
        self.proc.communicate()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py::MockDNSServer.__exit__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py]
    def __exit__(self, exc_type, exc_value, traceback):
        self.proc.kill()
        self.proc.communicate()

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__exit__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
    def __exit__(self, exc_type, exc_value, traceback):
        if self.proc:
            self.proc.kill()
            self.proc.communicate()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_critical [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_critical(self, message: str, extra: dict | None = None):
        self.logger.critical(message, extra=extra)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py::TestLoggingWithExtra.logger [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py]
    def logger(self, log_stream: StringIO) -> Generator[logging.Logger]:
        handler = logging.StreamHandler(log_stream)
        formatter = logging.Formatter(
            '{"levelname": "%(levelname)s", "message": "%(message)s", "spider": "%(spider)s", "important_info": "%(important_info)s"}'
        )
        handler.setFormatter(formatter)
        logger = logging.getLogger("log_spider")
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        yield logger

        logger.removeHandler(handler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::StreamLogger.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py]
    def __init__(self, logger: logging.Logger, log_level: int = logging.INFO):
        self.logger: logging.Logger = logger
        self.log_level: int = log_level
        self.linebuf: str = ""

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._log_tls_info [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py]
    def _log_tls_info(self, network_stream: AsyncNetworkStream) -> None:
        if not self._tls_verbose_logging:
            return
        extra_ssl_object = network_stream.get_extra_info("ssl_object")
        if isinstance(extra_ssl_object, ssl.SSLObject):
            _log_sslobj_debug_info(extra_ssl_object)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py::PeriodicLog.log [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py]
    def log(self) -> None:
        data: dict[str, Any] = {}
        if self.ext_timing_enabled:
            data.update(self.log_timing())
        if self.ext_delta_enabled:
            data.update(self.log_delta())
        if self.ext_stats_enabled:
            data.update(self.log_crawler_stats())
        logger.info(self.encoder.encode(data))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py::ItemPipelineManager.eb [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py]
        def eb(failure: Failure) -> Failure:
            assert isinstance(failure.value, FirstError)
            return failure.value.subFailure

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::private_handle_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py]
def private_handle_error(failure):
    pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/twisted_reactor_custom_settings_select.py::log_task_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/twisted_reactor_custom_settings_select.py]
def log_task_exception(task: Task) -> None:
    try:
        task.result()
    except Exception:
        logging.exception("Crawl task failed")  # noqa: LOG015

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport.py::printf_escape [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport.py]
def printf_escape(s: str) -> str:
    return s.replace("%", "%%")
```
