# scrapy-39 :: minilm

query: fix make_requests_from_url deprcation implementation, add tests

## selected nodes

- rank=1 layer=FUNCTION tokens=103 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py::TestRedirectMiddleware._test_passthrough file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py
- rank=2 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithParseMethod.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=3 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_request.py::TestRequestToCurl._test_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_request.py
- rank=4 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=5 layer=FUNCTION tokens=101 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::DuplicateStartSpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=6 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::RedirectedMediaDownloadSpider._process_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py
- rank=7 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request._set_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=8 layer=FUNCTION tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_core_downloader.py::TestContextFactory.testPayload file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_core_downloader.py
- rank=9 layer=FUNCTION tokens=568 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._get_request_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=10 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware.assertRobotsTxtRequested file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py
- rank=11 layer=FUNCTION tokens=385 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::strip_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=12 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py::TestSpider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py
- rank=13 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_scheduled_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py
- rank=14 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.from_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=15 layer=FUNCTION tokens=252 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py::OffsiteMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py
- rank=16 layer=FUNCTION tokens=69 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::TestResponseFromProcessException.download_func file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py
- rank=17 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClient.testNotFound file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py
- rank=18 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._build_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=19 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_linkextractors.py::TestLinkExtractorBase.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_linkextractors.py
- rank=20 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_cb_kwargs.py::KeywordArgumentsSpider.parse_spider_mw file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_cb_kwargs.py
- rank=21 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py::DownloadHandlers.download_request_async file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py
- rank=22 layer=FUNCTION tokens=328 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.run file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=23 layer=FUNCTION tokens=78 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_scheduler_base.py::PathsSpider.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_scheduler_base.py
- rank=24 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::InvalidProcessExceptionMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py
- rank=25 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::_Slot.add_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py::TestRedirectMiddleware._test_passthrough [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py]
        def _test_passthrough(req):
            rsp = Response(url, headers={"Location": url2}, status=301, request=req)
            r = self.mw.process_response(req, rsp)
            assert r is rsp

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithParseMethod.start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    async def start(self):
        test_body = b"""
        <html>
            <head><title>Page title</title></head>
            <body>
                <p><a href="/status?n=200">Item 200</a></p>  <!-- callback -->
                <p><a href="/status?n=201">Item 201</a></p>  <!-- callback -->
            </body>
        </html>
        """
        url = self.mockserver.url("/alpayload")
        yield Request(url, method="POST", body=test_body)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_request.py::TestRequestToCurl._test_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_request.py]
    def _test_request(self, request_object, expected_curl_command):
        curl_command = request_to_curl(request_object)
        assert curl_command == expected_curl_command

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [
            self.mockserver.url("/status?n=200"),
            self.mockserver.url("/status?n=404"),
            self.mockserver.url("/status?n=402"),
            self.mockserver.url("/status?n=500"),
        ]
        self.failed = set()
        self.skipped = set()
        self.parsed = set()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::DuplicateStartSpider.start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    async def start(self):
        for i in range(self.distinct_urls):
            for _ in range(self.dupe_factor):
                url = self.mockserver.url(f"/echo?headers=1&body=test{i}")
                yield Request(url, dont_filter=self.dont_filter)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py::RedirectedMediaDownloadSpider._process_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_crawl.py]
    def _process_url(self, url):
        return add_or_replace_parameter(
            self.mockserver.url("/redirect-to"), "goto", url
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_core_downloader.py::TestContextFactory.testPayload [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_core_downloader.py]
    async def testPayload(self, server_url: str) -> None:
        s = "0123456789" * 10
        crawler = get_crawler()
        client_context_factory = _load_context_factory_from_settings(crawler)
        body = await self.get_page(
            server_url + "payload", client_context_factory, body=s
        )
        assert body == to_bytes(s)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._get_request_headers [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py]
    def _get_request_headers(self) -> list[tuple[str, str]]:
        url = urlparse_cached(self._request)

        path = url.path
        if url.query:
            path += "?" + url.query

        # This pseudo-header field MUST NOT be empty for "http" or "https"
        # URIs; "http" or "https" URIs that do not contain a path component
        # MUST include a value of '/'. The exception to this rule is an
        # OPTIONS request for an "http" or "https" URI that does not include
        # a path component; these MUST include a ":path" pseudo-header field
        # with a value of '*' (refer RFC 7540 - Section 8.1.2.3)
        if not path:
            path = "*" if self._request.method == "OPTIONS" else "/"

        # Make sure pseudo-headers comes before all the other headers
        headers = [
            (":method", self._request.method),
            (":authority", url.netloc),
        ]

        # The ":scheme" and ":path" pseudo-header fields MUST
        # be omitted for CONNECT method (refer RFC 7540 - Section 8.3)
        if self._request.method != "CONNECT":
            headers += [
                (":scheme", self._protocol.metadata["uri"].scheme),
                (":path", path),
            ]

        content_length = str(len(self._request.body))
        headers.append(("Content-Length", content_length))

        content_length_name = self._request.headers.normkey(b"Content-Length")
        for name, values in self._request.headers.items():
            for value_bytes in values:
                value = str(value_bytes, "utf-8")
                if name == content_length_name:
                    if value != content_length:
                        logger.warning(
                            "Ignoring bad Content-Length header %r of request %r, "
                            "sending %r instead",
                            value,
                            self._request,
                            content_length,
                        )
                    continue
                headers.append((str(name, "utf-8"), value))

        return headers

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware.assertRobotsTxtRequested [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py]
    def assertRobotsTxtRequested(self, base_url: str) -> None:
        calls = self.crawler.engine.download_async.call_args_list
        request = calls[0][0][0]
        assert request.url == f"{base_url}/robots.txt"
        assert request.callback == NO_CALLBACK

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py::TestSpider.start_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py]
            def start_requests(self):
                raise RuntimeError

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.from_spider [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py]
    def from_spider(self, spider: Spider, results: TestResult) -> list[Request | None]:
        requests: list[Request | None] = []
        for method in self.tested_methods_from_spidercls(type(spider)):
            bound_method = spider.__getattribute__(method)
            try:
                requests.append(self.from_method(bound_method, results))
            except Exception:
                case = _create_testcase(bound_method, "contract")
                results.addError(case, sys.exc_info())

        return requests

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py::OffsiteMiddleware.process_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py]
    def process_request(self, request: Request, spider: Spider | None = None) -> None:
        assert self.crawler.spider
        if (
            request.dont_filter
            or request.meta.get("allow_offsite")
            or self.should_follow(request, self.crawler.spider)
        ):
            return
        domain = urlparse_cached(request).hostname
        if domain and domain not in self.domains_seen:
            self.domains_seen.add(domain)
            logger.debug(
                "Filtered offsite request to %(domain)r: %(request)s",
                {"domain": domain, "request": request},
                extra={"spider": self.crawler.spider},
            )
            self.stats.inc_value("offsite/domains")
        self.stats.inc_value("offsite/filtered")
        raise IgnoreRequest

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::TestResponseFromProcessException.download_func [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py]
        def download_func(request):
            raise ValueError("test")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClient.testNotFound [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py]
    def testNotFound(self, server_url):
        body = yield getPage(server_url + "notsuchfile")
        assert b"404 - No Such Resource" in body

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._build_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py]
    def _build_request(self, rule_index: int, link: Link) -> Request:
        return Request(
            url=link.url,
            callback=self._callback,
            errback=self._errback,
            meta={"rule": rule_index, "link_text": link.text},
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_linkextractors.py::TestLinkExtractorBase.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_linkextractors.py]
        def setup_method(self):
            body = get_testdata("link_extractor", "linkextractor.html")
            self.response = HtmlResponse(url="http://example.com/index", body=body)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_cb_kwargs.py::KeywordArgumentsSpider.parse_spider_mw [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_cb_kwargs.py]
    def parse_spider_mw(self, response, from_process_spider_input, from_process_start):
        self.checks.append(bool(from_process_spider_input))
        self.checks.append(bool(from_process_start))
        self.crawler.stats.inc_value("boolean_checks", 2)
        return Request(self.mockserver.url("/spider_mw_2"), self.parse_spider_mw_2)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py::DownloadHandlers.download_request_async [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/__init__.py]
    async def download_request_async(self, request: Request) -> Response:
        scheme = urlparse_cached(request).scheme
        handler = self._get_handler(scheme)
        if not handler:
            raise NotSupported(
                f"Unsupported URL scheme '{scheme}': {self._notconfigured[scheme]}"
            )
        assert self._crawler.spider
        if scheme in self._old_style_handlers:  # pragma: no cover
            return await maybe_deferred_to_future(
                cast(
                    "Deferred[Response]",
                    handler.download_request(request, self._crawler.spider),  # type: ignore[call-arg]
                )
            )
        return await handler.download_request(request)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.run [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py]
    def run(self, args: list[str], opts: Namespace) -> None:
        if len(args) != 1 or not is_url(args[0]):
            raise UsageError
        request = Request(
            args[0],
            callback=self._print_response,
            cb_kwargs={"opts": opts},
            dont_filter=True,
        )
        # by default, let the framework handle redirects,
        # i.e. command handles all codes expect 3xx
        if not opts.no_redirect:
            request.meta["handle_httpstatus_list"] = SequenceExclude(range(300, 400))
        else:
            request.meta["handle_httpstatus_all"] = True

        spidercls: type[Spider] = DefaultSpider
        assert self.crawler_process
        spider_loader = self.crawler_process.spider_loader
        if opts.spider:
            spidercls = spider_loader.load(opts.spider)
        else:
            spidercls = spidercls_for_request(spider_loader, request, spidercls)

        async def start(self: Spider) -> AsyncIterator[Any]:
            yield request

        spidercls.start = start  # type: ignore[method-assign]

        self.crawler_process.crawl(spidercls)
        self.crawler_process.start()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_scheduler_base.py::PathsSpider.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_scheduler_base.py]
    def __init__(self, mockserver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = map(mockserver.url, PATHS)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py::InvalidProcessExceptionMiddleware.process_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware.py]
            def process_request(self, request):
                raise RuntimeError

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py::_Slot.add_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/engine.py]
    def add_request(self, request: Request) -> None:
        self.inprogress.add(request)
```
