# scrapy-17 :: tacm-rerank

query: response_status_message should not fail on non-standard HTTP codes

## selected nodes

- rank=1 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::response_status_message file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=2 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory.gotStatus file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=3 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleStatus file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=4 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=5 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.should_cache_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=6 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=7 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=8 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=9 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.on_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=10 layer=FUNCTION tokens=407 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::HTTP11DownloadHandler.download_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=11 layer=FUNCTION tokens=473 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect_scheme_change file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=12 layer=FUNCTION tokens=190 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=13 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py::get_status_size file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py
- rank=14 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_fail file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=15 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=16 layer=FUNCTION tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=17 layer=FUNCTION tokens=405 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy.should_cache_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=18 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::RecoverySpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=19 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py
- rank=20 layer=FUNCTION tokens=325 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::maybe_deferred_to_future file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=21 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::response_status_message [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py]
def response_status_message(status: bytes | float | str) -> str:
    """Return status code plus status text descriptive message"""
    status_int = int(status)
    message = http.RESPONSES.get(status_int, "Unknown Status")
    return f"{status_int} {to_unicode(message)}"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory.gotStatus [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py]
    def gotStatus(self, version, status, message):
        """
        Set the status of the request on us.
        @param version: The HTTP version.
        @type version: L{bytes}
        @param status: The HTTP status code, an integer represented as a
        bytestring.
        @type status: L{bytes}
        @param message: The HTTP status message.
        @type message: L{bytes}
        """
        self.version, self.status, self.message = version, status, message

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleStatus [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py]
    def handleStatus(self, version, status, message):
        self.factory.gotStatus(version, status, message)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.should_cache_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py]
    def should_cache_response(self, response: Response, request: Request) -> bool:
        return response.status not in self.ignore_http_codes

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.on_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
    def on_error(self, failure):
        if isinstance(failure.value, HttpError):
            response = failure.value.response
            if response.status in self.bypass_status_codes:
                self.skipped.add(response.url[-3:])
                return self.parse(response)

        # it assumes there is a response attached to failure
        self.failed.add(failure.value.response.url[-3:])
        return failure

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::HTTP11DownloadHandler.download_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    async def download_request(self, request: Request) -> Response:
        """Return a deferred for the HTTP download"""
        if hasattr(self._crawler.spider, "download_maxsize"):  # pragma: no cover
            warn_on_deprecated_spider_attribute("download_maxsize", "DOWNLOAD_MAXSIZE")
        if hasattr(self._crawler.spider, "download_warnsize"):  # pragma: no cover
            warn_on_deprecated_spider_attribute(
                "download_warnsize", "DOWNLOAD_WARNSIZE"
            )

        agent = ScrapyAgent(
            contextFactory=self._contextFactory,
            bindAddress=self._bind_address,
            pool=self._pool,
            maxsize=getattr(
                self._crawler.spider, "download_maxsize", self._default_maxsize
            ),
            warnsize=getattr(
                self._crawler.spider, "download_warnsize", self._default_warnsize
            ),
            fail_on_dataloss=self._fail_on_dataloss,
            crawler=self._crawler,
            tls_verbose_logging=self._tls_verbose_logging,
        )
        try:
            with wrap_twisted_exceptions():
                return await maybe_deferred_to_future(agent.download_request(request))
        except ResponseDataLossError:
            if not self._fail_on_dataloss_warned:
                logger.warning(get_dataloss_msg(request.url))
                self._fail_on_dataloss_warned = True
            raise

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect_scheme_change [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
    def _test_cookie_redirect_scheme_change(
        self, secure, from_scheme, to_scheme, cookies1, cookies2, cookies3
    ):
        """When a redirect causes the URL scheme to change from *from_scheme*
        to *to_scheme*, while domain and port remain the same, and given a
        cookie on the initial request with its secure attribute set to
        *secure*, check if the cookie should be set on the Cookie header of the
        initial request (*cookies1*), if it should be kept by the redirect
        middleware (*cookies2*), and if it should be present on the Cookie
        header in the redirected request (*cookie3*)."""
        cookie_kwargs = {}
        if secure is not UNSET:
            cookie_kwargs["secure"] = secure
        input_cookies = [{"name": "a", "value": "b", **cookie_kwargs}]

        request1 = Request(f"{from_scheme}://a.example", cookies=input_cookies)
        self.mw.process_request(request1)
        cookies = request1.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies1 else None)

        response = Response(
            f"{from_scheme}://a.example",
            headers={"Location": f"{to_scheme}://a.example"},
            status=301,
        )
        assert self.mw.process_response(request1, response) == response

        request2 = self.redirect_middleware.process_response(request1, response)
        assert isinstance(request2, Request)
        cookies = request2.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies2 else None)

        self.mw.process_request(request2)
        cookies = request2.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies3 else None)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py]
    def add_options(self, parser: ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument("--spider", dest="spider", help="use this spider")
        parser.add_argument(
            "--headers",
            dest="headers",
            action="store_true",
            help="print response HTTP headers instead of body",
        )
        parser.add_argument(
            "--no-redirect",
            dest="no_redirect",
            action="store_true",
            default=False,
            help="do not handle HTTP 3xx status codes and print response as-is",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py::get_status_size [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py]
def get_status_size(response_status: int) -> int:
    return len(to_bytes(http.RESPONSES.get(response_status, b""))) + 15
    # resp.status + b"\r\n" + b"HTTP/1.1 <100-599> "

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager.should_fail [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def should_fail(self):
        assert self.results.failures
        assert not self.results.errors

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py]
    def __init__(self, settings: BaseSettings):
        self.ignore_schemes: list[str] = settings.getlist("HTTPCACHE_IGNORE_SCHEMES")
        self.ignore_http_codes: list[int] = [
            int(x) for x in settings.getlist("HTTPCACHE_IGNORE_HTTP_CODES")
        ]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_exception [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py]
    def process_spider_exception(
        self, response: Response, exception: Exception, spider: Spider | None = None
    ) -> Iterable[Any] | None:
        if isinstance(exception, HttpError):
            assert self.crawler.stats
            self.crawler.stats.inc_value("httperror/response_ignored_count")
            self.crawler.stats.inc_value(
                f"httperror/response_ignored_status_count/{response.status}"
            )
            logger.info(
                "Ignoring response %(response)r: HTTP status code is not handled or not allowed",
                {"response": response},
                extra={"spider": self.crawler.spider},
            )
            return ()
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy.should_cache_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py]
    def should_cache_response(self, response: Response, request: Request) -> bool:
        # What is cacheable - https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9.1
        # Response cacheability - https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.4
        # Status code 206 is not included because cache can not deal with partial contents
        cc = self._parse_cachecontrol(response)
        # obey directive "Cache-Control: no-store"
        if b"no-store" in cc:
            return False
        # Never cache 304 (Not Modified) responses
        if response.status == 304:
            return False
        # Cache unconditionally if configured to do so
        if self.always_store:
            return True
        # Any hint on response expiration is good
        if b"max-age" in cc or b"Expires" in response.headers:
            return True
        # Firefox fallbacks this statuses to one year expiration if none is set
        if response.status in {300, 301, 308}:
            return True
        # Other statuses without expiration requires at least one validator
        if response.status in {200, 203, 401}:
            return b"Last-Modified" in response.headers or b"ETag" in response.headers
        # Any other is probably not eligible for caching
        # Makes no sense to cache responses that does not contain expiration
        # info and can not be revalidated
        return False

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::RecoverySpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py]
    def parse(self, response):
        yield {"test": 1}
        self.logger.info("DONT_FAIL: %s", response.meta.get("dont_fail"))
        if not response.meta.get("dont_fail"):
            raise TabError

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py]
    def add_options(self, parser: ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-c",
            dest="code",
            help="evaluate the code in the shell, print the result and exit",
        )
        parser.add_argument("--spider", dest="spider", help="use this spider")
        parser.add_argument(
            "--no-redirect",
            dest="no_redirect",
            action="store_true",
            default=False,
            help="do not handle HTTP 3xx status codes and print response as-is",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::maybe_deferred_to_future [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py]
def maybe_deferred_to_future(d: Deferred[_T]) -> Deferred[_T] | Future[_T]:
    """Return *d* as an object that can be awaited from a :ref:`Scrapy callable
    defined as a coroutine <coroutine-support>`.

    What you can await in Scrapy callables defined as coroutines depends on the
    value of :setting:`TWISTED_REACTOR`:

    -   When :ref:`using the asyncio reactor <install-asyncio>`, you can only
        await on :class:`asyncio.Future` objects.

    -   When not using the asyncio reactor, you can only await on
        :class:`~twisted.internet.defer.Deferred` objects.

    If you want to write code that uses ``Deferred`` objects but works with any
    reactor, use this function on all ``Deferred`` objects::

        class MySpider(Spider):
            ...
            async def parse(self, response):
                additional_request = scrapy.Request('https://example.org/price')
                deferred = self.crawler.engine.download(additional_request)
                additional_response = await maybe_deferred_to_future(deferred)
    """
    if not is_asyncio_available():
        return d
    return deferred_to_future(d)

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
```
