# scrapy-27 :: codesearch

query: Fix RedirectMiddleware not honouring meta handle_httpstatus keys

## selected nodes

- rank=1 layer=FUNCTION tokens=504 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=2 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=3 layer=FUNCTION tokens=81 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::ProcessResponseMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py
- rank=4 layer=FUNCTION tokens=136 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClient.testRedirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py
- rank=5 layer=FUNCTION tokens=155 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.on_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=6 layer=FUNCTION tokens=267 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::MetaRefreshMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=7 layer=FUNCTION tokens=160 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py
- rank=8 layer=FUNCTION tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/test_spiders/spider3.py::Spider3.handles_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/test_spiders/spider3.py
- rank=9 layer=FUNCTION tokens=79 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/test_spiders/nested/spider4.py::Spider4.handles_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/test_spiders/nested/spider4.py
- rank=10 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=11 layer=FUNCTION tokens=74 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware.teardown_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=12 layer=FUNCTION tokens=387 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._redirect file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=13 layer=FUNCTION tokens=91 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py
- rank=14 layer=FUNCTION tokens=108 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::TestHttpErrorMiddlewareSettings.mw file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=15 layer=FUNCTION tokens=224 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::RFC2616PolicyTestMixin._process_requestresponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py
- rank=16 layer=FUNCTION tokens=290 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::AjaxCrawlMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
- rank=17 layer=FUNCTION tokens=133 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleResponse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py
- rank=18 layer=FUNCTION tokens=248 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware.handle_referer file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=19 layer=FUNCTION tokens=58 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::res404 file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=20 layer=FUNCTION tokens=473 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware._test_cookie_redirect_scheme_change file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=21 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::TestHttpErrorMiddlewareHandleAll.mw file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=22 layer=FUNCTION tokens=100 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py::SameOriginPolicy.referrer file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py
- rank=23 layer=FUNCTION tokens=47 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py

## context

