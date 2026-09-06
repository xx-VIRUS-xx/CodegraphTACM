# scrapy-23 :: hybrid

query: py3 fix HttpProxy and Retry Middlewares

## selected nodes

- rank=1 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestMaxRetryTimes._test_retry file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py
- rank=2 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=3 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=4 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=5 layer=FUNCTION tokens=938 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::get_retry_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=6 layer=FUNCTION tokens=745 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._check_deprecated_process_start_requests_use file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=7 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=8 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=9 layer=FUNCTION tokens=227 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler.get_downloader_middleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=10 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware._retry file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=11 layer=FUNCTION tokens=262 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::NO_CALLBACK file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=12 layer=FUNCTION tokens=198 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestBaseAsyncSpiderMiddleware._get_middleware_result file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py
- rank=13 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=14 layer=FUNCTION tokens=181 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestRetry._test_retry_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py
- rank=15 layer=FUNCTION tokens=128 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestMaxRetryTimes._test_retry [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::get_retry_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py]
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
    Returns a new :class:`~scrapy.Request` object to retry the specified
    request, or ``None`` if retries of the specified request have been
    exhausted.

    For example, in a :class:`~scrapy.Spider` callback, you could use it as
    follows::

        def parse(self, response):
            if not response.text:
                new_request_or_none = get_retry_request(
                    response.request,
                    spider=self,
                    reason='empty',
                )
                return new_request_or_none

    *spider* is the :class:`~scrapy.Spider` instance which is asking for the
    retry request. It is used to access the :ref:`settings <topics-settings>`
    and :ref:`stats <topics-stats>`, and to provide extra logging context (see
    :func:`logging.debug`).

    *reason* is a string or an :class:`Exception` object that indicates the
    reason why the request needs to be retried. It is used to name retry stats.

    *max_retry_times* is a number that determines the maximum number of times
    that *request* can be retried. If not specified or ``None``, the number is
    read from the :reqmeta:`max_retry_times` meta key of the request. If the
    :reqmeta:`max_retry_times` meta key is not defined or ``None``, the number
    is read from the :setting:`RETRY_TIMES` setting.

    *priority_adjust* is a number that determines how the priority of the new
    request changes in relation to *request*. If not specified, the number is
    read from the :setting:`RETRY_PRIORITY_ADJUST` setting.

    *logger* is the logging.Logger object to be used when logging messages

    *stats_base_key* is a string to be used as the base key for the
    retry-related job stats
    """
    settings = spider.crawler.settings
    assert spider.crawler.stats
    stats = spider.crawler.stats
    retry_times = request.meta.get("retry_times", 0) + 1
    if max_retry_times is None:
        max_retry_times = request.meta.get("max_retry_times")
        if max_retry_times is None:
            max_retry_times = settings.getint("RETRY_TIMES")
    if retry_times <= max_retry_times:
        logger.debug(
            "Retrying %(request)s (failed %(retry_times)d times): %(reason)s",
            {"request": request, "retry_times": retry_times, "reason": reason},
            extra={"spider": spider},
        )
        new_request: Request = request.copy()
        new_request.meta["retry_times"] = retry_times
        new_request.dont_filter = True
        if priority_adjust is None:
            priority_adjust = settings.getint("RETRY_PRIORITY_ADJUST")
        new_request.priority = request.priority + priority_adjust

        if callable(reason):
            reason = reason()
        if isinstance(reason, Exception):
            reason = global_object_name(reason.__class__)

        stats.inc_value(f"{stats_base_key}/count")
        stats.inc_value(f"{stats_base_key}/reason_count/{reason}")
        return new_request
    stats.inc_value(f"{stats_base_key}/max_reached")
    logger.error(
        "Gave up retrying %(request)s (failed %(retry_times)d times): %(reason)s",
        {"request": request, "retry_times": retry_times, "reason": reason},
        extra={"spider": spider},
    )
    return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._check_deprecated_process_start_requests_use [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py]
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
            if not hasattr(middleware, "process_start_requests")
            and hasattr(middleware, "process_start")
        ]
        if deprecated_middlewares and modern_middlewares:
            raise ValueError(
                "You are trying to combine spider middlewares that only "
                "define the deprecated process_start_requests() method () "
                "with spider middlewares that only define the "
                "process_start() method (). This is not possible. You must "
                "either disable or make universal 1 of those 2 sets of "
                "spider middlewares. Making a spider middleware universal "
                "means having it define both methods. See the release notes "
                "of Scrapy 2.13 for details: "
                "https://docs.scrapy.org/en/2.13/news.html"
            )

        self._use_start_requests = bool(deprecated_middlewares)
        if self._use_start_requests:
            deprecated_middleware_list = ", ".join(
                global_object_name(middleware.__class__)
                for middleware in deprecated_middlewares
            )
            warn(
                f"The following enabled spider middlewares, directly or "
                f"through their parent classes, define the deprecated "
                f"process_start_requests() method: "
                f"{deprecated_middleware_list}. process_start_requests() has "
                f"been deprecated in favor of a new method, process_start(), "
                f"to support asynchronous code execution. "
                f"process_start_requests() will stop being called in a future "
                f"version of Scrapy. If you use Scrapy 2.13 or higher "
                f"only, replace process_start_requests() with "
                f"process_start(); note that process_start() is a coroutine "
                f"(async def). If you need to maintain compatibility with "
                f"lower Scrapy versions, when defining "
                f"process_start_requests() in a spider middleware class, "
                f"define process_start() as well. See the release notes of "
                f"Scrapy 2.13 for details: "
                f"https://docs.scrapy.org/en/2.13/news.html",
                ScrapyDeprecationWarning,
                stacklevel=2,
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py]
    def __init__(self, *middlewares: Any, crawler: Crawler | None = None) -> None:
        self._check_deprecated_process_start_requests_use(middlewares)
        super().__init__(*middlewares, crawler=crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py]
    def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None:
        creds, proxy_url, scheme = None, None, None
        if "proxy" in request.meta:
            if request.meta["proxy"] is not None:
                creds, proxy_url = self._get_proxy(request.meta["proxy"], "")
        elif self.proxies:
            parsed = urlparse_cached(request)
            _scheme = parsed.scheme
            if (
                # 'no_proxy' is only supported by http schemes
                _scheme not in {"http", "https"}
                or (parsed.hostname and not proxy_bypass(parsed.hostname))
            ) and _scheme in self.proxies:
                scheme = _scheme
                creds, proxy_url = self.proxies[scheme]

        self._set_proxy_and_creds(request, proxy_url, creds, scheme)
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler.get_downloader_middleware [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py]
    def get_downloader_middleware(self, cls: type[_T]) -> _T | None:
        """Return the run-time instance of a :ref:`downloader middleware
        <topics-downloader-middleware>` of the specified class or a subclass,
        or ``None`` if none is found.

        .. versionadded:: 2.12

        This method can only be called after the crawl engine has been created,
        e.g. at signals :signal:`engine_started` or :signal:`spider_opened`.
        """
        if not self.engine:
            raise RuntimeError(
                "Crawler.get_downloader_middleware() can only be called after "
                "the crawl engine has been created."
            )
        return self._get_component(cls, self.engine.downloader.middleware.middlewares)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware._retry [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::NO_CALLBACK [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py]
def NO_CALLBACK(*args: Any, **kwargs: Any) -> NoReturn:
    """When assigned to the ``callback`` parameter of
    :class:`~scrapy.Request`, it indicates that the request is not meant
    to have a spider callback at all.

    For example:

    .. code-block:: python

       Request("https://example.com", callback=NO_CALLBACK)

    This value should be used by :ref:`components <topics-components>` that
    create and handle their own requests, e.g. through
    :meth:`scrapy.core.engine.ExecutionEngine.download`, so that downloader
    middlewares handling such requests can treat them differently from requests
    intended for the :meth:`~scrapy.Spider.parse` callback.
    """
    raise RuntimeError(
        "The NO_CALLBACK callback has been called. This is a special callback "
        "value intended for requests whose callback is never meant to be "
        "called."
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py::TestBaseAsyncSpiderMiddleware._get_middleware_result [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py]
    def from_crawler(cls, crawler: Crawler) -> Self:
        if not crawler.settings.getbool("HTTPPROXY_ENABLED"):
            raise NotConfigured
        auth_encoding: str | None = crawler.settings.get("HTTPPROXY_AUTH_ENCODING")
        return cls(auth_encoding)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py::TestRetry._test_retry_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_retry.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
    def __init__(self) -> None:
        if not self.listen_http and not self.listen_https:
            raise ValueError("At least one of listen_http and listen_https must be set")

        self.proc: Popen | None = None
        self.host: str = "127.0.0.1"
        self.http_port: int | None = None
        self.https_port: int | None = None
```
