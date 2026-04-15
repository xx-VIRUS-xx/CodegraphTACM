# scrapy-27 :: tacm-dyn-l4

query: Fix RedirectMiddleware not honouring meta handle_httpstatus keys

## selected nodes

- rank=1 layer=FILE tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=2 layer=CLASS tokens=49 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py::TestHttpErrorMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_httperror.py
- rank=3 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=4 layer=CLASS tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=5 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._modify_media_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=6 layer=FUNCTION tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_input file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=7 layer=FILE tokens=46 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
- rank=8 layer=CLASS tokens=67 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=9 layer=FUNCTION tokens=218 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=10 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=11 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py::MyRedirectMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_downloadermiddleware_redirect.py
- rank=12 layer=FUNCTION tokens=111 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=13 layer=FILE tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=14 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=15 layer=CLASS tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=16 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=17 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=18 layer=FUNCTION tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=19 layer=FUNCTION tokens=241 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py::_has_ajaxcrawlable_meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
- rank=20 layer=FUNCTION tokens=290 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.run file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=21 layer=FILE tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/conf.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/conf.py
- rank=22 layer=CLASS tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=23 layer=FUNCTION tokens=470 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper._scrape file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=24 layer=FUNCTION tokens=378 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_output_async file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=25 layer=FUNCTION tokens=191 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/conf.py::_map_keys file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/conf.py
- rank=26 layer=FUNCTION tokens=304 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::BaseRedirectMiddleware._engine_started file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=27 layer=FUNCTION tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py::Request.meta file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/__init__.py
- rank=28 layer=CLASS tokens=97 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request_json.py::TestJsonRequest file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_http_request_json.py
- rank=29 layer=FUNCTION tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py::get_meta_refresh file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/response.py
- rank=30 layer=CLASS tokens=61 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::Item file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py
- rank=31 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py::Item.keys file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/item.py
- rank=32 layer=FUNCTION tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.items file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=33 layer=FUNCTION tokens=8 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py

## context

