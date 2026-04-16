# scrapy-33 :: codesearch

query: Replace FailureFormatter with direct exc_info conversions in log calls

## selected nodes

- rank=1 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::failure_to_exc_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=2 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::logerror file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=3 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=4 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=5 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py::ItemPipelineManager.eb file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py
- rank=6 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::private_handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py
- rank=7 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py
- rank=8 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::eb file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=9 layer=FUNCTION tokens=199 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::logformatter_adapter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=10 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::ResponseMiddleware.process_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py
- rank=11 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.handle_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=12 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=13 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::InvalidProcessExceptionMiddleware.process_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py
- rank=14 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py
- rank=15 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SingleRequestSpider.on_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=16 layer=FUNCTION tokens=54 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::MethodsSpider.handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py
- rank=17 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_critical file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=18 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware._robots_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=19 layer=FUNCTION tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py::format_engine_status file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py
- rank=20 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_fail file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=21 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::DeprecatedSpiderArgMiddleware.process_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py
- rank=22 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=23 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::BytesReceivedCallbackSpider.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=24 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithErrback.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=25 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/twisted_reactor_custom_settings_select.py::log_task_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/twisted_reactor_custom_settings_select.py
- rank=26 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/reactorless_custom_settings.py::log_task_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/reactorless_custom_settings.py
- rank=27 layer=FUNCTION tokens=214 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::wrap_twisted_exceptions file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py
- rank=28 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_uri_params.py::TestURIParams._crawler_feed_exporter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_uri_params.py
- rank=29 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py::DownloaderStats.process_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py
- rank=30 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=31 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_misc/test_return_with_argument_inside_generator.py::_indentation_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_misc/test_return_with_argument_inside_generator.py
- rank=32 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.spider_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py
- rank=33 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._handle_failure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=34 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::ProcessSpiderInputSpiderWithErrback.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=35 layer=FUNCTION tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::DelaySpider.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=36 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_warning file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=37 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/mail.py::MailSender._sent_failed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/mail.py
- rank=38 layer=FUNCTION tokens=156 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.item_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py
- rank=39 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py::MockFTPServer.__exit__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py
- rank=40 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=41 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__exit__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py
- rank=42 layer=FUNCTION tokens=43 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pqueues.py::QueueProtocol.close file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pqueues.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py]
        def eb_wrapper(failure: Failure) -> None:
            case = _create_testcase(method, "errback")
            exc_info = failure.type, failure.value, failure.getTracebackObject()
            results.addError(case, exc_info)  # type: ignore[arg-type]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_error(self, message: str, extra: dict | None = None):
        self.logger.error(message, extra=extra)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py::ItemPipelineManager.eb [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/__init__.py]
        def eb(failure: Failure) -> Failure:
            assert isinstance(failure.value, FirstError)
            return failure.value.subFailure

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::private_handle_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py]
def private_handle_error(failure):
    pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py]
        def log_failure(msg: str) -> None:
            logger.error(msg, exc_info=True, extra={"spider": spider})  # noqa: LOG014

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::eb [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py]
    def eb(failure: Failure) -> Failure:
        assert isinstance(failure.value, FirstError)
        return failure.value.subFailure

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::ResponseMiddleware.process_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py]
            def process_exception(self, request, exception):
                calls.append("process_exception")
                return resp

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.handle_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def handle_exception(self, _failure: Failure) -> None:
        logger.error(
            "An error is caught while iterating the async iterable",
            exc_info=failure_to_exc_info(_failure),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def should_error(self):
        assert self.results.errors

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::InvalidProcessExceptionMiddleware.process_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py]
            def process_exception(self, request, exception):
                return 1

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::handle_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py]
def handle_error(failure):
    pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SingleRequestSpider.on_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def on_error(self, failure):
        self.meta["failure"] = failure
        if callable(self.errback_func):
            return self.errback_func(failure)
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::MethodsSpider.handle_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py]
    def handle_error(self, failure):
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_critical [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_critical(self, message: str, extra: dict | None = None):
        self.logger.critical(message, extra=extra)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py::format_engine_status [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/engine.py]
def format_engine_status(engine: ExecutionEngine) -> str:
    checks = get_engine_status(engine)
    s = "Execution engine status\n\n"
    for test, result in checks:
        s += f"{test:<47} : {result}\n"
    s += "\n"

    return s

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_fail [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def should_fail(self):
        assert self.results.failures
        assert not self.results.errors

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::DeprecatedSpiderArgMiddleware.process_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py]
            def process_exception(self, request, exception, spider):
                return resp

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def errback(self, failure):
        self.meta["failure"] = failure

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::BytesReceivedCallbackSpider.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def errback(self, failure):
        self.meta["failure"] = failure

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithErrback.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def errback(self, failure):
        self.logger.info("[errback] status %i", failure.value.response.status)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/twisted_reactor_custom_settings_select.py::log_task_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/twisted_reactor_custom_settings_select.py]
