# scrapy-33 :: minilm

query: Replace FailureFormatter with direct exc_info conversions in log calls

## selected nodes

- rank=1 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py
- rank=2 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::failure_to_exc_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=3 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::logerror file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=4 layer=FUNCTION tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.item_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py
- rank=5 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithErrback.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=6 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.handle_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=7 layer=FUNCTION tokens=417 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::_send_catch_log_deferred file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=8 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.spider_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py
- rank=9 layer=FUNCTION tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::logformatter_adapter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=10 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::ProcessSpiderInputSpiderWithErrback.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=11 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=12 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.download_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py
- rank=13 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._log_dataloss_warning file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=14 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py::TestLoggingWithExtra.logger file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py
- rank=15 layer=FUNCTION tokens=212 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.dropped file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py
- rank=16 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=17 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::RecoverySpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=18 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::eb file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=19 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py::ItemPipelineManager.eb file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py
- rank=20 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=21 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/mail.py::MailSender._sent_failed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/mail.py
- rank=22 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._handle_failure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=23 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SingleRequestSpider.on_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=24 layer=FUNCTION tokens=408 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::send_catch_log file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=25 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_signal.py::TestSendCatchLogDeferred._get_result file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_signal.py
- rank=26 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py
- rank=27 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=28 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::get_dataloss_msg file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py
- rank=29 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FeedExporter._exporter_supported file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py
- rank=30 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::MethodsSpider.handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py
- rank=31 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py]
        def log_failure(msg: str) -> None:
            logger.error(msg, exc_info=True, extra={"spider": spider})  # noqa: LOG014

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.item_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py]
    def item_error(
        self,
        item: Any,
        exception: BaseException,
        response: Response | Failure | None,
        spider: Spider,
    ) -> LogFormatterResult:
        """Logs a message when an item causes an error while it is passing
        through the item pipeline.
        """
        return {
            "level": logging.ERROR,
            "msg": ITEMERRORMSG,
            "args": {
                "item": item,
            },
        }

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithErrback.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def errback(self, failure):
        self.logger.info("[errback] status %i", failure.value.response.status)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.spider_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py]
    def spider_error(
        self,
        failure: Failure,
        request: Request,
        response: Response | Failure,
        spider: Spider,
    ) -> LogFormatterResult:
        """Logs an error message from a spider."""
        return {
            "level": logging.ERROR,
            "msg": SPIDERERRORMSG,
            "args": {
                "request": request,
                "referer": referer_str(request),
            },
        }

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::ProcessSpiderInputSpiderWithErrback.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py]
    def errback(self, failure):
        self.logger.info("Got a Failure on the Request errback")
        return {"from": "errback"}

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_error(self, message: str, extra: dict | None = None):
        self.logger.error(message, extra=extra)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.download_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py]
    def download_error(
        self,
        failure: Failure,
        request: Request,
        spider: Spider,
        errmsg: str | None = None,
    ) -> LogFormatterResult:
        """Logs a download error message from a spider (typically coming from
        the engine).
        """
        args: dict[str, Any] = {"request": request}
        if errmsg:
            msg = DOWNLOADERRORMSG_LONG
            args["errmsg"] = errmsg
        else:
            msg = DOWNLOADERRORMSG_SHORT
        return {
            "level": logging.ERROR,
            "msg": msg,
            "args": args,
        }

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._log_dataloss_warning [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py]
    def _log_dataloss_warning(self, url: str) -> None:
        if self._fail_on_dataloss_warned:
            return
        logger.warning(get_dataloss_msg(url))
        self._fail_on_dataloss_warned = True

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.dropped [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py]
    def dropped(
        self,
        item: Any,
        exception: BaseException,
        response: Response | Failure | None,
        spider: Spider,
    ) -> LogFormatterResult:
        """Logs a message when an item is dropped while it is passing through the item pipeline."""
        if (level := getattr(exception, "log_level", None)) is None:
            level = spider.crawler.settings["DEFAULT_DROPITEM_LOG_LEVEL"]
        if isinstance(level, str):
            level = getattr(logging, level)
        return {
            "level": level,
            "msg": DROPPEDMSG,
            "args": {
                "exception": exception,
                "item": item,
            },
        }

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py]
        def eb_wrapper(failure: Failure) -> None:
            case = _create_testcase(method, "errback")
            exc_info = failure.type, failure.value, failure.getTracebackObject()
            results.addError(case, exc_info)  # type: ignore[arg-type]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::RecoverySpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py]
    def parse(self, response):
        yield {"test": 1}
        self.logger.info("DONT_FAIL: %s", response.meta.get("dont_fail"))
        if not response.meta.get("dont_fail"):
            raise TabError

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::eb [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py]
    def eb(failure: Failure) -> Failure:
        assert isinstance(failure.value, FirstError)
        return failure.value.subFailure

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py::ItemPipelineManager.eb [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py]
        def eb(failure: Failure) -> Failure:
            assert isinstance(failure.value, FirstError)
            return failure.value.subFailure

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py]
    def _errback(self, failure: Failure) -> Iterable[Any]:
        rule = self._rules[cast("int", failure.request.meta["rule"])]  # type: ignore[attr-defined]
        return self._handle_failure(
            failure, cast("Callable[[Failure], Any]", rule.errback)
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/mail.py::MailSender._sent_failed [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/mail.py]
    def _sent_failed(
        self,
        failure: Failure,
        to: list[str],
        cc: list[str],
        subject: str,
        nattachs: int,
    ) -> Failure:
        errstr = str(failure.value)
        logger.error(
            "Unable to send mail: To=%(mailto)s Cc=%(mailcc)s "
            'Subject="%(mailsubject)s" Attachs=%(mailattachs)d'
            "- %(mailerr)s",
            {
                "mailto": to,
                "mailcc": cc,
                "mailsubject": subject,
                "mailattachs": nattachs,
                "mailerr": errstr,
            },
        )
        return failure

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._handle_failure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py]
    def _handle_failure(
        self, failure: Failure, errback: Callable[[Failure], Any] | None
    ) -> Iterable[Any]:
        if errback:
            results = errback(failure) or ()
            yield from iterate_spider_output(results)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SingleRequestSpider.on_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def on_error(self, failure):
        self.meta["failure"] = failure
        if callable(self.errback_func):
            return self.errback_func(failure)
        return None

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_signal.py::TestSendCatchLogDeferred._get_result [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_signal.py]
    def _get_result(self, signal, *a, **kw):
        return send_catch_log_deferred(signal, *a, **kw)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::handle_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py]
def handle_error(failure):
    pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_info [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_info(self, message: str, extra: dict | None = None):
        self.logger.info(message, extra=extra)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::get_dataloss_msg [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py]
def get_dataloss_msg(url: str) -> str:
    return (
        f"Got data loss in {url}. If you want to process broken "
        f"responses set the setting DOWNLOAD_FAIL_ON_DATALOSS = False"
        f" -- This message won't be shown in further requests"
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FeedExporter._exporter_supported [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py]
    def _exporter_supported(self, format_: str) -> bool:
        if format_ in self.exporters:
            return True
        logger.error("Unknown feed format: %(format)s", {"format": format_})
        return False

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::MethodsSpider.handle_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py]
    def handle_error(self, failure):
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def errback(self, failure):
        self.meta["failure"] = failure
```
