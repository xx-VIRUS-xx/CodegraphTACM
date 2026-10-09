# scrapy-20 :: tacm-dyn-l4

query: Fix SitemapSpider to extract sitemap urls from robots.txt properly

## selected nodes

- rank=1 layer=FILE tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=2 layer=CLASS tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=3 layer=FUNCTION tokens=302 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._parse_sitemap file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=4 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::sitemap_urls_from_robots file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=5 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::_sitemap_urls_from_robots_str file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=6 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=7 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=8 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=9 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=10 layer=CLASS tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=11 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider.assertSitemapBody file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=12 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=13 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/robotstxt.py::RobotParser.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/robotstxt.py
- rank=14 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=15 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=16 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=17 layer=FUNCTION tokens=188 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware._get_successful_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py
- rank=18 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.sitemap_filter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=19 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::Sitemap file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=20 layer=FUNCTION tokens=303 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.to_dict file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=21 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=22 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.process_request_2 file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=23 layer=FUNCTION tokens=346 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.robot_parser file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=24 layer=FUNCTION tokens=195 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/robotstxt.py::decode_robotstxt file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/robotstxt.py
- rank=25 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::Sitemap.__iter__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=26 layer=FUNCTION tokens=123 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py::Crawler._apply_settings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/crawler.py
- rank=27 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware._parse_robots file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=28 layer=FUNCTION tokens=163 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py::SpiderMiddlewareManager._process_spider_output file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/spidermw.py
- rank=29 layer=FUNCTION tokens=65 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py::TestRobotsTxtMiddleware.assertRobotsTxtRequested file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_robotstxt.py
- rank=30 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=31 layer=CLASS tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=32 layer=FUNCTION tokens=141 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.extract_contracts file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=33 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py

## context