def log_task_exception(task: Task) -> None:
    try:
        task.result()
    except Exception:
        logging.exception("Crawl task failed")  # noqa: LOG015

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/reactorless_custom_settings.py::log_task_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/reactorless_custom_settings.py]
def log_task_exception(task: Task) -> None:
    try:
        task.result()
    except Exception:
        logging.exception("Crawl task failed")  # noqa: LOG015

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::wrap_twisted_exceptions [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py]
def wrap_twisted_exceptions() -> Iterator[None]:
    """Context manager that wraps Twisted exceptions into Scrapy exceptions."""
    try:
        yield
    except SchemeNotSupported as e:
        raise UnsupportedURLSchemeError(str(e)) from e
    except CancelledError as e:
        raise DownloadCancelledError(str(e)) from e
    except TxConnectionRefusedError as e:
        raise DownloadConnectionRefusedError(str(e)) from e
    except DNSLookupError as e:
        raise CannotResolveHostError(str(e)) from e
    except ResponseFailed as e:
        raise DownloadFailedError(str(e)) from e
    except TxTimeoutError as e:
        raise DownloadTimeoutError(str(e)) from e

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_uri_params.py::TestURIParams._crawler_feed_exporter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport_uri_params.py]
    def _crawler_feed_exporter(self, settings):
        if self.deprecated_options:
            with pytest.warns(
                ScrapyDeprecationWarning,
                match="The `FEED_URI` and `FEED_FORMAT` settings have been deprecated",
            ):
                crawler = get_crawler(settings_dict=settings)
        else:
            crawler = get_crawler(settings_dict=settings)
        feed_exporter = crawler.get_extension(FeedExporter)
        return crawler, feed_exporter

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py::DownloaderStats.process_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py]
    def process_exception(
        self, request: Request, exception: Exception, spider: Spider | None = None
    ) -> Request | Response | None:
        ex_class = global_object_name(exception.__class__)
        self.stats.inc_value("downloader/exception_count")
        self.stats.inc_value(f"downloader/exception_type_count/{ex_class}")
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_info [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_info(self, message: str, extra: dict | None = None):
        self.logger.info(message, extra=extra)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_misc/test_return_with_argument_inside_generator.py::_indentation_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_misc/test_return_with_argument_inside_generator.py]
def _indentation_error(*args, **kwargs):
    raise IndentationError

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._handle_failure [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py]
    def _handle_failure(
        self, failure: Failure, errback: Callable[[Failure], Any] | None
    ) -> Iterable[Any]:
        if errback:
            results = errback(failure) or ()
            yield from iterate_spider_output(results)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::ProcessSpiderInputSpiderWithErrback.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py]
    def errback(self, failure):
        self.logger.info("Got a Failure on the Request errback")
        return {"from": "errback"}

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::DelaySpider.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def errback(self, failure):
        self.t2_err = time.time()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_warning [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def log_warning(self, message: str, extra: dict | None = None):
        self.logger.warning(message, extra=extra)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py::MockFTPServer.__exit__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/ftp.py]
    def __exit__(self, exc_type, exc_value, traceback):
        rmtree(str(self.path))
        self.proc.kill()
        self.proc.communicate()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py]
    def _errback(self, failure: Failure) -> Iterable[Any]:
        rule = self._rules[cast("int", failure.request.meta["rule"])]  # type: ignore[attr-defined]
        return self._handle_failure(
            failure, cast("Callable[[Failure], Any]", rule.errback)
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__exit__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
    def __exit__(self, exc_type, exc_value, traceback):
        if self.proc:
            self.proc.kill()
            self.proc.communicate()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pqueues.py::QueueProtocol.close [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pqueues.py]
    def close(self) -> None: ...
```
