# scrapy-20 :: tacm

query: Fix SitemapSpider to extract sitemap urls from robots.txt properly

## selected nodes

- rank=1 layer=FILE tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=2 layer=FILE tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=3 layer=FILE tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py
- rank=4 layer=CLASS tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=5 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=6 layer=CLASS tokens=236 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=7 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::Sitemap file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=8 layer=CLASS tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=9 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::SupportsFromCrawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py
- rank=10 layer=CLASS tokens=51 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=11 layer=CLASS tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=12 layer=CLASS tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlLinkExtractor file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=13 layer=CLASS tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=14 layer=CLASS tokens=14 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/telnet.py::TelnetConsole.Portal file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/telnet.py
- rank=15 layer=FUNCTION tokens=302 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._parse_sitemap file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=16 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::sitemap_urls_from_robots file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=17 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=18 layer=FUNCTION tokens=112 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::_sitemap_urls_from_robots_str file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=19 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.start_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=20 layer=FUNCTION tokens=62 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=21 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=22 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.sitemap_filter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=23 layer=FUNCTION tokens=106 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.from_crawler file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=24 layer=FUNCTION tokens=185 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.process_request_2 file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=25 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py::TestSitemapSpider.assertSitemapBody file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spider_sitemap.py
- rank=26 layer=FUNCTION tokens=346 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.robot_parser file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=27 layer=FUNCTION tokens=105 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=28 layer=FUNCTION tokens=351 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlParserLinkExtractor._extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=29 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=30 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=31 layer=FUNCTION tokens=401 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_sitemap_body file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=32 layer=FUNCTION tokens=259 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlLinkExtractor.extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=33 layer=FUNCTION tokens=34 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlLinkExtractor._extract_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=34 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py

## context

