# scrapy-17 :: hybrid

query: response_status_message should not fail on non-standard HTTP codes

## selected nodes

- rank=1 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.should_cache_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=2 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::response_status_message file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=3 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.on_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=4 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=5 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory.gotStatus file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=6 layer=FUNCTION tokens=190 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=7 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py::get_status_size file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py
- rank=8 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=9 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py
- rank=10 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::make_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py
- rank=11 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::get_dataloss_msg file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py
- rank=12 layer=FUNCTION tokens=504 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=13 layer=FUNCTION tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_exception file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=14 layer=FUNCTION tokens=203 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py::DownloaderStats.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py
- rank=15 layer=FUNCTION tokens=405 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy.should_cache_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=16 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DbmCacheStorage.retrieve_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=17 layer=FUNCTION tokens=183 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy.is_cached_response_valid file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=18 layer=FUNCTION tokens=169 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory._build_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=19 layer=FUNCTION tokens=102 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/view.py::Command._print_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/view.py
- rank=20 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=21 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.should_cache_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py]
    def should_cache_response(self, response: Response, request: Request) -> bool:
        return response.status not in self.ignore_http_codes

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::response_status_message [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py]
def response_status_message(status: bytes | float | str) -> str:
    """Return status code plus status text descriptive message"""
    status_int = int(status)
    message = http.RESPONSES.get(status_int, "Unknown Status")
    return f"{status_int} {to_unicode(message)}"

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
def _response(request: Request, status_code: int) -> Response:
    return Response(request.url, status=status_code, request=request)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::make_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py]
def make_response(
    url: str,
    status: int,
    headers: Headers,
    body: bytes = b"",
    flags: list[str] | None = None,
    certificate: Certificate | None = None,
    ip_address: IPv4Address | IPv6Address | None = None,
    protocol: str | None = None,
    stop_download: StopDownload | None = None,
) -> Response:
    respcls = responsetypes.responsetypes.from_args(headers=headers, url=url, body=body)
    response = respcls(
        url=url,
        status=status,
        headers=headers,
        body=body,
        flags=flags,
        certificate=certificate,
        ip_address=ip_address,
        protocol=protocol,
    )
    if stop_download:
        response.flags.append("download_stopped")
        if stop_download.fail:
            stop_download.response = response
            raise stop_download
    return response

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::get_dataloss_msg [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py]
def get_dataloss_msg(url: str) -> str:
    return (
        f"Got data loss in {url}. If you want to process broken "
        f"responses set the setting DOWNLOAD_FAIL_ON_DATALOSS = False"
        f" -- This message won't be shown in further requests"
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py]
    def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response:
        if (
            request.meta.get("dont_redirect", False)
            or response.status
            in getattr(self.crawler.spider, "handle_httpstatus_list", ())
            or response.status in request.meta.get("handle_httpstatus_list", ())
            or request.meta.get("handle_httpstatus_all", False)
        ):
            return response

        if "Location" not in response.headers or response.status not in {
            301,
            302,
            303,
            307,
            308,
        }:
            return response

        assert response.headers["Location"] is not None
        location = safe_url_string(response.headers["Location"])
        if response.headers["Location"].startswith(b"//"):
            request_scheme = urlparse_cached(request).scheme
            location = request_scheme + "://" + location.lstrip("/")

        redirected_url = urljoin(request.url, location)

        if not urlparse(redirected_url).fragment:
            fragment = urlparse_cached(request).fragment
            if fragment:
                redirected_url = urljoin(redirected_url, f"#{fragment}")

        redirected = self._build_redirect_request(request, response, url=redirected_url)
        if urlparse_cached(redirected).scheme not in {"http", "https"}:
            return response

        if (response.status in {301, 302} and request.method == "POST") or (
            response.status == 303 and request.method not in {"GET", "HEAD"}
        ):
            redirected = self._redirect_request_using_get(
                request, response, redirected_url
            )

        return self._redirect(redirected, request, response.status)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py::DownloaderStats.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py]
    def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response:
        self.stats.inc_value("downloader/response_count")
        self.stats.inc_value(f"downloader/response_status_count/{response.status}")
        reslen = (
            len(response.body)
            + get_header_size(response.headers)
            + get_status_size(response.status)
            + 4
        )
        # response.body + b"\r\n"+ response.header + b"\r\n" + response.status
        self.stats.inc_value("downloader/response_bytes", reslen)
        return response

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DbmCacheStorage.retrieve_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py]
    def retrieve_response(self, spider: Spider, request: Request) -> Response | None:
        data = self._read_data(spider, request)
        if data is None:
            return None  # not cached
        url = data["url"]
        status = data["status"]
        headers = Headers(data["headers"])
        body = data["body"]
        respcls = responsetypes.from_args(headers=headers, url=url, body=body)
        return respcls(url=url, headers=headers, status=status, body=body)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::RFC2616Policy.is_cached_response_valid [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py]
    def is_cached_response_valid(
        self, cachedresponse: Response, response: Response, request: Request
    ) -> bool:
        # Use the cached response if the new response is a server error,
        # as long as the old response didn't specify must-revalidate.
        if response.status >= 500:
            cc = self._parse_cachecontrol(cachedresponse)
            if b"must-revalidate" not in cc:
                return True

        # Use the cached response if the server says it hasn't changed.
        return response.status == 304

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory._build_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py]
    def _build_response(self, body, request):
        request.meta["download_latency"] = self.headers_time - self.start_time
        status = int(self.status)
        headers = Headers(self.response_headers)
        respcls = responsetypes.from_args(headers=headers, url=self._url, body=body)
        return respcls(
            url=self._url,
            status=status,
            headers=headers,
            body=body,
            protocol=to_unicode(self.version),
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/view.py::Command._print_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/view.py]
    def _print_response(self, response: Response, opts: argparse.Namespace) -> None:
        if not isinstance(response, TextResponse):
            logger.error("Cannot view a non-text response.")
            return
        open_in_browser(response)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py]
    def _assert_request_no3xx(self, pipeline_class, settings):
        pipe = pipeline_class(crawler=get_crawler(None, settings))
        request = Request("http://url")
        pipe._modify_media_request(request)

        assert "handle_httpstatus_list" in request.meta
        for status, check in [
            (200, True),
            # These are the status codes we want
            # the downloader to handle itself
            (301, False),
            (302, False),
            (302, False),
            (307, False),
            (308, False),
            # we still want to get 4xx and 5xx
            (400, True),
            (404, True),
            (500, True),
        ]:
            if check:
                assert status in request.meta["handle_httpstatus_list"]
            else:
                assert status not in request.meta["handle_httpstatus_list"]
```
