# scrapy-7 :: tacm-rerank

query: FormRequest: handle whitespaces in action attribute properly

## selected nodes

- rank=1 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_form_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=2 layer=FUNCTION tokens=107 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=3 layer=FUNCTION tokens=504 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=4 layer=FUNCTION tokens=205 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_output file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=5 layer=FUNCTION tokens=94 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=6 layer=FUNCTION tokens=190 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=7 layer=FUNCTION tokens=244 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_input file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=8 layer=FUNCTION tokens=126 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::attribute file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=9 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::warn_on_deprecated_spider_attribute file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=10 layer=FUNCTION tokens=182 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py
- rank=11 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py
- rank=12 layer=FUNCTION tokens=303 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py
- rank=13 layer=FUNCTION tokens=420 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_output_async file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=14 layer=FUNCTION tokens=82 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::rel_has_nofollow file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py
- rank=15 layer=FUNCTION tokens=291 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=16 layer=FUNCTION tokens=269 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=17 layer=FUNCTION tokens=64 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py::SignalManager.handle file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py
- rank=18 layer=FUNCTION tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py::TestSettingsAttribute.setup_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py
- rank=19 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py::CallLaterResult.cancel file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py
- rank=20 layer=FUNCTION tokens=93 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py::CallLaterResult.from_asyncio file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py
- rank=21 layer=FUNCTION tokens=171 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware.open_spider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py

## context

