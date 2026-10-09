# scrapy-4 :: tacm

query: Fix contract errback

## selected nodes

- rank=1 layer=FILE tokens=150 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=2 layer=FILE tokens=45 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=3 layer=CLASS tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::_AsyncCooperatorAdapter file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=4 layer=CLASS tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::Contract file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=5 layer=CLASS tokens=36 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_defer.py::TestAiterErrback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_defer.py
- rank=6 layer=CLASS tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_defer.py::TestIterErrback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_utils_defer.py
- rank=7 layer=CLASS tokens=461 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawl.py::TestCrawlSpider file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_crawl.py
- rank=8 layer=CLASS tokens=92 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::TestContractsManager file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=9 layer=CLASS tokens=22 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py::ScrapesContract file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py
- rank=10 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py::ReturnsContract file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py
- rank=11 layer=CLASS tokens=28 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py::CallbackKeywordArgumentsContract file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py
- rank=12 layer=CLASS tokens=24 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py::MetadataContract file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/default.py
- rank=13 layer=FUNCTION tokens=139 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::aiter_errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=14 layer=FUNCTION tokens=114 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::iter_errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=15 layer=FUNCTION tokens=37 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=16 layer=FUNCTION tokens=23 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::Contract.adjust_request_args file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=17 layer=FUNCTION tokens=330 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::ContractsManager.from_method file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=18 layer=FUNCTION tokens=32 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::ProcessSpiderInputSpiderWithErrback.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=19 layer=FUNCTION tokens=77 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::_AsyncCooperatorAdapter._call_anext file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=20 layer=FUNCTION tokens=96 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::_AsyncCooperatorAdapter._errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=21 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::CrawlSpiderWithErrback.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=22 layer=FUNCTION tokens=63 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::Contract.__init__ file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=23 layer=FUNCTION tokens=41 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::DemoSpider.invalid_regex_with_valid_contract file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=24 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::BytesReceivedCallbackSpider.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=25 layer=FUNCTION tokens=17 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=26 layer=FUNCTION tokens=251 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py::BaseSettings.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/settings/__init__.py
- rank=27 layer=FUNCTION tokens=16 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::DelaySpider.errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=28 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaPipeline._errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=29 layer=FUNCTION tokens=27 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py::TestMediaFailedFailure._errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_pipeline_media.py
- rank=30 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomContractSuccessSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=31 layer=FUNCTION tokens=21 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py::CustomContractFailSpider.parse file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_contracts.py
- rank=32 layer=FUNCTION tokens=143 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py::Command.run file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/commands/check.py
- rank=33 layer=FUNCTION tokens=120 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_check.py::TestCheckCommand._test_contract file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_command_check.py
- rank=34 layer=FUNCTION tokens=247 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py::_request_deferred file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py
- rank=35 layer=FUNCTION tokens=60 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._handle_failure file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=36 layer=FUNCTION tokens=176 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::defer_fail file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py
- rank=37 layer=FUNCTION tokens=50 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py::Headers.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/http/headers.py
- rank=38 layer=FUNCTION tokens=33 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py::CaselessDict.get file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/datatypes.py
- rank=39 layer=FUNCTION tokens=87 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SlowSpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=40 layer=FUNCTION tokens=35 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py::ProcessSpiderInputSpiderWithErrback.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/test_spidermiddleware_output_chain.py
- rank=41 layer=FUNCTION tokens=221 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py::Contract.wrapper file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/contracts/__init__.py
- rank=42 layer=FUNCTION tokens=40 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::HeadersReceivedCallbackSpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=43 layer=FUNCTION tokens=42 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py::TunnelingTCP4ClientEndpoint.connectFailed file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/core/downloader/handlers/http11.py
- rank=44 layer=FUNCTION tokens=68 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py::CrawlSpider._errback file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/spiders/crawl.py
- rank=45 layer=FUNCTION tokens=38 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py::_restore_callbacks file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/shell.py
- rank=46 layer=FUNCTION tokens=104 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py::MediaPipeline._process_request file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/pipelines/media.py
- rank=47 layer=FUNCTION tokens=44 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::SingleRequestSpider.on_error file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=48 layer=FUNCTION tokens=48 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::DelaySpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=49 layer=FUNCTION tokens=55 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py::BytesReceivedCallbackSpider.start file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/tests/spiders.py
- rank=50 layer=FUNCTION tokens=11 node=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py::coro file=/Users/xxvirusxx/PY/CodegraphTACM/scrapy/scrapy/utils/defer.py

## context

