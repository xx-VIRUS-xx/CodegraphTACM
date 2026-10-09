# scrapy-20 :: hybrid-cs

query: Fix SitemapSpider to extract sitemap urls from robots.txt properly

## selected nodes

- rank=1 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::sitemap_urls_from_robots file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=2 layer=FUNCTION tokens=344 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._parse_sitemap file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=3 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::_sitemap_urls_from_robots_str file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=4 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=5 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider.assertSitemapBody file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=6 layer=FUNCTION tokens=397 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.robot_parser file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=7 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware._get_emptybody_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py
- rank=8 layer=FUNCTION tokens=189 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware._get_garbage_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py
- rank=9 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=10 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=11 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::FilesPipeline.get_media_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py
- rank=12 layer=FUNCTION tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::extract_domain file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py
- rank=13 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.extract_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=14 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::FilteredSitemapSpider.sitemap_filter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=15 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware.assertRobotsTxtRequested file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py
- rank=16 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.sitemap_filter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=17 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_visited_urls file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py
- rank=18 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_loop.py::TestMain.track_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_loop.py
- rank=19 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_scheduler.py::StartUrlsSpider.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_scheduler.py
- rank=20 layer=FUNCTION tokens=444 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_sitemap_body file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=21 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py::ImagesPipeline.get_media_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py
- rank=22 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py::TestHeadersReceivedEngine._assert_visited_urls file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py
- rank=23 layer=FUNCTION tokens=238 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.process_request_2 file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=24 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::_NullCookieJar.extract_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=25 layer=FUNCTION tokens=95 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::FollowAllSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_urls_from_sitemapindex(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[str]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            if any(x.search(loc) for x in self._follow):
                yield loc

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider.assertSitemapBody [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py]
    def assertSitemapBody(self, response: Response, body: bytes | None) -> None:
        crawler = get_crawler()
        spider = self.spider_class.from_crawler(crawler, "example.com")
        assert spider._get_sitemap_body(response) == body

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def start_requests(self) -> Iterable[Request]:
        for url in self.sitemap_urls:
            yield Request(url, self._parse_sitemap)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_urls_and_callbacks_from_urlset(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[tuple[str, CallbackT]]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            for r, c in self._cbs:
                if r.search(loc):
                    yield loc, c
                    break

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::FilesPipeline.get_media_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py]
    def get_media_requests(
        self, item: Any, info: MediaPipeline.SpiderInfo
    ) -> list[Request]:
        urls = ItemAdapter(item).get(self.files_urls_field, [])
        if not isinstance(urls, list):
            raise TypeError(
                f"{self.files_urls_field} must be a list of URLs, got {type(urls).__name__}. "
            )
        return [Request(u, callback=NO_CALLBACK) for u in urls]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::extract_domain [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py]
def extract_domain(url: str) -> str:
    """Extract domain name from URL string"""
    o = urlparse(url)
    if o.scheme == "" and o.netloc == "":
        o = urlparse("//" + url.lstrip("/"))
    return o.netloc

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.extract_cookies [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def extract_cookies(self, response: Response, request: Request) -> None:
        wreq = WrappedRequest(request)
        wrsp = WrappedResponse(response)
        self.jar.extract_cookies(wrsp, wreq)  # type: ignore[arg-type]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::FilteredSitemapSpider.sitemap_filter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py]
            def sitemap_filter(self, entries):
                for entry in entries:
                    date_time = datetime.strptime(
                        entry["lastmod"].split("T")[0], "%Y-%m-%d"
                    )
                    if date_time.year > 2004:
                        yield entry

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware.assertRobotsTxtRequested [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py]
    def assertRobotsTxtRequested(self, base_url: str) -> None:
        calls = self.crawler.engine.download_async.call_args_list
        request = calls[0][0][0]
        assert request.url == f"{base_url}/robots.txt"
        assert request.callback == NO_CALLBACK

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.sitemap_filter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def sitemap_filter(
        self, entries: Iterable[dict[str, Any]]
    ) -> Iterable[dict[str, Any]]:
        """This method can be used to filter sitemap entries by their
        attributes, for example, you can filter locs with lastmod greater
        than a given date (see docs).
        """
        yield from entries

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_visited_urls [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py]
    def _assert_visited_urls(run: CrawlerRun) -> None:
        must_be_visited = [
            "/static/",
            "/redirect",
            "/redirected",
            "/static/item1.html",
            "/static/item2.html",
            "/static/item999.html",
        ]
        urls_visited = {rp[0].url for rp in run.respplug}
        urls_expected = {run.geturl(p) for p in must_be_visited}
        assert urls_expected <= urls_visited, (
            f"URLs not visited: {list(urls_expected - urls_visited)}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_loop.py::TestMain.track_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_loop.py]
        def track_url(request, spider):
            actual_urls.append(request.url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_scheduler.py::StartUrlsSpider.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_scheduler.py]
    def __init__(self, start_urls):
        self.start_urls = start_urls
        super().__init__(name="StartUrlsSpider")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_sitemap_body [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_sitemap_body(self, response: Response) -> bytes | None:
        """Return the sitemap body contained in the given response,
        or None if the response is not a sitemap.
        """
        if isinstance(response, XmlResponse):
            return response.body
        if gzip_magic_number(response):
            uncompressed_size = len(response.body)
            max_size = response.meta.get("download_maxsize", self._max_size)
            warn_size = response.meta.get("download_warnsize", self._warn_size)
            try:
                body = gunzip(response.body, max_size=max_size)
            except _DecompressionMaxSizeExceeded:
                return None
            if uncompressed_size < warn_size <= len(body):
                logger.warning(
                    f"{response} body size after decompression ({len(body)} B) "
                    f"is larger than the download warning size ({warn_size} B)."
                )
            return body
        # actual gzipped sitemap files are decompressed above ;
        # if we are here (response body is not gzipped)
        # and have a response for .xml.gz,
        # it usually means that it was already gunzipped
        # by HttpCompression middleware,
        # the HTTP response being sent with "Content-Encoding: gzip"
        # without actually being a .xml.gz file in the first place,
        # merely XML gzip-compressed on the fly,
        # in other word, here, we have plain XML
        if response.url.endswith(".xml") or response.url.endswith(".xml.gz"):
            return response.body
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py::ImagesPipeline.get_media_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py]
    def get_media_requests(
        self, item: Any, info: MediaPipeline.SpiderInfo
    ) -> list[Request]:
        urls = ItemAdapter(item).get(self.images_urls_field, [])
        if not isinstance(urls, list):
            raise TypeError(
                f"{self.images_urls_field} must be a list of URLs, got {type(urls).__name__}. "
            )
        return [Request(u, callback=NO_CALLBACK) for u in urls]

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py::TestHeadersReceivedEngine._assert_visited_urls [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py]
    def _assert_visited_urls(run: CrawlerRun) -> None:
        must_be_visited = ["/static/", "/redirect", "/redirected"]
        urls_visited = {rp[0].url for rp in run.respplug}
        urls_expected = {run.geturl(p) for p in must_be_visited}
        assert urls_expected <= urls_visited, (
            f"URLs not visited: {list(urls_expected - urls_visited)}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.process_request_2 [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py]
    def process_request_2(self, rp: RobotParser | None, request: Request) -> None:
        if rp is None:
            return

        useragent: str | bytes | None = self._robotstxt_useragent
        if not useragent:
            useragent = request.headers.get(b"User-Agent", self._default_useragent)
            assert useragent is not None
        if not rp.allowed(request.url, useragent):
            logger.debug(
                "Forbidden by robots.txt: %(request)s",
                {"request": request},
                extra={"spider": self.crawler.spider},
            )
            assert self.crawler.stats
            self.crawler.stats.inc_value("robotstxt/forbidden")
            raise IgnoreRequest("Forbidden by robots.txt")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::_NullCookieJar.extract_cookies [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py]
    def extract_cookies(self, response: HTTPResponse, request: ULRequest) -> None:
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::FollowAllSpider.parse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def parse(self, response):
        self.urls_visited.append(response.url)
        self.times.append(time.time())
        for link in self.link_extractor.extract_links(response):
            yield Request(link.url, callback=self.parse)
```
