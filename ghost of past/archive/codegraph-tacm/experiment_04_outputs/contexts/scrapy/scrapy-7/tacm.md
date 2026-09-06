# scrapy-7 :: tacm

query: FormRequest: handle whitespaces in action attribute properly

## selected nodes

- rank=1 layer=FILE tokens=76 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=2 layer=FILE tokens=53 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=3 layer=FILE tokens=66 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/asyncio.py
- rank=4 layer=CLASS tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::FormRequest file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=5 layer=CLASS tokens=19 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py::DataAction file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/curl.py
- rank=6 layer=CLASS tokens=122 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::TestCrawl file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py
- rank=7 layer=CLASS tokens=130 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=8 layer=CLASS tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=9 layer=CLASS tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline_crawl_with_pipeline/__init__.py::TestCmdlineCrawlPipeline file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_cmdline_crawl_with_pipeline/__init__.py
- rank=10 layer=CLASS tokens=31 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::CatchExceptionOverrideRequestMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py
- rank=11 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::CatchExceptionDoNotOverrideRequestMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py
- rank=12 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::ProcessResponseMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py
- rank=13 layer=CLASS tokens=29 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::RaiseExceptionRequestMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py
- rank=14 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::AlternativeCallbacksSpider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py
- rank=15 layer=CLASS tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py::AlternativeCallbacksMiddleware file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_attribute_binding.py
- rank=16 layer=CLASS tokens=30 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport.py::FailingBlockingFeedStorage file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_feedexport.py
- rank=17 layer=CLASS tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::S3FeedStorage file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py
- rank=18 layer=CLASS tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py::BlockingFeedStorage file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/extensions/feedexport.py
- rank=19 layer=FUNCTION tokens=83 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::_get_form_url file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=20 layer=FUNCTION tokens=89 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::attribute file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=21 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py::warn_on_deprecated_spider_attribute file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/deprecate.py
- rank=22 layer=FUNCTION tokens=164 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_output file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=23 layer=FUNCTION tokens=378 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_output_async file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=24 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=25 layer=FUNCTION tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/fetch.py
- rank=26 layer=FUNCTION tokens=127 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py::RedirectMiddleware.process_response file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/downloadermiddlewares/redirect.py
- rank=27 layer=FUNCTION tokens=470 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper._scrape file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=28 layer=FUNCTION tokens=193 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py::HttpErrorMiddleware.process_spider_input file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spidermiddlewares/httperror.py
- rank=29 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py::Command.add_options file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/shell.py
- rank=30 layer=FUNCTION tokens=25 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py::SignalManager.handle file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/signalmanager.py
- rank=31 layer=FUNCTION tokens=218 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipelineAllowRedirectSettings._assert_request_no3xx file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=32 layer=FUNCTION tokens=192 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py::FormRequest.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/request/form.py
- rank=33 layer=FUNCTION tokens=319 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py::Scraper.handle_spider_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/scraper.py
- rank=34 layer=FUNCTION tokens=52 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._handle_statuses file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=35 layer=FUNCTION tokens=12 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py::MethodsSpider.handle_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_request_dict.py
- rank=36 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py

## context