```text
file scrapy/utils/defer.py
imports: __future__, asyncio, inspect, warnings, collections, functools, typing, twisted
defines: _AsyncCooperatorAdapter, defer_fail, defer_succeed, _defer_sleep_async, defer_result, mustbe_deferred, mustbe_deferred, mustbe_deferred, parallel, parallel_async, process_chain, process_parallel, eb, iter_errback, aiter_errback, deferred_from_coro, deferred_from_coro, deferred_from_coro, deferred_f_from_coro_f, f, maybeDeferred_coro, _maybeDeferred_coro, deferred_to_future, maybe_deferred_to_future, _schedule_coro, ensure_awaitable, ensure_awaitable, ensure_awaitable, coro

file scrapy/contracts/__init__.py
imports: __future__, re, sys, collections, functools, inspect, types, typing
defines: Contract, ContractsManager, ContractTestCase, _create_testcase

class _AsyncCooperatorAdapter(Iterator, Generic[_T]):  [scrapy/utils/defer.py:176]
methods: _call_anext, _callback, _errback, __init__, __next__

class Contract:  [scrapy/contracts/__init__.py:24]
methods: add_post_hook, add_pre_hook, adjust_request_args, wrapper
         wrapper, __init__

class TestAiterErrback:  [scrapy/tests/test_utils_defer.py:92]
methods: iterbad, itergood, test_aiter_errback_good
         test_iter_errback_bad

class TestIterErrback:  [scrapy/tests/test_utils_defer.py:68]
methods: iterbad, itergood, test_iter_errback_bad
         test_iter_errback_good

class TestCrawlSpider:  [scrapy/tests/test_crawl.py:438]
methods: _on_item_scraped, _on_item_scraped, _run_spider, cb, cb
         cb, eb, eb, eb, eb, eb, eb, eb, eb, eb, eb
         setup_class, teardown_class
         test_async_def_asyncgen_parse
         test_async_def_asyncgen_parse_complex
         test_async_def_asyncgen_parse_exc
         test_async_def_asyncgen_parse_loop
         test_async_def_asyncio_parse
         test_async_def_asyncio_parse_items_list
         test_async_def_asyncio_parse_items_single_element
         test_async_def_asyncio_parse_reqs_list
         test_async_def_deferred_direct
         test_async_def_deferred_maybe_wrapped
         test_async_def_deferred_wrapped
         test_async_def_parse
         test_bytes_received_stop_download_callback
         test_bytes_received_stop_download_errback
         test_crawlspider_process_request_cb_kwargs
         test_crawlspider_with_async_callback
         test_crawlspider_with_async_generator_callback
         test_crawlspider_with_errback
         test_crawlspider_with_parse
         test_headers_received_stop_download_callback
         test_headers_received_stop_download_errback
         test_raise_closespider
         test_raise_closespider_reason
         test_response_ip_address
         test_response_ssl_certificate
         test_response_ssl_certificate_none
         test_spider_callback_deferred_deprecated
         test_spider_errback
         test_spider_errback_deferred_deprecated
         test_spider_errback_downloader_error
         test_spider_errback_downloader_error_exception
         test_spider_errback_downloader_error_item
         test_spider_errback_downloader_error_request
         test_spider_errback_exception
         test_spider_errback_item
         test_spider_errback_request
         test_spider_errback_silence

class TestContractsManager:  [scrapy/tests/test_contracts.py:249]
methods: setup_method, should_error, should_fail, should_succeed
         test_cb_kwargs, test_contracts
         test_custom_contracts, test_errback
         test_form_contract, test_inherited_contracts
         test_meta, test_regex, test_returns
         test_returns_async, test_same_url, test_scrapes

class ScrapesContract(Contract):  [scrapy/contracts/default.py:117]
methods: post_process

class ReturnsContract(Contract):  [scrapy/contracts/default.py:57]
methods: post_process, __init__

class CallbackKeywordArgumentsContract(Contract):  [scrapy/contracts/default.py:29]
methods: adjust_request_args

class MetadataContract(Contract):  [scrapy/contracts/default.py:43]
methods: adjust_request_args

async def aiter_errback(
    aiterable: AsyncIterator[_T],
    errback: Callable[Concatenate[Failure, _P], Any],
    *a: _P.args,
    **kw: _P.kwargs,
) -> AsyncIterator[_T]:
    """Wrap an async iterable calling an errback if an error is caught while
    iterating it. Similar to :func:`scrapy.utils.defer.iter_errback`.
    """
    it = aiterable.__aiter__()
    while True:
        try:
            yield await it.__anext__()
        except StopAsyncIteration:
            break
        except Exception:
            errback(failure.Failure(), *a, **kw)

def iter_errback(
    iterable: Iterable[_T],
    errback: Callable[Concatenate[Failure, _P], Any],
    *a: _P.args,
    **kw: _P.kwargs,
) -> Iterable[_T]:
    """Wrap an iterable calling an errback if an error is caught while
    iterating it.
    """
    it = iter(iterable)
    while True:
        try:
            yield next(it)
        except StopIteration:
            break
        except Exception:
            errback(failure.Failure(), *a, **kw)

    def __init__(self, contracts: Iterable[type[Contract]]):
        for contract in contracts:
            self.contracts[contract.name] = contract

    def adjust_request_args(self, args: dict[str, Any]) -> dict[str, Any]:
        return args

    def from_method(self, method: Callable, results: TestResult) -> Request | None:
        contracts = self.extract_contracts(method)
        if contracts:
            request_cls = Request
            for contract in contracts:
                if contract.request_cls is not None:
                    request_cls = contract.request_cls

            # calculate request args
            args, kwargs = get_spec(request_cls.__init__)

            # Don't filter requests to allow
            # testing different callbacks on the same URL.
            kwargs["dont_filter"] = True
            kwargs["callback"] = method

            for contract in contracts:
                kwargs = contract.adjust_request_args(kwargs)

            args.remove("self")

            # check if all positional arguments are defined in kwargs
            if set(args).issubset(set(kwargs)):
                request = request_cls(**kwargs)

                # execute pre and post hooks in order
                for contract in reversed(contracts):
                    request = contract.add_pre_hook(request, results)
                for contract in contracts:
                    request = contract.add_post_hook(request, results)

                self._clean_req(request, method, results)
                return request
        return None

    def errback(self, failure):
        self.logger.info("Got a Failure on the Request errback")
        return {"from": "errback"}

    def _call_anext(self) -> None:
        # This starts waiting for the next result from aiterator.
        # If aiterator is exhausted, _errback will be called.
        self.anext_deferred = deferred_from_coro(self.aiterator.__anext__())
        self.anext_deferred.addCallbacks(self._callback, self._errback)

    def _errback(self, failure: Failure) -> None:
        # This gets called on any exceptions in aiterator.__anext__().
        # It handles StopAsyncIteration by stopping the iteration and reraises all others.
        self.anext_deferred = None
        failure.trap(StopAsyncIteration)
        self.finished = True
        for d in self.waiting_deferreds:
            d.callback(None)

    def errback(self, failure):
        self.logger.info("[errback] status %i", failure.value.response.status)

    def __init__(self, method: Callable, *args: Any):
        self.testcase_pre = _create_testcase(method, f"@{self.name} pre-hook")
        self.testcase_post = _create_testcase(method, f"@{self.name} post-hook")
        self.args: tuple[Any, ...] = args

    def invalid_regex_with_valid_contract(self, response):
        """method with invalid regex
        @ scrapy is awsome
        @url http://scrapy.org
        """

    def errback(self, failure):
        self.meta["failure"] = failure

    def errback(self, failure):
        self.meta["failure"] = failure

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

    def errback(self, failure):
        self.t2_err = time.time()

    def _errback(self, result):
        self.pipe._mockcalled.append("request_errback")
        return result

    def _errback(self, result):
        self.pipe._mockcalled.append("request_errback")
        return result

    def parse(self, response):
        """
        @custom_success_contract
        """

    def parse(self, response):
        """
        @custom_fail_contract
        """

    def run(self, args: list[str], opts: argparse.Namespace) -> None:
        # load contracts
        assert self.settings is not None
        contracts = build_component_list(self.settings.getwithbase("SPIDER_CONTRACTS"))
        conman = ContractsManager(load_object(c) for c in contracts)
        runner = TextTestRunner(verbosity=2 if opts.verbose else 1)
        result = TextTestResult(runner.stream, runner.descriptions, runner.verbosity)

        # contract requests
        contract_reqs = defaultdict(list)

        assert self.crawler_process
    # ... truncated

    def _test_contract(
        self,
        proj_path: Path,
        contracts: str = "",
        parse_def: str = "pass",
        use_reactor: bool = True,
    ) -> None:
        self._write_contract(proj_path, contracts, parse_def)
        args = ["check"]
        if not use_reactor:
            args += ["-s", "TWISTED_REACTOR_ENABLED=False"]
        ret, out, err = proc(*args, cwd=proj_path)
        assert "F" not in out
        assert "OK" in err
        assert ret == 0

def _request_deferred(request: Request) -> Deferred[Any]:
    """Wrap a request inside a Deferred.

    This function is harmful, do not use it until you know what you are doing.

    This returns a Deferred whose first pair of callbacks are the request
    callback and errback. The Deferred also triggers when the request
    callback/errback is executed (i.e. when the request is downloaded)

    WARNING: Do not call request.replace() until after the deferred is called.
    """
    request_callback = request.callback
    request_errback = request.errback

    def _restore_callbacks(result: Any) -> Any:
        request.callback = request_callback
        request.errback = request_errback
        return result

    d: Deferred[Any] = Deferred()
    d.addBoth(_restore_callbacks)
    if request.callback:
        d.addCallback(request.callback)
    if request.errback:
        d.addErrback(request.errback)

    request.callback, request.errback = d.callback, d.errback
    return d

    def _handle_failure(
        self, failure: Failure, errback: Callable[[Failure], Any] | None
    ) -> Iterable[Any]:
        if errback:
            results = errback(failure) or ()
            yield from iterate_spider_output(results)

def defer_fail(_failure: Failure) -> Deferred[Any]:  # pragma: no cover
    """Same as twisted.internet.defer.fail but delay calling errback until
    next reactor loop

    It delays by 100ms so reactor has a chance to go through readers and writers
    before attending pending delayed calls, so do not set delay to zero.
    """
    warnings.warn(
        "scrapy.utils.defer.defer_fail() is deprecated, use"
        " twisted.internet.defer.fail(), plus an explicit sleep if needed.",
        category=ScrapyDeprecationWarning,
        stacklevel=2,
    )

    from twisted.internet import reactor

    d: Deferred[Any] = Deferred()
    reactor.callLater(_DEFER_DELAY, d.errback, _failure)
    return d

    def get(self, key: AnyStr, def_val: Any = None) -> bytes | None:
        try:
            return cast("list[bytes]", super().get(key, def_val))[-1]
        except IndexError:
            return None

    def get(self, key: AnyStr, def_val: Any = None) -> Any:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

    async def start(self):
        # 1st response is fast
        url = self.mockserver.url("/delay?n=0&b=0")
        yield Request(url, callback=self.parse, errback=self.errback)

        # 2nd response is slow
        url = self.mockserver.url(f"/delay?n={self.n}&b={self.b}")
        yield Request(url, callback=self.parse, errback=self.errback)

    async def start(self):
        yield Request(
            self.mockserver.url("/status?n=200"), self.parse, errback=self.errback
        )

            def wrapper(response: Response, **cb_kwargs: Any) -> list[Any]:
                cb_result = cb(response, **cb_kwargs)
                if isinstance(cb_result, (AsyncGenerator, CoroutineType)):
                    raise TypeError("Contracts don't support async callbacks")
                output = list(cast("Iterable[Any]", iterate_spider_output(cb_result)))
                try:
                    results.startTest(self.testcase_post)
                    self.post_process(output)
                    results.stopTest(self.testcase_post)
                except AssertionError:
                    results.addFailure(self.testcase_post, sys.exc_info())
                except Exception:
                    results.addError(self.testcase_post, sys.exc_info())
                else:
                    results.addSuccess(self.testcase_post)
                return output

    async def start(self):
        yield Request(
            self.mockserver.url("/status", is_secure=self.is_secure),
            errback=self.errback,
        )

    def connectFailed(self, reason: Failure) -> None:
        """Propagates the errback to the appropriate deferred."""
        self._tunnelReadyDeferred.errback(reason)

    def _errback(self, failure: Failure) -> Iterable[Any]:
        rule = self._rules[cast("int", failure.request.meta["rule"])]  # type: ignore[attr-defined]
        return self._handle_failure(
            failure, cast("Callable[[Failure], Any]", rule.errback)
        )

    def _restore_callbacks(result: Any) -> Any:
        request.callback = request_callback
        request.errback = request_errback
        return result

    async def _process_request(
        self, request: Request, info: SpiderInfo, item: Any
    ) -> FileInfo:
        fp = self._fingerprinter.fingerprint(request)

        eb = request.errback
        request.callback = NO_CALLBACK
        request.errback = None

        # Return cached result if request was already seen
        if fp in info.downloaded:
            await _defer_sleep_async()
    # ... truncated

    def on_error(self, failure):
        self.meta["failure"] = failure
        if callable(self.errback_func):
            return self.errback_func(failure)
        return None

    async def start(self):
        self.t1 = time.time()
        url = self.mockserver.url(f"/delay?n={self.n}&b={self.b}")
        yield Request(url, callback=self.parse, errback=self.errback)

    async def start(self):
        body = b"a" * self.full_response_length
        url = self.mockserver.url("/alpayload", is_secure=self.is_secure)
        yield Request(url, method="POST", body=body, errback=self.errback)

    async def coro() -> _T:
        return o
```
