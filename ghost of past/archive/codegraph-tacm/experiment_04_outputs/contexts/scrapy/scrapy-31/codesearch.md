# scrapy-31 :: codesearch

query: Do not break cookie parsing on non-utf8 headers

## selected nodes

- rank=1 layer=FUNCTION tokens=309 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::_parse_headers_and_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py
- rank=2 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._headers_encoding file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py
- rank=3 layer=FUNCTION tokens=470 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._format_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=4 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._debug_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=5 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._process_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=6 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._declared_encoding file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py
- rank=7 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::_cookie_to_set_cookie_value file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=8 layer=FUNCTION tokens=194 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=9 layer=FUNCTION tokens=99 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py::HeadersReceivedCrawlerRun.headers_received file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py
- rank=10 layer=FUNCTION tokens=360 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.add_cookie_header file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=11 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::_NullCookieJar.extract_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=12 layer=FUNCTION tokens=190 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._body_inferred_encoding file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py
- rank=13 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedErrbackSpider.headers_received file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=14 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.headers_received file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=15 layer=FUNCTION tokens=137 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware._handle_encoding file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py
- rank=16 layer=FUNCTION tokens=80 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::CrawlerRun.headers_received file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py
- rank=17 layer=FUNCTION tokens=113 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py
- rank=18 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=19 layer=FUNCTION tokens=487 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_header_redirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=20 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::DuplicateHeaderResource.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=21 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._debug_set_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::_parse_headers_and_cookies [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py]
def _parse_headers_and_cookies(
    parsed_args: argparse.Namespace,
) -> tuple[list[tuple[str, bytes]], dict[str, str]]:
    headers: list[tuple[str, bytes]] = []
    cookies: dict[str, str] = {}
    for header in parsed_args.headers or ():
        name, val = header.split(":", 1)
        name = name.strip()
        val = val.strip()
        if name.title() == "Cookie":
            for name, morsel in SimpleCookie(val).items():
                cookies[name] = morsel.value
        else:
            headers.append((name, val))

    for cookie_param in parsed_args.cookies or ():
        # curl can treat this parameter as either "key=value; key2=value2" pairs, or a filename.
        # Scrapy will only support key-value pairs.
        if "=" not in cookie_param:
            continue
        for name, morsel in SimpleCookie(cookie_param).items():
            cookies[name] = morsel.value

    if parsed_args.auth:
        user, password = parsed_args.auth.split(":", 1)
        headers.append(("Authorization", basic_auth_header(user, password)))

    return headers, cookies

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._headers_encoding [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py]
    def _headers_encoding(self) -> str | None:
        content_type = self.headers.get(b"Content-Type") or b""
        return http_content_type_encoding(to_unicode(content_type, encoding="latin-1"))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._format_cookie [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py]
    def _format_cookie(self, cookie: VerboseCookie, request: Request) -> str | None:
        """
        Given a dict consisting of cookie components, return its string representation.
        Decode from bytes if necessary.
        """
        decoded = {}
        flags = set()
        for key in ("name", "value", "path", "domain"):
            value = cookie.get(key)
            if value is None:
                if key in {"name", "value"}:
                    msg = f"Invalid cookie found in request {request}: {cookie} ('{key}' is missing)"
                    logger.warning(msg)
                    return None
                continue
            if isinstance(value, (bool, float, int, str)):
                decoded[key] = str(value)
            else:
                assert isinstance(value, bytes)
                try:
                    decoded[key] = value.decode("utf8")
                except UnicodeDecodeError:
                    logger.warning(
                        "Non UTF-8 encoded cookie found in request %s: %s",
                        request,
                        cookie,
                    )
                    decoded[key] = value.decode("latin1", errors="replace")
        for flag in ("secure",):
            value = cookie.get(flag, _UNSET)
            if value is _UNSET or not value:
                continue
            flags.add(flag)
        cookie_str = f"{decoded.pop('name')}={decoded.pop('value')}"
        for key, value in decoded.items():  # path, domain
            cookie_str += f"; {key.capitalize()}={value}"
        for flag in flags:  # secure
            cookie_str += f"; {flag.capitalize()}"
        return cookie_str

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._debug_cookie [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py]
    def _debug_cookie(self, request: Request) -> None:
        if self.debug:
            cl = [
                to_unicode(c, errors="replace")
                for c in request.headers.getlist("Cookie")
            ]
            if cl:
                cookies = "\n".join(f"Cookie: {c}\n" for c in cl)
                msg = f"Sending cookies to: {request}\n{cookies}"
                logger.debug(msg, extra={"spider": self.crawler.spider})

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._process_cookies [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py]
    def _process_cookies(
        self, cookies: Iterable[Cookie], *, jar: CookieJar, request: Request
    ) -> None:
        for cookie in cookies:
            cookie_domain = cookie.domain
            cookie_domain = cookie_domain.removeprefix(".")

            hostname = urlparse_cached(request).hostname
            assert hostname is not None
            request_domain = hostname.lower()

            if cookie_domain and _is_public_domain(cookie_domain):
                if cookie_domain != request_domain:
                    continue
                cookie.domain = request_domain

            jar.set_cookie_if_ok(cookie, request)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._declared_encoding [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py]
    def _declared_encoding(self) -> str | None:
        return (
            self._encoding
            or self._bom_encoding()
            or self._headers_encoding()
            or self._body_declared_encoding()
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::_cookie_to_set_cookie_value [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
def _cookie_to_set_cookie_value(cookie):
    """Given a cookie defined as a dictionary with name and value keys, and
    optional path and domain keys, return the equivalent string that can be
    associated to a ``Set-Cookie`` header."""
    decoded = {}
    for key in ("name", "value", "path", "domain"):
        if cookie.get(key) is None:
            if key in ("name", "value"):
                return None
            continue
        if isinstance(cookie[key], (bool, float, int, str)):
            decoded[key] = str(cookie[key])
        else:
            try:
                decoded[key] = cookie[key].decode("utf8")
            except UnicodeDecodeError:
                decoded[key] = cookie[key].decode("latin1", errors="replace")

    cookie_str = f"{decoded.pop('name')}={decoded.pop('value')}"
    for key, value in decoded.items():  # path, domain
        cookie_str += f"; {key.capitalize()}={value}"
    return cookie_str

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py]
    def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response:
        if request.meta.get("dont_merge_cookies", False):
            return response

        # extract cookies from Set-Cookie and drop invalid/expired cookies
        cookiejarkey = request.meta.get("cookiejar")
        jar = self.jars[cookiejarkey]
        cookies = jar.make_cookies(response, request)
        self._process_cookies(cookies, jar=jar, request=request)

        self._debug_set_cookie(response)

        return response

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py::HeadersReceivedCrawlerRun.headers_received [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine_stop_download_headers.py]
    def headers_received(self, headers, body_length, request, spider):
        super().headers_received(headers, body_length, request, spider)
        raise StopDownload(fail=False)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.add_cookie_header [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def add_cookie_header(self, request: Request) -> None:
        wreq = WrappedRequest(request)
        self.policy._now = self.jar._now = int(time.time())  # type: ignore[attr-defined]

        # the cookiejar implementation iterates through all domains
        # instead we restrict to potential matches on the domain
        req_host = urlparse_cached(request).hostname
        if not req_host:
            return

        if not IPV4_RE.search(req_host):
            hosts = potential_domain_matches(req_host)
            if "." not in req_host:
                hosts.append(req_host + ".local")
        else:
            hosts = [req_host]

        cookies = []
        for host in hosts:
            if host in self.jar._cookies:  # type: ignore[attr-defined]
                cookies.extend(self.jar._cookies_for_domain(host, wreq))  # type: ignore[attr-defined]

        attrs = self.jar._cookie_attrs(cookies)  # type: ignore[attr-defined]
        if attrs and not wreq.has_header("Cookie"):
            wreq.add_unredirected_header("Cookie", "; ".join(attrs))

        self.processed += 1
        if self.processed % self.check_expired_frequency == 0:
            # This is still quite inefficient for large number of cookies
            self.jar.clear_expired_cookies()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::_NullCookieJar.extract_cookies [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py]
    def extract_cookies(self, response: HTTPResponse, request: ULRequest) -> None:
        pass

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py::TextResponse._body_inferred_encoding [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/response/text.py]
    def _body_inferred_encoding(self) -> str:
        if self._cached_benc is None:
            content_type = to_unicode(
                cast("bytes", self.headers.get(b"Content-Type", b"")),
                encoding="latin-1",
            )
            benc, ubody = html_to_unicode(
                content_type,
                self.body,
                auto_detect_fun=self._auto_detect_fun,
                default_encoding=self._DEFAULT_ENCODING,
            )
            self._cached_benc = benc
            self._cached_ubody = ubody
        return self._cached_benc

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedErrbackSpider.headers_received [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def headers_received(self, headers, body_length, request, spider):
        self.meta["headers_received"] = headers
        raise StopDownload(fail=True)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.headers_received [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py]
    def headers_received(self, headers, body_length, request, spider):
        self.meta["headers_received"] = headers
        raise StopDownload(fail=False)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware._handle_encoding [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py]
    def _handle_encoding(
        self, body: bytes, content_encoding: list[bytes], max_size: int
    ) -> tuple[bytes, list[bytes]]:
        to_decode, to_keep = self._split_encodings(content_encoding)
        for encoding in to_decode:
            body = self._decode(body, encoding, max_size)
        return body, to_keep

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py::CrawlerRun.headers_received [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_engine.py]
    def headers_received(
        self, headers: Headers, body_length: int, request: Request, spider: Spider
    ) -> None:
        self.headers[request] = headers

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware.process_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py]
    def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None:
        request.headers.setdefault("Accept-Encoding", b", ".join(ACCEPTED_ENCODINGS))
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware.process_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py]
    def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None:
        if request.meta.get("dont_merge_cookies", False):
            return None

        cookiejarkey = request.meta.get("cookiejar")
        jar = self.jars[cookiejarkey]
        cookies = self._get_request_cookies(jar, request)
        self._process_cookies(cookies, jar=jar, request=request)

        # set Cookie header
        request.headers.pop("Cookie", None)
        jar.add_cookie_header(request)
        self._debug_cookie(request)
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_header_redirect [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
    def _test_cookie_header_redirect(
        self,
        source,
        target,
        *,
        cookies2,
    ):
        """Test the handling of a user-defined Cookie header when building a
        redirect follow-up request.

        We follow RFC 6265 for cookie handling. The Cookie header can only
        contain a list of key-value pairs (i.e. no additional cookie
        parameters like Domain or Path). Because of that, we follow the same
        rules that we would follow for the handling of the Set-Cookie response
        header when the Domain is not set: the cookies must be limited to the
        target URL domain (not even subdomains can receive those cookies).

        .. note:: This method tests the scenario where the cookie middleware is
                  disabled. Because of known issue #1992, when the cookies
                  middleware is enabled we do not need to be concerned about
                  the Cookie header getting leaked to unintended domains,
                  because the middleware empties the header from every request.
        """
        if not isinstance(source, dict):
            source = {"url": source}
        if not isinstance(target, dict):
            target = {"url": target}
        target.setdefault("status", 301)

        request1 = Request(headers={"Cookie": b"a=b"}, **source)

        response = Response(
            headers={
                "Location": target["url"],
            },
            **target,
        )

        request2 = self.redirect_middleware.process_response(request1, response)
        assert isinstance(request2, Request)

        cookies = request2.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies2 else None)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::DuplicateHeaderResource.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        request.responseHeaders.setRawHeaders(b"Set-Cookie", [b"a=b", b"c=d"])
        return b""

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._debug_set_cookie [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py]
    def _debug_set_cookie(self, response: Response) -> None:
        if self.debug:
            cl = [
                to_unicode(c, errors="replace")
                for c in response.headers.getlist("Set-Cookie")
            ]
            if cl:
                cookies = "\n".join(f"Set-Cookie: {c}\n" for c in cl)
                msg = f"Received cookies from: {response}\n{cookies}"
                logger.debug(msg, extra={"spider": self.crawler.spider})
```