```text
file scrapy/downloadermiddlewares/redirect.py
imports: __future__, logging, typing, urllib, w3lib, scrapy, typing_extensions
defines: BaseRedirectMiddleware, RedirectMiddleware, MetaRefreshMiddleware

class TestHttpErrorMiddleware:  [scrapy/tests/test_spidermiddleware_httperror.py:74]
methods: mw, test_handle_httpstatus_list
         test_process_spider_exception
         test_process_spider_input

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

    # ... truncated

class RedirectMiddleware(BaseRedirectMiddleware):  [scrapy/downloadermiddlewares/redirect.py:198]
methods: process_response

    def _modify_media_request(self, request: Request) -> None:
        if self.handle_httpstatus_list:
            request.meta["handle_httpstatus_list"] = self.handle_httpstatus_list
        else:
            request.meta["handle_httpstatus_all"] = True

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

file scrapy/downloadermiddlewares/ajaxcrawl.py
imports: __future__, logging, re, typing, warnings, w3lib, scrapy, typing_extensions
defines: AjaxCrawlMiddleware, _has_ajaxcrawlable_meta

class Request(object_ref):  [http/request/__init__.py:84]
methods: _set_body, _set_url, body, cb_kwargs, cookies, cookies
         copy, encoding, flags, flags, from_curl, headers
         headers, meta, replace, replace, replace, to_dict
         url, __init__, __repr__

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

class MyRedirectMiddleware(RedirectMiddleware):  [scrapy/tests/test_downloadermiddleware_redirect.py:440]
methods: —

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

file scrapy/utils/response.py
imports: __future__, os, re, tempfile, webbrowser, typing, weakref, twisted
defines: get_base_url, get_meta_refresh, response_status_message, _remove_html_comments, open_in_browser

    def _handle_statuses(self, allow_redirects: bool) -> None:
        self.handle_httpstatus_list = None
        if allow_redirects:
            self.handle_httpstatus_list = SequenceExclude(range(300, 400))

class BaseRedirectMiddleware:  [scrapy/downloadermiddlewares/redirect.py:30]
methods: _build_redirect_request, _engine_started, _redirect
         _redirect_request_using_get, from_crawler
         handle_referer, __init__

    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

    def __init__(self, settings: BaseSettings):
        self.handle_httpstatus_all: bool = settings.getbool("HTTPERROR_ALLOW_ALL")
        self.handle_httpstatus_list: list[int] = settings.getlist(
            "HTTPERROR_ALLOWED_CODES"
        )

def _has_ajaxcrawlable_meta(text: str) -> bool:
    """
    >>> _has_ajaxcrawlable_meta('<html><head><meta name="fragment"  content="!"/></head><body></body></html>')
    True
    >>> _has_ajaxcrawlable_meta("<html><head><meta name='fragment' content='!'></head></html>")
    True
    >>> _has_ajaxcrawlable_meta('<html><head><!--<meta name="fragment"  content="!"/>--></head><body></body></html>')
    False
    >>> _has_ajaxcrawlable_meta('<html></html>')
    False
    """

    # Stripping scripts and comments is slow (about 20x slower than
    # just checking if a string is in text); this is a quick fail-fast
    # path that should work for most pages.
    if "fragment" not in text:
        return False
    if "content" not in text:
        return False

    text = html.remove_tags_with_content(text, ("script", "noscript"))
    text = html.replace_entities(text)
    text = html.remove_comments(text)
    return _ajax_crawlable_re.search(text) is not None

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

file scrapy/utils/conf.py
imports: __future__, numbers, os, sys, configparser, operator, pathlib, typing
defines: build_component_list, _check_components, _map_keys, _validate_values, arglist_to_dict, closest_scrapy_cfg, init_env, get_config, get_sources, feed_complete_default_values_from_settings, feed_process_params_from_cli, check_valid_format

class Scraper:  [scrapy/core/scraper.py:103]
methods: _check_deprecated_itemproc_method, _check_if_closing
         _process_spidermw_output
         _process_spidermw_output_async, _scrape
         _scrape_next, _wait_for_processing, call_spider
         call_spider_async, close_spider
         close_spider_async, enqueue_scrape
         handle_spider_error, handle_spider_output
         handle_spider_output_async, is_idle, open_spider
         open_spider_async, start_itemproc
         start_itemproc_async, __init__

    async def _scrape(self, result: Response | Failure, request: Request) -> None:
        """Handle the downloaded response or failure through the spider callback/errback."""
        if not isinstance(result, (Response, Failure)):
            raise TypeError(
                f"Incorrect type: expected Response or Failure, got {type(result)}: {result!r}"
            )

        output: Iterable[Any] | AsyncIterator[Any]
        if isinstance(result, Response):
            try:
                # call the spider middlewares and the request callback with the response
                output = await self.spidermw.scrape_response_async(
                    self.call_spider_async, result, request
                )
            except Exception:
                self.handle_spider_error(Failure(), request, result)
            else:
                await self.handle_spider_output_async(output, request, result)
            return

        try:
            # call the request errback with the downloader error
            output = await self.call_spider_async(result, request)
        except Exception as spider_exc:
            # the errback didn't silence the exception
            assert self.crawler.spider
            if not result.check(IgnoreRequest):
                logkws = self.logformatter.download_error(
                    result, request, self.crawler.spider
                )
                logger.log(
                    *logformatter_adapter(logkws),
                    extra={"spider": self.crawler.spider},
                    exc_info=failure_to_exc_info(result),
                )
            if spider_exc is not result.value:
                # the errback raised a different exception, handle it
                self.handle_spider_error(Failure(), request, result)
        else:
            await self.handle_spider_output_async(output, request, result)

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

    def _map_keys(compdict: Mapping[Any, Any]) -> BaseSettings | dict[Any, Any]:
        if isinstance(compdict, BaseSettings):
            compbs = BaseSettings()
            for k, v in compdict.items():
                prio = compdict.getpriority(k)
                assert prio is not None
                if compbs.getpriority(convert(k)) == prio:
                    raise ValueError(
                        f"Some paths in {list(compdict.keys())!r} "
                        "convert to the same "
                        "object, please update your settings"
                    )
                compbs.set(convert(k), v, priority=prio)
            return compbs
        _check_components(compdict)
        return {convert(k): v for k, v in compdict.items()}

    def meta(self) -> dict[str, Any]:
        if self._meta is None:
            self._meta = {}
        return self._meta

class TestJsonRequest(TestRequest):  [scrapy/tests/test_http_request_json.py:12]
methods: test_body_data, test_body_data_none, test_body_none_data
         test_data, test_data_method, test_dumps_kwargs
         test_dumps_sort_keys, test_empty_body_data
         test_replace_data, test_replace_dumps_kwargs
         test_replace_sort_keys
         test_replacement_both_body_and_data_warns

def get_meta_refresh(
    response: TextResponse,
    ignore_tags: Iterable[str] = ("script", "noscript"),
) -> tuple[None, None] | tuple[float, str]:
    """Parse the http-equiv refresh parameter from the given response"""
    if response not in _metaref_cache:
        text = response.text[0:4096]
        _metaref_cache[response] = html.get_meta_refresh(
            text, get_base_url(response), response.encoding, ignore_tags=ignore_tags
        )
    return _metaref_cache[response]

    def keys(self) -> KeysView[str]:
        return self._values.keys()

def handle_error(failure):
    pass

# --- Layer 04: Variable context ---
# call-chain context
  called by: _test_cookie_redirect [test_downloadermiddleware_cookies.py]
  called by: _test_cookie_header_redirect [test_downloadermiddleware_cookies.py]

# call-chain context
  called by: _check_media_to_download [media.py]
  called by: _assert_request_no3xx [test_pipeline_media.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: __init__ [media.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: run [genspider.py]
  called by: _generate_template_variables [genspider.py]

# call-chain context
  called by: _has_ajax_crawlable_variant [ajaxcrawl.py]

# call-chain context
  called by: _run_command [cmdline.py]
  called by: start [crawler.py]

# call-chain context
  called by: _wait_for_processing [scraper.py]

# call-chain context
  called by: _scrape [scraper.py]
  called by: handle_spider_output [scraper.py]

# call-chain context
  called by: build_component_list [conf.py]

# call-chain context
  called by: process_response [redirect.py]

# call-chain context
  called by: get_header_size [stats.py]
  called by: _configure [exporters.py]

```
