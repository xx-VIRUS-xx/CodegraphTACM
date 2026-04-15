# scrapy-33 :: hybrid

query: Replace FailureFormatter with direct exc_info conversions in log calls

## selected nodes

- rank=1 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py
- rank=2 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::logerror file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=3 layer=FUNCTION tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::logformatter_adapter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=4 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.handle_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=5 layer=FUNCTION tokens=417 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::_send_catch_log_deferred file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=6 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::failure_to_exc_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=7 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=8 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py::TestLoggingWithExtra.logger file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py
- rank=9 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline.item_completed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=10 layer=FUNCTION tokens=359 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=11 layer=FUNCTION tokens=408 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::send_catch_log file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=12 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=13 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::StreamLogger.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=14 layer=FUNCTION tokens=132 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.log file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py
- rank=15 layer=FUNCTION tokens=180 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::MySpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py
- rank=16 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithErrback.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=17 layer=FUNCTION tokens=245 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::_ResponseReader.connectionLost file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=18 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcessBase._log_kill file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=19 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py::MockDNSServer.__exit__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py
- rank=20 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py::PeriodicLog.log file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/periodic_log.py
- rank=21 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=22 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__exit__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py
- rank=23 layer=FUNCTION tokens=399 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine._start_scheduled_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py
- rank=24 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::AlternativeCallbacksSpider.alt_callback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py]
        def log_failure(msg: str) -> None:
            logger.error(msg, exc_info=True, extra={"spider": spider})  # noqa: LOG014

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py]
        def eb_wrapper(failure: Failure) -> None:
            case = _create_testcase(method, "errback")
            exc_info = failure.type, failure.value, failure.getTracebackObject()
            results.addError(case, exc_info)  # type: ignore[arg-type]

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_info [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_info(self, message: str, extra: dict | None = None):
        self.logger.info(message, extra=extra)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::StreamLogger.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py]
    def __init__(self, logger: logging.Logger, log_level: int = logging.INFO):
        self.logger: logging.Logger = logger
        self.log_level: int = log_level
        self.linebuf: str = ""

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.log [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py]
    def log(self, message: Any, level: int = logging.DEBUG, **kw: Any) -> None:
        """Log the given message at the given log level

        This helper wraps a log call to the logger within the spider, but you
        can use it directly (e.g. Spider.logger.info('msg')) or use any other
        Python logger too.
        """
        self.logger.log(level, message, **kw)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithErrback.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def errback(self, failure):
        self.logger.info("[errback] status %i", failure.value.response.status)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::_ResponseReader.connectionLost [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def connectionLost(self, reason: Failure = connectionDone) -> None:
        if self._finished.called:
            return

        if reason.check(ResponseDone):
            self._finish_response()
            return

        if reason.check(PotentialDataLoss):
            self._finish_response(flags=["partial"])
            return

        if reason.check(ResponseFailed) and any(
            r.check(_DataLoss)
            for r in reason.value.reasons  # type: ignore[union-attr]
        ):
            if not self._fail_on_dataloss:
                self._finish_response(flags=["dataloss"])
                return

            exc = ResponseDataLossError()
            exc.__cause__ = reason.value
            reason = Failure(exc)

        self._finished.errback(reason)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::CrawlerProcessBase._log_kill [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def _log_kill(signum: int) -> None:
        signame = signal_names[signum]
        logger.info(
            "Received %(signame)s twice, forcing unclean shutdown", {"signame": signame}
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py::MockDNSServer.__exit__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/dns.py]
    def __exit__(self, exc_type, exc_value, traceback):
        self.proc.kill()
        self.proc.communicate()

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_error(self, message: str, extra: dict | None = None):
        self.logger.error(message, extra=extra)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__exit__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
    def __exit__(self, exc_type, exc_value, traceback):
        if self.proc:
            self.proc.kill()
            self.proc.communicate()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine._start_scheduled_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py]
    def _start_scheduled_request(self) -> bool:
        assert self._slot is not None  # typing
        assert self.spider is not None  # typing

        request = self._slot.scheduler.next_request()
        if request is None:
            self.signals.send_catch_log(signals.scheduler_empty)
            return False

        d: Deferred[Response | Request] = self._download(request)
        d.addBoth(self._handle_downloader_output, request)
        d.addErrback(
            lambda f: logger.info(
                "Error while handling downloader output",
                exc_info=failure_to_exc_info(f),
                extra={"spider": self.spider},
            )
        )

        def _remove_request(_: Any) -> None:
            assert self._slot
            self._slot.remove_request(request)

        d2: Deferred[None] = d.addBoth(_remove_request)
        d2.addErrback(
            lambda f: logger.info(
                "Error while removing request from slot",
                exc_info=failure_to_exc_info(f),
                extra={"spider": self.spider},
            )
        )
        slot = self._slot
        d2.addBoth(lambda _: slot.nextcall.schedule())
        d2.addErrback(
            lambda f: logger.info(
                "Error while scheduling new request",
                exc_info=failure_to_exc_info(f),
                extra={"spider": self.spider},
            )
        )
        return True

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::AlternativeCallbacksSpider.alt_callback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py]
    def alt_callback(self, response, foo=None):
        self.logger.info("alt_callback was invoked with foo=%s", foo)
```