```text
file scrapy/utils/deprecate.py
imports: __future__, inspect, warnings, typing, scrapy, collections
defines: DeprecatedClass, attribute, create_deprecated_class, _clspath, update_classpath, update_classpath, update_classpath, method_is_overridden, argument_is_required, warn_on_deprecated_spider_attribute

file http/request/form.py
imports: __future__, collections, typing, urllib, parsel, w3lib, scrapy, lxml
defines: FormRequest, _get_form_url, _urlencode, _get_form, _get_inputs, _value, _select_value, _get_clickable

file scrapy/utils/asyncio.py
imports: __future__, asyncio, logging, time, collections, typing, twisted, scrapy
defines: AsyncioLoopingCall, CallLaterResult, is_asyncio_available, _parallel_asyncio, worker, fill_queue, create_looping_call, call_later, run_in_thread

class FormRequest(Request):  [http/request/form.py:39]
methods: from_response, __init__

class DataAction(argparse.Action):  [scrapy/utils/curl.py:16]
methods: __call__

class TestCrawl:  [scrapy/tests/test_request_attribute_binding.py:65]
methods: setup_class, signal_handler, teardown_class
         test_downloader_middleware_alternative_callback
         test_downloader_middleware_do_not_override_in_process_exception
         test_downloader_middleware_override_in_process_exception
         test_downloader_middleware_override_request_in_process_response
         test_downloader_middleware_raise_exception
         test_response_200, test_response_error

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

class BaseSettings(MutableMapping[_SettingsKey, Any]):  [scrapy/settings/__init__.py:83]
methods: _assert_mutability, _get_key, _repr_pretty_, _to_dict
         add_to_list, copy, copy_to_dict, delete, freeze
         frozencopy, get, getbool, getdict, getdictorlist
         getfloat, getint, getlist, getpriority
         getwithbase, maxpriority, normalize_key, pop
         remove_from_list
         replace_in_component_priority_dict, restore_key
         set, set_in_component_priority_dict, setdefault
         setdefault_in_component_priority_dict, setdict
         setmodule, track_loaded_key, update, __contains__
         __delitem__, __getitem__, __init__, __iter__
         __len__, __setitem__

class TestCmdlineCrawlPipeline:  [tests/test_cmdline_crawl_with_pipeline/__init__.py:6]
methods: _execute, test_exception_at_open_spider_in_pipeline
         test_open_spider_normally_in_pipeline

class CatchExceptionOverrideRequestMiddleware:  [scrapy/tests/test_request_attribute_binding.py:24]
methods: process_exception

class CatchExceptionDoNotOverrideRequestMiddleware:  [scrapy/tests/test_request_attribute_binding.py:33]
methods: process_exception

class ProcessResponseMiddleware:  [scrapy/tests/test_request_attribute_binding.py:13]
methods: process_response

class RaiseExceptionRequestMiddleware:  [scrapy/tests/test_request_attribute_binding.py:18]
methods: process_request

class AlternativeCallbacksSpider(SingleRequestSpider):  [scrapy/tests/test_request_attribute_binding.py:41]
methods: alt_callback

class AlternativeCallbacksMiddleware:  [scrapy/tests/test_request_attribute_binding.py:48]
methods: from_crawler, process_response, __init__

class FailingBlockingFeedStorage(DummyBlockingFeedStorage):  [scrapy/tests/test_feedexport.py:89]
methods: _store_in_thread

class S3FeedStorage(BlockingFeedStorage):  [scrapy/extensions/feedexport.py:187]
methods: _store_in_thread, from_crawler, __init__

class BlockingFeedStorage(ABC):  [scrapy/extensions/feedexport.py:124]
methods: _store_in_thread, open, store

def _get_form_url(form: FormElement, url: str | None) -> str:
    assert form.base_url is not None  # typing
    if url is None:
        action = form.get("action")
        if action is None:
            return form.base_url
        return urljoin(form.base_url, strip_html5_whitespace(action))
    return urljoin(form.base_url, url)

def attribute(obj: Any, oldattr: str, newattr: str, version: str = "0.12") -> None:
    cname = obj.__class__.__name__
    warnings.warn(
        f"{cname}.{oldattr} attribute is deprecated and will be no longer supported "
        f"in Scrapy {version}, use {cname}.{newattr} attribute instead",
        ScrapyDeprecationWarning,
        stacklevel=3,
    )

def warn_on_deprecated_spider_attribute(attribute_name: str, setting_name: str) -> None:
    warnings.warn(
        f"The '{attribute_name}' spider attribute is deprecated. "
        "Use Spider.custom_settings or Spider.update_settings() instead. "
        f"The corresponding setting name is '{setting_name}'.",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )

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

        def handle() -> None:
            self.disconnect(handle, signal)
            d.callback(None)

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

    def __init__(
        self, *args: Any, formdata: FormdataType = None, **kwargs: Any
    ) -> None:
        if formdata and kwargs.get("method") is None:
            kwargs["method"] = "POST"

        super().__init__(*args, **kwargs)

        if formdata:
            items = formdata.items() if isinstance(formdata, dict) else formdata
            form_query_str = _urlencode(items, self.encoding)
            if self.method == "POST":
                self.headers.setdefault(
                    b"Content-Type", b"application/x-www-form-urlencoded"
                )
                self._set_body(form_query_str)
            else:
                self._set_url(
                    urlunsplit(urlsplit(self.url)._replace(query=form_query_str))
                )

    def handle_spider_error(
        self,
        _failure: Failure,
        request: Request,
        response: Response | Failure,
        spider: Spider | None = None,
    ) -> None:
        """Handle an exception raised by a spider callback or errback."""
        assert self.crawler.spider
        exc = _failure.value
        if isinstance(exc, CloseSpider):
            assert self.crawler.engine is not None  # typing
            _schedule_coro(
                self.crawler.engine.close_spider_async(reason=exc.reason or "cancelled")
            )
            return
        logkws = self.logformatter.spider_error(
            _failure, request, response, self.crawler.spider
        )
        logger.log(
            *logformatter_adapter(logkws),
            exc_info=failure_to_exc_info(_failure),
            extra={"spider": self.crawler.spider},
        )
        self.signals.send_catch_log(
            signal=signals.spider_error,
            failure=_failure,
            response=response,
            spider=self.crawler.spider,
        )
        assert self.crawler.stats
        self.crawler.stats.inc_value("spider_exceptions/count")
        self.crawler.stats.inc_value(
            f"spider_exceptions/{_failure.value.__class__.__name__}"
        )

    def _handle_statuses(self, allow_redirects: bool) -> None:
        self.handle_httpstatus_list = None
        if allow_redirects:
            self.handle_httpstatus_list = SequenceExclude(range(300, 400))

    def handle_error(self, failure):
        pass

    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))
```