```text
file scrapy/utils/sitemap.py
imports: __future__, warnings, io, typing, urllib, lxml, scrapy, collections
defines: Sitemap, sitemap_urls_from_robots, _sitemap_urls_from_robots_str

class SitemapSpider(Spider):  [scrapy/spiders/sitemap.py:26]
methods: _get_sitemap_body, _get_urls_and_callbacks_from_urlset
         _get_urls_from_sitemapindex, _parse_sitemap
         from_crawler, sitemap_filter, start
         start_requests, __init__

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

    def start_requests(self) -> Iterable[Request]:
        for url in self.sitemap_urls:
            yield Request(url, self._parse_sitemap)

    def _get_urls_from_sitemapindex(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[str]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            if any(x.search(loc) for x in self._follow):
                yield loc

class Request(object_ref):  [http/request/__init__.py:84]
methods: _set_body, _set_url, body, cb_kwargs, cookies, cookies
         copy, encoding, flags, flags, from_curl, headers
         headers, meta, replace, replace, replace, to_dict
         url, __init__, __repr__

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

class TestSitemapSpider(TestSpider):  [scrapy/tests/test_spider_sitemap.py:22]
methods: assertSitemapBody, test_alternate_url_locs
         test_compression_bomb_request_meta
         test_compression_bomb_setting
         test_compression_bomb_spider_attr
         test_download_warnsize_request_meta
         test_download_warnsize_setting
         test_download_warnsize_spider_attr
         test_get_sitemap_body
         test_get_sitemap_body_gzip_headers
         test_get_sitemap_body_xml_url
         test_get_sitemap_body_xml_url_compressed
         test_get_sitemap_urls_from_robotstxt
         test_get_sitemap_urls_from_robotstxt_skips_invalid_utf8_urls
         test_parse_sitemap_empty_body
         test_parse_sitemap_not_sitemap
         test_sitemap_filter
         test_sitemap_filter_with_alternate_links
         test_sitemap_filter_with_rule
         test_sitemap_follow, test_sitemap_urls
         test_sitemapindex_filter

    def assertSitemapBody(self, response: Response, body: bytes | None) -> None:
        crawler = get_crawler()
        spider = self.spider_class.from_crawler(crawler, "example.com")
        assert spider._get_sitemap_body(response) == body

    def _get_urls_and_callbacks_from_urlset(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[tuple[str, CallbackT]]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            for r, c in self._cbs:
                if r.search(loc):
                    yield loc, c
                    break

    def from_crawler(cls, crawler: Crawler, robotstxt_body: bytes) -> Self:
        """Parse the content of a robots.txt_ file as bytes. This must be a class method.
        It must return a new instance of the parser backend.

        :param crawler: crawler which made the request
        :type crawler: :class:`~scrapy.crawler.Crawler` instance

        :param robotstxt_body: content of a robots.txt_ file.
        :type robotstxt_body: bytes
        """

    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

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

    def _get_successful_crawler(self) -> Crawler:
        crawler = self.crawler
        crawler.settings.set("ROBOTSTXT_OBEY", True)
        ROBOTS = """
User-Agent: *
Disallow: /admin/
Disallow: /static/
# taken from https://en.wikipedia.org/robots.txt
Disallow: /wiki/K%C3%A4ytt%C3%A4j%C3%A4:
Disallow: /wiki/Käyttäjä:
User-Agent: UnicödeBöt
Disallow: /some/randome/page.html
""".encode()
        response = TextResponse("http://site.local/robots.txt", body=ROBOTS)

        async def return_response(request):
            deferred = Deferred()
            call_later(0, deferred.callback, response)
            return await maybe_deferred_to_future(deferred)

        crawler.engine.download_async.side_effect = return_response
        return crawler

    def sitemap_filter(
        self, entries: Iterable[dict[str, Any]]
    ) -> Iterable[dict[str, Any]]:
        """This method can be used to filter sitemap entries by their
        attributes, for example, you can filter locs with lastmod greater
        than a given date (see docs).
        """
        yield from entries

class Sitemap:  [scrapy/utils/sitemap.py:23]
methods: _get_tag_name, _process_sitemap_element, __init__, __iter__

    def to_dict(self, *, spider: scrapy.Spider | None = None) -> dict[str, Any]:
        """Return a dictionary containing the Request's data.

        Use :func:`~scrapy.utils.request.request_from_dict` to convert back into a :class:`~scrapy.Request` object.

        If a spider is given, this method will try to find out the name of the spider methods used as callback
        and errback and include them in the output dict, raising an exception if they cannot be found.
        """
        d = {
            "url": self.url,  # urls are safe (safe_string_url)
            "callback": (
                _find_method(spider, self.callback)
                if callable(self.callback)
                else self.callback
            ),
            "errback": (
                _find_method(spider, self.errback)
                if callable(self.errback)
                else self.errback
            ),
            "headers": dict(self.headers),
        }
        for attr in self.attributes:
            d.setdefault(attr, getattr(self, attr))
        if type(self) is not Request:  # pylint: disable=unidiomatic-typecheck
            d["_class"] = self.__module__ + "." + self.__class__.__name__
        return d

class RobotsTxtMiddleware:  [scrapy/downloadermiddlewares/robotstxt.py:34]
methods: _parse_robots, _robots_error, from_crawler
         process_request, process_request_2, robot_parser
         __init__

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

def decode_robotstxt(
    robotstxt_body: bytes, spider: Spider | None, to_native_str_type: bool = False
) -> str:
    try:
        if to_native_str_type:
            body_decoded = to_unicode(robotstxt_body)
        else:
            body_decoded = robotstxt_body.decode("utf-8-sig", errors="ignore")
    except UnicodeDecodeError:
        # If we found garbage or robots.txt in an encoding other than UTF-8, disregard it.
        # Switch to 'allow all' state.
        logger.warning(
            "Failure while parsing robots.txt. File either contains garbage or "
            "is in an encoding other than UTF-8, treating it as an empty file.",
            exc_info=sys.exc_info(),
            extra={"spider": spider},
        )
        body_decoded = ""
    return body_decoded

    def __iter__(self) -> Iterator[dict[str, Any]]:
        for event, elem in self.xmliter:
            if event == "start":
                continue

            if self._get_tag_name(elem) not in {"url", "sitemap"}:
                continue

            if d := self._process_sitemap_element(elem):
                yield d

    def _apply_settings(self) -> None:
        if self.settings.frozen:
            return

        self.addons.load_settings(self.settings)
        self.stats = load_object(self.settings["STATS_CLASS"])(self)

        lf_cls: type[LogFormatter] = load_object(self.settings["LOG_FORMATTER"])
        self.logformatter = lf_cls.from_crawler(self)

        self.request_fingerprinter = build_from_crawler(
            load_object(self.settings["REQUEST_FINGERPRINTER_CLASS"]),
    # ... truncated

    def _parse_robots(self, response: Response, netloc: str) -> None:
        assert self.crawler.stats
        self.crawler.stats.inc_value("robotstxt/response_count")
        self.crawler.stats.inc_value(
            f"robotstxt/response_status_count/{response.status}"
        )
        rp = self._parserimpl.from_crawler(self.crawler, response.body)
        rp_dfd = self._parsers[netloc]
        assert isinstance(rp_dfd, Deferred)
        self._parsers[netloc] = rp
        rp_dfd.callback(rp)

    def assertRobotsTxtRequested(self, base_url: str) -> None:
        calls = self.crawler.engine.download_async.call_args_list
        request = calls[0][0][0]
        assert request.url == f"{base_url}/robots.txt"
        assert request.callback == NO_CALLBACK

class ContractsManager:  [scrapy/contracts/__init__.py:92]
methods: _clean_req, cb_wrapper, eb_wrapper, extract_contracts
         from_method, from_spider
         tested_methods_from_spidercls, __init__

    def extract_cookies(self, response: HTTPResponse, request: ULRequest) -> None:
        pass

# --- Layer 04: Variable context ---
# call-chain context
  called by: _parse_sitemap [sitemap.py]

# call-chain context
  called by: sitemap_urls_from_robots [sitemap.py]

# call-chain context
  called by: process_start [spidermw.py]
  called by: start [sitemap.py]

# call-chain context
  called by: _parse_sitemap [sitemap.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: _parse_sitemap [sitemap.py]

# call-chain context
  called by: __init__ [__init__.py]
  called by: __init__ [scraper.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: _parse_sitemap [sitemap.py]

# call-chain context
  called by: push [squeues.py]
  called by: _assert_serializes_ok [test_request_dict.py]

# call-chain context
  called by: process_request [robotstxt.py]

# call-chain context
  called by: process_request [robotstxt.py]

# call-chain context
  called by: __init__ [robotstxt.py]
  called by: __init__ [robotstxt.py]

# call-chain context
  called by: run [shell.py]
  called by: crawl [crawler.py]

# call-chain context
  called by: robot_parser [robotstxt.py]

```
