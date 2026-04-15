# scrapy-27 :: tacm-full

query: Fix RedirectMiddleware not honouring meta handle_httpstatus keys

## selected nodes

- rank=1 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=2 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_input file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=3 layer=FUNCTION tokens=504 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=4 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=5 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=6 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=7 layer=FUNCTION tokens=86 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=8 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=9 layer=FUNCTION tokens=109 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=10 layer=FUNCTION tokens=328 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.run file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=11 layer=FUNCTION tokens=72 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.items file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=12 layer=FUNCTION tokens=355 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py::Shell.fetch file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py
- rank=13 layer=FUNCTION tokens=988 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream.close file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py
- rank=14 layer=FUNCTION tokens=116 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py
- rank=15 layer=FUNCTION tokens=356 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._engine_started file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _modify_media_request(self, request: Request) -> None:
        if self.handle_httpstatus_list:
            request.meta["handle_httpstatus_list"] = self.handle_httpstatus_list
        else:
            request.meta["handle_httpstatus_all"] = True

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _handle_statuses(self, allow_redirects: bool) -> None:
        self.handle_httpstatus_list = None
        if allow_redirects:
            self.handle_httpstatus_list = SequenceExclude(range(300, 400))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py]
    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.__init__ [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py]
    def __init__(self, settings: BaseSettings):
        self.handle_httpstatus_all: bool = settings.getbool("HTTPERROR_ALLOW_ALL")
        self.handle_httpstatus_list: list[int] = settings.getlist(
            "HTTPERROR_ALLOWED_CODES"
        )

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.items [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py]
    def items(self) -> Iterable[tuple[bytes, list[bytes]]]:  # type: ignore[override]
        return ((k, self.getlist(k)) for k in self.keys())

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py::Stream.close [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/http2/stream.py]
    def close(
        self,
        reason: StreamCloseReason,
        errors: Sequence[BaseException] | None = None,
        from_protocol: bool = False,
    ) -> None:
        """Based on the reason sent we will handle each case."""
        if self.metadata["stream_closed_server"]:
            raise StreamClosedError(self.stream_id)

        if not isinstance(reason, StreamCloseReason):
            raise TypeError(
                f"Expected StreamCloseReason, received {reason.__class__.__qualname__}"
            )

        # Have default value of errors as an empty list as
        # some cases can add a list of exceptions
        errors = errors or ()

        if not from_protocol:
            self._protocol.pop_stream(self.stream_id)

        self.metadata["stream_closed_server"] = True

        # We do not check for Content-Length or Transfer-Encoding in response headers
        # and add `partial` flag as in HTTP/1.1 as 'A request or response that includes
        # a payload body can include a content-length header field' (RFC 7540 - Section 8.1.2.6)

        # NOTE: Order of handling the events is important here
        # As we immediately cancel the request when maxsize is exceeded while
        # receiving DATA_FRAME's when we have received the headers (not
        # having Content-Length)
        if reason in {
            StreamCloseReason.MAXSIZE_EXCEEDED,
            StreamCloseReason.MAXSIZE_EXCEEDED_ACTUAL,
        }:
            expected_size = int(
                self._response["headers"].get(
                    b"Content-Length", self._response["flow_controlled_size"]
                )
            )
            error_msg = get_maxsize_msg(
                expected_size,
                self._download_maxsize,
                self._request,
                expected=reason == StreamCloseReason.MAXSIZE_EXCEEDED,
            )
            logger.error(error_msg)
            self._deferred_response.errback(DownloadCancelledError(error_msg))

        elif reason is StreamCloseReason.ENDED:
            self._fire_response_deferred()

        # Stream was abruptly ended here
        elif reason is StreamCloseReason.CANCELLED:
            # Client has cancelled the request. Remove all the data
            # received and fire the response deferred with no flags set

            # NOTE: The data is already flushed in Stream.reset_stream() called
            # immediately when the stream needs to be cancelled

            # There maybe no :status in headers, we make
            # HTTP Status Code: 499 - Client Closed Request
            self._response["headers"][":status"] = "499"
            self._fire_response_deferred()

        elif reason is StreamCloseReason.RESET:
            self._deferred_response.errback(
                ResponseFailed(
                    [
                        Failure(
                            f"Remote peer {self._protocol.metadata['ip_address']} sent RST_STREAM",
                            ProtocolError,
                        )
                    ]
                )
            )

        elif reason is StreamCloseReason.CONNECTION_LOST:
            self._deferred_response.errback(ResponseFailed(errors))

        elif reason is StreamCloseReason.INACTIVE:
            errors = (InactiveStreamClosed(self._request), *errors)
            self._deferred_response.errback(ResponseFailed(errors))

        else:
            assert reason is StreamCloseReason.INVALID_HOSTNAME
            self._deferred_response.errback(
                InvalidHostname(
                    self._request,
                    str(self._protocol.metadata["uri"].host, "utf-8"),
                    f"{self._protocol.metadata['ip_address']}:{self._protocol.metadata['uri'].port}",
                )
            )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py::TestCookiesMiddleware.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_cookies.py]
    def setup_method(self):
        crawler = get_crawler(DefaultSpider)
        crawler.spider = crawler._create_spider()
        self.mw = CookiesMiddleware.from_crawler(crawler)
        self.redirect_middleware = RedirectMiddleware.from_crawler(crawler)

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
```
