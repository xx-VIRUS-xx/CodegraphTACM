# scrapy-33 :: tacm-dyn-l4

query: Replace FailureFormatter with direct exc_info conversions in log calls

## selected nodes

- rank=1 layer=FILE tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=2 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=3 layer=FUNCTION tokens=162 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::logformatter_adapter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=4 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.replace file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=5 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::_send_catch_log_deferred file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=6 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::failure_to_exc_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=7 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::ExecutionEngine.log_failure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py
- rank=8 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py::logerror file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/signal.py
- rank=9 layer=CLASS tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=10 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::LogSpider.log_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=11 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_request_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=12 layer=FUNCTION tokens=151 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_spider_attr file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=13 layer=FUNCTION tokens=168 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline.item_completed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=14 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_invalid_netloc file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=15 layer=CLASS tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_loader.py::TestSelectortemLoader file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_loader.py
- rank=16 layer=FUNCTION tokens=319 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=17 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py::TestHttpCompression._test_compression_bomb_setting file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcompression.py
- rank=18 layer=CLASS tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestProcessSpiderException file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py
- rank=19 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py::log_scrapy_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/log.py
- rank=20 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_commands.py::TestCommandCrawlerProcess._replace_custom_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_commands.py
- rank=21 layer=FILE tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/ssl.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/ssl.py
- rank=22 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/ssl.py::_log_ssl_conn_debug_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/ssl.py
- rank=23 layer=FUNCTION tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.copy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=24 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.handle_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=25 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response.replace file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py
- rank=26 layer=FUNCTION tokens=144 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py::MySpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawler.py
- rank=27 layer=CLASS tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_dupefilters.py::TestRFPDupeFilter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_dupefilters.py
- rank=28 layer=CLASS tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=29 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._log_tls_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=30 layer=FUNCTION tokens=470 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper._scrape file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=31 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::sanitize_module_name file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py
- rank=32 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.eb_wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=33 layer=CLASS tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py::TestLogging file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py
- rank=34 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py::TestLogging.log_stream file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py
- rank=35 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py::TestLogging.logger file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_log.py
- rank=36 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/ssl.py::_log_sslobj_debug_info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/ssl.py
- rank=37 layer=FUNCTION tokens=11 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedResponse.info file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py

## context