```text
file scrapy/utils/sitemap.py
imports: __future__, warnings, io, typing, urllib, lxml, scrapy, collections
defines: Sitemap, sitemap_urls_from_robots, _sitemap_urls_from_robots_str

file scrapy/spiders/sitemap.py
imports: __future__, logging, re, collections, typing, scrapy, typing_extensions
defines: SitemapSpider, regex, iterloc

file scrapy/utils/misc.py
imports: __future__, ast, hashlib, inspect, os, re, warnings, collections
defines: SupportsFromCrawler, arg_to_iter, arg_to_iter, arg_to_iter, arg_to_iter, arg_to_iter, load_object, walk_modules_iter, walk_modules, md5sum, rel_has_nofollow, build_from_crawler, build_from_crawler, build_from_crawler, set_environ, walk_callable, is_generator_with_return_value, returns_none, warn_on_generator_with_return_value

class SitemapSpider(Spider):  [scrapy/spiders/sitemap.py:26]
methods: _get_sitemap_body, _get_urls_and_callbacks_from_urlset
         _get_urls_from_sitemapindex, _parse_sitemap
         from_crawler, sitemap_filter, start
         start_requests, __init__

class Request(object_ref):  [http/request/__init__.py:84]
methods: _set_body, _set_url, body, cb_kwargs, cookies, cookies
         copy, encoding, flags, flags, from_curl, headers
         headers, meta, replace, replace, replace, to_dict
         url, __init__, __repr__

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

class Sitemap:  [scrapy/utils/sitemap.py:23]
methods: _get_tag_name, _process_sitemap_element, __init__, __iter__

class RobotsTxtMiddleware:  [scrapy/downloadermiddlewares/robotstxt.py:34]
methods: _parse_robots, _robots_error, from_crawler
         process_request, process_request_2, robot_parser
         __init__

class SupportsFromCrawler(Protocol[_T_co, _P]):  [scrapy/utils/misc.py:168]
methods: from_crawler

class ContractsManager:  [scrapy/contracts/__init__.py:92]
methods: _clean_req, cb_wrapper, eb_wrapper, extract_contracts
         from_method, from_spider
         tested_methods_from_spidercls, __init__

class BaseSettings(MutableMapping[_SettingsKey, Any]):  [scrapy/settings/__init__.py:83]
methods: _assert_mutability, _get_key, _repr_pretty_, _to_dict
         add_to_list, copy, copy_to_dict, delete, freeze
         frozencopy, get, getbool, getdict, getdictorlist
         getfloat, getint, getlist, getpriority
         getwithbase, maxpriority, normalize_key, pop
         remove_from_list
         replace_in_component_priority_dict, restore_key
         set, set_in_component_priority_dict, setdefault
         setdefault_in_component_priority_dict, setdict
         setmodule, track_loaded_key, update, __contains__
         __delitem__, __getitem__, __init__, __iter__
         __len__, __setitem__

class LxmlLinkExtractor:  [scrapy/linkextractors/lxmlhtml.py:164]
methods: _compile_regexes, _extract_links, _link_allowed
         _process_links, extract_links, matches, __init__

class LxmlParserLinkExtractor:  [scrapy/linkextractors/lxmlhtml.py:60]
methods: _deduplicate_if_needed, _extract_links, _iter_links
         _process_links, extract_links, __init__

class Portal:  [scrapy/extensions/telnet.py:86]
methods: —

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

    def _get_urls_and_callbacks_from_urlset(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[tuple[str, CallbackT]]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            for r, c in self._cbs:
                if r.search(loc):
                    yield loc, c
                    break

    def sitemap_filter(
        self, entries: Iterable[dict[str, Any]]
    ) -> Iterable[dict[str, Any]]:
        """This method can be used to filter sitemap entries by their
        attributes, for example, you can filter locs with lastmod greater
        than a given date (see docs).
        """
        yield from entries

    def from_crawler(cls, crawler: Crawler, *args: Any, **kwargs: Any) -> Self:
        spider = super().from_crawler(crawler, *args, **kwargs)
        spider._max_size = getattr(
            spider, "download_maxsize", spider.settings.getint("DOWNLOAD_MAXSIZE")
        )
        spider._warn_size = getattr(
            spider, "download_warnsize", spider.settings.getint("DOWNLOAD_WARNSIZE")
        )
        return spider

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

    def assertSitemapBody(self, response: Response, body: bytes | None) -> None:
        crawler = get_crawler()
        spider = self.spider_class.from_crawler(crawler, "example.com")
        assert spider._get_sitemap_body(response) == body

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

    def __init__(self, *a: Any, **kw: Any):
        super().__init__(*a, **kw)
        self._cbs: list[tuple[re.Pattern[str], CallbackT]] = []
        for r, c in self.sitemap_rules:
            if isinstance(c, str):
                c = cast("CallbackT", getattr(self, c))  # noqa: PLW2901
            self._cbs.append((regex(r), c))
        self._follow: list[re.Pattern[str]] = [regex(x) for x in self.sitemap_follow]

    def _extract_links(
        self,
        selector: Selector,
        response_url: str,
        response_encoding: str,
        base_url: str,
    ) -> list[Link]:
        links: list[Link] = []
        # hacky way to get the underlying lxml parsed document
        for el, _, attr_val in self._iter_links(selector.root):
            # pseudo lxml.html.HtmlElement.make_links_absolute(base_url)
            try:
                if self.strip:
                    attr_val = strip_html5_whitespace(attr_val)  # noqa: PLW2901 this is intended
                attr_val = urljoin(base_url, attr_val)  # noqa: PLW2901
            except ValueError:
                continue  # skipping bogus links
            else:
                url = self.process_attr(attr_val)
                if url is None:
                    continue
            try:
                url = safe_url_string(url, encoding=response_encoding)
            except ValueError:
                logger.debug(f"Skipping extraction of link with bad URL {url!r}")
                continue

            # to fix relative links after process_value
            url = urljoin(response_url, url)
            link = Link(
                url,
                _collect_string_content(el) or "",
                nofollow=rel_has_nofollow(el.get("rel")),
            )
            links.append(link)
        return self._deduplicate_if_needed(links)

    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

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

    def extract_links(self, response: TextResponse) -> list[Link]:
        """Returns a list of :class:`~scrapy.link.Link` objects from the
        specified :class:`response <scrapy.http.Response>`.

        Only links that match the settings passed to the ``__init__`` method of
        the link extractor are returned.

        Duplicate links are omitted if the ``unique`` attribute is set to ``True``,
        otherwise they are returned.
        """
        base_url = get_base_url(response)
        if self.restrict_xpaths:
            docs = [
                subdoc for x in self.restrict_xpaths for subdoc in response.xpath(x)
            ]
        else:
            docs = [response.selector]
        all_links = []
        for doc in docs:
            links = self._extract_links(doc, response.url, response.encoding, base_url)
            all_links.extend(self._process_links(links))
        if self.link_extractor.unique:
            return unique_list(all_links, key=self.link_extractor.link_key)
        return all_links

    def _extract_links(self, *args: Any, **kwargs: Any) -> list[Link]:
        return self.link_extractor._extract_links(*args, **kwargs)

    def url(self) -> str:
        return self._url
```
