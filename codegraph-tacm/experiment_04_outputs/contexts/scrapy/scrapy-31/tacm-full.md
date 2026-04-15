# scrapy-31 :: tacm-full

query: Do not break cookie parsing on non-utf8 headers

## selected nodes

- rank=1 layer=FUNCTION tokens=473 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect_scheme_change file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=2 layer=FUNCTION tokens=470 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._format_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=3 layer=FUNCTION tokens=260 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_server_set_cookie_domain_followup file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=4 layer=FUNCTION tokens=285 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::_cookie_to_set_cookie_value file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=5 layer=FUNCTION tokens=319 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=6 layer=FUNCTION tokens=210 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._process_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=7 layer=FUNCTION tokens=309 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::_parse_headers_and_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py
- rank=8 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=9 layer=FUNCTION tokens=250 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._get_request_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=10 layer=FUNCTION tokens=233 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_user_set_cookie_domain_followup file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=11 layer=FUNCTION tokens=196 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=12 layer=FUNCTION tokens=303 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/request.py::request_to_curl file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/request.py
- rank=13 layer=FUNCTION tokens=119 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::SetCookie.render file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py
- rank=14 layer=FUNCTION tokens=59 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.set_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=15 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._debug_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=16 layer=FUNCTION tokens=56 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.__iter__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_server_set_cookie_domain_followup [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
    def _test_server_set_cookie_domain_followup(
        self,
        url1,
        url2,
        domain,
        *,
        cookies,
    ):
        request1 = Request(url1)
        self.mw.process_request(request1)

        input_cookies = [
            {
                "name": "a",
                "value": "b",
                "domain": domain,
            }
        ]

        headers = {
            "Set-Cookie": _cookies_to_set_cookie_list(input_cookies),
        }
        response = Response(url1, status=200, headers=headers)
        assert self.mw.process_response(request1, response) == response

        request2 = Request(url2)
        self.mw.process_request(request2)
        actual_cookies = request2.headers.get("Cookie")
        assert actual_cookies == (b"a=b" if cookies else None)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py]
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_user_set_cookie_domain_followup [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
    def _test_user_set_cookie_domain_followup(
        self,
        url1,
        url2,
        domain,
        *,
        cookies1,
        cookies2,
    ):
        input_cookies = [
            {
                "name": "a",
                "value": "b",
                "domain": domain,
            }
        ]

        request1 = Request(url1, cookies=input_cookies)
        self.mw.process_request(request1)
        cookies = request1.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies1 else None)

        request2 = Request(url2)
        self.mw.process_request(request2)
        cookies = request2.headers.get("Cookie")
        assert cookies == (b"a=b" if cookies2 else None)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/request.py::request_to_curl [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/request.py]
def request_to_curl(request: Request) -> str:
    """
    Converts a :class:`~scrapy.Request` object to a curl command.

    :param :class:`~scrapy.Request`: Request object to be converted
    :return: string containing the curl command
    """
    method = request.method

    data = f"--data-raw '{request.body.decode('utf-8')}'" if request.body else ""

    headers = " ".join(
        f"-H '{k.decode()}: {v[0].decode()}'" for k, v in request.headers.items()
    )

    url = request.url
    cookies = ""
    if request.cookies:
        if isinstance(request.cookies, dict):
            cookie = "; ".join(f"{k}={v}" for k, v in request.cookies.items())
            cookies = f"--cookie '{cookie}'"
        elif isinstance(request.cookies, list):
            cookie = "; ".join(
                f"{next(iter(c.keys()))}={next(iter(c.values()))}"
                for c in request.cookies
            )
            cookies = f"--cookie '{cookie}'"

    curl_cmd = f"curl -X {method} {url} {data} {headers} {cookies}".strip()
    return " ".join(curl_cmd.split())

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py::SetCookie.render [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_resources.py]
    def render(self, request):
        for cookie_name, cookie_values in request.args.items():
            for cookie_value in cookie_values:
                cookie = (cookie_name.decode() + "=" + cookie_value.decode()).encode()
                request.setHeader(b"Set-Cookie", cookie)
        return b""

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.set_cookie [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def set_cookie(self, cookie: Cookie) -> None:
        self.jar.set_cookie(cookie)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.__iter__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py]
    def __iter__(self) -> Iterator[Cookie]:
        return iter(self.jar)
```
