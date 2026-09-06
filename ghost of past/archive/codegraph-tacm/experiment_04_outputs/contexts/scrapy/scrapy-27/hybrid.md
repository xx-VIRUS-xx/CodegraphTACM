# scrapy-27 :: hybrid

query: Fix RedirectMiddleware not honouring meta handle_httpstatus keys

## selected nodes

- rank=1 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=2 layer=FUNCTION tokens=504 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=3 layer=FUNCTION tokens=328 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.run file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=4 layer=FUNCTION tokens=230 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py::HttpxDownloadHandler._warn_unsupported_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/_httpx.py
- rank=5 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_input file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=6 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=7 layer=FUNCTION tokens=356 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._engine_started file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=8 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=9 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::MetaRefreshMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=10 layer=FUNCTION tokens=355 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py::Shell.fetch file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py
- rank=11 layer=FUNCTION tokens=311 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._set_proxy_and_creds file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=12 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware.process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py
- rank=13 layer=FUNCTION tokens=121 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.returns_request_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=14 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=15 layer=FUNCTION tokens=387 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._redirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=16 layer=FUNCTION tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::Item.keys file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _handle_statuses(self, allow_redirects: bool) -> None:
        self.handle_httpstatus_list = None
        if allow_redirects:
            self.handle_httpstatus_list = SequenceExclude(range(300, 400))

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_input [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py]
    def process_spider_input(
        self, response: Response, spider: Spider | None = None
    ) -> None:
        if 200 <= response.status < 300:  # common case
            return
        meta = response.meta
        if meta.get("handle_httpstatus_all", False):
            return
        if "handle_httpstatus_list" in meta:
            allowed_statuses = meta["handle_httpstatus_list"]
        elif self.handle_httpstatus_all:
            return
        else:
            allowed_statuses = getattr(
                self.crawler.spider,
                "handle_httpstatus_list",
                self.handle_httpstatus_list,
            )
        if response.status in allowed_statuses:
            return
        raise HttpError(response, "Ignoring non-200 response")

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _modify_media_request(self, request: Request) -> None:
        if self.handle_httpstatus_list:
            request.meta["handle_httpstatus_list"] = self.handle_httpstatus_list
        else:
            request.meta["handle_httpstatus_all"] = True

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._engine_started [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py]
    def _engine_started(self) -> None:
        self._referer_spider_middleware = self.crawler.get_spider_middleware(
            RefererMiddleware
        )
        if self._referer_spider_middleware:
            return
        redirect_cls = global_object_name(self.__class__)
        referer_cls = global_object_name(RefererMiddleware)
        if self.__class__ in {RedirectMiddleware, MetaRefreshMiddleware}:
            replacement = (
                f"replace {redirect_cls} with a subclass that overrides the "
                f"handle_referer() method"
            )
        else:
            replacement = (
                f"or edit {redirect_cls} (if defined in your code base) to "
                f"override the handle_referer() method, or replace "
                f"{redirect_cls} with a subclass that overrides the "
                f"handle_referer() method."
            )
        logger.warning(
            f"{redirect_cls} found no {referer_cls} instance to handle "
            f"Referer header handling, so the Referer header will be removed "
            f"on redirects. To set a Referer header on redirects, enable "
            f"{referer_cls} (or a subclass), or {replacement}.",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py]
    def __init__(self, settings: BaseSettings):
        self.handle_httpstatus_all: bool = settings.getbool("HTTPERROR_ALLOW_ALL")
        self.handle_httpstatus_list: list[int] = settings.getlist(
            "HTTPERROR_ALLOWED_CODES"
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py::Shell.fetch [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py]
    def fetch(
        self,
        request_or_url: Request | str,
        spider: Spider | None = None,
        redirect: bool = True,
        **kwargs: Any,
    ) -> None:
        if isinstance(request_or_url, Request):
            request = request_or_url
        else:
            url = any_to_uri(request_or_url)
            request = Request(url, dont_filter=True, **kwargs)
            if redirect:
                request.meta["handle_httpstatus_list"] = SequenceExclude(
                    range(300, 400)
                )
            else:
                request.meta["handle_httpstatus_all"] = True
        response: Response | None = None
        if self._use_reactor:
            from twisted.internet import reactor

            with contextlib.suppress(IgnoreRequest):
                response = threads.blockingCallFromThread(
                    reactor, deferred_f_from_coro_f(self._schedule), request, spider
                )
        else:
            assert self._loop
            with contextlib.suppress(IgnoreRequest):
                future = asyncio.run_coroutine_threadsafe(
                    self._schedule(request, spider), self._loop
                )
                response = future.result()
        self.populate_vars(response, request, self.spider)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py::HttpProxyMiddleware._set_proxy_and_creds [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpproxy.py]
    def _set_proxy_and_creds(
        self,
        request: Request,
        proxy_url: str | None,
        creds: bytes | None,
        scheme: str | None,
    ) -> None:
        if scheme:
            request.meta["_scheme_proxy"] = True
        if proxy_url:
            request.meta["proxy"] = proxy_url
        elif request.meta.get("proxy") is not None:
            request.meta["proxy"] = None
        if creds:
            request.headers[b"Proxy-Authorization"] = b"Basic " + creds
            request.meta["_auth_proxy"] = proxy_url
        elif "_auth_proxy" in request.meta:
            if proxy_url != request.meta["_auth_proxy"]:
                if b"Proxy-Authorization" in request.headers:
                    del request.headers[b"Proxy-Authorization"]
                del request.meta["_auth_proxy"]
        elif b"Proxy-Authorization" in request.headers:
            if proxy_url:
                request.meta["_auth_proxy"] = proxy_url
            else:
                del request.headers[b"Proxy-Authorization"]

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py]
    def _assert_request_no3xx(self, pipeline_class, settings):
        pipe = pipeline_class(crawler=get_crawler(None, settings))
        request = Request("http://url")
        pipe._modify_media_request(request)

        assert "handle_httpstatus_list" in request.meta
        for status, check in [
            (200, True),
            # These are the status codes we want
            # the downloader to handle itself
            (301, False),
            (302, False),
            (302, False),
            (307, False),
            (308, False),
            # we still want to get 4xx and 5xx
            (400, True),
            (404, True),
            (500, True),
        ]:
            if check:
                assert status in request.meta["handle_httpstatus_list"]
            else:
                assert status not in request.meta["handle_httpstatus_list"]

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::Item.keys [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py]
    def keys(self) -> KeysView[str]:
        return self._values.keys()
```