```text
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _handle_statuses(self, allow_redirects: bool) -> None:
        self.handle_httpstatus_list = None
        if allow_redirects:
            self.handle_httpstatus_list = SequenceExclude(range(300, 400))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::ProcessResponseMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py]
    def process_response(self, request, response):
        return response.replace(request=Request(OVERRIDDEN_URL))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py::TestWebClient.testRedirect [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_webclient.py]
    def testRedirect(self, server_url):
        body = yield getPage(server_url + "redirect")
        assert (
            body
            == b'\n<html>\n    <head>\n        <meta http-equiv="refresh" content="0;URL=/file">\n'
            b'    </head>\n    <body bgcolor="#FFFFFF" text="#000000">\n    '
            b'<a href="/file">click here</a>\n    </body>\n</html>\n'
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::_HttpErrorSpider.on_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
    def on_error(self, failure):
        if isinstance(failure.value, HttpError):
            response = failure.value.response
            if response.status in self.bypass_status_codes:
                self.skipped.add(response.url[-3:])
                return self.parse(response)

        # it assumes there is a response attached to failure
        self.failed.add(failure.value.response.url[-3:])
        return failure

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py::RetryMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/retry.py]
    def process_response(
        self,
        request: Request,
        response: Response,
        spider: scrapy.Spider | None = None,
    ) -> Request | Response:
        if request.meta.get("dont_retry", False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason) or response
        return response

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/test_spiders/spider3.py::Spider3.handles_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/test_spiders/spider3.py]
    def handles_request(cls, request):
        return request.url == "http://spider3.com/onlythis"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/test_spiders/nested/spider4.py::Spider4.handles_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spiderloader/test_spiders/nested/spider4.py]
    def handles_request(cls, request):
        return request.url == "http://spider4.com/onlythis"

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _modify_media_request(self, request: Request) -> None:
        if self.handle_httpstatus_list:
            request.meta["handle_httpstatus_list"] = self.handle_httpstatus_list
        else:
            request.meta["handle_httpstatus_all"] = True

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware.teardown_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
    def teardown_method(self):
        del self.mw
        del self.redirect_middleware

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py::_wrong_credentials [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_proxy_connect.py]
def _wrong_credentials(proxy_url):
    bad_auth_proxy = list(urlsplit(proxy_url))
    bad_auth_proxy[1] = bad_auth_proxy[1].replace("scrapy:scrapy@", "wrong:wronger@")
    return urlunsplit(bad_auth_proxy)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::TestHttpErrorMiddlewareSettings.mw [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
    def mw(self) -> HttpErrorMiddleware:
        crawler = get_crawler(DefaultSpider, {"HTTPERROR_ALLOWED_CODES": (402,)})
        crawler.spider = crawler._create_spider()
        return HttpErrorMiddleware.from_crawler(crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py::RFC2616PolicyTestMixin._process_requestresponse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_httpcache.py]
    def _process_requestresponse(
        mw: HttpCacheMiddleware, request: Request, response: Response | None
    ) -> Response | Request:
        result = None
        try:
            result = mw.process_request(request)
            if result:
                assert isinstance(result, (Request, Response))
                return result
            assert response is not None
            result = mw.process_response(request, response)
            assert isinstance(result, Response)
            return result
        except Exception:
            print("Request", request)
            print("Response", response)
            print("Result", result)
            raise

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::AjaxCrawlMiddleware.process_response [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py]
    def process_response(
        self, request: Request, response: Response, spider: Spider
    ) -> Request | Response:
        if not isinstance(response, HtmlResponse) or response.status != 200:
            return response

        if request.method != "GET":
            # other HTTP methods are either not safe or don't have a body
            return response

        if "ajax_crawlable" in request.meta:  # prevent loops
            return response

        if not self._has_ajax_crawlable_variant(response):
            return response

        ajax_crawl_request = request.replace(url=escape_ajax(request.url + "#!"))
        logger.debug(
            "Downloading AJAX crawlable %(ajax_crawl_request)s instead of %(request)s",
            {"ajax_crawl_request": ajax_crawl_request, "request": request},
            extra={"spider": spider},
        )

        ajax_crawl_request.meta["ajax_crawlable"] = True
        return ajax_crawl_request

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py::ScrapyHTTPPageGetter.handleResponse [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/webclient.py]
    def handleResponse(self, response):
        if self.factory.method.upper() == b"HEAD":
            self.factory.page(b"")
        elif self.length is not None and self.length > 0:
            self.factory.noPage(self._connection_lost_reason)
        else:
            self.factory.page(response)
        self.transport.loseConnection()

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware.handle_referer [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py]
    def handle_referer(self, request: Request, response: Response) -> None:
        """Remove, modify or keep the Referer header of *request* based on the
        *response* that triggered *request*.

        By default, this method finds a run-time instance of
        scrapy.spidermiddlewares.referer.RefererMiddleware (or of a subclass)
        and uses it to set the right Referer header.

        Override this method if you use a different Scrapy component to handle
        Referer headers, of if you want to use a custom logic to set the
        Referer header on redirects.
        """
        request.headers.pop("Referer", None)
        if not self._referer_spider_middleware:
            return
        self._referer_spider_middleware.get_processed_request(request, response)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::res404 [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
def res404() -> Response:
    return _response(req, 404)

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::TestHttpErrorMiddlewareHandleAll.mw [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py]
    def mw(self) -> HttpErrorMiddleware:
        crawler = get_crawler(DefaultSpider, {"HTTPERROR_ALLOW_ALL": True})
        crawler.spider = crawler._create_spider()
        return HttpErrorMiddleware.from_crawler(crawler)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py::SameOriginPolicy.referrer [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/referer.py]
    def referrer(self, response_url: str, request_url: str) -> str | None:
        if self.origin(response_url) == self.origin(request_url):
            return self.stripped_referrer(response_url)
        return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::handle_error [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py]
def handle_error(failure):
    pass
```
