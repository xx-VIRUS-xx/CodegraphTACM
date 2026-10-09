# scrapy-17 :: codesearch

query: response_status_message should not fail on non-standard HTTP codes

## selected nodes

- rank=1 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::response_status_message file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=2 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=3 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.on_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=4 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleStatus file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=5 layer=FUNCTION tokens=88 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py::get_status_size file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py
- rank=6 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::make_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py
- rank=7 layer=FUNCTION tokens=166 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPClientFactory.gotStatus file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=8 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::AsyncDefSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=9 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SimpleSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=10 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=11 layer=FUNCTION tokens=504 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=12 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.should_cache_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py
- rank=13 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::res402 file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=14 layer=FUNCTION tokens=186 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_GET file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=15 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithParseMethod.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=16 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::AsyncDefAsyncioGenSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=17 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=18 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::res200 file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=19 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::res404 file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=20 layer=FUNCTION tokens=115 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase.assertEqualResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py
- rank=21 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.ignore_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py
- rank=22 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.ignore_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py
- rank=23 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=24 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=25 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py::TestRedirectMiddleware.get_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py
- rank=26 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect._assert_got_response_code file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=27 layer=FUNCTION tokens=405 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_POST_json file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=28 layer=FUNCTION tokens=184 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_POST_json_x10 file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=29 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithErrback.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=30 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::InvalidProcessResponseMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::response_status_message [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py]
def response_status_message(status: bytes | float | str) -> str:
    """Return status code plus status text descriptive message"""
    status_int = int(status)
    message = http.RESPONSES.get(status_int, "Unknown Status")
    return f"{status_int} {to_unicode(message)}"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
def _response(request: Request, status_code: int) -> Response:
    return Response(request.url, status=status_code, request=request)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleStatus [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py]
    def handleStatus(self, version, status, message):
        self.factory.gotStatus(version, status, message)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py::get_status_size [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/stats.py]
def get_status_size(response_status: int) -> int:
    return len(to_bytes(http.RESPONSES.get(response_status, b""))) + 15
    # resp.status + b"\r\n" + b"HTTP/1.1 <100-599> "

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::AsyncDefSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    async def parse(self, response):
        await defer.succeed(42)
        self.logger.info(f"Got response {response.status}")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SimpleSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def parse(self, response):
        self.logger.info(f"Got response {response.status}")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _handle_statuses(self, allow_redirects: bool) -> None:
        self.handle_httpstatus_list = None
        if allow_redirects:
            self.handle_httpstatus_list = SequenceExclude(range(300, 400))

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py::DummyPolicy.should_cache_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/httpcache.py]
    def should_cache_response(self, response: Response, request: Request) -> bool:
        return response.status not in self.ignore_http_codes

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::res402 [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
def res402() -> Response:
    return _response(req, 402)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_GET [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
    async def _check_GET(
        self,
        client: H2ClientProtocol,
        request: Request,
        expected_body: bytes,
        expected_status: int,
    ) -> None:
        response = await make_request(client, request)
        assert response.status == expected_status
        assert response.body == expected_body

        content_length_header = response.headers.get("Content-Length")
        assert content_length_header is not None
        content_length = int(content_length_header)
        assert len(response.body) == content_length

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithParseMethod.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def parse(self, response, foo=None):
        self.logger.info("[parse] status %i (foo: %s)", response.status, foo)
        yield Request(
            self.mockserver.url("/status?n=202"), self.parse, cb_kwargs={"foo": "bar"}
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::AsyncDefAsyncioGenSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    async def parse(self, response):
        await asyncio.sleep(0.2)
        yield {"foo": 42}
        self.logger.info(f"Got response {response.status}")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleResponse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py]
    def handleResponse(self, response):
        if self.factory.method.upper() == b"HEAD":
            self.factory.page(b"")
        elif self.length is not None and self.length > 0:
            self.factory.noPage(self._connection_lost_reason)
        else:
            self.factory.page(response)
        self.transport.loseConnection()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::res200 [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
def res200() -> Response:
    return _response(req, 200)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::res404 [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
def res404() -> Response:
    return _response(req, 404)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::TestBase.assertEqualResponse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py]
    def assertEqualResponse(self, response1, response2):
        assert response1.url == response2.url
        assert response1.status == response2.status
        assert response1.headers == response2.headers
        assert response1.body == response2.body

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.ignore_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/CrawlerProcess/caching_hostname_resolver.py]
    def ignore_response(self, response):
        self.logger.info(repr(response.ip_address))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py::CachingHostnameResolverSpider.ignore_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/AsyncCrawlerProcess/caching_hostname_resolver.py]
    def ignore_response(self, response):
        self.logger.info(repr(response.ip_address))

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py::TestRedirectMiddleware.get_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py]
    def get_response(self, request, location, status=302):
        headers = {"Location": location}
        return Response(request.url, status=status, headers=headers)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::TestProxyConnect._assert_got_response_code [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
    def _assert_got_response_code(self, code, log):
        assert str(log).count(f"Crawled ({code})") == 1

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_POST_json [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
    async def _check_POST_json(
        client: H2ClientProtocol,
        request: Request,
        expected_request_body: dict[str, str],
        expected_extra_data: str,
        expected_status: int,
    ) -> None:
        response = await make_request(client, request)

        assert response.status == expected_status

        content_length_header = response.headers.get("Content-Length")
        assert content_length_header is not None
        content_length = int(content_length_header)
        assert len(response.body) == content_length

        # Parse the body
        content_encoding_header = response.headers[b"Content-Encoding"]
        assert content_encoding_header is not None
        content_encoding = str(content_encoding_header, "utf-8")
        body = json.loads(str(response.body, content_encoding))
        assert "request-body" in body
        assert "extra-data" in body
        assert "request-headers" in body

        request_body = body["request-body"]
        assert request_body == expected_request_body

        extra_data = body["extra-data"]
        assert extra_data == expected_extra_data

        # Check if headers were sent successfully
        request_headers = body["request-headers"]
        for k, v in request.headers.items():
            k_str = str(k, "utf-8")
            assert k_str in request_headers
            assert request_headers[k_str] == str(v[0], "utf-8")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_POST_json_x10 [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
    async def _check_POST_json_x10(
        self,
        client: H2ClientProtocol,
        request: Request,
        expected_request_body: dict[str, str],
        expected_extra_data: str,
        expected_status: int,
    ) -> None:
        async def get_coro() -> None:
            await self._check_POST_json(
                client,
                request,
                expected_request_body,
                expected_extra_data,
                expected_status,
            )

        await self._check_repeat(get_coro, 10)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithErrback.errback [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def errback(self, failure):
        self.logger.info("[errback] status %i", failure.value.response.status)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::InvalidProcessResponseMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py]
            def process_response(self, request, response):
                return 1
```
