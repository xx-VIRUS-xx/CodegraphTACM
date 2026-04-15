# scrapy-20 :: minilm

query: Fix SitemapSpider to extract sitemap urls from robots.txt properly

## selected nodes

- rank=1 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::_sitemap_urls_from_robots_str file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=2 layer=FUNCTION tokens=344 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._parse_sitemap file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=3 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::sitemap_urls_from_robots file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=4 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=5 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=6 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.sitemap_filter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=7 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::Sitemap.__iter__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=8 layer=FUNCTION tokens=295 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::Sitemap._process_sitemap_element file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=9 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider.assertSitemapBody file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=10 layer=FUNCTION tokens=444 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_sitemap_body file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=11 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=12 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py
- rank=13 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware.assertRobotsTxtRequested file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py
- rank=14 layer=FUNCTION tokens=145 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.start_parsing file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py
- rank=15 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/robotstxt.py::RobotParser.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/robotstxt.py
- rank=16 layer=FUNCTION tokens=125 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FTPFeedStorage.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py
- rank=17 layer=FUNCTION tokens=397 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.robot_parser file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=18 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::SupportsFromCrawler.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py
- rank=19 layer=FUNCTION tokens=152 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware._robots_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=20 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::FilteredSitemapSpider.sitemap_filter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=21 layer=FUNCTION tokens=238 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.process_request_2 file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=22 layer=FUNCTION tokens=73 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::AjaxCrawlMiddleware.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
- rank=23 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http10.py::HTTP10DownloadHandler.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http10.py
- rank=24 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::_BaseSpiderMiddleware.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=25 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::AlternativeCallbacksMiddleware.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py
- rank=26 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers.py::BuggyDH.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_urls_from_sitemapindex(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[str]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            if any(x.search(loc) for x in self._follow):
                yield loc

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def start_requests(self) -> Iterable[Request]:
        for url in self.sitemap_urls:
            yield Request(url, self._parse_sitemap)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.sitemap_filter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def sitemap_filter(
        self, entries: Iterable[dict[str, Any]]
    ) -> Iterable[dict[str, Any]]:
        """This method can be used to filter sitemap entries by their
        attributes, for example, you can filter locs with lastmod greater
        than a given date (see docs).
        """
        yield from entries

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::Sitemap.__iter__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py]
    def __iter__(self) -> Iterator[dict[str, Any]]:
        for event, elem in self.xmliter:
            if event == "start":
                continue

            if self._get_tag_name(elem) not in {"url", "sitemap"}:
                continue

            if d := self._process_sitemap_element(elem):
                yield d

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::Sitemap._process_sitemap_element [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py]
    def _process_sitemap_element(
        self, elem: lxml.etree._Element
    ) -> dict[str, Any] | None:
        d: dict[str, Any] = {}
        alternate: list[str] = []
        has_loc = False

        for el in elem:
            try:
                tag_name = self._get_tag_name(el)
                if not tag_name:
                    continue

                if tag_name == "link":
                    if href := el.get("href"):
                        alternate.append(href)
                else:
                    d[tag_name] = el.text.strip() if el.text else ""
                    if not has_loc and tag_name == "loc":
                        has_loc = True
            finally:
                el.clear()
        elem.clear()
        parent = elem.getparent()
        if parent is not None:
            while elem.getprevious() is not None:
                del parent[0]

        if not has_loc:
            return None

        if alternate:
            d["alternate"] = alternate

        return d

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider.assertSitemapBody [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py]
    def assertSitemapBody(self, response: Response, body: bytes | None) -> None:
        crawler = get_crawler()
        spider = self.spider_class.from_crawler(crawler, "example.com")
        assert spider._get_sitemap_body(response) == body

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_urls_and_callbacks_from_urlset(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[tuple[str, CallbackT]]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            for r, c in self._cbs:
                if r.search(loc):
                    yield loc, c
                    break

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py::TestExtension.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline/extensions.py]
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware.assertRobotsTxtRequested [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py]
    def assertRobotsTxtRequested(self, base_url: str) -> None:
        calls = self.crawler.engine.download_async.call_args_list
        request = calls[0][0][0]
        assert request.url == f"{base_url}/robots.txt"
        assert request.callback == NO_CALLBACK

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py::Command.start_parsing [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/parse.py]
    def start_parsing(self, url: str, opts: argparse.Namespace) -> None:
        assert self.crawler_process
        assert self.spidercls
        self.crawler_process.crawl(self.spidercls, **opts.spargs)
        self.pcrawler = next(iter(self.crawler_process.crawlers))
        self.crawler_process.start()

        if not self.first_response:
            logger.error("No response downloaded for: %(url)s", {"url": url})

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/robotstxt.py::RobotParser.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/robotstxt.py]
    def from_crawler(cls, crawler: Crawler, robotstxt_body: bytes) -> Self:
        """Parse the content of a robots.txt_ file as bytes. This must be a class method.
        It must return a new instance of the parser backend.

        :param crawler: crawler which made the request
        :type crawler: :class:`~scrapy.crawler.Crawler` instance

        :param robotstxt_body: content of a robots.txt_ file.
        :type robotstxt_body: bytes
        """

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::FTPFeedStorage.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py]
    def from_crawler(
        cls,
        crawler: Crawler,
        uri: str,
        *,
        feed_options: dict[str, Any] | None = None,
    ) -> Self:
        return cls(
            uri,
            use_active_mode=crawler.settings.getbool("FEED_STORAGE_FTP_ACTIVE"),
            feed_options=feed_options,
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::SupportsFromCrawler.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py]
    def from_crawler(
        cls, crawler: Crawler, /, *args: _P.args, **kwargs: _P.kwargs
    ) -> _T_co: ...

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware._robots_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py]
    def _robots_error(self, exc: Exception, netloc: str) -> None:
        if not isinstance(exc, IgnoreRequest):
            key = f"robotstxt/exception_count/{type(exc)}"
            assert self.crawler.stats
            self.crawler.stats.inc_value(key)
        rp_dfd = self._parsers[netloc]
        assert isinstance(rp_dfd, Deferred)
        self._parsers[netloc] = None
        rp_dfd.callback(None)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::FilteredSitemapSpider.sitemap_filter [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py]
            def sitemap_filter(self, entries):
                for entry in entries:
                    date_time = datetime.strptime(
                        entry["lastmod"].split("T")[0], "%Y-%m-%d"
                    )
                    if date_time.year > 2004:
                        yield entry

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::AjaxCrawlMiddleware.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py]
    def from_crawler(cls, crawler: Crawler) -> Self:
        return cls(crawler.settings)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http10.py::HTTP10DownloadHandler.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http10.py]
    def from_crawler(cls, crawler: Crawler) -> Self:
        return cls(crawler.settings, crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::_BaseSpiderMiddleware.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py]
    def from_crawler(cls, crawler):
        return cls(crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::AlternativeCallbacksMiddleware.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py]
    def from_crawler(cls, crawler):
        return cls(crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers.py::BuggyDH.from_crawler [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloader_handlers.py]
    def from_crawler(cls, crawler):
        return cls(crawler)
```