```text
# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_form_url [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py]
def _get_form_url(form: FormElement, url: str | None) -> str:
    assert form.base_url is not None  # typing
    if url is None:
        action = form.get("action")
        if action is None:
            return form.base_url
        return urljoin(form.base_url, strip_html5_whitespace(action))
    return urljoin(form.base_url, url)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _modify_media_request(self, request: Request) -> None:
        if self.handle_httpstatus_list:
            request.meta["handle_httpstatus_list"] = self.handle_httpstatus_list
        else:
            request.meta["handle_httpstatus_all"] = True

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_output [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py]
    def handle_spider_output(
        self,
        result: Iterable[_T] | AsyncIterator[_T],
        request: Request,
        response: Response | Failure,
        spider: Spider | None = None,
    ) -> Deferred[None]:  # pragma: no cover
        """Pass items/requests produced by a callback to ``_process_spidermw_output()`` in parallel."""
        warnings.warn(
            "Scraper.handle_spider_output() is deprecated, use handle_spider_output_async() instead",
            ScrapyDeprecationWarning,
            stacklevel=2,
        )
        return deferred_from_coro(
            self.handle_spider_output_async(result, request, response)
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py]
    def _handle_statuses(self, allow_redirects: bool) -> None:
        self.handle_httpstatus_list = None
        if allow_redirects:
            self.handle_httpstatus_list = SequenceExclude(range(300, 400))

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py]
    def add_options(self, parser: ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument("--spider", dest="spider", help="use this spider")
        parser.add_argument(
            "--headers",
            dest="headers",
            action="store_true",
            help="print response HTTP headers instead of body",
        )
        parser.add_argument(
            "--no-redirect",
            dest="no_redirect",
            action="store_true",
            default=False,
            help="do not handle HTTP 3xx status codes and print response as-is",
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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::attribute [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py]
def attribute(obj: Any, oldattr: str, newattr: str, version: str = "0.12") -> None:
    cname = obj.__class__.__name__
    warnings.warn(
        f"{cname}.{oldattr} attribute is deprecated and will be no longer supported "
        f"in Scrapy {version}, use {cname}.{newattr} attribute instead",
        ScrapyDeprecationWarning,
        stacklevel=3,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::warn_on_deprecated_spider_attribute [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py]
def warn_on_deprecated_spider_attribute(attribute_name: str, setting_name: str) -> None:
    warnings.warn(
        f"The '{attribute_name}' spider attribute is deprecated. "
        "Use Spider.custom_settings or Spider.update_settings() instead. "
        f"The corresponding setting name is '{setting_name}'.",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py]
    def add_options(self, parser: ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-c",
            dest="code",
            help="evaluate the code in the shell, print the result and exit",
        )
        parser.add_argument("--spider", dest="spider", help="use this spider")
        parser.add_argument(
            "--no-redirect",
            dest="no_redirect",
            action="store_true",
            default=False,
            help="do not handle HTTP 3xx status codes and print response as-is",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-l",
            "--list",
            dest="list",
            action="store_true",
            help="only list contracts, without checking them",
        )
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            default=False,
            action="store_true",
            help="print contract tests for all spiders",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py::Command.add_options [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/genspider.py]
    def add_options(self, parser: argparse.ArgumentParser) -> None:
        super().add_options(parser)
        parser.add_argument(
            "-l",
            "--list",
            dest="list",
            action="store_true",
            help="List available templates",
        )
        parser.add_argument(
            "-e",
            "--edit",
            dest="edit",
            action="store_true",
            help="Edit spider after creating it",
        )
        parser.add_argument(
            "-d",
            "--dump",
            dest="dump",
            metavar="TEMPLATE",
            help="Dump template to standard output",
        )
        parser.add_argument(
            "-t",
            "--template",
            dest="template",
            default="basic",
            help="Uses a custom template.",
        )
        parser.add_argument(
            "--force",
            dest="force",
            action="store_true",
            help="If the spider already exists, overwrite it with the template",
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_output_async [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py]
    async def handle_spider_output_async(
        self,
        result: Iterable[_T] | AsyncIterator[_T],
        request: Request,
        response: Response | Failure,
    ) -> None:
        """Pass items/requests produced by a callback to ``_process_spidermw_output()`` in parallel.

        .. versionadded:: 2.13
        """
        it: Iterable[_T] | AsyncIterator[_T]
        if is_asyncio_available():
            if isinstance(result, AsyncIterator):
                it = aiter_errback(result, self.handle_spider_error, request, response)
            else:
                it = iter_errback(result, self.handle_spider_error, request, response)
            await _parallel_asyncio(
                it, self.concurrent_items, self._process_spidermw_output_async, response
            )
            return
        if isinstance(result, AsyncIterator):
            it = aiter_errback(result, self.handle_spider_error, request, response)
            await maybe_deferred_to_future(
                parallel_async(
                    it,
                    self.concurrent_items,
                    self._process_spidermw_output,
                    response,
                )
            )
            return
        it = iter_errback(result, self.handle_spider_error, request, response)
        await maybe_deferred_to_future(
            parallel(
                it,
                self.concurrent_items,
                self._process_spidermw_output,
                response,
            )
        )

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py::rel_has_nofollow [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/misc.py]
def rel_has_nofollow(rel: str | None) -> bool:
    """Return True if link rel attribute has nofollow type"""
    return rel is not None and "nofollow" in rel.replace(",", " ").split()

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

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py::SignalManager.handle [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py]
        def handle() -> None:
            self.disconnect(handle, signal)
            d.callback(None)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py::TestSettingsAttribute.setup_method [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_settings/__init__.py]
    def setup_method(self):
        self.attribute = SettingsAttribute("value", 10)

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py::CallLaterResult.cancel [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py]
    def cancel(self) -> None:
        """Cancel the underlying delayed call.

        Does nothing if the delayed call was already called or cancelled.
        """
        if self._timer_handle:
            self._timer_handle.cancel()
            self._timer_handle = None
        elif self._delayed_call and self._delayed_call.active():
            self._delayed_call.cancel()
            self._delayed_call = None

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py::CallLaterResult.from_asyncio [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py]
    def from_asyncio(cls, timer_handle: asyncio.TimerHandle) -> Self:
        """Create a CallLaterResult from an asyncio TimerHandle."""
        o = cls()
        o._timer_handle = timer_handle
        return o

# /Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py::HttpCompressionMiddleware.open_spider [/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/httpcompression.py]
    def open_spider(self, spider: Spider) -> None:
        if hasattr(spider, "download_maxsize"):
            warn_on_deprecated_spider_attribute("download_maxsize", "DOWNLOAD_MAXSIZE")
            self._max_size = spider.download_maxsize
        if hasattr(spider, "download_warnsize"):
            warn_on_deprecated_spider_attribute(
                "download_warnsize", "DOWNLOAD_WARNSIZE"
            )
            self._warn_size = spider.download_warnsize
```
