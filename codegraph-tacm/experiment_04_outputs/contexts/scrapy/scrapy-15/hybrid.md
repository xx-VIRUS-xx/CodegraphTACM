# scrapy-15 :: hybrid

query: Do not fail on canonicalizing URLs with wrong netlocs

## selected nodes

- rank=1 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py::OffsiteMiddleware.should_follow file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py
- rank=2 layer=FUNCTION tokens=147 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py::ImagesPipeline.get_media_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/images.py
- rank=3 layer=FUNCTION tokens=277 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=4 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::sitemap_urls_from_robots file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=5 layer=FUNCTION tokens=146 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::FilesPipeline.get_media_requests file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py
- rank=6 layer=FUNCTION tokens=172 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::TestEngineBase._assert_visited_urls file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py
- rank=7 layer=FUNCTION tokens=148 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py::TestHeadersReceivedEngine._assert_visited_urls file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py
- rank=8 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=9 layer=FUNCTION tokens=344 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._parse_sitemap file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=10 layer=FUNCTION tokens=479 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response.follow_all file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py
- rank=11 layer=FUNCTION tokens=129 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_response.py::TestResponse._assert_followed_all_urls file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_response.py
- rank=12 layer=FUNCTION tokens=385 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::strip_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=13 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=14 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=15 layer=FUNCTION tokens=568 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._get_request_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=16 layer=FUNCTION tokens=75 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_files.py::_create_item_with_files file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_files.py
- rank=17 layer=FUNCTION tokens=407 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::HTTP11DownloadHandler.download_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=18 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py::OffsiteMiddleware.should_follow [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/offsite.py]
    def should_follow(self, request: Request, spider: Spider) -> bool:
        regex = self.host_regex
        # hostname can be None for wrong urls (like javascript links)
        host = urlparse_cached(request).hostname or ""
        return bool(regex.search(host))

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::ScrapyAgent.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def __init__(
        self,
        *,
        contextFactory: IPolicyForHTTPS,
        connectTimeout: float = 10,
        bindAddress: str | tuple[str, int] | None = None,
        pool: HTTPConnectionPool | None = None,
        maxsize: int = 0,
        warnsize: int = 0,
        fail_on_dataloss: bool = True,
        crawler: Crawler,
        tls_verbose_logging: bool = False,
    ):
        self._contextFactory: IPolicyForHTTPS = contextFactory
        self._connectTimeout: float = connectTimeout
        self._bindAddress: str | tuple[str, int] | None = bindAddress
        self._pool: HTTPConnectionPool | None = pool
        self._maxsize: int = maxsize
        self._warnsize: int = warnsize
        self._fail_on_dataloss: bool = fail_on_dataloss
        self._txresponse: TxResponse | None = None
        self._crawler: Crawler = crawler
        self._tls_verbose_logging: bool = tls_verbose_logging

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py::TestHeadersReceivedEngine._assert_visited_urls [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py]
    def _assert_visited_urls(run: CrawlerRun) -> None:
        must_be_visited = ["/static/", "/redirect", "/redirected"]
        urls_visited = {rp[0].url for rp in run.respplug}
        urls_expected = {run.geturl(p) for p in must_be_visited}
        assert urls_expected <= urls_visited, (
            f"URLs not visited: {list(urls_expected - urls_visited)}"
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
def _wrong_credentials(proxy_url):
    bad_auth_proxy = list(urlsplit(proxy_url))
    bad_auth_proxy[1] = bad_auth_proxy[1].replace("scrapy:scrapy@", "wrong:wronger@")
    return urlunsplit(bad_auth_proxy)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py::Response.follow_all [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/__init__.py]
    def follow_all(
        self,
        urls: Iterable[str | Link],
        callback: CallbackT | None = None,
        method: str = "GET",
        headers: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None = None,
        body: bytes | str | None = None,
        cookies: CookiesT | None = None,
        meta: dict[str, Any] | None = None,
        encoding: str | None = "utf-8",
        priority: int = 0,
        dont_filter: bool = False,
        errback: Callable[[Failure], Any] | None = None,
        cb_kwargs: dict[str, Any] | None = None,
        flags: list[str] | None = None,
    ) -> Iterable[Request]:
        """
        Return an iterable of :class:`~.Request` instances to follow all links
        in ``urls``. It accepts the same arguments as ``Request.__init__()`` method,
        but elements of ``urls`` can be relative URLs or :class:`~scrapy.link.Link` objects,
        not only absolute URLs.

        :class:`~.TextResponse` provides a :meth:`~.TextResponse.follow_all`
        method which supports selectors in addition to absolute/relative URLs
        and Link objects.
        """
        if not hasattr(urls, "__iter__"):
            raise TypeError("'urls' argument must be an iterable")
        return (
            self.follow(
                url=url,
                callback=callback,
                method=method,
                headers=headers,
                body=body,
                cookies=cookies,
                meta=meta,
                encoding=encoding,
                priority=priority,
                dont_filter=dont_filter,
                errback=errback,
                cb_kwargs=cb_kwargs,
                flags=flags,
            )
            for url in urls
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_response.py::TestResponse._assert_followed_all_urls [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_response.py]
    def _assert_followed_all_urls(self, follow_obj, target_urls, response=None):
        if response is None:
            response = self._links_response()
        followed = response.follow_all(follow_obj)
        for req, target in zip(followed, target_urls, strict=False):
            assert req.url == target
            yield req

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_urls_from_sitemapindex(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[str]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            if any(x.search(loc) for x in self._follow):
                yield loc

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_urls_and_callbacks_from_urlset(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[tuple[str, CallbackT]]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            for r, c in self._cbs:
                if r.search(loc):
                    yield loc, c
                    break

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_files.py::_create_item_with_files [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_files.py]
def _create_item_with_files(*files: str) -> ItemWithFiles:
    item = ItemWithFiles()
    item["file_urls"] = files
    return item

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.start [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
    async def start(self):
        for url in self.start_urls:
            yield Request(url, self.parse, errback=self.on_error)
```
