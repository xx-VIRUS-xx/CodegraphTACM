# scrapy-31 :: hybrid-cs

query: Do not break cookie parsing on non-utf8 headers

## selected nodes

- rank=1 layer=FUNCTION tokens=470 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._format_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=2 layer=FUNCTION tokens=309 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::_parse_headers_and_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py
- rank=3 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::_cookie_to_set_cookie_value file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=4 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._process_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=5 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._debug_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=6 layer=FUNCTION tokens=487 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_header_redirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=7 layer=FUNCTION tokens=473 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect_scheme_change file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=8 layer=FUNCTION tokens=360 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.add_cookie_header file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=9 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=10 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::SetCookie.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=11 layer=FUNCTION tokens=165 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._debug_set_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=12 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._get_request_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=13 layer=FUNCTION tokens=319 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=14 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::_cookies_to_set_cookie_list file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect_scheme_change [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
    def _test_cookie_redirect_scheme_change(
        self, secure, from_scheme, to_scheme, cookies1, cookies2, cookies3
    ):
        """When a redirect causes the URL scheme to change from *from_scheme*
        to *to_scheme*, while domain and port remain the same, and given a
        cookie on the initial request with its secure attribute set to
        *secure*, check if the cookie should be set on the Cookie header of the
        initial request (*cookies1*), if it should be kept by the redirect
        middleware (*cookies2*), and if it should be present on the Cookie
        header in the redirected request (*cookie3*)."""
        cookie_kwargs = {}
        if secure is not UNSET:
            cookie_kwargs["secure"] = secure
        input_cookies = [{"name": "a", "value": "b", **cookie_kwargs}]

        request1 = Request(f"{from_scheme}://a.example", cookies=input_cookies)
        self.mw.process_request(request1)
        cookies = request1.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies1 else None)

        response = Response(
            f"{from_scheme}://a.example",
            headers={"Location": f"{to_scheme}://a.example"},
            status=301,
        )
        assert self.mw.process_response(request1, response) == response

        request2 = self.redirect_middleware.process_response(request1, response)
        assert isinstance(request2, Request)
        cookies = request2.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies2 else None)

        self.mw.process_request(request2)
        cookies = request2.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies3 else None)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::SetCookie.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        for cookie_name, cookie_values in request.args.items():
            for cookie_value in cookie_values:
                cookie = (cookie_name.decode() + "=" + cookie_value.decode()).encode()
                request.setHeader(b"Set-Cookie", cookie)
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._get_request_cookies [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py]
    def _get_request_cookies(
        self, jar: CookieJar, request: Request
    ) -> Sequence[Cookie]:
        """
        Extract cookies from the Request.cookies attribute
        """
        if not request.cookies:
            return ()
        cookies: Iterable[VerboseCookie]
        if isinstance(request.cookies, dict):
            cookies = tuple({"name": k, "value": v} for k, v in request.cookies.items())
        else:
            cookies = request.cookies
        for cookie in cookies:
            cookie.setdefault("secure", urlparse_cached(request).scheme == "https")
        formatted = filter(None, (self._format_cookie(c, request) for c in cookies))
        response = Response(request.url, headers={"Set-Cookie": formatted})
        return jar.make_cookies(response, request)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
    def _test_cookie_redirect(
        self,
        source,
        target,
        *,
        cookies1,
        cookies2,
    ):
        input_cookies = {"a": "b"}

        if not isinstance(source, dict):
            source = {"url": source}
        if not isinstance(target, dict):
            target = {"url": target}
        target.setdefault("status", 301)

        request1 = Request(cookies=input_cookies, **source)
        self.mw.process_request(request1)
        cookies = request1.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies1 else None)

        response = Response(
            headers={
                "Location": target["url"],
            },
            **target,
        )
        assert self.mw.process_response(request1, response) == response

        request2 = self.redirect_middleware.process_response(request1, response)
        assert isinstance(request2, Request)

        self.mw.process_request(request2)
        cookies = request2.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies2 else None)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::_cookies_to_set_cookie_list [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
def _cookies_to_set_cookie_list(cookies):
    """Given a group of cookie defined either as a dictionary or as a list of
    dictionaries (i.e. in a format supported by the cookies parameter of
    Request), return the equivalen list of strings that can be associated to a
    ``Set-Cookie`` header."""
    if not cookies:
        return []
    if isinstance(cookies, dict):
        cookies = ({"name": k, "value": v} for k, v in cookies.items())
    return filter(None, (_cookie_to_set_cookie_value(cookie) for cookie in cookies))
```
