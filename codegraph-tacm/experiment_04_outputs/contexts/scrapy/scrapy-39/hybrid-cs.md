# scrapy-39 :: hybrid-cs

query: fix make_requests_from_url deprcation implementation, add tests

## selected nodes

- rank=1 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::add_http_if_no_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=2 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=3 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py
- rank=4 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::RedirectedMediaDownloadSpider._process_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py
- rank=5 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py
- rank=6 layer=FUNCTION tokens=157 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream.check_request_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=7 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/extras/qpsclient.py::QPSSpider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/extras/qpsclient.py
- rank=8 layer=FUNCTION tokens=385 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::strip_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=9 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::guess_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=10 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_scheduled_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py
- rank=11 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::BrokenLinksMediaDownloadSpider._process_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py
- rank=12 layer=FUNCTION tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=13 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::MediaDownloadSpider._process_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py
- rank=14 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request._set_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=15 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py::load_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py
- rank=16 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::make_request_dfd file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=17 layer=FUNCTION tokens=242 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py
- rank=18 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.returns_request_cb_kwargs file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=19 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_invalid_netloc file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=20 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::verify_url_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py
- rank=21 layer=FUNCTION tokens=159 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClientCustomCiphersSSL.testPayload file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py
- rank=22 layer=FUNCTION tokens=253 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py::make_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/_download_handlers.py
- rank=23 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py::UrlContract.adjust_request_args file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py
- rank=24 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=25 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response._set_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py
- rank=26 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py
- rank=27 layer=FUNCTION tokens=71 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SimpleSpider.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=28 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_request.py::TestRequestToCurl._test_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_request.py
- rank=29 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::make_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=30 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomSuccessContract.adjust_request_args file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=31 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_curl.py::TestCurlToRequestKwargs._test_command file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_curl.py
- rank=32 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py::TestCmdline.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py
- rank=33 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py::reactor_pytest file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::add_http_if_no_scheme [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py]
def add_http_if_no_scheme(url: str) -> str:
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.IGNORECASE)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.add_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def add_requests(self, lvl: int, new_reqs: list[Request]) -> None:
        old_reqs = self.requests.get(lvl, [])
        self.requests[lvl] = old_reqs + new_reqs

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py]
    def make_url(index):
        return f"https://toscrape.com/{index}"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::RedirectedMediaDownloadSpider._process_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py]
    def _process_url(self, url):
        return add_or_replace_parameter(
            self.mockserver.url("/redirect-to"), "goto", url
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py::make_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pqueues.py]
    def make_request(index, data):
        meta = {}
        if data.get("start", False):
            meta["is_start_request"] = True
        return Request(
            url=make_url(index),
            priority=data.get("priority", 0),
            meta=meta,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream.check_request_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py]
    def check_request_url(self) -> bool:
        # Make sure that we are sending the request to the correct URL
        url = urlparse_cached(self._request)
        return (
            url.netloc == str(self._protocol.metadata["uri"].host, "utf-8")
            or url.netloc == str(self._protocol.metadata["uri"].netloc, "utf-8")
            or url.netloc
            == f"{self._protocol.metadata['ip_address']}:{self._protocol.metadata['uri'].port}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/extras/qpsclient.py::QPSSpider.start_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/extras/qpsclient.py]
    def start_requests(self):
        url = self.benchurl
        if self.latency is not None:
            url += f"?latency={self.latency}"

        slots = int(self.slots)
        if slots > 1:
            urls = [url.replace("localhost", f"127.0.0.{x + 1}") for x in range(slots)]
        else:
            urls = [url]

        idx = 0
        while True:
            url = urls[idx % len(urls)]
            yield Request(url, dont_filter=True)
            idx += 1

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::strip_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py]
def strip_url(
    url: str,
    strip_credentials: bool = True,
    strip_default_port: bool = True,
    origin_only: bool = False,
    strip_fragment: bool = True,
) -> str:
    """Strip URL string from some of its components:

    - ``strip_credentials`` removes "user:password@"
    - ``strip_default_port`` removes ":80" (resp. ":443", ":21")
      from http:// (resp. https://, ftp://) URLs
    - ``origin_only`` replaces path component with "/", also dropping
      query and fragment components ; it also strips credentials
    - ``strip_fragment`` drops any #fragment component
    """

    parsed_url = urlparse(url)
    netloc = parsed_url.netloc
    if (strip_credentials or origin_only) and (
        parsed_url.username or parsed_url.password
    ):
        netloc = netloc.split("@")[-1]

    if (
        strip_default_port
        and parsed_url.port
        and (parsed_url.scheme, parsed_url.port)
        in {
            ("http", 80),
            ("https", 443),
            ("ftp", 21),
        }
    ):
        netloc = netloc.replace(f":{parsed_url.port}", "")

    return urlunparse(
        (
            parsed_url.scheme,
            netloc,
            "/" if origin_only else parsed_url.path,
            "" if origin_only else parsed_url.params,
            "" if origin_only else parsed_url.query,
            "" if strip_fragment else parsed_url.fragment,
        )
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::guess_scheme [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py]
def guess_scheme(url: str) -> str:
    """Add an URL scheme if missing: file:// for filepath-like input or
    http:// otherwise."""
    if _is_filesystem_path(url):
        return _any_to_uri(url)
    return add_http_if_no_scheme(url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_scheduled_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py]
    def _assert_scheduled_requests(run: CrawlerRun, count: int) -> None:
        assert len(run.reqplug) == count

        paths_expected = [
            "/static/item999.html",
            "/static/item2.html",
            "/static/item1.html",
        ]

        urls_requested = {rq[0].url for rq in run.reqplug}
        urls_expected = {run.geturl(p) for p in paths_expected}
        assert urls_expected <= urls_requested
        scheduled_requests_count = len(run.reqplug)
        dropped_requests_count = len(run.reqdropped)
        responses_count = len(run.respplug)
        assert scheduled_requests_count == dropped_requests_count + responses_count
        assert len(run.reqreached) == responses_count

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::BrokenLinksMediaDownloadSpider._process_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py]
    def _process_url(self, url):
        return url + ".foo"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
    def parse(self, response):
        self.parsed.add(response.url[-3:])

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::MediaDownloadSpider._process_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py]
    def _process_url(self, url):
        return url

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request._set_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py]
    def _set_url(self, url: str) -> None:
        if not isinstance(url, str):
            raise TypeError(f"Request url must be str, got {type(url).__name__}")

        self._url = safe_url_string(url, self.encoding)

        if (
            "://" not in self._url
            and not self._url.startswith("about:")
            and not self._url.startswith("data:")
        ):
            raise ValueError(f"Missing scheme in request url: {self._url}")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py::load_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/docs/conftest.py]
