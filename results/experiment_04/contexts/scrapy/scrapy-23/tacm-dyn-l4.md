# scrapy-23 :: tacm-dyn-l4

query: py3 fix HttpProxy and Retry Middlewares

## selected nodes

- rank=1 layer=FILE tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=2 layer=CLASS tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=3 layer=FUNCTION tokens=85 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::get_retry_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=4 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=5 layer=CLASS tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=6 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=7 layer=FUNCTION tokens=134 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware._retry file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=8 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._check_deprecated_process_start_requests_use file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=9 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=10 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestRetry file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py
- rank=11 layer=FUNCTION tokens=131 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestRetry._test_retry_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py
- rank=12 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestRetry.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py
- rank=13 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=14 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestMaxRetryTimes._test_retry file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py
- rank=15 layer=FUNCTION tokens=261 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py::MiddlewareManager.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py
- rank=16 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=17 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=18 layer=FILE tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=19 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py::MiddlewareManager.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/middleware.py
- rank=20 layer=CLASS tokens=179 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestGetRetryRequest file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py
- rank=21 layer=CLASS tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawl.py::TestCrawl file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawl.py
- rank=22 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestBaseAsyncSpiderMiddleware._get_middleware_result file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py
- rank=23 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py::TestMain._test_sleep file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_process_start.py
- rank=24 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=25 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=26 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestProcessStartSimple._get_processed_start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py
- rank=27 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=28 layer=FUNCTION tokens=461 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.from_curl file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=29 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=30 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestSpiderMiddleware.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py
- rank=31 layer=CLASS tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestMaxRetryTimes file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py
- rank=32 layer=FILE tokens=90 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py
- rank=33 layer=FUNCTION tokens=173 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py::get_gcs_content_and_delete file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/test.py

## context

