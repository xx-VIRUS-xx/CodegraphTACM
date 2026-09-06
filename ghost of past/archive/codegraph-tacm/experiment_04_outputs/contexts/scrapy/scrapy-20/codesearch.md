# scrapy-20 :: codesearch

query: Fix SitemapSpider to extract sitemap urls from robots.txt properly

## selected nodes

- rank=1 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::sitemap_urls_from_robots file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=2 layer=FUNCTION tokens=344 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._parse_sitemap file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=3 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::_sitemap_urls_from_robots_str file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=4 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider.assertSitemapBody file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=5 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=6 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py::TestMain._test_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py
- rank=7 layer=FUNCTION tokens=397 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.robot_parser file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=8 layer=FUNCTION tokens=357 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py::OffsiteMiddleware.get_host_regex file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py
- rank=9 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::CrawlerRun.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py
- rank=10 layer=FUNCTION tokens=98 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.scrapes_item_ok file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=11 layer=FUNCTION tokens=239 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.crawled file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py
- rank=12 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=13 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.scrapes_dict_item_ok file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=14 layer=FUNCTION tokens=189 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware._get_garbage_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py
- rank=15 layer=FUNCTION tokens=215 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol.site file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=16 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware._get_emptybody_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py
- rank=17 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_downloadtimeout.py::TestDownloadTimeoutMiddleware.get_request_spider_mw file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_downloadtimeout.py
- rank=18 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=19 layer=FUNCTION tokens=142 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::MaxItemsAndRequestsSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=20 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::FilteredSitemapSpider.sitemap_filter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=21 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_loop.py::TestMain.track_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_loop.py
- rank=22 layer=FUNCTION tokens=174 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command._get_items_and_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::sitemap_urls_from_robots [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py]
def sitemap_urls_from_robots(
    robots_text: str | bytes,
    base_url: str | None = None,
) -> Iterable[str]:
    if isinstance(robots_text, bytes):
        for line in BytesIO(robots_text):
            if line.lstrip()[:8].lower() == b"sitemap:":
                try:
                    url = line.partition(b":")[2].strip().decode()
                except UnicodeDecodeError:
                    continue
                yield urljoin(base_url or "", url)

    else:
        yield from _sitemap_urls_from_robots_str(robots_text, base_url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._parse_sitemap [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _parse_sitemap(self, response: Response) -> Iterable[Request]:
        if response.url.endswith("/robots.txt"):
            urls = list(sitemap_urls_from_robots(response.body, base_url=response.url))
            return (Request(url, callback=self._parse_sitemap) for url in urls)

        body = self._get_sitemap_body(response)
        if not body:
            logger.warning(
                "Ignoring invalid sitemap: %(response)s",
                {"response": response},
                extra={"spider": self},
            )
            return ()

        s = Sitemap(body)

        if s.type == "sitemapindex":
            urls = list(self._get_urls_from_sitemapindex(self.sitemap_filter(s)))
            return (Request(loc, callback=self._parse_sitemap) for loc in urls)

        if s.type == "urlset":
            url_callback_pairs = list(
                self._get_urls_and_callbacks_from_urlset(self.sitemap_filter(s))
            )
            return (Request(loc, callback=c) for loc, c in url_callback_pairs)

        logger.warning(
            "Ignoring invalid sitemap: %(response)s",
            {"response": response},
            extra={"spider": self},
        )

        return ()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::_sitemap_urls_from_robots_str [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py]
def _sitemap_urls_from_robots_str(
    robots_text: str,
    base_url: str | None = None,
) -> Iterable[str]:
    warnings.warn(
        "Passing `str` type as `robots_text` is deprecated, use `bytes`",
        ScrapyDeprecationWarning,
        stacklevel=2,
    )
    for line in StringIO(robots_text):
        if line.lstrip()[:8].lower() == "sitemap:":
            url = line.partition(":")[2].strip()
            yield urljoin(base_url or "", url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider.assertSitemapBody [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py]
    def assertSitemapBody(self, response: Response, body: bytes | None) -> None:
        crawler = get_crawler()
        spider = self.spider_class.from_crawler(crawler, "example.com")
        assert spider._get_sitemap_body(response) == body

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_urls_from_sitemapindex(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[str]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            if any(x.search(loc) for x in self._follow):
                yield loc

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py::TestMain._test_spider [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_start.py]
    async def _test_spider(
        self, spider: type[Spider], expected_items: list[Any] | None = None
    ) -> None:
        actual_items = []
        expected_items = [] if expected_items is None else expected_items

        def track_item(item, response, spider):
            actual_items.append(item)

        crawler = get_crawler(spider)
        crawler.signals.connect(track_item, signals.item_scraped)
        await crawler.crawl_async()
        assert crawler.stats
        assert crawler.stats.get_value("finish_reason") == "finished"
        assert actual_items == expected_items

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.robot_parser [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py]
    async def robot_parser(self, request: Request) -> RobotParser | None:
        url = urlparse_cached(request)
        netloc = url.netloc

        if netloc not in self._parsers:
            self._parsers[netloc] = Deferred()
            robotsurl = f"{url.scheme}://{url.netloc}/robots.txt"
            robotsreq = Request(
                robotsurl,
                priority=self.DOWNLOAD_PRIORITY,
                meta={"dont_obey_robotstxt": True},
                callback=NO_CALLBACK,
            )
            assert self.crawler.engine
            assert self.crawler.stats
            try:
                resp = await self.crawler.engine.download_async(robotsreq)
                self._parse_robots(resp, netloc)
            except Exception as e:
                if not isinstance(e, IgnoreRequest):
                    logger.error(
                        "Error downloading %(request)s: %(f_exception)s",
                        {"request": request, "f_exception": e},
                        exc_info=True,
                        extra={"spider": self.crawler.spider},
                    )
                self._robots_error(e, netloc)
            self.crawler.stats.inc_value("robotstxt/request_count")

        parser = self._parsers[netloc]
        if isinstance(parser, Deferred):
            return await maybe_deferred_to_future(parser)
        return parser

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py::OffsiteMiddleware.get_host_regex [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py]
    def get_host_regex(self, spider: Spider) -> re.Pattern[str]:
        """Override this method to implement a different offsite policy"""
        allowed_domains = getattr(spider, "allowed_domains", None)
        if not allowed_domains:
            return re.compile("")  # allow all by default
        url_pattern = re.compile(r"^https?://.*$")
        port_pattern = re.compile(r":\d+$")
        domains = []
        for domain in allowed_domains:
            if domain is None:
                continue
            if url_pattern.match(domain):
                message = (
                    "allowed_domains accepts only domains, not URLs. "
                    f"Ignoring URL entry {domain} in allowed_domains."
                )
                warnings.warn(message, stacklevel=2)
            elif port_pattern.search(domain):
                message = (
                    "allowed_domains accepts only domains without ports. "
                    f"Ignoring entry {domain} in allowed_domains."
                )
                warnings.warn(message, stacklevel=2)
            else:
                domains.append(re.escape(domain))
        regex = rf"^(.*\.)?({'|'.join(domains)})$"
        return re.compile(regex)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::CrawlerRun.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py]
    def __init__(self, spider_class: type[Spider]):
        self.respplug: list[tuple[Response, Spider]] = []
        self.reqplug: list[tuple[Request, Spider]] = []
        self.reqdropped: list[tuple[Request, Spider]] = []
        self.reqreached: list[tuple[Request, Spider]] = []
        self.itemerror: list[tuple[Any, Response, Spider, Failure]] = []
        self.itemresp: list[tuple[Any, Response]] = []
        self.headers: dict[Request, Headers] = {}
        self.bytes: defaultdict[Request, list[bytes]] = defaultdict(list)
        self.signals_caught: dict[Any, dict[str, Any]] = {}
        self.spider_class = spider_class

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.scrapes_item_ok [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def scrapes_item_ok(self, response):
        """returns item with name and url
        @url http://scrapy.org
        @returns items 1 1
        @scrapes name url
        """
        return DemoItem(name="test", url=response.url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py::LogFormatter.crawled [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/logformatter.py]
    def crawled(
        self, request: Request, response: Response, spider: Spider
    ) -> LogFormatterResult:
        """Logs a message when the crawler finds a webpage."""
        request_flags = f" {request.flags!s}" if request.flags else ""
        response_flags = f" {response.flags!s}" if response.flags else ""
        return {
            "level": logging.DEBUG,
            "msg": CRAWLEDMSG,
            "args": {
                "status": response.status,
                "request": request,
                "request_flags": request_flags,
                "referer": referer_str(request),
                "response_flags": response_flags,
                # backward compatibility with Scrapy logformatter below 1.4 version
                "flags": response_flags,
            },
        }

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.process_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py]
    async def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> None:
        if request.meta.get("dont_obey_robotstxt"):
            return
        if request.url.startswith("data:") or request.url.startswith("file:"):
            return
        rp = await self.robot_parser(request)
        self.process_request_2(rp, request)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.scrapes_dict_item_ok [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def scrapes_dict_item_ok(self, response):
        """returns item with name and url
        @url http://scrapy.org
        @returns items 1 1
        @scrapes name url
        """
        return {"name": "test", "url": response.url}

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware._get_garbage_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py]
    def _get_garbage_crawler(self) -> Crawler:
        crawler = self.crawler
        crawler.settings.set("ROBOTSTXT_OBEY", True)
        response = Response(
            "http://site.local/robots.txt", body=b"GIF89a\xd3\x00\xfe\x00\xa2"
        )

        async def return_response(request):
            deferred = Deferred()
            call_later(0, deferred.callback, response)
            return await maybe_deferred_to_future(deferred)

        crawler.engine.download_async.side_effect = return_response
        return crawler

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol.site [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py]
    def site(self, tmp_path):
        r = File(str(tmp_path))
        r.putChild(b"get-data-html-small", GetDataHtmlSmall())
        r.putChild(b"get-data-html-large", GetDataHtmlLarge())

        r.putChild(b"post-data-json-small", PostDataJsonSmall())
        r.putChild(b"post-data-json-large", PostDataJsonLarge())

        r.putChild(b"dataloss", Dataloss())
        r.putChild(b"no-content-length-header", NoContentLengthHeader())
        r.putChild(b"status", Status())
        r.putChild(b"query-params", QueryParams())
        r.putChild(b"timeout", TimeoutResponse())
        r.putChild(b"request-headers", RequestHeaders())
        return Site(r, timeout=None)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware._get_emptybody_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py]
    def _get_emptybody_crawler(self) -> Crawler:
        crawler = self.crawler
        crawler.settings.set("ROBOTSTXT_OBEY", True)
        response = Response("http://site.local/robots.txt")

        async def return_response(request):
            deferred = Deferred()
            call_later(0, deferred.callback, response)
            return await maybe_deferred_to_future(deferred)

        crawler.engine.download_async.side_effect = return_response
        return crawler

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_downloadtimeout.py::TestDownloadTimeoutMiddleware.get_request_spider_mw [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_downloadtimeout.py]
    def get_request_spider_mw(self, settings=None):
        crawler = get_crawler(Spider, settings)
        spider = crawler._create_spider("foo")
        request = Request("http://scrapytest.org/")
        return request, spider, DownloadTimeoutMiddleware.from_crawler(crawler)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::MaxItemsAndRequestsSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def parse(self, response):
        self.items_scraped = 0
        self.pages_crawled = 1  # account for the start url
        for request in super().parse(response):
            if self.pages_crawled < self.max_requests:
                yield request
                self.pages_crawled += 1
            if self.items_scraped < self.max_items:
                yield Item()
                self.items_scraped += 1

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::FilteredSitemapSpider.sitemap_filter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py]
            def sitemap_filter(self, entries):
                for entry in entries:
                    date_time = datetime.strptime(
                        entry["lastmod"].split("T")[0], "%Y-%m-%d"
                    )
                    if date_time.year > 2004:
                        yield entry

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_loop.py::TestMain.track_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_loop.py]
        def track_url(request, spider):
            actual_urls.append(request.url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command._get_items_and_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def _get_items_and_requests(
        self,
        spider_output: Iterable[Any],
        opts: argparse.Namespace,
        depth: int,
        spider: Spider,
        callback: CallbackT,
    ) -> tuple[list[Any], list[Request], argparse.Namespace, int, Spider, CallbackT]:
        items, requests = [], []
        for x in spider_output:
            if isinstance(x, Request):
                requests.append(x)
            else:
                items.append(x)
        return items, requests, opts, depth, spider, callback
```