def load_response(url: str, filename: str) -> HtmlResponse:
    input_path = Path(__file__).parent / "_tests" / filename
    return HtmlResponse(url, body=input_path.read_bytes())

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::make_request_dfd [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
def make_request_dfd(client: H2ClientProtocol, request: Request) -> Deferred[Response]:
    return client.request(request, DummySpider())

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py::Spider.start_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/__init__.py]
    def start_requests(self) -> Iterable[Any]:
        warnings.warn(
            (
                "The Spider.start_requests() method is deprecated, use "
                "Spider.start() instead. If you are calling "
                "super().start_requests() from a Spider.start() override, "
                "iterate super().start() instead."
            ),
            ScrapyDeprecationWarning,
            stacklevel=2,
        )
        if not self.start_urls and hasattr(self, "start_url"):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)"
            )
        for url in self.start_urls:
            yield Request(url, dont_filter=True)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.returns_request_cb_kwargs [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def returns_request_cb_kwargs(self, response, url):
        """method which returns request
        @url https://example.org
        @cb_kwargs {"url": "http://scrapy.org"}
        @returns requests 1
        """
        return Request(url, callback=self.returns_item_cb_kwargs)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::verify_url_scheme [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py]
def verify_url_scheme(url: str) -> str:
    """Check url for scheme and insert https if none found."""
    parsed = urlparse(url)
    if parsed.scheme == "" and parsed.netloc == "":
        parsed = urlparse("//" + url)._replace(scheme="https")
    return parsed.geturl()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClientCustomCiphersSSL.testPayload [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py]
    def testPayload(self, server_url):
        s = "0123456789" * 10
        crawler = get_crawler(
            settings_dict={"DOWNLOADER_CLIENT_TLS_CIPHERS": self.custom_ciphers}
        )
        client_context_factory = build_from_crawler(
            _ScrapyClientContextFactory, crawler
        )
        body = yield getPage(
            server_url + "payload", body=s, contextFactory=client_context_factory
        )
        assert body == to_bytes(s)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py::UrlContract.adjust_request_args [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py]
    def adjust_request_args(self, args: dict[str, Any]) -> dict[str, Any]:
        args["url"] = self.args[0]
        return args

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def start_requests(self) -> Iterable[Request]:
        for url in self.sitemap_urls:
            yield Request(url, self._parse_sitemap)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response._set_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py]
    def _set_url(self, url: str) -> None:
        if isinstance(url, str):
            self._url: str = url
        else:
            raise TypeError(
                f"{type(self).__name__} url must be str, got {type(url).__name__}"
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-l",
            "--list",
            dest="list",
            action="store_true",
            help="only list contracts, without checking them",
        )
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            default=False,
            action="store_true",
            help="print contract tests for all spiders",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SimpleSpider.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def __init__(self, url="http://localhost:8998", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_request.py::TestRequestToCurl._test_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_request.py]
    def _test_request(self, request_object, expected_curl_command):
        curl_command = request_to_curl(request_object)
        assert curl_command == expected_curl_command

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::make_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
async def make_request(client: H2ClientProtocol, request: Request) -> Response:
    return await maybe_deferred_to_future(make_request_dfd(client, request))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomSuccessContract.adjust_request_args [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def adjust_request_args(self, args):
        args["url"] = "http://scrapy.org"
        return args

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_curl.py::TestCurlToRequestKwargs._test_command [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_curl.py]
    def _test_command(curl_command: str, expected_result: dict[str, Any]) -> None:
        result = curl_to_request_kwargs(curl_command)
        assert result == expected_result
        try:
            Request(**result)
        except TypeError as e:
            pytest.fail(f"Request kwargs are not correct {e}")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py::TestCmdline.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/__init__.py]
    def setup_method(self):
        self.env = get_testenv()
        tests_path = Path(__file__).parent.parent
        self.env["PYTHONPATH"] += os.pathsep + str(tests_path.parent)
        self.env["SCRAPY_SETTINGS_MODULE"] = "tests.test_cmdline.settings"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py::reactor_pytest [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/conftest.py]
def reactor_pytest(request) -> str:
    return request.config.getoption("--reactor")
```