```text
file scrapy/downloadermiddlewares/retry.py
imports: __future__, logging, typing, scrapy, typing_extensions
defines: RetryMiddleware, get_retry_request

class HttpProxyMiddleware:  [scrapy/downloadermiddlewares/httpproxy.py:26]
methods: _basic_auth_header, _get_proxy, _set_proxy_and_creds
         from_crawler, process_request, __init__

def get_retry_request(
    request: Request,
    *,
    spider: scrapy.Spider,
    reason: str | Exception | type[Exception] = "unspecified",
    max_retry_times: int | None = None,
    priority_adjust: int | None = None,
    logger: Logger = retry_logger,
    stats_base_key: str = "retry",
) -> Request | None:
    """
    # ... truncated

    def from_crawler(cls, crawler: Crawler) -> Self:
        if not crawler.settings.getbool("HTTPPROXY_ENABLED"):
            raise NotConfigured
        auth_encoding: str | None = crawler.settings.get("HTTPPROXY_AUTH_ENCODING")
        return cls(auth_encoding)

class RetryMiddleware:  [scrapy/downloadermiddlewares/retry.py:126]
methods: _retry, from_crawler, process_exception, process_response
         __init__

    def process_exception(
        self,
        request: Request,
        exception: Exception,
        spider: scrapy.Spider | None = None,
    ) -> Request | Response | None:
        if isinstance(exception, self.exceptions_to_retry) and not request.meta.get(
            "dont_retry", False
        ):
            return self._retry(request, exception)
        return None

    def _retry(
        self, request: Request, reason: str | Exception | type[Exception]
    ) -> Request | None:
        max_retry_times = request.meta.get("max_retry_times", self.max_retry_times)
        priority_adjust = request.meta.get("priority_adjust", self.priority_adjust)
        assert self.crawler.spider
        return get_retry_request(
            request,
            reason=reason,
            spider=self.crawler.spider,
            max_retry_times=max_retry_times,
            priority_adjust=priority_adjust,
        )

    def _check_deprecated_process_start_requests_use(
        self, middlewares: tuple[Any, ...]
    ) -> None:
        deprecated_middlewares = [
            middleware
            for middleware in middlewares
            if hasattr(middleware, "process_start_requests")
            and not hasattr(middleware, "process_start")
        ]
        modern_middlewares = [
            middleware
            for middleware in middlewares
    # ... truncated

    def __init__(self, settings: BaseSettings):
        if not settings.getbool("RETRY_ENABLED"):
            raise NotConfigured
        self.max_retry_times = settings.getint("RETRY_TIMES")
        self.retry_http_codes = {int(x) for x in settings.getlist("RETRY_HTTP_CODES")}
        self.priority_adjust = settings.getint("RETRY_PRIORITY_ADJUST")
        self.exceptions_to_retry = tuple(
            load_object(x) if isinstance(x, str) else x
            for x in settings.getlist("RETRY_EXCEPTIONS")
        )

class TestRetry:  [scrapy/tests/test_downloadermiddleware_retry.py:21]
methods: _test_retry_exception, setup_method, test_404, test_503
         test_dont_retry, test_dont_retry_exc
         test_exception_to_retry_added
         test_priority_adjust, test_twistederrors

    def _test_retry_exception(self, req, exception, mw=None):
        if mw is None:
            mw = self.mw

        # first retry
        req = mw.process_exception(req, exception)
        assert isinstance(req, Request)
        assert req.meta["retry_times"] == 1

        # second retry
        req = mw.process_exception(req, exception)
        assert isinstance(req, Request)
        assert req.meta["retry_times"] == 2

        # discard it
        req = mw.process_exception(req, exception)
        assert req is None

    def setup_method(self):
        self.crawler = get_crawler(DefaultSpider)
        self.crawler.spider = self.crawler._create_spider()
        self.mw = RetryMiddleware.from_crawler(self.crawler)
        self.mw.max_retry_times = 2

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

    def _test_retry(
        self,
        req,
        exception,
        max_retry_times,
        middleware=None,
    ):
        middleware = middleware or self.mw

        for _ in range(max_retry_times):
            req = middleware.process_exception(req, exception)
            assert isinstance(req, Request)

        # discard it
        req = middleware.process_exception(req, exception)
        assert req is None

    def __init__(self, *middlewares: Any, crawler: Crawler | None = None) -> None:
        self.crawler: Crawler | None = crawler
        if crawler is None:
            warnings.warn(
                f"MiddlewareManager.__init__() was called without the crawler argument"
                f" when creating {global_object_name(self.__class__)}."
                f" This is deprecated and the argument will be required in future Scrapy versions.",
                category=ScrapyDeprecationWarning,
                stacklevel=2,
            )
        self.middlewares: tuple[Any, ...] = middlewares
        # Only process_spider_output and process_spider_exception can be None.
        # Only process_spider_output can be a tuple, and only until _async compatibility methods are removed.
        self.methods: dict[str, deque[Callable | tuple[Callable, Callable] | None]] = (
            defaultdict(deque)
        )
        self._mw_methods_requiring_spider: set[Callable] = set()
        for mw in middlewares:
            self._add_middleware(mw)

    def process_response(
        self,
        request: Request,
        response: Response,
        spider: scrapy.Spider | None = None,
    ) -> Request | Response:
        if request.meta.get("dont_retry", False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason) or response
        return response

    def __init__(self, *middlewares: Any, crawler: Crawler | None = None) -> None:
        self._check_deprecated_process_start_requests_use(middlewares)
        super().__init__(*middlewares, crawler=crawler)

file scrapy/downloadermiddlewares/httpproxy.py
imports: __future__, base64, typing, urllib, scrapy, typing_extensions
defines: HttpProxyMiddleware

    def from_crawler(cls, crawler: Crawler) -> Self:
        mwlist = cls._get_mwlist_from_settings(crawler.settings)
        middlewares = []
        enabled = []
        for clspath in mwlist:
            try:
                mwcls = load_object(clspath)
                mw = build_from_crawler(mwcls, crawler)
                middlewares.append(mw)
                enabled.append(clspath)
            except NotConfigured as e:
                if e.args:
                    logger.warning(
                        "Disabled %(clspath)s: %(eargs)s",
                        {"clspath": clspath, "eargs": e.args[0]},
                        extra={"crawler": crawler},
                    )

        logger.info(
            "Enabled %(componentname)ss:\n%(enabledlist)s",
            {
                "componentname": cls.component_name,
                "enabledlist": pprint.pformat(enabled),
            },
            extra={"crawler": crawler},
        )
        return cls(*middlewares, crawler=crawler)

class TestGetRetryRequest:  [scrapy/tests/test_downloadermiddleware_retry.py:262]
methods: get_spider, test_basic_usage, test_custom_logger
         test_custom_stats_key
         test_log_extra_retries_exceeded
         test_log_extra_retry_success
         test_max_retries_reached
         test_max_retry_times_argument
         test_max_retry_times_meta
         test_max_retry_times_setting, test_no_spider
         test_one_retry, test_priority_adjust_argument
         test_priority_adjust_setting
         test_reason_builtin_exception
         test_reason_builtin_exception_class
         test_reason_custom_exception
         test_reason_custom_exception_class
         test_reason_string, test_two_retries

class TestCrawl:  [scrapy/tests/test_crawl.py:64]
methods: _assert_retried, _on_item_scraped, _on_item_scraped
         _test_delay, cb, cb, setup_class, teardown_class
         test_crawl_multiple
         test_crawlerrunner_accepts_crawler
         test_engine_status, test_fixed_delay
         test_follow_all, test_format_engine_status
         test_open_spider_error_on_faulty_pipeline
         test_randomized_delay, test_referer_header
         test_retry_503, test_retry_conn_aborted
         test_retry_conn_failed, test_retry_conn_lost
         test_retry_dns_error, test_start_bug_before_yield
         test_start_bug_yielding, test_start_dupes
         test_start_items, test_start_unsupported_output
         test_timeout_failure, test_timeout_success
         test_unbounded_response, test_unknown_url_scheme

    async def _get_middleware_result(
        self, *mw_classes: type[Any], start_index: int | None = None
    ) -> Any:
        setting = self._construct_mw_setting(*mw_classes, start_index=start_index)
        self.crawler = get_crawler(
            Spider, {"SPIDER_MIDDLEWARES_BASE": {}, "SPIDER_MIDDLEWARES": setting}
        )
        self.crawler.spider = self.crawler._create_spider("foo")
        self.mwman = SpiderMiddlewareManager.from_crawler(self.crawler)
        return await self.mwman.scrape_response_async(
            self._scrape_func, self.response, self.request
        )

    async def _test_sleep(self, spider_middlewares):
        class TestSpider(Spider):
            name = "test"

            async def start(self):
                yield ITEM_A

        await self._test(spider_middlewares, TestSpider, [ITEM_A])

    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

    async def _get_processed_start(
        self, *mw_classes: type[Any]
    ) -> AsyncIterator[Any] | None:
        class TestSpider(Spider):
            name = "test"

            async def start(self):
                for i in range(2):
                    yield Request(f"https://example.com/{i}", dont_filter=True)
                yield {"name": "test item"}

        setting = self._construct_mw_setting(*mw_classes)
        self.crawler = get_crawler(
            TestSpider, {"SPIDER_MIDDLEWARES_BASE": {}, "SPIDER_MIDDLEWARES": setting}
        )
        self.crawler.spider = self.crawler._create_spider()
        self.mwman = SpiderMiddlewareManager.from_crawler(self.crawler)
        return await self.mwman.process_start()

class Request(object_ref):  [http/request/__init__.py:84]
methods: _set_body, _set_url, body, cb_kwargs, cookies, cookies
         copy, encoding, flags, flags, from_curl, headers
         headers, meta, replace, replace, replace, to_dict
         url, __init__, __repr__

    def from_curl(
        cls,
        curl_command: str,
        ignore_unknown_options: bool = True,
        **kwargs: Any,
    ) -> Self:
        """Create a Request object from a string containing a `cURL
        <https://curl.se/>`_ command. It populates the HTTP method, the
        URL, the headers, the cookies and the body. It accepts the same
        arguments as the :class:`Request` class, taking preference and
        overriding the values of the same arguments contained in the cURL
        command.

        Unrecognized options are ignored by default. To raise an error when
        finding unknown options call this method by passing
        ``ignore_unknown_options=False``.

        .. caution:: Using :meth:`from_curl` from :class:`~scrapy.Request`
                     subclasses, such as :class:`~scrapy.http.JsonRequest`, or
                     :class:`~scrapy.http.XmlRpcRequest`, as well as having
                     :ref:`downloader middlewares <topics-downloader-middleware>`
                     and
                     :ref:`spider middlewares <topics-spider-middleware>`
                     enabled, such as
                     :class:`~scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware`,
                     :class:`~scrapy.downloadermiddlewares.useragent.UserAgentMiddleware`,
                     or
                     :class:`~scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware`,
                     may modify the :class:`~scrapy.Request` object.

        To translate a cURL command into a Scrapy request,
        you may use `curl2scrapy <https://michael-shub.github.io/curl2scrapy/>`_.
        """
        request_kwargs = curl_to_request_kwargs(curl_command, ignore_unknown_options)
        request_kwargs.update(kwargs)
        return cls(**request_kwargs)

    def __init__(
        self,
        url: str,
        callback: CallbackT | None = None,
        method: str = "GET",
        headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        body: bytes | str | None = None,
        cookies: CookiesT | None = None,
        meta: dict[str, Any] | None = None,
        encoding: str = "utf-8",
        priority: int = 0,
        dont_filter: bool = False,
    # ... truncated

class TestBodyOrStr:  [scrapy/tests/test_utils_iterators.py:509]
methods: _assert_type_and_value, test_body_or_str

# --- Layer 04: Variable context ---
# call-chain context
  called by: _retry [retry.py]

# call-chain context
  called by: __init__ [__init__.py]
  called by: __init__ [scraper.py]

# call-chain context
  called by: _test_retry_exception [test_downloadermiddleware_retry.py]
  called by: _test_retry [test_downloadermiddleware_retry.py]

# call-chain context
  called by: process_response [retry.py]
  called by: process_exception [retry.py]

# call-chain context
  called by: __init__ [spidermw.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: _test_cookie_redirect [test_downloadermiddleware_cookies.py]
  called by: _test_cookie_header_redirect [test_downloadermiddleware_cookies.py]

# call-chain context
  called by: __init__ [__init__.py]
  called by: __init__ [scraper.py]

# call-chain context
  called by: _test_simple_base [test_spidermiddleware.py]
  called by: _test_asyncgen_base [test_spidermiddleware.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

```
