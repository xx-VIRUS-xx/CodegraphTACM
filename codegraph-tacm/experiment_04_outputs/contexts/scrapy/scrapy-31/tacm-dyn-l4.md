# scrapy-31 :: tacm-dyn-l4

query: Do not break cookie parsing on non-utf8 headers

## selected nodes

- rank=1 layer=FILE tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=2 layer=CLASS tokens=557 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=3 layer=FUNCTION tokens=415 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect_scheme_change file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=4 layer=FUNCTION tokens=201 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_server_set_cookie_domain_followup file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=5 layer=FUNCTION tokens=265 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=6 layer=FUNCTION tokens=420 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._format_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=7 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=8 layer=FUNCTION tokens=175 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_user_set_cookie_domain_followup file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=9 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=10 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.headers file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=11 layer=FUNCTION tokens=270 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::_parse_headers_and_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py
- rank=12 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py::CookiesMiddleware._process_cookies file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/cookies.py
- rank=13 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=14 layer=FUNCTION tokens=266 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/request.py::request_to_curl file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/request.py
- rank=15 layer=CLASS tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_robotstxt_interface.py::TestDecodeRobotsTxt file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_robotstxt_interface.py
- rank=16 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=17 layer=FUNCTION tokens=235 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::_cookie_to_set_cookie_value file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=18 layer=FUNCTION tokens=320 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.add_cookie_header file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=19 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py::CookieJar.set_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/cookies.py
- rank=20 layer=FUNCTION tokens=15 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::_NullCookieJar.set_cookie file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=21 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=22 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py

## context

```text
file scrapy/http/headers.py
imports: __future__, collections, typing, w3lib, scrapy, typing_extensions
defines: Headers

class TestCookiesMiddleware:  [scrapy/tests/test_downloadermiddleware_cookies.py:54]
methods: _test_cookie_header_redirect, _test_cookie_redirect
         _test_cookie_redirect_scheme_change
         _test_server_set_cookie_domain_followup
         _test_user_set_cookie_domain_followup
         assertCookieValEqual, setup_method, split_cookies
         teardown_method, test_basic, test_complex_cookies
         test_cookie_header_redirect_different_domain
         test_cookie_header_redirect_different_domain_forcing_get
         test_cookie_header_redirect_same_domain
         test_cookie_header_redirect_same_domain_forcing_get
         test_cookie_redirect_different_domain
         test_cookie_redirect_different_domain_forcing_get
         test_cookie_redirect_same_domain
         test_cookie_redirect_same_domain_forcing_get
         test_cookie_redirect_secure_false_downgrade
         test_cookie_redirect_secure_false_upgrade
         test_cookie_redirect_secure_true_downgrade
         test_cookie_redirect_secure_true_upgrade
         test_cookie_redirect_secure_undefined_downgrade
         test_cookie_redirect_secure_undefined_upgrade
         test_cookiejar_key
         test_do_not_break_on_non_utf8_header
         test_dont_merge_cookies, test_invalid_cookies
         test_keep_cookie_from_default_request_headers_middleware
         test_keep_cookie_header, test_local_domain
         test_merge_request_cookies
         test_primitive_type_cookies
         test_request_cookies_encoding
         test_request_headers_cookie_encoding
         test_server_set_cookie_domain_public_period
         test_server_set_cookie_domain_suffix_private
         test_server_set_cookie_domain_suffix_public_period
         test_server_set_cookie_domain_suffix_public_private
         test_setting_default_cookies_enabled
         test_setting_disabled_cookies_debug
         test_setting_enabled_cookies_debug
         test_setting_false_cookies_enabled
         test_setting_true_cookies_enabled
         test_user_set_cookie_domain_public_period
         test_user_set_cookie_domain_suffix_private
         test_user_set_cookie_domain_suffix_public_period
         test_user_set_cookie_domain_suffix_public_private

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

    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

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

class Request(object_ref):  [http/request/__init__.py:84]
methods: _set_body, _set_url, body, cb_kwargs, cookies, cookies
         copy, encoding, flags, flags, from_curl, headers
         headers, meta, replace, replace, replace, to_dict
         url, __init__, __repr__

    def headers(
        self, value: Mapping[AnyStr, Any] | Iterable[tuple[AnyStr, Any]] | None
    ) -> None:
        if isinstance(value, Headers):
            self._headers = value
        else:
            self._headers = (
                Headers(value, encoding=self.encoding) if value is not None else None
            )

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

class TestDecodeRobotsTxt:  [scrapy/tests/test_robotstxt_interface.py:114]
methods: test_decode_non_utf8, test_decode_utf8
         test_decode_utf8_bom, test_native_string_conversion

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

# --- Layer 04: Variable context ---
# call-chain context
  called by: _get_request_cookies [cookies.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: curl_to_request_kwargs [curl.py]

# call-chain context
  called by: process_request [cookies.py]
  called by: process_response [cookies.py]

# call-chain context
  called by: _test_request [test_utils_request.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: _cookies_to_set_cookie_list [test_downloadermiddleware_cookies.py]

```
