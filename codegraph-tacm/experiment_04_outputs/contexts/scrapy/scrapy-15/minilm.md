# scrapy-15 :: minilm

query: Do not fail on canonicalizing URLs with wrong netlocs

## selected nodes

- rank=1 layer=FUNCTION tokens=70 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::_canonicalize_link_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=2 layer=FUNCTION tokens=385 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::strip_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=3 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::url_is_from_any_domain file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=4 layer=FUNCTION tokens=117 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::add_http_if_no_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=5 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::sitemap_urls_from_robots file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=6 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlLinkExtractor._process_links file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=7 layer=FUNCTION tokens=157 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream.check_request_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=8 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py::TestHttps2ClientProtocol._check_invalid_netloc file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http2_client_protocol.py
- rank=9 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.get_host file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=10 layer=FUNCTION tokens=568 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream._get_request_headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=11 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=12 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py
- rank=13 layer=FUNCTION tokens=249 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlLinkExtractor._link_allowed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py
- rank=14 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request._set_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=15 layer=FUNCTION tokens=397 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py::RobotsTxtMiddleware.robot_parser file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/robotstxt.py
- rank=16 layer=FUNCTION tokens=231 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::FilesPipeline.file_path file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py
- rank=17 layer=FUNCTION tokens=154 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py::_sitemap_urls_from_robots_str file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/sitemap.py
- rank=18 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::url_is_from_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py
- rank=19 layer=FUNCTION tokens=57 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/testsite.py::SiteTest.url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/testsite.py
- rank=20 layer=FUNCTION tokens=124 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py::ReferrerPolicy.potentially_trustworthy file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py
- rank=21 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::verify_url_scheme file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py
- rank=22 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_response.py::check_base_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_response.py
- rank=23 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::InvalidHostname.__str__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=24 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/__init__.py::_is_valid_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/__init__.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::_canonicalize_link_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py]
def _canonicalize_link_url(link: Link) -> str:
    return canonicalize_url(link.url, keep_fragments=True)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::url_is_from_any_domain [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py]
def url_is_from_any_domain(url: UrlT, domains: Iterable[str]) -> bool:
    """Return True if the url belongs to any of the given domains"""
    host = _parse_url(url).netloc.lower()
    if not host:
        return False
    return any((host == d) or (host.endswith(f".{d}")) for d in map(str.lower, domains))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::add_http_if_no_scheme [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py]
def add_http_if_no_scheme(url: str) -> str:
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.IGNORECASE)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlLinkExtractor._process_links [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py]
    def _process_links(self, links: list[Link]) -> list[Link]:
        links = [x for x in links if self._link_allowed(x)]
        if self.canonicalize:
            for link in links:
                link.url = canonicalize_url(link.url)
        return self.link_extractor._process_links(links)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::WrappedRequest.get_host [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def get_host(self) -> str:
        return urlparse_cached(self.request).netloc

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_and_callbacks_from_urlset [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_urls_and_callbacks_from_urlset(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[tuple[str, CallbackT]]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            for r, c in self._cbs:
                if r.search(loc):
                    yield loc, c
                    break

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py::SitemapSpider._get_urls_from_sitemapindex [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/sitemap.py]
    def _get_urls_from_sitemapindex(
        self, it: Iterable[dict[str, Any]]
    ) -> Iterable[str]:
        for loc in iterloc(it, self.sitemap_alternate_links):
            if any(x.search(loc) for x in self._follow):
                yield loc

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py::LxmlLinkExtractor._link_allowed [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/lxmlhtml.py]
    def _link_allowed(self, link: Link) -> bool:
        if not _is_valid_url(link.url):
            return False
        if self.allow_res and not _matches(link.url, self.allow_res):
            return False
        if self.deny_res and _matches(link.url, self.deny_res):
            return False
        parsed_url = urlparse(link.url)
        if self.allow_domains and not url_is_from_any_domain(
            parsed_url, self.allow_domains
        ):
            return False
        if self.deny_domains and url_is_from_any_domain(parsed_url, self.deny_domains):
            return False
        if self.deny_extensions and url_has_any_extension(
            parsed_url, self.deny_extensions
        ):
            return False
        return not self.restrict_text or _matches(link.text, self.restrict_text)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py::FilesPipeline.file_path [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/files.py]
    def file_path(
        self,
        request: Request,
        response: Response | None = None,
        info: MediaPipeline.SpiderInfo | None = None,
        *,
        item: Any = None,
    ) -> str:
        media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()  # noqa: S324
        media_ext = Path(request.url).suffix
        # Handles empty and wild extensions by trying to guess the
        # mime type then extension or default to empty string otherwise
        if media_ext not in mimetypes.types_map:
            media_ext = ""
            media_type = mimetypes.guess_type(request.url)[0]
            if media_type:
                media_ext = cast("str", mimetypes.guess_extension(media_type))
        return f"full/{media_guid}{media_ext}"

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py::url_is_from_spider [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/url.py]
def url_is_from_spider(url: UrlT, spider: type[Spider]) -> bool:
    """Return True if the url belongs to the given spider"""
    return url_is_from_any_domain(url, _spider_domains(spider))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/testsite.py::SiteTest.url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/testsite.py]
    def url(self, path: str) -> str:
        return urljoin(self.baseurl, path)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py::ReferrerPolicy.potentially_trustworthy [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py]
    def potentially_trustworthy(self, url: str) -> bool:
        # Note: this does not follow https://w3c.github.io/webappsec-secure-contexts/#is-url-trustworthy
        parsed_url = urlparse(url)
        if parsed_url.scheme == "data":
            return False
        return self.tls_protected(url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::verify_url_scheme [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py]
def verify_url_scheme(url: str) -> str:
    """Check url for scheme and insert https if none found."""
    parsed = urlparse(url)
    if parsed.scheme == "" and parsed.netloc == "":
        parsed = urlparse("//" + url)._replace(scheme="https")
    return parsed.geturl()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_response.py::check_base_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_response.py]
    def check_base_url(burl):
        path = urlparse(burl).path
        if not path or not Path(path).exists():
            path = burl.replace("file://", "")
        bbody = Path(path).read_bytes()
        assert bbody.count(b'<base href="' + to_bytes(url) + b'">') == 1
        return True

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::InvalidHostname.__str__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py]
    def __str__(self) -> str:
        return f"InvalidHostname: Expected {self.expected_hostname} or {self.expected_netloc} in {self.request}"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/__init__.py::_is_valid_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/linkextractors/__init__.py]
def _is_valid_url(url: str) -> bool:
    return url.split("://", 1)[0] in {"http", "https", "file", "ftp"}
```
