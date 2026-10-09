# scrapy-27 :: minilm

query: Fix RedirectMiddleware not honouring meta handle_httpstatus keys

## selected nodes

- rank=1 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=2 layer=FUNCTION tokens=666 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._build_redirect_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=3 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::MetaRefreshMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=4 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._warn_unsupported_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=5 layer=FUNCTION tokens=504 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=6 layer=FUNCTION tokens=387 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._redirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=7 layer=FUNCTION tokens=473 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect_scheme_change file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=8 layer=FUNCTION tokens=328 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.run file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=9 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py::ScrapyProxyH2Agent.get_key file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py
- rank=10 layer=FUNCTION tokens=218 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._redirect_request_using_get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=11 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=12 layer=FUNCTION tokens=246 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingAgent._requestWithEndpoint file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=13 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.returns_request_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=14 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _handle_statuses(self, allow_redirects: bool) -> None:
        self.handle_httpstatus_list = None
        if allow_redirects:
            self.handle_httpstatus_list = SequenceExclude(range(300, 400))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._build_redirect_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py]
    def _build_redirect_request(
        self, source_request: Request, response: Response, *, url: str, **kwargs: Any
    ) -> Request:
        redirect_request = source_request.replace(
            url=url,
            **kwargs,
            cls=None,
            cookies=None,
        )
        if "_scheme_proxy" in redirect_request.meta:
            source_request_scheme = urlparse_cached(source_request).scheme
            redirect_request_scheme = urlparse_cached(redirect_request).scheme
            if source_request_scheme != redirect_request_scheme:
                redirect_request.meta.pop("_scheme_proxy")
                redirect_request.meta.pop("proxy", None)
                redirect_request.meta.pop("_auth_proxy", None)
                redirect_request.headers.pop(b"Proxy-Authorization", None)

        has_cookie_header = "Cookie" in redirect_request.headers
        has_authorization_header = "Authorization" in redirect_request.headers
        if has_cookie_header or has_authorization_header:
            default_ports = {"http": 80, "https": 443}

            parsed_source_request = urlparse_cached(source_request)
            source_scheme, source_host, source_port = (
                parsed_source_request.scheme,
                parsed_source_request.hostname,
                parsed_source_request.port
                or default_ports.get(parsed_source_request.scheme),
            )

            parsed_redirect_request = urlparse_cached(redirect_request)
            redirect_scheme, redirect_host, redirect_port = (
                parsed_redirect_request.scheme,
                parsed_redirect_request.hostname,
                parsed_redirect_request.port
                or default_ports.get(parsed_redirect_request.scheme),
            )

            if has_cookie_header and (
                redirect_scheme not in {source_scheme, "https"}
                or source_host != redirect_host
            ):
                del redirect_request.headers["Cookie"]

            # https://fetch.spec.whatwg.org/#ref-for-cors-non-wildcard-request-header-name
            if has_authorization_header and (
                source_scheme != redirect_scheme
                or source_host != redirect_host
                or source_port != redirect_port
            ):
                del redirect_request.headers["Authorization"]

        self.handle_referer(redirect_request, response)

        return redirect_request

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::MetaRefreshMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py]
    def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response:
        if (
            request.meta.get("dont_redirect", False)
            or request.method == "HEAD"
            or not isinstance(response, HtmlResponse)
            or urlparse_cached(request).scheme not in {"http", "https"}
        ):
            return response

        interval, url = get_meta_refresh(response, ignore_tags=self._ignore_tags)
        if not url:
            return response
        redirected = self._redirect_request_using_get(request, response, url)
        if urlparse_cached(redirected).scheme not in {"http", "https"}:
            return response
        if cast("float", interval) < self._maxdelay:
            return self._redirect(redirected, request, "meta refresh")
        return response

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._warn_unsupported_meta [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py]
    def _warn_unsupported_meta(self, meta: dict[str, Any]) -> None:
        if meta.get("bindaddress"):
            # configurable only per-client:
            # https://github.com/encode/httpx/issues/755#issuecomment-2746121794
            logger.error(
                f"The 'bindaddress' request meta key is not supported by"
                f" {type(self).__name__} and will be ignored."
            )
        if meta.get("proxy"):
            # configurable only per-client:
            # https://github.com/encode/httpx/issues/486
            logger.error(
                f"The 'proxy' request meta key is not supported by"
                f" {type(self).__name__} and will be ignored."
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py]
    def process_response(
        self, request: Request, response: Response, spider: Spider | None = None
    ) -> Request | Response:
        if (
            request.meta.get("dont_redirect", False)
            or response.status
            in getattr(self.crawler.spider, "handle_httpstatus_list", ())
            or response.status in request.meta.get("handle_httpstatus_list", ())
            or request.meta.get("handle_httpstatus_all", False)
        ):
            return response

        if "Location" not in response.headers or response.status not in {
            301,
            302,
            303,
            307,
            308,
        }:
            return response

        assert response.headers["Location"] is not None
        location = safe_url_string(response.headers["Location"])
        if response.headers["Location"].startswith(b"//"):
            request_scheme = urlparse_cached(request).scheme
            location = request_scheme + "://" + location.lstrip("/")

        redirected_url = urljoin(request.url, location)

        if not urlparse(redirected_url).fragment:
            fragment = urlparse_cached(request).fragment
            if fragment:
                redirected_url = urljoin(redirected_url, f"#{fragment}")

        redirected = self._build_redirect_request(request, response, url=redirected_url)
        if urlparse_cached(redirected).scheme not in {"http", "https"}:
            return response

        if (response.status in {301, 302} and request.method == "POST") or (
            response.status == 303 and request.method not in {"GET", "HEAD"}
        ):
            redirected = self._redirect_request_using_get(
                request, response, redirected_url
            )

        return self._redirect(redirected, request, response.status)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._redirect [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py]
    def _redirect(self, redirected: Request, request: Request, reason: Any) -> Request:
        ttl = request.meta.setdefault("redirect_ttl", self.max_redirect_times)
        redirects = request.meta.get("redirect_times", 0) + 1

        if ttl and redirects <= self.max_redirect_times:
            redirected.meta["redirect_times"] = redirects
            redirected.meta["redirect_ttl"] = ttl - 1
            redirected.meta["redirect_urls"] = [
                *request.meta.get("redirect_urls", []),
                request.url,
            ]
            redirected.meta["redirect_reasons"] = [
                *request.meta.get("redirect_reasons", []),
                reason,
            ]
            redirected.dont_filter = request.dont_filter
            redirected.priority = request.priority + self.priority_adjust
            logger.debug(
                "Redirecting (%(reason)s) to %(redirected)s from %(request)s",
                {"reason": reason, "redirected": redirected, "request": request},
                extra={"spider": self.crawler.spider},
            )
            return redirected
        logger.debug(
            "Discarding %(request)s: max redirections reached",
            {"request": request},
            extra={"spider": self.crawler.spider},
        )
        raise IgnoreRequest("max redirections reached")

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.run [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py]
    def run(self, args: list[str], opts: Namespace) -> None:
        if len(args) != 1 or not is_url(args[0]):
            raise UsageError
        request = Request(
            args[0],
            callback=self._print_response,
            cb_kwargs={"opts": opts},
            dont_filter=True,
        )
        # by default, let the framework handle redirects,
        # i.e. command handles all codes expect 3xx
        if not opts.no_redirect:
            request.meta["handle_httpstatus_list"] = SequenceExclude(range(300, 400))
        else:
            request.meta["handle_httpstatus_all"] = True

        spidercls: type[Spider] = DefaultSpider
        assert self.crawler_process
        spider_loader = self.crawler_process.spider_loader
        if opts.spider:
            spidercls = spider_loader.load(opts.spider)
        else:
            spidercls = spidercls_for_request(spider_loader, request, spidercls)

        async def start(self: Spider) -> AsyncIterator[Any]:
            yield request

        spidercls.start = start  # type: ignore[method-assign]

        self.crawler_process.crawl(spidercls)
        self.crawler_process.start()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py::ScrapyProxyH2Agent.get_key [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/agent.py]
    def get_key(self, uri: URI) -> ConnectionKeyT:
        """We use the proxy uri instead of uri obtained from request url"""
        return b"http-proxy", self._proxy_uri.host, self._proxy_uri.port

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._redirect_request_using_get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py]
    def _redirect_request_using_get(
        self, request: Request, response: Response, redirect_url: str
    ) -> Request:
        redirect_request = self._build_redirect_request(
            request,
            response,
            url=redirect_url,
            method="GET",
            body="",
        )
        redirect_request.headers.pop("Content-Type", None)
        redirect_request.headers.pop("Content-Length", None)
        redirect_request.headers.pop("Content-Encoding", None)
        redirect_request.headers.pop("Content-Language", None)
        redirect_request.headers.pop("Content-Location", None)
        return redirect_request

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py]
    def process_request(
        self, request: Request, spider: Spider | None = None
    ) -> Request | Response | None:
        creds, proxy_url, scheme = None, None, None
        if "proxy" in request.meta:
            if request.meta["proxy"] is not None:
                creds, proxy_url = self._get_proxy(request.meta["proxy"], "")
        elif self.proxies:
            parsed = urlparse_cached(request)
            _scheme = parsed.scheme
            if (
                # 'no_proxy' is only supported by http schemes
                _scheme not in {"http", "https"}
                or (parsed.hostname and not proxy_bypass(parsed.hostname))
            ) and _scheme in self.proxies:
                scheme = _scheme
                creds, proxy_url = self.proxies[scheme]

        self._set_proxy_and_creds(request, proxy_url, creds, scheme)
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingAgent._requestWithEndpoint [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py]
    def _requestWithEndpoint(
        self,
        key: Any,
        endpoint: TCP4ClientEndpoint,
        method: bytes,
        parsedURI: URI,
        headers: TxHeaders | None,
        bodyProducer: IBodyProducer | None,
        requestPath: bytes,
    ) -> Deferred[IResponse]:
        # proxy host and port are required for HTTP pool `key`
        # otherwise, same remote host connection request could reuse
        # a cached tunneled connection to a different proxy
        key += self._proxyConf
        return super()._requestWithEndpoint(
            key=key,
            endpoint=endpoint,
            method=method,
            parsedURI=parsedURI,
            headers=headers,
            bodyProducer=bodyProducer,
            requestPath=requestPath,
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.returns_request_meta [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py]
    def returns_request_meta(self, response):
        """method which returns request
        @url https://example.org
        @meta {"cookiejar": "session1"}
        @returns requests 1
        """
        return Request(
            "https://example.org", meta=response.meta, callback=self.returns_item_meta
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py::BaseMockServer.url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/mockserver/http_base.py]
    def url(self, path: str, is_secure: bool = False) -> str:
        port = self.port(is_secure)
        scheme = "https" if is_secure else "http"
        return f"{scheme}://{self.host}:{port}{path}"
```