```text
file scrapy/utils/log.py
imports: __future__, logging, pprint, sys, collections, typing, twisted, scrapy
defines: TopLevelFormatter, StreamLogger, LogCounterHandler, SpiderLoggerAdapter, failure_to_exc_info, configure_logging, install_scrapy_root_handler, _uninstall_scrapy_root_handler, get_scrapy_root_handler, _get_handler, log_scrapy_info, log_reactor_info, logformatter_adapter

class Request(object_ref):  [http/request/__init__.py:84]
methods: _set_body, _set_url, body, cb_kwargs, cookies, cookies
         copy, encoding, flags, flags, from_curl, headers
         headers, meta, replace, replace, replace, to_dict
         url, __init__, __repr__

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

    def replace(
        self, *args: Any, cls: type[Request] | None = None, **kwargs: Any
    ) -> Request:
        """Create a new Request with the same attributes except for those given new values"""
        for x in self.attributes:
            kwargs.setdefault(x, getattr(self, x))
        if cls is None:
            cls = self.__class__
        return cls(*args, **kwargs)

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
    # ... truncated

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

        def log_failure(msg: str) -> None:
            logger.error(msg, exc_info=True, extra={"spider": spider})  # noqa: LOG014

    def logerror(failure: Failure, recv: TypingAny) -> Failure:
        if dont_log is None or not isinstance(failure.value, dont_log):
            logger.error(
                "Error caught on signal handler: %(receiver)s",
                {"receiver": recv},
                exc_info=failure_to_exc_info(failure),
                extra={"spider": spider},
            )
        return failure

class LogSpider(MetaSpider):  [scrapy/tests/spiders.py:94]
methods: log_critical, log_debug, log_error, log_info, log_warning
         parse

    def log_info(self, message: str, extra: dict | None = None):
        self.logger.info(message, extra=extra)

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

    async def _check_invalid_netloc(client: H2ClientProtocol, url: str) -> None:
        from scrapy.core.http2.stream import InvalidHostname  # noqa: PLC0415

        request = Request(url)
        with pytest.raises(InvalidHostname) as exc_info:
            await make_request(client, request)
        error_msg = str(exc_info.value)
        assert "localhost" in error_msg
        assert "127.0.0.1" in error_msg
        assert str(request) in error_msg

class TestSelectortemLoader:  [scrapy/tests/test_loader.py:260]
methods: test_add_css_re, test_add_xpath_re, test_get_css
         test_get_xpath, test_init_method
         test_init_method_errors
         test_init_method_with_base_response
         test_init_method_with_response
         test_init_method_with_response_css
         test_init_method_with_selector
         test_init_method_with_selector_css
         test_replace_css, test_replace_css_multi_fields
         test_replace_css_re, test_replace_xpath
         test_replace_xpath_multi_fields
         test_replace_xpath_re

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

class TestProcessSpiderException(TestBaseAsyncSpiderMiddleware):  [scrapy/tests/test_spidermiddleware.py:559]
methods: _callback, _test_asyncgen_nodowngrade, test_exc_async
         test_exc_async_async, test_exc_async_simple
         test_exc_simple, test_exc_simple_async
         test_exc_simple_simple

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

file scrapy/utils/ssl.py
imports: __future__, logging, ssl, typing, OpenSSL, scrapy
defines: _make_ssl_context, _log_sslobj_debug_info, ffi_buf_to_string, x509name_to_string, get_temp_key_info, get_openssl_version, _log_ssl_conn_debug_info

def _log_ssl_conn_debug_info(hostname: str, connection: OpenSSL.SSL.Connection) -> None:
    logger.debug(
        "SSL connection to %s using protocol %s, cipher %s",
        hostname,
        connection.get_protocol_version_name(),
        connection.get_cipher_name(),
    )
    server_cert = connection.get_peer_certificate()
    if server_cert:
        logger.debug(
            'SSL connection certificate: issuer "%s", subject "%s"',
            x509name_to_string(server_cert.get_issuer()),
            x509name_to_string(server_cert.get_subject()),
        )
    key_info = get_temp_key_info(connection._ssl)
    if key_info:
        logger.debug("SSL temp key: %s", key_info)

    def copy(self) -> Self:
        return self.replace()

    def handle_exception(self, _failure: Failure) -> None:
        logger.error(
            "An error is caught while iterating the async iterable",
            exc_info=failure_to_exc_info(_failure),
        )

    def replace(
        self, *args: Any, cls: type[Response] | None = None, **kwargs: Any
    ) -> Response:
        """Create a new Response with the same attributes except for those given new values"""
        for x in self.attributes:
            kwargs.setdefault(x, getattr(self, x))
        if cls is None:
            cls = self.__class__
        return cls(*args, **kwargs)

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

class TestRFPDupeFilter:  [scrapy/tests/test_dupefilters.py:41]
methods: test_df_direct_scheduler, test_df_from_crawler_scheduler
         test_dupefilter_path, test_filter, test_log
         test_log_debug, test_log_debug_default_dupefilter
         test_request_fingerprint, test_seenreq_newlines

class HttpxDownloadHandler(BaseHttpDownloadHandler):  [downloader/handlers/_httpx.py:74]
methods: _cancel_maxsize, _get_httpx_response, _get_server_ip
         _log_dataloss_warning, _log_tls_info
         _read_response, _warn_unsupported_meta, close
         download_request, __init__

    def _log_tls_info(self, network_stream: AsyncNetworkStream) -> None:
        if not self._tls_verbose_logging:
            return
        extra_ssl_object = network_stream.get_extra_info("ssl_object")
        if isinstance(extra_ssl_object, ssl.SSLObject):
            _log_sslobj_debug_info(extra_ssl_object)

    async def _scrape(self, result: Response | Failure, request: Request) -> None:
        """Handle the downloaded response or failure through the spider callback/errback."""
        if not isinstance(result, (Response, Failure)):
            raise TypeError(
                f"Incorrect type: expected Response or Failure, got {type(result)}: {result!r}"
            )

        output: Iterable[Any] | AsyncIterator[Any]
        if isinstance(result, Response):
            try:
                # call the spider middlewares and the request callback with the response
                output = await self.spidermw.scrape_response_async(
                    self.call_spider_async, result, request
                )
            except Exception:
                self.handle_spider_error(Failure(), request, result)
            else:
                await self.handle_spider_output_async(output, request, result)
            return

        try:
            # call the request errback with the downloader error
            output = await self.call_spider_async(result, request)
        except Exception as spider_exc:
            # the errback didn't silence the exception
            assert self.crawler.spider
            if not result.check(IgnoreRequest):
                logkws = self.logformatter.download_error(
                    result, request, self.crawler.spider
                )
                logger.log(
                    *logformatter_adapter(logkws),
                    extra={"spider": self.crawler.spider},
                    exc_info=failure_to_exc_info(result),
                )
            if spider_exc is not result.value:
                # the errback raised a different exception, handle it
                self.handle_spider_error(Failure(), request, result)
        else:
            await self.handle_spider_output_async(output, request, result)

    def info(self) -> Self:
        return self

    def close(self):
        pass

# --- Layer 04: Variable context ---
# call-chain context
  called by: _download [engine.py]
  called by: _scrape [scraper.py]

# call-chain context
  called by: get_setting_name_and_refid [scrapydocs.py]
  called by: main [linkfix.py]

# call-chain context
  called by: send_catch_log_deferred [signalmanager.py]
  called by: send_catch_log_deferred [signal.py]

# call-chain context
  called by: handle_exception [parse.py]
  called by: _start_scheduled_request [engine.py]

# call-chain context
  called by: close_spider_async [engine.py]

# call-chain context
  called by: process_item [media.py]

# call-chain context
  called by: _scrape [scraper.py]

# call-chain context
  called by: __init__ [crawler.py]

# call-chain context
  called by: connectionMade [http11.py]
  called by: handshakeCompleted [protocol.py]

# call-chain context
  called by: __init__ [crawler.py]
  called by: get_retry_request [retry.py]

# call-chain context
  called by: get_setting_name_and_refid [scrapydocs.py]
  called by: main [linkfix.py]

# call-chain context
  called by: run [crawl.py]
  called by: run [runspider.py]

# call-chain context
  called by: _read_response [_httpx.py]

# call-chain context
  called by: _wait_for_processing [scraper.py]

# call-chain context
  called by: load_settings [addons.py]
  called by: _start_scheduled_request [engine.py]

# call-chain context
  called by: connectionLost [protocol.py]
  called by: stream_ended [protocol.py]

```
